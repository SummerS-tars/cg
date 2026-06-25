# Week 12-14 / Part 6 Review Iteration

## 内部 Review 1：主线完整性

- 检查结果：P6 raw 覆盖 ray tracing、AABB/BVH、rendering equation、Monte Carlo path tracing、sampling optimization、denoising / DLSS。
- 处理：指南按“Whitted ray tracing -> acceleration -> rendering equation -> path tracing -> optimization -> real-time denoising”组织。
- Shadow map 不作为主章，避免超出 raw 主线。

## 内部 Review 2：公式与直觉

- 渲染方程必须逐项解释，不只贴公式。
- Monte Carlo estimator、SPP、variance、Russian Roulette 的概率补偿必须使用 LaTeX 并解释视觉意义。
- BVH 用小场景例子解释剔除逻辑。

## 内部 Review 3：术语与考试格式

- 首次出现术语使用 `中文(English)` 或 `Abbr(Full English Name，中文对照)`。
- 重点术语：Ray Tracing、Path Tracing、GI、BRDF、AABB、BVH、TLAS、BLAS、PDF、SPP、RR、NEE、DLSS、G-buffer。

## 内部 Review 4：最终整合检查

- 每个主体章节就近放 `参考 raw`。
- Mermaid 至少包含 ray tracing 管线和实时去噪流程。
- 表格避免竖线数学表达；路径类型使用代码或 LaTeX 安全呈现。
- 最终指南不包含采集计划或补采说明。
