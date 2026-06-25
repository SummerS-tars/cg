# Week 10-11 / Part 5 Focus Map

> **生成时间**：2026-06-26  
> **输入 run**：`notebooklm-raw/week10-11/runs/20260626-001017`  
> **Stage 2 状态**：4/4 completed，0 retry；与 P6 stage-2 小并发运行，未降级串行。

## 1. 认知重点分级

| 主题 | 等级 | 已有 raw | 指南处理 |
|------|------|----------|----------|
| 模型加载与场景标准 | critical | `concept-breakdown-model-loading-standards` | 作为 P5 主线：OBJ / FBX / GLTF / GLB / USD 保存什么，如何进入渲染管线 |
| GLTF 场景加载与 PBR | critical | `concept-breakdown-gltf-pbr-bridge` | 解释 P5 作业线索：场景加载、材质、纹理、PBR 参数如何连接 |
| 顶点属性与 GPU 管线入口 | critical | `concept-breakdown-model-loading-standards` | 用数据流图说明 Position / Normal / UV / Material / Texture 到 shader / ray tracer |
| 几何表示概览 | important | `concept-breakdown-geometry-representations` | 做概念对比，不展开未见算法推导 |
| 曲线曲面 / mesh processing | gap | `gap-audit-curves-mesh-processing` | 明确“已覆盖 / 部分覆盖 / 未覆盖”，避免编造 Bezier、B-spline、half-edge 等细节 |
| PBR 到 GI 的过渡 | important | `concept-breakdown-gltf-pbr-bridge`、P6 raw | 作为 P5 结尾承接 P6，不在 P5 重写路径追踪 |

## 2. 难点与缺口

1. **Part 名义与 raw 覆盖不完全一致**：规划写“几何建模 / 曲线曲面 / 网格”，但 raw 更支持“模型加载 / 场景表示 / PBR 过渡”。
2. **GLTF / USD 容易被讲成纯格式名词**：指南需要用“文件数据 -> CPU 解析 -> GPU buffer / material / texture -> shader / ray tracer”的数据流解释。
3. **PBR 与 GI 边界要清晰**：P5 负责材质和场景数据的物理化表达；P6 才进入完整全局光照与渲染方程。
4. **几何表示只能概览**：Week 14 raw 可支持 polygon mesh、point cloud、NURBS、implicit surfaces、voxels、CSG 等用途对比，但不支持详细算法。
5. **曲线曲面 / mesh processing 是正式缺口**：Bezier、B-spline、de Casteljau、half-edge、QEM、Catmull-Clark 细节未覆盖，应在指南中标注为扩展而非考试主线。

## 3. Stage 3 目标

Stage 3 围绕 P5 的可交付主线补 visual explanation、examples 和缺口边界：

1. `visual-explain-model-data-pipeline`：把 GLTF / OBJ / USD 数据进入渲染管线整理成 Mermaid 图素材。
2. `examples-gltf-pbr-material-flow`：补 GLTF / PBR 材质参数、纹理贴图和 shader / ray tracer 输入之间的例子。
3. `compare-geometry-representations-boundaries`：整理几何表示对比表，并明确哪些只有概览、哪些缺失算法。
4. `review-gap-boundary-curves-mesh`：整理最终指南应如何保守处理曲线曲面 / mesh processing 缺口。

## 4. Optional Stage 4 判断

暂不生成 optional stage-4。Stage 1-2 已足够支撑一个“P5 资料校准版”学习指南；缺失的传统曲线曲面 / mesh processing 需要用户补充 source 后再用 `supplement-*` 追加，而不是让 NotebookLM 根据通用知识补写。
