# **Chapter 8 Special Schematic Symbols**

Special Symbols in SailWind Logic include power symbols, ground symbols, and off-page reference

symbols. SailWind Logic enables only one part definition in the library for Special Symbols. For this 

reason, the options for these types are grayed out and unavailable when you are in the Part Editor and 

you select **File menu > New**. You can only modify the existing symbols or add new symbols to the part

definition.

Special Symbol Naming Conventions

Assigning Alternative Symbols for the Ground Part

Assigning Alternative Symbols for the Off-Page Part

Assigning Alternative Symbols for the Power Part

Creating New Special Symbols

Creating New Special Symbols From Existing Symbols

Updating Special Symbol Mappings

Management of Special Symbols in the Library

## **Special Symbol Naming Conventions**

The special symbols in the SailWind Logic library use specific names or a unique naming prefix. This 

topic contains tables that provide definitions that can help you to locate a special symbol in the library.

**Table 20. Off-Page Reference Symbols**

**Symbol** 

**Description**

REFIN 

Off -page reference for left side

REFOUT 

Off -page reference for right side

**Table 21. Power Symbols**

**Symbol** 

**Description**

\+ 

+5 volt and +12 volt symbols, arrow pointing up

\- 

-5 volt and 12 volt symbols, arrow pointing down

BUBBLE 

+5 volt symbol with a circle

Y 

+5 volt symbol with a ‘Y’ shape

**Table 22. Ground Symbols**

**Symbol** 

**Description**

GND 

Standard ground

SailWind Logic Guide 

167Special Schematic Symbols

Assigning Alternative Symbols for the Ground Part

**Table 22. Ground Symbols (continued)**

**Symbol** 

**Description**

AGND 

Analog ground

CHGND 

Chassis ground

## **Assigning Alternative Symbols for the Ground Part**



If your design requires the use of multiple ground symbols, use the Assign Alternatives for Ground Part 

dialog box to assign ground symbols.

**Procedure**

1. In the Part Editor, on the toolbar, click the **Open** button.
2. In the Select Type of Editing Item Dialog Box, click Ground and then click **OK**.

The current symbols are displayed.

3. Click the **Edit Electrical** button.
4. Click **Add**. This creates a new entry for the symbol.

**Tip**

To add a new ground symbol, follow the procedure in Creating New Special Symbols.

5. In the Special Symbol column, click the button to the right of the newly created text box.

The “Browse for Special Symbols dialog box” on page 487 appears.

6. To filter the symbols, type a wildcard or expression on page 105 in the Items box, and click **Apply**.
7. Select a symbol decal.
8. Click **OK**.
9. In the Assign Alternatives for Ground Part Dialog Box, select the text box under Pin Type.
10. Click **Edit**.
11. Select a pin type from the dropdown list box.

This is normally set to Ground.

12. Select and edit the text box for the Signal Name.
13. Click **OK**.

168 

SailWind Logic GuideSpecial Schematic Symbols

Assigning Alternative Symbols for the Off-Page Part

## **Assigning Alternative Symbols for the Off-Page Part**

If your design requires the use of multiple different off-page symbols, use the Assign Alternatives for Off

Page Part dialog box to assign additional off-page reference symbols.

**Note:**

See “Special Schematic Symbols” on page 167 for additional information on the creation and 

use of special schematic symbols.

**Procedure**

1. In the Part Editor, on the toolbar, click the **Open** button.
2. In the Select Type of Editing Item Dialog Box click Off-page and then click **OK**.

The current symbols are displayed.

3. Click the **Edit Electrical** button.
4. Click **Add**.

This creates a new entry for the symbol.

**Tip**

To add a new off-page reference symbol, follow the procedure in Creating New Special 

Symbols.

5. In the Special Symbol column, click the button to the right of the newly created text box.

The Browse for Special Symbol dialog box on page 487 appears.

6. To filter the symbols, type a wildcard or expression on page 105 in the Items box, and click **Apply**.
7. Select a symbol decal.
8. Click **OK**.
9. In the Assign Alternatives for Off-Page Part Dialog Box, select the text box under Pin Type.
10. Click **Edit**.
11. Select a pin type from the dropdown list box.

**Tip**

For left side off-page references, select Source, for right side, select Load.

12. Click **OK**.

SailWind Logic Guide 

169Special Schematic Symbols

Assigning Alternative Symbols for the Power Part

## **Assigning Alternative Symbols for the Power** Part

If your design requires the use of multiple different power symbols, use the Assign Alternatives for Power

Part dialog box to assign additional power symbols.

**Procedure**

1. In the Part Editor, on the toolbar, click the **Open** button.
2. In the Select Type of Editing Item Dialog Box, click Power, and then click **OK**.

The current symbols appear.

3. Click the **Edit Electrical** button.
4. Click **Add**.

This creates a new entry for the symbol.

**Tip**

To add a new power symbol, follow the procedure in Creating New Special Symbols.

5. In the Special Symbol column, click the button to the right of the newly created text box.

The “Browse for Special Symbols dialog box” on page 487 appears.

6. To filter the symbols, type a wildcard or expression on page 105 in the Items box, and click **Apply**.
7. Select a symbol decal.
8. Click **OK**.
9. In the Assign Alternatives for Power Part Dialog Box, select the text box under Pin Type.
10. Click **Edit**.
11. Select a pin type from the dropdown list box.

This is normally set to Power.

12. Select and edit the text box for the Signal Name.
13. Click **OK**.

## **Creating New Special Symbols**

Special symbols in SailWind Logic include power symbols, ground symbols, and off-page reference

symbols. SailWind Logic enables only one part definition in the library for special symbols. For this 

reason, the options for these types are unavailable when you are in the Part Editor and you select the 

**File > New** menu item.

See also Creating New Special Symbols From Existing Symbols.

170 

SailWind Logic GuideSpecial Schematic Symbols

Creating New Special Symbols

**Procedure**

1. In the Part Editor, click the **Open** button.
2. In the Select Type of Editing Item Dialog Box, select the type of symbol to add: Off-page, Power, or

Ground.

3. Click **OK**.

The currently defined symbols display for the chosen type.

4. Click the **Edit > Part Type Editor** menu item, or on the toolbar, click the **Edit Electrical** button.

The Assign Alternatives dialog box for the type of Special Symbol appears.

Refer to the following topics for additional information:

• **Off-page symbols** — Refer to Assigning Alternative Symbols for the Off-Page Part.

• **Power symbols** — Refer to Assigning Alternative Symbols for the Power Part.

• **Ground symbols** — Refer to Assigning Alternative Symbols for the Ground Part.

5. Click **Add**. The software creates a new entry.
6. Type a name for the new symbol and enter the appropriate information.

**Tip**

For left side off-page references, select Source, for right side, select Load.

7. Click **OK**.
8. Click the **Edit > CAE Decal Editor** menu item, or on the toolbar, click the **CAE Decal Editor** 

button.

The Select Pin Decal Dialog Box appears.

9. Select the new symbol name and when prompted, click **OK** to create the new symbol.
10. Click the **Decal Editing Toolbar** button, click the **Create 2D Line** button, and then right-click and 

use the available commands to create the symbol.

**Tip**

In the schematic, the net connection point will be the origin of the symbol.

11. Reposition the text strings as required.
12. Click the **File > Return to Part** menu item, and when prompted, click **Yes** to keep the gate 

changes.

The new symbol and existing symbols are displayed.

13. Click the **File > Save** menu item.

SailWind Logic Guide 

171Special Schematic Symbols

Creating New Special Symbols From Existing Symbols

If the Save Part Type to Library Dialog Box displays, accept the defaults and click **OK**.

14. Click the **File > Exit Part Editor** menu item.

**Tip**

For SailWind Logic to recognize the new special symbol, perform the instructions in The 

Update From Library Function.

## Creating New Special Symbols From Existing Symbols

Special symbols in SailWind Logic include power symbols, ground symbols, and off-page reference

symbols. SailWind Logic enables only one part definition in the library for off-page reference symbols, so

this option is unavailable when you click the **New** button to create a new part. You can modify the existing

symbols and/or add new symbols.

See also Creating New Special Symbols.

**Procedure**

1. Do one of the following:

• Copy an Existing Special Symbol

a. In the Library Manager (**File > Library** menu item), click the **Logic** button.

b. To filter the symbols, type a wildcard or expression on page 105 in the Filter box, and click 

**Apply**.

See also Special Symbol Naming Conventions.

c. Click **Copy**. The Save CAE Decal to Library dialog box displays.

**Tip**

**Copy** is unavailable if the Library list is set to All Libraries. (The library name is listed 

before the item in the CAE Decals list.) Double-click on the symbol to enter the library 

and then click **Copy**.

d. Type a name for the new special symbol.

e. Click **OK**.

• Modify an Existing Special Symbol

a. In the Library Manager, click the **Logic** button.

b. To filter the symbols, type a wildcard or expression on page 105 in the Items box and click 

**Apply**.

c. Select the symbol in the CAE Decals area.

172 

SailWind Logic GuideSpecial Schematic Symbols

Updating Special Symbol Mappings

d. Click **Edit**.

**Tip**

**Edit** is unavailable if the Library list is set to All Libraries. (The library name is listed 

before the item in the CAE Decals list.) Double-click on the symbol to enter the library 

and then click **Edit**.

e. Minimize the Library Manager dialog box or move it to one side.

f. Modify the graphics and rearrange the text strings as required.

g. Click the **Save** button.

2. Close the Library Manager dialog box or use it for another operation.

Refer to the following topics for information on assigning the new decal as an alternate decal:

**Table 23. Topic List Regarding Assigning New Decal as Alternate Decal**

**Alternate symbols** 

**Topic to see**

Off-page symbols 

Assigning Alternative Symbols for the Off-Page Part

Power symbols 

Assigning Alternative Symbols for the Power Part

Ground symbols 

Assigning Alternative Symbols for the Ground Part

## **Updating Special Symbol Mappings**

You can change the assignment or “mapping” of a special symbol using the Update from Library function.

For example, you can assign a new ground symbol to both a common ground and an analog ground.

**Procedure**

1. Click the **Tools > Update from Library** menu item.
2. In the Mode area of the Update From Library Dialog Box, choose “Update design from library.”
3. In the Items area, select one or more of the following check boxes:

• Off-page symbols

• Ground symbols

• Power symbols

4. Click **OK**.
5. In the Schematic Symbol column of the Remap Special Symbols Dialog Box, locate the power,

ground, or off-page symbol that you want to re-map double-click on the corresponding Library

Symbol box and then select the new symbol that you want to assign to the schematic symbol.

SailWind Logic Guide 

173Special Schematic Symbols

Management of Special Symbols in the Library

**Note:**

Only symbols currently associated with the special symbols in your library appear in the 

Library Symbol dropdown list.

6. Repeat step 4 for every symbol you want to re-map.
7. Click **OK**.

SailWind Logic updates the symbols and generates the Update From Library report on page 206.

The updated symbols appear in the “Mapped to” column of the report.

## **Management of Special Symbols in the Library**

Special Symbols are those used to create off-page reference, power and ground symbols, and

connectors. The default location of these special symbols is the *C:\<install_folder>\<version>\Libraries*.

Reinstalling the library will overwrite the common library files. If you modify a special symbol and want 

to keep the change, use Library/Export to transfer the symbol from the *C:\<install_folder>\<version>*

*\Libraries* folder to the *C:\<install_folder>\<version>\Libraries\usr* folder or to another library name.

174 

SailWind Logic Guide