# notebooklm-raw 数据目录说明

原始 NotebookLM 采集结果，与学习指南 `guides/` 分离。

## 目录结构

```
notebooklm-raw/
├── manifests/<module>.json       # 采集计划 → git
└── <module>/
    ├── knowledge-graph.md        # Phase 1.5 产出 → git
    ├── topics-map.md             # Agent 预拆分（可选）→ git
    └── runs/
        ├── latest → <canonical>  # 最近 completed run
        └── <timestamp>/
            ├── run.meta.json, run.log, manifest.snapshot.json
            ├── <batch>.prompt.txt, <batch>.answer.md   → git
            └── <batch>.answer.json                     → gitignore
```

## Git 策略

| 纳入 git | 不纳入 git |
|----------|-----------|
| `manifests/*.json`, `knowledge-graph.md` | `**/*.answer.json`（约为 .md 的 60 倍体积） |
| `*.prompt.txt`, `*.answer.md` | 失败/已合并的临时 run（直接删除，不写 gitignore） |
| `run.meta.json`, `run.log` | |

`.answer.md` 是 Agent 整合的唯一必要原始素材。

## 采集命令

见 `SKILL.md` Phase 1。脚本：`.cursor/skills/cg-course-notebooklm/scripts/nlm-collect.py`。

## raw 采集策略

raw 收集阶段的目标是**覆盖课程材料**，不是直接写出精炼指南。Agent 后续整合时可以压缩和取舍，但 manifest 设计必须尽量保证粒度完整、来源清楚、重点可追溯。

### Part 通用采集层级

| 顺序 | batch id 建议 | 采集对象 | 输出要求 |
|------|---------------|----------|----------|
| 1 | `overview-skeleton` | 相关 Week 课程记录 + 相关课件 | 全面列出本 Part 的大知识点、授课顺序、重要性、来源 |
| 2 | `concept-breakdown-<topic>` | `overview-skeleton` 中的大知识点 | 拆出子知识点；给基础解释、直觉入口、公式/管线位置 |
| 3 | `deep-dive-<topic>` | 核心、难点或易混主题 | 继续拆分子知识点，给详细解释、推导、图形直觉 |
| 4 | `examples-<topic>` | 课件、课本、Project 或可构思例题 | 获取或构思例题/示例，并逐步讲解 |
| 5 | `misconceptions-<topic>` | 易混概念、常见错误 | 对比表：为什么易混、正确理解、记忆方式 |
| 6 | `project-bridge` | Project、代码框架、考试复习 | 说明知识点如何落到代码、调试、作业或复习题 |

执行方式：

1. 先跑 `overview-skeleton`，读回回答后再设计 `concept-breakdown-*`；不要凭通用 CG 常识直接深采。
2. `concept-breakdown-*` 完成后，Agent 标注 `critical / important / normal`，只对需要深入的主题补 `deep-dive-*` 和 `examples-*`。
3. 整合时发现 raw 缺口，追加 `supplement-*` 或上述命名 batch，并用 `--only <batch-id> --resume runs/latest` 续跑。

### 课件专用采集

课件采集必须单独成组，prompt 要求 NotebookLM **仅限指定课件**，避免注意力分散到课堂记录、论文或其他周次。

| 顺序 | batch id 建议 | Prompt 必问 |
|------|---------------|-------------|
| 1 | `slide-skeleton-<slides>` | “请仅依据以下课件，按课件顺序说明分了几个主要模块、每个模块讲什么知识点、哪些最重要。” |
| 2 | `slide-module-detail-<slides>-<module>` | “请仅依据该课件的这个模块，详细说明每个知识点含义、课件如何讲、有哪些重要图片、示例或例题。” |
| 3 | `slide-examples-<slides>-<topic>` | “请仅依据该课件抽取例题/图片/伪代码；若课件没有完整例题，请明确说明并构思一个贴合课件的小例子。” |

课件 raw 可服务两类产物：

- 课件自身学习指南或 PPT 梳理索引；
- 分 Part 学习指南中的重点解释、图片口头化说明、例题和易混点。

## 整合流程

```
Phase 1    nlm-collect → runs/latest/
Phase 1.5  通读 *.answer.md → knowledge-graph.md
Phase 2-3  基础框架 → 补充 → 深挖 → Mermaid/串联 → 自审迭代
```

失败或已合并的 run 目录应**直接删除**，不要堆积。
