# CG Week 5-6 内部 Review 与迭代记录

> **对象**：`guides/CG-Week5-6-学习指南.md`  
> **依据**：`notebooklm-raw/week5-6/knowledge-graph.md` 与 Stage 1-3 `*.answer.md`  
> **日期**：2026-06-25

## Draft 0：基础框架

按知识图谱建立章节：

1. 术语表
2. 知识地图
3. 投影后管线、裁剪与视口
4. 扫描转换 / 光栅化
5. 可编程管线边界
6. Hidden Surface Removal 与 Z-buffer
7. 算法对比、资料缺口与复习路线

## Draft 1：基础补充

- 从 Stage 2 raw 补齐 Clipping、Viewport Transformation、Scan Conversion、Programmable Pipeline、HSR 和 Z-buffer 的基础解释。
- 将核心术语按英语考试格式写入术语表，例如 `HSR(Hidden Surface Removal，隐藏面消除 / 消隐)`、`Z-buffer(Depth Buffer，深度缓冲)`、`BSP Tree(Binary Space Partitioning Tree，二叉空间剖分树)`。
- 在核心章节末尾加入 `参考 raw` 引用块，避免最终指南末尾集中堆资料索引。

## Draft 2：重难点深挖

- 依据 Stage 3 raw 加入 Projection 后管线 Mermaid、扫描线覆盖例题、Z-buffer 伪代码、同一像素两个 fragment 的深度测试例子。
- 对 Stage 2 `concept-breakdown-clipping-viewport` 中 Liang-Barsky 参数区间的排版噪声做审计：原回答出现 `$t \\in [11]$ [12]`，指南中改为正确的 $t \in [0,1]$。
- 将 A-buffer、BSP Tree、Scan-line、Area Subdivision 等作为算法族对比，不扩展为超过 raw 支持的大章。

## Draft 3：可视化与串联

- 加入 4 张 Mermaid 图：P2→P3 管线链、Clipping/NDC/Viewport 链、现代 GPU shader / fixed-function 边界、复习路线。
- 明确 P3 与 P4 的承接：P3 决定 fragment 是否能留下，P4 决定留下来的 fragment 是什么颜色。
- Week 6 笔记、Project 文档、Sampling / Anti-aliasing 缺口只作为资料边界说明，不写成采集计划。

## Review 1：质量标准自检

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 术语首次解释 | 通过 | 核心术语均在术语表和正文首现附近解释 |
| 英语考试术语格式 | 通过 | 使用 `中文(English)` 或 `Abbr(Full English Name，中文对照)` |
| 数学表达 LaTeX | 通过 | viewport mapping、扫描线交点、Z-buffer 例子使用 LaTeX |
| 章节就近引用 | 通过 | 核心章节均有 `参考 raw` 块 |
| 最终指南无采集说明 | 通过 | 未加入 manifest、补采步骤或 Step 4 说明 |
| Markdown 表格安全 | 通过 | 表格内未使用未转义竖线绝对值写法 |
| Mermaid 合理 | 通过 | Mermaid 表达空间链、管线边界和复习路线 |
| 课纲偏差标注 | 通过 | 明确 Week 6 / Project / Sampling raw 缺口 |

## Optional Stage 4 决策

不追加 optional stage-4。Stage 1-3 已覆盖当前 source 中可验证的核心主题；Sampling / Anti-aliasing 与 Project 细节缺口来自 source list 缺失，强行追问容易得到跨周混合答案。后续若用户上传 Week 6 笔记或 Project 文档，可用 `supplement-*` 单独补采。

## 后续建议

- 用户 Review 时若需要考试练习，可追加独立题单，重点覆盖 viewport mapping、扫描线覆盖、Z-buffer 伪代码和 HSR 算法对比。
- 若后续补齐 Week 6 / Project source，再补采 MSAA、采样频率、抗锯齿与项目调试关联 raw。
