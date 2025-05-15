# 链接到 SailWind 布局教程

将 SailWind Logic 原理图数据转发到 SailWind Layout 有两种方法：

创建 SailWind Layout 可以读取的网络表并将其导入 SailWind Layout 使用 SailWind Layout 链接自动管理 SailWind Logic 和 SailWind Layout 之间的数据传输。

SailWind Layout 链接自动在 SailWind Logic 和 SailWind Layout 之间传递设计数据，是同步原理图和 PCB 设计数据库的首选方法。

SailWind Layout 链接的另一个优势是工具间通信。使用这项自动化技术可以在链接的应用程序之间进行交叉探测。交叉探测是指在一个应用程序中选择网络、元件或引脚，从而在链接的应用程序中选中相应的对象。

SailWind Logic 支持 OLE 自动化。此功能允许您使用 Visual Basic、Microsoft Visual $^ { \mathsf { C } + + }$ 或其他工具开发自定义应用程序，以从 SailWind Logic 数据库中提取特定数据。

**准备**

如果它尚未运行，请启动 SailWind Logic 并打开 \\SailWind Projects\\Samples 文件夹中名为 preview.sch 的文件。

要求：本教程要求示例库保持其原始搜索顺序。在 SailWind 布局搜索顺序中，预览库必须位于通用库之前，否则将导致错误。

## 创建网表

创建网表是将原理图数据传入 SailWind Layout 以启动 PCB 设计流程的基本方法。网表包含元件列表、元件类型及其所有网络连接。网表还可以包含设计规则和层堆栈（可选）。

**要创建网表：**

1.  工具菜单 $>$ 布局网表。
    
2.  在“网表到 PCB”对话框中，接受默认设置并单击“确定”以创建网表。输出窗口中将显示指向 Preview.asc 网表文件的链接。单击该链接即可在默认文本编辑器中打开该文件。
    
3.  在继续下一部分之前，请检查网表文件的内容并关闭该文件。
    

## 使用 SailWind 布局链接

您可以使用 SailWind Layout Link 的功能在 SailWind Logic 和 SailWind Layout 之间进行交叉探测。使用此功能可以执行原理图驱动的布局或布局的后期设计审查。

1.  工具菜单 $>$ SailWind 布局。
    
2.  在“连接到 SailWind Layout”对话框中，单击“新建”以启动新的 SailWind Layout 会话。SailWind Layout 启动可能需要一些时间。
    
3.  SailWind Layout 启动后，两个应用程序将链接在一起，并启用 SailWind Logic 和 SailWind Layout 之间的交叉探测。同时会显示“SailWind Layout 链接”对话框。请花点时间重新调整 SailWind Logic 和 SailWind Layout 应用程序窗口的大小和位置，使它们各自覆盖一半的屏幕。
    

提示：重新排列窗口后，您可能需要调整 SailWind Logic 和 SailWind Layout 中视图的大小。在每个程序中，按下 Home 键即可使视图在重新排列的窗口中居中。

4.  为了减少使用 SailWind Layout 所需的设置，您将导入一个包含本教程所需的一些基本 PCB 元素的文件。

a. 在 SailWind Layout 中的文件菜单上，单击导入。
b. 在 \\SailWind Projects\\Samples 文件夹中找到并导入逻辑 tutorial.asc 文件。

**将网络表发送到 SailWind Layout**

使用 SailWind Layout Link 自动生成并将网络表发送到 SailWind Layout。

在 SailWind Layout Link 对话框中的“设计”选项卡上，单击“发送网表”，即可从 SailWind Logic 生成网表并将其发送到 SailWind Layout。此过程完成后，所有元器件均已定位到设计原点，准备进行布局。

提示：如果出现提示“原理图网络列表可能有错误。是否要继续？”，请单击“是”。

**原理图驱动的布局**

现在您已经拥有了包含原理图中元件和网络的 SailWind Layout 设计，接下来需要准备元件进行放置。您还需要将 SailWind Layout 设置为“移动”模式，以便在 SailWind Logic 中选择元件时，所选元件会随之移动。

**在 SailWind 布局中**

使用“分散元件”命令将元件分布在电路板轮廓的外部。

1.  在工具菜单上，单击分散组件，然后单击是以确认分散。
2.  单击“Board”按钮可使视图适合电路板轮廓。

启用移动组件动词模式。

L 1. 在工具栏上，单击设计工具栏按钮打开设计工具栏。由 2. 在设计工具栏上，单击移动按钮将 SailWind Layout 置于移动组件模式。

**在 SailWind Logic 中**

在 SailWind Logic 中选择 J1 组件。

1.  在“选择”工具栏上，单击“无”过滤器按钮，然后单击“零件”过滤器按钮将 SailWind Logic 置于仅支持组件选择的模式。
2.  选择原理图逻辑表左侧的 J1 连接器的任意引脚。
3.  将鼠标指针移至 SailWind Layout 窗口。您现在正在 SailWind Layout 中移动 J1。

**在 SailWind 布局中**

将组件放置在 SailWind 布局中。

1.  单击鼠标右键，然后单击“另一面”。
2.  通过输入 S 1650 400 并按 Enter 键将其定位到 X1650,Y400。
3.  按空格键放置 J1。
4.  在设计工具栏上，单击选择按钮退出移动模式

**SailWind Logic 中的多项选择**

您还可以通过在 SailWind Logic 中进行组选择并在 SailWind Layout 中应用“移动顺序”命令来按顺序移动多个组件

**在 SailWind Logic 中**

在 SailWind Logic 中进行组选择。

1.  不选择任何内容，将指针放在原理图的左上角，然后单击并将指针拖向原理图的右下角。
2.  当多个组件被包含在选择矩形内时，松开鼠标按钮。
3.  一旦完成选择，SailWind Logic 中与您选择相对应的组件就会在 SailWind Layout 中被选中。

**在 SailWind 布局中**

按顺序移动组件。

1.  单击鼠标右键，然后单击“移动顺序”。
    
2.  单击“全部是”。
    
3.  单击放置第一个组件。结果：下一个组件将附加到您的指针上并可移动。
    
4.  继续放置零件，直到不再有组件附着到指针上。
    

**布局驱动的选择**

您还可以根据 SailWind Layout 中的选择来驱动 SailWind Logic 中的选择。

**在 SailWind Logic 中**

启用 SailWind Logic 来接收在 SailWind Layout 中所做的选择。

1.  在 SailWind Layout Link 对话框中，单击 Selection 选项卡。
2.  选中“接收选择”复选框以使 SailWind Logic 能够接收在 SailWind Layout 中所做的选择。

**在 SailWind 布局中**

在 SailWind Layout 中选择 Y1 组件。

1.  使用搜索并选择非模态命令，输入 ssy1 并按 Enter 键，找到并选择振荡器 Y1。结果：在 SailWind Layout 和 SailWind Logic 中，Y1 组件被选中。
2.  输入 ssc3 并按 Enter 键，搜索并选择 C3。这将演示 SailWind Logic 如何响应 SailWind Layout 中的选择，并自动更改工作表以显示该零件。
3.  输入 ssu6 并按 Enter 键，搜索并选择 U6。由于 U6 是多门控器件，因此在 SailWind Logic 中会选中该器件的所有门控。器件的每个门控都会在“选择”工具栏上的“搜索和选择”框中单独列出。

**在 SailWind Logic 中**

选择 U6 的特定实例。

1.  在“选择”工具栏上的“搜索和选择”列表中滚动浏览项目，然后点击“U6B”。选择将更改为仅包含 U6B。这就是在 SailWind Logic 中管理多门控部件选择的方法。
2.  不要保存该文件的副本。
3.  关闭 SailWind Layout Link 对话框和 SailWind Layout，而不保存任何更改。

您已完成与 SailWind Layout 教程的链接。