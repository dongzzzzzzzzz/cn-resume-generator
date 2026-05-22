---
name: cn-resume-generator
description: Generate and improve Chinese domestic job-search resumes and application packages. Use when the user asks to 写简历, 改简历, 生成简历, 优化简历, 针对JD优化, 做BOSS/智联/猎聘/脉脉/拉勾简历, 准备校招/社招/实习/转行简历, 生成开聊话术, 评估候选人和岗位匹配度, 面试前准备, 或根据简历/JD预测面试问题. The skill is for China's hiring platforms and HR/hunter screening reality, not default overseas ATS score chasing.
---

# CN Resume Generator

Create a domestic China job-search package: resume strategy, evidence audit, clean attachment resume, platform paste version, opening/referral scripts, JD-fit risk warning, interview-question forecast, and pre-interview study plan.

## Core Principle

**最高原则：真实可防守。** 简历、平台话术、面试答案必须共享同一事实源。简历中的每个卖点都必须能在面试中防守；答不出来的内容不要写成强断言。

Optimize for truthful employability, not cosmetic polish.

- Make the resume easier for HR, hiring managers, and hunters to understand in 30 seconds.
- Match the target JD and platform context without inventing credentials, employers, projects, ownership, or metrics.
- Surface weak fit clearly before the interview. A resume can frame evidence; it cannot fake ability.
- Treat ATS as a compatibility check only for large-company, foreign-company, and campus-portal scenarios.
- Use `[待确认]` only in a clearly named draft/checking version, never in the final application resume.
- Do not load every reference upfront. Read the required reference at the step where it is needed.
- Skill source files, references, sample data, and test descriptions must use fictional anonymized examples only. Never preserve real user names, contact details, company timelines, internal project names, or identifiable case details in the skill.

## Workflow

1. **Parse inputs**
   - Classify candidate type: `社招`, `应届生`, `实习`, `转行`, or `高管/专家`.
   - Classify platform: `BOSS`, `智联`, `猎聘`, `脉脉`, `拉勾`, `校招网申`, or `通用附件`.
   - Classify task: `新建简历`, `旧简历改造`, `针对JD定制`, `面试准备`, or `公开脱敏案例`.
   - If the user only says "帮我写简历" or similar, ask first for target role/JD, candidate type, old resume/raw experience, and desired output.
   - If there is no old resume, raw experience, or concrete facts, enter `从零起步模式`: read `references/from-scratch-intake.md`, collect evidence first, and do not generate a resume or platform script yet.
   - For PDF/image resumes, extract readable text first and verify timeline, employers, titles, projects, and contact details before auditing.

2. **Plan resume strategy**
   - Read `references/resume-strategy.md`.
   - Identify the target role's screening logic: hard gates, top 3 capabilities, differentiators, and likely rejection risks.
   - Decide the candidate positioning: `强匹配`, `相近转化`, `保守投递`, or `不建议投递`.
   - Draft the internal strategy before writing: main selling line, secondary selling points, content to weaken or omit, expected section structure, and delivery mode.
   - If the material is messy, classify and rank it before asking. If it is hollow, ask for evidence instead of expanding labels.
   - Do not generate a resume until this strategy decision exists.

3. **Audit evidence, probe claims, and choose mode**
   - Read `references/evidence-audit.md`.
   - Keep evidence collection separate from evidence selection: record user facts first, then map them to the JD.
   - Extract JD hard requirements and the top 3 role capabilities.
   - Map candidate evidence to the JD and mark evidence level: strong, probeable, weak, missing, or risky; then mark match type: direct, indirect, or unrelated.
   - Apply 3 hard gates: timeline/resume abnormality, missing JD hard requirement, and missing case for core role capability.
   - Before broad follow-up, read `references/deep-probe.md` and the relevant role probe section.
   - Before targeted follow-up, read `references/claim-led-probing.md`.
   - Use two-layer probing: first understand the experience, then verify the specific claims needed for the chosen strategy.
   - Ask up to 3 high-value questions per turn. Each question must say what claim or writing strength it verifies, such as ownership, metric basis, scope, depth, or personal boundary.
   - Probe by resume/core-experience group, not by every possible claim. After at most 2 rounds, choose `正式投递版`, `保守投递版`, `草稿校对版`, `采集清单`, or `不建议投递包`.
   - After each user answer, digest it before writing: what can be written, what must be conservative, what still needs confirmation, and what is forbidden.
   - Record strategy, gate status, asked probes, answer digestion, unanswered items, final forbidden/downgrade list, and selected mode in `证据审计与补充问题.md`.

4. **Generate package**
   - Do not create the output folder, write `resume-data.json`, render Markdown/DOCX, or write platform scripts until evidence audit is complete and either formal/conservative mode is allowed or `快速草稿模式` is selected.
   - If only category labels are available, output `经历采集清单.md` or gap-closing advice; do not create a fill-in-the-blank resume.
   - Before generating resume content, read `references/role-playbooks.md` and `references/common-resume-problems.md`.
   - Before generating platform scripts, read `references/platform-playbooks.md`.
   - Default to `深挖优先模式`: ask before writing when a hard gate fails.
   - Use `快速草稿模式` only when real experience facts exist but limited details remain unresolved. Name outputs as draft/checking versions, downgrade uncertain claims, and mark missing facts as `[待确认]`.
   - If fit is `不建议投递`, generate a risk-first package: state why fit is low, do not package the resume as high-fit, and provide safer wording, alternative targets, or gap-closing advice.
   - Project bullets use a flexible `3+1` structure: background/goal, solution/key action, result/impact, and optionally real challenge/tradeoff/reusable method. Do not fill the optional bullet with empty language.
   - Work experience states responsibility boundary and outcomes; project experience states method, architecture, process, or decisions. Avoid repeating the same metric or claim in both.
   - Every core project must prove a specific capability. If you cannot explain what capability a project proves, downgrade, merge, or omit it.
   - Final resume, online version, platform scripts, self-introduction, and interview answers must inherit the same strategy and evidence source. Do not make platform copy stronger than the attachment resume.
   - Use role language from `references/role-playbooks.md` when needed.
   - Apply `references/common-resume-problems.md` as the final resume QA checklist.

5. **Prepare defense, render, and QA**
   - Read `references/risk-rubric.md` before producing `JD适配风险提示.md`.
   - Predict interview questions only from the resume, JD, and confirmed user facts.
   - If company/role-specific prep matters, search public sources such as 牛客, 脉脉, BOSS articles, 看准, 职朋, 应届生求职网, or user-provided links. Do not log in, bypass permissions, or scrape private content.
   - Read `references/interview-question-playbooks.md`.
   - Read `references/rendering-qa.md` before finalizing structured data and rendered files.
   - Prefer a folder under the current workspace: `resume-output/<YYYYMMDD>-<岗位>/`.
   - Build structured `resume-data.json`, then run `scripts/render_resume.py` to create Markdown and DOCX.
   - Run `scripts/qa_check.py resume-data.json <rendered-md> --audit 证据审计与补充问题.md` before final delivery.
   - If QA reports `fatal`, fix the resume or change it to a clearly named draft/checking version before delivery.
   - If QA reports `warning`, handle it by rewriting, downgrading, omitting, or explaining why it remains.
   - `修改说明.md` must describe only changes that are actually present in the final files.
   - If PDF export tooling is available, export PDF; otherwise leave DOCX + Markdown.

## Minimum Input Template

When the user has not provided enough information, ask them to paste this:

```text
目标岗位/JD：
候选人类型：社招 / 应届生 / 实习 / 转行 / 高管专家
目标平台：BOSS / 智联 / 猎聘 / 脉脉 / 拉勾 / 校招网申 / 通用附件
旧简历或经历草稿：
是否用于公开演示：是/否
希望输出：附件简历 / 平台粘贴版 / 面试准备 / 全部
```

## Output Contract

Default output folder:

```text
resume-output/<YYYYMMDD>-<target-role>/
├── <姓名>-<岗位>-附件简历.docx
├── <姓名>-<岗位>-附件简历.md
├── 在线简历粘贴版.md
├── 平台话术包.md
├── 经历采集清单.md
├── 证据审计与补充问题.md
├── JD适配风险提示.md
├── 面试追问预测.md
├── 面试前补课清单.md
├── 修改说明.md
└── resume-data.json
```

Each final package must be immediately usable:

- Attachment resume: clean single-column Chinese resume suitable for upload.
- Platform paste version: sectioned text for online-resume fields.
- Platform scripts: BOSS opening message, 脉脉 referral request, 猎头摘要, or platform-specific equivalent.
- Intake checklist: used when facts are not enough to write a defensible resume.
- Evidence audit: evidence strength, allowed phrasing, missing facts, and claims that cannot be exaggerated.
- Risk warning: fit level, interview exposure points, delivery risk, and preparation advice.
- Interview forecast: questions tied to the user's actual resume projects and target JD.
- Study plan: what to review in 1 day, 3 days, and longer-term.

Keep `证据审计与补充问题.md` and `JD适配风险提示.md` distinct:

- `证据审计与补充问题.md`: "证据真假强弱、能不能写、还要问什么。"
- `JD适配风险提示.md`: "岗位匹配高低、面试会暴露什么、怎么准备。"

`证据审计与补充问题.md` must include:

- `核心卖点假设`
- `回答消化结论`
- `可写内容`
- `需保守表达`
- `仍需确认`
- `终稿禁止/降级清单`

## Candidate-Type Rules

- **社招**: emphasize business context, personal action, collaboration scope, tools/methods, and measurable results.
- **应届生**: do not fabricate projects. Mine coursework, graduation project, competitions, clubs, internships, part-time work, self-built demos, and learning proof.
- **实习**: emphasize availability, learning speed, coursework/practice relevance, and basic execution reliability.
- **转行**: explain why the candidate is not starting from zero; translate prior experience into target-role evidence.
- **高管/专家**: emphasize business scale, team scale, budget/revenue/cost ownership, strategic decisions, and industry credibility.

For `应届生`, `实习`, `转行`, or hollow old resumes, use `references/from-scratch-intake.md` before drafting when concrete evidence is missing.

## Platform Rules

- **BOSS**: optimize first-screen fit and direct opening message.
- **智联**: optimize online field completeness, attachment resume, and campus/enterprise screening compatibility.
- **猎聘**: optimize hunter-forwardable summary, seniority, stability, and compensation/level fit.
- **脉脉**: optimize professional profile, personal brand, referral request, and target-company networking message.
- **拉勾**: optimize internet-role keywords, project links, product/operation/tech stack, and growth metrics.
- **校招网申**: optimize form fields, campus experiences, open-question material, and conservative ATS compatibility.

## Privacy and Truthfulness

- In public-demo mode, anonymize names, schools, companies, phone, email, links, project names, and sensitive business data.
- In real-application mode, preserve user-provided facts but remind the user to verify all contact details and claims.
- In draft or audit files, mark uncertain metrics as `待确认`; in final resumes, omit or downgrade unconfirmed claims instead of converting them into facts.
- Never claim `主导`, `负责核心`, `精通`, `独立完成`, or quantified impact unless the user evidence supports it.
- Do not write real user cases into skill references, sample files, tests, or instructions. Use `候选人A`, `某公司`, `某项目`, and `demo@example.com` style placeholders.
- Real user material may be used as local input for a run, but must not be preserved in the skill source.

## Script Usage

Create a `resume-data.json` with candidate and section data. `candidate.summary`, `candidate.gender`, `candidate.birth`, and `candidate.years_of_experience` are supported when the user provides them; never invent them.

Render:

```bash
python3 scripts/render_resume.py resume-data.json --output-dir resume-output/20260506-产品经理 --basename 候选人A-产品经理
python3 scripts/qa_check.py resume-data.json resume-output/20260506-产品经理/候选人A-产品经理-附件简历.md --audit resume-output/20260506-产品经理/证据审计与补充问题.md
```

The script renders:

- `<basename>-附件简历.md`
- `<basename>-附件简历.docx` when `python-docx` is installed

If the script cannot create DOCX, still provide the Markdown resume and tell the user what dependency is missing.
