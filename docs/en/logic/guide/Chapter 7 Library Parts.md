# Chapter 7 Library Parts  

The processes associated with creating, managing and editing library parts contain many levels of detail. You can use the Decal Editor to create CAE decals (schematic symbols) including the editing of gates, terminals, pins, pin numbers, sequence numbers, attribute labels, and then use the Part Editor to incorporate the data into part types.  

Part Editor Operations   
Object Selection Control in the Decal Editor   
Changing and Updating Library Parts   
Creating New Parts from Existing Parts   
Save the Part/Decal to the Library   
Selecting Multiple Objects in the Decal Editor   
CAE Decals   
Part Types  

## Part Editor Operations  

Use the Part Editor to create and modify standard schematic symbols such as gates, resistors, capacitors, connectors, etc., and special symbols such as ground/power and off-page references. You also use the Part Editor to create new CAE decals, pin decals, and assign PCB decals, the physical representation of the part in a PCB design system.  

You can access the Part Editor by clicking the Tools $>$ Part Editor menu item, or clicking the Edit button in the Library Manager dialog box.  

Unneeded menu commands and toolbar buttons are removed or replaced with menu commands and toolbar buttons specific to creating and modifying parts.  

A SailWind Logic part is comprised of the three elements shown in the following table:  

Table 15. SailWind Logic Part Elements   

| Element   | Description                                                  |
| --------- | ------------------------------------------------------------ |
| Part Type | The electrical information for a part. This includes the logic family, CAE Decal assignment, part name, connection pins, gate swapping information, attributes, etc. See also Modifying Electrical Information for a Part. |
| Decal     | gate. See also Creating a New CAE Decal.                     |
| PCB Decal | The_graphical representation of the part when it is drawn in the PCB design program. It is often referred to as the footprint. Assigning a PCB Decal is optional and only required if you are passing a netlist to SailWind Layout. |

• Changing and Updating Library Parts Creating Single Gate Parts Creating Multigate Parts Creating New Parts from Existing Parts Creating a New Connector Creating a New CAE Decal Creating a New Pin Decal Special Schematic Symbols  

## Object Selection Control in the Decal Editor  

You can control object selection using the preset filter settings, or you can use the Selection Filter dialog box.  

Controlling Object Selection Using Preset Filter Settings Controlling Object Selection Using the Selection Filter Dialog Box  

### Controlling Object Selection Using Preset Filter Settings  

You can control object selection using the preset filter settings that are available from the right mouse button menu. This enables quick access for selecting terminals, labels, drafting items or anything.  

**Procedure** 

1. Right-click in the Decal Editor.   
2. Click Select Terminals, Select Labels, or Select Drafting Items. To select all of these options, click Select Anything.  

### Controlling Object Selection Using the Selection Filter Dialog Box  

You can control which objects you can select by using the Selection Filter dialog box. This provides quick access for selecting parts, gates, nets, pins, buses, connections, 2D lines, text and other design objects.  

**Procedure** 

1. Do one of the following:  

• Click the Edit $>$ Filter menu item.   
• Right-click in the workspace and click Filter.   
• Right-click in the Decal Editor and click Filter.  

The Selection Filter dialog box appears.  

See alsoUsing the Selection Filter.  

2. Select one or more of the items, for example: Pins, Labels, 2D Lines, or Text. To select all of these options, click Anything. To clear all of the options, click Nothing.  

3. Click Close.  

**Related Topics**  

Selecting Multiple Objects in the Decal Editor  

## Changing and Updating Library Parts  

When you add a part to a schematic, SailWind Logic creates a copy of the library part and adds it to the schematic database. Thereafter, the schematic representation is uncoupled from the library. Modifying a part in the Part Editor will only affect the library entry of that part, not the current version of the part type in the schematic.  

**Related Topics**  

Modifying Parts The Update From Library Function  

## Creating New Parts from Existing Parts  

You can create a new part by adapting an existing part. Make a copy of an existing CAE decal if pins need to be added or deleted. Modifying an existing CAE Decal without first making a copy will modify all parts that use that decal.  

**Prerequisites**  

• Verify which CAE decal is referenced by the part you are going to copy.   
• Modify that CAE decal and save it with a new name.  

**Procedure** 

1. In the Part Editor, click the File $>$ Open menu item, or click the Open button on the toolbar.   
2. In the Select Type of Editing Item Dialog Box, click CAE Decal and then click OK. The Get Gate Decal from Library dialog box displays.   
3. In the Items box, type a wildcard or expression on page 105 to filter the symbols, and click Apply.   
4. Click OK. You enter the Decal Editor and the decal appears.   
5. Modify the decal as required.   
6. Click the File $>$ Save As menu item. The Save CAE Decal to Library dialog box displays.   
7. Type a name for the new CAE decal and select a library folder.   
8. Click OK.   
9. Click the File $>$ Exit menu item.  

!Note:  

Making a copy of the part uses the same process as making a copy of the CAE decal, except you select Part Type instead of selecting CAE Decal from the Select type of editing item dialog box.  

• Change both the CAE decal and the electrical information, then save it as a new part.   
• You can rename a modified decal that you accessed through the part type.  

See also Saving Part Types.  

## Save the Part/Decal to the Library  

From within the Part Editor, you can save a part/decal to the library. After adding the part to the library, you can then place it into a design.  

**Procedure** 

1. Click the File $>$ Save As menu item.   
   The Save Part and Gate Decals As dialog box appears.   
2. Select a library folder for the new part. The default is C:\<install_folder>\<version>\Libraries.   
3. Type a name for the new part or decal.   
4. Click OK.   
5. Click the File $>$ Exit Part Editor menu item.  

![](/images/c2ff244e1ef9815ba90f686c257069d6b8e84f5de23f9c333d3b83166b507d40.jpg)  

Tip   
A checking routine is executed when you save a part. Resolve all errors before exiting the Part Editor; parts with errors cannot be added to the schematic.  

## Selecting Multiple Objects in the Decal Editor  

You can select multiple objects in the Decal Editor. This enables you to move, rotate of mirror multiple objects simultaneously.  

**Procedure** 

1. Use the Filter Selection to determine which objects you can select. See also Object Selection Control in the Decal Editor.  

2. Do one of the following:  

Right-click in the Decal Editor and select a filter, or click Select All to select all of the objects that are selected in the Filter Selection dialog box.   
Click and drag over the objects you want to select.   
Ctrl+click on each object you want to select.  

![](/images/49462c3067e4137af8005f7e0e4245393b0f4a2cdf22de76e9bf41d9557f9a6c.jpg)  

!Tip  

When moving multiple objects in the Decal Editor, right-click to access the Rotate 90, X Mirror, and Y Mirror commands.  

## CAE Decals  

Use the CAE Decal Editor to create and edit CAE Decals, otherwise known as schematic symbols or logic decals.  

Constructing the New CAE Decal   
Using the Decal Wizard   
Manually Construct the New Part   
Creating a New CAE Decal   
Creating Single Gate Parts   
Creating Multigate Parts   
Adding Terminals   
Changing Objects in the Decal Editor   
Setting a Pin Number   
Setting a Pin Name   
Setting a Pin Type   
Setting Pin Swaps   
Changing a Pin Number   
Changing a Pin Name   
Changing a Pin Decal   
Changing Sequence Numbers   
Attribute Labels   
Creating Attribute Labels   
Modifying Terminals   
Setting the Origin for a Part   
Getting Gate Decals From the Library   
Assigning Pin Information to the CAE Decal   
Saving a Modified Decal With a Different Name  

### Constructing the New CAE Decal  

Using the Part Editor you can construct a new CAE decal by adding gates and defining the logic family.  

**Procedure** 

1. Click the Tools $>$ Part Editor menu item.   
2. In the Part Editor, on the toolbar, click the Edit Electrical button. This displays the “Part Information for Part dialog box” on page 134.   
3. In the Part Information for Part dialog box, select the PCB Decals tab to assign the PCB decal. The pin count for the assigned PCB decal must be equal to or greater than the number in the electrical description.   
4. Select the Gates tab.   
5. Click Add, once for the each gate in the part. The gates are listed alphanumerically in the Gates multicolumn list box. 6. Double-click on the CAE Decal column for a gate, and then select the Browse (…) button. The Assign Decal to Gate dialog box appears.   
6. To filter the decals, type a wildcard or expression on page 105 in the Filter box, and click Apply.   
7. Click Assign. Click OK when you finish assigning decals for the gate.   
8. (Optional) Assign gate swapping information for the part. Refer to the Gates Tab on page 144 topic for additional information.   
9. Repeat steps 5 through 8 for the other gates.   
10. Click the Pins tab to use Pin Count to indicate the number of pins in the part. Enter the number of pins for the entire package including signal pins, not for an individual gate.   
11. On the General tab, select a Logic Family and Prefix from the list and other electrical information as required. See also Modifying Electrical Information for a Part.   
12. Click OK.  

**Results**  

The Part Editor now displays the assigned CAE Decal outlines. Note that no pin information appears.  

### Using the Decal Wizard  

Use the Decal Wizard dialog box to automatically create a new CAE decal. You must be in the Decal Editor mode of the Part Editor, and creating gate information, to use this feature.  

**Procedure** 

1. Click the Tools $>$ Part Editor menu item.   
2. In the Part Editor, on the standard toolbar, click the New button.   
3. In the Select Type of Editing Item dialog box, click CAE Decal, and click OK. You are now in the Decal Editor and ready to create a new CAE decal.   
4. Click the Decal Editing Toolbar button.   
5. Click the CAE Decal Wizard button.   
6. To set the horizontal and vertical distance from the terminal connection point to the decal outline, type a value or use the arrows to indicate the pin length in the Pin Length area.   
7. To set the horizontal and vertical distance between pins, type a value or use the arrows to specify the distance in the Pin Spacing area.   
8. To set the width of the decal outline, type a value or use the arrows in the Min Width box.  

![](/images/bc5db5136d178339bb64d0d2c5cc55f3abb6612720503cf190c912712b9a8188.jpg)  

Tip Pin decals are moved left or right to accommodate the box width.  

9. To set the minimum height of the decal outline, type a value or use the arrows in the Min Height box.  

![](/images/19a1694443ac0557c5a39105372d422782f8f32850992dfcf8e6c694ba405984.jpg)  

!Tip  

If you enter a value larger than needed to accommodate the number of input or output pins, space is added to the bottom of the decal.  

10. In the Left Pins area, select the pin decals for the left, or input, side of the part from the Pin Decal list, and then type the number of pins in the Pin Count box or use arrows to indicate the pin count.  

11. In the Right Pins area, select the pin decals for the right, or output, side of the part from the Pin Decal list, and then type the number of pins in the Pin Count box or use arrows to indicate the pin count.  

12. In the Upper Pins area, select the pin decal to use for the upper pins, and then type the number of pins in the Pin Count box or use arrows to indicate the pin count.  

13. In the Lower Pins area, select the pin decal to use for the lower pins, and then type the number of pins in the Pin Count box or use arrows to indicate the pin count.  

14. Click OK.  

**Results**  

The Decal Wizard creates a rectangle of the correct size, adds the pins, and creates place holders for the sequence number, pin number, pin type, and swap information.  

![](/images/fb3ccdb64a9fcbfcfa9085875156830aa280640abc73f18fc7e86c29b108d8e8.jpg)  

Tip Use the Part Editor Drafting toolbar to modify the basic information created by the decal wizard. You can add additional terminals, change the pin decal, or change the pin sequence number.  

### Manually Construct the New Part  

You can manually construct a new part for use in your design by creating the 2D line body shape, adding terminals, assigning pin numbers and pin names.  

**Procedure** 

1. Click the Tools $>$ Part Editor menu item.   
2. In the Part Editor, on the Part Editor toolbar, click the New button.   
3. In the “Select type of editing” dialog box, click Part Type, and click OK.   
4. On the Part Editor toolbar, click the Edit Graphics button. When prompted, click OK to confirm the   
   creation of a new part.  

5. On the Part Editor toolbar, click the Decal Editing Toolbar button to open the Symbol Editing toolbar.  

6. Click the Create 2D Line button, then construct the body of the decal. Refer to the Creating 2D Line Items topic for additional information.  

7. Click the Add Terminal button. See also Adding Terminals.  

8. Indicate the locations for the terminals.  

9. Right-click and click Cancel when finished adding terminals.  

10. Click the Set Pin Number button.  

11. In the Set Pin Number dialog box, in the Start pin number area, type values in the Prefix and/or Suffix boxes.  

A preview of pin numbers based on your input is displayed below the boxes.  

![](/images/fa9047a3ab59c6ac4426cd8b2a41e129990427e368f6f101d73863514ed3abdb.jpg)  

!Tip  

Exceptions can be applied:  

• Alphabetic and numeric values can be used in either box. For example, A1 or 1A.   
• For a single numeric, use either Prefix or Suffix box, and void the other box.  

12. In the Increment options area, choose what to increment by clicking either Increment prefix or Increment suffix.  

13. In the Step value box, type a positive or negative number to increase or decrease the pin numbers with consecutive or stepped values.  

14. If using alphanumerics, you can select the Use JEDEC pin numbering check box to ensure legal alphanumeric values are used.  

15. Click OK.  

16. Select each pin or pin text in ascending sequence to assign a number. You can click twice on a pin to skip a number.  

![](/images/c9181d9eac12827796de71da0ebcaed515ffc921d79352edcf90207ffc6c3850.jpg)  

Note: You can use the Change Pin Number button to change a pin number if necessary.  

17. Use the other options of the Symbol Editing toolbar to modify the pin numbers and add pin names, pin swapping information, pin type, etc.  

18. On the File menu, select Return to Part, and then click Yes when the keep changes to gate message appears.  

### Creating a New CAE Decal  

Creating a CAE Decal follows the same basic steps as creating a new packaged part. Start by placing SailWind Logic directly into decal editing mode, and then create the new CAE decal.  

**Procedure** 

1. Click the Tools $>$ Part Editor menu item.  

2. In the Part Editor, on the Part Editor toolbar, click the New button.  

3. In the Select Type of Editing Item Dialog Box, select CAE Decal.  

4. Click OK. Four text entries are displayed in the working area  

Table 16. CAE Decal Editing Mode - Text Entries In Working Area   

| Entry          | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| REF            | The default space reserved for the reference designator in the schematic. |
| PART-TYPE      | The default location of the part type name in the schematic. |
| * Free Label 1 | The default location for the first displayed attribute.      |
| * Free Label 2 | The default location for the second displayed attribute.     |

5. Construct the new CAE decal for the part manually or with SailWind-Logic’s Decal Wizard automatic part creation tool.  

• Use the Decal Wizard on page 116 to create the outline and add terminals. (Optional) Use the Part Editor Symbol Editing Toolbar to add additional terminals, change the pin decal, or change the pin sequence number.   
(Optional) Add additional attribute labels. See the Creating Attribute Labels topic for more information.  

6. Save the part on page 113 to the library.  

### Creating Single Gate Parts  

Single gate parts are parts that are represented by a single schematic symbol, such as an applicationspecific integrated circuit. Perform the basic procedure for creating a single gate part in the Part Editor.  

Creating a new part involves multiple steps, with dialog boxes and information windows to for assistance.   
See the referenced documentation in the steps that follow for additional information.  

In the following steps, you create the CAE Decal before entering electrical information. This causes the part type and the CAE decal to share the same name. If you want to use an existing CAE decal instead of creating a new one, specify the electrical information first.  

See also Creating Multigate Parts.  

**Procedure** 

1. Click the Tools $>$ Part Editor menu item.  

2. In the Part Editor, click the Edit $>$ CAE Decal Editor menu item, or on the Part Editor toolbar, click the Edit Graphics button.  

3. In the Select Gate Decal dialog box, enter a name for the decal and click OK when prompted to create a decal for the new part.  

Four text entries are displayed in the working area: REF is the default space reserved for the reference designator in the schematic. PART-TYPE is the default location of the part type name in the schematic. \*Free Label 1 is the default location for the first displayed attribute. \*Free Label 2 is the default location for the second displayed attribute.  

See also Attribute Labels.  

4. Construct the new CAE decal for the part manually on page 117 or with the automatic part creation tool in the Decal Wizard on page 116.  

5. Within the Part Editor, if you created the CAE decal in step 4 using the Decal Wizard, use the Decal Editing Toolbar to modify the pin numbers created by the decal wizard and add pin names, gate swapping information, and so forth.  

6. On the File menu, select Complete.  

7. Assign electrical information to the part.  

a. On the Part Editor toolbar, click the Edit Electrical button. The “Part Information for Part” on page 134 dialog box displays.   
b. Set the pin count to indicate the total number of pins in the part. This is mandatory if there are signal pins in the part that were not added when you created the CAE decal in the steps above. (Optional) Click the Decals tab to assign the PCB decal. The pin count for the assigned PCB decal must be equal to or greater than the electrical description.   
c. On the General tab, select a Logic Family from the list. See also Viewing and Setting General Part Information. (Optional) Select the Pins tab and assign power and ground signal information.   
d. Select the Attributes tab and assign bill of material and part list information.   
e. Click OK. The Part Editor displays the CAE Decal.  

8. Save the part on page 113 to the library.  

### Creating Multigate Parts  

Multigate parts are parts that use more than one symbol or gate to represent a complete part in the PCB design system, for example, a 7400. This topic discusses the basic procedure for creating a multigate part in SailWind Logic.  

See the referenced documentation in the topics below for additional information.  

The steps required to create a multigate part are as follows:  

1. Construct the new CAE decal on page 115 for the part.   
2. Assigning Pin Information to the CAE Decal   
3. Save the Part/Decal to the Library.  

### Adding Terminals  

A terminal consists of a pin decal and a series of text strings that define the terminal's number, swap data, etc.  

**Procedure** 

1. On the Decal Editing Toolbar, click the Add Terminal button.   
2. In the Pin Decal Browse dialog box, select a decal, then click OK. The pin decal attaches to the cursor.   
3. Move the cursor into position and click to anchor the pin. Before placing the terminal, you can use the popup menu to modify the orientation of the terminal and modify terminal information, including the pin number, pin name, pin type, and swap class. After a terminal is placed, a new terminal, identical to the first, is attached to the cursor for placement. If you defined a pin number or pin name, these are automatically incremented to the next number and name for the new terminal. If you assigned pin type and swap class, the values are copied to the new terminal.   
4. When finished, right-click and click Cancel.  

### Changing Objects in the Decal Editor  

Depending upon the object type that you select, you can choose between a number of different methods to change one or more objects in the Decal Editor. These include such operations as query/modify, move, copy, delete and combine or explode.  

**Procedure** 

1. Select the objects you want to modify. See also Selecting Multiple Objects in the Decal Editor.  

2. Right-click in the Decal Editor for editing options.  

3. Refer to the following table to see which editing options are available, depending on the objects selected.  

Table 17. Decal Editor - Editing Options Based on Selected Object   

| Objects Selected | Menu Commands Available                                      |
| ---------------- | ------------------------------------------------------------ |
| Drafting Items   | Query/Modify, Move, Copy, and Delete. Explode and Combine are available when multiple objects are selected. (See Modifying Drafting Objects) |
| Labels           | Move                                                         |
| Terminals        | Query/Modify, Move, Copy, and Delete (See Modifying Terminals) |
| Combination      | Move is available for any combination of objects. Copy and Delete are available for all objects except labels. |

### Setting a Pin Number  

Use Set Pin Number to assign pin numbers to several pins. The pin number is incremented each time you select a pin.  

**Procedure** 

1. On the Decal Editing toolbar, click the Set Pin Number button.  

2. In the Set pin number dialog box, in the Start pin number area, type values in the Prefix and/or Suffix boxes.  

A preview of pin numbers based on your input is displayed below the boxes.  

!Tip  

When entering pin numbers, observe the following:  

• Alphabetic and numeric values can be used in either box. For example, A1 or 1A.   
• For a single numeric, use either Prefix or Suffix box, and void the other box.  

3. In the Increment options area, choose what to increment by clicking either Increment prefix or Increment suffix.  

4. In the Step value box, type a positive or negative number to increase or decrease the pin numbers with consecutive or stepped values.  

5. If using alphanumerics, you can select the “Use JEDEC pin numbering” check box to ensure legal alphanumeric values are used.  

6. Click OK.  

7. Select each pin or pin text in ascending sequence to assign a number.  

You can click twice on a pin to skip a number.   
Use the Change Pin Number button in the Editing Toolbar within the Part Editor to change a pin number if necessary.   
Right-click and click Cancel when finished.  

### Setting a Pin Name  

Use Set Pin Name to add or change the name for several pins. Pin names label the function of a pin, for example, CLK, DATA0, and so forth. The suffix of the name increments each time you select a pin. This command does not check for duplicate naming conventions.  

Precede the text with the backslash character (\) to add a bar over the text characters.  

**Procedure** 

1. On the Decal Editing toolbar, click the Set Pin Name button.  

2. Type the pin name in the information window.  

3. Click OK.  

4. Select each pin to assign names.  

The pin name increments each time you click a pin, enabling you to assign pin names to a part sequentially (for example, D0, D1, D2, and so forth). To skip a particular pin name in the sequence, select the same pin until the desired pin name appears, then continue selecting other pins.  

5. Right-click and click Cancel when finished.  

6. Use the Change Pin Name button from the Part Editor Decal Editing toolbar to change the name of a single pin.  

### Setting a Pin Type  

Use Set Pin Type to change the type of pin the terminal represents, for example, load, source, and so on.   
You can choose between verb mode or object mode when performing this task.  

Setting a Pin Type Using Verb Mode Setting a Pin Type Using Object Mode  

#### Setting a Pin Type Using Verb Mode  

You can use verb mode to set pin types. Start the command and then select one or more objects to which you want to apply the command.  

**Procedure** 

1. On the Decal Editing toolbar, click the Set Pin Type button. The Pin Type information window appears.   
2. Select a pin type from the dropdown list box Table 18 lists the available pin types and their corresponding letters.   
3. Select the pins to which to apply the pin type information. The text string associated with the pin is modified to reflect the new pin type.   
4. Repeat steps 2 and 3 if necessary.   
5. Right-click and click the Cancel popup menu item to exit the verb mode.  

#### Setting a Pin Type Using Object Mode  

You can use object mode to set pin types. Select one or more objects and then select the command you want to use to perform an action on them.  

**Procedure** 

1. Select the decal pins to which to apply the pin type information.   
2. On the Decal Editing toolbar, click the Set Pin Type button. The Pin Type information window appears.   
3. Select a pin type from the dropdown list box. Table 18 lists the available pin types and their corresponding letters.  

4. Click OK.  

Table 18. Characters Used to Represent Pin Types   

| Letter | Represents this pin type |
| ------ | ------------------------ |
| B      | Bidirectional Pin        |
| C      | Open Collector Pin       |
| G      | Ground Pin               |
| L      | Load Pin                 |
| Ｏ     | Or-Tieable Source Pin    |
| P      | Power Pin                |
| Ｓ     | Source Pin               |
| T      | Tristate Pin             |
| U      | Undefined                |
| Z      | Terminator Pin           |

### Setting Pin Swaps  

Use Set Pin Swap to define a swap class for a terminal. The PCB layout software uses swapping information for length minimization and routing optimization. The swap class is assigned by a numeric value. The number for classes is 0, if the pin is not to be swapped under any circumstances, and 1 through 99. A pin can be swapped with any other pin within the gate that has the same swap class number.  

Setting Pin Swaps Using Verb Mode Setting Pin Swaps Using Object Mode  

#### Setting Pin Swaps Using Verb Mode  

You can set pin swaps using verb mode. Start the command and then select one or more objects to which you want to apply the command.  

**Procedure** 

1. On the Decal Editing toolbar, click the Set Pin Swap button.   
2. Type the number that identifies the swap class in the information window.   
3. Click OK.   
4. Select the pins to assign as this swap class.   
5. Right-click and click the Cancel popup menu item to exit the verb mode.  

#### Setting Pin Swaps Using Object Mode  

You can set pin swaps using object mode. Select one or more objects and then select the command you want to use to perform an action on them.  

**Procedure** 

1. Select the decal pins to assign as the swap class.   
2. On the Decal Editing toolbar, click the Set Pin Swap button.   
3. Type the character that identifies the swap class in the information window.   
4. Click OK.  

### Changing a Pin Number  

This command changes the number assigned to a pin. It does not check for duplicate numbering.  

![](/images/a12ddaf923a25df1e9bc24da275831292b6be2b5848a063049e5f5ca85fe06f1.jpg)  

Tip   
To assign numbers to several pins in an ascending sequence, use the Set Pin Number button from the Editing Toolbar in the Part Editor.  

Changing Pin Numbers Using Verb Mode Changing Pin Numbers Using Object Mode  

#### Changing Pin Numbers Using Verb Mode  

You can change pin numbers using verb mode. Start the command and then select one or more objects to which you want to apply the command.  

**Procedure** 

1. On the Decal Editing toolbar, click the Change Pin Number button.  

2. Type the new number in the information window.  

? Tip Alphanumeric pin numbers are valid.  

3. Click OK.  

4. Select the terminal requiring a new number.  

5. Right-click and click the Cancel popup menu item to exit verb mode.  

#### Changing Pin Numbers Using Object Mode  

You can change pin numbers using object mode. Select one or more objects and then select the command you want to use to perform an action on them.  

**Procedure** 

1. Select the decal terminal.  

2. On the Decal Editing toolbar, click the Change Pin Number button.  

3. Type the new number in the information window.  

0 Tip Alphanumeric pin numbers are valid.  

4. Click OK to update the selected terminal.  

### Changing a Pin Name  

Changes the name assigned to a single pin. Pin names are used to label the function of a pin, for example, CLK, DATA0, and so on. This command does not check for duplicate naming conventions.  

Precede the text with the back slash character (\) to add a bar over the text characters.  

![](/images/e543e96d3975e1caa6b3144a8b2548717685140ac1b188a01925061452a8701a.jpg)  

Tip   
To assign names to several pins in an ascending sequence, use the Set Pin Name button from the Editing Toolbar in the Part Editor.  

Changing Pin Names Using Verb Mode Changing Pin Names Using Object Mode  

#### Changing Pin Names Using Verb Mode  

You can change pin names using verb mode. Start the command and then select one or more objects to which you want to apply the command.  

**Procedure** 

1. On the Decal Editing toolbar, click the Change Pin Name button.   
2. Select the decal terminal requiring a new name.   
3. Type the new name in the information window.   
4. Click OK.   
5. Right-click and click the Cancel popup menu item to exit verb mode.  

#### Changing Pin Names Using Object Mode  

You can change pin names using object mode. Select one or more objects and then select the command you want to use to perform an action on them.  

**Procedure** 

1. Select the decal terminal.   
2. On the Decal Editing toolbar, click the Change Pin Name button.   
3. Type the new name in the information window.   
4. Click OK to update the selected terminal.  

### Changing a Pin Decal  

You can select a different pin decal for existing terminals in your schematic symbol. This is especially useful when defining connector pin usage or when redefining a symbol in the library.  

Changing Pin Decals Using Verb Mode Changing Pin Decals Using Object Mode  

#### Changing Pin Decals Using Verb Mode  

You can change pin decals using verb mode. Start the command and then select one or more objects to which you want to apply the command.  

**Procedure** 

1. On the Decal Editing toolbar, click the Change Pin Decal button. The Pin Decal Browse Dialog   
   Box appears.   
2. Select the new pin decal from the list to add to the gate.   
3. Click OK.   
4. Select the terminals requiring new decals to complete the change.   
5. Right-click and click the Cancel popup menu item to exit the verb mode.  

#### Changing Pin Decals Using Object Mode  

You can change pin decals using object mode. Select one or more objects and then select the command you want to use to perform an action on them.  

**Procedure** 

1. Select one or more decal terminals.   
2. Click the Change Pin Decal button.   
3. Select the in decal required from the list of pin decals.   
4. Click OK to update the selected terminals.  

### Changing Sequence Numbers  

Use Change Sequence Number from the Part Editor Decal Editing Toolbar to change the sequence for pins in the part. The pin sequence number is used to set a corresponding number for the pins in alternate CAE decals. When you assign pin numbers with Set Pin Number or change a pin number with Change Pin Number, the same number is assigned to any alternate decals.  

**Procedure** 

1. On the Decal Editing toolbar, click the Change Sequence Number button.   
2. Select the pin requiring a new sequence number.   
3. Type the new sequence number in the information window.   
4. Click OK.  

### Attribute Labels  

Attribute Labels are placeholders for attributes within a CAE Decal. When you add an attribute to a part, it is placed in this reserved location. SailWind Logic lets you create an unlimited number of attribute labels.  

**See also Attributes Overview.**  

Use attribute labels to customize attribute locations in the design. You can create and place attribute labels so that when a part is added to a design, assigned attributes are less likely to exist where a connection or other design information exists. You can also specify a unique justification or orientation for the label.  

!Tip  

When working with attribute labels, observe the following:  

• If you add an attribute and do not have an available attribute label, the attribute is added just below the insertion point of the part. Additional attributes are added below the last one.   
• Attribute labels do not display in the Schematic Editor or the Part Editor. You must be viewing a decal to view an attribute label. Use Display Colors to control the display of attribute labels when creating or edit a decal. See also Setting Display Colors.   
• You can create an attribute label with a specific name; one that matches the actual attribute's name. This makes placement of specific attribute information easier. You can also use a generic attribute label name, or free label, for any attribute assigned to the part. The name used is \*Free Label N, where N is the number of the labe   
• As you add attributes, they are placed at either the location that matches the attribute name, if specified, or the first available free label location. See also Creating Attribute Labels.  

### Creating Attribute Labels  

You can create attribute labels while editing or creating a CAE Decal.  

**Procedure** 

1. On the Decal Editing toolbar, click the Add Attribute Label button.  

2. Define the attribute label using one of the following methods:  

Type a name in the Attribute Name list box for the label that corresponds to an attribute. Select a name from the Attribute Name list box. When you select an attribute name, it is removed from the list box.  

Select \*Free Label to use a free label. When you Select Free Label, the number increments to the next available number.   
Select Browse Lib Attr to open the Browse Library Attributes dialog box, select an attribute name from the list and then click OK.  

3. (Optional) Set the text size, width, or justification.  

4. Click OK. See also Setting Display Colors.  

### Modifying Terminals  

Use the Terminal Properties dialog box to view or modify the properties of the terminals selected in the Decal Editor.  

**Procedure** 

1. In the Decal Editor, right-click a decal terminal and click the Properties popup menu item. This opens the Terminal Properties dialog box.   
2. To change the pin decal for all the terminals selected in the Decal Editor, click Change Pin Decal.   
3. In the Pin Decal Browse dialog box, select a pin decal, and then click OK.   
4. To change the terminal number, type the new value in the Number box. If you select multiple terminals in the Decal Editor, this option is unavailable.   
5. To change the terminal name, type the new name in the Name box. If you select multiple terminals in the Decal Editor, this option is unavailable.   
6. To change the swap class value, type a new value in the Swap class box. If the values of the terminals differ, this text box is blank.  

7. Click OK.  

### Setting the Origin for a Part  

From within the Part Editor, use the Setup $>$ Set Origin menu item to specify a new origin for a CAE Decal. When you add a part in SailWind Logic, the point of insertion is determined by the origin of the decal. You can perform this task while creating or modifying a decal.  

**Procedure** 

1. Open a CAE Decal in the Decal Editor and click the Setup $>$ Set Origin menu item.   
2. Indicate a new origin. An information window with the new X,Y coordinate appears.   
3. Click Yes to accept the new origin.  

**Related Topics**  

Creating a New CAE Decal  

### Getting Gate Decals From the Library  

Use the “Get Gate Decal from Library” dialog box to open an existing CAE Decal in the Part Editor.  

**Procedure** 

1. In the Part Editor, click the Open button.   
2. In the “Select Type of Editing Item” dialog box, click CAE Decal and then click OK.   
3. Type a wildcard or expression on page 105 in the Items box to filter the symbols, and click Apply.   
4. Select the part from the decals area.   
5. Click OK. The selected decal displays.  

### Assigning Pin Information to the CAE Decal  

You can view and modify pin information for a CAE decal in the Part Editor. You can also assign JEDEC pin numbering if your symbol requires you to use that standard.  

**Procedure** 

1. In the Part Editor, open a Part Type, and click the Edit Graphics button.   
2. In the Select Gate Decal dialog box, select a gate from the Gate list, or select a gate from the work area. The decal displays in the CAE Decal Editor.   
3. Click the Decal Editing Toolbar button to display the Decal Editing Toolbar, then click the Set Pin Number button.   
4. In the “Set pin number” dialog box, in the “Start pin number” area, type values in the Prefix and/or Suffix boxes. A preview of pin numbers based on your input is displayed below the boxes.  

!Tip  

When specifying the pin numbers, note the following:  

• Alphabetic and numeric values can be used in either box. For example, A1 or 1A.   
• For a single numeric, use either Prefix or Suffix box, and void the other box.  

5. In the Increment options area, choose what to increment by clicking either Increment prefix or Increment suffix.  

6. In the Step value box, type a positive or negative number to increase or decrease the pin numbers with consecutive or stepped values.  

7. If using alphanumerics, select the “Use JEDEC pin numbering” check box if you want to ensure legal alphanumeric values are used.  

8. Click OK.  

9. Select each pin or pin text in ascending sequence to assign a number.  

You can click twice on a pin to skip a number.  

Use Change Pin Number to change a pin number if necessary. Refer to the Terminal Toolbox topic for additional information.  

The software assigns the same pin numbers to any alternate CAE decals.  

10. Set other pin information such as pin type and pin swapping, as needed.  

11. Right-click and click the Cancel popup menu item to exit the process.  

12. Repeat the steps for the other gates.  

### Saving a Modified Decal With a Different Name  

If you modify a decal associated with a part type, use the Save Part and Gate Decals As dialog box to rename the decal. After modifying the decal, you can save it with a different name.  

**Procedure** 

1. Click the File $>$ Return to Part menu item, and then click Yes to the “Returning to Part level - Keep changes to Gate?” prompt.   
2. Click the File $>$ Save As menu item. The “Save Part and Gate Decals As” dialog box appears.   
3. Select the decal in the Name of Gate Decal multicolumn list box and click Edit.   
4. Type a new name for the Decal and click OK.   
5. Click Yes to the “Part Type item exists. Overwrite item?” prompt to replace the current library part with the one containing the modified decal.  

**Related Topics**  

Saving Part Types  

## Part Types  

You use the Part Editor to work with part information. This is a collection of the electrical and attribute information that represents the physical characteristics of a part as opposed to the graphical representation contained in the CAE decal.  

Modifying Electrical Information for a Part   
Viewing and Setting General Part Information   
Editing Logic Families   
Assigning PCB Decals   
Assigning Gates to Parts   
Assigning CAE Decals to Gates   
Part Information - Pins   
Managing Attributes   
Browsing Library Attributes   
Part Information - Pin Mapping   
Assigning Alternate Logic Decals for Connector Symbols   
Saving Part Types   
Library Management for Saved Part Types   
Saving a Modified Part Type With a Different Name   
Creating a New Connector   
Browsing for Connectors   
Creating a New Pin Decal   
Editing Objects in the Decal Editor  

### Modifying Electrical Information for a Part  

Use the Part Information dialog box to modify electrical information for a part. Electrical information includes the part statistics, the logic family, the PCB decal assignment, the CAE decal assignment, gate and signal pins, gate swapping information, and various other attributes.  

You must identify the electrical or part type information, before assigning a CAE Decal to the part.  

You access this information by clicking the Tools $>$ Part Editor menu item, and then, on the toolbar, click the Edit Electrical button.  

You can perform the following actions in the Part Information dialog box:  

• Viewing and Setting General Part Information - General tab   
• Assigning PCB Decals to library parts - PCB Decals tab   
• Assigning Gates to Parts - Gates tab Part Information - Pins tab Managing Attributes - Attributes tab  

Part Information - Pin Mapping tab • Assigning Alternate Logic Decals for Connector Symbols - Connector tab  

**Related Topics**  

Managing Libraries and Library Data  

### Viewing and Setting General Part Information  

Use the General tab in the Part Information dialog box to view part statistics and set family information.  

Viewing Part Statistics Setting the Logic Family Setting General Part Information  

#### Viewing Part Statistics  

Information about the part you are creating or editing is listed under part statistic categories.  

Table 19. Part Statistic Categories   

| Category         | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| Pin Count        | Displays the total number of pins in the part. Includes gate pins, signal pins, and unused pins. If multiple decals are assigned with different pin counts, a range of smallest to largest decal pin counts is shown. |
| Decal            | Displays the name of the decal, as chosen on the PCB Decals tab. |
| Gate Count       | Displays how many gates exist in the part.                   |
| Signal Pin Count | Displays the number of signal pins in the part.              |

#### Setting the Logic Family  

You can set the logic family to define a component type and assign an alphanumeric Reference Designator (RefDes) prefix for part recognition in your design.  

![](/images/e2cb616d1c7cb2de9dc46606603cfe258cb4a582095316d0c87c5980cb46156a.jpg)  

!Note:  

Beginning with PADS 9.0, die parts and flip chips are identified by the Special Purpose settings in the Part Type rather than by the DIE and FLP logic families. With this change, any reference designator (logic family) can be assigned to a die part or flip chip.  

**Procedure** 

1. In the Part Editor, click the Edit Electrical button and in the Part Information for Part dialog box, click the General tab.  

2. To identify the logic family, select a logic family from the list in the Logic Family area.  

When you select a logic family, the default reference designator prefix for this part appears next to Ref. Prefix.  

!Tip  

The default is UND, or undefined. If you leave the logic family undefined, the software prompts you for the reference designator prefix when you add a part. You can specify an alpha prefix or an alphanumeric prefix.  

3. Alternatively, if you want to add, delete, and edit logic families and default reference designator prefixes, click Families.  

The Logic Families dialog box opens.  

a. Make your changes and then click OK to return to the Part Information for Part dialog box.   
b. Select the new or updated logic family from the list.  

See also Editing Logic Families.  

#### Setting General Part Information  

You can set the general part information such as logical to physical pin mapping, special purpose part definitions and ECO registration for a part.  

**Procedure** 

1. In the Part Editor, click the Edit Electrical button and in the Part Information for Part dialog box, click the General tab. 2. Select the “Define mapping of Part Type pin numbers to PCB Decal” check box to activate the Pin Mapping tab where you can map logical pin numbers to different physical pin numbers.  

**Restriction:**  

Note the following restrictions:  

• The check box is unavailable after you add one or more alphanumeric decals to the part type. Remove the assigned alphanumeric decal to make the check box available. The check box also becomes available if you assign a numeric decal. However, you will still need to remove the alphanumeric decal from the list to make the part valid. • You must assign a decal to use the Pin Mapping tab. • Only decals with sequential numerical pin numbers can be used with pin mapping.  

3. Select the Special Purpose check box, then select the appropriate radio button to identify the part as one of the following types:  

• Connector — In contrast to other part types, connectors do not require a prefix list, or gate definitions.  

**Restriction:**  

When working with connectors, note the following restrictions:  

• This check box is automatically selected when you create or modify connectors. It is unavailable if you open a part other than a connector.   
• This check box is unavailable when the part already has gate or pin assignments.   
• The Gate Decals tab is unavailable when the Connector check box is selected.   
• Some Pins tab controls not applicable to connector parts are disabled.  

Die Part — See the following note.  

• Flip Chip — See the following note.  

![](/images/50976a96086fb5ae4e6c36066a8cc57e7c2647350239c2691c5bd7698bf20beb.jpg)  

!Note:  

Beginning with PADS 9.0, die parts and flip chips are identified by the Special Purpose settings in the Part Type rather than by the DIE and FLP logic families. With this change, any reference designator (logic family) can be assigned to a die part or flip chip.  

4. To enable a part to be passed between the design and schematic file for forward and backward annotation, click ECO Registered Part. By default, all existing part types in your design are ECO registered.  

![](/images/e6eb81415ad8b4c36fc161c11e4b6761534b27e6fff42cb0e5328c5e91f35929.jpg)  

!Tip  

Typically, you do not select this check box for non-electrical parts. For example, if you create and add a mounting hole to your design in the layout software, you would not need the part (mounting hole) to pass back to your schematic when you perform a backward annotation of the design.  

5. To apply the part information edits to other parts in the library, type prefixes and wildcards into the Prefix List box matching the names of the other parts to update.  

![](/images/3975e6019670137b1f57693e63c7cc454b4718e70b81ea32f6e090a145213618.jpg)  

!Note:  

Examples of prefix and wildcard usage:  

• Question mark ? in a prefix acts as a wildcard for one character. The prefix $"?4"$ is the equivalent of $"54"$ or “74”. • If you type $"\textdegree2"$ as the suffix, the edits are applied to all parts ending in 02.  

![](/images/335384dbaa5e6d1d7a64be90c717120d42b350b3b69f1998cb6177fb664c6157.jpg)  

**CAUTION**:  

The software applies the contents of the Prefix List box when you click OK or Save As from other tabs in the Part Information dialog box.  

6. Click the Check Part button to check the part for missing or inconsistent information while the Part Information dialog box is open.  

7. Click OK.  

### Editing Logic Families  

To add, delete, or modify logic family names and default reference designator prefixes, use the Logic Families dialog box.  

Adding a Logic Family   
Changing the Name or Prefix of a Logic Family   
Deleting a Logic Family  

#### Adding a Logic Family  

If you are creating a new part for your design that requires a logic family definition that does not exist in the predefined list, you can add a new logic family to the database for use in current and future designs.  

**Procedure** 

1. In the Part Editor, open a Part Type, and click the Edit Electrical button.   
2. In the Part Information dialog box, click the General tab and then click the Families button.   
3. In the Logic Families dialog box, click Add. A new entry opens in the Logic Families list.   
4. In the Family text box, type the new logic family name.   
5. Click in the Prefix text box, and type the prefix you want to use for the new family. You can specify an alphabetic prefix or an alphanumeric prefix. The maximum length for the prefi is six characters. The last character must be an alphabetic character.  

6. Click OK.  

#### Changing the Name or Prefix of a Logic Family  

If your design requirements require it, you can change the name or prefix of an existing logic family.  

**Procedure** 

1. In the Part Editor, open a Part Type, and click the Edit Electrical button.   
2. In the Part Information dialog box, click the General tab and then click the Families button.   
3. In the Logic Families dialog box, select the logic family from the list.   
4. In the Family text box, type the name of the new family.   
5. In the Prefix text box, type the new prefix to associate with the new family.   
6. Click OK.  

#### Deleting a Logic Family  

If your design requirements change, or you no longer need or support a particular logic family, you can delete a logic family.  

**Procedure** 

1. In the Part Editor, open a Part Type, and click the Edit Electrical button.   
2. In the Part Information dialog box, click the General tab and then click the Families button.   
3. In the Logic Families dialog box, select the logic family that you want to delete from the list.   
4. Click the Delete button.   
5. Click OK.  

**Related Topics**  

Modifying Electrical Information for a Part  

### Assigning PCB Decals  

To assign decals, or footprints, to library parts, use the PCB Decals tab in the Part Information dialog box.   
You must assign a decal before assigning gate information, signal pin names, or pin mapping to a part.   
The decal also specifies the number of pins in the part.  

Assigning an Existing Decal Assigning a New Decal Unassigning a Decal Changing the Default Decal Resetting the Tab Data  

#### Assigning an Existing Decal  

There are situations where you might want to define more than one PCB decal to a part. This enables one symbol to represent different versions of a part that exist in different physical packages. You can assign up to sixteen PCB decals to a part.  

**Procedure** 

1. Open a Part Type.   
2. On the toolbar in the Part Editor, click the Edit Electrical button and then, in the Part Information dialog box, click the PCB Decals tab.   
3. In the Library dropdown list, select the library from which you want to assign decals. The available decals from the selected library appear in the Unassigned Decals list box.  

4. To filter the contents of the Unassigned Decals list use any of the following:  

a. Type Wildcards and Expressions into the Filter box.  

Tip Type asterisk \* in the Filter box to display all decals.  

b. Type a number in the Pin Count box, and then click Apply.  

0 Tip Delete all numbers in the Pin Count box to display all decals. This box is always available as a filter to enable decals of differing pin counts to be assigned.  

c. Click the “Show only Decals with pin numbers matching Part Type” check box to filter out decals that do not have pin numbers matching existing gate and signal pins on the Pins tab, or the physical pin numbers on the Pin Mapping tab.  

5. Select a decal name from the Unassigned Decals list box.  

6. Click Assign. The selected decal is assigned to the part and moved to the Assigned Decals list box.  

![](/images/9a8e700d1f91afbf0693a5e90618a025d6a6053268c0a7d872399d22e67dd3ae.jpg)  

!Tip  

As a shortcut, double-click on a decal name to assign it to the part.  

**Restriction:**  

Note the following restrictions:  

• You must assign a decal with enough pins for all the defined gate pins and signal pins on the Pins tab. • Only decals with sequential numerical pin numbers can be used with pin mapping.  

7. To assign additional decals to the part, repeat Steps 4 and 5 above.  

8. You can check the part for missing or inconsistent information while the Part Information dialog box is open. Click the Check Part button.  

The software checks the assigned decals when you exit the tab (regardless of whether you click the Check Part button) to ensure they contain physical pin numbers for all the gate and signal pins defined in the Pins tab.  

#### Assigning a New Decal  

You can specify a decal that does not exist in the library yet, but may exist in another PCB designer’s library, or may be created later.  

**Procedure** 

1. Open a Part Type.   
2. In the Part Editor, on the toolbar, click the Edit Electrical button and then in the Part Information dialog box, click the PCB Decals tab.   
3. Click Assign New.   
4. In the New PCB Decal dialog box, type a name and click OK. The name is added to the end of the Assigned Decals list.  

#### Unassigning a Decal  

As your design needs change, you may need to remove a current decal assignment so that you can reassign a different decal to a part.  

**Procedure** 

1. Open a Part Type.   
2. In the Part Editor, on the toolbar, click the Edit Electrical button and then in the Part Information   
   dialog box, click the PCB Decals tab.   
3. Select a decal name from the Assigned Decals list box.   
4. Click Unassign.  

The decal is unassigned from the part, and moved to the Unassigned Decals list box.  

Tip As a shortcut, double-click on a decal name to remove it from the Assigned Decals list.  

#### Changing the Default Decal  

The first decal listed in the Assigned Decals list box is the default decal used when you add the part to Layout. You can make any decal in the Assigned Decals list the default decal by moving it to the top of the list.  

**Procedure** 

1. Open a Part Type.   
2. In the Part Editor, on the toolbar, click the Edit Electrical button and then in the Part Information dialog box, click the PCB Decals tab.   
3. In the Assigned Decals list, select the decal that you want to make the default.   
4. Click Up until the decal is at the top of the list. The decal becomes the default decal.  

#### Resetting the Tab Data  

You may sometimes want to discard changes you have made in the current session with the PCB Decals tab, and return the tab’s data to its original state.  

**Procedure** 

1. Open a Part Type.   
2. In the Part Editor, on the toolbar, click the Edit Electrical button and then in the Part Information dialog box, click the PCB Decals tab.   
3. Click Reset. 一 Tip Clicking Reset affects the current tab only.  

**Related Topics**  

Modifying Electrical Information for a Part  

### Assigning Gates to Parts  

Use the Gates tab to assign gate information to a part, including the number of gates, gate swap information, and CAE Decals for the part.  

Note: A space and a period (.) are illegal characters for pin names.  

Gate Decal and Alternates Gate and Pin Swap Information Assigning Gates to a Part  

#### Gate Decal and Alternates  

For each gate, you can enter the CAE Decal name which is the name of the logic symbol that is used to display the part in the schematic. Alternate decal assignments must have the same number of pins. One primary and three alternate decals may be defined for each gate. Assigning a CAE Decal is optional in SailWind Layout, but required in SailWind Logic.  

#### Gate and Pin Swap Information  

If at least one decal is assigned to a part, you can enter or modify its gate information. This includes enabling or disabling swaps for gates within a part or between similar parts. This information lets SailWind Logic know which gates it can substitute for connection length minimization after placement.  

To gate swap, assign a number to the gate on the Gates tab. Gates with like numbers can swap within the part, or to other similar parts. A value of one (1) indicates that the gate is swappable with gates of the same part type in the schematic database. If a part contains more than one type of swappable gate, then identify the second type with the number 2, the third type with 3, etc. The number 0 indicates that no swapping can occur.  

#### Assigning Gates to a Part  

You can assign gates to a part.  

**Procedure** 

1. Open a Part Type, on the toolbar, click the Edit Electrical button, and then click the Gates tab.   
2. To add a gate to the part, click Add. The gate appears in the Gate list. The first gate is automatically designated A, the second gate B, and so forth. When you select a gate, the Pins list shows the number of pins for the selected gate.   
3. To swap gates with the same Swap ID number, select the gate click Edit, and then type a value between 1 and 100 in the Swap column. To disable swap for the gate, type a value of 0.  

4. To define Logic decals for the gate, select the cell under CAE Decal 1 click Edit, and then type a decal name in the CAE Decal box or click the Browse button to search for a decal from a library.  

The Browse button opens the Assign Decal to Gate dialog box.  

!Tip  

You can define up to 4 alternates; you do not have to define alternates.  

See also Assigning CAE Decals to Gates.  

5. To remove the selected gate from the Gates list, click Delete.  

The gates following the removed gate are automatically renamed in sequential order.  

![](/images/65ce2c044a17d74d4acbfccddd05bda401b3825f4ba34fd03099db98affaf67a.jpg)  

!Tip  

If you delete a gate, the pins information in the Pins tab is reset. You can add a gate and move the pins from one gate to the other on the Pins tab to retain pin information before you delete the gate.  

6. To return the options on the tab to the original settings when the tab first appeared, click Reset. This resets only the current tab.  

Gate pins are added on the Pins tab.  

See also Part Information - Pins.  

### Assigning CAE Decals to Gates  

The Assign Decal to Gate dialog box is used to assign a decal to each of the gates in a part. Some parts may have multiple gates of different types, so you can assign individual specific decals to each of the gates.  

**Procedure** 

1. Open a Part Type, on the toolbar, click the Edit Electrical button, and then click the Gates tab.   
2. Select the cell under CAE Decal 1 and click the Edit button or double-click the cell under CAE Decal 1.   
3. Type a decal name in the CAE Decal box or click the “...” Browse button to search for a decal from a library. The Browse button opens the Assign Decal to Gate dialog box.   
4. Select the library from which you want to assign decals. The available decals from the selected library appear in the Unassigned Decals list box. The list changes according to the library you select.   
5. To limit the items that appear in the Unassigned Decals list box, type a wildcard or expression on page 105 in the Filter box and click Apply.   
6. Select the decals you want to assign to the gate from the Unassigned Decals list and click Assign.  

![](/images/f6689cc63f13b60e49b0fc364eb3849fe09ce9d2e5a97658d28bf71da99348c0.jpg)  

!Tip  

When assigning decals, observe the following:  

• The decal you select in the Unassigned Decals list box is displayed in the preview box.   
• You can assign up to four decals. Assigned decals must have the same number of pins. The first decal is the default decal, the decal used when you add a part to the schematic.  

7. To change the order, select the decal in the Assigned Decals list and click Up or Down.  

8. To remove a decal from the gate, select it from the Assigned Decals list and click Unassign.  

9. To assign a decal name of a nonexistent decal in the library, click Assign New. The Assign New Gate Decal dialog box appears.  

!Tip  

You can specify a decal that does not exist in your library, but may exist in another designer’s library, or that you may create later.  

10. Click OK to apply your changes.  

### Part Information - Pins  

Use the Pins tab in the Part Information dialog box to assign gate pins, signal pins, and unused pins to the part. Pin numbers added to the Pins tab, must match those of the PCB Decal. Use the Pin Mapping tab to overlay logical (schematic) alphanumeric pin numbers onto the physical numeric PCB decal.  

![](/images/7091c9f3e5710c1bf7e390b2dca2a95a0a647fbbaff399741a09cee542e6398e.jpg)  

Tip To undo all changes for this tab only, click Reset.  

Adding One or More Pins to a Part   
Editing Pin Data   
Assigning a Signal Pin   
Assigning an Unused Pin   
Sorting Table Data   
Renumbering Pins   
Deleting Pins   
Error Checking   
Signal Pin Nets  

#### Adding One or More Pins to a Part  

You can add pins to a part using several methods. You can add all pins automatically by assigning a decal. You can add a single pin to the part, add a series of pins, and paste pins from a database; or you can import pins using a comma separate value (CSV) file.  

Adding a Single Pin   
Adding a Series of Pins   
Assigning a Decal   
Pasting Pin Information   
Importing Pins Using a CSV File  

##### Adding a Single Pin  

You can use the Pins tab on the Part Information dialog box to add a single pin to a part.  

**Procedure** 

1. Open a Part Type, then, on the toolbar, click the Edit Electrical button.  

2. On the Pins tab of the Part Information dialog box, click the Add Pin button.  

Note:   
You must add a pin number to make the pin valid, and then change any other fields as needed.  

If this is the first pin to be added, it takes the default of belonging to Gate-A. If pins already exist, the new pin takes the Pin Group of the currently selected pin.  

##### Adding a Series of Pins  

You can use the Pins tab on the Part Information dialog box to add a series of pins to a part.  

**Procedure** 

1. Open a Part Type, on the toolbar, click the Edit Electrical button, and then click the Pins tab in the Part Information dialog box.   
2. On the Pins tab of the Part Information dialog box, click the Add Pins button.   
3. In the Add Pins dialog box, type the number of pins to add in the Number of pins box.   
   0 Tip Total pins for the part can not exceed 32,767.  

4. In the Start pin number area, type values in the Prefix and/or Suffix boxes. A preview of pin numbers based on your input is displayed below the boxes.  

![](/images/f8dc31d425e3f59b6e0f76ff7e1ed803d3ecc87d6c040519731668af9082cce1.jpg)  

!Tip  

When entering pin numbers, observe the following:  

• Alphabetic and numeric values can be used in either box. For example, A1 or 1A. If you type alphanumerics and the decal uses numerics, you must use the Pin Mapping tab to map the alphanumerics onto the decal. • For a single numeric, use either the Prefix or Suffix box, and void the other box.  

5. In the Increment options area, choose what to increment by clicking either Increment prefix or Increment suffix.  

6. In the Step value box, type a positive or negative number by which to increase or decrease the pin numbers with consecutive or stepped values.  

7. If using alphanumerics, you can select the “Use JEDEC pin numbering” check box to ensure that legal alphanumeric values are used.  

8. Click OK.  

The new pins display in the list on the Pins tab of the Part Information dialog box.  

##### Assigning a Decal  

When you assign a decal on the PCB Decals tab, the pin numbers from the decal are automatically populated into the Pins tab table. PCB Decal pin numbers can be alphanumeric or numeric and the pin numbers in the PCB Decal must match the pin numbers listed in the Pins tab table.  

##### Pasting Pin Information  

You can copy selected table data from the Pins tab or from Microsoft Excel and paste it into the Pins table. The selected cell in the table is the paste origin. Data is pasted below and to the right of the paste origin.  

**Procedure** 

1. Open a Part Type, on the toolbar, click the Edit Electrical button, and then click the Pins tab in the Part Information dialog box.   
2. If you are copying from Excel, select data and use the Excel Copy command. If you are copying from the Pins tab, select data and click the Copy button on the Pins tab.   
3. Click the Paste button to paste the data into the table starting at the paste origin.  

**Restriction:**  

When the pasted data includes either Pin Group or Pin Number data, the software adds extra pin rows automatically, otherwise the paste will fail if the number of rows and columns in the pasted data does not match those available in the table below and to the right of the paste origin.  

##### Importing Pins Using a CSV File  

You can import data from a comma separated value file into a pins table.  

**Procedure** 

1. Open a Part Type, on the toolbar, click the Edit Electrical button, and then click the Pins tab in the Part Information dialog box.  

2. Click the Import CSV button.  

3. In the File Open dialog box, browse and select the CSV file.  

4. Click Open to begin the import.  

The entire contents of the Pins tab table is replaced with the data of the CSV file.  

!Note:  

CSV field names must correspond to the column headers in the Pins tab table. Only the first two characters of the header must match. For example, “Pi” for the Pin Group column. Gate or “Ga” are acceptable alternatives to the Pin Group header.  

![](/images/c8c9b726f8645132c6f71ec580a4ea852c775fad5652a777a0bf04e210a51d10.jpg)  

Tip A sample CSV file is located in your \SailWind projects\Samples folder.  

#### Editing Pin Data  

You can click a cell in the row of the pin you are editing to edit the cell contents, or select one or more cells of the same column and click the Edit button.  

**Procedure** 

1. Open a Part Type, on the toolbar, click the Edit Electrical button, and then click the Pins tab in the Part Information dialog box.   
2. Click the Pin Group cell and choose gate, signal pin, or unused pin from the list. Gates listed in the Pin Group cell list are added using the Gates tab. Signal pins require a signal name in the Name cell. See Assigning a Signal Pin, Assigning an Unused Pin.   
3. Click the Number cell and type a pin number for the pin. The Number cell must contain at least 1 character and can contain up to 15 characters.  

Note: The pin number must match the PCB decal. For example, alphanumeric to alphanumeric.  

![](/images/2a1aafcedf219c67192ebf587392a006169a1d78126845c520071faf9a498979.jpg)  

!Tip  

Pin numbers can be either numeric or alphanumeric. Prior to PADS2007, alphanumeric pin numbers were not legal on the PCB decal but overlaid the numeric decal numbers, and were stored within the Part Type. You can continue to keep numeric PCB decals and use the Pin Mapping tab to overlay different pin numbers onto the numeric PCB decal pin numbers. See Part Information - Pin Mapping.  

4. Click the Name cell and type a pin signal or function name. For example, “Clock” or “CLK.” A pin name is not required. The Name column is not used for unused pins.  

![](/images/8c29ad8688f7028708ca5a2a8ee338d323cf6924983298fa88e263d5c7cbc5fe.jpg)  

**Restriction:**  

Gate pin names can contain up to 40 characters, while signal pin names can contain up to 47. All alphanumeric characters are accepted. In signal pin names, you cannot use special characters such as question marks ?, curly braces $\{\}$ , asterisks \*, periods ., commas , , or spaces. But in gate pin names, you can use any character except a space.  

5. Click the Type cell and choose a pin type from the list.  

The type column is only used with gate pins.  

6. Click the Swap cell and type a swap number, or use the up/down arrows.  

!Tip  

You swap pins within gates to uncross connections and facilitate routing. Pins with like numbers can swap within a gate. Type 0 to disable swapping.  

7. Click the Sequence (Seq.) cell and type the gate sequence number. The sequence number determines the mapping of CAE gate pins to PCB decal pins. The sequence is automatically shared with alternate CAE decals. For example, the sequence number shows how pin numbers appear on the CAE gate decal; therefore, in Gate A, sequence number 1 could be pin 1, but in Gate B, sequence number 1 would be pin 4.  

![](/images/dd3be48dff1702fb1dd34aba27b85cf1338511ab6e9f84b7e04c0430d84cabf1.jpg)  

!Note:  

Exception: When editing pin data for connectors, only the Pin Group and Number columns are relevant. Data entered in other columns is rejected. Connectors do not have gates, so the Pin Group column just indicates whether a pin is a connector pin or an unused pin.  

#### Assigning a Signal Pin  

Assign signal names to implicit pins—pins which are not displayed on any gate in the schematic. Typically, ground and power pins are the only implicit pins. You are not required to use Signal Pins. Instead, you can add power and ground pins to a gate or create a separate gate for power and/or ground pins. For the parts in the libraries shipped with SailWind Logic, the standard ground signal name is GND. The standard power signal name is $+5V.$  

#### Assigning an Unused Pin  

You can assign a pin to be an unused pin. An unused pin is a pin that is defined in a PCB decal but has no electrical function in the part type. The unused pin information is not saved in the part type, but is derived automatically based on the number of assigned gate and signal pins to the number of pins in the assigned PCB decal.  

#### Sorting Table Data  

You can sort the columns in a pins table in ascending order.  

**Procedure** 

1. Open a Part Type, on the toolbar, click the Edit Electrical button, and then click the Pins tab in the Part Information dialog box.   
2. Double-click a column header to sort the column.  

#### Renumbering Pins  

You can renumber pins in a pins table on the Pins tab of the Part Information dialog box. If required, you can use JEDEC pin numbering.  

**Procedure** 

1. Open a Part Type, on the toolbar, click the Edit Electrical button, and then click the Pins tab in the Part Information dialog box.   
2. Select one or more cells in the Number column.   
3. Click the Renumber button. In the Renumber Pins dialog box, the Number of pins box displays the number of pins selected for renumbering.   
4. In the Start pin number area, type values in the Prefix and/or Suffix boxes. A preview of pin numbers based on your input is displayed below the boxes.  

!Tip  

When entering pin numbers, observe the following:  

• Alphabetic and numeric values can be used in either box. For example, A1 or 1A.   
• For a single numeric, use either the Prefix or Suffix box, and void the other box.   

5. In the Increment options area, choose what to increment by clicking either Increment prefix or Increment suffix.   
6. In the Step value box, type a positive or negative number by which to increase or decrease the pin numbers with consecutive or stepped values.   
7. If using alphanumerics, you can select the “Use JEDEC pin numbering” check box to ensure that legal alphanumeric values are used.  

8. Click OK to apply your changes.  

The renumbered pins display on the Pins tab of the Part Information dialog box.  

#### Deleting Pins  

If you need to modify the part, you can delete pins in the Pin table on the Pins tab.  

**Procedure** 

1. Open a Part Type, on the toolbar, click the Edit Electrical button, and then click the Pins tab in the Part Information dialog box.   
2. Select one or more cells in the Pin column you want to delete and then click the Delete Pins button.  

#### Error Checking  

When you click Check Part, OK, or Save As, or when you click a different tab, validation occurs and checks are run for error conditions.  

The following conditions are checked:  

• Empty pin numbers, pin numbers with embedded spaces, duplicated Pin numbers or special characters such as question marks ?, curly braces $\{\}$ , asterisks \*, periods ., commas , , or spaces. • Empty, duplicated, or non-sequential sequence numbers within a single gate. • Non-empty Type cells for signal pins or unused pins, or empty Type cells for gate pins. • Pin names with illegal characters for gate pins, net names with illegal characters for signal pins, empty name for signal pins. Blank pin names are permitted for gate pins. • Empty pin swap for gate pins, non-empty pin swap for signal and unused pins. Pin swap values for gate pins outside of the range 0 to 100.  

#### Signal Pin Nets  

If signal pin nets are invisible, they do not belong to any particular sheet; therefore, they cannot be individually selected using the mouse.  

See also Signal Pin Nets Dialog Box.  

### Managing Attributes  

Use the Attributes tab in the Part Information dialog box to add an attribute to a part. A large number of predefined attribute types are available for selection.  

See also “Attributes Overview” on page 222.  

Adding an Attribute   
Modifying an Attribute   
Pasting Attribute Information   
Deleting an Attribute   
Setting Default Attributes   
Adding an Attribute From the Attribute Library   
Resetting the Attribute List  

#### Adding an Attribute  

You can add attribute names and values to a part using the Part Editor.  

**Procedure** 

1. In the Part Editor, open a Part Type, and click the Edit Electrical button.   
2. In the Part Information dialog box, click the Attributes tab.   
3. Click Add.   
4. Type an attribute name in the Attribute column.   
5. Type an attribute value in the Value column.   
6. Click OK to assign the new attribute.  

#### Modifying an Attribute  

You can modify attribute names and values for a part using the Part Editor.  

**Procedure** 

1. In the Part Editor, open a Part Type, and click the Edit Electrical button.   
2. In the Part Information dialog box, click the Attributes tab.   
3. Double-click an attribute from the Attribute multi-column list box, or select the attribute and click Edit.  

4. Type a new attribute name or value in the appropriate text box.  

![](/images/bf98be76b3784514266c6abbcc42d9aeca181fc11ec394eb97158e246465c031.jpg)  

!Tip  

Modifying attributes in the Attributes tab modifies the attribute only in the part being edited. Use the Manage Schematic Attributes Dialog Box and the Library Manager Dialog Box to manage attributes design-wide or in all libraries.  

#### Pasting Attribute Information  

You can copy selected table data from the Attribute tab or from Microsoft Excel and paste it into the Attributes table. The selected cell in the table is the paste origin. Data is pasted below and to the right of the paste origin.  

**Procedure** 

1. In Excel, select data and use the Copy command in Excel, or on the Attributes tab, select data and click the Attributes tab Copy button.   
2. Click the Paste button to paste the data into the table starting at the paste origin.   
3. Click OK.  

#### Deleting an Attribute  

You can delete attribute names and values for a part using the Part Editor.  

**Procedure** 

1. In the Part Editor, open a Part Type, and click the Edit Electrical button.   
2. In the Part Information dialog box, click the Attributes tab.   
3. Select an attribute.   
4. Click Delete.   
5. Click OK.  

#### Setting Default Attributes  

You can save a set of attributes as default attributes to be added automatically each time a new part is created.  

**Procedure** 

1. In the Part Editor, open a Part Type, and click the Edit Electrical button.   
2. In the Part Information dialog box, click the Attributes tab.   
3. Add all desired default attributes to the list of attributes for a part.   
4. Click Save As Default.  

Restriction:   
Values are not saved along with the default attributes.   
Tip   
When the default attribute list is created, it is saved in a defaultattribute.txt file that is shared between SailWind Logic and SailWind Layout.  

5. Click OK.  

#### Adding an Attribute From the Attribute Library  

You can search through all of the other attribute lists in the library for attributes to add to your current list.  

**Procedure** 

1. In the Part Editor, open a Part Type, and click the Edit Electrical button.   
2. In the Part Information dialog box, click the Attributes tab.   
3. Click Browse Lib. Attr to search for an attribute. See also Browsing Library Attributes.   
4. In the Browse Library Attributes dialog box, select an attribute group from the Group dropdown list to limit the display of attributes to only those of a particular group.   
5. Locate the attribute you want to add from the list and double-click it or select it and click OK to add it to the Attributes tab in the Part Information dialog box.   
6. Click OK to close the Part Information dialog box.  

#### Resetting the Attribute List  

If you make changes to the attribute list and then later decide you do not want to keep them, you can reset the Attribute list for the current session back to the state it was in before the tab was accessed.  

**Procedure** 

1. In the Part Editor, open a Part Type, and click the Edit Electrical button.   
2. In the Part Information dialog box, click the Attributes tab.   
3. Click the Reset button to undo all changes made in the current editing session (returns the attribute list to before the tab was accessed).  

Restriction: Only the current tab is reset.  

### Browsing Library Attributes  

You can browse and list all of the attribute names from libraries specified in the Library List dialog box.  

**Procedure** 

1. Click the Browse Lib. Attr button to open the Browse Library Attributes dialog box.  

2. In the Filter list, select a category of attributes to match your search.  

Note: Click Refresh to update the Attributes in library list.  

3. Select an attribute from the list.  

4. Click OK.  

![](/images/3436bb6bcf6e5998ac3f83d40bef174d57b44b1b759615221a1fe88ecde12ffc.jpg)  

Tip The Attributes in library list includes part type and decal attributes.  

### Part Information - Pin Mapping  

Use the Pin Mapping tab in the Part Information dialog box to overlay alphanumeric pin numbers onto numeric PCB decal pins. Prior to PADS 2007, alphanumeric pin numbers could not be saved in PCB decals.  

**Requirements:**  

• On the General tab, select the “Define mapping of Part Type pin numbers to PCB Decal” check box to make the Pin Mapping tab available. On the PCB Decals tab, assign a decal with sequential numerical pin numbers to use the Pin Mapping tab. The decal determines the number of pins in the part.  

!Tip  

To undo all changes for this tab only, click Reset.  

Mapping Alphanumeric Pin Numbers to Numeric Decals   
Unmapping Pins   
Checking the part  

#### Mapping Alphanumeric Pin Numbers to Numeric Decals  

You can use the Pin Mapping tab to map alphanumeric pin numbers to numeric decals.  

**Prerequisites**  

• On the General tab of the Part Information dialog box, select the “Define mapping of Part Type pin numbers to PCB Decal” check box to make the Pin Mapping tab available. On the PCB Decals tab, assign a decal with sequential numerical pin numbers to use the Pin Mapping tab. The decal determines the number of pins in the part.  

**Procedure** 

1. Click the Pin Mapping tab of the Part Information dialog box. In the decal list above the preview window, select the assigned decal to which you want to map alphanumeric pins.  

2. Map the pins using one of the following methods:  

• In the Unmapped Pins list, select one or more alphanumerics. Select one or the starting row in the Part Type column if you have a consecutive list to map. Click Map.   
• Select a cell in the Part Type column and click the Edit button, or simply double-click the cell. Select an alphanumeric in the Unmapped Pins list and double click the pin in the decal preview window to map the alphanumeric to the pin. The next row in the Unmapped Pins list becomes the next selected alphanumeric for mapping.  

Click Copy Map to copy both columns of the mapping table. Paste the mapping table into Excel. Make mass edits. Copy the data from Excel and click Paste Map on the Pin Mapping tab.  

Restriction:   
Copy Map and Paste Map only work with the whole pin mapping table and not selective rows.  

3. Repeat as necessary.  

4. Click OK.  

#### Unmapping Pins  

You can use the Pin Mapping tab to unmap pins from a decal.  

**Prerequisites**  

• On the General tab of the Part Information dialog box, select the “Define mapping of Part Type pin numbers to PCB Decal” check box to make the Pin Mapping tab available. On the PCB Decals tab, assign a decal with sequential numerical pin numbers to use the Pin Mapping tab. The decal determines the number of pins in the part.  

**Procedure** 

1. On the Pin Mapping tab of the Part Information dialog box, select a Decal pin number.   
2. Click Unmap.  

#### Checking the part  

After you have finished entering or editing part information, you can check to ensure the information entered in the Part Information dialog box is correct.  

**Procedure** 

Click the Check Part button to check for missing or inconsistent information entered in the Part Information dialog box.  

### Assigning Alternate Logic Decals for Connector Symbols  

Use the Connector tab to define the alternate Logic decals to display in a schematic. Decals are referred to as Special Symbols. You can associate a logical Pin Type with each alternate so that you can have a graphical indication of the connector pin function in the schematic.  

**Restriction:**  

The Connector tab is available only when you open an existing connector or create a new connector.  

!Tip  

Many users like to use a different symbol, or decal, to distinguish between input (Source) and output (Load) pins. You may define multiple symbols for each of the ten different pin types.  

You can define Special Symbols, or connector decals, for different pin types in the part.  

**Procedure** 

1. Open a Part Type, click the Edit Electrical button on the toolbar and then click the Connector tab.   
2. Click Add.   
3. Type a Special Symbol or select one from a library by clicking the Browse button.   
   The Browse button opens the Browse for Special Symbols Dialog Box.   
4. Double-click the new Pin Type entry, or select the new entry and click Edit.   
5. Select a Pin Type from the Pin Type dropdown list.   
6. If you want to remove the special symbol from the list, click Delete.   
7. To return the options on the tab to the original settings when the tab first appeared, click Reset.  

0 Tip Reset only resets the current tab.  

### Saving Part Types  

After you finish defining or editing your Part Types, you can save them to the library for further use in the current and future design sessions.  

Use the Save Part and Gate Decals As Dialog Box to save part types to the library. You can also rename the associated decal during the save process. If you change the pin count or other information in the decal, this prevents other parts that use the same decal from being affected.  

![](/images/2cd0f39c49622fc6ec4f334a34035cac1854373abf5c4ff298611c5f5e53f942.jpg)  

Tip   
The Change Type option of the Part Properties dialog box will not update the schematic copy of the part with the modified version in the library if you decrease the number of pins in the associated decal.  

**Procedure** 

1. Click the File $>$ Save As menu item.  

2. In the “Save Part and Gate Decals As” dialog box, type a name in the Name of Part text box.  

3. Select a library location from the Library dropdown list box.  

To change the name of the associated decal, select the decal from the CAE Decal column of the Names of Decals multicolumn list box and click Edit.  

Type a new name for the decal.  

4. ClickOK.  

5. If the part type already exists, the message “Part Type item exists. Overwrite item Y/N?” appears. Click Yes to overwrite the part or No to cancel the save.  

6. If you modified the part using Edit Part/Hierarchical Symbol to enter the Part Editor, the message “Update all parts of Part Type” appears. Click Yes to update parts on the schematic with the revised library version or No to leave the schematic version of the part unchanged.  

### Library Management for Saved Part Types  

Knowing where parts are located can help you to better manage your library content. Part Type and decals are saved in specific locations so that they can be logically arranged and found when needed.  

The library folder used for part types and associated decals is described below:  

• Part type data is saved under the name and library chosen in the Save Part and Gate Decals As dialog box.   
• Decals created when editing the part type are saved in the same library as the part type.   
Decals that are modified but not renamed are saved to the library from which they were opened.   
Renamed decals, whether modified or not, if unique across all libraries, are saved in the same library as the part type.   
• Renamed decals that are not unique across all libraries display the overwrite warning prompt. If you click Yes to overwrite an existing decal with the renamed decal, it replaces the library copy in its current library. If you answer No to the overwrite prompt, you can select a different decal name and folder.  

**Related Topics**  

Save Part and Gate Decals As Dialog Box  

Saving a Modified Decal With a Different Name  

Saving a Modified Part Type With a Different Name  

### Saving a Modified Part Type With a Different Name  

If you modify a part type and want to keep the existing library copy, use the Save Part and Gate Decals As dialog box to rename the part. After modifying the electrical information you can save the modified part.  

**Procedure** 

1. Click the File $>$ Save As menu item. The Save Part and Gate Decals As dialog box appears.   
2. Type a new name for the part type in the Name of Part text box.   
3. (Optional) Use the Library dropdown list box to specify a new library location. See also Library Management for Saved Part Types, Saving a Modified Decal With a Different Name.   
4. Click OK.  

Related Topics Saving Part Types  

### Creating a New Connector  

Connectors differ from other parts in that a connector is typically shown as a number of individual pins, rather than a single complete part. When a connector is used on a schematic, the pin number rather than the reference designation is incremented, for example, P1-1, P1-2, P1-3, not P1, P2, P3.  

Also, you can assign several CAE Decals to a connector for left and right side locations on the schematic and for alternate decals. The connectors supplied with SailWind Logic use the prefix CON in their name. You can open an existing connector to see how they are constructed.  

**Procedure** 

1. In the Part Editor, click the New button.   
2. In the Select type of editing item dialog box, select “Connector” and then click OK.   
3. Click the Edit Electrical button. The Part Information for Part -- New Connector dialog box on page 134 displays.   
4. On the Pins tab, add pins. For more information, see Part Information - Pins.   
5. Select the Connector tab.   
6. Add the schematic symbols for the connector in the Special Symbols area. See also Connector Tab on page 159.   
7. Select the PCB Decals tab to assign PCB decals for the connector. See also PCB Decals Tab on page 141.  

8. Select the Attributes tab to assign attribute information. See the Managing Attributes topic for more information. 9. Click OK to close the Part Information dialog box. The connector symbols display in the Part Editor. 10. Click the File $>$ Save As menu item. 11. Enter a name and library folder location. 12. Click OK. 13. Click the File $>$ Exit Part Editor menu item.  

### Browsing for Connectors  

Use the Browse for Connector dialog box to access the library and open an existing connector.  

**Procedure** 

1. Type a wildcard or expression on page 105 in the Items box to filter the connectors, and click Apply.   
2. Select a connector from the list.   
3. Click OK. The connector decal(s) display in the Part Editor.  

**Related Topics**  

Creating a New Connector  

### Creating a New Pin Decal  

Pin Decals are used to represent the terminal pins on a part. You can make a copy of an existing pin decal and modify it or you can create a new pin decal.  

Create a New Pin From an Existing Pin Decal Create a New Pin Decal  

#### Create a New Pin From an Existing Pin Decal  

To save design time and promote reuse, you can create a new pin from an existing pin decal.  

**Procedure** 

1. In the Part Editor, click the Open button.   
2. In the Select Type of Editing Item Dialog Box, select “Pin Decal” and then click OK The Pin Decal Browse dialog box displays.   
3. Select an existing pin decal from the Pins area. The highlighted decal is displayed in the Picture area.   
4. Click OK.   
5. Modify the graphics for the decal and position the text strings as required.   
6. Click the File $>$ Save As menu item. The Save Item to Library dialog box displays.   
7. Enter a name and library location for the new pin decal.   
8. Click OK.  

#### Create a New Pin Decal  

When you create a new Pin Decal, SailWind Logic automatically creates the necessary text strings for the associated pin information. You only need to specify the 2D lines that represent the terminal pin, then reposition the text strings.  

**Procedure** 

1. In the Part Editor, click the New button.   
2. In the Select Type of Editing Item Dialog Box, select Pin Decal.   
3. Click OK. Four text entries are displayed in the working area:   
   • #E is a placeholder for the pin number.   
   • PNAME is a placeholder for the pin name. NETNAME is a placeholder for the net name.   
   • #0:TYP $\cdot=\cup$ SWP $\scriptstyle=0$ are placeholders for the sequence number, pin type and swap class.  

4. Use the Create 2D Line button in the Decal Editing toolbar to create the pin decal.  

5. Reposition the text strings, if necessary.  

6. Click the File $>$ Save menu item.  

The Save Item to Library dialog box appears.  

7. Enter a name and library location for the new pin decal.  

8. Click OK.  

Tip To control which decals are displayed in the Pin Decal List, use the Pin List Manager  

### Editing Objects in the Decal Editor  

The Decal Editor offers a flexible environment for editing your decals. You can create new parts, edit existing parts and also create derivative parts from existing parts.  

To edit objects in the Decal Editor, refer to the following topics:  

• Object Selection Control in the Decal Editor Selecting Multiple Objects in the Decal Editor Changing Objects in the Decal Editor Modifying Terminals  

