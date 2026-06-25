# Week 7-9 / Part 4 Focus Map

> **生成时间**：2026-06-25  
> **输入 run**：`notebooklm-raw/week7-9/runs/20260625-234459`  
> **Stage 2 状态**：6/6 completed；`concept-breakdown-texture-filtering-applications` 因一次 GET_NOTEBOOK 连接失败重试 1 次后成功。

## 1. 认知重点分级

| 主题 | 等级 | 已有 raw | 指南处理 |
|------|------|----------|----------|
| 局部光照(Local Illumination) | critical | `concept-breakdown-local-shading-phong` | 作为 P4 起点，解释 fragment 可见后如何由法线、光源、视线和材质计算颜色 |
| Lambert / Phong / Blinn-Phong | critical | `concept-breakdown-local-shading-phong`、`source-skeleton-improved-illumination` | 需要公式、几何向量图、ambient / diffuse / specular 视觉效果 |
| Microfacet BRDF | critical | `concept-breakdown-microfacet-brdf`、`slide-skeleton-lecture07` | 解释 BRDF 输入输出、D/F/G、roughness、Fresnel，与 Phong 的关系 |
| Flat / Gouraud / Phong Shading | important | `concept-breakdown-shading-interpolation` | 用表格对比计算频率、插值对象、视觉质量、代价和缺陷 |
| Shader Data Flow | critical | `concept-breakdown-shader-data-flow` | 从 vertex attributes → rasterizer interpolation → fragment shader inputs → uniforms / textures → output color 画图 |
| Texture Mapping 基础 | critical | `concept-breakdown-texture-mapping-basics` | 解释 parameterization、UV、texture lookup、perspective-correct interpolation |
| Texture Filtering / Mipmaps / LOD | critical | `concept-breakdown-texture-filtering-applications` | 解释 aliasing、nearest、bilinear、mipmap、trilinear、LOD 直觉 |
| Texture Applications | important | `concept-breakdown-texture-filtering-applications`、`slide-skeleton-lecture08` | 对比 modulation、illumination、bump、normal、displacement、environment mapping |
| Visibility / HSR | compressed | `overview-skeleton` | 只作为 P3 承接，不重复 Z-buffer 大章 |

## 2. 难点与缺口

1. **光照公式的向量语义**：Stage 2 给出 $\vec n$、$\vec l$、$\vec v$、$\vec r$、$\vec h$，指南需要用图和公式说明每个向量如何影响颜色。
2. **Phong 与 Blinn-Phong 的关系**：需要明确 $\vec r \cdot \vec v$ 与 $\vec n \cdot \vec h$ 的差别，以及高光指数控制 glossy 程度。
3. **Microfacet BRDF 不宜讲成纯公式**：要把 $D/F/G$ 解释成“法线分布 / 角度反射 / 微遮挡”三种视觉现象。
4. **P3 到 P4 的数据流**：需要明确 interpolated attributes 属于 rasterizer 输出、fragment shader 输入；uniform / sampler 是 P4 额外输入。
5. **Texture Mapping 的 UV 范围排版噪声**：`concept-breakdown-texture-mapping-basics` 把 UV 通常取值范围写成 `$[8]$`，指南中应审计并改为 $[0,1]$。
6. **Filtering / Mipmap 的直觉**：需要用 footprint 与 $D=\log_2 L$ 说明为什么远处纹理要降采样。

## 3. Stage 3 目标

Stage 3 围绕 critical 难点补 deep-dive、examples 和 visual explanation：

1. `visual-explain-fragment-shading-pipeline`：把 P3 fragment 到 P4 color output 的数据流画成可放入指南的图示。
2. `deep-dive-phong-blinn-lighting-example`：补 Lambert / Phong / Blinn-Phong 的向量、公式、数值或视觉例。
3. `deep-dive-microfacet-brdf-visual`：补 BRDF 与 D/F/G 的视觉解释。
4. `compare-shading-interpolation-methods`：整理 Flat / Gouraud / Phong Shading 对比和缺陷。
5. `examples-texture-uv-filtering-applications`：补 UV、透视校正、filtering / mipmap、normal / bump / displacement / environment mapping 的例子。

## 4. Optional Stage 4 判断

暂不生成 optional stage-4。Stage 1-2 已覆盖 P4 主线；Project / GLSL 代码框架 source 未在 source list 中单独出现，因此不做 `project-bridge`。若用户后续上传 shader 代码或作业框架，再以 `supplement-*` 追加。
