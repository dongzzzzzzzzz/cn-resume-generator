#!/usr/bin/env python3
"""Lightweight QA checks for rendered Chinese resume Markdown.

The script is intentionally heuristic. It catches structural mistakes and
explicitly forbidden claims; it does not replace evidence judgment.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class CheckResult:
    level: str
    code: str
    message: str


def _text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _candidate(data: dict[str, Any]) -> dict[str, Any]:
    return data.get("candidate") or data.get("profile") or {}


def _is_draft(data: dict[str, Any], markdown_path: Path) -> bool:
    mode = _text(data.get("delivery_mode") or data.get("mode") or data.get("交付模式"))
    name = markdown_path.name
    return any(token in mode or token in name for token in ["草稿", "校对", "draft", "Draft"])


def _section_titles(md: str) -> set[str]:
    return {m.group(1).strip() for m in re.finditer(r"^##\s+(.+?)\s*$", md, re.M)}


def _section_bullets(md: str) -> dict[str, list[str]]:
    current = ""
    sections: dict[str, list[str]] = {}
    for line in md.splitlines():
        heading = re.match(r"^##\s+(.+?)\s*$", line)
        if heading:
            current = heading.group(1).strip()
            sections.setdefault(current, [])
            continue
        bullet = re.match(r"^\s*[-•]\s+(.+?)\s*$", line)
        if bullet and current:
            sections.setdefault(current, []).append(bullet.group(1).strip())
    return sections


def _normalize_chars(text: str) -> set[str]:
    return {ch for ch in text if re.match(r"[\w\u4e00-\u9fff]", ch)}


def _jaccard(a: str, b: str) -> float:
    left = _normalize_chars(a)
    right = _normalize_chars(b)
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def _extract_metrics(text: str) -> list[str]:
    patterns = [
        r"\d+(?:\.\d+)?%",
        r"\d+(?:\.\d+)?\+",
        r"\d+(?:\.\d+)?\s*(?:万|千|百|元|天|小时|分钟|人|个|条|次|家|分)",
        r"从[^，。；\n]{1,24}?(?:提升|降低|缩短|增长|减少|优化)至[^，。；\n]{1,24}",
    ]
    found: list[str] = []
    for pattern in patterns:
        found.extend(re.findall(pattern, text))
    return found


def _load_audit_claims(path: Path | None) -> tuple[list[str], list[str]]:
    if not path or not path.exists():
        return [], []
    text = path.read_text(encoding="utf-8")
    forbidden: list[str] = []
    downgrade: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        match_forbid = re.search(r"禁止[：:]\s*(.+)", stripped)
        if match_forbid:
            phrase = match_forbid.group(1).strip()
            if phrase:
                forbidden.append(phrase)
        match_strong = re.search(r"强表达[：:]\s*(.+)", stripped)
        if match_strong:
            phrase = match_strong.group(1).strip()
            if phrase:
                downgrade.append(phrase)
    return forbidden, downgrade


def check_summary(data: dict[str, Any], md: str) -> list[CheckResult]:
    cand = _candidate(data)
    summary = cand.get("summary") or data.get("summary")
    if summary and "## 个人优势" not in md:
        return [CheckResult("fatal", "missing-summary", "candidate.summary exists but rendered Markdown has no 个人优势 section.")]
    return []


def check_pending_markers(data: dict[str, Any], md: str, markdown_path: Path) -> list[CheckResult]:
    if "[待确认]" in md and not _is_draft(data, markdown_path):
        return [CheckResult("fatal", "pending-marker", "Formal-looking resume contains [待确认]. Use draft/checking mode or remove it.")]
    return []


def check_core_sections(md: str) -> list[CheckResult]:
    titles = _section_titles(md)
    if not ({"工作经历", "项目经历", "教育经历"} & titles):
        return [CheckResult("fatal", "missing-core-section", "Rendered resume has no 工作经历, 项目经历, or 教育经历 section.")]
    return []


def check_contact(data: dict[str, Any], md: str) -> list[CheckResult]:
    cand = _candidate(data)
    results: list[CheckResult] = []
    for key, label in [("phone", "phone"), ("email", "email")]:
        value = _text(cand.get(key))
        if value and value not in md:
            results.append(CheckResult("fatal", "contact-not-rendered", f"Candidate {label} exists in data but is not rendered."))
        if not value:
            results.append(CheckResult("warning", "contact-missing", f"Candidate {label} is missing."))
    for key, label in [
        ("gender", "gender"),
        ("birth", "birth"),
        ("years_of_experience", "years_of_experience"),
    ]:
        value = _text(cand.get(key))
        if value and value not in md:
            results.append(CheckResult("fatal", "contact-not-rendered", f"Candidate {label} exists in data but is not rendered."))
    return results


def check_overlap(sections: dict[str, list[str]]) -> list[CheckResult]:
    results: list[CheckResult] = []
    work = sections.get("工作经历", [])
    projects = sections.get("项目经历", [])
    for left in work:
        for right in projects:
            score = _jaccard(left, right)
            if score >= 0.60:
                results.append(CheckResult("warning", "bullet-overlap", f"Work/project bullets look similar ({score:.2f}): {left[:36]} / {right[:36]}"))
    return results


def check_repeated_metrics(sections: dict[str, list[str]]) -> list[CheckResult]:
    seen: dict[str, str] = {}
    results: list[CheckResult] = []
    for bullets in sections.values():
        for bullet in bullets:
            for metric in _extract_metrics(bullet):
                if metric in seen and seen[metric] != bullet:
                    results.append(CheckResult("warning", "repeated-metric", f"Metric appears in multiple bullets: {metric}"))
                else:
                    seen[metric] = bullet
    return results


def check_hollow_bullets(sections: dict[str, list[str]]) -> list[CheckResult]:
    result_words = "提升|降低|缩短|增长|减少|优化|完成|产出|交付|发现|解决|建立|搭建|设计|上线|落地|转化|回款|准确率|效率|成本|周期|满意度|覆盖"
    results: list[CheckResult] = []
    for section, bullets in sections.items():
        if section not in {"工作经历", "项目经历", "实习经历", "校园经历"}:
            continue
        for bullet in bullets:
            starts_hollow = re.match(r"^(负责|参与|协助)", bullet)
            has_result = re.search(result_words, bullet) or re.search(r"\d", bullet)
            if starts_hollow and not has_result:
                results.append(CheckResult("warning", "hollow-bullet", f"Bullet may be responsibility-only: {bullet[:70]}"))
    return results


def check_long_bullets(sections: dict[str, list[str]]) -> list[CheckResult]:
    results: list[CheckResult] = []
    for bullets in sections.values():
        for bullet in bullets:
            if len(bullet) > 140:
                results.append(CheckResult("warning", "long-bullet", f"Bullet is long and may be overloaded ({len(bullet)} chars): {bullet[:60]}"))
    return results


def check_audit_claims(md: str, audit_path: Path | None) -> list[CheckResult]:
    forbidden, downgrade = _load_audit_claims(audit_path)
    results: list[CheckResult] = []
    for phrase in forbidden:
        if phrase and phrase in md:
            results.append(CheckResult("fatal", "forbidden-claim", f"Forbidden audit phrase appears in final resume: {phrase}"))
    for phrase in downgrade:
        if phrase and phrase in md:
            results.append(CheckResult("warning", "downgrade-claim", f"Audit marked this expression for downgrade but it appears in final resume: {phrase}"))
    return results


def run_checks(data_path: Path, markdown_path: Path, audit_path: Path | None) -> list[CheckResult]:
    data = json.loads(data_path.read_text(encoding="utf-8"))
    md = markdown_path.read_text(encoding="utf-8")
    sections = _section_bullets(md)
    results: list[CheckResult] = []
    results.extend(check_summary(data, md))
    results.extend(check_pending_markers(data, md, markdown_path))
    results.extend(check_core_sections(md))
    results.extend(check_contact(data, md))
    results.extend(check_overlap(sections))
    results.extend(check_repeated_metrics(sections))
    results.extend(check_hollow_bullets(sections))
    results.extend(check_long_bullets(sections))
    results.extend(check_audit_claims(md, audit_path))
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Run lightweight QA checks on rendered resume Markdown.")
    parser.add_argument("data_json", type=Path)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--audit", type=Path, default=None)
    args = parser.parse_args()

    results = run_checks(args.data_json, args.markdown, args.audit)
    fatal_count = sum(1 for result in results if result.level == "fatal")
    warning_count = sum(1 for result in results if result.level == "warning")

    if not results:
        print("QA PASS: no fatal or warning findings.")
        return 0

    for result in results:
        print(f"{result.level.upper()} [{result.code}] {result.message}")
    print(f"QA SUMMARY: {fatal_count} fatal, {warning_count} warning")
    return 1 if fatal_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
