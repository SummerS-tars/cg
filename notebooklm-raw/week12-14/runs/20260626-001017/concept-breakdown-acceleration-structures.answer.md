在光线追踪（Ray Tracing）中，性能优化的核心目标是解决**大量光线与场景几何体（Geometry）求交测试**带来的计算瓶颈 [1, 2]。以下基于课堂记录与 OptiX 资料，展开 AABB、BVH、RT Core 及 OptiX 在性能优化中的关键角色。

### 1. 轴对齐包围盒 AABB (Axis-Aligned Bounding Box) 与区间直觉
**轴对齐包围盒 AABB (Axis-Aligned Bounding Box)** 是最基础且硬件友好的加速结构，它用一个边与坐标轴平行的立方体包裹复杂的几何体 [2, 3]。

*   **光线-包围盒求交（Ray-Box Test）的区间直觉**：
    该测试的核心是 **Slab 方法**。在 3D 空间中，一个 AABB 可以看作是三对分别垂直于 x、y、z 轴的平行平面（Slabs）的交集 [3]。
    *   **区间重叠逻辑**：对于光线在每一个轴向上的投影，我们都能计算出它进入该轴向平面对的时间 $t_{min}$ 和离开的时间 $t_{max}$ [3]。
    *   **判断准则**：光线与盒子相交的直觉在于——只有当光线**进入了所有维度的平面后，且尚未离开任何一个维度的平面**，才算真正进入了盒子 [3]。
    *   **数学表达**：令光线在三轴上的进入时间最大值为 $t_{enter}$，离开时间的最小值为 $t_{exit}$。若满足 $t_{enter} < t_{exit}$ 且 $t_{exit} > 0$，则判定为相交 [3]。这种计算仅涉及简单的加减乘除与逻辑比较，极其高效，是硬件加速的首选 [2, 3]。

### 2. 层次包围盒 BVH (Bounding Volume Hierarchy) 为何降低复杂度
如果对场景中 $N$ 个几何体进行暴力遍历，计算复杂度为 $O(N)$，在大规模场景下不可接受 [4]。**层次包围盒 BVH (Bounding Volume Hierarchy)** 通过空间层次结构将复杂度大幅降低。

*   **树状组织结构**：BVH 将物体组织成一棵二叉树。根节点包裹整个场景，子节点包裹局部区域，叶子节点则包含具体的几何图元 [2, 3]。
*   **空间剔除（Spatial Culling）**：在遍历时，若光线未击中父节点的包围盒，则可以瞬间剔除其下方成千上万个子节点和图元 [3]。
*   **复杂度飞跃**：通过这种“分而治之”的策略，求交测试的复杂度从线性的 $O(N)$ 降低到了对数级的 $O(\log N)$ [5]。这意味着即便场景复杂度增加数倍，计算量的增长也相对缓慢。
*   **TLAS 与 BLAS**：在现代实现（如 Vulkan RTX 或 OptiX）中，BVH 进一步分为**顶层加速结构 TLAS (Top-Level Acceleration Structure，针对物体实例)** 和**底层加速结构 BLAS (Bottom-Level Acceleration Structure，针对单个物体的三角形网格)**，以支持动态物体的快速更新 [6]。

### 3. RT Core 与 OptiX 在管线中的角色
硬件加速的介入使实时光线追踪成为可能，其中 RT Core 是硬件基础，而 OptiX 是软件桥梁。

*   **RT Core (Ray Tracing Core，光线追踪核心)**：
    这是 NVIDIA RTX 架构中的专用硬件单元，旨在将软件中开销最大的逻辑“固化”到电路中 [7]。
    *   **硬件化功能**：RT Core 专门负责**加速包围盒遍历（BVH Traversal）**和**光线-三角形求交（Ray-Triangle Intersection）** [1, 7]。
    *   **效能提升**：相比于传统的使用计算着色器（Compute Shader）模拟，RT Core 能在极低能耗下处理每秒数十亿次的光线遍历，从而释放通用流处理器（Streaming Multiprocessor）去执行着色计算 [6, 7]。

*   **OptiX (NVIDIA OptiX Ray Tracing Engine，NVIDIA OptiX 光线追踪引擎)**：
    OptiX 是一个**可编程的光线追踪管线**，其核心是一个**领域特定即时编译器 JIT (Domain-Specific Just-In-Time Compiler)** [8, 9]。
    *   **管线角色**：OptiX 负责将用户定义的各种程序（如光线生成 Ray Generation、最近命中 Closest Hit、相交 Intersection 等）组合成一个高效的 GPU 内核（Kernel） [8, 10]。
    *   **黑盒优化**：开发者只需定义几何体和材质逻辑，OptiX 会在后台自动管理 **BVH 的构建、更新与加速结构在 RT Core 上的高效遍历** [11-13]。
    *   **角色总结**：如果说 RT Core 是“引擎中的强力活塞”，那么 OptiX 就是“整台高性能跑车的控制系统”，它协调硬件资源并允许开发者通过可编程接口实现复杂的物理渲染算法（如路径追踪） [8, 14]。

来源：[5], [8], [11], [10], [13], [9], [14], [1], [7], [3], [2], [6], [4]