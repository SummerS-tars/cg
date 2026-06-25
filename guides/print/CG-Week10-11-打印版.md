# CG Week 10-11 打印版：模型加载、场景表示与 PBR 过渡

## 0. 术语表

| 术语 | 本 Part 中的含义 | 先记住的直觉 |
|------|------------------|--------------|
| 模型加载(Model Loading) | 把 3D 文件解析成渲染器能使用的几何、材质、纹理和场景层级数据 | 文件不是图像，而是渲染所需数据包 |
| 场景表示(Scene Representation) | 用节点、网格、材质、纹理和变换描述一个可渲染场景 | 把物体、层级和外观组织起来 |
| OBJ(Wavefront OBJ，经典几何格式) | 以几何网格为主的常见模型格式 | 简单、通用，但场景和 PBR 能力有限 |
| GLTF(Graphics Language Transmission Format，图形语言传输格式) | 面向现代实时渲染和传输的 3D 场景格式 | 常被理解成 3D 内容的传输格式 |
| GLB(GLTF Binary，GLTF 二进制格式) | GLTF 的二进制打包形式 | 把 JSON、buffer、纹理等打进一个文件 |
| USD(Universal Scene Description，通用场景描述) | 工业级复杂场景描述标准 | 更适合大型制作管线和资产协作 |
| PBR(Physically Based Rendering，基于物理的渲染) | 用物理一致的材质参数描述表面反射 | 材质参数要接近真实光学行为 |
| BRDF(Bidirectional Reflectance Distribution Function，双向反射分布函数) | 描述入射光有多少反射到观察方向 | 材质反光规则 |
| UV(UV Coordinates，纹理坐标) | 2D 纹理空间坐标，通常在 $[0,1]$ | 在图片上取样的位置 |
| VB(Vertex Buffer，顶点缓冲区) | GPU 中保存顶点属性的缓冲区 | 顶点数据上 GPU 后住在这里 |
| IB(Index Buffer，索引缓冲区) | GPU 中保存顶点索引顺序的缓冲区 | 复用顶点并组成三角形 |
| BVH(Bounding Volume Hierarchy，层次包围盒) | 用包围盒树加速 ray tracing 求交 | 先排除大块不可能命中的几何 |
| TLAS(Top-Level Acceleration Structure，顶层加速结构) | 光追中组织场景实例的上层加速结构 | 管“哪些实例在场景里” |
| BLAS(Bottom-Level Acceleration Structure，底层加速结构) | 光追中组织单个 mesh 三角形的底层加速结构 | 管“一个 mesh 内部有哪些三角形” |

## 1. 知识地图

P4 已经讲完着色(Shading)、纹理映射(Texture Mapping)和片元阶段的材质表现。Week 10-11 解决的是更靠前的问题：**这些几何、材质、纹理和场景层级数据从哪里来，如何进入渲染管线？**

```mermaid
flowchart LR
    File[模型和场景文件<br/>OBJ / GLTF / USD] --> CPU[CPU 解析与场景组织]
    CPU --> Geo[几何数据<br/>Position / Normal / UV]
    CPU --> Mat[材质和纹理<br/>Material / Texture]
    CPU --> Scene[场景图<br/>Scene Graph]
    Geo --> GPU[GPU 资源<br/>VB / IB / Textures]
    Mat --> GPU
    Scene --> Draw[Shader 或 Ray Tracer]
    GPU --> Draw
    Draw --> Image[最终图像<br/>Framebuffer]
```

> **追问：为什么 P5 不直接变成曲线曲面推导？**
> 因为当前 raw 显示，这一 Part 的可复习主线更像“资产如何进入渲染器”：模型文件、GLTF、PBR 材质、场景层级和几何表示边界。曲线曲面与 mesh processing 的部分细节要按资料边界保守处理。

## 2. 核心知识

### 2.1 从模型文件到最终图像：渲染器到底读进了什么

常见模型 / 场景格式包括 OBJ(Wavefront OBJ，经典几何格式)、FBX(Filmbox，动画和层级场景格式)、GLTF(Graphics Language Transmission Format，图形语言传输格式)、GLB(GLTF Binary，GLTF 二进制格式)，以及 USD(Universal Scene Description，通用场景描述)。它们不是“图片”，而是把几何、材质、纹理、层级和动画打包给渲染器。

```mermaid
flowchart TD
    A[GLTF / OBJ / USD 文件] --> B[CPU 解析器]
    B --> C[提取顶点 / 法线 / UV / 材质 / 纹理]
    C --> D[构建场景图和变换矩阵]
    D --> E[上传 GPU 资源]
    E --> F1[VB 和 IB<br/>顶点与索引]
    E --> F2[Textures<br/>纹理与采样器]
    E --> F3[Constants<br/>相机 / 光源 / 材质参数]
    E --> F4[TLAS 和 BLAS<br/>光追加速结构]
    F1 --> G[Shader 或 Ray Tracer]
    F2 --> G
    F3 --> G
    F4 --> G
    G --> I[Framebuffer 最终图像]
```

关键数据可以按“几何、外观、组织、加速”四类记：

| 数据 | 英文术语 | 作用 |
|------|----------|------|
| 顶点位置 | Position | 定义几何形状在局部空间的位置 |
| 法线 | Normal | 告诉着色器表面朝向，用于光照计算 |
| UV 坐标 | UV Coordinates | 把二维纹理贴到三维表面 |
| 材质 | Material | 描述表面颜色、粗糙度、金属度等反射属性 |
| 纹理 | Texture | 用图像承载颜色、法线、粗糙度等空间变化 |
| 场景图 | Scene Graph | 用层级结构组织对象和变换 |
| 加速结构 | Acceleration Structure | 为 ray tracing 快速求交服务 |

**小结**：模型加载把“文件资产”转成“管线资源”。接下来最重要的工程格式是 GLTF，因为它把几何和现代材质放在同一套传输结构里。

### 2.2 GLTF 与 PBR：P5 的实践核心

GLTF 常被称为“3D 界的 JPEG”，因为它面向高效传输和现代实时渲染。对 P5 来说，GLTF 的价值在于它能把**几何数据**和 **PBR 材质参数**一起带进渲染器。

PBR(Physically Based Rendering，基于物理的渲染)关注的是：光线打到某个表面后，这个表面应该怎样反射光。它通常使用如下参数：

| 参数 | 英文 | 控制什么 |
|------|------|----------|
| 反照率 | Albedo | 表面基础颜色，不包含阴影 |
| 粗糙度 | Roughness | 微平面分布越散，表面越哑光 |
| 金属度 | Metallic | 决定材质更像金属还是电介质 |
| 法线贴图 | Normal Map | 不增加几何复杂度，也能制造细微凹凸 |
| BRDF | Bidirectional Reflectance Distribution Function | 描述入射光如何被表面反射到观察方向 |

一个简化的 GLTF / PBR 数据流是：

```mermaid
flowchart LR
    A[GLTF nodes / meshes] --> B[模型变换与网格]
    C[GLTF materials] --> D[Albedo / Roughness / Metallic]
    E[Texture images] --> F[UV 采样]
    B --> G[Shader 或 Ray Tracer]
    D --> G
    F --> G
    H[Light / Camera] --> G
    G --> I[PBR 表面颜色]
```

PBR 和 GI(Global Illumination，全局光照)的分界要记清：PBR 解决“**表面如何反射**”，也就是给定一束入射光，材质如何把它反射出去；GI 解决“**光从哪里来**”，包括直接光和多次反弹后的间接光。因此，P5 让场景数据和材质变得“物理化”，P6 再用 ray tracing / path tracing 去模拟完整光能传递。

**小结**：GLTF 把资产结构带进渲染器，PBR 把表面反射规则带进材质系统。下一步要看这些资产背后的几何可以有哪些表示方式。

### 2.3 几何表示：知道每种表示适合什么

当前 raw 支持的是几何表示(Object Representations)的概览，而不是完整算法推导。复习时重点是识别不同表示的适用场景。

| 表示方法 | 英文术语 | 适用场景 | 当前 raw 覆盖 |
|----------|----------|----------|---------------|
| 多边形网格 | Polygon Mesh | 游戏、实时渲染、通用模型输入 | 覆盖较多 |
| 点云 | Point Cloud | LiDAR、SLAM、逆向工程 | 部分覆盖 |
| 细分曲面 | Subdivision Surface | 影视角色、平滑模型 | 概念覆盖 |
| 参数曲面 / NURBS | NURBS(Non-Uniform Rational B-Splines，非均匀有理 B 样条) | CAD、汽车、航空工业设计 | 概念覆盖 |
| 隐式曲面 | Implicit Surface | 流体、水滴融合、代数求交 | 部分覆盖 |
| 体素 | Voxel | CT / MRI、科学可视化、体数据 | 概念覆盖 |
| 构造实体几何 | CSG(Constructive Solid Geometry，构造实体几何) | 机械零件、布尔建模 | 概念覆盖 |
| 过程建模 | Procedural Modeling | 地形、植物、大规模自然场景 | 概念覆盖 |

多边形网格最适合 GPU 光栅化，因为三角形容易插值、裁剪和并行处理。点云更接近传感器原始数据，通常需要重建成曲面。NURBS 适合工业精确曲面，但实时渲染常要先离散化。隐式曲面适合用方程描述融合或体积效果，ray tracing 中可通过方程求交。

> **直观理解：mesh 为什么在实时渲染里最常见？**
> 不是因为 mesh 能表达所有几何细节，而是因为三角形非常适合现代 GPU 管线：顶点处理、光栅化、插值、深度测试都围绕它高效实现。

**小结**：几何表示决定资产如何存储和处理。最后还要明确哪些内容当前 raw 不足，复习时不要硬背成主线。

## 3. 易混点

| 易混点 | 正确认法 |
|--------|----------|
| GLTF 等于 OBJ 的新版 | OBJ 偏几何和简单材质；GLTF 更适合现代场景、PBR 材质和 Web / 实时传输 |
| PBR 等于 GI | PBR 定义表面反射规律；GI 模拟光线在场景中的多次传递 |
| Mesh 等于所有几何表示 | Mesh 是离散三角形或多边形；NURBS、implicit surface、voxel 等服务不同建模需求 |
| Texture 等于 Material | Texture 是图像或数据；Material 是如何解释这些数据的表面模型 |
| Scene Graph 等于 Acceleration Structure | 场景图组织对象层级；BVH、TLAS、BLAS 服务 ray tracing 求交加速 |
| 资料缺口等于可以忽略 | 缺口不是不重要，而是当前指南不能把未充分支持的细节写成主线 |
