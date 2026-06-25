# CG Week 3-4 内部 Review 与迭代记录

> **对象**：`guides/CG-Week3-4-学习指南.md`  
> **依据**：`notebooklm-raw/week3-4/knowledge-graph.md` 与 Stage 1-3 `*.answer.md`  
> **日期**：2026-06-25

## Draft 0：基础框架

按知识图谱建立章节：

1. 术语表
2. 知识地图
3. 几何变换与齐次坐标
4. 矩阵组合与层次结构
5. 相机与 View Matrix
6. 投影、Clip Space、NDC、Viewport
7. 重难点、串联与复习路线

## Draft 1：基础补充

- 从 Stage 2 raw 补齐每节基础解释：几何变换、齐次坐标、矩阵顺序、相机参数、投影分类、裁剪与视口。
- 将核心术语按英语考试格式写入术语表，例如 `NDC(Normalized Device Coordinates，规范化设备坐标)`、`MVP(Model-View-Projection，模型-观察-投影)`。
- 在核心章节末尾加入 `参考 raw` 引用块，避免最终指南末尾集中堆资料索引。

## Draft 2：重难点深挖

- 依据 Stage 3 raw 加入矩阵顺序例题、View Matrix 的“反向移动世界”解释、透视投影相似三角形推导、NDC 到视口公式。
- 对 Stage 3 `examples-transform-order-matrix-chain` 中明显异常的数值排版做了审计：不照抄原始坐标，改用 Agent 校正后的 LaTeX 点例；该偏差已记录在 `knowledge-graph.md`。
- 补充易混点：M/V/P 黑盒化、点/向量混淆、Projection 后直接当屏幕坐标、叉积顺序写反。

## Draft 3：可视化与串联

- 加入 3 张 Mermaid 图：Part 2 空间链、Projection → Pixel 链、Week 串联图。
- 复习路线按“画空间链 → 手推矩阵顺序 → 构造 View Matrix → 解释投影与 $w$ → 区分 Clip/NDC/Viewport”组织。
- DirectX / 可编程管线、Z-buffer 等 Stage 3 提到的后续内容只作为 Week 5 之后承接，不展开为 Part 2 主线。

## Review 1：新质量标准自检

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 术语首次解释 | 通过 | 核心术语均在术语表和正文首现附近解释 |
| 英语考试术语格式 | 通过 | 使用 `中文(English)` 或 `Abbr(Full English Name，中文对照)` |
| 数学表达 LaTeX | 通过 | 核心矩阵、向量、投影与 viewport 公式使用 LaTeX |
| 章节就近引用 | 通过 | 核心章节均有 `参考 raw` 块 |
| 最终指南无采集说明 | 通过 | 未加入 manifest、补采计划或 Step 4 说明 |
| Markdown 表格安全 | 通过 | 未使用会破坏表格的未转义竖线绝对值写法 |
| Mermaid 合理 | 通过 | Mermaid 只表达空间链和课程串联，不堆无关细节 |
| 课纲偏差标注 | 通过 | 课件04-05 的 Lecture05 内容压缩为后续承接 |

## Optional Stage 4 决策

不追加 optional stage-4。Stage 1-3 已覆盖核心骨架、模块展开、例题和视觉解释；进一步的 misconceptions 或 Project bridge 可在用户 Review 后按具体问题补采。

## 后续建议

- 用户 Review 时若希望面向考试，可追加一份独立练习题文档，重点覆盖矩阵顺序、look-at 构造、透视除法和 NDC/Viewport 映射。
- 若后续 Project 文档上传到 NotebookLM，再补采 Project 与 MVP 调试的关联 raw；该计划不进入最终学习指南。
