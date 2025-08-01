# 学习用户界面

SailWind Router 用户界面设计简洁高效。SailWind Router 既满足高级用户需求，又兼顾初学者体验。其界面和交互方式与其他 Windows™ 应用程序（包括 SailWind Layout）类似。您可通过键盘、菜单、工具栏和快捷菜单与 SailWind Router 交互。

**本课程内容：**

1. 指针位置显示

2. 取消命令

3. 快捷菜单

4. 平移、缩放和滚动

5. 选择对象

😎**前提**

如果尚未运行，请启动 SailWind Router 并打开 \SailWind Projects\Samples 文件夹中的 **preview.pcb** 文件。

## 指针位置显示

当您在工作区移动指针时，其相对于原点的绝对 X、Y 坐标会显示在屏幕右下角的状态栏中。

1. 将指针置于设计上，观察状态栏读数

2. 移动指针时注意 X、Y 坐标变化

## 取消命令

您可随时按 Esc 键或右键点击并从快捷菜单中选择 Cancel 来取消当前命令或操作序列。

**例外：** 无法使用 Esc 取消自动布线操作。

## 缩放、平移和滚动

**缩放**

设计居中与放大有多种方法。本练习将使用鼠标操作：

对于双键鼠标，标准工具栏上的 Zoom 按钮可启用/禁用缩放模式。缩放模式下指针变为放大镜图标。

- 对于三键鼠标，中键始终可用作缩放

- 带滚轮的鼠标可结合快捷键进行滚动和缩放

> [!tip] 平移和缩放功能也可通过视图菜单命令、数字小键盘和 Windows 滚动条实现。详情参阅 *SailWind Router 帮助*。

**缩放练习**

1. 在标准工具栏点击 **Zoom** 按钮

**例外：** 使用三键鼠标可跳过此步

2. 放大操作

    - 左键点击并按住要放大的工作区中心区域

    **例外：** 使用三键鼠标时改用中键

    - 向上拖动指针（远离身体方向），动态矩形将随指针移动

    - 释放鼠标完成操作

3. 缩小操作：重复步骤 2 但向下拖动指针（朝向身体方向）

4. 练习使用缩放调整视图

> [!tip] 点击标准工具栏的 **View Board** 按钮可恢复原始视图

5. 点击标准工具栏的 **Zoom** 按钮退出缩放模式

**滚轮缩放**

1. 按住 **Ctrl**

2. 向上滚动滚轮（远离身体）放大

3. 向下滚动滚轮（朝向身体）缩小

**导航窗口缩放调整**

可在工作区修改导航窗口的缩放级别：

1. 指向工作区设计中心按 **F5** 增加导航窗口缩放级别（长按平滑缩放）

2. 按 **F6** 减小导航窗口缩放级别（长按平滑缩放）

**平移**

1. 指向新视图中心停止移动指针

2. 按 **Insert** 键使该区域成为视图中心

**备选方案：** 点击鼠标中键（三键鼠标无需进入缩放模式即可平移）

**三键鼠标平滑滚动**

1. 工具菜单选择 **Options**

2. 点击 **Global/General** 标签，在 Pointer Settings 区域勾选 **Pan display with pointer movements**

3. 点击 **OK**

**效果：** 当元件或走线移至屏幕边缘时，软件会自动向指针方向平移。同时启用平滑滚动。

**滚轮垂直/水平滚动**

1. 向上滚动滚轮（远离身体）向上滚动

2. 向下滚动滚轮（朝向身体）向下滚动

3. 按住 **Shift**

4. 向上滚动滚轮向左滚动

5. 向下滚动滚轮向右滚动

## 选择对象

通过指针悬停并点击可选择任何对象（如元件、走线或网络），这称为*面向对象选择*。

**循环选择**

在密集区域可能需要多次尝试才能选中特定对象。可通过循环选择功能遍历当前选择附近的所有对象。

1. 右键点击选择 **Select Anything**

2. 在工作区选择 U1 的 28 脚（U1 是板底中部的大型 SOIC，28 脚位于 U1 左上角）

3. 按 **Tab** 或点击标准工具栏的 **Cycle** 按钮循环选择 28 脚附近的所有可选对象

4. 选中所需项目后停止循环

设计时可能需要仅选择特定对象（如仅选择元件）。可通过 Selection Filter 工具栏限制选择范围，该工具栏可指定哪些设计对象可选。

**筛选选择**

1. 点击标准工具栏的 **Selection Filter** 按钮显示筛选工具栏

2. 点击 **Anything** 按钮启用全对象选择

3. 点击 **Components** 按钮禁用元件选择

4. 尝试选择工作区中的元件边框（此时不可选）

5. 选择非元件对象（此时可选）

6. 按 **Esc** 取消所有选择

**使用选择快捷键**

未选择任何对象时右键点击，将显示包含选择快捷键的菜单。选择快捷方式会更新 Selection Filter 工具栏的设置。

1. 未选择任何对象且筛选工具栏打开时，右键点击 **Select Nets**（注意工具栏更新为仅允许网络选择）

2. 再次右键点击 **Select Anything**（工具栏更新为允许选择任何对象，默认仍禁用网络、管脚对和路径）

**选择同类型所有对象**

可通过 Selection Filter 工具栏或选择快捷键选择某类型的所有项目。

1. 未选择任何对象时，右键点击 **Select Components**

2. 再次右键点击 **Select All** 选择设计中所有元件

3. 不要保存设计副本

**您已完成用户界面概念教程。**