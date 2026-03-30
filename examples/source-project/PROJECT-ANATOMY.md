# Project Anatomy: Enterprise Security Management Center

> A quantitative map of the full system — showing how Meta-Rules, Ontologies, Configurations, and Generated Code connect across 6 domains and 50+ modules.

**No source code is included in this report.** All numbers are real, derived from the production repository as of March 2026.

---

## System Scale at a Glance

| Metric | Count |
|:---|:---|
| Business Domains | 6 (Asset, Identity, Policy, Affairs, Posture, Knowledge) + System |
| `model.yaml` Configurations | **54** (one per module/sub-module) |
| Ontology Extractions (`ontology-extracted.md`) | 7 (one per major domain) |
| `.cursor/rules/` Core Rules | 15 files, 83.8 KB total |
| `.cursor/rules/modules/` Auto-Generated Rules | 6 files (one per domain) |
| Design & Architecture Documents (`docs/`) | **397 files**, 76.2 MB total |
| Rule Optimization Records | 5 documented optimization rounds |
| Backend Source Files (`backend/src/`) | 617 files, 1,491 KB |
| Frontend Source Files (`frontend/src/`) | 274 files, 1,377 KB |
| Total Source Files | **891** |

---

## Layer Architecture: How Everything Connects

```
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER 1: GOVERNANCE                          │
│                    .cursor/rules/ (21 rules)                    │
│                                                                 │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────────┐  │
│  │ design-is-  │  │ workflow-    │  │ ontology-workflow.mdc │  │
│  │ authority   │  │ router.mdc   │  │ (ODD pipeline)        │  │
│  │ .mdc        │  │ (60+ routes) │  │                       │  │
│  └──────┬──────┘  └──────┬───────┘  └───────────┬───────────┘  │
│         │               │                       │              │
│         ▼               ▼                       ▼              │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  rule-evolution.mdc → 5 documented optimization rounds   │  │
│  │  (self-improving closed loop)                            │  │
│  └──────────────────────────────────────────────────────────┘  │
│         │                                                      │
│         ▼  [Generates]                                         │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  modules/asset.mdc  │ modules/identity.mdc │ ...× 6     │  │
│  │  (auto-generated domain rules)                           │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   LAYER 2: DOMAIN KNOWLEDGE                     │
│                   docs/domain/ (397 files)                      │
│                                                                 │
│  For each of the 6 domains:                                     │
│                                                                 │
│  ┌─────────────────────┐    ┌──────────────────────────────┐   │
│  │ PM Specification    │───▶│ ontology-extracted.md (×7)   │   │
│  │ (requirements doc)  │    │ Formal domain concepts,      │   │
│  │                     │    │ relationships, constraints    │   │
│  └─────────────────────┘    └──────────────┬───────────────┘   │
│                                             │                   │
│                                             ▼                   │
│                              ┌──────────────────────────────┐  │
│                              │ model.yaml (×54)             │  │
│                              │ Per-module config:           │  │
│                              │ fields, types, components,   │  │
│                              │ validation rules, UI layout  │  │
│                              └──────────────┬───────────────┘  │
│                                             │                   │
│  ┌──────────────────────────────────────────┼──────────────┐   │
│  │ _technical/                              │              │   │
│  │  ├── modules.yaml (module registry)      │              │   │
│  │  ├── tables.yaml  (DB schema map)        │              │   │
│  │  └── 14 tech docs total                  │              │   │
│  └──────────────────────────────────────────┼──────────────┘   │
└─────────────────────────────────────────────┼──────────────────┘
                                              │
                                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  LAYER 3: CODE GENERATION                       │
│                                                                 │
│  model.yaml ──▶ gen-schema.js ──▶ schema.ts (frontend)         │
│  model.yaml ──▶ gen-backend.js ──▶ Entity + Mapper + Crud*     │
│                                    (backend four-piece set)     │
│                                                                 │
│  ┌───────────────────────────┐  ┌───────────────────────────┐  │
│  │ Frontend (274 files)      │  │ Backend (617 files)       │  │
│  │ Vue 3 + ListPageEngine    │  │ Spring Boot + MyBatis     │  │
│  │ Schema-driven rendering   │  │ AbstractCrudService base  │  │
│  │ 1,377 KB total            │  │ 1,491 KB total            │  │
│  └───────────────────────────┘  └───────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Domain Breakdown: 54 model.yaml Configurations

| Domain | Modules | model.yaml files | Key Examples |
|:---|:---|:---|:---|
| **Asset** | Asset core, category, domain, grade, type, meta-field, archive, ignore, discovery, discover-result, discover-task | 11 | `asset/model.yaml` (core entity with 30+ fields) |
| **Identity** | Personnel, organization, application, device, managed-system | 5 | `identity/personnel/model.yaml` |
| **Policy** | Auth, auth-subject, auth-object, authorization, dynamic-authorization, baseline, compliance-plan, protection, security-plan, role, task-type, disposal-task, analysis-indicator, analysis-task, linkage-action | 15 | `policy/authorization/model.yaml` |
| **Affairs** | Incident, work-order, approval, approval-rule, audit-log, risk-warning, violation-notice, vuln-check, asset-vulnerability, baseline-check, baseline-noncompliance | 11 | `affairs/incident/model.yaml` |
| **Posture** | Alert, indicator, analysis-model | 3 | `posture/alert/model.yaml` |
| **Knowledge** | Vulnerability, vuln-type, blackwhitelist, directory, publish-task, receive-task, classify, subscribe | 8 | `knowledge/vulnerability/model.yaml` |
| **System** | Sys-user, dict, audit-log | 3 | `system/sys-user/model.yaml` |

---

## Rule Optimization History

5 documented optimization rounds, each with quantified before/after metrics:

| Date | Optimization | Key Metric Improvement |
|:---|:---|:---|
| 2026-03-14 | Design-First Implementation Path | Files read: 9+ → 4-6; Search ops: 5+ → 0-1 |
| 2026-03-14 | Ontology-Driven Debugging Path | Thinking pauses: 111s → ~30s |
| 2026-03-14 | Concept Traceability Routing | Added ontology-first diagnostic pipeline |
| 2026-03-14 | Component Behavior Debugging | Added UI rendering logic chain |
| 2026-03-14 | Test Routing & Subagent Constraints | Prevented AI from running untested code |

---

## The Generalization Pipeline

```
SOURCE PROJECT (this report)              CURSOR-GENESIS (reusable atoms)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

15 core rules (Chinese, 83.8KB)  ──────▶  4 universal atoms (English, 12KB)
 ├── design-is-authority.mdc     ──────▶   design-authority.mdc
 ├── workflow-router.mdc         ──────▶   routing-engine.mdc
 ├── ontology-workflow.mdc       ──────▶   ontology-driven-dev.mdc
 └── rule-optimization-guide.mdc ──────▶   rule-evolution.mdc

6 auto-generated domain rules    ──────▶  (Proof of "generative governance")
54 model.yaml configs            ──────▶  (Proof of ODD pipeline at scale)
5 optimization records           ──────▶  (Proof of self-evolution loop)
397 design docs                  ──────▶  (Proof of design-first methodology)
891 source files                 ──────▶  (Proof of production-scale delivery)
```

---

## How to Read This Report

If you are a **Cursor team member** reviewing this:
1. The 4 generalized atoms in `stable/atoms/rules/enterprise/` are ready to use in any project.
2. The `examples/source-project/` directory contains the 21 original rules — you can read them to see the unedited, battle-tested originals.
3. This anatomy report shows the scale behind those rules: 54 configs, 397 docs, 891 source files — all governed by 21 rules.
4. The "Lessons Learned" section in `examples/source-project/README.md` documents what we got wrong (Rule vs. Plan confusion) and how the generalized atoms fixed it.
