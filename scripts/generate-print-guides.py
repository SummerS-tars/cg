#!/usr/bin/env python3
"""Generate compact print-friendly CG study guides.

The print edition keeps glossary, formulas, examples, diagrams and common
pitfalls, while removing source/process notes and review/navigation sections.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GUIDES_DIR = ROOT / "guides"
PRINT_DIR = GUIDES_DIR / "print"

SOURCE_FILES = [
    "CG-Week1-2-学习指南.md",
    "CG-Week3-4-学习指南.md",
    "CG-Week5-6-学习指南.md",
    "CG-Week7-9-学习指南.md",
    "CG-Week10-11-学习指南.md",
    "CG-Week12-14-学习指南.md",
    "CG-Week15-16-学习指南.md",
]

DROP_SECTION_KEYWORDS = [
    "本指南要回答的问题",
    "资料边界",
    "资料缺口",
    "知识串联",
    "复习路线",
    "复习 Checklist",
    "最后复习 Checklist",
    "与前后 Part",
    "期末怎么复习",
]

DROP_LINE_KEYWORDS = [
    "参考来源",
    "参考 raw",
    ".answer.md",
    "notebooklm-raw/",
    "review-iteration",
    "knowledge-graph",
    "manifest",
    "source list",
    "raw batch",
    "阶段摘要",
    "Agent 内部 Review",
    "用户 Review",
    "状态",
    "对应 Part",
    "课纲注",
    "本节叙事线",
    "本节要回答",
    "承接",
]


def heading_level(line: str) -> int | None:
    stripped = line.lstrip()
    if not stripped.startswith("#"):
        return None
    marks = len(stripped) - len(stripped.lstrip("#"))
    if marks == 0 or marks > 6:
        return None
    return marks if len(stripped) > marks and stripped[marks] == " " else None


def should_drop_section(line: str) -> bool:
    return any(keyword in line for keyword in DROP_SECTION_KEYWORDS)


def should_drop_line(line: str) -> bool:
    return any(keyword in line for keyword in DROP_LINE_KEYWORDS)


def compact_blank_lines(lines: list[str]) -> list[str]:
    compacted: list[str] = []
    blank = False
    for line in lines:
        is_blank = line.strip() == ""
        if is_blank and blank:
            continue
        compacted.append(line)
        blank = is_blank
    while compacted and compacted[-1].strip() == "":
        compacted.pop()
    compacted.append("")
    return compacted


def transform(text: str) -> str:
    output: list[str] = []
    skip_until_level: int | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        level = heading_level(line)

        if skip_until_level is not None:
            if level is not None and level <= skip_until_level:
                skip_until_level = None
            else:
                continue

        if level is not None and should_drop_section(line):
            skip_until_level = level
            continue

        if should_drop_line(line):
            continue

        if line.startswith("# "):
            line = line.replace("学习指南", "打印版", 1)

        output.append(line)

    return "\n".join(compact_blank_lines(output))


def write_readme(outputs: list[Path]) -> None:
    lines = [
        "# 计算机图形学学习指南打印版",
        "",
        "本目录为开卷翻阅准备，只保留术语、核心概念、公式、图示、例子、易混点和重要结论。",
        "",
        "删减规则：移除导读定位、采集与出处说明、跨章节导航、复习安排和练习式自检。",
        "",
        "## 文件列表",
        "",
    ]
    lines.extend(f"- [{path.name}](./{path.name})" for path in outputs)
    lines.append("")
    (PRINT_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    PRINT_DIR.mkdir(parents=True, exist_ok=True)

    outputs: list[Path] = []
    for source_name in SOURCE_FILES:
        source_path = GUIDES_DIR / source_name
        target_name = source_name.replace("学习指南", "打印版")
        target_path = PRINT_DIR / target_name
        target_path.write_text(transform(source_path.read_text(encoding="utf-8")), encoding="utf-8")
        outputs.append(target_path)

    write_readme(outputs)


if __name__ == "__main__":
    main()
