# cursor-genesis

> Cursor AI 协作研发的组件库和知识库

## 定位

这是 knowledge-graph 体系下的一个**叶子节点**，专注于 Cursor 领域。

**职责**：
- 生产 Cursor 相关的组件和知识
- 接收使用方的回流改进
- 暴露标准化索引供上层检索

**不负责**：
- 跨领域知识关联（上层职责）
- 治理框架设计（leaf-node-framework 职责）

## 目录结构

```
cursor-genesis/
├── meta.yaml                 # 节点元信息
├── stable/                   # 【对外发布】稀疏检出目标
│   ├── atoms/               # 原子层
│   │   ├── rules/          # Cursor Rules
│   │   ├── capabilities/   # 原子能力（四层认知）
│   │   ├── standalone/     # 独立角色
│   │   └── code-templates/ # 代码脚手架
│   ├── packs/               # 套装层
│   │   └── v1-talk/        # 简化版套装
│   └── knowledge/           # 知识层（可被上层索引）
│       ├── index.yaml      # 知识索引
│       ├── cursor-specs/
│       ├── prompt-engineering/
│       ├── architecture-decisions/
│       └── learnings/
├── backflow/                 # 【回流区】
│   ├── pending/             # 待审批
│   └── processing/          # 处理中
├── workspace/                # 【本地工作台】.gitignore
└── scripts/                  # 【自动化】
```

## 使用方式

### 新项目引入

```bash
# 稀疏检出 v1-talk 套装
git clone --filter=blob:none --sparse https://github.com/you/cursor-genesis.git .cursor-genesis
cd .cursor-genesis
git sparse-checkout set stable/packs/v1-talk stable/atoms/rules stable/atoms/capabilities
```

### 回流改进

```bash
# Fork 后提交 PR 到 backflow/pending/
git checkout -b backflow/my-improvement
# 添加你的改进到 backflow/pending/{project-hash}/{your-name}/{commit-id}/
git push origin backflow/my-improvement
# 然后提 PR
```

## 套装说明

| 套装 | 定位 | 适用人群 |
|:---|:---|:---|
| v1-talk | only talk，对话触发 | 普通用户 |
| v2-advanced | 完整功能，skill/commands/hooks | 专业用户（规划中） |

## 版本

当前版本：1.0.0

详见 [CHANGELOG](./CHANGELOG.md)
