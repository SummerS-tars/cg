# CG 本学期 Part 总览（Phase 0 盘点）

> **课程**：计算机图形学（Computer Graphics）  
> **依据**：`guides/CG课程-16周内容梳理.md` 的待校准 16 周框架  
> **盘点日期**：2026-06-25  
> **状态**：本文件是采集规划与同步状态矩阵；2026-06-25 已确认 CG Notebook UUID 与 source list，P1 / `week1-2` 已完成 raw、knowledge graph、学习指南与内部 review。

---

## Part 分层（待真实资料校准）

按 CG 课程常见认知路线划分 7 个采集/整合 Part。真实周次、Project 节点和考试重点到位后，应以课程记录与课件为准修订。

| Part | module 目录 | 覆盖周次 | 主题 | 主要资料期望 | 指南目标 |
|------|-------------|----------|------|--------------|----------|
| **P1** | `week1-2` | W1–W2 | 图形学总览 + 数学基础 | 课程大纲、W1/W2 记录、数学基础课件 | `guides/CG-Week1-2-学习指南.md` |
| **P2** | `week3-4` | W3–W4 | 变换 / 相机 / 投影 | 变换、相机、投影课件与例题 | `guides/CG-Week3-4-学习指南.md` |
| **P3** | `week5-6` | W5–W6 | 光栅化 / 可见性 / 采样 | 光栅化、深度、抗锯齿课件与 Project 说明 | `guides/CG-Week5-6-学习指南.md` |
| **P4** | `week7-9` | W7–W9 | 着色 / 光照 / 纹理 | 光照模型、GLSL、纹理课件与代码框架 | `guides/CG-Week7-9-学习指南.md` |
| **P5** | `week10-11` | W10–W11 | 几何建模 / 曲线曲面 / 网格 | 曲线曲面、mesh、模型加载资料 | `guides/CG-Week10-11-学习指南.md` |
| **P6** | `week12-14` | W12–W14 | 高级渲染 / 光线追踪 / 全局光照 | shadow map、ray tracing、path tracing 资料 | `guides/CG-Week12-14-学习指南.md` |
| **P7** | `week15-16` | W15–W16 | 项目整合 / 复习展示 | Project 文档、评分标准、复习范围 | `guides/CG-Week15-16-学习指南.md` |

### Part 内采集层级（v4）

每个 Part 的 manifest 不应只写几个大问题，而要按“覆盖 → 拆分 → 深挖 → 示例 → 串联”设计 batch。raw 阶段覆盖优先于精炼，指南阶段再按重要程度压缩。

| 层级 | 必要性 | batch id 建议 | 说明 |
|------|--------|---------------|------|
| 全面骨架 | 必做 | `overview-skeleton` | NotebookLM 综合相关 Week 记录和课件，列出大知识点、授课顺序、重要性和来源 |
| 知识点拆分 | 必做 | `concept-breakdown-<topic>` | 对骨架中的每个大知识点拆子知识点，给基础解释、直觉和管线位置 |
| 重点深挖 | 按需 | `deep-dive-<topic>` | 对核心/难点/易混点继续拆分，补详细解释、推导、直观理解 |
| 示例例题 | 按需 | `examples-<topic>` | 从课件、教材、Project 中抽取例题；没有现成例题时明确构思依据 |
| 课件骨架 | 重要课件必做 | `slide-skeleton-<slides>` | 仅限指定课件，按课件顺序梳理模块、知识点和重点 |
| 课件模块详解 | 按需 | `slide-module-detail-<slides>-<module>` | 仅限指定课件，讲模块内知识点、重要图片、示例、例题 |
| 易混点 | 推荐 | `misconceptions-<topic>` | 易混概念、常见错误、记忆方式 |
| 项目桥接 | 推荐 | `project-bridge` | 串联前后周、渲染管线、Project/考试复习 |

课件采集 prompt 必须写明“仅限以下课件”，防止 NotebookLM 把课堂记录、论文或其他周次混入课件梳理。

### 叙事链（Part 间承接）

```text
P1 管线地图和数学语言
  → P2 用矩阵、相机和投影把 3D 放进屏幕空间
  → P3 用光栅化、深度和采样把几何变成片元
  → P4 用 shader、光照和纹理决定像素外观
  → P5 用曲线曲面和 mesh 构造更复杂几何
  → P6 用阴影、光线追踪和全局光照提升真实感
  → P7 回到 Project、展示和考试总复习
```

---

## 本地资料对齐

| 类别 | 本地状态 | NotebookLM 期望 | 当前动作 |
|------|----------|-----------------|----------|
| 课程大纲 | 未发现 | `课纲-计算机图形学` | 需要用户提供本地路径或上传状态 |
| 课件 PDF | 未发现 | `课件01-*` … `课件NN-*` | 需要用户提供课件目录 |
| 课程记录 W1–W16 | 未发现 | `笔记-week01-CG` … `笔记-week16-CG` | 需要从邮箱/FiCS/iCourse 导出并核对停课周 |
| Project / 作业文档 | 未发现 | `Project-*`、`Assignment-*` | 需要用户提供文档和评分要求 |
| NotebookLM source list | 已验证：CG Notebook `c46f03a0-be2e-4cbb-8172-24a3ee0fce88`，29 个 source 均 `ready` | 与上述标题逐项一致 | 详见 `notebooklm-raw/capability-check.md`；后续按 manifest 逐 Part 对齐 source |
| raw 采集结果 | P1 已完成 | `notebooklm-raw/week1-2/runs/latest/*.answer.md` | 后续 Part 待 manifest 创建与采集 |

> **重要**：当前仓库只有采集工具和规范，不包含可据以定稿的课程原文。所有 Part 的主题与周次均为采集规划，不是已验证课表。

---

## 流水线进度矩阵

| Part | manifest | topics-map | raw 采集 | knowledge-graph | 学习指南 |
|------|----------|------------|----------|-----------------|----------|
| P1 `week1-2` | 已创建 | 已生成 | 已采集 12/12 | 已生成 | 已写用户 Review 前版本 |
| P2 `week3-4` | 待创建 | 未生成 | 未采集 | 未生成 | 待写 |
| P3 `week5-6` | 待创建 | 未生成 | 未采集 | 未生成 | 待写 |
| P4 `week7-9` | 待创建 | 未生成 | 未采集 | 未生成 | 待写 |
| P5 `week10-11` | 待创建 | 未生成 | 未采集 | 未生成 | 待写 |
| P6 `week12-14` | 待创建 | 未生成 | 未采集 | 未生成 | 待写 |
| P7 `week15-16` | 待创建 | 未生成 | 未采集 | 未生成 | 待写 |

---

## NotebookLM Source 对齐（已完成能力检查，待逐 Part 对齐）

当前已验证 Notebook：`c46f03a0-be2e-4cbb-8172-24a3ee0fce88`（计算机图形学 Notebook）。远端 source list 返回 29 个 `ready` source，包括 Week 1/2/3/4/5/7/8/9/11/12/13/14/15 课堂笔记、课件 01–09 与若干渲染/路径追踪论文。下面是建议的 Part 对齐表，仍需结合真实课表确认停课周、Project/作业资料是否已补齐。

| Part | 建议 Source |
|------|-------------|
| P1 | `课纲-计算机图形学`、`笔记-week01-CG`、`笔记-week02-CG`、总览/数学基础课件 |
| P2 | `笔记-week03-CG`、`笔记-week04-CG`、变换/相机/投影课件 |
| P3 | `笔记-week05-CG`、`笔记-week06-CG`、光栅化/深度/采样课件、相关 Project 文档 |
| P4 | `笔记-week07-CG`、`笔记-week08-CG`、`笔记-week09-CG`、着色/光照/纹理课件、shader 代码框架 |
| P5 | `笔记-week10-CG`、`笔记-week11-CG`、曲线曲面/mesh 课件 |
| P6 | `笔记-week12-CG`、`笔记-week13-CG`、`笔记-week14-CG`、高级渲染/光线追踪课件 |
| P7 | `笔记-week15-CG`、`笔记-week16-CG`、Project 说明、展示/复习范围 |

认证与 source 对齐建议按本仓库 skill 执行：

```bash
export HTTPS_PROXY=http://127.0.0.1:7897 HTTP_PROXY=http://127.0.0.1:7897
export https_proxy=http://127.0.0.1:7897 http_proxy=http://127.0.0.1:7897
python3 ~/service/openclaw/workspace/skills/notebooklm-integration/scripts/sync-auth.py --force
python3 ~/service/openclaw/workspace/skills/notebooklm-integration/scripts/sync-auth.py --check
notebooklm use c46f03a0-be2e-4cbb-8172-24a3ee0fce88
notebooklm source list
```

> Agent 不应在 WSL 中执行 `notebooklm login` 或触发 Windows 浏览器登录；需要用户先在 Windows 侧完成登录，再同步认证。

---

## 建议采集顺序

1. **Phase 0：真实资料盘点**  
   补齐课程资料根目录、课件列表、Week 记录、Project 文档，并更新 `guides/CG课程-16周内容梳理.md`。

2. **Phase 1：Part 骨架采集**  
   先为目标 Part 创建 `overview-skeleton`，让 NotebookLM 对相关 Week 记录和课件做全面内容骨架梳理。

3. **Phase 1：分 Part 分层深采**  
   根据骨架回答创建 `concept-breakdown-*`；再为核心/难点补 `deep-dive-*`、`examples-*`、`misconceptions-*`、`project-bridge`。

4. **Phase 1：课件专用采集**  
   对目标 Part 的重要课件增加 `slide-skeleton-*` 和 `slide-module-detail-*`，仅限课件来源，按课件原序覆盖图片、示例和例题。

5. **Phase 1.5：知识图谱**  
   通读 `runs/latest/*.answer.md`，生成 `notebooklm-raw/<module>/knowledge-graph.md`。

6. **Phase 2–3：学习指南内部迭代**  
   按认知顺序写 `guides/CG-Week*-学习指南.md`，执行“基础框架 → 基础补充 → 重难点深挖 → Mermaid/串联 → 自审迭代”，不要按 raw 拼接。

---

*Phase 0 产出；真实资料到位后，本文件应成为 manifest、raw、knowledge-graph 与学习指南的进度总表。*
