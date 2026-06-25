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

## 整合流程

```
Phase 1    nlm-collect → runs/latest/
Phase 1.5  通读 *.answer.md → knowledge-graph.md
Phase 2-3  → guides/CG-Week*-学习指南.md
```

失败或已合并的 run 目录应**直接删除**，不要堆积。
