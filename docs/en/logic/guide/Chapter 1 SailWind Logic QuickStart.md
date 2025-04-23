# Chapter 1 SailWind Logic QuickStart  

SailWind Logic is a robust, multi-sheet, schematic capture solution that builds an effective front-end environment for SailWind Layout.  

Step 1 - Start a New Design   
Step 2 - Select the Sheet Size   
Step 3 - Add Parts and Connector Symbols   
Step 4 - Add Buses   
Step 5 - Add Connections to Parts, Connectors, and Buses   
Step 6 - Add Off-Page Symbols   
Step 7 - Add Power and Ground Symbols   
Step 8 - Print the Schematic   
Step 9 - Generate Reports   
Step 10 - Create a Layout Netlist  

## Step 1 - Start a New Design  

Launch SailWind Logic and start a new design from the Welcome Screen.  

**Procedure** 

1. Click the Windows Start $>$ SailWind [version] $>$ SailWind Logic menu item.   
2. On the Welcome Screen, click New.  

## Step 2 - Select the Sheet Size  

SailWind Logic starts with an empty schematic sheet of the default size. You can change the sheet size.  

**Procedure** 

1. Click the Tools $>$ Options menu item.  

2. In the Options dialog box, click the Design category.  

3. Select the size you want from the Sheet area:  

a. Choose the size of the sheet by clicking in the Size box and selecting from the dropdown list.   
b. Choose a corresponding sheet border by clicking Choose and selecting the appropriate border from the “Drafting Items” list of the “Get Drafting Item from Library” dialog box.   
c. Click OK to close the Get Drafting Item from Library dialog box.   
d. Click OK to close the Options dialog box.  

4. To maximize the sheet size within your viewing area, on the main toolbar, click the Sheet button.  

## Step 3 - Add Parts and Connector Symbols  

You can add parts and connector symbols to your design as needed.  

Adding a Part Adding a Connector Symbol  

### Adding a Part  

You can add parts to your design individually, or you can add multiple instances.  

**Procedure** 

1. Click the Schematic Editing Toolbar button, then click the Add Part button.   
2. In the Filter section of the Add Part from Library dialog box, set the Library to “All Libraries.”   
3. In the Items box, type the \* wildcard character, and click Apply.   
4. Select a part and notice the symbol of the part in the preview window. Click Add. The part in outline form attaches to the pointer and is ready for placement.   
5. Move the pointer to move the part to an appropriate location and click to place the part. Another copy of the selected part automatically attaches to the pointer for placement.  

![](/images/9b8ae109bc0070645ed4404f0fa15becd29537220f020b27d6bbf62586a1078e.jpg)  

Tip SailWind Logic automatically adds reference designators to parts as they are added.  

6. Click to place another part or press the Esc key to cancel the placement of the same part type.  

7. Click Close to close the Add Part from Library dialog box.  

### Adding a Connector Symbol  

Each pin of a connector has a unique symbol for the schematic. This results in multiple symbols that make up one part. All connector pins have the same reference designator to show that they are symbol pins of the same part.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Add Part button.   
2. In the Filter area of the “Add Part from Library” dialog box, select the “connect” library from the Library list, then click Apply.   
3. Select a connector symbol to add to the schematic and click Add.  

![](/images/21dbdf5ae83c5fe7b3daf7131b29ff1d1d35764c6d096c42708c5c4ccb818108.jpg)  

!Tip  

If the symbol faces the wrong direction when attached to the pointer, right-click and click the Alternate popup menu item. Right-clicking and clicking the Alternate popup menu multiple times enables you to choose one of any available symbols to represent the connector.  

4. Click to place the connector symbol.  

5. When you have finished placing all of the desired symbols, right-click and select Cancel or press the Esc key to end the placement mode.  

6. Close the dialog box.  

## Step 4 - Add Buses  

Buses are used to consolidate a group of nets into one connection. This eliminates the potential clutter of many nets going from, or to, the same location in the design.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Add Bus button.  

2. Click to start the bus, click to add the corner, and double-click to finish the shape.  

!Tip  

To remove the corner you just placed, press the Backspace key. To cancel the bus placement, press the Esc key.  

3. In the Add Bus dialog box, type a name for the bus in the Bus Name box.  

4. If the bus is to be used for strictly memory or data arrays, select Bit Format in the Bus Type area; otherwise, select Mixed Net.  

• Bit Format — The name of the bus must follow the bit format shown for arrayed connections.  

0 Tip [NN:NN] represents [LSB:MSB].  

Mixed Nets — The name of the bus must be unique. Add the names of all subnets to the Bus Nets area. The mixed net bus can also contain bit format connections. To enter values for a range, double-click the Start and End cells.  

5. Click OK.  

6. Click to place the bus name.  

## Step 5 - Add Connections to Parts, Connectors, and Buses  

Add connections to parts, connectors, and buses to define the connectivity of your design.  

**Procedure** 

1. Click the Schematic Editing Toolbar button and then click the Add Connection button.  

2. At the endpoint of a component pin, click to start a connection and draw the connection. The connections are orthogonal by default, and you must click to create corners.  

!Tip  

To remove the corner you just placed, press Backspace. To cancel the connection, press Esc.  

3. End the connection using one of the following methods:  

Click at the endpoint of another pin on a part or connector.   
• If you create a connection that ends in a bus, in the Add Bus Net Name dialog box, select the net from the Net name list and click OK.  

The connection and its name remain selected in the design.  

4. Place the label using one of the following:  

• If you are satisfied with the location of the net name label, click in empty space. • If the net name label is not in the correct location, right-click and click the Move popup menu item. The label attaches to the pointer. Click to place the label.  

## Step 6 - Add Off-Page Symbols  

When connections need to connect to a circuit on another schematic sheet in the design, an off-page symbol is used. The off-page symbol has multiple representations, similar to a connector.  

**Procedure** 

1. Create a connection from the pin of a part in the design.   
2. Right-click and click the Off-page popup menu item. The default symbol appears on the pointer for placement, attached to the end of the connection.   
3. If the symbol is not facing the correct direction, right-click and click the Alternate popup menu ite until you find the correctly oriented symbol.  

4. Click to place the symbol.  

5. In the Add Net Name dialog box, type the net name and click OK.  

## Step 7 - Add Power and Ground Symbols  

Power and ground symbols are added to the end of a connection and have different representations according to the ground or power name.  

**Procedure** 

1. Create a connection from the pin of a part.   
2. Click to make a corner and drag up for power or drag down for ground.   
3. Right-click and click the Ground popup menu item or Power depending on the connection and the direction it has been drawn. The default ground or power symbol appears on the pointer. Notice the name that is annotated to the connection is displayed on the status bar in the lower left corner. If you clicked Power, it is $+5V$ ; if you clicked Ground, it is GND.   
4. If you want a different voltage or ground, right-click and click the Alternate popup menu item for different graphical symbols and different names.  

## Step 8 - Print the Schematic  

When you have finished editing your design, you can print it for checking and documentation purposes.  

**Procedure** 

1. Click the File $>$ Print menu item.   
2. In the Print dialog box, click Options.   
3. In the Options dialog box, examine the Preview window. The outline within the larger area represents the area of the paper that will be taken up by the schematic. This plot area is often oriented perpendicular to the printed sheet. If this is the case, to maximize the design area on the printed sheet, click on the Orientation box (in the “Positioning” area) and select 90 as the orientation angle; then click OK.   
4. Click the Properties button to make any printer changes before printing/plotting. Do not change the orientation of the sheet (Portrait to Landscape) as this will conflict with the orientation set previously in the Options dialog box.   
5. After completing this setup, click OK.  

## Step 9 - Generate Reports  

You can generate a number of different reports for design analysis.  

**Procedure** 

1. Click the File $>$ Reports menu item.  

2. In the Reports dialog box, click what you want to report on, and click OK.  

![](/images/b2b41006f54c0b3cf81ef3b2c46fcb452555f5f9a7e56c92b9deb518140bd62b.jpg)  

!Tip  

You can report on more than one item at a time, with each item generating a report (TXT file). These reports open in the default text editor and are formatted with a default set of customizable options.  

**Results**  

The report generates and a link to the report displays in the Output window. Click the link to view the report.  

## Step 10 - Create a Layout Netlist  

You can create a Layout netlist to examine the database and to pass the design data to SailWind Layout.  

**Procedure** 

1. Click the Tools $>$ Layout Netlist menu item. The default name of the netlist is default.asc, unless you saved the schematic.  

2. Give the file a unique name and click OK. The netlist opens in the default text editor for viewing.  

0 Tip If you saved the schematic, the default name of the netlist (the Output File Name) is the name of the schematic followed by an .asc file extension.  

