# 案例研究：企业安全管理平台

> 首个 Enterprise Pack 验证案例
> 项目类型：企业级安全管理中心（等保 2.0 合规）
> 技术栈：Spring Boot + Vue 3
> 规模：6 个业务域，50+ 模块
> 交付：零到验收 < 2 周

---

## 一、项目背景

基于等保 2.0（GB/T 22239-2019）标准，实现安全运营闭环：预防 → 检测 → 响应 → 恢复。

项目规模超过 50 个模块时，遇到了典型的 AI 协作规模化问题：

- Agent 读取历史代码推断架构，导致架构漂移
- 没有语义约束时字段缺失率高达 35%
- 无法为每个模块手写规则（成本过高）

**解决方案**：引入 Enterprise Pack 的生成式规则系统。

---

## 二、六域架构

从原始业务文档（4 大系统）推导出 6 个业务域：

| 域 | 类型 | 职能 |
|:---|:---|:---|
| **asset** | 基础域 | 被保护的对象（设备、应用、数据资产），全生命周期管理 |
| **identity** | 基础域 | 访问主体（人员、组织、设备身份、应用身份） |
| **knowledge** | 支撑域 | 参考数据（漏洞库、黑白名单、知识目录），发布/订阅模式 |
| **posture** | 流程域 | 感知安全状态（12 种分析能力 + 10 种态势类型 + 告警） |
| **policy** | 流程域 | 定义安全规则（基线、防护策略、认证/授权策略、预案） |
| **affairs** | 流程域 | 执行安全事务（审批、工单、案事件、漏洞检查、审计） |

**依赖方向**：基础域（asset, identity）← 流程域（posture, policy, affairs）依赖

---

## 三、Meta-Rules 如何驱动 16 条规则生成

4 条 Meta-Rules 作为认知框架，指导 Agent 为每个域生成专属规则：

```
design-authority.mdc      ← 锁定设计文档为唯一权威
    ↓
routing-engine.mdc        ← 意图路由：模糊语言 → 确定性读取路径
    ↓
ontology-driven-dev.mdc   ← 从本体推导字段和逻辑
    ↓
rule-evolution.mdc        ← 记录认知路径优化，防止重复踩坑
    ↓
生成 16 条域专属规则（workflow-router / design-is-authority / frontend-dev /
                      backend-dev / security-domain / technical-ontology /
                      entity-boundary / integration-dev / product-mode /
                      acceptance-guide / test-ops / rule-optimization-guide /
                      modules/asset / modules/identity / modules/policy /
                      modules/affairs）
```

---

## 四、ODD（本体驱动开发）的实际效果

### 4.1 传统方式 vs ODD

| 场景 | 传统方式 | ODD |
|:---|:---|:---|
| Agent 推导字段 | 扫描旧代码，猜测字段名 | 读 ontology-extracted.md，直接得到权威字段清单 |
| 新模块开发 | 字段缺失率 35%，需反复补 | 字段缺失率接近 0 |
| 跨域关系 | Agent 不知道 asset→identity 依赖方向 | 本体中已定义，Agent 直接查询 |
| 新概念归属 | 拍脑袋决定放哪个模块 | 按归属规则4条判定（实体/动作/被管理对象/执行事务）|

### 4.2 本体分级体系

本案例验证了三级本体分类的有效性：

| 级别 | 文件命名 | 本案例中的示例 |
|:---|:---|:---|
| 核心本体（core） | `ontology-extracted.md` | SecurityAsset、IdentitySubject、SecurityPolicy |
| 卫星本体（satellite） | `ontology-satellite.md` | AssetType、VulnerabilityRecord |
| 扩展视图（extended） | `ontology-extended.md` | AssetRiskView、ComplianceView |

---

## 五、量化指标

| 指标 | 数值 | 归因 |
|:---|:---|:---|
| 交付周期 | < 2 周（零到验收） | Meta-Rules 消除架构漂移，开发路径确定 |
| Token 读取浪费降低 | 60% | design-authority 禁止扫描历史代码 |
| 字段缺失率 | 35% → ~0% | ODD 本体作为权威字段来源 |
| 生成域专属规则 | 16 条 | 4 条 Meta-Rules 驱动生成 |
| 覆盖模块 | 50+ | 规则覆盖全部业务域 |
| 规则自演化记录 | 持续更新 | rule-evolution 空间记录优化历程 |

---

## 六、可复用的方法论提炼

本案例验证了两层可复用产出：

**第一层：领域本体提取方法论**（换任何业务领域都可用）
- 五步流程：规格说明 → 素材扫描 → 实现层对照 → 概念化 → 形式化
- 显式摘录原则：不依赖记忆，从文档逐段摘录，标注出处
- 本体分级判断：4个判断维度决定核心/卫星/扩展

**第二层：顶层设计审视方法论**（审视任何方法论质量的流程）
- 在审视安管项目设计的过程中涌现
- 按维度检查项目方法论质量的通用框架

详见 `methodology/` 目录。

---

## 七、系统演化链条

```
安全管理中心最终版（全面材料）
  → 六域业务本体提取（认知建立）
  → 身份管理设计材料补充（本体丰富 + 跨域关系）
  → 技术本体 + model.yaml（认知→技术映射）
  → ListPageEngine + AbstractCrudService（代码引擎设计）
  → 开发模态页面（认知展示为可操作界面）
  → 验收模态（按标书固定展示）
  → 元数据管理发现低代码能力
  → 用户模态（简化操作表面）
```

每一步都由设计文档驱动，Agent 在本体语义约束下工作，不跨越设计边界。
