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

## raw 采集策略（v4.1 动态分层）

raw 收集阶段的目标是**覆盖课程材料**，不是直接写出精炼指南。Agent 后续整合时可以压缩和取舍，但 manifest 设计必须尽量保证粒度完整、来源清楚、重点可追溯。

### Multi-stage dynamic manifest

Part 采集不再一次性固定完整 batch 列表，而是“跑一层、读 raw、生成下一层”。每个阶段的 manifest 都要保存到 `notebooklm-raw/manifests/`，对应 run、summary 和 focus map 要落盘，保证后续能复现 Agent 当时为何追问。

| Stage | batch id 建议 | 采集对象 | 输出要求 |
|-------|---------------|----------|----------|
| 1 skeleton / slide-skeleton | `overview-skeleton`、`slide-skeleton-<slides>` | 相关 Week 课程记录 + 相关课件 | 全面列出本 Part / 课件原序大知识点、授课顺序、重要性、来源；少量固定总结类问题 |
| Agent gate | - | Stage 1 raw | 产出 `stage1-summary.md`，列出真实模块、source 匹配、偏差、缺失与 stage-2 manifest |
| 2 module expansion / concept breakdown | `concept-breakdown-<module>`、必要的 `slide-module-detail-*` | stage-1 发现的真实模块 | 拆出子知识点；给基础解释、直觉入口、公式/管线/坐标位置 |
| Agent gate | - | Stage 2 raw | 产出 `focus-map.md`，标注 critical / important / normal、难点、缺口与 stage-3 manifest |
| 3 targeted deep dive / examples / visual explanation | `deep-dive-<topic>`、`examples-<topic>`、`visual-explain-<topic>` | focus map 中的重点难点或高价值主题 | 深入解释、推导、图形直觉、示例/例题和视觉化说明 |
| Optional 4 | `misconceptions-<topic>`、`project-bridge`、`glossary-raw`、`supplement-*` | 仅限 stage-2/3 显示确有价值的主题 | 追加易混点、项目桥接、术语 raw 或缺口补采；在 review 记录追加理由 |

执行方式：

1. Stage 1 只放 `overview-skeleton` 与必要的 `slide-skeleton-*`。不要在最早固定 raw 中放 `misconceptions-*`、`project-bridge` 这类后置判断问题。
2. Agent 通读 stage-1 answers，把摘要和真实模块写入 `stage1-summary.md`，并把摘要显式写进 stage-2 manifest 的 metadata 或 prompt。
3. Stage 2 完成后，Agent 产出 `focus-map.md`，再生成 stage-3 manifest；不要依赖 NotebookLM chat history 记住上一轮。
4. Stage 3 只追问 focus map 中的重点难点或高价值 topics。Stage 4 仅按缺口追加。
5. 整合时发现 raw 缺口，追加 `supplement-*` 或上述命名 batch，并用新 manifest 或 `--only <batch-id> --resume runs/latest` 续跑。

### clear_conversation 原则

- 正式 batch 默认 `clear_conversation: true`，使每个回答成为独立、可追溯、可复现 raw 样本，避免历史上下文污染。
- 上一轮结果由 Agent 摘要后显式写入下一轮 prompt 或 manifest metadata，例如 `stage_input_summary`、`stage1_summary_ref`、`focus_map_ref`。
- 探索性连续追问可以 `clear_conversation: false`，但必须标记 `exploratory: true`，并在 run/review 中说明“探索性，不作为最终可复现 raw 主路径”。需要进入主路径时，应重写为正式 batch 并清理上下文后重新采集。

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
Phase 1    stage manifest → nlm-collect → stage summary/focus map → next manifest
Phase 1.5  通读 *.answer.md → knowledge-graph.md
Phase 2-3  基础框架 → 补充 → 深挖 → Mermaid/串联 → 自审迭代
```

失败或已合并的 run 目录应**直接删除**，不要堆积。
