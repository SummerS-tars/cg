# Week 10-11 / Part 5 Review Iteration

## 内部 Review 1：范围校准

- 检查结果：P5 raw 不支持完整曲线曲面 / mesh processing 理论课。
- 处理：指南主体改为“模型加载、场景标准、GLTF/PBR 过渡、几何表示概览”，并把 Bezier、B-spline、half-edge、QEM、Catmull-Clark 等列为缺口 / 扩展。
- 风险控制：不在最终指南中保留采集计划或补采说明，只在“资料边界”中说明 raw 支撑范围。

## 内部 Review 2：术语与考试格式

- 首次出现术语使用 `中文(English)` 或 `Abbr(Full English Name，中文对照)`。
- 重点术语：GLTF、GLB、USD、PBR、BRDF、UV、VB、IB、BVH、TLAS、BLAS。
- 几何表示表格避免未转义竖线；数学符号使用 LaTeX。

## 内部 Review 3：叙事与引用

- 每个主体章节就近放 `参考 raw`，避免末尾堆 raw 索引。
- Mermaid 至少包含模型数据流图。
- 易混点：PBR 解决“表面如何反射”，GI 解决“光从哪里来”；P5 与 P6 分界需明确。

## 内部 Review 4：最终整合检查

- 保留：模型文件数据流、GLTF/PBR 例子、几何表示概览、资料边界。
- 压缩：传统曲线曲面数学推导。
- 删除：采集计划、补采计划、manifest 说明。
