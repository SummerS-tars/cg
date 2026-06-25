在计算机图形学渲染管线中，从**观察空间(View Space/Camera Space)**到最终**像素坐标(Pixel Coordinates)**的链路是实现“近大远小”视觉效果并最终成像的核心过程 [1], [2]。基于 Week 4 课堂记录和课件，这一链路的完整深挖如下：

### 1. 透视投影与裁剪空间 (Perspective Projection & Clip Space)

**透视投影(Perspective Projection)** 的核心目标是将三维观察空间中的顶点映射到一个二维平面上，模拟人眼“近大远小”的视觉特性 [3], [4]。

*   **相似三角形(Similar Triangles)推导**：
    假设相机位于原点，向 $-z$ 轴观察，近裁剪面距离为 $n$。对于观察空间中的点 $P(x, y, z)$，其在投影平面上的坐标 $P'(x', y')$ 可通过相似三角形原理推导 [5], [4]：
    $$\frac{x'}{n} = \frac{x}{z} \Rightarrow x' = \frac{n \cdot x}{z}$$
    $$\frac{y'}{n} = \frac{y}{z} \Rightarrow y' = \frac{n \cdot y}{z}$$
*   **裁剪空间(Clip Space)**：
    投影变换通过一个 **投影矩阵(Projection Matrix)** 将顶点转换到裁剪空间 [6], [2]。此时顶点的坐标表示为四维**齐次坐标(Homogeneous Coordinates)** $(x, y, z, w)$ [7], [4]。
*   **为什么在裁剪空间裁剪？**
    裁剪(Clipping)发生在投影矩阵变换之后、透视除法之前 [2]。主要原因是为了**效率和鲁棒性**：
    1.  **线性度**：在齐次坐标系下，所有的几何图元（如线段、多边形）仍然保持线性，便于使用 **Cohen-Sutherland(利于线段)或Sutherland-Hodgeman(利于多边形)** 算法进行高效裁剪 [8], [9]。
    2.  **避免除零错误**：如果先进行透视除法，位于相机后方或 $z=0$ 处的点会导致计算异常；在裁剪空间可以利用 $w$ 分量（通常存储了原始的 $-z$ 值）直接判断顶点是否在**视锥体(View Frustum)**内 [4], [2]。

### 2. 透视除法与 NDC (Perspective Division & NDC)

完成裁剪后，硬件执行 **透视除法(Perspective Division)**，这是将 3D 转换到 2D 效果的实质性步骤 [2]。

*   **计算过程**：将裁剪空间的坐标除以其 $w$ 分量 [4]：
    $$\begin{bmatrix} x_{ndc} \\ y_{ndc} \\ z_{ndc} \end{bmatrix} = \begin{bmatrix} x/w \\ y/w \\ z/w \end{bmatrix}$$
*   **标准设备坐标 NDC(Normalized Device Coordinates)**：
    透视除法的结果使坐标进入 NDC 空间 [10], [2]。在大多数 API（如 WebGL/OpenGL）中，这是一个轴对齐的单位立方体，范围通常在 $[-1, 1]^3$ [2]。

### 3. 视口变换 (Viewport Transformation)

最后一步是将规范化的 NDC 坐标映射到实际屏幕窗口的**像素坐标(Pixel Coordinates)** [1], [10]。

*   **视口映射(Viewport Mapping)公式**：
    假设屏幕视口左下角为 $(vx_1, vy_1)$，宽度为 $w$，高度为 $h$。NDC 坐标 $(x_{ndc}, y_{ndc})$ 到像素坐标 $(v_x, v_y)$ 的映射为 [11]：
    $$v_x = vx_1 + (x_{ndc} - (-1)) \cdot \frac{w}{1 - (-1)} = vx_1 + (x_{ndc} + 1) \cdot \frac{w}{2}$$
    $$v_y = vy_1 + (y_{ndc} - (-1)) \cdot \frac{h}{1 - (-1)} = vy_1 + (y_{ndc} + 1) \cdot \frac{h}{2}$$

---

### 参数控制说明

| 参数名称 | 术语全称及缩写 | 控制内容 |
| :--- | :--- | :--- |
| **FOV** | **Field of View(视场角)** | 控制相机的视野范围。FOV 越大，看到的场景越多，但物体在屏幕上显得越小 [12], [4]。 |
| **aspect** | **Aspect Ratio(宽高比)** | 屏幕宽度与高度的比例（$W/H$），确保投影后的物体不会发生比例拉伸 [13], [4]。 |
| **near/far** | **Near/Far Planes(近/远裁剪面)** | 定义相机可见的深度范围。只有在此范围内的物体才会被保留，防止渲染过远或过近的无用图元 [6], [4]。 |
| **w 分量** | **$w$ component** | 在投影矩阵中，通过将 $z$ 值编码进 $w$ 分量（通常 $w = -z$），为后续的透视除法做准备 [5], [4]。 |
| **透视除法** | **Perspective Division** | 通过除以 $w$ 产生“近大远小”的缩放效果，并把物体坐标压缩进 NDC 立方体 [4], [2]。 |

---

### 简化坐标流动例子

1.  **View Space**: 顶点位于相机正前方，坐标为 $(0, 0, -10)$ [1]。
2.  **Projection**: 应用投影矩阵（假设 $n=1, f=100$），转换到 **Clip Space** 得到齐次坐标 $(0, 0, 9.8, 10)$。注意此时 $w=10$ 存储了深度信息 [6], [4]。
3.  **Clipping**: 检查 $x, y, z$ 是否在 $[-w, w]$ 范围内。此处 $0$ 和 $9.8$ 均在 $[-10, 10]$ 内，通过 [8]。
4.  **Perspective Division**: 所有分量除以 $w(10)$，得到 **NDC** 坐标 $(0, 0, 0.98)$ [4], [2]。
5.  **Viewport Transformation**: 假设屏幕为 $1024 \times 1024$。应用映射公式，得到 **Pixel Coordinates** $(512, 512)$，即屏幕中心点 [10], [11]。