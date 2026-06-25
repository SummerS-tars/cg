# Week 3-4 / Part 2 Focus Map

> **生成时间**：2026-06-25  
> **输入 run**：`notebooklm-raw/week3-4/runs/20260625-224204`  
> **Stage 2 状态**：6/6 completed；从失败点续跑完成，`concept-breakdown-clip-ndc-viewport` 重试 2 次后成功。

## 1. 认知重点分级

| 主题 | 等级 | 已有 raw | 指南处理 |
|------|------|----------|----------|
| 几何变换(Geometric Transformation) 与齐次坐标(Homogeneous Coordinates) | critical | `concept-breakdown-geometric-transforms` | 作为 Part 2 起点，必须解释点/向量、`w`、4x4 矩阵和统一矩阵乘法 |
| 矩阵组合(Matrix Composition) 与变换顺序 | critical | `concept-breakdown-composition-hierarchy` | 需要视觉化“先旋转再平移”和“先平移再旋转”的差异，补可跟读数值例 |
| 层次结构(Transformation Hierarchy) / Scene Graph | important | `concept-breakdown-composition-hierarchy` | 作为矩阵链工程用途，压缩进变换章节 |
| 相机模型(Camera Model) 与观察变换(Viewing Transformation) | critical | `concept-breakdown-camera-view`、`slide-module-detail-lecture04-part2` | 需要补 look-at 构造、R/U/B 基向量、camera-to-world 求逆的直观解释 |
| 投影变换(Projection Transformation) | critical | `concept-breakdown-projection`、`slide-module-detail-lecture04-part2` | 需要补正交/透视对比、相似三角形、FOV/aspect/near/far 作用 |
| 裁剪空间(Clip Space)、透视除法(Perspective Division)、NDC、视口变换(Viewport Transformation) | critical | `concept-breakdown-clip-ndc-viewport`、`slide-module-detail-lecture04-part2` | 需要补一条从 View Space 到 Pixel Coordinates 的完整数值/视觉链 |
| 裁剪算法(Cohen-Sutherland / Sutherland-Hodgman) | normal | `concept-breakdown-clip-ndc-viewport`、`slide-module-detail-lecture04-part2` | 只解释为什么裁剪在视口前，算法细节了解即可 |
| 可编程管线(Programmable Pipeline) | normal | `slide-module-detail-lecture04-part2` | 只作为后续 Week 的承接，不展开 DirectX 版本细节 |

## 2. 难点与缺口

1. **变换顺序的视觉结果**：Stage 2 已说明矩阵不交换，但需要一个小点或小物体的可跟读例子，帮助读者避免只背公式。
2. **View Matrix 的逆向思维**：Stage 2 已给出 `camera-to-world` 再求逆，但指南需要把“移动相机”等价于“反向移动世界”讲透。
3. **投影后的空间链**：Stage 2 覆盖了 Clip Space、Perspective Division、NDC、Viewport，但需要串成一张完整管线图，并解释为什么在 Clip Space 裁剪。
4. **英语考试术语**：指南必须把 MVP、FOV、NDC、Clip Space、View Space、Viewport 等术语按中英格式解释。
5. **Markdown 表格安全**：对比表中避免未转义竖线；绝对值、矩阵、分段条件放入 LaTeX 或正文。

## 3. Stage 3 目标

Stage 3 不固定追问 misconceptions / project-bridge，只围绕 focus map 的 critical 难点补 deep-dive、examples 和 visual explanation：

1. `examples-transform-order-matrix-chain`：变换顺序、绕任意点旋转、父子矩阵链的数值/图形例。
2. `deep-dive-view-matrix-lookat`：相机基向量、look-at、view matrix 求逆和几何意义。
3. `deep-dive-projection-clip-ndc`：透视投影、Clip Space、Perspective Division、NDC 与 Viewport 的完整链路。
4. `visual-explain-mvp-pipeline`：把 Model/View/Projection 到像素的空间流动讲成可放入指南的图示与术语对照。

## 4. Optional Stage 4 判断

暂不生成 optional stage-4。当前 raw 已覆盖核心主题，后续是否补 `misconceptions-*` 或 `project-bridge` 应等 Stage 3 读完后再判断；若 Stage 3 已足够，直接进入 knowledge graph 和学习指南整合。
