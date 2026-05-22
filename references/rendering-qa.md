# Rendering QA

Use this after drafting `resume-data.json` and before final delivery. It complements `common-resume-problems.md` and `qa_check.py`.

## Data Contract

- `sections` is the main rendered source.
- `candidate.summary` is supported as a shortcut for `个人优势`; do not duplicate it if `sections` already contains that section.
- `candidate.gender`, `candidate.birth`, and `candidate.years_of_experience` may be rendered only when user-provided.
- Final resumes must not contain `[待确认]`; draft/checking files may contain it only when clearly labeled.

## Work vs Project Split

Work experience should state:

- role boundary,
- business or process context,
- important outputs,
- defensible result or impact.

Project experience should state:

- why the project existed,
- method, structure, workflow, or decision,
- challenge or tradeoff when real,
- result, adoption, or reusable output.

Avoid repeating the same metric, phrase, or claim across work and project sections. If both sections mention the same work, make them serve different purposes.

## Hollow Bullet Check

A bullet is likely hollow when it:

- starts with `负责`, `参与`, or `协助`;
- has no concrete scene, deliverable, result, method, customer/user, or scope;
- only lists responsibilities or tools.

Not hollow:

- `负责X，使用Y产出Z`.
- `参与X，完成Y交付物`.
- `协助X，将周期从A缩短到B` when the metric is defensible.

Use a weaker but concrete bullet rather than adding unverified metrics.

## Bullet Length and Density

- One bullet should usually carry one main idea.
- Split a bullet when it combines unrelated actions, multiple metrics, and multiple claims.
- For most resumes, keep core project bullets to `3+1`: background/goal, solution/action, result/impact, optional challenge/tradeoff.

## Date and Timeline Checks

Check:

- project dates fall within plausible job, school, or independent-work periods;
- full-time jobs do not overlap unless explained;
- very short tenure or gaps are acknowledged in risk notes when relevant.

Do not invent dates to repair a timeline. Ask, downgrade precision, or mark draft-only when needed.

## Package Consistency

Before delivery, compare:

- attachment resume,
- online paste version,
- platform scripts,
- interview answers,
- risk warning,
- modification notes.

They must share the same facts and claim strength. `修改说明.md` may only describe changes that actually appear in the final files.

## QA Script Use

Run:

```bash
python3 scripts/qa_check.py resume-data.json <rendered-md> --audit 证据审计与补充问题.md
```

Treat:

- `fatal`: fix before formal delivery, or change to draft/checking mode.
- `warning`: rewrite, downgrade, omit, or explain why it remains.

The script catches structural and explicit risks. It does not replace evidence judgment.
