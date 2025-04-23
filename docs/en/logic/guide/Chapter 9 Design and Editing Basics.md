# Chapter 9 Design and Editing Basics  

A wide selection of methods are available for design editing and navigation. This enables a high level of flexibility for selecting, moving, duplicating, and deleting design objects. A robust selection filter allows precise selection of design objects individually and as groups. There are also operations available for finding design objects as well as a very powerful step and repeat function.  

Design Operations   
Modes of Operation   
Selecting Objects   
Controlling Selections   
Filtering Object Selections   
Using the Selection Filter   
Selection List   
Find Objects   
Step and Repeat  

# Design Operations  

When you start SailWind Logic or select New from the File menu, a drawing format is automatically added to the work area. The drawing format is the representation of the sheet on which you will begin to create your schematic design.  

See Options Dialog Box, Design Category for information about changing the default drawing format. Use Options to set the default working grid, display grid, text size, etc.  

To add new design information:  

• On the toolbar, click the Schematic Editing toolbar button   
Add and edit parts from libraries Create hierarchical symbols   
Add connections   
• Swap pins and reference designators Define bus structures Create and edit non-electrical information; text, charts, notes, etc  

**Related Topics**  

Part Editor Operations  

# Modes of Operation  

You can use the different modes of operation to edit designs in SailWind Logic. These include verb mode and object mode. There are also multiple choices available for zooming to various areas of your design using your pointer device or keyboard commands. To accommodate repetitive operations, you can use duplicate mode, delete mode, or move mode  

Editing Basics Zooming Using Duplicate Mode Using Delete Mode Using Move Mode  

# Editing Basics  

Most design work involves editing the database—adding, modifying, and deleting items. This section describes the modes of operation in SailWind Logic that enable you to edit your designs.  

SailWind Logic has two basic modes of operation: Object Select Mode (Select Object First), and Verb Mode (Select Command First). In addition to these operational modes, SailWind Logic has Zoom mode. Zooming overrides all other modes until you specify another mode.  

Verb Mode (Select Command First) Object Select Mode (Select Object First)  

# Verb Mode (Select Command First)  

Commands that operate on a selected object are considered verb commands. In Verb mode, select the mode, and then select the objects on which to perform the command.  

**Procedure** 

1. To put SailWind Logic in Verb mode, select one of the following commands from the standard toolbar.  

Using Duplicate Mode Using Move Mode   
• Using Delete Mode Query Mode — (see Schematic Object Modification)  

2. Then select an object. When you move the cursor off the toolbar, a small V appears on the cursor to show that SailWind Logic is in Verb mode.  

3. To exit Verb mode, on the Schematic Editing toolbar, click the Select button or press the Esc key.  

# Object Select Mode (Select Object First)  

In Object Select mode, select the object, and then select a command to perform an action.  

**Procedure** 

1. Position the cursor over the object and click once. The selected item highlights. 2. Select a command, using one of the following:  

• Right-click and click a command. Click a command from a menu.   
• Click a button.  

# Zooming  

The Zoom button acts as a toggle. You can zoom in, out or to a specific area of the design.  

Zooming In   
Zooming Out   
Specify the Zoom Area  

# Zooming In  

You can zoom into the view to see more detail in your design.  

**Procedure** 

1. On the standard toolbar, click Zoom to enter zoom mode.   
2. Point to the new view center and click.  

# Zooming Out  

You can zoom out from the current view to see more of the objects in your design.  

**Procedure** 

1. On the standard toolbar, click Zoom to enter zoom mode.   
2. Point to the new view center and right-click.  

# Specify the Zoom Area  

To view a specific area of your design, you can drag a rectangle to specify the zoom area.  

**Procedure** 

1. On the standard toolbar, click the Zoom button to enter zoom mode.   
2. Press and hold the left button and drag diagonally upward to zoom in.   
3. Press and hold the left button and drag diagonally downward to zoom out. See also Creation of Groups.  

# Using Duplicate Mode  

Use Duplicate Mode to replicate existing parts, text, and drafting objects. When you copy parts, SailWind Logic automatically increments the reference designator and gate modifier.  

**Procedure** 

1. On the toolbar, click the Duplicate mode button.  

2. Select the item to copy.  

A duplicate of the item follows the cursor movement.  

3. (Optional) Depending on the available options for the selected item, you can adjust the orientation and other settings from the popup menu before placement. Position the item and indicate its location to complete the copy.  

4. When you finish placing copies of this item, right-click and click the Cancel popup menu item.  

SailWind Logic remains in duplicate mode until you select another mode or the Select button from the toolbar. You can also press the Esc key to exit the mode.  

**Related Topics**  

Schematic Parts Non-Electrical Objects Step and Repeat  

# Using Delete Mode  

Use Delete mode to remove parts, connections, unconnected buses, text, drafting objects, and hierarchical symbols from the design. If you delete a part with connections, SailWind Logic also deletes the connections.  

![](/images/d445e567778ec0c42085fb7ea426777f60656870391d239f375b010c08f15cee.jpg)  

!Tip  

If you are in Object Select Mode (Select Object First), you can delete a part without deleting the connections.  

**Procedure** 

1. On the toolbar, click the Delete mode button.  

2. Select the object to delete.  

SailWind Logic remains in Delete mode until you select another mode or the Select button from the standard toolbar. You can also press the Esc key to exit the mode.  

# Using Move Mode  

Use Move Mode to adjust the position of existing parts, connections, text, and drafting objects.  

**Procedure** 

1. On the toolbar, click the Move mode button.   
2. Select the object to move.  

The object follows the cursor movement.  

![](/images/7f6e998d79e692e09ecb0f484516b518feffaa83a0c89ffcdda978c7b6556f95.jpg)  

!Tip  

(Optional) Depending on the available options for the selected object, you can adjust the orientation and other settings from the popup menu before placement. Position the object and indicate its location to complete the move.  

SailWind Logic remains in move mode until you select another mode or the Select button from the toolbar. You can also press the Esc key to exit the mode.  

# Selecting Objects  

You can select individual or multiple objects in your design. Selecting multiple objects enables you to apply a specific action to multiple objects simultaneously.  

!Note:  

You can also search and select objects. For more information, see Searching for an Object by Typing Information.  

Selecting One Object   
Selecting Several Objects   
Selecting All Objects in an Area   
Selecting All Objects on a Sheet   
Selecting an Object on All Sheets in a Schematic  

# Selecting One Object  

To highlight or apply a command only to one object, you can select a single object in your design.  

**Procedure** 

Place the cursor over the object and click the left mouse button.  

The object selects and highlights.  

Any previously selected objects are deselected. If you click over empty space, all previously selected objects are deselected.  

If you try to select an object in a dense or crowded area, use the Using the Selection Filter to disable other items for selection.  

To select invisible signal pin nets, which you cannot select by clicking on them, see the Signal Pin Nets topic.  

# Selecting Several Objects  

To highlight or apply a command to multiple objects, you can select several objects in your design.  

**Procedure** 

Press and hold the Ctrl key while you select multiple items.   
If you did not select an object previously, the software adds it to the set of selected objects.   
If you selected the object previously, the software removes it from the set of selected objects.  

# Selecting All Objects in an Area  

To highlight or apply a command to all objects, you can select all of the objects in a particular area of the design.  

**Procedure** 

1. Hold the left mouse button down and drag a selection rectangle around one or more objects; start at one corner of the area and drag to the opposite diagonal corner.   
2. When you release the button, the software selects all objects contained within the rectangle. You can add additional objects to the selection or remove objects from the selection using Ctrl +click.  

# Selecting All Objects on a Sheet  

On the sheet you are viewing, you can select all objects of a particular type, depending on the Selection Filter you are using.  

For example, you could select all nets or all gates on the sheet.  

**Procedure** 

To select all objects of a particular type on the sheet you are viewing, click the Edit $>$ Select All on Sheet menu item, or press Ctr $+\mathsf{A}$ .  

# Selecting an Object on All Sheets in a Schematic  

Across the entire schematic, you can select all objects of a particular type, depending on the Selection Filter you are using. For example, you could select all nets or all gates on every sheet in the schematic.  

**Procedure** 

To select all objects of a particular type on every sheet in the schematic, click the Edit $>$ Select All on Schematic menu item, or press Shift $+\mathsf{C t r l}+\mathsf{A}$ .  

# Controlling Selections  

Sometimes you cannot easily select the object you want because several objects exist at the same location. You can use the Selection Filter to specify specific object types so that only those items can be selected.  

To control what information you select, use the Using the Selection Filter.  

See also Selection List.  

# Filtering Object Selections  

There are three ways to filter the objects you select: the Selection toolbar buttons, the popup menu when nothing is selected, and the Selection Filter Dialog Box.  

Filtering With the Selection Toolbar Filtering With the Popup Menu Filtering With the Selection Filter Dialog Box  

# Filtering With the Selection Toolbar  

Use the Selection toolbar buttons to enable or disable object selection. This enables you to limit your selection to only specific object types.  

**Procedure** 

1. On the toolbar, click the Selection Toolbar button.   
2. On the Selection Filter toolbar, click the buttons for the objects for which you want to enable or disable selection.  

Tip You cannot use the Parts Filter and the Gates Filter at the same time.  

# Filtering With the Popup Menu  

With nothing selected, you can use the popup menu that appears to set the selection filter to the desired object type.  

**Procedure** 

1. With nothing selected in the schematic, right-click to open the popup menu.   
2. Select the object you want to filter from the list.  

# Filtering With the Selection Filter Dialog Box  

You can use the Selection Filter dialog box to specify a specific filter. This enables very precise selection of objects by enabling only those object types that you want to select.  

**Procedure** 

1. Click the Edit $>$ Filter menu item.   
2. Select the desired item or items for your filter.  

# Using the Selection Filter  

Use the Selection Filter dialog box to control which objects you can select. The Selection Filter offers the capability to set very precise filters enabling you to select anything, a very narrow subset of the available design objects, or nothing at all. You can use the Nothing selection to quickly reset the filter and then you can make a new filter selection.  

**Procedure** 

1. With nothing selected, right-click and click the Filter popup menu item. As an alternative, click the Edit $>$ Filter menu item.   
2. In the Selection Filter dialog box, select the check box beside each design object that you want to turn on or off. Click Anything if you want to select the check boxes for all design objects or click Nothing if you want to clear all check boxes.  

3. Click Close.  

**Related Topics**  

Filtering Object Selections Object Select Mode (Select Object First)  

# Selection List  

The Selection list provides an efficient means of searching and selecting particular objects in your design.  

Searching for an Object by Typing Information Selecting an Object With Area Selection  

# Searching for an Object by Typing Information  

You can search for one or many objects by entering search criteria in the Selection List box of the Selection toolbar.  

![](/images/2fbe4345bb738f2bf8b4c4b2b6e0b84763f27fbad6d3d5c9a0cd7f9d5f7a80d9.jpg)  

**Restriction:**  

You must set the selection filter to enable selection of the object type being searched.  

**Procedure** 

1. On the Standard toolbar, click the Selection Toolbar button.  

2. In the list box of the Selection Filter toolbar, type information about the object.  

For example, type the part name, gate name, part type name, net name, or pin name of the object you want, and then press the Enter key.  

The workspace pans to the object and selects it.  

!Tip  

When working with the Selection List, note the following: ◦ The Selection List supports Wildcards and Expressions. ◦ You can search for several objects by separating entries with commas.  

See also Filtering Object Selections.  

# Selecting an Object With Area Selection  

When you make an area selection, the Selection list on the Selection toolbar displays the selected objects and the sheet on which they are located. When multiple objects are selected, All in List appears in the list, making it easier for you to locate a particular object by just selecting the item, especially in a congested design.  

**Procedure** 

1. On the Standard toolbar, click the Selection Toolbar button.   
2. Click the Selection Filter toolbar buttons to include the object you want to locate. See also Filtering Object Selections.   
3. Make an area selection in the general area of the object you want to locate.  

4. Select the particular object from the Selection list on the Selection Filter toolbar. If desired, select “All in List” to re-select all of the objects in the multiple selection.  

5. Click the Next Object or Previous Object buttons to move the selection from one object to the next in the current multiple selection.  

!Tip  

Other selection methods:  

• To make multiple selections in the schematic, use Ctrl or Shift and click. • To locate a very small object, zoom in on the current sheet, then select the object from the list.  

# Find Objects  

You can search for objects in SailWind Logic using a number of different options. These include the modeless commands, the Selection Toolbar, the Selection Filter, and by controlling the view.  

Table 24. Search for Objects in SailWind Logic Using These Options   


<table><tr><td>Option</td><td>Description</td></tr><tr><td>Modeless Commands and Keyboard Shortcuts on page 569</td><td>Use keystrokes to locate specific objects or types of objects.</td></tr><tr><td>Selection Toolbar</td><td>Controls which types of objects you can select, locates specific objects from a multiple selection, or moves between sheets in the schematic.</td></tr><tr><td>Using the Selection Filter</td><td>Controls types of objects you can select. Enables you to select the object you want even when several objects exist at the same location.</td></tr><tr><td>View Control</td><td>Changes the perspective and size of the work area.</td></tr></table>  

# Step and Repeat  

Use Step and Repeat to multiply objects as you place them during an add or duplicate operation. Step and Repeat is available in the Schematic Editor and the Decal Editor. In the Schematic Editor, the Step and Repeat command copies parts, connections, text, or drafting items. In the Decal Editor, the Step and Repeat command copies terminals, text, or drafting items.  

**Procedure** 

1. Select an object during an add or duplicate operation. While a dynamic object is attached to the cursor, right-click and click the Step and Repeat popup menu item.  

![](/images/27b14a8d6e06623fc42ed212aaae9321cab3a796563ab156c7ce2eb738a9836a.jpg)  

Tip   
When adding a new object in the Schematic Editor, you must place the first object manually before you can use Step and Repeat.  

2. In the Step and Repeat dialog box, click the direction of placement for the array.  

3. In the Count box, type the number of objects to place or click the arrow buttons.  

4. In the Distance box, type the distance between objects or click the arrow buttons.  

![](/images/6b964dda315fa9691708420e362548484e38e7f63408a5ba40de5b00ea2a71dd.jpg)  

!Tip  

If you place a second object and then Step and Repeat, the spacing between the objects will become the default value in the Distance box and will repeat the pattern you have started.  

5. Click the Preview button to view the placement of the multiple objects based on the options you set. The placement of the objects is based on the location of the original object selected.  

![](/images/55392d890bee4a05dd4422ec03746aa4832b86b5c49a3f4e34384c2ed052beee.jpg)  

Tip Zoom Mode is available during Step and Repeat.  

6. After achieving the desired placement preview, click OK to place the objects.  

# Results  

After using Step and Repeat, the original dynamic object is still attached to the cursor. You can continue to add or duplicate using this object, or you can press the Esc key to end the operation.  

When duplicating connections, only connections with valid start and end points remain after the Step and Repeat operation; even if invalid connections appear during the preview. A duplicated connection can start on a component pin or on another connection segment. A duplicated connection can end on a component pin, a connection segment, or a bus segment.  

SailWind Logic automatically assigns new bus netnames to bus segment copies. The new netname is based on the original bus segment netname, plus one. For example, if you make a duplicate of bus segment D00, the duplicate is assigned the netname D01.  

# See also Working With Floating Connections.  

If you manually place a duplicate within $0.5"$ of the original (in both X and Y directions), the next connection is placed at the same offset. Then press the Space Bar to place a new duplicate. You can continue to use this semi-automated Step and Repeat process to place subsequent duplicates.  

