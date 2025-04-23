# Chapter 15 Schematic Object Modification  

Changes and edits to your design objects are fully-supported in SailWind Logic. This includes the modification of drafting objects, fields, parts, reference designators, part attributes, labels, pins, and buses. You can modify individual instances of objects, or you can choose to update the library objects so that any modifications are available to your future design sessions.  

Modifying Drafting Objects   
Modifying Fields   
Modifying Parts   
Reference Designator Renumbering   
Automatically Renumbering Reference Designators   
Setting Reference Designators by Sheet in a New Schematic   
Setting Reference Designators by Sheet in Completed Schematics   
Modifying Part Attributes   
Modifying Part Attribute Labels   
Modifying Part Type Labels   
Searching the Library for a Decal   
Rename Part   
Rename Gate   
Modifying Reference Designator Labels   
Modifying Pins   
Modifying Pin Label Fonts   
Modifying Nets   
Modifying Net Name Labels   
Modify Buses   
Modifying Bus Name Labels   
Modifying Off-Page Labels   
Modifying Label Font Sizes   
Modifying Text   
Modifying Hierarchical Components  

# Modifying Drafting Objects  

Use the Drafting Properties dialog box to modify the line width, style, and orientation of selected drafting objects.  

![](/images/d2330e1ada9889bcfac12fb10a6f10c80d2a2781412a619b6564442d0ea198da.jpg)  

Tip Use the Schematic Editing toolbar to modify the shape of 2D lines.  

**Procedure** 

1. Select a drafting object, right-click and click Properties.   
2. In the Width box, type a new line width for the drafting object. The width box lists the current line width of the selected drafting object. Use the Line Widths tab in the Options dialog box to change the default line width.  

3. Select the Filled check box to create a filled shape from a selected polygon.  

Restriction: This option is unavailable for circles, paths, and if you used Pull Arc to modify the polygon.  

4. In the Style area, select a line style option for the selected drafting object.  

5. In the Rotation box, select the degree of rotation from the Rotation list.  

!Tip  

When rotating objects, observe the following:  

• Rotation can be 0 or 90 degrees.   
• The point used when selecting the object is the also the point of rotation.  

6. Select the Mirror by X or Mirror by Y check boxes to mirror the selected drafting object in the X (horizontal) or Y (vertical) direction.  

# Modifying Fields  

Use the Field Properties dialog box to modify a field name or change its text size, orientation, or justification.  

**Procedure** 

1. Select a field, right-click and click Properties.   
2. In the Field Properties dialog box, the Name box displays the selected Field string. Modify the existing string, select a new one, or type a new text string.   
3. In the Value box, type the value you want displayed. Note that the Value box is unavailable for system fields since the value is derived from your system.   
4. To place the field at a precise X,Y coordinate location, type the value in the X and Y boxes.  

!Tip  

If this is blank when you click OK, the field attaches to the pointer until you click to indicate the location.  

5. In the Rotation list, select the degree of rotation you want.  

Rotation can be 0 or 90 degrees.  

6. In the Size box, type the font size you want.  

Stroke font sizes must be between 10 and 1000 mils; system font sizes must be between 1 and 72 points.  

7. For stroke font, in the Line Width box, type the line width.  

8. For system fonts, select the font you want to use in the Font list.  

You can also click a system font style you want applied: B for Bold, I for Italic, or U for Underlined.  

9. To set the Justification, click the Horizontal and Vertical options you want.  

10. Click OK.  

# Modifying Parts  

Use the Part Properties dialog box to create and edit part attributes. You can also define signal pins and control the visibility of attributes assigned to the part.  

![](/images/9b09d08a78de15c9ee981d5560106d096eefc8a82d129fddbbfd25b20b516ea6.jpg)  

Tip   
This dialog box contains several sub-dialog boxes. Before using any of these sub-dialog boxes, changes made in open dialog box must be applied to the design.   
Changing the Reference Designator   
Changing the Part Type   
Changing Part Information   
Changing the Visibility of Text   
Changing Part Attributes   
Changing PCB Decals   
Assigning Unused Pins as Signal Pins  

# Changing the Reference Designator  

If you need to reassign gates in your design, you can change the reference designator of a selected gate  

**Procedure** 

1. Select a part, right-click and click Properties.   
2. In the Reference Designator area, click Rename Gate to change the reference designator of the selected gate, type the new gate reference designator information and click OK.   
3. Click Rename Part to change the reference designator of the selected part, type the new part reference designator information and click OK.  

# Changing the Part Type  

Use the Change Part Type dialog box to change the selected part(s) to a new part type. The new part type can be one that already exists in the schematic or in the parts library.  

**Procedure** 

1. Click the Tools $>$ Options menu item, then click the Design category.   
2. Set the “Allow overwriting of attribute values in design with blank values from library” check box appropriately to allow or prevent overwriting of non-blank attribute values with blank (“placeholder”) values from the library.   
3. Select a part or parts, right-click and click Properties.   
4. In the Part Type area, click Change Type to change the selected part(s) to a new part type.  

5. In the Change Part Type Dialog Box, use the Filter to limit your search results to a chosen library (or libraries) for a specific part or item name, or names that match a wildcard or expression on page 105. Click Apply to search the libraries and display the search results.  

6. Use the Library dropdown list to select specific library directories or the All Libraries setting.  

7. Type \* to view all parts or items in the chosen libraries.  

8. Scroll through the Parts list to find a part type.  

!Tip  

When examining the parts list, note the following:  

• The Parts list box displays the parts that matched the search filter settings.   
• The decal of a selected part displays in the preview area to the left of the list box.  

9. Set how attributes are updated in the Attributes area.  

10. Set how parts are updated in the “Apply update to” area.  

!Tip  

When updating parts, observe the following:  

• You can update the part definition in the schematic with a modified version in the library.   
Select the same part name, then click All Parts This Type in the “Apply Update to” Area.   
• If you change a part type to one with fewer pins, the connections going to the missing pins are not deleted. They are attached to automatically generated off-page symbols. You are notified of all disconnected pins.  

# Changing Part Information  

As your design needs evolve, you can change part properties as required.  

**Procedure** 

1. Select a part, right-click and click Properties.   
2. Click Statistics to display gate and connection information for the selected part. This information is displayed in the default text editor so you can save the contents to a file.   
3. Select a gate decal name from the Gate Decal list to change the gate decal of the selected gate or part to one of the predefined alternate decals.  

# Changing the Visibility of Text  

You may decide to retain but turn off the visibility of certain text objects in your design. An example would be to turn off the display of the tolerance values for a family of components such as resistors where they all are assigned a default value.  

**Procedure** 

1. Select a part, right-click and click Properties.   
2. Click Visibility to change the visibility of associated text. See also Controlling Text Visibility for a Part.  

# Changing Part Attributes  

As your design progresses, you may find it necessary to change or modify attributes. You can change the attributes by modifying the part properties.  

**Procedure** 

1. Select a part, right-click and click Properties.   
2. Click Attributes to assign or modify part attributes. See also Modifying Part Attributes.  

# Changing PCB Decals  

Use the PCB Decal Assignment dialog box to assign alternate PCB decals to schematic parts. Decal names are included in the netlist file to display the proper decal, or footprint, when the file is imported into the PCB design file. You can select a decal assigned as an alternate during part creation, override the decal with one from the library, or enter a name for an undefined decal you plan to create later in the PCB design.  

**Procedure** 

1. Select a part, right-click and click Properties.   
2. Click PCB Decals to assign alternate PCB decals.   
3. In the PCB Decal Assignment dialog box, in the Assigned in Schematic box, type a new decal name for a decal you plan to create later in the PCB design.  

!Tip  

The Assigned in Schematic box displays the name of the currently selected decal as it is assigned to the schematic from the current library.  

4. Select the “No specific PCB Decal” check box to remove the assigned decal.  

The default decal assigned to the part type is used when the netlist is imported to SailWind Layout;   
no decal assignment appears in the netlist.  

5. In the Alternates in Library list, select a decal from the current part type definition in the library.  

6. Click Assign to assign the decal to the part.  

i Tip The preview window displays the currently selected decal.  

7. Click the Browse button to search a library for a decal. See also Searching the Library for a Decal.  

8. Set how parts are updated in the Apply update to area.  

• This Part — Only updates the selected part.   
• All Parts This Type — Updates all matching parts in the design with the new decal.  

9. Click OK.  

# Assigning Unused Pins as Signal Pins  

Use the Part Signal Pins dialog box to assign any unused pins as additional signal pins. When the part type is created and stored in the library, the standard power and ground pins for part types are defined.  

Signal pins assigned during part creation cannot be modified through this dialog box. Instead, use the Assigning Signal Pin Names to Parts dialog box in the Library Manager.  

**Procedure** 

1. Select a part, right-click and click Properties.  

2. Click Sig Pins.  

The Part Signal Pins dialog box lists pins and their corresponding signal names. A signal pin is a pin that has a signal net (GND for example) assigned by a schematic capture program during part type creation.  

See also “Part Information - Pins” on page 147.  

3. In the Part Signal Pins dialog box, select a pin in the Unused Pins list.  

4. Click Add to add the unused pin to the Signal Pins list.  

5. Assign a signal name in the Signal Pins area.  

6. To modify the signal name of the pin, select the pin in the Signal Pins list and click Edit.  

7. To move the pin to the Unused Pins list, select the pin in the Signal Pins list and then click Remove.  

8. Set the update settings in the Apply update to area.  

• This Part — Updates the selected part only.   
• All Parts This Type — Updates all parts of the same type.  

9. Click OK.  

# Reference Designator Renumbering  

Manually renumber single or automatically renumber reference designators in the schematic. SailWind Layout can renumber the reference designators automatically in a pattern, to optimize finding your parts on a manufactured printed circuit board. Once the parts are renumbered in SailWind Layout, you can synchronize the designs again by back annotating an .eco file of the changed designators.  

To manually renumber a reference designator in SailWind Logic, see Changing the Reference Designator.  

To automatically renumber reference designators in SailWind Logic, see “Automatically Renumbering Reference Designators” on page 280.  

To automatically renumber the reference designators in SailWind Layout, see Changing the Reference Designators of Multiple Components in ECO Mode (Autorenumbering) in the SailWind Layout Guide.  

# Automatically Renumbering Reference Designators  

Renumber reference designators on a sheet by sheet basis with control over the starting value, increment, and pattern.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Auto Renumber Parts button  

2. In the “Auto Renumber Parts Dialog Box” on page 473, select the sheets to renumber.  

3. Choose which reference designator prefixes to renumber.  

4. If needed, set the Cell size to smaller cells. See the example below.  

5. Set the Renumber settings for your situation.  

6. Set the Precedence pattern.  

7. Click OK.  

An ECO file is automatically generated. If the Output window is open, a link to the file appears in the log. If the output window is closed, the ECO file opens in your default text editor.  

8. If the board layout has already been started in SailWind Layout, you must import the ECO file to update the reference designators in SailWind Layout. This exact file must be used. Do not overwrite this file with a new one or generate an ECO file using the Compare/ECO Tools until SailWind Layout has been updated with the renumbering. In SailWind Layout, click the File $>$ Import menu item. Browse for the .eco file and import the changes.  

# Examples  

The following graphic displays the result of a smaller cell size on the parts in the schematic. Cell borders have been drawn to illustrate how it works. The parts within the cells are renumbered in the Precedence pattern and then the cells also are processed in the same pattern.  

![](/images/1e9466fcf0b9cdcbeb56363131e9ac0f098246e722771cf02eedda687f1aea6b.jpg)  
Figure 5. Cell Size Illustration  

# Setting Reference Designators by Sheet in a New Schematic  

Set reference designator start values by sheet. If you will have multiple channels, each occupying one schematic sheet, and you want the reference designators to have predetermined ranges you can set a start value for designated sheets.  

**Procedure** 

1. Click the Setup $>$ Sheets menu item.   
2. In the “Sheets Dialog Box” on page 717. Click the Add button and add all the sheets for the multiple channels.   
3. Name the schematic sheets.   
4. In the RefDes Start Value column, for each channel sheet, type the starting value for referenc designators of components added or copied and pasted to the schematic sheet.  

# Setting Reference Designators by Sheet in Completed Schematics  

Renumber reference designators in schematics that already have assigned reference designators.. If you will have multiple channels, each occupying one schematic sheet, and you want the reference designators to have predetermined ranges you can renumber them.  

# Prerequisites  

• Determine which schematic sheets need to be renumbered and which reference designators should be renumbered on those sheets.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Auto Renumber Parts button.   
2. In the “Auto Renumber Parts Dialog Box” on page 473, select the sheets to renumber.   
3. Choose which reference designator prefixes to renumber.   
4. If needed, set the Cell size to smaller cells. See the example below.   
5. Set a Start Value and Increment value.   
6. Select the “Increment Start Value by Sheet” check box.   
   This sets the starting number to match the sheet number and not the order of the sheet in the list.   
7. Set the Precedence pattern.   
8. Click OK.  

# Examples  

The following graphic displays the result of a smaller cell size on the parts in the schematic. Cell borders have been drawn to illustrate how it works. The parts within the cells are renumbered in the Precedence pattern and then the cells also are processed in the same pattern.  

![](/images/734f466438bc7fe002f3bac984a44c03eb80f6abeec2b2bc22ac65b10af49b03.jpg)  
Figure 6. Cell Size Illustration  

# Modifying Part Attributes  

Use the Part Attributes dialog box to assign or modify part attributes, which is information about the part such as manufacturer and cost.  

**Procedure** 

1. Select a part, right-click and click Attributes.   
2. To add an attribute to a part on the schematic, click Add.   
3. In the Name column type a name or click Browse Lib Attr to select an existing attribute name.   
4. In the Value column, type a value for the attribute.   
5. To edit a name or value in the Attributes list, select a name or value and click Edit or double click   
   name or value.   
6. To delete an attribute, select a name or value and click Delete.  

7. Set how parts are updated in the “Apply update to” area.  

• This Part — Only updates the selected part.   
• All Parts This Type — Updates all matching parts in the design.  

![](/images/3318355c22b860d23451d8214df1d605faec6e57c7d7f80e7c31c2af700801d3.jpg)  

!Tip  

Adding or changing attributes in a part at the schematic level does not update the part type (in the library). Edit the part in the Part Editor to update the library part.  

# Related Topics  

Part Editor Operations Attributes Overview  

# Modifying Part Attribute Labels  

Use the Attribute Properties dialog box to provide text and font settings for one or more part attribute labels.  

**Procedure** 

1. Select nothing, right-click and click Select Documentation.  

2. Select a part attribute label, right-click and click Properties.  

3. In the Attribute Properties dialog box, type a new value for the attribute.  

![](/images/4a3fbbcf1e2403341bb300ef7867c00f8539b6de26c5d19840f043be25d6e6d8.jpg)  

Tip If you selected multiple attribute labels, you cannot change the value.  

4. In the Rotation box, select the degree of rotation from the Rotation list. Rotation can be 0 or 90 degrees.  

5. In the Size box, type the size in mils for the height of the stroke font (from the top of the tallest character to the bottom of the lowest character), or in points for system fonts.  

![](/images/945e9a0c275b55997324388bbded67110e48f5eabc556564228fc471829de6ca.jpg)  

Tip   
Type a stroke font size between 10 and 1000 mils or a system font size between 1 and 72 points.  

6. For stroke font, in the Line Width box, type the width of the line used to create the characters.  

7. For system fonts, select the font you want to use.  

You can also click a system font style you want applied: B for bold, I for Italic, or U for Underlined.  

8. To set the Justification, click the Horizontal and Vertical options you want.   
9. Click OK.  

# Modifying Part Type Labels  

Use the Part Type Label Properties dialog box to provide text and font settings for one or more part type labels.  

**Procedure** 

1. Select nothing, right-click and clickSelect Documentation.   
2. Select a part type label, right-click and click Properties.   
3. In the Part Type Label Properties dialog box, click Change Type if you want to change the part type. See also Changing the Part Type.   
4. In the Rotation box, select the degree of rotation from the Rotation list. Rotation can be 0 or 90 degrees.   
5. In the Size box, type the size in mils for the height of the stroke font (from the top of the tallest character to the bottom of the lowest character), or in points for system fonts. Tip   
   Type a stroke font size between 10 and 1000 mils or a system font size between 1 and 72 points.  

![](/images/13071c11df89796857c6b268806edc23eb723ff367191238f77034b0079b55c2.jpg)  

6. For stroke font, in the Line Width box, type the width of the line used to create the characters.  

7. For system fonts, select the font you want to use. You can also click a system font style you want applied: B for Bold, I for Italic, or U for Underlined.  

8. To set the Justification, click the Horizontal and Vertical options you want.  

9. Click OK.  

# Searching the Library for a Decal  

Use the Get Decal from Library dialog box to search a library for a decal. You can use the filters to quickly narrow down your search parameters to find the exact part that you require.  

**Procedure** 

1. Select a part, right-click, click Properties, and then click the PCB Decals button.   
2. In the PCB Decal Assignment dialog box, click the Browse button.  

3. In the Get Decal from Library dialog box, use Filter to limit your search results to a chosen library (or libraries) for a specific part or item name, or names that match a wildcard or expression on page 105. Click Apply to search the libraries and display the search results.  

!Tip  

When searching, observe the following:  

• Use the Library dropdown list to select specific library directories or the All Libraries setting.   
• Type a prefix plus an asterisk in the Items text box. For example, type ${\mathsf{D}}{\mathsf{I}}{\mathsf{P}}^{\star}$ to view all decals that begin with DIP. Type an asterisk only to view all decals in the selected libraries. Type only\* to view all parts or items in the chosen libraries.   
• Enter a value in the Pin Count text box to narrow the search further. Pin Count grays if a decal is already defined for the selected part. Pin Count is on if the No Specific PCB Decal is on in the PCB Decal Assignment dialog box.  

4. Scroll through the Decals list box to find and select a decal.  

![](/images/935d7484d4608606c4f6a920dbd22e25394d095eb3a16e8f4bfda22b08af8a49.jpg)  

!Tip  

Decals are displayed as follows:  

• The Decals list box displays the decals that matched the search filter settings.   
• The selected decal displays in the preview area to the left of the list box.  

5. Click OK to exit the dialog box.  

You return to the PCB Decal Assignment dialog box.  

# Rename Part  

Use Rename Part to change the reference designator for the selected part or gate. All gates are renamed if you change the reference designator of one gate of a multi-gated part. You are prevented from assigning an already used reference designator.  

**Procedure** 

1. Select a part, right-click and click Properties.   
2. In the Part Properties dialog box, click Rename Part.   
   An information window displays.   
3. Type the new part reference designator information.   
4. ClickOK.  

# Rename Gate  

Use Rename Gate to change the reference designator of the selected gate. You are prevented from assigning an already used reference designator or an unused gate of a part with a different part type.  

**Procedure** 

1. Select a part, right-click and click Properties.   
2. In the Part Properties dialog box, click Rename Gate.   
   An information window displays.   
3. Type the new gate reference designator information.   
4. ClickOK.  

# Modifying Reference Designator Labels  

Use the Reference Designator Properties dialog box to view and modify label size and justification as wel as text and font settings for one or more reference designator labels.  

**Procedure** 

1. Select nothing, right-click and click Select Documentation.  

2. Select a reference designator label, right-click and click Properties.  

3. In the Reference Designator Properties dialog box, in the Rename area, select Gate to rename just the single gate. Select Part to rename the entire part.  

Tip If you select a gate with only one part, Gate is unavailable.  

4. In the Rotation box, select the degree of rotation from the Rotation list. Rotation can be 0 or 90 degrees.  

5. In the Size box, type the size in mils for the height of the stroke font (from the top of the tallest character to the bottom of the lowest character), or in points for system fonts.  

!Tip  

Type a stroke font size between 10 and 1000 mils or a system font size between 1 and 72 points.  

6. For stroke font, in the Line Width box, type the width of the line used to create the characters.  

7. For system fonts, select the font you want to use. You can also click a font style you want applied: B for Bold, I for Italic, or U for Underlined.  

8. To set the Justification, click the Horizontal and Vertical options you want.  

9. Click OK.  

# Modifying Pins  

Use the Pin Properties dialog box to view pin information, to modify parts and nets to which the selected pin is connected, and also to set font settings for pin number and pin name labels.  

**Procedure** 

1. Select a pin, right-click and click Properties.   
2. In the Pin Properties dialog box, click the Part/Gate button to change part or gate attribute information. See also Modifying Parts.   
3. Click the Net button to modify the net name and attributes of a named net.  

!Tip  

To modify the net name or attributes of a $\$89$ named net, use the Query Mode button to select a net near a pin to change it from a $\$89$ named net.  

See also Modifying Nets.  

4. Click the Font button to open the Pin Label Fonts dialog box where you set font preferences. See also Modifying Pin Label Fonts.  

5. Click OK.  

# Modifying Pin Label Fonts  

To improve the legibility of your schematic, you can use the Pin Label Fonts dialog box to change the fonts of a pin label.  

**Procedure** 

1. Select a pin label, right-click and click Properties.   
2. In the Pin area of the Pin Label Fonts dialog box, type the line width in the Line Width box for stoke font.   
3. For stroke or system fonts, in the Size box, type the size  (in mils for stroke font, in points for system fonts).  

!Tip  

Type a stroke font size between 10 and 1000 mils or a system font size between 1 and 72 points.  

4. For system fonts, select the font you want to use. You can also click a font style if you want one: B for bold, I for italic, or U for underlined.  

5. Click OK.  

# Modifying Nets  

To rename a net or edit its attributes and values, you can use the Net Properties dialog box to access net specific properties.  

**Procedure** 

1. Select a net, right-click and click Properties.  

!Tip  

Select the connection segment where it enters or exits a part. Selecting any other segment of the connection will not allow net name labels to be added.  

2. Type a new name in the Net Name box or select an existing name from the list.  

!Tip  

When working with net names, observe the following:  

• If you select a name from the list, the message “Net <netname> already exists - OK to combine nets (Y/N)?” appears. Click Yes to combine the nets, or click No to enter a different net name.   
• If you delete all visible net name labels, the net and all subnets retain the net name. Net names do not revert to a generated $\$59$ nnnn system number. You must rename the net.   
• If you attempt to combine a named and an unnamed net, the resulting net will always take the name of the named net. Any similar attribute names will always take their values from the named net.   
• The Connectivity Report identifies subnets tied together without a visible net name by   
flagging them as missing an off-page symbol.  

3. In the Rename area, click This Instance to apply the new net name to the selected connection or click All Instances to apply the new net name to all instances of this connection.  

![](/images/c701e1645c988fbb8923ed7750127fa1c027c77295fc1f5cf79a221f6f7a160b.jpg)  

Tip Selecting This Instance will cause the net to be split into two separate nets.  

4. Select the Net Name Label check box to add a visible label to the selected net segment.  

You must select the connection segment where it enters or exits a part, or the Net Name Label check box will be unavailable.  

!Tip  

Clearing the Net Name Label check box removes the visible label. The net and all subnets retain the net name.  

5. Click Statistics to display connection information in the default text editor.  

6. Click Attributes to open the Net Attributes dialog box and modify the net attributes. See also Creating Net Attributes.  

7. Click Rules to open the Net Rules dialog box and modify the net rules.  

See also Setting Up Net Rules.  

8. Click OK.  

The new net name is placed over the connection segment.  

0 Tip Use Using Move Mode to adjust the placement of the net name text.  

# Modifying Net Name Labels  

Use the Net Name Properties dialog box to provide or change text and font settings for one or more net name labels.  

**Procedure** 

1. Select nothing, right-click and click Select Documentation.  

2. Select a net name label, right-click and click Properties  

3. Type a new name in the Net Name box or select an existing name from the list.  

!Tip  

When working with net names, observe the following:  

• If you select a name from the list, the message “Net <netname> already exists - OK to combine nets (Y/N)?” appears. Click Yes to combine the nets, or click No to enter a different net name.   
• If you delete all visible net name labels, the net and all subnets retain the net name. Net   
names do not revert to a generated $\$89$ nnnn system number. You must rename the net.   
• If you attempt to combine a named and an unnamed net, the resulting net will always take the name of the named net. Any similar attribute names will always take their values from the named net.   
• The Connectivity Report identifies subnets tied together without a visible net name by flagging them as Subnets with Missing Net Name.  

4. In the Rename area, click This Instance to apply the new net name to the selected connection or click All Instances to apply the new net name to all instances of this connection.  

![](/images/75658168fe8d69bfee556f865f86f64740e6489f3815025a4c70b6dd665aaf64.jpg)  

Tip   
Selecting This Instance will cause the current segment of the net to take the new net name and be split from the other instances.  

5. In the Rotation box, select the degree of rotation from the Rotation list.  

Rotation can be 0 or 90 degrees.  

6. In the Size box, type the size in mils for the height of the stroke font (from the top of the tallest character to the bottom of the lowest character), or in points for system fonts.  

!Tip  

Type a stroke font size between 10 and 1000 mils or a system font size between 1 and 72 points.  

7. For stroke font, in the Line Width box, type the width of the line used to create the characters.  

8. For system fonts, select the font you want to use.  

You can also click a system font style you want applied: B for Bold, I for Italic, or U for Underlined.  

9. To set the Justification, click the Horizontal and Vertical options you want.  

10. Click OK.  

# Modify Buses  

Use the Bus Properties dialog box to change the name of a bus or change the bus type.  

Changing the Name of a Bus Changing the Bus Type Managing Bus Nets  

# Changing the Name of a Bus  

As your design evolves, you may need to add or delete nets to or from a bus. Once you have made these modifications, you can change the name of a bus to reflect those changes.  

**Procedure** 

1. Select a bus, right-click and click Properties.   
2. Type a new name for the bus in the Bus Name box or select an existing name from the list. See also Naming Buses.  

!Tip  

If you change the bit range for a bit format bus, the new bit range nn:mm must be equal to or greater than the old bit range. The signals attached to the bus will keep their old bit number, but take the new name.  

3. In the Rename area, click This instance to apply the new bus name to the selected bus, or click All instances to apply the new bus name to all instances of this bus.  

4. Select the Bus Name Label check box to add a visible label to the selected bus.  

# Changing the Bus Type  

As your design evolves, you may find it necessary to change the type of a bus from a bit format bus to a mixed net bus or the other way around. You can use Properties to change the bus type.  

**Procedure** 

1. Select a bus, right-click and click Properties.   
2. In the Bus Type area, click the bus type you want. The Bus Type determines which bus names appear in the Bus Name list.  

!Tip  

If you change the bus type from bit format to mixed net bus, the bus name changes to just the prefix. The bus name prefix and bit range are added to the Bus Nets list box.  

![](/images/97da91ee9ea03bb1ce7b2b327cd4596c153d79c860c19637b248d857154da713.jpg)  

# Restriction:  

You can change a mixed net bus to a bit format bus only if all of the connected nets conform to the bit sequenced names, which you define in the Bus Name text box. Before you can change a mixed net bus to a bit format bus, you must delete the bus nets from the Bus Nets list box.  

# Managing Bus Nets  

You may find it necessary to expand the range of a bus to include additional sequential nets. Use Properties to add sequential nets to a bus.  

# Restrictions and Limitations  

The Bus Nets area is not available when the Bit Format bus type is selected.  

**Procedure** 

1. Select a bus, right-click and click Properties.   
2. Click Add to add a new row in the Bus Nets list.   
3. Type the bus prefix in the Name/Prefix column.  

!Tip  

Use the following naming conventions:  

• For a single net, type the net name.   
• For a range of sequential nets, type the prefix for the sequence of nets.  

4. In the Start column, type the starting bit number for a sequence of nets.  

5. In the End column, type the ending bit number for a sequence of nets.  

!Tip  

To add an individual net to the bus, type the net name in the Prefix/Name column. Do not type Start and End values for a single net that is not sequenced by bit number.  

6. Click Edit to modify a selected cell in the Bus Nets list.  

7. Click Delete to remove a net from the Bus nets list.  

8. Click Down to move the selected row down one position in the Bus Nets list.  

0 Tip The order in which nets appear in the Bus Nets list determines the default order for naming nets as they are connected to a bus.  

9. Click Up to move the selected row up one position in the Bus Nets list.  

# Related Topics  

Managing Buses Modifying Bus Name Labels  

# Modifying Bus Name Labels  

Use the Bus Name Properties dialog box to provide or change text and font settings for one or more bus name labels.  

**Procedure** 

1. With nothing selected, right-click and click Select Documentation.  

2. Select a bus name label, right-click and click Properties.  

3. In the Bus Name Properties dialog box, click Bus to open the Bus Properties dialog Box. See also Modify Buses.  

4. In the Rotation box, select the degree of rotation from the Rotation list. Rotation can be 0 or 90 degrees.  

5. In the Size box, type the size in mils for the height of the stroke font (from the top of the tallest character to the bottom of the lowest character), or in points for system fonts.  

![](/images/9fd5f3f0dcad7643ba6b870674eae3764cee63ee763610197688e6193f70290c.jpg)  

Tip   
Type a stroke font size between 10 and 1000 mils or a system font size between 1 and 72 points.  

6. For stroke font, in the Line Width box, type the width of the line used to create the characters.  

7. For system fonts, select the font you want to use. You can also click a system font style you want applied: B for Bold, I for Italic, or U for Underlined.  

8. To set the Justification, click the Horizontal and Vertical options you want.  

9. Click OK.  

!Tip  

Font properties you specify in the Net Name Label Properties dialog box are also applied to the off-page reference label.  

# Modifying Off-Page Labels  

Use the Off Page Properties dialog box to set the maximum sheet numbers per line and the rotation settings for off page labels.  

**Procedure** 

1. Select an off-page label, right-click and click Properties.   
2. In the Off-Page Properties Dialog Box, type the maximum sheet numbers allowed per line, from 0 to 99.   
3. In the Rotation box, select the degree of rotation from the Rotation list. Rotation can be 0 or 90 degrees.   
4. Click OK.  

# Modifying Label Font Sizes  

New labels are created using a system default font size. You can’t change this default, but you can modify the font sizes of labels after they are created.  

**Procedure** 

1. Select the labels you want to change, right-click and click Properties.  

# Restriction:  

All the labels selected must be of the same type; for example, all net name labels or all reference designator labels.  

2. In the Properties dialog box, enter the new Size value.  

!Tip  

Type a stroke font size between 10 and 1000 mils or a system font size between 1 and 72 points.  

# 3. Click OK.  

Table 32. Related Topics   


<html><body><table><tr><td>Attribute Properties Dialog Box</td><td>Part Type Label Properties Dialog Box</td></tr><tr><td>Bus Name Properties Dialog Box</td><td>Pin Label Fonts Dialog Box</td></tr><tr><td>Net Name Properties Dialog Box</td><td>Reference Designator Properties Dialog Box</td></tr></table></body></html>  

# Modifying Text  

Use the Text Properties dialog box to modify free text or change its size, orientation or justification.  

**Procedure** 

1. Select text, right-click and click Properties.   
2. In the Text Properties dialog box, the Text box displays the selected text string. Modify the existing text string, or type a new text string.   
3. In the X,Y location boxes, type new values to move the text string to a specified location. If you need to move text outside the sheet, you must move the text with the cursor instead.   
4. In the Rotation box, select the degree of rotation from the Rotation list. Rotation can be 0 or 90 degrees.  

5. For stroke font, in the Line Width box, type the line width.  

6. In the Size box, type the size  (in mils for stroke font, in points for system fonts).  

!Tip  

Type a stroke font size between 10 and 1000 mils or a system font size between 1 and 72 points.  

7. For system fonts, select the font you want to use.  

You can also click a font style: B for bold, I for Italic, or U for Underlined.  

8. In the Justification area, set the horizontal and vertical justification of the text.  

9. If you combined the selected text string with a drafting object, click Parent to display the Drafting Objects Properties dialog box to modify the drafting object.  

10. Click OK.  

# Related Topics  

Modifying Drafting Objects Combining 2D Lines and Text  

# Modifying Hierarchical Components  

When created and added to an existing sheet, hierarchical components cannot be accessed through the Sheet list in the toolbar unless the parent sheet is displayed. They are also excluded from the Sheet command in the Setup menu. Use the Hierarchical Component Properties dialog box to assign a hierarchical component to the next available sheet number to make it accessible from the Sheet list when a sheet other than the parent sheet is displayed.  

Use the Sheets command under the Setup menu to modify the sheet name or the numeric order.  

**Procedure** 

1. Select a hierarchical component, right-click and click Properties.   
2. In the Query Hierarchical Component dialog box, type a new name in the Name box to rename the hierarchical component.   
3. Select the Visibility check box to the right of the Name box to display the name on top of the hierarchical component in the schematic.   
4. Click Numbered to assign the hierarchical component the next available sheet number. The assigned sheet number is displayed in the field above this option.   
5. Click Un-numbered to remove a sheet number assignment from a hierarchical component.   
6. In the Associated Sheet area, select the Visibility check box to display the sheet number in the schematic.   
7. ClickOK.  

