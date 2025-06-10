# 设计规则检查

Design Verification 命令可检查设计中的间距、连通性、高速和平面层错误。这种高级间距检查快速准确，精度达0.00001英寸。通过SailWind Router的Design Verification命令，您可以检查以下间距规则违规：

- 网络与所有对象的间距

- 同网络限制

- 最小/最大线宽

如果您还拥有可选的安全功能（如SailWind高速布线和DFM），则可进行以下额外检查：

- 网络和引脚对长度

- 差分对

- 自动测试违规

- 制造检查

**本课内容：**

- SailWind Router与SailWind Layout的设计验证对比

- 在SailWind Router中检查设计规则

- 在SailWind Layout中检查设计规则

**限制条件**

本教程需要Verify Design安全选项。在SailWind Router中，点击帮助菜单中的**Installed Options**以确认您是否可以继续。

**准备工作**

如果尚未运行，请启动SailWind Router并打开\SailWind Projects\Samples文件夹中的**previewrouterverify.pcb**文件。

## SailWind Router与SailWind Layout的设计验证对比

SailWind Router包含许多高级功能，包括可选的组件规则高速设计规则支持、SMD过孔、差分对和等长规则。使用这些高级规则的设计可以通过SailWind Router中的Design Verification命令进行检查。

SailWind Layout不支持这些高级功能的设计验证；但是，您可以在SailWind Layout中访问组件规则、SMD过孔、差分对和等长规则的检查。这样您就可以在不来回切换SailWind Layout和SailWind Router的情况下查找和修正设计错误。

## 在SailWind Router中检查设计规则

**Options按钮 > Design Verification选项卡**

SailWind Router中的Design Verification工具会扫描设计数据库，查找所有设计规则违规。如果检测到错误，它们会以错误符号标记并在电子表格窗口中列出。

**执行完整间距检查**

1. 您可以使用此选项卡上的选项设置设计验证。或者，点击Design verification scheme name列表中的预定义方案之一。

2. 您可以检查整个设计或仅检查工作区中可见的部分设计。检查范围由Conduct checks区域决定。

如果选中**In visible workspace only**复选框，请使用缩放命令调整设计比例并设置检查区域。如果清除**In visible workspace only**复选框，则无论工作区中可见的区域如何，都会检查整个设计。

3. 在Conduct checks区域，选中**On visible objects and layers only**复选框以仅检查可见对象。清除该复选框可检查设计中的所有内容，即使对象或整个层不可见。

**提示：** 使用Options对话框中的Display选项卡更改对象和层的可见性。

4. 在Check design for区域，选中**Object Clearance**复选框。

5. 确保选中**Net against all objects**、**Keepout restrictions**和**Objects against board outline**复选框。清除所有其他复选框。

6. 点击**OK**退出Options对话框。

7. 要检查设计，请点击Design Verification工具栏上的**Verify Design**按钮。**替代方法：** 点击Tools菜单中的Verify Design。

**查看间距错误**

设计中会包含错误。使用以下方法之一检查错误：

- 使用电子表格窗口Errors选项卡中显示的错误报告获取发现的错误信息。

- 在Selection Filter工具栏上，点击**Errors**按钮，选择设计中的错误标记，右键点击并选择**Properties**。将显示Error Properties对话框。您可以使用SailWind Router的布局和布线工具修正错误。

完成后，请勿保存设计副本。

**您已完成设计验证教程。**