# 第 2 章 交互式布线快速入门

如需手动布线而非使用自动布线流程，您可以对设计的全部或部分进行手动布线。

请按照以下步骤快速开始。

或者，您可以观看 SailWind Layout 和 SailWind Router 的入门视频了解网表项目，或查看 SailWind Router 网表项目介绍视频了解所有高级功能，用于布局和布线您的设计。


🙊**限制**

某些选项卡或功能的访问可能需要您的 SailWind Router 配置中未提供的选项

1. [步骤 1 打开 SailWind Layout 文件](#page-0-0)

2. [步骤 2 设置默认设计属性](#page-1-0)

3. [步骤 3 交互式布线](#page-2-0)

4. [步骤 4 交互式布线时推挤走线](#page-3-0)

## 步骤 1 - 打开 SailWind Layout 文件

SailWind Router 可读写原生 SailWind Layout 设计文件。请按照以下步骤加载 SailWind Layout 文件。

🏃‍♂️‍**步骤**

1. 在标准工具栏上，点击 **打开** 按钮。

2. 在文件类型列表中，选择 **PCB 设计文件 (\*.pcb,\*.bre)**。

3. 点击您需要的 SailWind Layout 设计文件，然后点击 **打开**。例如，打开 *C:\SailWind Projects\Samples* 文件夹中名为 *previewplaced.pcb* 的文件。该文件将在 SailWind Router 中打开。

4. 如果加载的文件包含走线，请使用取消布线功能删除所有走线。

	- 在设计区域右键点击并选择 **选择网络** 弹出菜单项。

	- 右键点击并选择 **全选** 弹出菜单项。所有网络将被选中。

	- 右键点击并选择 **取消布线** 弹出菜单项。

> 替代方案：按 Delete 键。

## 步骤 2 - 设置默认设计属性

在 SailWind Layout 中设置的所有设计属性和设计规则会自动转移到 SailWind Router，尽管您可以在 SailWind Router 中更改它们。SailWind Router 还具有一些额外的独特属性。

🏃‍♂️‍**步骤**

1. 在标准工具栏上，点击 **特性** 按钮。

2. 使用对话框中的选项卡分配特性。参见[表](#page-1-1)[3](#page-1-1)。

3. 点击 **确定** 关闭属性对话框。某些选项卡或功能的访问可能需要您的 SailWind Router 配置中未提供的选项。

   | 选项卡                | 用途                                   |
   | --------------------- | -------------------------------------- |
   | 间距(Clearance)       | 分配默认对象到对象的间距。             |
   | 同网络(Same net)      | 分配默认同网络对象到对象的间距。       |
   | 布线(Routing)         | 分配默认走线宽度、默认拆线和推挤偏好。 |
   | 过孔偏好(Via Biasing) | 分配默认过孔类型偏好。                 |
   | 层偏好(Layer Biasing) | 分配默认层偏好。                       |
   | 测试点(Test Points)   | 分配默认测试点间距和残段长度。         |
   | 层(Layers)            | 启用层，设置其成本并分配其布线方向。   |
   | 网格(Grid)            | 分配默认网格值。                       |
   | 扇出(Fanout)          | 为从 SMD 焊盘扇出分配参数。            |
   | 焊盘入口(Pad Entry)   | 分配走线进出焊盘的规则。               |
   | 拓扑(Topology)        | 分配走线拓扑偏好。                     |

   **表 3. 设计属性选项卡**

4. 有关每个选项卡的更多信息，请点击选项卡中的 **帮助**。

## 步骤 3 - 交互式布线

交互式布线允许您手动选择所需的走线路径。您可以通过预先设置某些选项和启用某些功能来设定交互式布线期间的软件自动输入级别。

[设置交互式布线选项](#page-2-1) [交互式布线](#page-3-1)

### 设置交互式布线选项

在交互式布线前设置您的设计选项。

您可以按需更改选项；不过，以下程序提供了推荐的初始设置。

🏃‍♂️‍**步骤**

1. 点击 **工具 > 选项** 菜单项 > **布线** 类别 > **常规** 子类别。

2. 在"布线角度"区域，选择您偏好的角度（正交、对角线或任意角度）。

3. 在交互式布线区域，清除"动态布线"复选框。

   > [!tip] 交互式布线时，每次添加一个线段。当您选中动态布线复选框时，移动指针时会自动添加多个线段和拐角。

4. 在推挤器区域，选中"启用推挤器"复选框。特定软件配置能够在交互式添加走线时推挤和移动走线。这是通过启用推挤器实现的。推挤器将在后续步骤中使用。推挤器会推开和移动走线以帮助您布线。

5. 点击"跟随指针推挤"选项。这允许您无需点击即可进行推挤。

6. 点击实时推挤。这会立即推挤而无需引导走线到开放区域。

7. 查看交互式布线区域和选项对话框其他选项卡中的其他设置。

   > [!warning] 在 **颜色** 选项卡上，确保"连接"颜色设置为可见颜色。

8. 点击 **确定**。

### 交互式布线

SailWind Router 可以智能地布线您的连接，响应路径中的障碍物并相应调整走线以确保满足设计规则。

🏃‍♂️‍**步骤**

1. 右键点击并选择 **选择未布线/管脚** 弹出菜单项。

2. 在工作区中选择一个未布线或管脚。

3. 右键点击并选择 **交互式布线** 弹出菜单项。

   > 替代方案：按 F3 键。

4. 移动指针并点击创建走线中的每个拐角。

   > [!tip] 当您在选项对话框 > **布线** 类别 > **常规** 子类别中选择动态布线复选框时，您无需点击添加拐角。拐角和线段会自动添加。

5. 当完成点上出现单圈或双圈时，点击您想要完成走线的对象。

> 替代方案：当指针靠近您想要完成走线的对象时，右键点击并选择 **完成** 弹出菜单项。

## 步骤 4 - 交互式布线时推挤走线

启用推挤器后，交互式布线器会为您正在布线的走线清理路径，同时保持现有连接。

🏃‍♂️‍**步骤**

1. 选择一个未布线或管脚，右键点击并选择 **交互式布线**。布线时请注意，如果您尝试跨越另一条走线，或接近小于最小走线间距，另一条走线会推开以保持最小间距。

2. 布线时，右键点击并注意您的推挤选项。尝试推挤选项。参见[表](#page-3-2)[4.](#page-3-2)

3. 完成连接。布线时，您可以临时更改推挤设置以完成走线。


| 命令           | 用途                                                                     |
|----------------|--------------------------------------------------------------------------|
| 向后推挤走线 | 允许在交互式布线时将走线推挤到指针后方 |
| 不推挤        | 关闭当前走线的推挤功能                                 |

**表 4. 推挤器选项**

| 命令                   | 用途                                                                                                                                      |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 点击后推挤          | 在您点击拐角后重新布线障碍物。如果选择点击后推挤<br>，它只会在您点击输入拐角或过孔后推挤。 |
| 跟随指针推挤         | 在移动指针时重新布线障碍物                                                                                                   |
| 拆除阻碍走线 | 取消布线障碍物                                                                                                                           |
