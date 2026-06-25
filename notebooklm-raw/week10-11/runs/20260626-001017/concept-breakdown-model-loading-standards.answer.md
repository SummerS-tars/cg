在计算机图形学的 Part 5（P5）模块中，“模型加载与场景标准”是连接建模上游与渲染下游的关键桥梁。基于 Week 11、12 和 14 的课堂记录及相关文献，该模块的核心内容展开如下：

### 一、 主流模型与场景标准

随着图形技术从早期的局部光照向基于物理的渲染（Physically Based Rendering, PBR）及实时光线追踪演进，行业标准也在不断发生变革 [1, 2]。

1.  **OBJ (Wavefront OBJ)**：源于上世纪 80 年代的经典格式，主要保存几何顶点和简单的材质信息，表现力在现代复杂场景中较为有限 [2]。
2.  **FBX (Filmbox)**：目前产业界广泛使用的通用标准，能够支持复杂的动画、层级结构和多种材质定义 [2]。
3.  **GLTF/GLB (Graphics Language Transmission Format, 图形语言传输格式)**：被誉为“3D 界的 JPEG”，因其高效的传输性能和对 Web 及 AI 生成的友好性，正逐渐成为新一代通用标准 [2, 3]。
4.  **USD (Universal Scene Description, 通用场景描述)**：由 Pixar（皮克斯）提出，现已成为 NVIDIA 和 Apple 等公司主推的工业界标准，专门用于描述极其复杂的场景层级和协作流程 [2, 3]。

### 二、 模型文件通常保存的数据

一个完整的模型或场景文件不仅是几何体的集合，更是一个复杂的数据容器，通常包含以下核心数据：

*   **几何数据 (Geometry Data)**：包括顶点 (Vertex) 的三维坐标 $(x, y, z)$、索引 (Index)、法线 (Normal) 和切线空间 (Tangent Frame) 信息 [4-6]。
*   **场景层级与变换 (Hierarchy & Transformations)**：
    *   **变换 (Transformation)**：定义物体在空间中的平移、旋转和缩放 [7, 8]。
    *   **场景图 (Scene Graphs)**：使用树形层级结构组织物体。每个节点存储一个相对于其父节点的 **变换矩阵 (Transformation Matrix)** [9, 10]。
*   **材质与纹理 (Materials & Textures)**：
    *   **UV 坐标 (UV Coordinates)**：建立从三维表面到二维纹理空间的映射关系 [11]。
    *   **PBR 材质属性**：包括反照率 (Albedo)、粗糙度 (Roughness)、金属度 (Metallic)、高光 (Specular) 以及法线贴图 (Normal Map) 等 [4, 12, 13]。
*   **动画数据 (Animation Data)**：包括刚体动画层级、关节旋转参数或更复杂的骨骼权重信息 [10, 14]。

### 三、 数据如何进入 P4/P5 渲染管线

在 P4（可编程管线）和 P5（包含模型加载的进阶渲染）中，模型数据通过以下流程进入渲染管线：

1.  **解析与加载 (Parsing & Loading)**：CPU 端通过解析器（如 GLTF 加载器）读取文件，将二进制数据转化为内存中的缓冲区 (Buffer) [1, 15]。
2.  **资源绑定 (Resource Binding)**：
    *   几何数据进入 **输入装配阶段 (Input-Assembler Stage)**，顶点存储于顶点缓冲区 VBV (Vertex Buffer View)，绘制顺序由索引缓冲区 IBV (Index Buffer View) 指定 [16, 17]。
    *   材质和纹理被加载至显存，通过 **常量缓冲区 (Constant Buffer)** 或着色器资源视图进行绑定 [15, 16, 18]。
3.  **坐标变换 (Coordinate Transformations)**：
    *   **顶点着色器 (Vertex Shader)** 接收顶点数据，并应用模型变换 (Modeling Transformation) 将其从局部坐标系转换到世界坐标系，随后进行视图和投影变换 [16, 17, 19]。
    *   在处理具有层级结构的场景（如 USD 或 FBX）时，需要通过矩阵连乘计算出每个物体的全局变换矩阵 [10, 20]。
4.  **加速结构构建 (Acceleration Structures)**：对于 P5 涉及的进阶渲染，加载的模型数据常用于构建 **BVH (Bounding Volume Hierarchy, 层次包围盒)** 等空间加速结构，以实现高效的可见性确定和求交计算 [17, 21]。
5.  **片段着色与输出 (Fragment Shading & Output)**：在 **片段着色器 (Fragment Shader)** 中，通过插值得到的 UV 坐标采样纹理，并结合材质参数和光照模型计算最终像素颜色 [11, 17]。

通过这一流程，存储在标准文件（如 GLTF 或 USD）中的复杂数据得以转化为 GPU 可处理的流式信息，最终生成高质量的渲染图像 [22, 23]。