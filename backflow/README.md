# 回流机制说明 (Backflow Mechanism)

> **版本**: 1.0.0
> **更新日期**: 2026-02-26

## 概述

回流机制是 cursor-genesis 从下游项目收集改进和创新的核心流程。当你在实际项目中使用 cursor-genesis 时发现改进点或创造了新的有价值内容，可以通过回流机制贡献回来，让整个生态受益。

## 回流流程

```
下游项目使用 → 发现改进点 → 提交到 pending/ → 审核 → 移至 processing/ → 完善 → 合并到 stable/
```

### 阶段说明

1. **pending/** - 待审核区
   - 下游项目提交的原始内容
   - 等待初步审核
   - 目录结构：`pending/<project-hash>/<contributor-name>/<commit-id>/`

2. **processing/** - 处理中区
   - 通过初审的内容
   - 正在进行完善、测试、文档化
   - 可能需要与贡献者沟通调整

3. **stable/** - 稳定发布区
   - 审核通过并完善的内容
   - 正式发布，供所有下游项目使用
   - 遵循语义化版本管理

## 提交指南

### 1. 准备工作

在提交回流前，请确保：

- ✅ 内容已在你的项目中充分验证
- ✅ 有清晰的使用场景和价值说明
- ✅ 符合 cursor-genesis 的现有风格和结构
- ✅ 不包含敏感信息或私有数据
- ✅ 已阅读 [TEMPLATE.md](TEMPLATE.md) 并准备好填写

### 2. 提交步骤

#### Step 1: Fork 仓库

```bash
# 在 GitHub 上 fork cursor-genesis 到你的账号
# 然后克隆你的 fork
git clone https://github.com/your-username/cursor-genesis.git
cd cursor-genesis
```

#### Step 2: 创建回流分支

```bash
git checkout -b backflow/your-improvement-name
```

**分支命名规范**：
- `backflow/new-capability-xxx` - 新增能力
- `backflow/improve-rule-xxx` - 改进规则
- `backflow/fix-xxx` - Bug 修复
- `backflow/doc-xxx` - 文档改进

#### Step 3: 创建回流目录

```bash
# 生成项目 hash（可选，或使用项目简称）
PROJECT_HASH="anfu-test-a3f2"  # 示例
CONTRIBUTOR="zhangsan"
COMMIT_ID="20260226-001"

mkdir -p backflow/pending/${PROJECT_HASH}/${CONTRIBUTOR}/${COMMIT_ID}
cd backflow/pending/${PROJECT_HASH}/${CONTRIBUTOR}/${COMMIT_ID}
```

#### Step 4: 填写提交信息

```bash
# 复制模板
cp ../../../../TEMPLATE.md SUBMISSION.md

# 编辑 SUBMISSION.md，填写所有必填字段
# 使用你喜欢的编辑器
```

#### Step 5: 添加回流内容

```bash
# 创建内容目录
mkdir content

# 根据内容类型组织文件
# 示例 1: 回流一个改进的规则文件
mkdir content/rules
cp /path/to/your/improved-rule.mdc content/rules/

# 示例 2: 回流一个新的能力定义
mkdir content/capabilities
cp /path/to/your/new-capability.md content/capabilities/

# 示例 3: 回流一个新的团队模式
mkdir content/patterns
cp /path/to/your/new-pattern.md content/patterns/
```

#### Step 6: 添加验证材料（可选但推荐）

```bash
mkdir tests
# 添加测试用例、使用截图、效果对比等
cp /path/to/test-case.md tests/
cp /path/to/screenshot.png tests/
```

#### Step 7: 提交并创建 PR

```bash
# 返回仓库根目录
cd ../../../../..

# 提交更改
git add backflow/pending/${PROJECT_HASH}/${CONTRIBUTOR}/${COMMIT_ID}
git commit -m "backflow: [简短描述你的改进]

详细说明：
- 改进内容：xxx
- 解决问题：xxx
- 验证情况：xxx
"

# 推送到你的 fork
git push origin backflow/your-improvement-name

# 在 GitHub 上创建 Pull Request
# PR 标题格式：[Backflow] 简短描述
# PR 描述：引用 SUBMISSION.md 中的关键信息
```

## 审核标准

### 内容质量

- **清晰性**: 文档清晰，代码可读，命名规范
- **完整性**: 包含必要的说明、示例、使用指南
- **可复用性**: 具有通用性，不是项目特定的硬编码

### 一致性

- **风格一致**: 遵循 cursor-genesis 的文件结构和命名规范
- **格式一致**: Markdown 格式、YAML 格式符合现有标准
- **术语一致**: 使用与现有文档一致的术语和概念

### 价值

- **解决真实问题**: 有明确的使用场景和价值
- **非重复**: 不与现有内容重复或冲突
- **可维护**: 易于理解和维护

### 验证

- **已测试**: 在实际项目中验证过
- **有案例**: 提供使用案例或示例
- **可复现**: 其他人可以按照说明复现效果

## 审核流程

### 1. 初审（1-3 天）

维护者会检查：
- 是否符合基本格式要求
- 是否包含必填信息
- 是否有明显的质量问题

**可能的结果**：
- ✅ **通过初审** → 移至 `processing/`
- ⚠️ **需要补充** → 在 PR 中留言，要求补充信息
- ❌ **不符合要求** → 关闭 PR，说明原因

### 2. 详细审核（3-7 天）

对于通过初审的内容，维护者会：
- 详细审查内容质量
- 测试验证功能
- 检查与现有内容的兼容性
- 可能与贡献者沟通调整

**可能的结果**：
- ✅ **审核通过** → 准备合并到 `stable/`
- 🔄 **需要修改** → 在 PR 中提出修改建议
- ❌ **不适合合并** → 关闭 PR，说明原因

### 3. 合并发布（1-3 天）

审核通过后：
- 内容从 `processing/` 合并到 `stable/`
- 更新 CHANGELOG.md
- 根据变更类型决定版本号
- 发布新版本（如果需要）

## 审核时间预期

| 内容类型 | 初审 | 详细审核 | 总计 |
|:---|:---|:---|:---|
| Bug 修复 | 1 天 | 1-2 天 | 2-3 天 |
| 文档改进 | 1 天 | 1-2 天 | 2-3 天 |
| 规则优化 | 1-2 天 | 2-3 天 | 3-5 天 |
| 新增能力 | 2-3 天 | 3-5 天 | 5-8 天 |
| 新增模式 | 2-3 天 | 4-7 天 | 6-10 天 |
| 重大变更 | 3-5 天 | 7-14 天 | 10-19 天 |

**注意**：以上时间为工作日，不包括周末和节假日。

## 回流内容类型

### ✅ 适合回流的内容

1. **新的原子能力（Capability）**
   - 新的角色定义
   - 新的思维模型
   - 新的应用场景

2. **改进的规则文件（Rule）**
   - 更清晰的规则表达
   - 新的约束条件
   - 优化的触发逻辑

3. **新的团队协作模式（Pattern）**
   - 新的团队拓扑
   - 新的协作流程
   - 新的场景编排

4. **经验总结和最佳实践**
   - 使用心得
   - 踩坑记录
   - 优化建议

5. **Bug 修复**
   - 文档错误
   - 配置问题
   - 逻辑缺陷

6. **文档改进**
   - 补充说明
   - 示例代码
   - 使用指南

### ❌ 不适合回流的内容

1. **项目特定的业务逻辑**
   - 特定领域的实体定义
   - 特定业务的流程规则
   - 公司内部的规范

2. **敏感信息**
   - API 密钥、密码
   - 内部系统地址
   - 客户数据

3. **未经验证的实验性内容**
   - 仅在理论上可行
   - 未在实际项目中使用
   - 效果不明确

4. **与现有内容重复**
   - 已有类似功能
   - 仅是微小差异
   - 可以通过配置实现

## 贡献者权益

### 署名

- 所有被合并的回流内容都会在 CHANGELOG.md 中署名
- 重要贡献会在 README.md 的贡献者列表中展示

### 反馈

- 维护者会在 PR 中及时反馈审核意见
- 对于不能合并的内容，会说明原因和改进建议

### 优先支持

- 活跃贡献者的问题和建议会得到优先响应
- 可以参与 cursor-genesis 的规划讨论

## 常见问题

### Q1: 我的回流内容多久会被审核？

根据内容类型，初审通常在 1-3 天内完成。详细审核时间见上方的"审核时间预期"表格。

### Q2: 如果我的回流被拒绝了怎么办？

维护者会在 PR 中说明拒绝原因。你可以：
- 根据反馈修改后重新提交
- 在 Issue 中讨论改进方案
- 在你的项目中继续使用（不影响你的使用）

### Q3: 可以回流多个改进吗？

可以，但建议：
- 每个 PR 只包含一个主要改进
- 相关的多个小改进可以放在一个 PR 中
- 不相关的改进应该分别提交

### Q4: 回流的内容会被修改吗？

可能会。维护者可能会：
- 调整格式以符合规范
- 优化文档表达
- 重命名文件以保持一致性
- 重大修改会与贡献者沟通

### Q5: 我可以撤回回流吗？

在合并到 `stable/` 之前可以撤回。合并后：
- 内容已成为 cursor-genesis 的一部分
- 遵循开源协议（如果有）
- 不能撤回，但可以提交改进

## 联系方式

- **问题反馈**: 在 cursor-genesis 仓库提交 Issue
- **讨论交流**: 在 PR 或 Issue 中留言
- **紧急问题**: 在 PR 中 @维护者

---

**感谢你的贡献！每一个回流都让 cursor-genesis 更强大。**
