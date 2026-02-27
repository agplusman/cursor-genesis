# Skill: 知识回流管理（cursor-genesis 内部使用）

> cursor-genesis 项目内部使用的回流命令
> 用于接收下游项目回流，以及向 knowledge-graph 上报

## 触发方式

使用 `/backflow` 触发此 skill

## 角色定位

cursor-genesis 是叶子节点，处于中间层：

- **上游**：knowledge-graph（私有仓库）
- **下���**：anfu_test 等实际项目

## 命令

### 查看状态

```
/backflow status
```

### 接收下游回流

```
# 查看待审批的 PR
/backflow review

# 审批特定 PR
/backflow review <pr-number>

# 处理已审批内容
/backflow process
```

### 向上游上报

```
# 准备上报内容
/backflow prepare --to knowledge-graph

# 提交上报
/backflow submit --to knowledge-graph
```

### 同步上游知识

```
/backflow sync --from knowledge-graph
```

## 配置

`.claude/backflow.yaml`:

```yaml
role: leaf

upstream:
  name: knowledge-graph
  repo: https://github.com/SYMlp/knowledge-graph  # 私有
  local_path: d:\Project\knowledge-graph

downstream:
  - name: anfu_test
    local_path: d:\Project\work\anfu_test

export_protocol:
  format:
    must_include:
      - problem_domain
      - solution_summary
      - applicable_scenario
    must_not_include:
      - project_specific_code
```

## 目录结构

```
cursor-genesis/
├── stable/
│   └── knowledge/
│       └── exports/           # 待上报到 knowledge-graph
├── backflow/
│   ├── pending/              # 下游 PR 目标
│   └── processing/           # 已审批待处理
└── .claude/
    ├── backflow.yaml
    └── skills/
        └── backflow.md       # 本文件
```

## 工作流

### 处理下游回流

```bash
# 1. 查看 PR
/backflow review
# 列出 anfu_test 等项目提交的 backflow PR

# 2. 审批 merge
/backflow review 123

# 3. 处理内容
/backflow process
# 整理到 stable/atoms/ 或 stable/knowledge/
```

### 向上游上报

```bash
# 1. 准备内容
/backflow prepare --to knowledge-graph
# 整理 exports/ 中的内容

# 2. 提交
/backflow submit --to knowledge-graph
# 因为 knowledge-graph 是私有仓库
# 会在本地 knowledge-graph 仓库创建分支和 PR
```
