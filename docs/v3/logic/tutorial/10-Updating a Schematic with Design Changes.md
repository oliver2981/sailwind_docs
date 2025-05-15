# 使用设计变更更新原理图教程

在典型的工程环境中，设计修改通常以工程变更单 (ECO) 的形式记录。在设计中实施这些变更可能需要替换引脚和栅极、删除或添加部件、删除或添加网络、重命名组件、重命名网络或更改部件类型。SailWind Layout 提供工具来快速实施这些修改，并准确记录这些修改，以便存档并添加到原理图中。

在 SailWind Layout 中执行的 ECO 变更会记录在一个扩展名为 \*.eco 的 ASCII 文件中。该文件以其原生格式，可以被 SailWind Logic 读取，从而将 SailWind Layout 中所做的变更添加到原理图注释中。

# 在本课中：

导入 ECO 文件比较文件并导出 ECO 文件

# 准备

如果它尚未运行，请启动 SailWind Logic 并打开 \\SailWind Projects\\Samples 文件夹中名为 preview.sch 的文件。

# 导入 ECO 文件

检查原理图中的几个参考指示器。现在导入一个 .eco 文件。

1.  文件菜单 $>$ 导入。
    
2.  如果出现“加载前保存文件”消息，请单击“否”。
    
3.  在文件类型列表中，单击 ECO 文件 (\*.eco)。
    
4.  选择 \\SailWind Projects\\Samples 文件夹中的 previewassy.eco 文件，然后点击“打开”。结果：原理图上的所有参考指示器均已更新。原理图已重新绘制，并会显示一条消息，告知您 ECO 流程已完成。
    
5.  单击“确定”。
    

# 比较文件并导出 ECO 文件

您可以使用 Compare/ECO 命令比较原理图和设计文件，并创建用于更新 SailWind Layout 的 ECO 文件。

1.  打开名为 previeweco.sch 的文件。请勿保存对 preview.sch 文件的更改。本教程设计中已添加一个额外的电容 (C11)。
    
2.  在工具菜单上，单击比较/ECO。
    
3.  在比较/ECO 对话框中，单击文档选项卡。
    
4.  在“要比较的原始原理图设计”区域中，单击“浏览”。选择 preview.sch 设计，然后单击“打开”。
    
5.  在“输出选项”区域中，单击“浏览”。将输出文件命名为 \\SailWind Projects\\Samples 文件夹中的 previeweco.eco，然后单击“保存”。
    
6.  点击“运行”。输出窗口中将显示指向 previeweco.eco 文件的链接。检查后关闭该文件。可能会打开一个或多个 ecogtmp.err 文件，其中包含正在比较的文件的相关信息。您可以关闭这些文件。
    
7.  启动 SailWind Layout 并打开位于 \\SailWind Projects\\Samples 文件夹中名为 preview.pcb 的文件。
    
8.  在“视图”菜单上，单击“范围”。
    
9.  在文件菜单上，单击导入。
    
10.  在文件类型列表中，单击 ECO Files (\*.eco)，选择\\SailWind Projects\\Samples 文件夹中的 previeweco.eco 文件，然后单击打开。
    
11.  点击“确定”。新的电容 C11 将位于原点附近。
    
12.  关闭 SailWind Layout 而不保存任何更改。
    

# 使用 SailWind Layout Link 自动进行前向注释

您可以使用 SailWind Layout Link，只需单击按钮即可自动将原理图中的注释更改转发到 SailWind Layout。

1.  打开名为 previeweco.sch 的文件。请勿保存对 preview.sch 文件的更改。本教程设计中已添加一个额外的电容 (C11)。
    
2.  在“工具”菜单上，单击“SailWind 布局”。
    

提示：如果 SailWind Layout 尚未打开，则会显示“连接到 SailWind Layout”对话框。单击“打开”即可启动包含原始设计的新 SailWind Layout 会话。在“文件打开”对话框中，选择 preview.pcb 文件，然后单击“打开”。

3.  在 SailWind Layout Link 对话框中，单击 Design 选项卡。
    
4.  可选：如果您想在更新前检查设计差异，请点击“比较 PCB”按钮。系统会比较两个版本，并将差异写入 \\SailWind Projects 文件夹中的 logic.rep 文件。要查看报告，请点击“输出窗口”中的 logic.rep 链接。
    
5.  在“设计”选项卡上：