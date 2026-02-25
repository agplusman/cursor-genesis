# Topic Research Team Pattern

> **Status**: Active
> **Description**: A specialized team for conducting academic and technical topic research, starting from topic decomposition to deep analysis.

## Team Composition

| Role ID | Role Name | File Path | Responsibility |
| :--- | :--- | :--- | :--- |
| **R1** | **Topic Guide (Navigator)** | `prompts-library/templates/capabilities/01_insight/topic-guide.md` | Deconstructs the topic, defines the research essence, and sets the North Star. |
| **R2** | **Research Architect** | `prompts-library/templates/capabilities/02_architecture/research-architect.md` | Designs the standard Research Framework, defines Boundaries, and pre-sets Innovation/Barriers. |
| **R3** | **Literature Hunter** | `prompts-library/templates/capabilities/01_insight/literature-hunter.md` | Generates precise search strategies, defines filters, and creates gap analysis templates. |
| **R4** | **Experiment Designer** | `prompts-library/templates/capabilities/04_quality/experiment-designer.md` | Designs scientific validation protocols, including variable control, grouping strategy, and metrics. |
| **R5** | **Research Executor** | `prompts-library/templates/capabilities/03_engineering/research-executor.md` | Plans the execution flow (Dev -> Run -> Analyze), manages artifacts, and ensures delivery/feedback loops. |

## 🔄 Interaction Workflow

1.  **Initialization**: User provides a Topic Name (e.g., "CoT in AIOps").
2.  **Phase 1 - Navigation (R1)**:
    *   **Trigger**: New topic received.
    *   **Action**: R1 analyzes the topic and outputs the "Research Navigation Guide".
    *   **Goal**: Establish the "North Star" for the research.
3.  **Phase 2 - Architecture (R2)**:
    *   **Input**: R1's Navigation Guide + Topic Name.
    *   **Action**: R2 designs the Research Framework and Innovation Strategy.
    *   **Goal**: Create a roadmap (Tasks, Outputs) and define the "Winning Edge" (Innovation/Barriers).
4.  **Phase 3 - Literature Strategy (R3)**:
    *   **Input**: R2's Framework (Innovation Points).
    *   **Action**: R3 generates the Search Strategy and Gap Analysis Template.
    *   **Goal**: Direct the user to find specific evidence that supports the pre-set innovation.
5.  **Phase 4 - Validation Design (R4)**:
    *   **Input**: R2's Framework + R3's Gaps.
    *   **Action**: R4 designs the "Experimental Group vs. Control Group" logic and metric system.
    *   **Goal**: Ensure the innovation is scientifically verifiable.
6.  **Phase 5 - Execution Planning (R5)**:
    *   **Input**: R4's Design + R2's Framework.
    *   **Action**: R5 breaks down the work into Dev/Run/Analyze tasks and defines the final deliverables.
    *   **Goal**: Turn the "Paper Design" into "Actionable Tasks" and "Tangible Artifacts".
