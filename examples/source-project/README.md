# Source Project Example: Enterprise Security Management Center

These files are the **original, production-tested** `.cursor/rules/` from a real enterprise project (6 domains, 50+ modules, Java + Vue 3).

They demonstrate how the generalized meta-rules in `stable/atoms/rules/enterprise/` were actually used in practice — with project-specific business logic, Chinese-language domain terms, and concrete routing tables tied to real modules.

## Mapping: Source → Generalized

| Source Rule (this directory) | Generalized Atom | What changed during generalization |
|:---|:---|:---|
| `design-is-authority.mdc` | `stable/atoms/rules/enterprise/design-authority.mdc` | Removed project-specific file paths; translated to English; kept core constraints |
| `workflow-router.mdc` | `stable/atoms/rules/enterprise/routing-engine.mdc` | Removed 60+ project-specific route entries; kept the routing framework and classification logic |
| `ontology-workflow.mdc` | `stable/atoms/rules/enterprise/ontology-driven-dev.mdc` | Removed references to specific sub-domains (asset, identity, policy); kept the ODD pipeline |
| `rule-optimization-guide.mdc` | `stable/atoms/rules/enterprise/rule-evolution.mdc` | Translated the 7-section record structure; kept the closed-loop methodology |

## Key Observations

1. The source `workflow-router.mdc` has **60+ routing entries** across 4 modes (Development, Acceptance, User, Meta). The generalized version keeps the framework but lets each project define its own routes.

2. The source rules are in **Chinese** — demonstrating that the meta-rule methodology is language-agnostic and can be adapted for any locale.

3. The source project also generated **6 domain-specific sub-rules** (`modules/asset.mdc`, `modules/identity.mdc`, etc.) from these meta-rules — proving the "rules that generate rules" claim.
