# Chapter 12 Non-Electrical Objects  

A full complement of editing commands are available for working with non-electrical objects. Use the drafting commands to create lines, arcs, text, and all other items not generally associated with connectivity.  

Creating 2D Line Items   
Adding Text   
Moving Text   
Adding Circles   
Adding Polygons or Paths   
Adding Rectangles   
Modifying 2D Line Items   
Pulling Arcs   
Combining 2D Lines and Text   
Uncombining 2D Lines and Text   
Exploding Combinations   
Adding Drafting Items to a Library   
Adding Drafting Items From a Library   
Modifying Objects in a 2D Lines Library  

## Creating 2D Line Items  

To add drafting objects such as polygons, circles, rectangles, paths, as well as, arcs to polygons or paths, click the Create 2D Line button on the Schematic Editing toolbar. This changes the default popup menu to a specific popup menu for creating 2D line items.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Create 2D Line button.  

Right-click and set one or more of the following values before you add the drafting obje  

Table 27. Creating 2D Line Items - Options   


| Option     | Description                                          |
|------------|------------------------------------------------------|
| (Shape)    | Select to add a Polygon, Circle, Rectangle, or Path. |
| Width      | Specify a width value to override the default.       |
| Orthogonal | Adds segments in 90-degree increments.               |
| Diagonal   | Adds segments in 45-degree increments.               |
| Any Angle  | Adds segments at any angle.                          |

## Adding Text  

Free text is text not belonging to another object. All alpha, numeric, and special characters on the keyboard are valid. The maximum text string length is 72 characters including spaces.  

To add multiple lines of text to a design, see Embedding a Text Document.  

**Procedure** 

1. On the Schematic Editing Toolbar, click the Create Text button.  

2. Type the text string you want.  

To add a text entry with a bar over the characters, precede the text with the \ character. To place a bar over only a portion of text, enclose that section with the \ character.   
For example, typing \READ\WRITE places a bar over READ.  

3. To place the field at a precise X,Y coordinate location, type the value in the X and Y boxes.  

0 Tip If this is blank when you click OK, the field attaches to the pointer until you click to indicate the location.  

4. In the Rotation box, select the degree of rotation from the Rotation list. Rotation can be 0 or 90 degrees.  

5. For stroke font, in the Line Width box, type the line width.  

6. In the Size box, type the size (in mils for stroke font, in points for system fonts).  

!Tip  

Type a stroke font size between 10 and 1000 mils or a system font size between 1 and 72 points.  

7. For system fonts, select the font you want to use.  

You can also click a font style: B for bold, I for Italic, or U for Underlined.  

8. In the Justification area, set the horizontal and vertical justification of the text.  

9. If you combined the selected text string with a drafting object, right-click the text string, click Properties, and then select Parent to display the Drafting Properties dialog box to modify the drafting object.  

10. Click OK.  

**Related Topics**  

Combining 2D Lines and Text  

## Moving Text  

When you add a part to the schematic, all of the text associated with the symbol (reference designator, part name, pin number, attributes, etc.) appears in a predefined location. You can move the text to make room for other parts or connections or to make the schematic more readable.  

**Restrictions and Limitations**  

You can move a pin number a maximum of one inch from its pin terminal.   
• If you select and move a visible net name, with snap to grid enabled, the new net name snaps to the Labels and Text grid. To set the labels and text grid, use the General page in the Options dialog box. See “Options Dialog Box, General Category” on page 595.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Move mode button.   
2. Select the text string. It attaches to the cursor.   
3. Move the cursor and indicate a new position for the text. While moving text, you can modify the string using commands in the popup menu. The commands listed in the popup menu are based on the type of text being moved.  

## Adding Circles  

You can use the 2D line drafting command to add circle drafting objects to your design.  

**Procedure** 

1. On the Schematic Editing toolbar, click Create 2D Line then right-click and click the Circle popup menu item.   
2. Indicate the center point of the circle. A circle outline follows the cursor movement.   
3. Indicate the radius length to end the circle addition.  

## Adding Polygons or Paths  

You can use the 2D drafting command to add polygons or paths (with or without arcs) to your design.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Create 2D Line button then right-click and click the Polygon or Path popup menu item.   
2. Indicate the start point. A line follows the cursor movement.  

3. Move the cursor to the next corner and click again.  

. Continue adding corners in the same manner. a. If you want to add an arc rather than a straight segment, right-click and click Add Arc. b. To remove the last corner, press the backspace key or right-click and click the Del Corner popup menu item.  

5. Double-click to end the addition.  

Polygons automatically close; paths terminate at the last-defined corner.  

## Adding Rectangles  

You can use the 2D drafting command to add rectangle drafting objects to your design.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Create 2D Line button, right-click and click the Rectangle popup menu item.   
2. Indicate one corner of the rectangle. A box outline follows the cursor movement.   
3. Indicate the diagonally opposite corner at which to end the rectangle.  

## Modifying 2D Line Items  

You can use the Modify 2D Line button to change drafting objects. This changes the default popup menu to a specific popup menu for modifying 2D line items.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Modify 2D Line button.  

2. Select the line segment or corner to modify.  

The object is placed in Move mode.  

Use the popup menu to enable other 2D line modifications. If you select a segment, the following modification functions are available:  

Table 28. Modify 2D Line Item Options   


| Option      | Description                                 |
|-------------|---------------------------------------------|
| Pull Arc    | Converts a segment or corner into an arc.   |
| Split       | Divides a segment into two segments.        |
| Del Segment | Deletes the line segment at the pick point. |
| Width       | Changes the line width of the item.         |

| Option                       | Description                                                                                              |
|------------------------------|----------------------------------------------------------------------------------------------------------|
| Filled                       | Fills a closed polygon.                                                                                  |
| Solid Style and Dotted Style | Changes the line style to a solid or a dashed line. You cannot specify dotted lines for circles or arcs. |
| Orthogonal                   | Moves are made in 90-degree increments.                                                                  |
| Diagonal                     | Moves are made in 45-degree increments.                                                                  |
| Any Angle                    | Moves are made at any angle.                                                                             |

If you choose a corner, the popup menu uses most of the options as selected segments, plus the following:  

Table 29. Modify 2D Line Item - Corner Option   


| Option     | Description                                                                            |
|------------|----------------------------------------------------------------------------------------|
| Del Corner | Deletes the corner. A line segment is created between the corner's original endpoints. |

3. Reposition the cursor and indicate a new location for the item.  

## Pulling Arcs  

Pull Arc moves the selected line segment to create an arc, as the cursor is moved. Horizontal lines move in the vertical direction. Vertical lines move in the horizontal direction. Diagonal lines move in all directions, unless anchored by a line at the end of the diagonal. If an existing arc is selected, its endpoints remain fixed and the arc chord follows the cursor.  

Use the Pull Arc command to convert a drafting segment or corner into an arc. The starting points of the drafting segment become the start and stop angle for the new arc.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Modify 2D Line button.   
2. Select the line for arc conversion.   
3. Right-click and click the Pull Arc popup menu item. An arc follows the cursor movement.   
4. Click to indicate the end of the arc conversion.  

## Combining 2D Lines and Text  

In SailWind Logic, combining is the process of merging two or more 2D line or text items into a single complex 2D line item. After you have combined them, you can manipulate the group (move, rotate, duplicate, and so forth) as a single item. This is useful for creating title blocks or other similar features.  

**Restrictions and Limitations**  

• A combination can only include 2D lines or text. This differs from a group on page 215, which is a collection of objects (which may or may not include 2D lines or text) on the schematic.  

**Procedure** 

Use one of the following:  

• Using Object Mode a. Select a 2D line or block of text. b. Using Ctrl-click, continue to select items to combine. c. Right-click and click the Combine popup menu item. The selected items are combined.  

Tip When you select a 2D line item from the combination for move, duplicate, etc., all items are selected for the operation. Selecting text first will not select the whole group.  

• Using Verb Mode  

a. On the Schematic Editing toolbar, click the Combine/Uncombine button.  

b. Right-click and click the Combine popup menu item, then select a line item.  

![](/images/dc3bffe5fab06d2af1cccf279711c653010d66d007579b3f1755ae71fd399f0d.jpg)  

!Tip  

When combining 2D lines and text, always select the 2D line first, then select the text. If you try to select a text item before first selecting a 2D line, the message “No drawing item to add text to” displays.  

c. Continue to select the items to combine. Selected line items change to the highlight color.  

d. Right-click and click the Complete popup menu item. The selected items are combined.  

e. Click the Select button or press the Esc key to exit the Combine/Uncombine function.  

![](/images/bf6d65290d54df4d794e2a539496823ddbb1c85f6274699fb595b40bdb539b51.jpg)  

!Tip  

Selecting a 2D line item in the combination for move, duplicate, and so on, selects all items for the operation. Selecting text first does not select the whole group.  

**Related Topics**  

Adding Text Uncombining 2D Lines and Text Exploding Combinations  

## Uncombining 2D Lines and Text  

You can use the Uncombine command to remove individual objects from a combination.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Combine/Uncombine button, right-click and click the Uncombine popup menu item.   
2. Select the line or text item to remove.   
3. Continue selecting items to remove as necessary.   
4. Right-click and click the Complete popup menu item or press the Esc key when you finish removing objects from the group. The objects return to their original states and locations.  

**Related Topics**  

Exploding Combinations  

## Exploding Combinations  

You can use the Explode command to separate all objects from a combination.  

**Procedure** 

Use one of the following:  

• Using object mode: a. Select a 2D line item from the group. b. Right-click and click Explode. The combination is no longer combined, and objects are separated.  

!Tip  

In object mode, you can only explode a combination if it contains text items. Use the verb mode method (below) to explode a combination that does not have text items.  

• Using verb mode:  

a. On the Schematic Editing toolbar, click the Combine/Uncombine button.   
b. Right-click and click the Explode popup menu item and select the item to explode.   
c. Right-click and click the Complete popup menu item.  

## Adding Drafting Items to a Library  

You can save a 2D line item or a complex 2D line item in the schematic to a lines library. This makes it available in the current or future design sessions.  

**Procedure** 

1. Select an item, right-click and click the Save to Library popup menu item.   
2. Type the item name and specify the library location in the Save to Library dialog box.   
3. Click OK.  

## Adding Drafting Items From a Library  

Use the Get Drafting Item from Library dialog box to load a 2D line item from the available libraries to the current schematic.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Add 2D Line from Library button.  

2. In the Get Drafting Item from Library dialog box, select an item from the Drafting Items list.  

If the list does not contain the item you need, use the filter to search the available libraries. Use the wildcard convention, with or without leading characters, to expand or narrow the filter. Click Apply to activate the filter. SailWind Logic searches only active libraries with the Lines parameter checked for the 2D element.  

3. Click OK. The item follows the cursor movement.  

4. (Optional) You can rotate or mirror the item before you indicate its location. Right-click and click Rotate, Mirror $\pmb{\mathsf{X}}$ , or Mirror Y as often as needed to set the correct orientation of the item.  

5. Click to place the item.  

## Modifying Objects in a 2D Lines Library  

To edit an object that is stored in a 2D Lines library, you must first bring that object into the design workspace, make the desired edits and then save it back into the library.  

**Procedure** 

1. In the SailWind Logic workspace, on the Schematic Editing Toolbar, click the Add 2D Line from Library button.   
2. In the Get Drafting Item from Library dialog box, select the desired object from the Drafting Items list and click OK. The item will attach to the cursor.   
3. In the design workspace click a location to place the item.   
4. Make the desired edits using the commands available on the Schematic Editing Toolbar and the right mouse button menus.   
5. After you have completed the desired edits, select the objects that make up the drawing item, right click and choose Save to Library.   
6. You can choose to either overwrite the item or save it as a new item. Clicking OK saves the 2D line object back into the 2D Lines library.  

!Tip  

To save multiple objects that include lines and text, you must first select all the items, choose Combine from the right mouse menu, and then choose Save to Library from the right mouse button menu.  

