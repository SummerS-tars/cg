# Week 12-14 / Part 6 Focus Map

> **生成时间**：2026-06-26  
> **输入 run**：`notebooklm-raw/week12-14/runs/20260626-001017`  
> **Stage 2 状态**：6/6 completed，0 retry；与 P5 stage-2 小并发运行，未降级串行。

## 1. 认知重点分级

| 主题 | 等级 | 已有 raw | 指南处理 |
|------|------|----------|----------|
| Whitted-style Ray Tracing | critical | `concept-breakdown-ray-tracing-basics` | 作为 P6 起点，解释 ray generation、intersection、shadow ray、反射 / 折射递归 |
| AABB / BVH / RT Core / OptiX | critical | `concept-breakdown-acceleration-structures` | 用空间剔除和管线图解释性能瓶颈如何被解决 |
| Rendering Equation / GI | critical | `concept-breakdown-rendering-equation-gi` | 用公式和直觉解释局部到全局、BRDF、visibility、geometry term |
| Path Types / Radiosity | important | stage-1 / stage-2 GI raw | 用对比表压缩说明 OpenGL、ray tracing、radiosity、path tracing 能处理什么光路 |
| Monte Carlo / Path Tracing | critical | `concept-breakdown-monte-carlo-path-tracing` | 解释 PDF、estimator、SPP、variance、$N=1$、噪声收敛 |
| RR / Importance Sampling / NEE | critical | `concept-breakdown-sampling-optimization` | 解释无偏终止和降方差策略，给视觉例 |
| Denoising / DLSS / Real-time RT | important | `concept-breakdown-denoising-realtime-rt` | 作为工业落地章节：low spp、G-buffer、时空去噪、Tensor Core |

## 2. 难点与缺口

1. **光线追踪与路径追踪边界**：Whitted-style 处理镜面反射 / 折射，path tracing 用 Monte Carlo 求解包含漫反射多次弹射的渲染方程。
2. **渲染方程不能只贴公式**：需要解释 $L_o$、$L_e$、$f_r$、$L_i$、$\cos\theta$、$V$、$G$ 的视觉意义。
3. **Monte Carlo 与噪声直觉**：要把 PDF、estimator、variance、SPP 和“样本越多越平滑”联系起来。
4. **Russian Roulette 的无偏性**：必须说明存活路径除以概率 $P$，否则容易误以为它只是随机提前停止。
5. **NEE / direct light sampling**：需要说明为什么小光源难命中、为什么改为采样光源面积。
6. **实时去噪章节要避免过深工程细节**：raw 支持 G-buffer、运动向量、法线、反照率、DLSS 和硬件角色，但不支持具体神经网络结构。

## 3. Stage 3 目标

Stage 3 围绕 critical 难点补 deep-dive、examples 和 visual explanation：

1. `visual-explain-ray-tracing-pipeline`：整理 ray generation -> intersection -> shading -> shadow/reflection/refraction recursion -> output 的图示。
2. `deep-dive-bvh-aabb-example`：补 AABB slab test、BVH 剔除和 RT Core / OptiX 角色的可视化解释。
3. `deep-dive-rendering-equation-terms`：补渲染方程各项的视觉意义和局部 / 全局对比。
4. `examples-monte-carlo-path-tracing-noise`：补 PDF / estimator / SPP / variance / $N=1$ 的例子。
5. `compare-rr-importance-nee`：整理 Russian Roulette、importance sampling、direct light sampling / NEE 的对比素材。
6. `visual-explain-realtime-denoising`：整理 low-spp -> G-buffer -> temporal/spatial denoising -> DLSS / Tensor Core 的图示。

## 4. Optional Stage 4 判断

暂不生成 optional stage-4。Stage 1-2 已覆盖 P6 主线；shadow map 在 P6 规划中出现但 raw 中不是主线，最终指南可作为实时效果背景压缩说明。若用户后续上传 shadow map 专项课件，再追加 `supplement-shadow-map`。
