---
name: cg-course-notebooklm
description: >-
  计算机图形学课程按周学习资料流水线：设计 NotebookLM 单问 manifest、运行 nlm-collect
  采集落盘、通读 raw 产出知识图谱、叙事化整合学习指南。在用户提到 CG课程、计算机图形学、
  Week学习指南、NotebookLM采集、manifest、知识图谱、学习指南整合时使用。
---

# CG 课程 × NotebookLM 学习 Skill

> **课程**：计算机图形学（CG）  
> **Notebook**：`c46f03a0-be2e-4cbb-8172-24a3ee0fce88`（计算机图形学 Notebook；短前缀在 Python API 下会 RPC 失败）  
> **仓库根**：含 `notebooklm-raw/` 与 `guides/` 的项目目录

## 何时启用

- 新周次/新模块：设计 manifest → 采集 → 知识图谱 → 学习指南
- 补采：`supplement-*` batch 或 `--only` 续跑
- 整合迭代：Review 追问回写指南

**不启用**：纯概念答疑（无新周次产出）、与课程流水线无关的任务。

## 角色分工

| 角色 | 职责 |
|------|------|
| NotebookLM | 单问单答，标注来源 |
| `nlm-collect.py` | 认证、代理、采集、重试、落盘 |
| Agent | manifest、通读 raw、知识图谱、叙事整合、追问回写 |
| 用户 | Review、定稿、Windows 侧刷新认证 |

**原则**：raw 收集阶段覆盖优先于精炼，宁可多问骨架、拆分、例题和难点；指南整合阶段再按重要程度取舍。Agent 以 raw 为素材，必须补：全景节、空间/几何直觉、公式与矩阵含义、渲染管线图、易混对比、追问直观块。

## 六阶段流程

```
Phase 0   资料盘点（本地目录 + NotebookLM source 对齐）
Phase 1   分层采集（manifest + nlm-collect.py → notebooklm-raw/）
Phase 1.5 通读全部 *.answer.md → knowledge-graph.md  ★不可跳过
Phase 2   按图谱写 guides/CG-Week*-学习指南.md 基础框架
Phase 3   补充、重点深挖、Mermaid、内部 Review 迭代  ★不可跳过
Phase 4   用户 Review 迭代
Phase 5   定稿（checklist.md）
```

```mermaid
flowchart LR
    P0[Phase 0] --> P1[Phase 1 分层采集]
    P1 --> P15[Phase 1.5 知识图谱]
    P15 --> P2[Phase 2-3 指南内部迭代]
    P2 --> P4[Phase 4-5 迭代定稿]
```

## Phase 0：资料盘点

1. 对齐本地计算机图形学课件、课堂记录、作业/项目说明与 NotebookLM source list
2. 更新 `guides/CG课程-内容梳理.md` 进度
3. 标注缺失周次、缺失课件与作业关联

## Phase 1：采集

### 命令（在仓库根目录执行）

```bash
cd <repo>
export HTTPS_PROXY=http://127.0.0.1:7897 HTTP_PROXY=http://127.0.0.1:7897
NLM=.cursor/skills/cg-course-notebooklm/scripts/nlm-collect.py

# 预览
python $NLM notebooklm-raw/manifests/<module>.json --dry-run

# 完整采集
python $NLM notebooklm-raw/manifests/<module>.json --delay 8

# 续跑 / 补采
python $NLM notebooklm-raw/manifests/<module>.json \
  --resume notebooklm-raw/<module>/runs/latest

python $NLM notebooklm-raw/manifests/<module>.json \
  --only <batch-id> --resume notebooklm-raw/<module>/runs/latest

# 合并补采 run
python $NLM merge-runs <src_run> <dst_run>
```

### Manifest 设计原则

- **一个 batch = 一个 chat**（`clear_conversation: true`）
- **raw 覆盖优先**：先问全局骨架，再按骨架拆知识点，再深挖重点/难点；不要在采集阶段为了简短而跳过边角知识。
- **仍按 Part / module 组织**：每个 Part 独立 manifest、run、knowledge-graph；必要时为同一 Part 增加 `slides-*` 或 `supplement-*` batch。
- 复杂主题拆开（如变换矩阵 / 投影 / 光照模型 / 光栅化 / 纹理映射各一问）
- 字段：`id`, `layer`, `priority`, `title`, `prompt`, `clear_conversation`
- 模板：`templates/manifest-template.json`
- 范例路径：`notebooklm-raw/manifests/weekX-Y.json`

### Batch 命名与采集层级

| 层级 | batch id 建议 | 目标 |
|------|---------------|------|
| Part 骨架 | `overview-skeleton` | 让 NotebookLM 根据相关课程记录与课件列出完整内容骨架、大知识点和重要性 |
| 知识点拆分 | `concept-breakdown-<topic>` | 拆出大知识点下的子知识点，给基础解释和理解入口 |
| 重点深挖 | `deep-dive-<topic>` | 对核心/难点继续拆分子知识点，获取更详细、直观解释 |
| 示例例题 | `examples-<topic>` | 从课件、课本、Project 或 NotebookLM 可见资料中抽取/构思例题并讲解 |
| 课件骨架 | `slide-skeleton-<slides>` | 仅限相关课件，按课件顺序梳理模块、知识点和重点 |
| 课件模块详解 | `slide-module-detail-<slides>-<module>` | 仅限相关课件，逐模块讲含义、图片、示例、例题 |
| 易混点 | `misconceptions-<topic>` | 对比易混概念、常见错误和记忆方式 |
| 项目桥接 | `project-bridge` | 把知识点接到 Project、代码管线、考试或复习任务 |

### raw 获取顺序

1. **Part 骨架**：先问 `overview-skeleton`，要求 NotebookLM 综合相关 Week 课程记录和课件，全面列出本 Part 讲了哪些大知识点、顺序、重要性和资料来源。
2. **知识点拆分**：Agent 通读骨架回答后，为每个大知识点创建 `concept-breakdown-*` batch，要求 NotebookLM 拆子知识点并给基础解释。
3. **重点判断**：Agent 根据第 2 步 raw 判断核心/难点/易混点，补 `deep-dive-*`、`examples-*`、`misconceptions-*`、`project-bridge`。
4. **课件专用采集**：对重要课件单独建 `slide-skeleton-*` 与 `slide-module-detail-*`，prompt 必须写明“仅限以下课件”，防止 NotebookLM 混入其他资料。
5. **补采**：整合时发现缺口，再追加 `supplement-*` 或上述命名 batch，用 `--only` + `--resume` 续跑。

### Prompt 必含

中文；点名 Part、周次和课件编号；明确 source 范围；要求标注来源；L1 要几何/视觉直觉，L3 要矩阵、坐标或数值例；禁止一 prompt 多问。课件 prompt 必须包含“请仅依据/仅限以下课件”，并要求按课件顺序输出模块、重要图片、示例和例题。

### 采集产出

```
notebooklm-raw/<module>/runs/<ts>/
  run.meta.json, run.log, *.prompt.txt, *.answer.md
notebooklm-raw/<module>/runs/latest → 最近 completed run
```

完成判定：存在非空 `*.answer.md`。详见 `docs/raw-data.md`。

## Phase 1.5：知识图谱（必须先于指南正文）

1. **通读** `runs/latest/*.answer.md` 全部 batch
2. **审计**与课纲偏差（NotebookLM 可能混入其他周内容）
3. 产出 `notebooklm-raw/<module>/knowledge-graph.md`：

| 必填节 | 内容 |
|--------|------|
| 认知阶梯 | Mermaid flowchart，顺序≠采集顺序 |
| 节点清单 | 认知目标 \| batch \| 关键素材 \| Agent 须补充 |
| 叙事承接表 | 章节 \| 要回答 \| 承接 \| 引出 \| raw |
| batch→章节映射 | 整合深度标注 |
| 课纲审计 | 偏差说明 |

## Phase 2–3：整合学习指南

**详细规范**：`docs/integration-guide.md`（叙事、语言、Mermaid、文档结构）

**硬性要求**：

- 每个大模块（几何变换、投影、光照、光栅化、纹理、曲线曲面等）先有**全景节**（学什么、学完能做什么），再进公式
- 章级「叙事线」+ 节级「本节要回答」+ 小结→承接
- ≥3 张 Mermaid/ASCII 管线图，≥2 组易混对比表，≥3 处追问/直观理解块
- 公式和代码必须解释几何意义、坐标系位置、输入输出与常见误差
- 不得一次写完就交付：必须经历「基础框架 → 基础补充 → 重难点深挖 → 内部 Review → 迭代整合 → 再 Review」后，才进入用户 Review。

**产出**：`guides/CG-Week{N}-学习指南.md` 或 `guides/CG-Week{N-M}-学习指南.md`

## Phase 4：用户追问补充

Phase 4 是用户 Review，不替代 Agent 内部自审。用户看到前，Agent 应已完成至少一轮内部 Review 和迭代整合。

1. 追加 manifest batch：`supplement-<主题>`
2. `--only supplement-xxx --resume runs/latest`
3. 回写指南：`> **追问：**` / `> **直观理解：**` / 对比表 / 管线图

## Phase 5：定稿

跑 `docs/checklist.md`，更新 `guides/CG课程-16周内容梳理.md`，用户确认。

## 环境与排错

**认证 SOP（权威）**：`~/service/openclaw/workspace/skills/notebooklm-integration/docs/auth-sop.md`

见 `docs/troubleshooting.md`：认证、代理 `127.0.0.1:7897`、超时重试。

**能力检查记录**：`notebooklm-raw/capability-check.md`。2026-06-25 已复用 Windows 侧 storage，同步后 `sync-auth --check`、`notebooklm list --json`、CG Notebook `source list --json` 通过。

**Agent 禁止**：`notebooklm login`、WSL 浏览器、从 WSL 调 Windows 登录、`sync-auth --refresh`。

## 本 Skill 目录

```
.cursor/skills/cg-course-notebooklm/
├── SKILL.md
├── scripts/nlm-collect.py
├── docs/
│   ├── integration-guide.md
│   ├── raw-data.md
│   ├── checklist.md
│   └── troubleshooting.md
└── templates/
    └── manifest-template.json
```

## 禁止事项

- 未通读 raw / 未产出知识图谱就写指南
- 大模块无全景节直接推导
- 只粘贴 NotebookLM 输出不做叙事串联
- 一次 prompt 问整周内容
- Agent 在 WSL 尝试 `notebooklm login` 或浏览器登录（见 auth-sop.md）
- Agent 编造公式、图示或坐标推导不标注来源
