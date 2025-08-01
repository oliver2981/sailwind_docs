# 添加与复制元件教程
通常，原理图输入需要进行多次添加、复制或删除元件操作。

**本课程涵盖以下主题：**

1. 添加元件
2. 删除元件
3. 复制元件

😎**前提**

如果尚未运行，请启动 SailWind Logic 并打开\SailWind Projects\Samples 文件夹中的**previewstart.sch**文件。

## 添加元件
添加元件时，系统会提供实时元件封装功能来自动分配参考标识符。

**调整视图大小**

开始前，请调整视图大小以适配 U1 和 U5B 门周围区域，如下图所示。

![](/logic/tutorial/4/_page_0_Figure_12.jpeg)

**添加元件**

元件直接从库添加到原理图。在本练习中，您将使用"添加元件"命令向原理图添加新的 AM100415 元件。

1. 点击**添加元件**按钮
2. 在"从库添加元件"对话框中，在筛选区域选择库列表中的(所有库)
3. 在项目框中输入**AM100\***并点击**应用**，对库中前五个字符为 AM100 的所有元件执行通配符搜索。结果将显示在项目列表中
4. 从元件列表中选择**AM100415**。该元件将显示在预览窗口中
5. 点击**添加**。AM100415 元件将附着到设计区域中的指针上
6. 在"从库添加元件"对话框中点击**关闭**

**放置元件**

每次添加新元件时，它都会附着到指针上。通过定位和放置完成元件添加。本练习需要精确放置元件。

1. 将元件定位在 R1 和 U5B 之间的**X6500,Y7900**位置。使用状态栏上的坐标显示作为参考。不要使用 D:(delta)坐标
2. 点击将元件放置在原理图上

   > [!TIP]
   >
   >  您可以看到 U3 是该元件的参考标识符。尽管前缀 U 最后使用的参考标识符编号是 7，但系统确定编号 3 未被使用。在恢复编号序列前会自动分配未使用的编号。

3. 在设计空白区域添加更多元件。放置完符号后按**Esc**

删除或重新编号元件产生的间隙会自动填充以优化元件使用。添加多门元件时，现有元件中未使用的门将在创建新封装前被优先使用。

## 删除元件
要删除 AM100415 的多个实例：

1. 点击**删除模式**按钮
2. 选择 AM100415 元件的副本。如果无法删除元件，请右键点击并选择**选择元件**

    > [!TIP]
    >
    >  为获得最佳效果，选择时将指针放在元件边框上

3. 重复这些步骤删除您添加的其他元件，U3 除外
4. 右键点击并选择**取消**退出删除模式

**替代方法：** 按 Esc 取消

5. 在视图菜单中点击**重绘**刷新工作区显示。**替代方法：** 按 Ctrl+D 重绘

## 复制元件
使用"复制"命令可在原理图上复制元件。

1. 点击**复制模式**按钮
2. 选择 U3 添加 AMD 元件的副本。与"添加元件"命令类似，元件将附着到指针并进入移动元件模式
3. 点击在原理图上放置多个副本。右键点击并选择**取消**停止复制 U3

   ![](/logic/tutorial/4/_page_2_Picture_2.jpeg)

4. 在设计工具栏上点击**选择**按钮退出复制模式

   **替代方法：** 按 Esc 退出模式

5. 右键点击并选择**选择元件**。使用 Ctrl+点击选择除 U3 外您添加的所有其他元件。右键点击并选择**删除**

    > [!TIP]
    >
    >  您可以对多个对象应用更改。上例中选择的所有元件都被删除。多个选定元件的其他选项包括属性添加、属性可见性更改和保存到库。多个选择的可用选项根据所选对象类型而异。

6. 不要保存文件副本

**您已完成添加和复制元件教程**