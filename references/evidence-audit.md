# Evidence Audit

Use this before drafting any resume or platform script. The goal is to decide what can be written, what must be downgraded, and what needs follow-up.

Evidence audit must follow the strategy decision in `resume-strategy.md` and feed the final QA script. Treat it as the fact ledger for the whole package.

## Evidence Unit

For each important experience, extract:

```text
场景：
个人职责边界：
方法/工具：
交付物：
结果：
数据口径：
可追问细节：
不可夸大点：
```

Do not require every field for every bullet, but high-value resume claims need enough fields to survive interview follow-up.

## Collection vs Selection

Keep these phases separate:

1. **Collect**: record the user's facts without judging fit or filling gaps from imagination.
2. **Map**: after collection, map facts to JD hard requirements and the top 3 role capabilities.
3. **Select**: mark each evidence item as `直接匹配`, `间接匹配`, or `无关`, then decide what enters the resume.

Do not filter too early during collection, and do not write unrelated evidence just because it sounds impressive.

## Evidence Levels

| Level | Use when | Allowed writing |
|---|---|---|
| 强证据 | Has clear scene, personal action, result or defensible output, and contribution boundary. | Can be used as a resume selling point. |
| 可深挖 | Has scene/action, but result, metric, or contribution boundary is unclear. | Ask follow-up before strong wording; otherwise write conservatively. |
| 弱证据 | Mostly responsibility description with no scene, output, or result. | Keep as plain responsibility or omit. |
| 无证据 | JD asks for a capability but resume has no supporting experience. | Do not claim it; list as gap/risk. |
| 风险证据 | Claim may exceed actual contribution, seniority, metric, or ownership. | Downgrade wording and flag in audit. |

Risky strong words include `主导`, `负责核心`, `独立完成`, `从0到1`, `精通`, `体系化`, `战略`, and precise metrics without user-confirmed basis.

High-value claims need these fields to be defensible:

```text
数据口径：
个人贡献边界：
结果归因主体：
使用/影响范围：
禁止或需降级表达：
```

If these fields are missing for a precise metric, strong ownership claim, broad scope claim, seniority claim, or platform/system/process claim, downgrade it from `强证据` to `可深挖` or `风险证据`.

## Match Types and Sorting

- **直接匹配**: proves a JD hard requirement or top-3 capability in the same role context.
- **间接匹配**: proves a transferable action pattern, but not the same role context.
- **无关**: does not support the target role, hard requirement, or positioning.

Resume priority:

```text
直接匹配 > 间接匹配 > 无关
核心能力1 > 核心能力2 > 核心能力3
强证据 > 可深挖 > 弱证据
```

Write only direct and useful indirect evidence. Cut unrelated evidence first.

Indirect evidence must use a concrete action analogy:

- Allowed: `在客户需求沟通中，将模糊诉求整理成方案清单；这一动作与目标岗位中把业务需求拆成执行任务的逻辑相近。`
- Avoid: `销售经历培养了沟通能力。`
- Forbidden: writing indirect evidence as equivalent experience, such as `具备测试项目经验` when the source evidence is only customer communication.

## Hard Gates

Block a formal application version and ask follow-up when any hard gate fails:

1. **Timeline/resume abnormality**: unexplained gap, overlap, very short full-time tenure pattern, or recent experience too old for the target.
2. **JD hard requirement missing**: degree, years, certificate, city, language, tech stack, portfolio, industry background, or work authorization cannot be supported.
3. **Core capability lacks case**: a top-3 role capability has no defendable story or output.

Ask at most 3 questions per round. If 2 rounds still cannot fill hard-gate or core-capability facts, recommend `快速草稿模式`.

## Minimum Generation Threshold

Use JD top 3 capabilities:

- **充足**: all 3 have direct, defensible evidence. Generate formal version.
- **部分充足**: 1-2 have direct evidence and the rest have useful indirect evidence. Generate conservative version plus gap-closing advice.
- **不足**: only 1 capability has direct evidence and the rest have no useful match. Do not generate a formal resume; output `经历采集清单.md` plus gap-closing path.
- **空白**: no capability has direct or useful indirect evidence. Output direction advice, alternative targets, and learning path.

Indirect evidence cannot by itself make a candidate high-fit for a core capability.
If there are only category labels or indirect-only evidence for all core capabilities, do not use `快速草稿模式` to create a fill-in resume; output intake/gap-closing materials.

## Completion Standard

Before drafting a formal resume or platform script, all of these must be true:

- The core area has an evidence level for every row.
- The core area has a match type and write priority for every row.
- Each core row has an allowed wording decision.
- Each core row has either a follow-up question, `无需追问`, a downgrade decision, or a draft-only `[待确认]` note.
- Every `可深挖`, `弱证据`, or `风险证据` in the core area has been handled by follow-up, downgrade, omission, or draft-only confirmation.
- The audit records whether hard gates passed, failed, or moved the work to `快速草稿模式`.

Do not create output folders, write `resume-data.json`, or render documents before this standard is met, unless the selected mode is explicitly `快速草稿模式`.

## Audit Output

Create `证据审计与补充问题.md`.

### Core Area

Audit only JD hard requirements and the top 3 role capabilities with full columns:

```text
JD要求：
候选证据：
证据等级：
匹配关系：
写入优先级：
允许写法：
需追问：
面试风险：
```

### Supplemental Area

For lower-priority JD items, keep it short:

```text
JD要求：
证据等级：
需追问：
```

Do not chase every supplemental weak item. Follow up only when it changes fit judgment, a resume selling point, or interview risk.

Include a short process record:

```text
核心卖点假设：
回答消化结论：
可写内容：
需保守表达：
仍需确认：
终稿禁止/降级清单：
门禁状态：
已追问：
未确认项：
交付模式：正式投递版 / 保守投递版 / 草稿校对版 / 采集清单 / 不建议投递包
```

`终稿禁止/降级清单` should be structured so `qa_check.py` can read it. Use this format:

```text
## 终稿禁止/降级清单

### 禁止表达
- 禁止：团队级平台
  原因：仅个人或小组试点，未确认团队级采用
- 禁止：主导业务增长
  原因：候选人只负责部分执行，增长归因不完整

### 需降级表达
- 强表达：独立完成
  建议写法：负责其中X模块
- 强表达：提升50%
  建议写法：提升有待确认，改写为优化了流程
```

Only put explicit words or phrases in this list. Do not ask the QA script to infer broad semantics.

## Hollow Resume Detection

Treat an old resume as evidence-poor when it has:

- Responsibilities without specific action/result.
- Tool names without usage scene or output.
- Project names without personal contribution or deliverable.
- Mostly `负责`, `参与`, `协助` but no concrete `做了什么` and `结果如何`.

When detected, tell the user the resume lists experience but lacks defensible details, then use the from-scratch/deep-probe strategy to collect facts. Do not expand hollow labels into strong resume bullets.

## Formal vs Draft

- **正式投递版**: use only confirmed facts; no `[待确认]` in the resume body.
- **草稿校对版**: allowed only when real experience facts exist and limited details remain unresolved after probes. File names and notes must say it needs confirmation before submission.
