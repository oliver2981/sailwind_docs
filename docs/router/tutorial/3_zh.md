# 设计准备

在 SailWind Router 中进行布线会话前，您可以为当前会话设置设计环境并保存设置以供将来使用。

**本课内容：**

1. 布线前准备步骤

2. 更改项目颜色

3. 定义层对

4. 设置默认布线角度

5. 设置布线网格和过孔网格

6. 启用实际宽度显示

7. 设置自动平移

8. 设置防护带

9. 保存默认设置

😎**前提**

如果尚未运行，请启动 SailWind Router 并打开\SailWind Projects\Samples 文件夹中的**previewplaced.pcb**文件。

## 布线前准备步骤

开始布线前，您需要执行一些准备工作。具体步骤因个人和设计而异。以下准备步骤专为本教程设计，建议您按照这些步骤操作以获得完整的教程体验。

## 更改项目颜色

**选项按钮 > 颜色选项卡**

为了提高布线时的可见性并减少屏幕杂乱，可以禁用不需要显示的项目。

1. 清除电源层和地平面的图层复选框以禁用这些平面层的显示

2. 在**颜色选择**区域点击背景色（黑色）

3. 在常规选项区域点击**背景**将背景显示为黑色

4. 在常规选项区域，点击**参考标识**、**禁止区**、**顶层边框**和**底层边框**列中的项目使这些项目不可见

5. 在**颜色选择**区域点击浅绿色

6. 在常规选项区域点击**连接**将连接显示为浅绿色

7. 保持选项对话框打开以备下一主题使用

> [!tip] 在 SailWind Router 中您可以保存颜色配置以便在其他设计中重复使用。完成颜色选项卡中的颜色分配后，您可以保存颜色配置。在颜色选项卡的颜色方案区域，点击**另存为**，为新颜色方案提供名称并点击**确定**。

## 定义层对

**选项按钮 > 布线/常规选项卡**

定义布线层对可减少交互式布线期间手动切换层的时间。配对布线层将层切换限制在层对成员之间。对于这个四层设计，明显的布线对由主元件层和次元件层组成。

1. 在层对区域，从第一层列表中选择**主元件面**，在第二层列表中选择**次元件面**

2. 保持选项对话框打开以备下一主题使用

## 设置默认布线角度

**选项按钮 > 布线/常规选项卡**

布线角度设置决定了交互式布线期间相邻走线段允许的角度（以度为单位）。

**有三种布线角度设置：**

| 布线角度 | 描述 |
|---------|------|
| 对角线 | 相邻走线段限制为 45 度间隔 |
| 正交 | 相邻走线段限制为 90 度间隔 |
| 任意角度 | 相邻走线段不受角度限制 |

在本教程中，将布线角度设置为正交。

1. 在布线角度区域，点击**正交**

2. 点击**确定**关闭选项对话框

## 设置布线网格和过孔网格

![](/router/tutrial/3/_page_2_Picture_1.jpeg)

在本课中，使用布线和过孔网格来辅助学习过程。

将布线和过孔网格设置为 8.33 密耳以适应设计的 8 密耳走线和 8 密耳间距要求：

1. 将布线和过孔网格的 X增量和 Y增量值设置为**8.33**

2. 点击**确定**保存设置并关闭**设计特性**对话框。或者您可以使用快捷键设置网格

3. 使用网格快捷键，输入**gr 8.33**并按**Enter**设置布线网格

4. 输入**gv 8.33**并按**Enter**设置过孔网格

## 启用实际宽度显示

**选项按钮 > 全局/常规选项卡**

您可以启用或禁用实际宽度显示以查看走线的真实宽度。

1. 在显示设置区域，在最小线宽框中输入**8**

2. 点击**应用**激活设置

3. 保持选项对话框打开以备下一主题使用

## 设置自动平移

**选项按钮 > 全局/常规选项卡**

在布线会话期间，平移设计可能很方便。SailWind Router 包含一个自动平移功能，可以跟随指针自动平移屏幕。

1. 在指针设置区域，选中**随指针移动平移显示**复选框以启用自动平移功能

2. 点击**确定**关闭选项对话框

## 设置防护带

**选项按钮 > 全局/常规选项卡**

在交互式布线和编辑期间，SailWind Router 可以显示所有对象周围的防护带以指示间距边界。当指针接近对象时，会在附近对象周围显示可见边框，指示当前操作有效规则的间距边界。

![](/router/tutrial/3/_page_3_Picture_1.jpeg)

1. 在显示设置区域，选中**在对象上显示防护带**复选框

2. 点击**确定**应用设置并关闭选项对话框

3. 不要保存设计副本

**您已完成布线前准备步骤教程。**