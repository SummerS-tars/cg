# CG Week 1-2 内部 Review 与迭代记录

> **对象**：`guides/CG-Week1-2-学习指南.md`  
> **依据**：`notebooklm-raw/week1-2/knowledge-graph.md` 与 `runs/latest/*.answer.md`  
> **日期**：2026-06-25

## Draft 0：基础框架

按 `knowledge-graph.md` 的认知阶梯建立章节：

1. 术语表
2. 知识地图
3. CG 学科与应用
4. 渲染管线
5. 扫描转换
6. 数学语言
7. 重难点与串联

## Review 1：发现的问题

| 问题 | 风险 | 处理 |
|------|------|------|
| 原规划容易把 P1 写成“总览 + 数学基础”，弱化 Week 2 扫描转换 | 与 raw 不一致，遗漏 Bresenham、DDA、曲线、多边形填充 | 将扫描转换提升为核心章节 `2.3` |
| raw 中关于矩阵/齐次坐标与课件02存在来源差异 | 误导读者以为 Lecture02 已完整推导矩阵 | 在 `2.4` 增加课纲注，明确这是 Week 2 笔记/后续承接 |
| 管线术语容易停留在定义 | 读者无法调试片元、framebuffer、深度测试问题 | 加入三角形数据流和“片元不是像素”追问块 |
| DDA/Bresenham 对比缺少可操作公式 | 学习指南变成概念对比，不能复习算法 | 加入决策参数公式和更新规则 |
| Project 信息不足 | 可能编造作业细则 | 只写 raw 可确认的环境搭建、AI 互动记录、复习落点，并标注缺 Project 文档 |

## Draft 1：迭代后的关键改动

- 新增 Mermaid 管线图、坐标空间链路图、知识地图图。
- 将 `misconceptions-part1` 整合为易混点表和重难点解释。
- 将 `examples-pipeline-and-math` 改写为 Bresenham 可复习公式，不直接粘贴 raw。
- 增加 3 个固定块：`追问：为什么第一周讲应用第二周讲画线`、`直观理解：片元不是像素`、`追问：为什么不用普通坐标直接写 x+tx`。
- 改为在核心章节附近使用简短 `参考 raw` 引用块；完整 raw 映射保留在 `knowledge-graph.md` 与本 review 文档，不再放入最终指南末尾大表。

## 用户 Review 反馈回补：术语、引用与最终指南边界

用户指出初版指南存在以下质量问题，并已回补到 `guides/CG-Week1-2-学习指南.md` 与 workflow 规范：

| 反馈 | 风险 | 已处理 |
|------|------|--------|
| `DDA` 与 `Bresenham` 首次出现未解释，术语表缺失 | 读者第一次见算法名时无法建立概念；英语考试也缺术语对照 | 补充 `DDA(Digital Differential Analyzer，数字微分分析器)` 与 `Bresenham 直线算法(Bresenham Line Algorithm)` 的术语表条目和正文首现解释 |
| 最后集中“资料索引”表过长 | 学习时来源与知识点脱节 | 移除最终指南末尾资料索引，改为各核心章节末尾 `参考 raw` 引用块 |
| `Step 4 补充采集说明` 出现在最终指南 | 混淆学习指南与采集计划 | 从最终指南移除，补采建议迁移到本 review 文档 |
| Markdown 表格中 `|m|` 破坏渲染 | 表格列被错误拆分 | 改写为 `abs(m)`，并将表格竖线检查加入 checklist |
| 期末为英语考试 | 缺少中英术语对照 | 术语表和正文首现改用 `中文(English)` / `Abbr(Full English Name，中文对照)` 格式 |

新增自检点：

1. 正文首次出现的专业术语、算法名、缩写、坐标空间和矩阵名必须解释并进入术语表。
2. 核心知识章节附近必须有简短 `参考 raw` 引用块。
3. 最终指南不得包含补采计划、manifest 计划或长篇 raw 索引。
4. Markdown 表格内避免未转义 `|`；绝对值条件写成 `abs(m)`。

## Review 2：Checklist 自检

| 检查项 | 状态 | 说明 |
|--------|------|------|
| Phase 1 completed | 通过 | `run.meta.json` 为 completed，12/12 ok |
| Phase 1.5 知识图谱 | 通过 | 已生成 `knowledge-graph.md` |
| 大模块全景节 | 通过 | `知识地图` 与每个核心小节的叙事线提供全景 |
| Mermaid/ASCII 图 | 通过 | 3 张 Mermaid 图 |
| 易混对比 | 通过 | DDA/Bresenham、主步进轴、扫描线/区域填充、点/向量等 |
| 追问/直观理解块 | 通过 | 3 处 |
| 术语首现解释与英文对照 | 通过 | 补充 DDA、Bresenham、Shader、Depth Test、MVP 等术语 |
| 来源可追溯 | 通过 | 核心章节就近 `参考 raw`；完整映射保留在知识图谱 |
| 最终指南无采集计划 | 通过 | `Step 4 补充采集说明` 已移出最终指南 |
| Markdown 表格安全 | 通过 | `|m|` 已改写为 `abs(m)` |
| 课纲偏差标注 | 通过 | 标注课件02未完整讲矩阵/齐次坐标 |
| Project 细节 | 有缺口 | 缺独立 Project/评分文档，未补采 |

## 后续建议

- 用户确认 Project/作业文档上传后，补采 `supplement-project-rubric-part1`。
- 若要面向考试训练，补采或手工构造完整 Bresenham 决策参数表。

## 采集计划存放说明

以下内容不进入最终学习指南，只作为 raw / review 层面的后续计划：

- 若用户确认 Project/作业文档已上传到 NotebookLM，可补采 `supplement-project-rubric-part1`，用于把 Project 评分要求与 Week 1-2 基础概念对齐。
- 若用户需要更强考试训练，可补采 `supplement-bresenham-numeric-example`，获取完整决策参数表；在未补采前，指南只保留当前 raw 支撑的公式和直觉说明。
