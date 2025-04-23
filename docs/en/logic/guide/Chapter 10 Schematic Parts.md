# Chapter 10 Schematic Parts  

Numerous methods are available for adding, swapping, saving, updating and controlling visibility of parts in your design. These operations can be performed on individual design objects, or groups of objects.  

Adding Parts   
Adding Connector Pins   
Adding Single Gate Parts   
Adding Multigate Parts   
Controlling Text Visibility for a Part   
Using Alternate Symbols   
Swapping Reference Designators   
Saving Part Types to a Library   
The Update From Library Function   
Deleting a Part   
Deleting a Part and Its Connections   
Cut, Copy, and Paste   
Copy as Bitmap   
Creation of Groups   
Group Anchor Points   
Management of Groups   
Attributes Overview   
Manage Attributes in a Schematic   
Resistor Values Defined on Parts  

# Adding Parts  

Use the Add Part from Library dialog box to load a part from a library into the current schematic drawing.   
SailWind Logic automatically assigns a reference designator when you add the part.  

Refer to the Adding Single Gate Parts and Adding Multigate Parts topics for additional information.  

Refer to the Using Duplicate Mode topic for information on adding parts by making copies of parts that already exist in the schematic.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Add Part button.  

2. Select a part in the Items list or select a part from the Part Name dropdown list box in the Add Part From Library Dialog Box.  

![](/images/385cae5fd27c3044e65d89f6c502e87abc4ae3eda5922de2574833f042789678.jpg)  

!Tip  

Use the filter to locate the part. Use the wildcard convention, with or without leading characters, to expand or narrow the filter. Click Apply to activate the filter.  

3. Click Add. The part attaches to and follows the cursor movement.  

(Optional) You can rotate or mirror the item before you indicate its location. Right-click and click Rotate 90, X Mirror, and Y Mirror as often as needed to set the correct orientation of the item. Click Alternate to place an alternate symbol, if available. Click Next Type to select a different gate in the part, if available.  

4. Click on the schematic to place the part; another instance attaches to the cursor automatically.  

5. When you are done adding the part(s), right-click and click the Cancel popup menu item or press the Esc key.  

**Related Topics**  

Using Alternate Symbols Adding Connector Pins  

# Adding Connector Pins  

Connector pins are special symbols within SailWind Logic libraries. You add them like multigate parts, whereby the pin number increments each time you add a connector symbol. SailWind Logic does not increment the reference designator until you use all the connector pins.  

After adding one or more pins of a connector and establishing a reference designator, use Using Duplicate Mode to add additional pins. This causes SailWind Logic to use the same reference designator for new pins.  

# Adding Single Gate Parts  

Single gate parts are parts that are represented by a single schematic symbol. When you add the part to the schematic, unique reference designator assignment starts with the next available reference designator number.  

The Adding Parts section lists the step-by-step procedure.  

You specify the reference designator prefix in the General tab on page 136 of the Part information dialog box when you create a part.  

Related Topics  

Adding Multigate Parts  

# Adding Multigate Parts  

Multigate parts are parts that consist of more than one symbol or gate to represent a complete part; for example, a 7400 which contains 4 gates. You can create parts that have multiple gates of a single type or multiple gates of different types.  

When you add a new multigate part, the gate with the lowest set of pin numbers is used along with the next available reference designator and an alphanumeric suffix, or gate modifier. The reference designator and suffix are separated by the dash $(-)$ character. For example, a 7400 added to a new schematic would use the gate with pins 1 through 3 and would be assigned as part U1-A. When you add additional gates of the same part, the next available gate and gate modifier is used, for example, the gate with pins 4 through 6 is added and assigned as U1-B.  

SailWind Logic continually manages the packaging of gates in a schematic. If you delete, rename, or change the part type of a gate, SailWind Logic keeps track of these changes and fills in the gaps when a new gate is added.  

# Using Alphanumeric Prefixes  

You can use any combination of letters and numbers in SailWind Logic to define a reference designator prefix.  

You specify this prefix in the General tab on page 136 of the Part information dialog box when you create a part.  

If you specify a reference designator prefix that contains alphanumeric characters, SailWind Logic maintains this prefix for multigate parts. A prefix of U1A for a part containing four gates, when added to a design, would use reference designator assignments U1A-A, U1A-B, U1A-C, and U1A-D.  

“Adding Parts” on page 189   
• Adding Single Gate Parts   
Rename Gate   
Rename Part   
Modifying Parts  

# Controlling Text Visibility for a Part  

Use the Part Text Visibility dialog box to control the display of text associated with the selected part. You can control the visibility of one part or all parts of the same type.  

**Procedure** 

1. Select a part, right-click and click the Visibility popup menu item.   
2. In the Attributes list, select the check boxes of attributes to display in the schematic.   
3. In the “Item Visibility” area, select the check boxes to display the corresponding label, such as par type or pin numbers.   
4. In the “Attribute Name Display” area, set the attribute name option. Display just the attribute value or display the attribute name and its value, for example, PCB DECAL $\c=$ SO14. • All Off — Makes all attribute names invisible, displays only the value. • No Change — Keeps the current attribute name visibility settings. • All On — Displays all attribute names and their values.  

5. In the “Apply Update to” area, set the selected part update options. This area is unavailable if you have selected more than one part on the schematic.  

This Gate — Updates the selected gate. This Part — Updates a part or all associated gates of a part. • All Parts This Type — Updates all matching gates or parts in the design  

6. Click OK.  

![](/images/b2544efeacc3b34fb7e8891b00cd791ad83af22430e64cfcde3f553ce190f982.jpg)  

!Tip  

When using object mode selection on page 177, with multiple parts selected, check boxes may be in an intermediate state (selected, yet you cannot edit them) because some selected parts have the check box selected and others have it cleared. You can select or clear the check box and update all selected parts.  

# Using Alternate Symbols  

Some parts can be shown in the schematic with more than one representation. One example of this is the NAND gate, with its DeMorgan representation. A second example is the use of IEEE and ANSII symbol standards. Within SailWind Logic’s library, it is possible to define one primary and up to three alternate symbols for a part.  

While placing the part in the schematic, the Alternate command enables you to select the version you want to use in the schematic.  

Power symbols, ground symbols, and off-page reference symbols are also available as alternate symbols  

When you add a new part or duplicate an existing part, and you want the alternate representation, rightclick and click Alternate before placing the part.  

**Procedure** 

Right-click and click the Alternate popup menu item while in Duplicate or Move mode.  

# Swapping Reference Designators  

To swap reference designators, you can use the Swap Ref. Des. button on the Schematic Editing toolbar or Swap Ref. Des. on the popup menu. If the reference designator prefixes of the selected parts are different, swapping also updates the reference designators of other parts in the package.  

Swapping Reference Designators Using Verb Mode Swapping Reference Designators by Selecting One Part at a Time Swapping Reference Designators by Selecting Both Parts First  

# Swapping Reference Designators Using Verb Mode  

You can swap reference designators using verb mode. Using verb mode enables you to initiate the command and then perform consecutive swap operations without having to restart the command each time.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Swap Ref. Des. button.   
2. Select the first part.   
3. Select the second part with which to swap reference designators. The software changes or swaps the reference designators on the selected parts. Alternatively, to use the popup menu to swap reference designators, you can either select one part at a time or select both parts at once.  

# Swapping Reference Designators by Selecting One Part at a Time  

You can swap reference designators by selecting one part at a time.  

**Procedure** 

1. Select the first component.   
2. Right-click and click the Swap Ref. Des. popup menu item.   
3. Select another component to complete the swap.  

# Swapping Reference Designators by Selecting Both Parts First  

You can swap reference designators by selecting both parts first, and then specifying the command.  

**Procedure** 

1. Using Ctrl $^+$ click, select the component reference designators you want to swap.   
2. Right-click and click the Swap Ref. Des. popup menu item to complete the swap.  

# Saving Part Types to a Library  

You can save one part type, multiple part types, or all part types in a schematic to the library.  

Saving One or More Part Types in the Schematic Saving All of the Part Types in the Schematic Saving Off-Page to Library  

# Saving One or More Part Types in the Schematic  

You can save one or more part types to a library. Once saved to the library, these parts are available for use in the current design as well as future design sessions.  

**Procedure** 

1. Select one or more parts in the schematic.   
2. Right-click and click the Save to Library popup menu item.   
   The Save Part Types to Library Dialog Box appears.   
3. Select the library where you want to save the part types.   
4. Click OK.  

# Saving All of the Part Types in the Schematic  

You can save all of the part types in the schematic to a library. This enables you to quickly save all of the part types and make them available for the current and future design sessions.  

**Procedure** 

1. Right-click and click the Select Parts popup menu item.   
2. Right-click again and click the Select All on Schematic popup menu item.   
3. Right-click and click the Save to Library popup menu item.   
   The Save Part Types to Library Dialog Box appears.   
4. Select the library where you want to save the part types.  

5. Click OK.  

!Tip  

When saving part types, observe the following:  

• If a part type or logic decal you are saving already exists in the library, a message box appears. Click Yes to overwrite the part type or logic decal in the library. Click No to save only those part types that do not already exist in the library. Click Cancel to return to the Save Parts to Library dialog box without saving the part types to the library. • When parts of the same type have attributes with the same values, the attribute names and values are saved in the library with the part type. When parts of the same type have different values for the same attribute name, only the attribute name with a blank value is saved to the library.  

# Saving Off-Page to Library  

Use Save Off-page to Library to update the off-page, ground, or power symbols in the library with the current version(s) in the schematic.  

**Procedure** 

1. Click the Tools $>$ Save Off-page to Library menu item.   
2. Select the symbol to update.   
3. Click OK. The selected item is opened in the Part Editor.   
4. Modify the symbols as required.   
5. Click the File $>$ Save menu item.   
6. Follow the prompts to replace the versions currently in the library and update the symbols in the   
   schematic.  

**Related Topics**  

Special Schematic Symbols  

# The Update From Library Function  

In SailWind Logic, when you add parts from the library to a schematic, a copy of the library content for the parts is written into the schematic. Over time, however, as updates are made to the library, the parts in the schematic can become out of sync with newer versions in the library. Use Update From Library to synchronize the parts in your design with the latest versions from the library.  

Use Update from Library (UFL) to:  

Create a report of any part differences between the current schematic and the library.  

• Update the schematic to reflect the current state of the library.  

You can compare or update the following categories of items:  

Part types CAE decals Pin decals Ground symbols Power symbols Off-page symbols  

You can compare or update:  

• All of any or all of these categories.   
• Selected part types, CAE decals, and pin decals. You cannot compare/update selected ground, power, or off-page symbols.  

# CAUTION:  

Since the only link between library and schematic content for an item is the item’s name, updating can have unforeseen and unintended consequences. When part types or gates are replaced globally in a schematic, they are replaced without regard to any local editing of the item; edited instances of parts or gates are replaced with the common instance from the library. The undesirable consequences of such changes could range from minor, like a repositioned label, to catastrophic, like deleted pins or disconnected nets.  

To prevent such unintended consequences, the update function always prompts you before updating any item in the schematic that has a newer timestamp than its counterpart in the library. To prepare yourself to respond to these prompts, before updating you should:  

1. Generate a comparison report (using the Generate comparison report button in the Update From Library dialog box).   
2. In the comparison report, locate the status messages identifying items whose timestamps are newer than in the library.   
3. Determine and write down what your response will be to each prompt when it occurs during the update.  

You may also want to update a copy of the schematic, and check/test the updated copy for unwanted changes or behavior.  

Undoing an Update   
Updating a Schematic From the Library   
Updating Selected Part Types From the Library   
Updating Selected CAE Decals From the Library   
Updating Selected Pin Decals From the Library   
The Compare/Update Process   
How to Read the Update Report  

# Undoing an Update  

The update process creates an undo checkpoint before it begins the update. If after the update you determine that you want to reinstate the design to its previous state you can revert to the previous checkpoint.  

You can undo any update (whether completed, canceled, or failed) to the last-saved checkpoint using the Edit $>$ Undo menu command.  

# Updating a Schematic From the Library  

Information in your library can be subject to changes and updates. To ensure that the content in your design is in agreement with the latest updated library content, you can update a schematic with new versions of parts from the library.  

You can update all items in any or all of these categories:  

• Part types CAE decals Pin decals • Ground symbols Power symbols • Off-page symbols  

**Procedure** 

1. Click the Tools $>$ Options menu item, then click the Design category.  

2. In the Options area, select or clear the “Allow overwriting of attribute values in design with blank values from library” check box as appropriate; click OK to close the Options dialog box.  

3. Click the File $>$ Library menu item, then click the Manage Lib. List button.  

4. Set the library list order that Update from Library will use when searching the libraries for items matching the items in the design. (See General Compare/Update Rules.) Click OK then close the Library Manager dialog box.  

5. Click the Tools $>$ Update from Library menu item.  

6. Modify the settings in the Update From Library Dialog Box as appropriate.  

7. Click OK.  

![](/images/aa40218c4fcbbecdb62b25321665257da3ba3e173563be4c7675c52e138a304e.jpg)  

Tip   
When the comparison or update operation is completed, the update report opens and a link to the report file displays in the Output Window.  

**Related Topics**  

The Compare/Update Process How to Read the Update Report Update From Library Dialog Box Updating Selected Part Types From the Library Updating Selected CAE Decals From the Library Updating Selected Pin Decals From the Library  

# Updating Selected Part Types From the Library  

As you make changes and updates to your library content, you may also need to selectively update parts in your design. You can select one or more parts and then update the part types of all parts having the same part type(s) to synchronize with the latest version in the library.  

**Restrictions and Limitations**  

All parts having the same part type as a selected part are updated, but attributes are updated only for the parts actually selected.  

**Procedure** 

1. Click the Tools $>$ Options menu item, then click the Design category.   
2. In the Options area, select or clear the “Allow overwriting of attribute values in design with blank values from library” check box as appropriate and click OK.  

Schematic Parts Updating Selected CAE Decals From the Library  

3. Click the File $>$ Library menu item, then click the Manage Lib. List button.  

4. Set the library list order that Update from Library will use when searching the libraries for items matching the items in the design. (See General Compare/Update Rules.) Click OK then close the Library Manager dialog box.  

5. In the Schematic Editor, with nothing selected, right-click and click the Select Parts (or Select Gates) popup menu item.  

6. Select the parts whose part types you want to compare/update.  

![](/images/cbc6e072d627d737cc9754552777b211ec521dea13f07f04b545ff944a287aff.jpg)  

!Tip  

If you want to update all but a few part types, select all the parts/gates, then in Step 8, clear the check boxes of the part types you do not want to update.  

7. Right-click and click the Update $>$ Part Type popup menu item.  

8. Modify the settings in the Update Selected Part Type From Library Dialog Box as appropriate.  

9. Click OK.  

**Results**  

When the comparison or update operation completes, the update report opens and a link to the report file displays in the Output Window.  

**Related Topics**  

The Compare/Update Process How to Read the Update Report Updating a Schematic From the Library Updating Selected CAE Decals From the Library Updating Selected Pin Decals From the Library  

# Updating Selected CAE Decals From the Library  

You can select one or more parts, and then update the CAE decals of all parts that use the same decal(s)  

**Restrictions and Limitations**  

This procedure updates the pin decal assignments in the CAE decals, but does not update the pin decals themselves. Use one of the procedures in Updating Selected Pin Decals From the Library to update the pin decals.  

As a corollary, if, for instance, you update CAE decal X to use PINB instead of PINA, it uses the version of PINB geometry currently in the schematic. If the schematic does not have a PINB, it installs from the library.  

**Procedure** 

1. Click the File $>$ Library menu item, then click the Manage Lib. List button  

2. Set the library list order that Update from Library uses when searching the libraries for items matching the items in the design. (See General Compare/Update Rules.) Click OK then close the Library Manager.  

3. In the Schematic Editor, with nothing selected, right-click and click the Select Parts (or Select Gates) menu item.  

4. Select the parts/gates whose CAE decals you want to compare/update.  

!Tip  

If you want to update all but a few CAE decals, select all the parts/gates, then in Step 6 clear the check boxes of the decals you do not want to update.  

5. Right-click and click the Update $>$ CAE Decal menu item.  

6. Modify the settings in the Update Selected CAE Decals From Library Dialog Box as appropriate.  

7. Click OK.  

**Results**  

When the comparison or update operation completes, the update report opens and a link to the report file displays in the Output Window.  

**Related Topics**  

The Compare/Update Process   
How to Read the Update Report   
Update Selected CAE Decals From Library Dialog Box   
Updating a Schematic From the Library   
Updating Selected Part Types From the Library   
Updating Selected Pin Decals From the Library  

# Updating Selected Pin Decals From the Library  

You can update selected pin decals from the library using the Update from Library dialog box or directly from within the schematic editor.  

Updating Selected Pin Decals Using the Update From Library Dialog Box Updating Selected Pin Decals Using the Schematic Editor  

# Updating Selected Pin Decals Using the Update From Library Dialog Box  

As you make changes and updates to the content in your library, you may need to synchronize pin decals in your design with the updated library content. You can use the Update From Library dialog box to update all instances of one or more selected pin decal(s).  

**Procedure** 

1. Click the File $>$ Library menu item, then click the Manage Lib. List button   
2. Set the library list order that Update from Library will use when searching the libraries for items matching the items in the design. (See General Compare/Update Rules.) Click OK then close the Library Manager dialog box.   
3. Click the Tools $>$ Update from Library menu item.   
4. Select the Pin Decals check box, and select the decals you want to compare/update.   
5. Click OK.  

**Results**  

When the comparison or update operation completes, the update report opens and a link to the report file displays in the Output Window.  

# Updating Selected Pin Decals Using the Schematic Editor  

As you make changes to the content in your library, you may need to refresh your design content to reflect those updates. You can use the Update Selected Pin Decals from Library dialog box to select one or more pins, and update all instances of the pin decal(s) used by the selected pin(s).  

**Procedure** 

1. Click the File $>$ Library menu item, then click the Manage Lib. List button.   
2. Set the library list order that Update from Library will use when searching the libraries for items matching the items in the design. (See General Compare/Update Rules.) Click OK then close the Library Manager dialog box.   
3. In the Schematic Editor, with nothing selected, right-click and click the Select Pins popup menu item.   
4. Select the pins you want to compare/update.  

0 Tip If you want to update all but a few pin decals, select all the parts/gates, then in Step 6 clear the check boxes of the decals you do not want to update.  

5. Right-click and click the Update $>$ Pin Decal menu item.  

6. Modify the settings in the Update Selected Pin Decals From Library Dialog Box as appropriate.  

7. Click OK.  

**Results**  

When the comparison or update operation completes, the update report opens and a link to the report file displays in the Output Window.  

**Related Topics**  

The Compare/Update Process   
How to Read the Update Report   
Update Selected Pin Decals From Library Dialog Box   
Updating a Schematic From the Library   
Updating Selected Part Types From the Library   
Updating Selected CAE Decals From the Library  

# The Compare/Update Process  

The update process begins with a comparison of the schematic content with the library content. When schematic content is found to be different from the library content, the schematic content is updated according to the options set in the Update From Library dialog box, and the results documented in the report file. The compare process is the same, except that the schematic is not updated.  

# General Compare/Update Rules  

There are a number of rules that govern the compare/update process.  

In comparing and updating, the following general rules apply for all items:  

• Matching items — For each item in the schematic, all available libraries are searched to find a matching named entry, and the first matching entry found is used. If no match is found, comparison of the item is skipped, and a “not found” entry is made in the report file.  

![](/images/5ad6d5b6018fba62e24258cb719e332b8ea32498ee6e852e5f2e1acf589556dd.jpg)  

Tip   
Libraries are searched in the order shown in the Library List dialog box. You can use this dialog box to change the search order.  

• Timestamps — Each item in the schematic and library has a timestamp. Schematics of PADS versions prior to 2005 SPac2 do not have timestamps. A comparison of the timestamps determines what is compared/updated, as follows:  

◦ Timestamp in schematic is older — If the timestamp in the schematic is older than the timestamp in the library, the item in the schematic is always compared/updated.  

Timestamps are the same — If the timestamps in the library and schematic are the same, comparison/update of the item depends on the setting of the Include items with identical time stamp check box in the Update From Library Dialog Box. If this check box is cleared, no comparison/update is made; if the check box is selected, all items are compared/updated regardless of timestamps.  

Timestamp in schematic is newer — If the timestamp in the schematic is newer than the timestamp in the library:  

• When you are comparing, a status message is written to the report. • When you are updating, a status message is written to the update report, and you are prompted to choose whether to update the schematic or not.  

• What is updated — When an item is updated, the content from the library replaces the entire content of the item in the schematic.  

# Skipped Updates  

There are 3 situations in which the update of an item is skipped.  

These situations are:  

When an item in the design is newer than the equivalent item in the library, and you reply No to the “<item> in the schematic has a more recent time stamp than in the library. OK to overwrite the version in the schematic?” prompt.   
• When a newer item in the library has fewer pins than the equivalent older item in the design.   
• When the number of GND, POWER or OFF symbols in the library is fewer than the number of available symbols in the design.  

# Older Schematics  

Schematics of PADS versions prior to 2005 SPac2 do not have timestamps. When one of these is opened, the timestamps on all part types, decals, pin decals, and off-page, power & ground symbols are set to zero. To determine if the content of the part types and decals in the schematic is in sync with the library, compare the schematic and library with the Hide identical results check box selected.  

# What is Compared  

Many design objects are examined during the compare process.  

The following table lists the content compared and reported for each item selected for comparison or update.  

Table 25. Compared and Reported Part Structures   


<table><tr><td> Item</td><td>Item Component</td><td>What is Compared & Reported</td></tr><tr><td colspan="2">Timestamps</td><td>See“General Compare/Update Rules" on page 203.</td></tr><tr><td colspan="2">Part Type</td><td>Logic Family, Number of gates, Number of connector pins, Number of Signal pins, List of attribute names</td></tr><tr><td></td><td>For each gate:</td><td>Number of CAE Decals, CAE Decal names, Number of electrical pins on gate, Gate swap class.</td></tr><tr><td></td><td>For each gate pin:</td><td>Pin number (alphanumeric if defined), Pin name, Pin type, Pin swap class</td></tr><tr><td></td><td>For each signal pin:</td><td>Pin Number (alphanumeric if defined), Net name</td></tr><tr><td></td><td>For each attribute:</td><td>Value string Note: There can be attributes in the library that are just placeholders, with blank values that must be set for each individual part in the schematic. Any attribute in the library with a blank. value is considered to be such a placeholder, and updates of corresponding attributes in the schematic is controlled by the“Allow overwriting of attribute values in design with blank values from library" check box in the Options Dialog Box, Design Category.</td></tr><tr><td colspan="2">PCB Decal assignment</td><td>The part's assigned PCB Decal name is on the list of PCB Decal alternates for the Library part type. If it is not, a warning is written to the report, but the decal</td></tr><tr><td colspan="3">PCB Decal pin count</td></tr><tr><td></td><td>For connectors: For normal parts:</td><td>Number of pins in the PCB Decal assigned to each connector part is equal to the number of connector pins defined for the part type. Number of pins in the PCB Decal assigned to each normal part is</td></tr><tr><td></td><td></td><td>equal to or greater than the highest electrical pin number used in the gates defined for the Library part type. Restriction: Pin counts cannot be updated in the schematic. Pin count differences are flagged as warnings in the update report.</td></tr><tr><td colspan="3">CAE Decals</td></tr><tr><td rowspan="2"></td><td rowspan="2">Gate Decal details:</td><td>Number of attribute labels, attribute label name, number of text, number of terminals.</td></tr><tr><td>Restrictions: · CAE Decal graphics are not compared.</td></tr><tr><td></td><td>Terminal details:</td><td>· Details of text items are not compared. Pin decal name assigned to each terminal.</td></tr><tr><td></td><td></td><td>Restriction: If terminal pin counts differ, the decal cannot be updated in the schematic separately from the part types.</td></tr></table>  

Table 25. Compared and Reported Part Structures (continued)   


<table><tr><td> Item</td><td>Item Component</td><td>What is Compared & Reported</td></tr><tr><td rowspan="3">Pin Decals</td><td rowspan="3"></td><td>Pin Decal name.</td></tr><tr><td>Update notes: · Because default pin name and pin number label locations are "hard-wired" in the CAE decal when it is created, the locations of</td></tr><tr><td>pin names and numbers in the schematic are unaffected when a Pin decal is updated. · Pin decals do provide a default location for net names on the schematic, but the actual used net name locations are stored separately and therefore net name locations are not affected by an update.</td></tr><tr><td>Power & Ground Symbols</td><td></td><td>Symbol name, type, Signal Pin name</td></tr><tr><td>Off-Page Symbols</td><td></td><td>Symbol name, type</td></tr></table>  

# How to Read the Update Report  

Every time you update a design from the library or generate a comparison report, Update from Library writes the results of the operation to a new UpdateReport.txt file in C:\SailWind Projects. You can use a text editor to open and review the content of this report and verify that the design objects are the intended versions.  

The Update Report gives you information about the items you selected for comparison or update, such as:  

Whether the timestamp of an item in the design is older, newer, or the same as the item’s timestamp in the library.   
Whether the content of an item in the design is the same as or different from the item’s content in the library.  

The report consists of 4 sections:  

• Report header information — General information about the report itself. Example:  

1 \*PAD5 LOQiC 9.2\* UPDATE FROM LIBRARY REPORT   
2 12:10:48 05/14/10 DEM0.5CH   
3 / C:\PADs Projects\UpdateFroml ibrary_Logic_report.txt  

• Report Options — A list of options selected for this operation in the Update from Library dialog box. Example:  

12 REPORT OPTIONS   
13 1   
14   
15 This report was run with the following options:   
16 Update design from library   
17 Include items with identical time stamp   
18 Summary and Details   
19 Part types and attributes   
20 Preserve design attributes not found in library   
21 Add new attributes not found in design   
22 Update common attributes   
23 CAE Decals   
24 Pin Decals:   
25 PIN   
26 PINB   
27 PCLK   
28 PCLK8   
29 PINIEB   
30 PINORE   
3f PINSHORT   
32 PINVRTS   
33 Off-Page symbols   
34 Ground symbols   
35 1. Power symbols  

Report Summary — A tabular listing of compared part types, CAE decals, off-page symbols, ground symbols, and power symbols, showing the comparison results and update status for the package as a whole. Example:  

37   
38 REPORT SUMMARY   
39 835   
40   
41 Compare status:   
42 Compared - 137   
43 Differences- 72   
44 Warnings - 1   
45 Errors- 0   
46 Skipped- 1   
47   
48 Update status:   
49 Updated - 137   
50 Warnings - 1   
51 Failed - 1   
52 5kipped - 1   
53   
54   
55 Compared Part Types   
56   
57   
58 1 Design update   
59 Part Type Timestamp Content Found in Library Status See Line   
60   
61 7404 Older than library Different ti UPDATED 307   
62 7402 Older than library Different ti UPDATED 668   
5 7474 Older than library Different ti UPDATED 861   
64 7432 Older than library Different ti UPDATED 996   
65 COW\26P\ED Older than library Different mi5c UPDATED 1145   
66 1 XTAL1 Older than library Different mi5c UPDATED 1652  

• Report Details — Complete comparison and update details for all compared packages. Example:  

299   
300 REPORT DETAIL5   
301   
302   
303   
304 -= Part Types =-   
305   
306   
307 7404   
308   
309 Part Type Timestamp: Older than Tibrary - (   
310 Library: ti   
311 Detaiis:   
312 Logic Family: TTI 5ame as library   
313 Gate Count:6 Same as library   
314 Pin Count:   
315 Connector: 12 5ame as library   
316 5ignal:2 Same as library   
317 Gate 1 Details:   
318 Logic Decal Details:   
319 Count:4 Same as library   
320 1.Name: INV Same as library   
321 2.Name: INVL Same as library   
322 3.Name: INVDM Same as library   
323 4.Name: INVDML Same as library   
324 Gate 5wap Class: 1 Same as library   
325 Gate Pin Count: 2 Same as library   
326 Gate Pins Details:   
327 1.pin:   
328 Wumber: 1 Same as library   
329 Name: Not assigned Same as library   
330 Pin Type: Load Same as Tibrary   
311 Swap Class: 0 Same as library   
332 #2.Pin   
333 Number : ？ Same as library   
334 Name : Not assigned Same as library   
335 Pin Type: Source Same as library   
336 ！ Swap Class: 0 Same as library  

Table 26 lists and describes the messages returned for compared/updated items in the Update Report.  

Table 26. Update Report Messages   


<table><tr><td>Message</td><td>Reption</td><td>Refers to:</td><td>Means</td></tr><tr><td>Cannot get CAE DECAL from Library!!!</td><td>Details</td><td>CAE decal</td><td>CAE decal exists in design but not in library.</td></tr></table>  

Table 26. Update Report Messages (continued)   


<table><tr><td>Message</td><td>Reptort</td><td> Refers to:</td><td> Means</td></tr><tr><td>Cannot get GATE from Library!!!</td><td>Details</td><td>Gate</td><td>Gate exists in design but not in library.</td></tr><tr><td>Cannot get GATE from Library - Comparison Skipped</td><td>Details</td><td>Gate</td><td>Gate exists in design but not in library.</td></tr><tr><td>Cannot get PACKAGE from Library!!!</td><td>Details</td><td>Package</td><td>Package exists in design but not in library.</td></tr><tr><td>Cannot get PIN DECAL from Library!!!</td><td>Details</td><td>Pin decal</td><td>Pin decal exists in design but not in library.</td></tr><tr><td>CANCELLED</td><td> Summary</td><td>Item update</td><td>Operation was canceled by user.</td></tr><tr><td>COMPARE CANCELLED</td><td>Summary & Details</td><td>Compare operation</td><td>Operation was canceled by user.</td></tr><tr><td>COMPARE ERROR</td><td>Details</td><td>Compare operation</td><td>No items selected or item(s) unavailable.</td></tr><tr><td>COMPARE SKIPPED</td><td>Details</td><td>Compare operation</td><td>Cannot compare because CAE decal terminal count differs in design and library.</td></tr><tr><td>COMPARE STOPPED!</td><td>Details</td><td>Compare operation</td><td>Operation was canceled by user.</td></tr><tr><td>Compared items match</td><td> Summary</td><td>Item content</td><td>All compared item content is the same in the design and the library. The following items are not compared: · CAE Decal graphics · Details of CAE Decal</td></tr><tr><td>CONTENT UPDATED</td><td>Details</td><td>Item update status</td><td>text items Content in the design updated with content from library.</td></tr><tr><td>Decal Count Mismatch</td><td>Details</td><td>CAE decal</td><td>CAE decal terminal count in design differs from count in library.</td></tr><tr><td>Different</td><td>Summary & Details</td><td>Item content</td><td>Item content in design differs from content in library.</td></tr></table>  

Table 26. Update Report Messages (continued)   


<table><tr><td>Message</td><td>Report Section</td><td>Refers to:</td><td> Means</td></tr><tr><td>Different timestamp</td><td>Summary</td><td>Pin Decal timestamp</td><td>Timestamps in design and library differ.</td></tr><tr><td>FAILED</td><td> Summary</td><td>Item update status</td><td>Update has failed due to an unspecified error.</td></tr><tr><td>In library: Not in design</td><td>Details</td><td>Item status</td><td>Item in library not found in design.</td></tr><tr><td>Newer than library</td><td>Summary & Details</td><td>Timestamp in design</td><td>Timestamp in design newer than in library.</td></tr><tr><td>No CAE Decal found!!!</td><td>Details</td><td>CAE decal</td><td>CAE Decals check box selected in dialog box but no CAE decal found in design.</td></tr><tr><td>No PIN Decal found or selected!!!</td><td>Details</td><td>Pin decal</td><td>Either: · Pin decal selected in. dialog box not found in design, or · Pin decals check box selected but no pins selected.</td></tr><tr><td>Not assigned</td><td>Details</td><td>Gate pin</td><td>Gate pin assigned in design is not assigned in library.</td></tr><tr><td>Not assigned in library part</td><td>Details</td><td>Compared item</td><td>The PCB Decal assigned to the part in the design is not in the set of decals assigned to the part in the library.</td></tr><tr><td>Not in design</td><td> Summary</td><td>Off-page, PWR and GND symbols</td><td>The symbol exists in the library, but is not used in the design.</td></tr><tr><td> Not in library</td><td>Details</td><td>Compared item</td><td>Item in design not found in library.</td></tr><tr><td>Older than library</td><td>Summary & Details</td><td>Timestamp in design</td><td>Timestamp in design older than in library.</td></tr><tr><td>Operation canceled by USER!!!</td><td>Details</td><td>Update or Compare operation</td><td>Operation was canceled by user.</td></tr><tr><td>PERFORMED UNDO OPERATION</td><td>Details</td><td>Update or Compare operation</td><td>Operation canceled by user.</td></tr></table>  

Table 26. Update Report Messages (continued)   


<table><tr><td>Message</td><td>Report Section</td><td>Refers to:</td><td>Means</td></tr><tr><td>Same as library</td><td>Summary & Details</td><td>Timestamp in design Item content in design</td><td>Timestamps in design and library are equal. Item content is the same in design and library.</td></tr><tr><td>SKIPPED</td><td>Summary</td><td>Item update</td><td>User has replied “No" to the “<item> in the schematic has a more recent time stamp than in the library. OK to overwrite the version in the schematic?" prompt.</td></tr><tr><td>STOPPED</td><td>Summary</td><td>Item update</td><td>Operation canceled by user.</td></tr><tr><td>UPDATE CANCELLED</td><td>Details</td><td>Item update</td><td>Operation was canceled by user.</td></tr><tr><td>UPDATE FAILED</td><td>Details</td><td>Item update</td><td>An error occurred in the update process and the update failed.</td></tr><tr><td>UPDATE MESSAGE</td><td>Details</td><td>Item update</td><td>Explains cause of an Update failure.</td></tr><tr><td>UPDATE SKIPPED</td><td>Details</td><td>Item update</td><td>User has replied “No” to the “<item> in the schematic has a more recent time stamp than in the library. OK to overwrite the version in the schematic?" prompt.</td></tr><tr><td>UPDATE STOPPED!</td><td>Details</td><td>Item update</td><td>Operation canceled by user.</td></tr><tr><td>WARNING</td><td>Details</td><td>PCB Decal</td><td>PCB Decal in the library has fewer pins than in the design.</td></tr></table>

Related Topics  

**Related Topics**  

The Update From Library Function The Compare/Update Process  

# Deleting a Part  

When deleting a part that is selected in object mode, you can choose to delete the part only, or the part and its connections.  

**Procedure** 

1. Select a part.   
2. If you want to keep connections attached to the part, right-click and click the Preserve Connections popup menu item to enable it. The Preserve Connections option is enabled by default.  

![](/images/c1df724a5ce3c2e2fd721f9bb2669a83f9a2dcc475681b1f1fc678de50fcd71b.jpg)  

Tip Preserve Connections is enabled when a check mark appears next to it in the menu.  

3. Right-click and click the Delete popup menu item.  

The software leaves the connections at their original locations.  

# Deleting a Part and Its Connections  

If a design no longer requires a part, and you are not going to replace the part with a similar one (and therefore you do not need to preserve its connections), you can delete the part and its connections.  

**Procedure** 

1. Select a part.   
2. If you want to remove connections attached to the part, right-click and click the Preserve Connections popup menu item to disable it. The Preserve Connections option is enabled by default.  

0 Tip Preserve Connections is disabled when a check mark does not appear next to it in the menu.  

3. Right-click and click the Delete popup menu item.  

The software deletes the part and its connections.  

**Related Topics**  

Object Select Mode (Select Object First) Adding Off-Page References Working With Floating Connections  

# Cut, Copy, and Paste  

In a manner similar to other standard applications, you can cut, copy and paste objects in your design.  

• Use the Edit menu items or the Ctr $+{\sf X}$ , Ctrl $+\mathsf{C}$ , or Ctrl+P shortcuts.   
• Connections that extend outside a selection are assigned off-page symbols at the break point.   
• SailWind Logic only maintains one cut or copy in the paste buffer.   
• You can paste into a new design.  

# Copy as Bitmap  

The Copy as Bitmap command lets you define a rectangular area to copy graphics information to the paste buffer as a bitmap image. Once copied, you can, for example switch to Microsoft Word and use the Home $>$ Paste menu item to insert the bitmap into a document.  

**Procedure** 

1. Click the Edit $>$ Copy as Bitmap menu item.   
2. Drag the cursor over the area to copy. All items in the rectangle including the background, dot grid, color, etc., are copied.   
3. Open the application in which to place the bitmap and use the Paste command to place the image.  

# Creation of Groups  

A group is a collection of objects on the schematic. By default, connections that extend outside the group are clipped so they stop at the boundary used to define the group. Once you select a group, you can move it, copy it to the paste buffer, delete it, duplicate it, or save it to a file for use in another design.  

![](/images/140e1ee4b7b4ea3a378ca798da161998b7b9d8ac99f42e84b3af1f490a44f487.jpg)  

Tip A group differs from a combination, which consists only of 2D lines or 2D lines and text.  

See also Combining 2D Lines and Text.  

Creating a Group Setting the Origin of Groups  

# Creating a Group  

To perform an operation on multiple objects simultaneously, create a group and then move it, copy it to the paste buffer, delete it, duplicate it, or save it to a file for use in another design.  

**Restrictions and Limitations**  

• Certain group commands are available only if the group consists of mixed items. For example, the “Preserve by Boundary” popup menu item is unavailable if the group consists of components only.  

**Procedure** 

1. Set the selection filter to the objects you want to select. See also Using the Selection Filter.   
2. Area select the objects in the group. As an alternative, you can use Ctrl+click to select all objects to include in the group. The software highlights the included objects.   
3. To preserve connections that extend outside the group boundary, right-click and click the Preserve by Boundary popup menu item.   
4. To preserve single pin nets that remain after you delete a part or bus, right-click and click the Preserve Connections popup menu item.   
5. As needed, Ctr $^+$ click objects in the group to remove them, or Ctrl $^+$ click objects outside the group to add them to the group.  

The software highlights the included objects.  

# Setting the Origin of Groups  

When you create a group, the software creates an origin automatically. The software uses this origin when moving or placing groups. You may want to change the origin when it is optimal to have the origin at a specific location.  

**Restrictions and Limitations**  

You must enable the Preserve by Boundary option and the boundary must be visible to set the origin.   
When the boundary is not visible, the group rotates around the center of the selection.  

**Procedure** 

1. Select the group.   
2. Right-click and click the Set Origin popup menu item. A bullseye attaches to the pointer.   
3. Move the cursor to the new origin and click to set it.  

**Related Topics**  

Management of Groups  

# Group Anchor Points  

When duplicating or moving a group, SailWind Logic places the anchor point of the group at a pre-defined location.  

Keep the following anchor point criteria in mind:  

• If you have enabled the “Preserve by boundary” feature, SailWind Logic anchors to a point on the design grid closest to the group’s origin.  

![](/images/d32e54e8cb1ae658180598cc59ef9cd0d715a4453d17c44f7099b39a8ba0c58c.jpg)  
Figure 3. Anchor Point with “Preserve by Boundary”  

• If you have not enabled the “Preserve by boundary” feature, SailWind Logic anchors to either a group object that lies on the design grid or—if no part of the group is on the design grid—it anchors to a group object that is closest to the origin.  

![](/images/d18b456e202eaffd72640cfcc7c07bf84e7b15e5629b5f8b0a85d951d73288b4.jpg)  
Figure 4. Anchor Point with no “Preserve by Boundary”  

# Management of Groups  

Using a group, you can perform an operation on its contents as a single entity. Once you create a group, you can save it, delete it, move it, or reuse it.  

Duplicating an Existing Group   
Moving Groups   
Deleting Groups   
Saving Groups   
Pasting Groups From a File   
Automatic Connection When Pasting   
Rotate or Mirror a Group  

# Duplicating an Existing Group  

You can duplicate all of the items in a group that already exist on a schematic. When you duplicate a group of objects, reference designator names are assigned automatically.  

**Procedure** 

1. Select a group, right-click and click the Duplicate popup menu item.  

![](/images/db6566adb130d750a3306570f4b6bb3bc287ea54b34bbdcc66da1e657b076c92.jpg)  

Note:   
The anchor point of the duplicate group depends on certain conditions. For more information, see Group Anchor Points.  

2. Move the cursor to the location for the duplicate, and click to place it.  

3. Repeat the above step to create additional copies.  

0 Tip You can set SailWind Logic to display only the group’s outline during copy operations.  

See also Creation of Groups.  

# Moving Groups  

Using the Move command, you can move a group to any location on the sheet.  

**Procedure** 

1. Select a group, right-click and click the Move popup menu item.  

![](/images/79e9d76b8a8260554e5a2a6a64ac32e0a2cb02646c3dccebb62a0f2f752fe7e3.jpg)  

!Note:  

As you move the group, its anchor point depends on certain conditions. For more information, see Group Anchor Points.  

2. Move the cursor to the new group location and click to place it.  

![](/images/59121a97134947c4b2cf363ab1531285fbccb2529e85187f7daf2eb6688af2a7.jpg)  

Tip You can set SailWind Logic to display only the group’s outline during move operations.  

See also Creation of Groups.  

# Deleting Groups  

When deleting a group, you can choose to delete or retain the connections that are outside the group boundary.  

**Procedure** 

1. Select a group, right-click and click the Delete popup menu item.  

2. To preserve connections that extend outside the group boundary, right-click and click the Preserve by Boundary popup menu item.  

!Tip  

When preserving connections, note the following:  

• Preserve by Boundary must be checked to use this capability, otherwise, the feature is disabled.   
• When you preserve connections outside the group boundary, the connections are automatically assigned off-page symbols upon deletion. Unnamed connections are uniquely named with a $"\$\$\$\$\gg$ prefix.  

3. To preserve single pin nets that remain after you delete a part or bus, right-click and click the Preserve Connections popup menu option.  

See also Detach, Working With Floating Connections.  

# Saving Groups  

You can save the contents of a group for use on other schematic sheets or a different design. Saved groups are stored in the \SailWind Projects folder with a .grp extension.  

**Restrictions and Limitations**  

• The group must consist of mixed items. The “Save to File” command is not available if you select only components or other objects.  

**Procedure** 

1. Select a group, right-click and click the Save to File popup menu item.   
2. In the File Name area, type a name.   
3. Click Save.  

# Pasting Groups From a File  

You can save a group to a file so that you can use it again in the current or future designs. Use Paste from File to insert a group that was previously saved to a file.  

When you paste a group into a sheet:  

• Named nets retain their name, and unnamed nets are assigned default signal names.   
• All parts are named with the next available reference designator names.  

![](/images/6301a52bf2c7ed02e9d711b2aae1a14fa9a230287a36a955cc67c6155acfba7e.jpg)  

!Tip  

To control renaming of reference designators, use the “Preserve Reference Designators on Paste option” check box in the Options dialog box, Design category.  

**Procedure** 

1. Click the Edit $>$ Paste from File menu item.  

2. In the Load Group File dialog box, select the group to paste.  

3. Click Open. The group attaches to the cursor.  

4. Move the pointer to the location for the group, and click to place it.  

!Tip  

If the design contains parts with the same reference designation as those in the group, a report generates.  

See also Preserving Reference Designators.  

# Automatic Connection When Pasting  

When pasting a group from a file into your design, unconnected pins, unterminated wires, or bus segments in a group can connect automatically.  

• Unconnected pins connect automatically with unterminated wire ends or unconnected pins. • Unterminated wire ends connect automatically to bus segments only if the unterminated wire is a named subnet of the bus.  

# Rotate or Mirror a Group  

You can rotate or mirror a group while the group is selected. You can also rotate or mirror a group during a move.  

**Procedure** 

1. Select a group and right-click.   
2. Click the Rotate 90, X Mirror, or Y Mirror popup menu item.  

**Restriction:**  

The group must consist of mixed items. The commands are not available if only components are selected.  

**Related Topics**  

Creation of Groups  

# Attributes Overview  

Attributes enable you to associate information with a schematic symbol. Attributes are made of two parts: an attribute name, and its corresponding value. For example, you can create an attribute named Part Description and assign its value as Hex Inverter.  

You can create an attribute that is assigned to every part in the library, every part in the open design, a part type, or to only one part in the design.  

• To add an attribute to all parts in a library, create the attribute in the Manage Library Attributes dialog box. See also Managing Library Attributes. To add an attribute to every part in the open design, create the attribute in the Managing Schematic Attributes dialog box. See also Manage Attributes in a Schematic.   
• To add an attribute to a specific part, create the attribute using the Attributes tab while editing the part. See also Managing Attributes. To add an attribute to a part on the schematic without updating the part type, use the Part Attributes dialog box.  

See also Modifying Part Attributes and Resistor Values Defined on Parts.  

To display attributes in the schematic after creating them, use the visibility controls. See also Controlling Text Visibility for a Part.   
• To create placeholders in CAE Decals so that attributes are placed in a predefined locations, use attribute labels. See also Attribute Labels.  

# Manage Attributes in a Schematic  

Use the Manage Schematic Attributes dialog box to manage attributes at the schematic level. You can create a new attribute and automatically assign it to every part in your design. You can also rename an attribute in, or delete an attribute from, the schematic. All parts are automatically updated.  

See also Attributes Overview.  

Creating Attributes Renaming Attributes Deleting Attributes  

# Creating Attributes  

You can create a new attribute and automatically assign it to every part in a design.  

**Procedure** 

1. Click the Edit $>$ Attribute Manager menu item.  

2. In the Manage Schematic Attributes dialog box, click Add Attr.  

3. In the Add New Attribute dialog box do one of the following:  

Type a name for the attribute in the Attribute Name text box. • Click Browse Lib Attr to select an attribute already defined in the library. Select an attribute name from this dialog box and then click OK.  

4. Type a value for the attribute in the Attribute Value text box.  

5. Click OK to close the Add New Attribute dialog box.  

6. Click Close to close the Manage Schematic Attributes dialog box.  

# Renaming Attributes  

You can rename an existing attribute and apply the change to each part in the design.  

**Procedure** 

1. Click the Edit $>$ Attribute Manager menu item.   
2. In the Manage Schematic Attributes dialog box, select one or more attributes in the Attributes in   
   Schematic list.   
3. Click Add. The attributes are added to the Attributes Selected for Rename list.   
4. Select the attribute in the New Name column and click Edit New Name.   
5. In the Attribute Name text box, do one of the following:  

• Type a name for the attribute   
• Click Browse Lib Attr to select an attribute already defined in the library. Select an attribute name from this dialog box, and then click OK.  

6. Click Rename Attrs to rename the attribute and remove it from the Attributes Selected for Rename list box.  

7. Click Close.  

0 Tip Click Remove or Remove All to place the selected attributes back into the Attributes in Schematic list and keep the current name.  

# Deleting Attributes  

You can delete an attribute from all parts in the design:  

**Procedure** 

1. Click the Edit $>$ Attribute Manager menu item.   
2. Select one or more attributes in the Attributes in Schematic list.   
3. Click Delete Attrs then click Yes at the prompt.   
4. Click Close.  

# Resistor Values Defined on Parts  

Discrete parts such as resistors and capacitors are created with Value and Tolerance attributes. The value for these attributes is not defined in the part symbol, but is set when the part is added to the drawing.  

Use the Part Attributes Dialog Box on page 283 to modify these values.  

