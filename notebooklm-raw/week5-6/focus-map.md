# Week 5-6 / Part 3 Focus Map

> **生成时间**：2026-06-25  
> **输入 run**：`notebooklm-raw/week5-6/runs/20260625-232714`  
> **Stage 2 状态**：6/6 completed；0 retry。

## 1. 认知重点分级

| 主题 | 等级 | 已有 raw | 指南处理 |
|------|------|----------|----------|
| 投影后管线后段(Post-projection Pipeline) | critical | `concept-breakdown-pipeline-after-projection` | 作为 Part 3 全景，承接 P2 的 Projection / NDC，串到 Clipping、Viewport、Rasterization、HSR |
| 裁剪(Clipping) 与视口变换(Viewport Transformation) | important | `concept-breakdown-clipping-viewport` | 解释为什么先裁剪再视口映射；保留 Cohen-Sutherland / Liang-Barsky 的直觉 |
| 扫描转换(Scan Conversion) / 光栅化(Rasterization) | critical | `concept-breakdown-scan-conversion-rasterization` | 需要补从连续图元到 fragment 的视觉链，包含 triangle coverage、scan-line、Bresenham、interpolation |
| 可编程管线(Programmable Pipeline) | important | `concept-breakdown-programmable-pipeline` | 作为工程背景；讲清 vertex shader、fixed-function rasterizer、fragment shader、output merger / depth test 的责任边界 |
| 消隐(Hidden Surface Removal, HSR) 分类 | critical | `concept-breakdown-hidden-surface-overview` | 用 object-space vs image-space 组织算法族，突出 back-face culling、painter、ray casting |
| Z-buffer(Depth Buffer，深度缓冲) | critical | `concept-breakdown-depth-buffer-algorithms` | 需要给出逐 fragment 深度比较伪流程、初始化、更新和局限 |
| A-buffer、BSP Tree、Scan-line、Area Subdivision | important/normal | `concept-breakdown-hidden-surface-overview`、`concept-breakdown-depth-buffer-algorithms` | 用对比表压缩，突出 A-buffer 处理 transparency / antialiasing 的动机 |
| Sampling / Anti-aliasing | gap | `concept-breakdown-depth-buffer-algorithms` 仅在 A-buffer 中提到 aliasing | 不作为 P3 主线大章；在资料缺口和后续建议中说明，不伪造 Week 6 raw |

## 2. 难点与缺口

1. **从 NDC 到 fragment 的空间链**：Stage 2 已解释 Clipping、Viewport、Rasterization，但指南需要一张完整图，说明每步的输入输出、坐标状态和责任边界。
2. **光栅化与消隐的交错关系**：Stage 2 把 HSR 放在 scan conversion 之前或期间，也提到 depth test 在 fragment 后、framebuffer 前；指南要明确“概念上为可见性问题，工程上常随光栅化/输出合并执行”。
3. **Z-buffer 的可跟读流程**：Stage 2 给出了初始化、比较、更新；需要补一个像素上两个三角形竞争的例子。
4. **算法族容易混淆**：Back-face Culling、Painter、Ray Casting、Z-buffer、BSP 的处理空间和适用场景不同，Stage 3 应补对比素材。
5. **Stage 2 raw 排版噪声**：`concept-breakdown-clipping-viewport` 把 Liang-Barsky 的 $t \in [0,1]$ 写成了 `$t \\in [11]$ [12]`；指南中应审计并改正。
6. **资料缺口**：未发现 Week 6 笔记 / Project 文档；采样与抗锯齿仅由 A-buffer 间接触及，无法按原计划扩展成完整大章。

## 3. Stage 3 目标

Stage 3 只围绕 focus map 的 critical 难点补 deep-dive、examples 和 visual explanation：

1. `visual-explain-post-projection-pipeline`：把 Projection 后到 framebuffer 前的管线讲成可放入指南的 Mermaid / 术语图。
2. `examples-rasterization-scanline-interpolation`：补 scan conversion、triangle coverage、scan-line、Bresenham 和插值的例题 / 直觉材料。
3. `deep-dive-zbuffer-depth-test`：深挖 Z-buffer / depth test 的逐像素流程、初始化、比较、更新和局限。
4. `compare-hidden-surface-algorithms`：整理 HSR 算法族对比，区分 object-space / image-space、适用场景、局限。

## 4. Optional Stage 4 判断

暂不生成 optional stage-4。Stage 1-2 已确认 P3 的 source 缺口来自 NotebookLM source list 本身；强行补 `sampling-antialiasing` 容易脱离 raw。若用户后续上传 Week 6 笔记、Project 文档或专门抗锯齿课件，再以 `supplement-*` 追加。
