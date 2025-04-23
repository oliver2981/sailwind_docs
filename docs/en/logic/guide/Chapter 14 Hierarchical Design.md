# **Chapter 14 Hierarchical Design**

SailWind Logic supports hierarchical design where you can create symbols to represent entire sub

schematics and show system interactivity at a higher level. You can create hierarchy from either the top

down or the bottom up.

Hierarchical Design Overview

Creating a Top-Down Hierarchy

Creating a Bottom-Up Hierarchy

Pushing Into the Hierarchy

Popping Up the Hierarchy

Modifying a Hierarchical Symbol

Copying a Hierarchical Symbol

Deleting a Hierarchical Symbol

## **Hierarchical Design Overview**

Using hierarchical design, you can create high-level symbols to represent complex sub-schematics, or 

repetitive elements in your design. You can create a hierarchy by using either the top down or the bottom

up design strategy.

• **Top down** — You define a hierarchical symbol and then the underlying logic.

• **Bottom up** — You create a schematic, then define the hierarchical symbol for the schematic.

You can also assign or unassign hierarchical connections in the Hierarchical Component properties on 

page 296 dialog box.

Level 0 is the top design level that contains the design contents. Numbered sheets from sheet 1 to 

1024 represent the design contents. A SailWind Logic design cannot exceed a total number of 1024 

hierarchical and numbered sheets.

You can navigate the hierarchy with the Push Hierarchy on page 269 and Pop Hierarchy on page 270

commands on the **View** menu.

When a hierarchical symbol is copied, any existing underlying schematic content is also copied. SailWind 

Logic updates the reference designator names of the underlying symbols. There is a one-to-one 

correspondence between hierarchy symbols and a schematic sheet. The underlying logic for duplicated 

hierarchical symbols is stored as a unique sheet, and can be edited without affecting the logic of other

hierarchical symbols. Even though you copy a hierarchical symbol, its underlying schematics can be 

completely different from the copied symbol’s underlying schematics.

## **Creating a Top-Down Hierarchy**

In top-down design, you create a hierarchical symbol before the underlying schematic exists. This 

enables you to create the container object and then populate it with the lower level design elements. Pin 

names tie together signals between hierarchical levels.

SailWind Logic Guide 

267Hierarchical Design

Creating a Bottom-Up Hierarchy

SailWind Logic ties together all instances of a common signal name, regardless of where they are found 

in the design, into a single connection net. You establish connectivity across the hierarchy by using the

same signal name in the underlying logic.

**Prerequisites**

• Ensure that the off-page signals in the underlying schematic are consistent with the pin names in

the hierarchical symbol.

**Procedure**

1. On the Schematic Editing toolbar, click the **New Hierarchical Symbol** button.
2. In the Hierarchical Symbol Wizard Dialog Box, in the Hierarchical Sheet area, type the symbol 

name in the Sheet Name text box.

3. Select your preferred Pin Decal for both input and output pins from the appropriate dropdown list 

boxes.

4. Specify the Pin Count for both input and output pins.

The Preview area displays the symbol outline.

5. Click **OK**. The hierarchical symbol appears in the Part Editor on page 109 window.

**Tip**

Because the symbol is a hierarchical one, it has no pin numbers. The pin name associated 

with pins of the hierarchical symbol identify the net name of the connection that is tied to 

the pin. All pins on a hierarchical symbol must have a pin name. You cannot complete the

hierarchical symbol until you assign a name to each pin.

6. In the Part Editor, double-click each pin to open the Terminal Properties dialog box on page 131

where you name the selected pin. You must name each pin of the symbol.

7. Click the **File > Complete** menu item.

This closes the Part Editor, and the new symbol attaches to the cursor.

8. Move the cursor to a desired location and click to place the symbol in the schematic.
9. You can navigate this hierarchy with the **View > Push Hierarchy**, and **View > Pop Hierarchy** 

menu commands.

**Related Topics**

Creating a Bottom-Up Hierarchy

## **Creating a Bottom-Up Hierarchy**

In bottom-up design, you create a hierarchical symbol from an existing sheet that represents the 

underlying logic. This enables you to create the lower level design and then wrap it in the hierarchical 

symbol.

268 

SailWind Logic GuideHierarchical Design

Pushing Into the Hierarchy

SailWind Logic adds an input or output pin in the symbol for each off-page reference on the schematic

sheet. SailWind Logic places off-page references with a pin type of Source on the left side of the

hierarchical symbol, and off-page references with a pin type of Load on the right side. (Pin types for off

page references are defined in the library under electrical.)

**Procedure**

1. Switch to the sheet to which you want to add the hierarchical symbol. If needed, add a new 

schematic sheet to the sheet set using the **Setup > Sheets** menu item.

2. On the Schematic Editing toolbar, click the **New Hierarchical Symbol** button.
3. On the Hierarchical Symbol Wizard dialog box, select an existing sheet from the Sheet Number 

dropdown list box in the Hierarchical Sheet section.

4. Type a name for the symbol in the Sheet Name text box.
5. Select your preferred Pin Decal for both input and output pins from the appropriate dropdown list 

box.

The Preview area displays the symbol outline. The number of input/output pins on the symbol 

is automatically set from the number and type of off-sheet reference symbols on the underlying

schematic sheet and the pin count boxes are unavailable for editing.

6. Click **OK**.

The hierarchical symbol appears in the Part Editor on page 109 window. An input or output pin is

located on the symbol to match each off-page reference on the underlying schematic sheet.

7. Click the **File > Complete** menu item.

This closes the Part Editor, and the new symbol attaches to the cursor.

8. Move the cursor to a desired location and click to place the symbol in the schematic.
9. You can navigate this hierarchy with the **View > Push Hierarchy** and **View > Pop Hierarchy** menu 

commands.

**Related Topics**

Creating a Top-Down Hierarchy

## **Pushing Into the Hierarchy**

Use the Push Hierarchy command to look inside or push down into a hierarchical symbol to view the 

underlying logic.

**Procedure**

1. Click the **View > Push Hierarchy** menu item.
2. Select the hierarchical symbol.

SailWind Logic Guide 

269Hierarchical Design

Popping Up the Hierarchy

Alternatively, you can select the hierarchical symbol, right-click and click **Push Hierarchy**.

**Tip**

If there is no underlying schematic representation of the selected symbol, a blank sheet 

appears.

## **Popping Up the Hierarchy**

Use the Pop Hierarchy command to replace the current sheet with its corresponding hierarchical symbol.

**Procedure**

In a hierarchical sub-schematic, click the **View > Pop Hierarchy** menu item.

**Tip**

In the Sheets list on the main toolbar, a sub-schematic is displayed with an indented icon.

## **Modifying a Hierarchical Symbol**

Once created, you can modify a hierarchical symbol to add or subtract design detail.

**Procedure**

1. Select a hierarchical symbol, right-click and click **Edit Hierarchical Symbol**.
2. Modify the symbol in the Part Editor on page 109.
3. Click the **File > Complete** menu item when you are finished with the changes.

**Tip**

If you add terminals to a hierarchical symbol, ensure that you give them pin names, 

and that the names also appear as off-page references in the sheet with the underlying

schematic.

**Related Topics**

Hierarchical Symbol Wizard Dialog Box

Deleting a Hierarchical Symbol

## **Copying a Hierarchical Symbol**

When you copy a hierarchical symbol, the sheets that the symbol references will also be copied and 

added as new sheets to the schematic. SailWind Logic assigns new reference designators to the part 

types in the copied sheets. If the referenced sheet also contains hierarchical symbols, then SailWind 

270 

SailWind Logic GuideHierarchical Design

Deleting a Hierarchical Symbol

Logic also copies the sheets referenced by those symbols, and so on, down the entire sub-tree of the 

hierarchy.

**Procedure**

1. Select the symbol in the design.

When you select a hierarchical symbol in copy mode, a warning prompt appears. If you click **Yes**

in the prompt window, SailWind Logic copies the hierarchical symbol, and all directly or indirectly

referenced sheets. If any numbered sheets are referenced, SailWind Logic assigns the copies new 

sheet numbers.

2. Ctrl+drag a copy.
3. In the warning prompt, click **Yes**.

The symbol copy attaches to the cursor.

4. Click the place the symbol.

**Related Topics**

Hierarchical Symbol Wizard Dialog Box

Modifying a Hierarchical Symbol

Deleting a Hierarchical Symbol

## **Deleting a Hierarchical Symbol**

You can delete a hierarchical symbol, but use caution when performing the operation.

**Procedure**

1. On the Schematic Editing Toolbar, click the **Delete** button.
2. When you select a hierarchical symbol in delete mode, the message “OK to delete sheets 

associated with the hierarchy - Warning: there is no Undo for this operation” appears. Be sure of

your intent before confirming the command.

• If you click **Yes**, SailWind Logic deletes the hierarchical symbol and any associated sheets 

throughout the hierarchy.

• If you click **No**, and it is a hierarchical symbol without a sheet number, SailWind Logic assigns it

the next unused sheet number and it becomes a normal, numbered sheet.

SailWind Logic Guide 

271Hierarchical Design

Deleting a Hierarchical Symbol

272 

SailWind Logic Guide