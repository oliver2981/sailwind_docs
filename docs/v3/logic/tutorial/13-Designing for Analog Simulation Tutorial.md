# 模拟仿真设计教程

模拟器件需要特殊的模拟属性。SPICE 网表功能使用模拟属性为 SPICE 仿真器构建 SPICE 网表。SPICE 模型也可以链接到器件，为 SPICE 网表生成器提供所需的值。

# 在本课中：

创建 RLC 电路 创建运算放大器电路 将模型添加到库中

# 限制

本教程需要 SailWind SPICEnet 许可选项。在“帮助”菜单上，点击“已安装选项”以确定是否可以继续。

# 准备

如果尚未运行，请启动 SailWind Logic。

# 创建 RLC 电路

使用模拟元件构建电阻-电感-电容电路。为元件添加模拟属性，以便将其添加到 SPICE 工具的网表中。

# 开始新的原理图

单击“新建”按钮。出现提示时，单击“否”以保存文件。

# 添加香料库

设计的部件位于 Spice 库中。请将该库添加到库管理器。

1.  文件菜单 $>$ 库。
2.  在“库管理器”对话框中，单击“管理库列表”。
3.  在“库列表”对话框中，单击“添加”。
4.  在添加库对话框中，选择 spice 库并单击打开。
5.  在库列表中选中香料库，点击向上按钮，直到香料库位于
    位于列表顶部。
6.  单击“确定”。
7.  在“库管理器”对话框中，单击“关闭”。

# 添加模拟部分

通过在原理图中添加所需部件来开始构建 RLC 电路。

1.  添加零件按钮
    
2.  在“从库添加零件类型”对话框的“过滤器”区域中，确保 Spice 库已列在“库”列表中，且“项目”框包含“\*”以显示所有库项目。如果过滤器中有任何更改，请单击“应用”。
    
3.  选择 CAP0805 电容器，然后单击添加。
    

# 需绘制的电路

![](/logic/tutorial/e68600bad48977e84bd9762c1a69ad13d910afdc5cd12508dc5971275947ebc3.jpg)

4.  单击以将电容器放置在原理图中。
5.  按 Esc 键取消添加额外的电容器。
6.  在“从库添加零件”对话框中，对以下零件类型重复步骤 3-5。

<table data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><tbody data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">零件类型</td></tr><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td>IND-MOLDED</td></tr><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td>RES0805</td></tr><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">电压供应*</td></tr></tbody></table>

\*如果出现提示，请使用 V 作为字母前缀。7. 完成后，单击“从库添加零件”对话框中的“关闭”。

# 添加与模拟部分的连接

连接所有组件，使用上一节中的图片作为指导。

1.  添加连接按钮
    
2.  选择一个图钉来开始连接，单击以创建角，然后选择一个图钉来完成
    你的连接。
    
3.  选择电容器和电压源之间的连接。
    
4.  拖动以创建电源存根，向下移动指针。
    
5.  单击鼠标右键，然后单击“地面”。
    
6.  单击以放置地面符号。
    
7.  按 Esc 退出添加连接模式。
    

# 标记连接

标记组件之间的连接。标签使 SPICE 网表更易于理解。

1.  右键单击，然后单击“选择任意内容”。
2.  双击电源和电阻器之间的网络。
3.  在网络属性对话框中，选中网络名称标签复选框。
4.  在网络名称框中输入 INPUT，然后单击确定。
5.  对剩余网络重复步骤 2-4。使用
    下表。

<table data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><tbody data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">网络之间</td><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">网络名称</td></tr><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">电阻器和电感器</td><td>MID</td></tr><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">电感器和电容器</td><td>OUT</td></tr></tbody></table>

接地连接会自动加上接地符号标记。

# 审查模拟属性

属性已添加到库或原理图中的元件。检查原理图中元件上预定义的 SPICE 属性。

1.  右键单击 $>$ 选择零件 $>$ 选择一个零件 $>$ 右键单击​​ $>$ 属性。
2.  在“零件属性”对话框中，检查“Sim.Analog.Order”和“Sim.Analog.Prefix”属性。所有模拟属性都包含前缀“Sim.Analog”。
3.  单击“确定”关闭“零件属性”对话框。
    提示：您可以在“帮助”中找到 SPICE/Analog 属性的详细列表。在“帮助”的“主题”选项卡中，指向“SPICE 网表属性词汇表”。

# 设置网络列表

SPICE Netlister 为几种不同的 SPICE 工具创建网表格式。

1.  工具菜单 $>$ SPICE 网表。
2.  在 SPICEnet 对话框的选择工作表列表区域中，选中工作表 1 复选框。
3.  在输出格式列表中，选择您将使用的 SPICE 软件的供应商格式。
4.  单击“模拟设置”。
5.  选中 AC 分析复选框。
6.  单击 AC 分析按钮。
7.  确保间隔设置为每十年 10 个点。
8.  确保频率从 1Hz 开始到 1kHz 结束，然后单击“确定”。
9.  在“模拟设置”对话框中单击“确定”。
10.  在 SPICEnet 对话框中单击“确定”以创建网络表。

# 检查网表

网络表在默认文本编辑器中打开，可以在导入 SPICE 软件之前查看或编辑。

1.  注意 AC 分析中的参数。
2.  请注意，连接和属性值列在引用的部分旁边。
3.  不要保存该文件的副本。

# 完成运算放大器电路

完成另一个常见的模拟电路——运算放大器电路。从库中添加一个运算放大器，并检查 SPICE 网表。

# 打开运算放大器电路

单击打开按钮，打开 \\SailWind Projects\\Samples 文件夹中名为 opamp.sch 的文件。

# 添加缺失的运算放大器

1.  添加部件按钮
2.  在“从库中添加零件类型”对话框中，选择 OP-471 零件，然后单击“添加”。
3.  将零件放置在原理图中的开放式连接上，然后单击以放置
    门。
4.  按 Esc 键取消添加额外的运算放大器门。
5.  单击“从库中添加零件类型”对话框中的“关闭”。

# 添加属性值

将网络名称值添加到放大器的模拟属性中。

1.  不选择任何内容 $>$ 右键单击​​ $>$ 选择零件。
    
2.  选择 U1-A 零件。
    
3.  右键单击，然后单击属性。
    
4.  双击 Neg 属性的值框。
    
5.  在值框中输入 OP\_VIN。
    
6.  重复步骤 4 和 5，并对每个属性使用以下值。
    

<table data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><tbody data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">属性</td><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">价值</td></tr><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">出去</td><td>VOUT</td></tr><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">位置</td><td>GND</td></tr></tbody></table>

7.  单击“确定”。

# 设置网络列表

1.  工具菜单 $>$ SPICE 网表。
    
2.  在 SPICEnet 对话框的“选择工作表”列表中，选中“工作表 1”复选框。
    
3.  在输出格式列表中，选择您将使用的 SPICE 软件的供应商格式。
    
4.  单击“模拟设置”。
    
5.  选中“瞬态”复选框并清除所有其他复选框。
    
6.  单击“瞬态”按钮。
    
7.  确保以下参数存在。
    

<table data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><tbody data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">范围</td><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">价值</td></tr><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">数据步长时间</td><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">1毫秒</td></tr><tr data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499"><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">总分析时间</td><td data-immersive-translate-walked="b5f3c362-7258-4a8e-9342-1fc1e071c499" data-immersive-translate-paragraph="1">10毫秒</td></tr></tbody></table>

8.  选中使用初始条件复选框，然后单击确定。
    
9.  在“模拟设置”对话框中单击“确定”。
    
10.  在 SPICEnet 对话框中单击“确定”以创建网络表。
    

# 检查网表

检查网表是否有错误。

注意这一行\*无法打开数据文件 lm741n.mod。

提示：原理图中的放大器是指模拟模型，并且库中没有模型文件。

# 将模型添加到库中

向库中的 lm741 部件添加 SPICE 模型，为网络列表编制者提供仿真所需的基本值。

1.  使用资源管理器窗口，导航到您的库文件夹。C:<install\_folder><version>\\ Libraries\\
2.  添加一个名为 spice 的新文件夹。
3.  在 spice 文件夹中，添加一个名为 Analog Models 的新文件夹。
4.  从 C:\\SailWind Projects\\Samples 文件夹复制 lm741n.mod 文件并将其粘贴到 Analog Models 文件夹中。

# 运行 SPICE Netlister

使用库中添加的模型创建无错误的 SPICE 网表。

1.  工具菜单 $>$ SPICE 网表。
2.  确保您的设置没有改变。
3.  在 SPICE Netlist 对话框中单击 OK 即可创建网络表。
4.  单击“是”覆盖现有文件。
5.  检查网络表以查看其他 SPICE 模型信息。

您已完成创建库零件教程。