import os
import json
import argparse
import glob
import time
import concurrent.futures
from pathlib import Path
from typing import List, Dict, Optional

# Try importing openai, handle if not installed
try:
    from openai import OpenAI
except ImportError:
    print("Error: 'openai' package is not installed. Please run: pip install openai")
    exit(1)

try:
    import pandas as pd
except ImportError:
    print("Warning: 'pandas' is not installed. CSV export might be limited. Run: pip install pandas")
    pd = None

# ================= Configuration =================
# You can set these via environment variables or CLI args
DEFAULT_API_BASE = os.getenv("LLM_API_BASE", "https://api.deepseek.com/v1")  # Example: DeepSeek
DEFAULT_API_KEY = os.getenv("LLM_API_KEY", "sk-...")
DEFAULT_MODEL = os.getenv("LLM_MODEL", "deepseek-chat") # Use a cheap model!

# Prompt Paths (Relative to this script)
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent  # Adjusted for new location
PROMPT_LIB = PROJECT_ROOT / "standalone" / "legacy"

JAVA_PROMPT_PATH = PROMPT_LIB / "java-excavator.md"
VUE_PROMPT_PATH = PROMPT_LIB / "vue-inspector.md"

# ================= Utils =================

def load_prompt(file_path: Path) -> str:
    if not file_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def clean_json_output(content: str) -> str:
    """Removes Markdown code blocks if present."""
    content = content.strip()
    if content.startswith("```json"):
        content = content[7:]
    if content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    return content.strip()

def analyze_file(client: OpenAI, model: str, file_path: Path, prompt_template: str) -> Dict:
    """Sends a single file to the LLM for analysis."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code_content = f.read()
    except Exception as e:
        return {"file": str(file_path), "error": f"Read Error: {str(e)}"}

    system_prompt = f"""
    {prompt_template}

    IMPORTANT: You must ONLY output valid JSON. Do not include any conversational text.
    """

    user_message = f"Here is the code file content:\n\n{code_content}"

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.1, # Low temp for extraction
            response_format={"type": "json_object"} # Force JSON if supported
        )

        raw_content = response.choices[0].message.content
        clean_content = clean_json_output(raw_content)

        try:
            data = json.loads(clean_content)
            # Add file metadata
            data["_meta_filepath"] = str(file_path)
            data["_meta_filename"] = file_path.name
            return data
        except json.JSONDecodeError:
            return {"file": str(file_path), "error": "JSON Parse Error", "raw_output": raw_content}

    except Exception as e:
        return {"file": str(file_path), "error": f"API Error: {str(e)}"}

# ================= Main Execution =================

def main():
    parser = argparse.ArgumentParser(description="Legacy Code Excavator - Batch analyze Java/Vue files with LLM")
    parser.add_argument("--target", required=True, help="Directory to scan")
    parser.add_argument("--output", default="analysis_report", help="Output filename prefix")
    parser.add_argument("--workers", type=int, default=5, help="Number of concurrent threads")
    parser.add_argument("--api-key", default=DEFAULT_API_KEY, help="LLM API Key")
    parser.add_argument("--base-url", default=DEFAULT_API_BASE, help="LLM Base URL")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model name")

    args = parser.parse_args()

    # 1. Setup Client
    client = OpenAI(api_key=args.api_key, base_url=args.base_url)

    # 2. Load Prompts
    print(f"Loading prompts from {PROMPT_LIB}...")
    try:
        java_prompt = load_prompt(JAVA_PROMPT_PATH)
        vue_prompt = load_prompt(VUE_PROMPT_PATH)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # 3. Find Files
    target_path = Path(args.target)
    java_files = list(target_path.rglob("*.java"))
    vue_files = list(target_path.rglob("*.vue"))

    print(f"Found {len(java_files)} Java files and {len(vue_files)} Vue files.")

    results = []

    # 4. Process (Concurrency)
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = []

        # Submit Java Tasks
        for f in java_files:
            futures.append(executor.submit(analyze_file, client, args.model, f, java_prompt))

        # Submit Vue Tasks
        for f in vue_files:
            futures.append(executor.submit(analyze_file, client, args.model, f, vue_prompt))

        # Collect Results
        total = len(futures)
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            res = future.result()
            results.append(res)
            print(f"[{i+1}/{total}] Processed: {res.get('_meta_filename', 'Unknown')}")

    # 5. Export
    output_json = f"{args.output}.json"
    output_csv = f"{args.output}.csv"

    # Save Raw JSON
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nRaw JSON saved to {output_json}")

    # Save Flattened CSV (if pandas exists)
    if pd:
        # Flattening logic specific to our schemas
        flat_data = []
        for r in results:
            if "error" in r:
                flat_data.append({"file": r["file"], "status": "ERROR", "error_msg": r["error"]})
                continue

            # Basic Flattening
            item = {
                "file": r.get("_meta_filepath"),
                "status": "SUCCESS",
                "class_name": r.get("file_info", {}).get("class_name") or r.get("component_meta", {}).get("name"),
                "type": r.get("file_info", {}).get("parent_class") or r.get("component_meta", {}).get("page_type"),
                "is_template": r.get("domain_logic", {}).get("is_crud_template") or r.get("pattern_analysis", {}).get("is_standard_template"),
                "metrics_loc": r.get("metrics", {}).get("lines_of_code"),
                "custom_methods": str(r.get("domain_logic", {}).get("custom_methods", [])),
                "api_calls": str(r.get("external_calls") or r.get("interaction_layer", {}).get("api_calls", []))
            }
            flat_data.append(item)

        df = pd.DataFrame(flat_data)
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")
        print(f"Summary CSV saved to {output_csv}")

        # 6. Generate "Portrait" (Analysis Summary)
        template_count = df[df["is_template"] == True].shape[0]
        custom_count = df[df["is_template"] == False].shape[0]
        print(f"\n===== Portrait Summary =====")
        print(f"Total Files: {len(df)}")
        print(f"Standard Templates: {template_count}")
        print(f"Custom Logic Files: {custom_count}")
        print(f"Please check '{output_csv}' and filter by 'is_template=False' to find domain logic.")

if __name__ == "__main__":
    main()
