# exports/ 目录说明

## 用途

存放待上报到 knowledge-graph 的精炼内容。

## 目录结构

```
exports/
├── capability-changes/    # 能力变更
├── refined-knowledge/     # 精炼知识
└── feedback/             # 方案反馈
```

## 使用流程

1. 将精炼后的内容放入对应目录
2. 使用 `/export status` 查看待上报内容
3. 使用 `/export prepare` 准备上报清单
4. 使用 `/export submit` 提交 PR 到上游

## 内容格式

每个文件应包含：
- 标题和摘要
- 问题描述
- 解决方案
- 验证结果
- 相关标签

详见 `stable/packs/knowledge-manage/leaf-node/skills/node-export.skill.yaml`
