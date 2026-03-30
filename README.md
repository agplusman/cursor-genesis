# cursor-genesis

> **A Generative Agentic Engineering Platform for Cursor**
> 
> *"Stop writing code. Start engineering how your AI writes code."*

## What is this?

`cursor-genesis` is a distribution platform for reusable AI cognitive assets. 

When configuring AI for large-scale enterprise software (e.g., 50+ modules, tens of thousands of lines of code), default AI behavior degrades: it hallucinates architectures, relies too much on legacy patterns, and loses context. 

Instead of writing manual prompts for every single module, `cursor-genesis` uses **Meta-Rules**. When we discover a robust AI working model in a production enterprise project, we crystallize it into an "**Atom**" (e.g., a `.mdc` rule) and package it into a "**Pack**" for downstream teams to inject into their own repositories via Git sparse-checkout.

## The Crown Jewels: Enterprise Meta-Rules

Extracted from a real-world enterprise system delivery (6 domains, 50+ modules, zero to acceptance in 2 weeks), this repository contains the core meta-rules that govern how an Agent *should* behave in a massive codebase. 

Located in `stable/atoms/rules/enterprise/`:

1. **`design-authority.mdc` (Design is Authority)**
   Strictly forbids the agent from scanning legacy code to guess architecture patterns. It mandates that the Agent must read the Domain Ontology and declarative configs first, saving 60%+ in wasted, hallucinatory token reads.

2. **`routing-engine.mdc` (Intent-Based Route Engine)**
   Automatically intercepts vague natural language inputs (e.g., "the dropdown is empty") and routes them into deterministic diagnostic and file-reading pipelines. 

3. **`ontology-driven-dev.mdc` (ODD Paradigm)**
   A structured pipeline governing how the Agent should extract entity boundaries from PM specification documents, map them into a `model.yaml`, and deterministically generate code without missing fields.

4. **`rule-evolution.mdc` (Agent Self-Evolution)**
   A closed-loop system constraint. Whenever the AI detects its own behavior or cognitive path was suboptimal, it must document the failure, analyze the root cause, and rewrite its own rules to prevent future mistakes.

## Provenance & Validation Status

These meta-rules are **not theoretical**. They were extracted and generalized from a production enterprise system (an Enterprise Security Management Center: 6 business domains, 50+ modules, full-stack Java + Vue 3) that was delivered from zero to acceptance review in 2 weeks.

| Rule | Origin | Production Validation |
|:---|:---|:---|
| `design-authority` | Discovered after observing 60%+ wasted token reads from legacy code scanning | Eliminated architecture drift across 50+ modules |
| `routing-engine` | Evolved through 5 documented optimization rounds with quantified before/after metrics | Reduced diagnostic file reads from 9+ to 4-6; search operations from 5+ to 0-1 |
| `ontology-driven-dev` | Created after measuring 35% field omission rate in first ontology extraction | Brought omission rate to near-zero across 6 domains |
| `rule-evolution` | Meta-rule created to prevent recurring behavioral failures | 5 optimization records with full root-cause analysis |

The generalized versions in this repository are the first step in making these patterns available for any enterprise-scale Cursor project. Backflow from downstream adoption will continue to refine them.

## Architecture

This repository is split into two layers:

### 1. Atoms (`stable/atoms/`)
The smallest reusable units of AI cognition. Context-agnostic.
- `rules/enterprise/`: **Enterprise Meta-Rules** — the core governance system (4 rules)
- `rules/`: Additional base rules (production safety, project conventions)
- `capabilities/`: Four-layer cognition bounds (insight, architecture, engineering, quality)
- `patterns/`: Team orchestration templates (6 team patterns)

### 2. Packs (`stable/packs/`)
User-facing scenario combinations. Users don't pick atoms; they install packs.
- `v1-talk/`: A conversational orchestration pack with 6 team patterns.
- `deep-research/`: A Plan → Execute → Synthesize research workflow.
- `knowledge-manage/`: Knowledge system management pack.
- `create-toolkit/`: Project scaffolding toolkit.

### 3. Examples (`examples/`)
Real-world source rules from the production enterprise project that the Enterprise Meta-Rules were extracted from. Includes the original Chinese-language rules with 60+ routing entries, proving these atoms are battle-tested — not theoretical.

See [`examples/source-project/README.md`](examples/source-project/README.md) for the full source-to-generalized mapping.

## How to use (Downstream Injection)

You can inject these cognitive assets into any new Cursor project without downloading the entire repository, using Git sparse-checkout.

```bash
# In your new project's root directory:
git clone --filter=blob:none --sparse https://github.com/SYMlp/cursor-genesis.git .cursor-genesis
cd .cursor-genesis

# Inject only the enterprise meta-rules
git sparse-checkout set stable/atoms/rules/enterprise

# Copy the rules to your local cursor directory
cp -r stable/atoms/rules/enterprise/* ../.cursor/rules/
```

## The Vision

Cursor is not just an IDE with autocomplete. It is a substrate for building autonomous software engineering pipelines. `cursor-genesis` aims to be the standard library for those pipelines—turning individual prompt engineering into scalable, distributable enterprise workflows.

---
*Built for the future of AI-native engineering.*
