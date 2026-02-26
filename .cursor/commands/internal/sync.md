# /sync - 从上游拉取知识

> 认知系统体系内部命令，用于叶子节点从 knowledge-graph 拉取知识

## 用途

叶子节点（如 cursor-genesis）从 knowledge-graph 拉取：
- 根事实（roots/*.yaml）
- 叶子节点规范（meta/leaf-node-spec.md）
- 相关主题索引（index/topics/*.yaml）

## 子命令

### /sync status

查看与上游的同步状态。

**输出示例**：
```
同步状态：
- roots/cognitive-science.yaml: synced (2026-02-20)
- meta/leaf-node-spec.md: outdated (上游更新于 2026-02-25)
- index/topics/ai-collaboration.yaml: local_only
```

### /sync pull

从上游拉取更新。

**流程**：
1. 读取 `meta.yaml` 中的 `receives_from_upper` 配置
2. 执行 git sparse-checkout 或 submodule update
3. 将更新放入 `pending/upstream/` 待审批
4. 提示用户审批后合入 `stable/`

### /sync config

查看或修改拉取配置。

**配置位置**：`meta.yaml`

```yaml
receives_from_upper:
  - type: root_facts
    source: roots/*.yaml
    auto_pull: true

  - type: leaf_node_spec
    source: meta/leaf-node-spec.md
    auto_pull: true

  - type: topic_index
    source: index/topics/ai-collaboration.yaml
    auto_pull: false  # 按需拉取
```

## 前置条件

- 当前项目是 knowledge-graph 的叶子节点
- 已配置 git remote 或 submodule 指向 knowledge-graph
- `meta.yaml` 中有 `receives_from_upper` 配置

## 底层实现

基于 Git 的选择性拉取：

```bash
# sparse-checkout 方式
git sparse-checkout set <paths>
git pull origin main

# submodule 方式
git submodule update --remote
```

## 与 /backflow 的关系

```
knowledge-graph
      ↑ /backflow submit (上报)
      │
      ↓ /sync pull (拉取)
cursor-genesis
```

- `/sync`：拉取上游知识（下达）
- `/backflow`：向上游回流内容（上报）
