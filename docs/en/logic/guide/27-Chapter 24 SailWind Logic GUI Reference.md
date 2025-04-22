# Chapter 24 SailWind Logic GUI Reference

The section contains information on all of the GUI elements in SailWind Logic.

AC Analysis Dialog Box
Add Attribute Label Dialog Box
Add Bus Dialog Box
Add/Edit Command Dialog Box
Add Field Dialog Box
Add Free Text Dialog Box
Add Net to Class Dialog Box
Add New Attribute Dialog Box
Add New Attribute to Library Dialog Box
Add Part From Library Dialog Box
Add Pins Dialog Box
Archiver Dialog Box
Archiver Additional Files Dialog Box
Archiver Libraries Dialog Box
ASCII Output Dialog Box
Assign Alternatives for Ground Part Dialog Box
Assign Alternatives for Off-Page Part Dialog Box
Assign Alternatives for Power Part Dialog Box
Assign Decal to Gate Dialog Box
Assign New Gate Decal Dialog Box
Assign New PCB Decal Dialog Box
Assign Shortcut Dialog Box
Attribute Properties Dialog Box
Auto Renumber Parts Dialog Box
Basic Script Editor
Basic Scripts Dialog Box
Bill of Materials Setup Dialog Box
Browse for Connectors Dialog Box
Browse for Special Symbols Dialog Box
Browse Library Attributes Dialog Box
Bus Name Properties Dialog Box
Bus Properties Dialog Box
CAE Decal Wizard Dialog Box
Capture a New View Dialog Box
Change Part Type Dialog Box
Check for Updates Dialog Box
Class Rules Dialog Box
Clearance Rules Dialog Box

SailWind Logic Guide

431

SailWind Logic GUI Reference

Compare/ECO Tools Dialog Box
Conditional Rule Setup Dialog Box
Connect to SailWind Layout Dialog Box
Connect to SailWind Router Dialog Box
Crash Detected Dialog Box
Create PDF Dialog Box
Customize Dialog Box
DC Source Sweep Analysis Dialog Box
Default Rules Dialog Box
Differential Pairs Dialog Box
Display Colors Dialog Box
Display Colors Dialog Box - Part Editor
Drafting Properties Dialog Box
Edit Button Image Dialog Box
Fields Dialog Box
Field Properties Dialog Box
Font Replacement Dialog Box
Fonts Dialog Box
Get Drafting Items From Library Dialog Box
Get Gate Decal From Library Dialog Box
Get PCB Decal From Library Dialog Box
Hierarchical Symbol Wizard Dialog Box
HiSpeed Rules Dialog Box
Installed Options Dialog Box
Library List Dialog Box
Library Manager Dialog Box
Log Test Dialog Box
Logic Families Dialog Box
Make Field Dialog Box
Manage Library Attributes Dialog Box
Manage Schematic Attributes Dialog Box
Media Wizard Dialog Box
Modeless Commands and Keyboard Shortcuts
Net Attributes Dialog Box
Net Name Properties Dialog Box
Net Properties Dialog Box
Net Rules Dialog Box
Netlist to PCB Dialog Box
Off-Page Properties Dialog Box
Options Dialog Box
Options Dialog Box - Part Editor, General Category
Options Dialog Box - Print/Plot
Output Window
SailWind Layout Link Dialog Box

432

SailWind Logic Guide

SailWind Logic GUI Reference

SailWind Router Link Dialog Box
SailWind Suite Configuration Dialog Box
Part Attributes Dialog Box
Part Information Dialog Box
Part Properties Dialog Box
Part Signal Pins Dialog Box
Part Text Visibility Dialog Box
Part Type Label Properties Dialog Box
Pen Plotter Advanced Setup Dialog Box
Pen Plotter Setup Dialog Box
PCB Decal Assignment Dialog Box
Photo Plotter Advanced Setup Dialog Box
Photo Plotter Setup Dialog Box
Pin Decal Browse Dialog Box
Pin Decal List Management Dialog Box
Pin Label Fonts Dialog Box
Pin Properties Dialog Box
Plot Dialog Box
Print Dialog Box
Project Explorer
Query Hierarchical Component Dialog Box
Reference Designator Properties Dialog Box
Remap Special Symbols Dialog Box
Rename Gate Dialog Box
Rename Part Dialog Box
Renumber Pins Dialog Box
Report Manager Dialog Box
Reports Dialog Box
Routing Rules Dialog Box
Rules Dialog Box
Rules Report Dialog Box
Save CAE Decal to Library Dialog Box
Save Configuration Dialog Box
Save Drafting Item to Library Dialog Box
Save Off-Page to Library Dialog Box
Save Part and Gate Decals As Dialog Box
Save Part Types to Library Dialog Box
Save Part Type to Library Dialog Box
Save PCB Decal to Library Dialog Box
Save View Dialog Box
Select Gate Decal Dialog Box
Select Pin Decal Dialog Box
Select Type of Editing Item Dialog Box
Selection Filter Dialog Box

SailWind Logic Guide

433

SailWind Logic GUI Reference

Selections Preview Dialog Box
Server Busy Dialog Box
Sheets Dialog Box
Signal Pin Nets Dialog Box
Simulation Setup Dialog Box
SPICEnet Dialog Box
Step and Repeat Dialog Box
Text Properties Dialog Box
Transient Analysis Dialog Box
Update From Library Dialog Box
Update Selected CAE Decals From Library Dialog Box
Update Selected Part Type From Library Dialog Box
Update Selected Pin Decals From Library Dialog Box

434

SailWind Logic Guide

SailWind Logic GUI Reference
AC Analysis Dialog Box

## AC Analysis Dialog Box

To access: Tools  > SPICE Netlist  menu item > Simulation Setup  button > AC Analysis  button

Set options specifically for an AC analysis.

Note:
Pictures in this document are for reference only, to help users better understand the software
operation. In the case of interface difference due to version changes, the interface of SailWind
Logic in practice shall prevail.

Figure 14. AC Analysis Dialog Box

Objects

Name

Interval area

Table  48. AC Analysis Fields

Description

Specifies the number of points and the variation: Decade, Octave,
or Linear.

Frequency

Specifies the Starting and Ending frequencies.

Related Topics

Creating a SPICE Netlist

Setting Up AC Analysis

SailWind Logic Guide

435

SailWind Logic GUI Reference
Add Attribute Label Dialog Box

## Add Attribute Label Dialog Box

To access:

• Select a part > right-click > Edit Part  menu item > Edit Graphics button > select a gate > Decal

Editing Toolbar  button > Add Attribute Label  button

• With nothing selected > Tools  > Part Editor  menu item > Edit Graphics button > Decal Editing

Toolbar  button > Add Attribute Label  button

Use the Add Attribute Label dialog box to create attribute labels while editing or creating a CAE Decal.

Figure 15. Add Attribute Label Dialog Box

Objects

Table  49. Edit Attribute Label Fields

Name

Description

Attribute Name list

Lists all of the attributes available to you.

 Tip
You can type the attribute name or browse the Library
Attributes.

Browse Lib. Attr.  button

Opens the Browse Library Attributes Dialog Box.

Height

Width

Rotation

Specifies the height of the text.

Specifies the width of the text.

Specifies the rotation of the text: 0 or 90 degrees.

Horizontal/Vertical Justification

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

436

SailWind Logic Guide

Related Topics

Creating Attribute Labels

SailWind Logic GUI Reference
Add Attribute Label Dialog Box

SailWind Logic Guide

437

SailWind Logic GUI Reference
Add Bus Dialog Box

## Add Bus Dialog Box

To access: Schematic Editing toolbar > Add Bus  button> click to indicate starting point > double-click to
indicate ending point

Use the Add Bus dialog box to create attribute labels while editing or creating a CAE Decal.

Figure 16. Add Bus Dialog Box

Objects

Name

Bus Name

Table  50. Add Bus Dialog Box Fields

Description

Specifies the name of the bus. Select or type the name you want.

Rename area

Specifies to rename this instance or all instances of the bus.

 Restriction:
Available only in query mode.

Bus Type area

Specifies which bus names appear in the Bus Name list.

438

SailWind Logic Guide

Table  50. Add Bus Dialog Box Fields  (continued)

Name

Description

SailWind Logic GUI Reference
Add Bus Dialog Box

Add Bus Name Label

Bus Nets table

Select the Add Bus Name Label check box to add the bus name
as a label to the bus at the end of the bus closest to where you
selected it.

 Restriction:
The check box is unavailable when the end of the selected bus
has a label.

 Tip

• A bus can have two labels, one on each end.
• A bus label is not required.
• To delete a bus label, select the label in the schematic and

click the Delete  button on the standard toolbar.

Lists the name or prefix of the bus net, the starting bit number for
a sequence of nets, and the ending bit number for a sequence of
nets.

 Restriction:
Available only if the bus is a mixed net bus.

 Tip

• For a single net, type the net name.

• For a range of sequential nets, type the prefix for the sequence

of nets.

Add  button

Adds a row to the Bus Nets table.

 Restriction:
Available only if the bus is a mixed net bus.

Edit  button

Makes the selected row available for editing.

 Restriction:
Available only if the bus is a mixed net bus.

Delete  button

Removes the selected row from the Bus Nets table.

 Restriction:
Available only if the bus is a mixed net bus.

Down/Up  buttons

Moves the selected row up or down in the Bus Nets table.

 Restriction:
Available only if the bus is a mixed net bus.

Related Topics
Managing Buses

SailWind Logic Guide

439

SailWind Logic GUI Reference
Add/Edit Command Dialog Box

## Add/Edit Command Dialog Box

To access: Tools  > Customize  menu item > Commands  tab > select a command >New  or Edit  button

Use the Add Command dialog box to create commands that you can then use as selections on menus or
as buttons on toolbars.

Figure 17. Add Command Dialog Box

Objects

Table  51. Add/Edit Dialog Box Fields

Name

Description

Command name

The name of the new command.

Based on

Arguments

 Tip
Type an ampersand before the letter you want to use as the Alt
keyboard shortcut.

The command on which you want to base the new command.

Any arguments for the new command.

 Tip
Use a space to separate arguments. If an argument contains a
space, enclose the argument in quotation marks (“”).

 Restriction:
SailWind Router only.

Description

Lists what the new command does.

Use Default Image

Use the recommended image.

440

SailWind Logic Guide

SailWind Logic GUI Reference
Add/Edit Command Dialog Box

Table  51. Add/Edit Dialog Box Fields  (continued)

Name

Description

Select User-defined Image

Select or create your own image to associate with the new
command.

New  button

Edit  button

Open the Edit Button Image Dialog Box.

Open a button in the Edit Button Image Dialog Box.

Related Topics

Creating a Custom Command

Creating a Custom Menu

SailWind Logic Guide

441

SailWind Logic GUI Reference
Add Field Dialog Box

## Add Field Dialog Box

To access: Select nothing or a 2D line object > right-click > Add Field  menu item

Use the Add Field dialog box to add a field to your schematic.

Figure 18. Add Field Dialog Box

Objects

Name

Name list

Value

X/Y

442

Table  52. Add Field Dialog Box Fields

Description

Type the name of a new field or select from a list of the fields
available to you.

The value of the field.

 Restriction:
The Value box is unavailable for system fields since the value
is derived from your system.

Type coordinates to place the field label in a specified location.

SailWind Logic Guide

SailWind Logic GUI Reference
Add Field Dialog Box

Table  52. Add Field Dialog Box Fields  (continued)

Name

Description

 Tip
Leave these blank to attach the field to your pointer and click to
indicate the location.

Rotation

Line Width

Specifies the rotation of the text: 0 or 90 degrees.

Specifies the line width for stroke fonts only.

Size

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

Font Style

Enables you to change the font style to bold, italic, and underlined.

Font list

 Restriction:
System fonts only.

The fonts available to you. This lists either stroke fonts or system
fonts. You choose which type of font to use in the Fonts Dialog
Box.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles: B  for bold, I  for italic, or U  for
underlined.

Horizontal/Vertical Justification

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Related Topics
Adding a Field

SailWind Logic Guide

443

SailWind Logic GUI Reference
Add Free Text Dialog Box

## Add Free Text Dialog Box

To access: Schematic Editing toolbar > Create Text  button

Use the Add Free Text dialog box to add free text (not belonging to another object).

Figure 19. Add Free Text Dialog Box

Objects

Name

Text

X/Y

Rotation

Line Width

444

Table  53. Add Free Text Dialog Box Fields

Description

Type the text you want in the schematic.

Places the text in a specified location. Negative coordinates are
not permitted. If you want to place text outside the sheet, you must
move it there with the cursor.

 Tip
Leave these blank to attach the text to your pointer and click to
indicate the location.

Specifies the rotation of the text: 0 or 90 degrees.

Specifies the line width for stroke fonts only.

SailWind Logic Guide

Table  53. Add Free Text Dialog Box Fields  (continued)

Name

Description

SailWind Logic GUI Reference
Add Free Text Dialog Box

Size

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

Font Style

Enables you to change the font style to bold, italic, and underlined.

Font list

 Restriction:
System fonts only.

The fonts available to you. This lists either stroke fonts or system
fonts. You choose which type of font to use in the Fonts Dialog
Box.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles: B  for bold, I  for italic, or U  for
underlined.

Horizontal/Vertical Justification

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Related Topics
Adding Text

SailWind Logic Guide

445

SailWind Logic GUI Reference
Add Net to Class Dialog Box

## Add Net to Class Dialog Box

To access: With nothing selected, right-click > Select Nets  > select one or more nets > right-click > Make
Class  menu item

Use the Add Net to Class dialog box to create a new class or to add nets to an existing class.

Figure 20. Add Net to Class Dialog Box

Objects

Table  54. Add Net Class Dialog Box Fields

Name

Description

Create New Class

Specifies to create a new class using the selected net(s).

Add to Existing Class

Specifies to add the selected net(s) to an existing class.

Selected Nets

Add to Class

 Restriction:
This is unavailable if there are no existing classes.

Lists all of the nets you selected in the schematic.

Specifies the name of the class. Type a new name or accept the
default.

 Restriction:
This is unavailable if you select Add to Existing Class an only
one class exists.

Existing Classes

Lists all of the existing classes in the schematic.

446

SailWind Logic Guide

SailWind Logic GUI Reference
Add New Attribute Dialog Box

## Add New Attribute Dialog Box

To access: Edit  > Attribute Manager  menu item > Add Attr  button

Use the Add New Attribute dialog box to set name and value properties when adding new attributes to the
schematic.

Figure 21. Add New Attribute Dialog Box

Objects

Table  55. Add New Attribute Dialog Box Fields

Name

Description

Browse Lib. Attr  button

Opens the Browse Library Attributes Dialog Box.

Attribute Name

Attribute Value

The name of the new attribute.

The value of the new attribute.

Related Topics

Manage Attributes in a Schematic

SailWind Logic Guide

447

SailWind Logic GUI Reference
Add New Attribute to Library Dialog Box

## Add New Attribute to Library Dialog Box

To access: File  > Library  menu item > Library Manager dialog box > Attr Manager  button > Add Attr
button

Use the Add New Attribute to Library dialog box to set name and value properties when adding new
attributes to libraries.

Figure 22. Add New Attribute to Library Dialog Box

Objects

Table  56. Add New Attribute to Dialog Box Fields

Name

Description

Browse Lib. Attr  button

Opens the Browse Library Attributes Dialog Box.

Attribute Name

Attribute Value

The name of the new attribute.

The value of the new attribute.

448

SailWind Logic Guide

SailWind Logic GUI Reference
Add Part From Library Dialog Box

## Add Part From Library Dialog Box

To access: Schematic Editing toolbar > Add Part  button

Use the Add Part from Library dialog box to load a part from a library into the current schematic drawing.
SailWind Logic automatically assigns a reference designator when you add the part.

Figure 23. Add Part From Library Dialog Box

Objects

Table  57. Add Part From Library Dialog Box Fields

Name

Description

Preview area

Shows the selected item.

Items

Library list

Items

Apply  button

Part Name list

Lists the items in the selected library. The number of objects that
appear depends on the filter settings.

Specifies the library you want to use.

Narrows the search. You can use wildcards or expressions  on
page 105. An asterisk (*) displays all parts in the list.

Searches the library for the specified item.

Select a recently used part.

 Tip
The sixteen most recently used parts are available in the Part
Name dropdown list box. You can clear this buffer by removing
the entries in the SailWindlogic.ini  file, under the [Last Added
Parts] heading.

SailWind Logic Guide

449

SailWind Logic GUI Reference
Add Part From Library Dialog Box

Related Topics
Adding Parts

450

SailWind Logic Guide

SailWind Logic GUI Reference
Add Pins Dialog Box

## Add Pins Dialog Box

To access:

• File  > Library  menu item > select a Library > Parts  button > New  button > on the Part Editor

Toolbar click Edit Electrical  > Pins  tab > Add Pins  button

• File  > Library  menu item> select a Library > Parts  button > select a part > Edit  button > on the

Part Editor Toolbar click Edit Electrical  > Pins  tab > Add Pins  button

Use the Add Pins dialog box to add pins to a part type.

Figure 24. Add Pins Dialog Box

Objects

Name

Description

Table  58. Add Pins Dialog Box Fields

Number of pins

Specifies the number of pins to add using the Add Pins dialog box.

Prefix

The prefix you want for your pins.

 Tip

• Alphabetic and numeric values can be used. For example,

A1 or 1A.

• For a single numeric, use either Prefix or Suffix box, and

void the other box.

Suffix

The suffix you want for your pins.

SailWind Logic Guide

451

SailWind Logic GUI Reference
Add Pins Dialog Box

Table  58. Add Pins Dialog Box Fields  (continued)

Name

Description

 Tip

• Alphabetic and numeric values can be used. For example,

A1 or 1A.

• For a single numeric, use either Prefix or Suffix box, and

void the other box.

Pin numbers

A preview of pin numbers based on your input in the Prefix and
Suffix boxes.

Increment prefix/Increment suffix

Indicates whether you want the prefix or the suffix to increment.

Step value

A positive or negative number by which to increase or decrease
the pin numbers with consecutive or stepped values.

Verify valid JEDEC pin numbering Ensures that legal alphanumeric values are used.

452

SailWind Logic Guide

SailWind Logic GUI Reference
Archiver Dialog Box

## Archiver Dialog Box

To access: File  > Archive  menu item

Use the Archiver dialog box to create archives of your schematics, designs, files and folders, and
libraries.

Figure 25. Archiver Dialog Box

Objects

Name

PCB Design

Table  59. Archiver Dialog Box Fields

Description

Specifies the location and name of the PCB design you want to
archive. To choose the file you want, type the location or click the
Browse button.

Select Create PDF to create a PDF file of the PCB design.

SailWind Logic Guide

453

SailWind Logic GUI Reference
Archiver Dialog Box

Name

Schematic

Table  59. Archiver Dialog Box Fields  (continued)

Description

Specifies the location and name of the schematic file you want to
archive. This is automatically populated with the information from the
current design. To change the design, or if no design was opened, type
the location or click the Browse  button.

Specifies to create a PDF file of the schematic file.

 Restriction:
This is unavailable if the file you chose is different from the current
design.

Add libraries

Specifies that you want to include libraries in the archive.

Additional files

Target folder

• All  — Add all of your libraries to the archive.

• Select  — Add only the libraries you specify.

Click the Browse  button to open the Archiver Libraries Dialog Box.

Specifies that you want to include other files and folders in your
archive. Click the Browse  button to open the Archiver Additional Files
Dialog Box.

Specifies where you want the archive to be located. Type the path or
click the Browse  button.

Requirement:  The target folder must be empty.

Compress using zip format

Specifies to create a zip file. The file will be in the following format:

<project_name>YYYYMMDDHHMMSS.zip

Where YYYY is the year, MM is the month, DD is the day, HH is the
hour - in military time, MM is the minute, and SS is the second of the
exact time you created the file.

Related Topics

Archiving Your Schematic

454

SailWind Logic Guide

SailWind Logic GUI Reference
Archiver Additional Files Dialog Box

## Archiver Additional Files Dialog Box

To access: File  > Archive  menu item > Additional Files check box > Browse  button

Use the Archiver: Additional dialog box to add files and folders to the schematic you want to archive.

Figure 26. Archiver Additional Files Dialog Box

Objects

Table  60. Archiver Additional Fields Dialog Box

Name

Description

Additional files list

Lists the files and folders you want to include in your archive.

Add File  button

Add folder  button

Opens the Additional File dialog box where you can select individual
files you want to add to the Additional files list.

Opens the Browse for Folder dialog box where you can select an entire
folder to add to the Additional files list.

Remove  button

Removes the selected file or folder from the Additional files list.

Remove All  button

Removes all of the files and folders from the Additional files list.

Related Topics

Archiving Your Schematic

SailWind Logic Guide

455

SailWind Logic GUI Reference
Archiver Libraries Dialog Box

## Archiver Libraries Dialog Box

To access: File  > Archive  menu item > Add libraries check box > Select > Browse  button

Use the Archiver: Libraries dialog box to add libraries to the schematic you want to archive.

Figure 27. Archiver Libraries Dialog Box

Objects

Table  61. Archiver Libraries Dialog Box Fields

Name

Description

Available libraries

Lists all of the libraries available for you to add to the archive.

Add >>  button

<< Remove  button

Add all >>  button

 Restriction:
If your library is not listed in the Library Manager, it will not appear
in this list.

Moves the selected library from the Available libraries list to the
Selected libraries list.

Moves the selected library from the Selected libraries list to the
Available libraries list.

Moves all of the libraries from the Available libraries list to the Selected
libraries list.

<< Remove all  button

Moves all of the libraries from the Selected libraries list to the Available
libraries list.

456

SailWind Logic Guide

Related Topics

Archiving Your Schematic

SailWind Logic GUI Reference
Archiver Libraries Dialog Box

SailWind Logic Guide

457

SailWind Logic GUI Reference
ASCII Output Dialog Box

## ASCII Output Dialog Box

To access: File  > Export  menu item > type a filename > Save  button

Use the ASCII Output dialog box to select the sections you want to export to the ASCII file.

Figure 28. ASCII Output Dialog Box

Objects

Table  62. ASCII Output Dialog Box Fields

Name

Description

Schematic Params

Specifies to export the default system settings from the Options  tabs.

Sheet Params

Specifies to export the specific sheet information such as window
scale, centering, etc.

Text

Lines

Plot Params

Fields

Decals

Part Types

Specifies to export the free text together with location, level, and size.

Specifies to export the 2D-line items.

Specifies to export the information related to the CAM output settings
and configurations generated using the Plot command.

Specifies to export the fields used in the schematic and their values.

Specifies to export the part decals and their contents.

Specifies to export the library part attributes such as manufacturer,
cost, and notes.

458

SailWind Logic Guide

SailWind Logic GUI Reference
ASCII Output Dialog Box

Name

Parts

Connections

Rules

Table  62. ASCII Output Dialog Box Fields  (continued)

Description

Specifies to export the parts used in the schematic and their reference
designators.

Specifies to export all connections on the schematic, including paths,
tie-dots, and off-page flags.

Specifies to export the clearance, routing, and others specified in
Design Rules.

Select All  button

Selects all items.

Unselect All  button

Clears all items.

Output Version

Specifies the version of the software you are using.

Filename

Displays the location and name of the file.

 Tip
This was specified in the File Export dialog box.

Related Topics

Exporting to ASCII Output

SailWind Logic Guide

459

SailWind Logic GUI Reference
Assign Alternatives for Ground Part Dialog Box

## Assign Alternatives for Ground Part Dialog Box

To access: Tools  > Part Editor  menu item > Part Editor > Open  button > Ground > OK  button > Edit
Electrical  button

Use the Assign Alternatives for Ground Part dialog box to assign or create additional ground symbols.

Note:
For additional information on the creation and use of special schematic symbols, see “Special
Schematic Symbols”  on page 167.

Figure 29. Assign Alternatives for Ground Part Dialog Box

Objects

Name

Picture

Attribute table

Table  63. Assign Alternatives For Ground Part Dialog Box Fields

Description

Displays a picture of the selected Special Symbol.

• Special Symbol  — The name of a connector pin decal for use

in the schematic.

• Pin Type  — The function of the special symbol.

• Signal Name  — The name of the signal.

Opens the Browse for Special Symbols Dialog Box.

460

SailWind Logic Guide

SailWind Logic GUI Reference
Assign Alternatives for Ground Part Dialog Box

Table  63. Assign Alternatives For Ground Part Dialog Box Fields  (continued)

Name

Description

 Tip
This button is available only in the Special Symbols columns,
and only when the cell is available for editing.

Edit  button

Makes the selected cell available for editing.

 Tip
You can also double-click the cell to edit the contents.

Adds a new row at the bottom of the table.

Removes the selected row.

Add  button

Delete  button

Related Topics

Assigning Alternate Logic Decals for Connector Symbols

Special Schematic Symbols

SailWind Logic Guide

461

SailWind Logic GUI Reference
Assign Alternatives for Off-Page Part Dialog Box

## Assign Alternatives for Off-Page Part Dialog Box

To access: Tools  > Part Editor  menu item > Open  button > Off-page > OK  button > Edit Electrical
button

Use the Assign Alternatives for Off-Page Part dialog box to assign or create additional off-page reference
symbols.

Note:
For additional information on the creation and use of special schematic symbols, see “Special
Schematic Symbols”  on page 167.

Figure 30. Assign Alternatives for Off-Page Part Dialog Box

Objects

Name

Picture

Attribute table

Table  64. Assign Alternatives for Off-Page Part Dialog Box Fields

Description

Displays a picture of the selected Special Symbol.

• Special Symbol  — The name of a connector pin decal for use

in the schematic.

• Pin Type  — The function of the special symbol.

Opens the Browse for Special Symbols Dialog Box.

462

SailWind Logic Guide

SailWind Logic GUI Reference
Assign Alternatives for Off-Page Part Dialog Box

Table  64. Assign Alternatives for Off-Page Part Dialog Box Fields  (continued)

Name

Description

 Tip
This button is available only in the Special Symbols columns,
and only when the cell is available for editing.

Edit  button

Makes the selected cell available for editing.

 Tip
You can also double-click the cell to edit the contents.

Adds a new row at the bottom of the table.

Removes the selected row.

Add  button

Delete  button

Related Topics

Assigning Alternative Symbols for the Off-Page Part

Special Schematic Symbols

SailWind Logic Guide

463

SailWind Logic GUI Reference
Assign Alternatives for Power Part Dialog Box

## Assign Alternatives for Power Part Dialog Box

To access: Tools  > Part Editor  menu item > Open  button > Power > OK  button > Edit Electrical  button

Use the Assign Alternatives for Power Part dialog box to assign or create additional power symbols.

Note:
For additional information on the creation and use of special schematic symbols, see “Special
Schematic Symbols”  on page 167.

Figure 31. Assign Alternatives for Power Part Dialog Box

Objects

Name

Picture

Attribute table

Table  65. Assign Alternatives for Power Part Dialog Box Fields

Description

Displays a picture of the selected Special Symbol.

• Special Symbol  — The name of a connector pin decal for use

in the schematic.

• Pin Type  — The function of the special symbol.

• Signal Name  — The name of the signal.

Opens the Browse for Special Symbols Dialog Box.

 Tip
This button is available only in the Special Symbols columns,
and only when the cell is available for editing.

464

SailWind Logic Guide

Table  65. Assign Alternatives for Power Part Dialog Box Fields  (continued)

SailWind Logic GUI Reference
Assign Alternatives for Power Part Dialog Box

Name

Edit  button

Add  button

Delete  button

Related Topics

Description

Makes the selected cell available for editing.

 Tip
You can also double-click the cell to edit the contents.

Adds a new row at the bottom of the table.

Removes the selected row.

Assigning Alternative Symbols for the Power Part

Special Schematic Symbols

SailWind Logic Guide

465

SailWind Logic GUI Reference
Assign Decal to Gate Dialog Box

## Assign Decal to Gate Dialog Box

To access: Tools  > Part Editor  menu item > Edit Electrical  button > Gates  tab > (if a new part, click
Add) > double-click a CAE Decal cell > Browse  button

Use the Assign Alternatives for Power Part dialog box to assign or create additional power symbols.

Figure 32. Assign Decal to Gate Dialog Box

Objects

Name

Library list

Filter

Table  66. Assign Decal to Gate Dialog Box Fields

Description

Lists all your available libraries. Filters the Unassigned Decals list
to only the selected library.

Searches the chosen library (or libraries) for a specific part or item
name, or names that match a wildcard or expression  on page 105.
Type * to view all parts or items in the chosen libraries. Click Apply
to search the libraries and display the search results.

Preview area

Displays the item selected in the Assigned Decals list.

Unassigned Decals list

Lists all of the decals that are available to assign.

Assign New  button

Opens the Assign New Gate Decal Dialog Box.

Assign >>  button

<< Unassign  button

Moves the decal from the Unassigned Decals list to the Assigned
Decals list.

Moves the decal from the Assigned Decals list to the Unassigned
Decals list.

Assigned Decals list

Lists all of the decals that have been assigned.

466

SailWind Logic Guide

Table  66. Assign Decal to Gate Dialog Box Fields  (continued)

Name

Description

Up/Down  buttons

Moves the selected decal up or down in the Assigned Decals list.

SailWind Logic GUI Reference
Assign Decal to Gate Dialog Box

Related Topics

Assigning CAE Decals to Gates

SailWind Logic Guide

467

SailWind Logic GUI Reference
Assign New Gate Decal Dialog Box

## Assign New Gate Decal Dialog Box

To access: File  > Library  menu item > select a Library > Parts  button > select part > New  or Edit  button

> on Part Editor Toolbar click Edit Electrical  > Gates  tab > (if new part click Add) > double-click CAE
> Decal cell > Browse  button > Assign New

Use the Assign New Gate dialog box to assign a new gate decal when it doesn’t yet exist in the Library.

Figure 33. Assign New Gate Decal Dialog Box

Objects

Table  67. Assign New Gate Decal Dialog Box Fields

Name

Description

Text box

Enter the name of the new gate decal you intend to add to the library.

468

SailWind Logic Guide

SailWind Logic GUI Reference
Assign New PCB Decal Dialog Box

## Assign New PCB Decal Dialog Box

To access: File  > Library  menu item > select a Library > Parts  button > select part > New  or Edit  button

> on Part Editor Toolbar click Edit Electrical  > PCB Decals  tab > Assign New

Use the Assign New PCB Decal dialog box to assign a new PCB Decal when it doesn’t yet exist in the
Library.

Figure 34. Assign New PCB Decal Dialog Box

Objects

Table  68. Assign New PCB Decal Dialog Box Fields

Name

Description

Text box

Enter the name of the new PCB decal you intend to add to the library.

SailWind Logic Guide

469

SailWind Logic GUI Reference
Assign Shortcut Dialog Box

## Assign Shortcut Dialog Box

To access: Tools  > Customize  menu item > Keyboard and Mouse  tab > select a mode > select a
command folder > select a command > New  button

Create a new shortcut key using the Assign Shortcut dialog box.

Figure 35. Assign Shortcut Dialog Box

Objects

Table  69. Assign Shortcut Dialog Box Fields

Name

Description

Press new shortcut key

Type the shortcut you want to use.

Select a pointer event

Set a pointer event shortcut

Similar shortcuts list

Lists the shortcut keys already assigned to other commands.

470

SailWind Logic Guide

SailWind Logic GUI Reference
Attribute Properties Dialog Box

## Attribute Properties Dialog Box

To access: Select a part attribute label > right-click > Properties  menu item

Use the Attribute Properties dialog box to provide text and font settings for one or more part attribute
labels.

Figure 36. Attribute Properties Dialog Box

Objects

Name

Name

Value

Rotation

Size

Table  70. Attribute Properties Dialog Box Fields

Description

The name of the selected attribute.

Specifies the label you want in the schematic.

Specifies the rotation of the label: 0 or 90 degrees.

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

SailWind Logic Guide

471

SailWind Logic GUI Reference
Attribute Properties Dialog Box

Table  70. Attribute Properties Dialog Box Fields  (continued)

Name

Description

Line Width

Specifies the line width for stroke fonts only.

Font list

The fonts available to you. This lists either stroke fonts or system
fonts.

You choose which type of font to use in the Fonts Dialog Box.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles: B  for bold, I  for italic, or U  for
underlined.

Horizontal/Vertical Justification

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Related Topics

Modifying Part Attribute Labels

472

SailWind Logic Guide

SailWind Logic GUI Reference
Auto Renumber Parts Dialog Box

## Auto Renumber Parts Dialog Box

To access: Schematic Editing toolbar > Auto Renumber Parts  button

Automatically renumber the reference designators on schematic sheets in a pattern. Choose the sheets,
reference designator prefixes, pattern and numbering range.

Objects

Name

Sheets

Description

Choose which sheets to renumber.

Hierarchical sheets appear differently depending on whether they have been created
from the top down or the bottom up.

SailWind Logic Guide

473

SailWind Logic GUI Reference
Basic Script Editor

Name

Description

• Bottom-up  — Sheets display at the primary level instead of being indented in the
list. When using Increment Start Value by Sheet, the reference designators are
renumbered on each sheet.

• Top-down  — Sheets are indented to show they are sub-sheets. When using

Increment Start Value by Sheet, the sheets inherit the same base level number as
the parent sheet.

Prefix List

Cell size

Choose which reference designator families to renumber. The list displays the total
number of reference designators in brackets. The prefix types and totals update
based on the sheets selected in the Sheets list.

Renumbering is applied according to the Precedence pattern within the cell area.
Specify the size of cells in which to apply the renumbering pattern. Cells are arranged
across the schematic area in selected Precedence pattern. For an illustration
explaining cell size, see “Automatically Renumbering Reference Designators”  on
page 280.

Renumber

• Start Value  — The number to apply to the first of each type of renumbered

reference designator.

• Increment  — The gap in numbers to apply to the reference designator numbers.

• Increment Start Value by Sheet  — Use the sheet number as the start number

- the sheet number as shown in the Sheets Dialog Box  and not the order of the
  sheet in this dialog. For example, if the Start Value is 101, then sheet number
  1 will start with number 101, but sheet 2 will start with number 201. If used in
  combination with large start values, the reference designator numbers may quickly
  run into the software limit. For example, if the start value is set to 1000, and there
  are 40 schematic sheets, then reference designators on sheet 40 would start at
  40,000 - well over the limit of 32,766.

Start value and increment are applied to each reference designator family separately.
For example, the schematic has the following components: C1, C2, C3, R1, R2. Start
Value is 10 and Increment is 5. The result of renumbering is: C10, C15, C20, R10,
R15.Parts on sheets are renumbered in the order of the sheets: first, parts from sheet
number 1, then from sheet number 2 and so on. If a part belongs to more than one
sheet, it gets renumbered on the selected sheet with the lowest number.

Precedence

Specifies the pattern used to renumber parts within a cell area. Also specifies
the pattern used for the application of cells to process over the schematic page.
Renumbering is performed based upon the first pin of the symbol encountered in the
given precedence direction.

## Basic Script Editor

Basic is a simple scripting language. Like many Windows applications, such as Microsoft Word and Excel,
SailWind applications include Basic capabilities to enable users to customize their applications using a
standard scripting language.

You can use the Basic Script Editor to create, edit, run, and troubleshoot Basic scripts from SailWind
applications. To open the editor:

474

SailWind Logic Guide

SailWind Logic GUI Reference
Basic Script Editor

• Tools  > Basic Scripts  > Basic Script Editor  menu item

Figure 37. Basic Script Editor

SailWind Logic Guide

475

SailWind Logic GUI Reference
Basic Scripts Dialog Box

## Basic Scripts Dialog Box

To access: Tools  > Basic Scripts  > Basic Scripts  menu item

The Basic Scripts dialog box provides easy access to your Basic scripts.

Figure 38. Basic Scripts Dialog Box

Objects

Table  71. Basic Scripts Dialog Box Fields

Name

Description

Basic Script List

Lists the scripts available to you.

X  button

Specifies to use the smaller dialog box vs. the entire dialog box.

In Menu

Run  button

 Tip
To use the smaller dialog box, select the script you want to run and
press Enter.

Specifies to add the selected script to the Basic Scripts  menu.

Runs the selected script.

 Restriction:
You can not run multiple scripts at the same time.

 Tip
If the selected script has an error during compilation, it
automatically opens in the Basic Script editor for correction.

Edit  button

Opens the Sax Basic Engine dialog box with the selected script loaded.

See also Managing the Sax Basic Engine  on page 389

476

SailWind Logic Guide

SailWind Logic GUI Reference
Basic Scripts Dialog Box

Table  71. Basic Scripts Dialog Box Fields  (continued)

Name

Description

Load File  button

Adds a new script to the list.

 Tip

• You can load up to 32,767 scripts. Scripts are not compiled
when they are loaded; they are compiled when you run them
• The list of scripts you load into this dialog box is saved in the
VBScripts.ini  file, so they load every time you open the Basic
Scripts dialog box.

Unload  button

Removes the selected script from the list.

Description area

Displays the location of the selected script.

Related Topics

Using the Basic Scripts Dialog Box

SailWind Logic Guide

477

SailWind Logic GUI Reference
Bill of Materials Setup Dialog Box

## Bill of Materials Setup Dialog Box

The Bill of Materials report produces a user-configurable list of the parts contained in the current
schematic. You can direct any part attribute in the schematic to a Bill of Materials report.

Restriction:
Including non-ECO-registered parts and non-electrical parts in the bill of materials is constrained.
See Options Dialog Box, Design Category  for details.

To access: File  > Reports  menu item > Setup  button

Bill of Materials Setup Dialog Box, Attributes Tab
Bill of Materials Setup Dialog Box, BOM Config Tab
Bill of Materials Setup Dialog Box, Format Tab

478

SailWind Logic Guide

SailWind Logic GUI Reference

### Bill of Materials Setup Dialog Box, Attributes Tab

Bill of Materials Setup Dialog Box, Attributes Tab
To access: File  > Reports  menu item > Setup  button > Attributes  tab

Use the Attributes  tab to modify the Attribute content, the corresponding column headings, and column
width of the report. The attribute order in the content list determines the column arrangement in the BOM
report. There is a limit of 12 attributes in the Bill of Materials report.

Figure 39. Attributes tab

Objects

Name

Attribute table

Table  72. Bill of Materials Setup Dialog Box Fields

Description

Specifies the attributes in, headings for, and width of the BOM
report.

• Part Attribute column  — Specifies the attributes you want
in the report. You can list up to twelve attribute names. Each
attribute defines a column in the report.

• Field Header column  — Specifies the column heading for
each attribute in the report. You can specify any character
except the colon ( : ).

• Width column  — Specifies the number of characters across

the column for each attribute in the report: 1 to 200.

SailWind Logic Guide

479

SailWind Logic GUI Reference
Bill of Materials Setup Dialog Box, Attributes Tab

Table  72. Bill of Materials Setup Dialog Box Fields  (continued)

Name

Up  button

Description

Moves the selected row up by one.

 Tip
The attribute order in the content list determines the column
arrangement in the BOM report.

Down  button

Moves the selected row down by one.

 Tip
The attribute order in the content list determines the column
arrangement in the BOM report.

Add  button

Adds a row to the bottom of the table where you can select a new
part attribute.

 Tip
You can list up to twelve attribute names. Each attribute defines
a column in the BOM report.

Edit  button

Makes the selected box editable.

 Restriction:
You cannot edit the part attribute name, but you can select a
new attribute to replace the one currently listed.

Remove  button

Removes the selected row from the table and therefore the
attribute from the report.

Reset  button

Restores the default content from the .ini file.

Related Topics

The Bill of Materials Report

480

SailWind Logic Guide

SailWind Logic GUI Reference
Bill of Materials Setup Dialog Box, BOM Config Tab

### Bill of Materials Setup Dialog Box, BOM Config Tab

To access: File  > Reports  menu item > Setup  button > BOM Config  tab

Use the BOM Config  tab to preview the Bill of Materials report format and copy any selected lines of
the file to a Windows clipboard. You can also specify rows to export to a TXT/CSV file. The default view
orders the attributes by the sort field you specified on the Format  tab.

Figure 40. BOM Config Tab

Objects

Name

Report table

Table  73. Bill of Materials Setup Dialog Box-BOM Config Fields

Description

Remark

Displays the BOM report in table format for you to select and copy
any row or export to a CSV/TXT file. This table shows the data
from the attributes you selected on the Attributes tab.

Select All  button

Selects all rows in the table.

Use these functionality buttons to specify what and how to copy
selected rows to the Windows clipboard.

Copy  button

Specifies to copy the row(s) you’ve selected to the Windows
clipboard.

Include table header

Specifies to copy the table header in addition to the row(s) you’ve
selected.

Export  button

Exports the BOM report to a CSV/TXT file.

You can exclude the row(s) you don't want by checking the NC
checkbox.

Use these functionality buttons to specify what and how to export
allowable rows to a CSV/TXT file.

Combine Reference  button

Specifies to include reference designators sharing identical Part
Name in the same cell.

SailWind Logic Guide

481

SailWind Logic GUI Reference
Bill of Materials Setup Dialog Box, BOM Config Tab

Table  73. Bill of Materials Setup Dialog Box-BOM Config Fields  (continued)

Name

Description

Remark

Clear NC  button

Specifies to clear all the NC checkboxes selected in the table.

Related Topics

The Bill of Materials Report

482

SailWind Logic Guide

SailWind Logic GUI Reference
Bill of Materials Setup Dialog Box, Format Tab

### Bill of Materials Setup Dialog Box, Format Tab

To access: File  > Reports  menu item > Setup  button > Format  tab

Use the Format  tab to modify the output format of the Bill of Material report. The default settings originate
from the .ini  file.

Objects

Name

Delimiter area

Table  74. Bill of Materials Setup Dialog Box-Format Tab Fields

Description

Specifies the type of delimiter you want to distinguish the report
columns.

• None  — no delimiter used.

• Separator  — places a vertical bar between report fields.

• Tab  — separates columns with a tab spacing.

SailWind Logic Guide

483

SailWind Logic GUI Reference
Bill of Materials Setup Dialog Box, Format Tab

Table  74. Bill of Materials Setup Dialog Box-Format Tab Fields  (continued)

Name

Description

• Comma  — places a comma character between report fields.

• Custom  — specify any character as a delimiter.

File Format list

Specifies the output file format.

Reset  button

Settings list

Save As  button

Restores the default content from the .ini  file.

Specifies to use a previously saved report format setting.

Saves report format settings for the current design to a specified
file so you can create different format configurations for different
designs

Delete  button

Removes the selected setting in the Settings list.

Format Options area

Report Title

Specifies the title of the report.

Combine Value/Tolerance

Ref. Designator Separation Mode

Specifies to combine the Value and Tolerance attributes of a part
in the part name.

Example:  The 1/4 watt resistor would have a part type name of
R1/4W or R1/4W.4.7K,+/-5%. SailWind Logic evaluates parts that
have either a different Value or Tolerance attribute as different part
types.

• Single Ref. Designator per line  — Although some

components are identical, display each component instance on
a new line. This increases the BOM report size.

• Multiple Ref. Designator per line  — Combines identical
component instances on one line and lists all reference
designators based on the settings below:

• Compress Ranges  — Displays ranges of components

with a dash between min and max value. For example, if
components C1, C2, C3, and C4 are identical, they are
displayed as C1-4. This can shorten the list of reference
designators listed for a component type.

If you clear this check box, ranges are not compressed and
individual reference designators are listed for the line entry.
For example, C1,C2,C3,C4.

• Ref designator Delimiter  — Specify a single character
to place between multiple reference designators. For
example, use a comma for “C1,C2,C3”, or use an asterisk
for “C1*C2*C3”. Although you can type multiple characters in
this box, only the first character applies.

Sort By list

Specifies the attribute in which to sort the report list.

 Tip
Select None to sort by Part Type.

484

SailWind Logic Guide

SailWind Logic GUI Reference
Bill of Materials Setup Dialog Box, Format Tab

Related Topics

The Bill of Materials Report

SailWind Logic Guide

485

SailWind Logic GUI Reference
Browse for Connectors Dialog Box

## Browse for Connectors Dialog Box

To access: Tools  > Part Editor  menu item > Open  button > select Connector > OK  button

Use the Browse for Connectors dialog box to browse a library and select a connector for editing from the
library (or libraries) specified in the Library list.

Figure 41. Browse for Connectors Dialog Box

Objects

Name

Preview area

Part Types

Library list

Items

Table  75. Browse for Connectors Dialog Box Fields

Description

Shows the selected part.

Lists the items in the selected library. The number of objects that
appear depends on the filter settings.

Specifies the library you want to use.

Narrows the search. You can use wildcards or expressions  on
page 105. An asterisk (*) displays all parts in the list.

Apply  button

Searches the library for the specified item.

Related Topics

Browsing for Connectors

486

SailWind Logic Guide

SailWind Logic GUI Reference
Browse for Special Symbols Dialog Box

## Browse for Special Symbols Dialog Box

To access: Tools  > Part Editor  menu item > open an off-page part > Edit Electrical  button > double-click
in a field in the Special Symbols column > Browse  button

Use the Browse For Special Symbols dialog box to access the library for decals you want to specify
as Special Symbols. Special Symbols are those used to create off-page reference, power and ground
symbols, and connectors.

Figure 42. Browse for Special Symbols Dialog Box

Objects

Name

Preview area

Gate Decals

Library list

Items

Table  76. Browse for Special Symbols Dialog Box Fields

Description

Shows the selected item.

Lists the items in the selected library. The number of objects that
appear depends on the filter settings.

Specifies the library you want to use.

Narrows the search. You can use wildcards or expressions  on
page 105. An asterisk (*) displays all parts in the list.

Apply  button

Searches the library for the specified item.

Related Topics

Assigning Alternative Symbols for the Ground Part

Assigning Alternative Symbols for the Off-Page Part

SailWind Logic Guide

487

SailWind Logic GUI Reference
Browse for Special Symbols Dialog Box

Assigning Alternative Symbols for the Power Part

Assigning Alternate Logic Decals for Connector Symbols

488

SailWind Logic Guide

SailWind Logic GUI Reference
Browse Library Attributes Dialog Box

## Browse Library Attributes Dialog Box

To access: Tools  > Part Editor  menu item > Edit Electrical  button > Attributes  tab > Browse Lib. Attr
button

Use the Browse Library Attributes dialog box to browse and list all attribute names from libraries specified
in the Library List dialog box.

Figure 43. Browse Library Attributes Dialog Box

Objects

Name

Attribute

Group

Table  77. Browse Library Attributes Dialog Box Fields

Description

Displays the selected attribute.

Filters the attribute list. (Includes structured attributes.)

Refresh  button

Manually updates the attribute list if you change the list of libraries in
the Library Manager.

Related Topics

Browsing Library Attributes

SailWind Logic Guide

489

SailWind Logic GUI Reference
Bus Name Properties Dialog Box

## Bus Name Properties Dialog Box

To access: Select a bus name label > right-click > Properties  menu item

Use the Bus Name Properties dialog box to provide or change text and font settings for one or more bus
name labels.

Figure 44. Bus Name Properties Dialog Box

Objects

Name

Name

Bus  button

Rotation

Size

Table  78. Bus Name Properties Dialog Box FIelds

Description

The name of the selected bus.

Opens the Bus Properties Dialog Box.

Specifies the rotation of the label: 0 or 90 degrees.

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

490

SailWind Logic Guide

Table  78. Bus Name Properties Dialog Box FIelds  (continued)

Name

Description

SailWind Logic GUI Reference
Bus Name Properties Dialog Box

Line Width

Specifies the line width for stroke fonts only.

Font list

The fonts available to you.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles: B  for bold, I  for italic, or U  for
underlined.

Font Style

Enables you to change the font style to bold, italic, and underlined.

 Restriction:
System fonts only.

Horizontal/Vertical Justification

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Related Topics

Modifying Bus Name Labels

SailWind Logic Guide

491

SailWind Logic GUI Reference
Bus Properties Dialog Box

## Bus Properties Dialog Box

To access: Select a bus > right-click > Properties  menu item

Use the Bus Properties dialog box to change the name of the bus, change the bus type, and manage bus
nets.

Figure 45. Bus Properties Dialog Box

Objects

Name

Bus Name

Rename area

Bus Type area

Table  79. Bus Properties Dialog Box Fields

Description

Specifies the name of the bus. Select or type the name you want.

Specifies to rename this instance or all instances of the bus.

Specifies which bus names appear in the Bus Name list.

Add Bus Name Label

Select the Add Bus Name Label check box to add the bus name
as a label to the bus at the end of the bus closest to where you
selected it.

492

SailWind Logic Guide

Table  79. Bus Properties Dialog Box Fields  (continued)

Name

Description

 Tip

SailWind Logic GUI Reference
Bus Properties Dialog Box

Bus Nets table

• A bus can have two labels, one on each end.
• The check box is unavailable when the end of the selected

bus has a label.

• A bus label is not required.
• To delete a bus label, select the label in the schematic and

click the Delete  button on the standard toolbar.

Lists the name or prefix of the bus net, the starting bit number for
a sequence of nets, and the ending bit number for a sequence of
nets.

 Restriction:
Available only if the bus is a mixed net bus.

 Tip

• For a single net, type the net name.
• For a range of sequential nets, type the prefix for the

sequence of nets.

Add  button

Adds a row to the Bus Nets table.

 Restriction:
Available only if the bus is a mixed net bus.

Edit  button

Makes the selected row available for editing.

 Restriction:
Available only if the bus is a mixed net bus.

Delete  button

Removes the selected row from the Bus Nets table.

 Restriction:
Available only if the bus is a mixed net bus.

Down/Up  buttons

Moves the selected row up or down in the Bus Nets table.

 Restriction:
Available only if the bus is a mixed net bus.

Related Topics
Managing Buses

SailWind Logic Guide

493

SailWind Logic GUI Reference
CAE Decal Wizard Dialog Box

## CAE Decal Wizard Dialog Box

To access: Tools  > Part Editor  menu item > New  button > CAE Decal > OK  button > Decal Editing
Toolbar  button > CAE Decal Wizard  button

Use the Decal Wizard dialog box to automatically create a new CAE decal. You must be in the Decal
Editor mode of the Part Editor, and creating gate information, to use this feature.

Figure 46. CAE Decal Wizard Dialog Box

Objects

Table  80. CAE Decal Wizard Dialog Box contents

Name

Description

Preview area

Displays what the CAE decal looks like based on your settings.

Pin Length area

Sets the horizontal and vertical distance from the terminal connection
point to the decal outline.

Pin Spacing area

Sets the horizontal and vertical distance between pins.

Box Parameters area

Sets the width and height of the decal outline.

Left Pins area

 Tip

• Pin decals are moved left or right to accommodate the box

width.

• If you enter a value larger than needed to accommodate the

number of input or output pins, space is added to the bottom of
the decal.

Specifies the pin decal and pin count for the left, or input, side of the
part.

• Pin Decal  — Specifies the pin decal to use for this side.

• Pin Count  — Specifies the number of pins to use on this side.

Right Pins area

Specifies the pin decal and pin count for the right, or output, side of the
part.

494

SailWind Logic Guide

SailWind Logic GUI Reference
CAE Decal Wizard Dialog Box

Table  80. CAE Decal Wizard Dialog Box contents  (continued)

Name

Description

• Pin Decal  — Specifies the pin decal to use for this side.

• Pin Count  — Specifies the number of pins to use on this side.

Upper Pins area

Specifies the pin decal and pin count for the upper side of the part.

• Pin Decal  — Specifies the pin decal to use for this side.

• Pin Count  — Specifies the number of pins to use on this side.

Lower Pins area

Specifies the pin decal and pin count for the lower side of the part.

• Pin Decal  — Specifies the pin decal to use for this side.

• Pin Count  — Specifies the number of pins to use on this side.

Related Topics

Using the Decal Wizard

SailWind Logic Guide

495

SailWind Logic GUI Reference
Capture a New View Dialog Box

## Capture a New View Dialog Box

To access: View  > Save View  menu item > Capture  button

Use the Capture a New View dialog box to name the view you want to save.

Figure 47. Capture a New View Dialog Box

Objects

Name

Name

Table  81. Capture a New View Dialog Box contents

Description

Specifies the name you want for the view. View n  is the default name
where n  is the next number available.

 Tip
You can create up to nine views. The view names appear at the
bottom of the View  menu.

Related Topics

Saving and Restoring Views

496

SailWind Logic Guide

SailWind Logic GUI Reference
Change Part Type Dialog Box

## Change Part Type Dialog Box

To access: Select a part > right-click > Properties  > Change Type  button

Use the Change Part Type dialog box to change the selected part to a new part type. The new part type
can be one that already exists in the schematic or in the parts library. If multiple parts are selected, all of
the selected parts are changed.

Figure 48. Change Part Type Dialog Box

Objects

Name

Picture area

Part Types list

Table  82. Change Part Type Dialog Box Contents

Description

Displays the part selected in the Part Types list.

Lists all of the part types according to the filter settings.

Update attributes common to
design and library

Updates parts having common attributes with the attribute values
contained in the new part.

Preserve attributes in design not
present in library

Retains attributes that exist in the current part even though they do
not exist in the new part.

SailWind Logic Guide

497

SailWind Logic GUI Reference
Change Part Type Dialog Box

Table  82. Change Part Type Dialog Box Contents  (continued)

Name

Description

Apply update to area

Sets how parts are updated in the Apply update to area:

• This Gate  — Only updates the selected gate.

• Selected Gates  — Only updates the selected gates.

 Restriction:
Available only when multiple parts are selected.

• This Part  — Only updates a part or all associated gates of a

part.

• Selected Parts  — Only updates a part or all associated gates

of the selected parts.

 Restriction:
Available only when multiple parts are selected.

• All Parts This Type  — Updates all matching gates and/or parts

in the design.

 Restriction:
Unavailable when multiple parts are selected.

 Tip

• You can update the part definition in the schematic with a

modified version in the library. Select the same part name,
then click All Parts This Type in the Apply Update to Area.

• If you change a part type to one with fewer pins, the

connections going to the missing pins are not deleted. They
are attached to automatically generated off-page symbols.
You are notified of all disconnected pins.

Library list

Items

Specifies the library you want to use.

Narrows the search. You can use wildcards or expressions  on
page 105. An asterisk (*) displays all parts in the list.

Apply  button

Searches the library for the specified item.

Related Topics
Modifying Parts

498

SailWind Logic Guide

SailWind Logic GUI Reference
Check for Updates Dialog Box

## Check for Updates Dialog Box

To access: Help  > Check for Updates  menu item

Use the Check for Updates dialog box to manually check for a new version of SailWind, and to disable or
enable automatic checks.

Figure 49. Check for Updates Dialog Box

Objects

Table  83. Check for Updates Dialog Box contents

Name

Description

Check for Updates  button

Manually checks for a new version of the SailWind software.

Disable “Check for Updates”
functionality

Determines if SailWind automatically checks for a new version of the
software.

Click to stop SailWind from automatically checking for a new version
of the SailWind products; click to clear to have SailWind automatically
check for a new version.

Related Topics
SailWind Updates

SailWind Logic Guide

499

SailWind Logic GUI Reference
Class Rules Dialog Box

## Class Rules Dialog Box

To access: Setup  > Design Rules  menu item > Class  button

Use the Class Rules dialog box to define rules that apply to a collection of nets known as a net class and
to multiple net classes.

Figure 50. Class Rules Dialog Box

Objects

Name

Class Name

Class list

Table  84. Class Rules Dialog Box Contents

Description

Specifies the class name for which you want to apply rules.

Defines net classes by name and parenthetically notes the rules
that apply, if any, to the class.

Show Classes with Rules

Specifies to list only classes with at least one set of rule definitions.

Add  button

Delete  button

Adds a new Class Name to the Class list.

Removes the selected Class Name from the Class list.

Rename  button

Renames the selected Class Name in the Class list.

 Tip
Select the name in the list, type the new name in the Class
Name box and then click Rename.

500

SailWind Logic Guide

SailWind Logic GUI Reference
Class Rules Dialog Box

Table  84. Class Rules Dialog Box Contents  (continued)

Name

Description

Clearance  button

Opens the Clearance Rules Dialog Box.

Routing  button

Hi Speed  button

Report  button

Available list

Add>>  button

Opens the Routing Rules Dialog Box.

Opens the HiSpeed Rules Dialog Box.

Opens the Rules Report Dialog Box.

Lists all of the available nets for this Class.

Moves the net from the Available list to the Selected list.

<<Remove  button

Moves the net from the Selected list to the Available list.

Selected list

Default  button

Lists all of the selected nets for this Class.

Removes non-default rules from the selected nets, so that only
default rules apply.

SailWind Logic Guide

501

SailWind Logic GUI Reference
Clearance Rules Dialog Box

## Clearance Rules Dialog Box

To access: Setup  > Design Rules  menu item > a rule hierarchy button > Clearance  button

Use the Clearance Rules dialog box to define the spacing permitted between objects. When objects are
imported, the On-line DRC and Verify Design programs use these rules to check and report clearance
violations.

Figure 51. Clearance Rules Dialog Box

Objects

Table  85. Clearance Rules Dialog Box contents

Name

Description

Same Net area

Defines edge-to-edge clearance values between items that are in the
same net.

 Tip

• To define the minimum spacing between any two objects, type

the value in the corresponding text box.

• To define the same spacing value for all text boxes in one matrix
column, press the button above the column. Type a value and
click OK.

• To define the same spacing value for all text boxes in one matrix
row, press the button in the left column. Type a value and click
OK.

• To define the same spacing value for all text boxes in the matrix,

press the All  button. Type a value and click OK.

See also Same Net Matrix

Trace Width area

Specifies to restrict the trace width to a range of values.

502

SailWind Logic Guide

Table  85. Clearance Rules Dialog Box contents  (continued)

SailWind Logic GUI Reference
Clearance Rules Dialog Box

Name

Description

 Tip

• In the Recommended box, type the width you want to assign to

the trace when routing begins.

• In the Minimum and Maximum boxes, values are respected

by routing routines that must use trace width to achieve some
high-speed routing functions, such as impedance matching.

Clearance area

Defines edge-to-edge clearances between two object types:

• To define the minimum spacing between any two objects, type the

value in the appropriate text box.

• To define the same spacing value for all text boxes in one matrix
column, press the button above the column and type a value.

• To define the same spacing value for all text boxes in one matrix

row, press the button in the left column and type a value.

• To define the same spacing value for all text boxes in the matrix,

press the All  button and type a value.

Other area

Specifies other optional clearance values.

• Drill to Drill  — The minimum edge-to-edge spacing between two

drill holes.

• Body to Body  — The minimum edge-to-edge spacing between two

component bodies.

Delete  button

Removes this set of Clearance rules from your rules hierarchy.

 Tip
You cannot delete the Default Clearance rules.

Related Topics

Setting Up Clearance Rules

SailWind Logic Guide

503

SailWind Logic GUI Reference
Compare/ECO Tools Dialog Box

## Compare/ECO Tools Dialog Box

When you compare two versions of a design, you can create an output file that lists the differences
between the two versions. The report file is named Logic.rep  and is written to the \SailWind Projects
folder.

Restriction:
Transferring non-ECO-registered parts and non-electrical parts is constrained. See Options
Dialog Box, Design Category  for details.

To access: Tools  > Compare/ECO  menu item

Compare/ECO Tools Dialog Box, Documents Tab
Compare/ECO Tools Dialog Box, Comparison Tab

504

SailWind Logic Guide

SailWind Logic GUI Reference
Compare/ECO Tools Dialog Box, Documents Tab

### Compare/ECO Tools Dialog Box, Documents Tab

To access: Tools  > Compare/ECO  menu item > Documents  tab

Use the Documents  tab to specify the design netlists to compare and the files to create.

Tip
You can compare designs in any of the following forms:

• Schematic in memory
• Binary schematic file (.sch)
• PADS-format ASCII file (.asc)

Restriction:
Transferring non-ECO-registered parts and non-electrical parts is constrained. See Options
Dialog Box, Design Category  for details.

Figure 52. Compare/ECO Tools Dialog Box, Documents Tab

SailWind Logic Guide

505

SailWind Logic GUI Reference
Compare/ECO Tools Dialog Box, Documents Tab

Objects

Table  86. Compare/ECO Tools Dialog Box, Documents Tab Contents

Name

Description

Original Schematic Design to
Compare

New Current Schematic Design

Output Options

Generate ECO File

Related Topics

Specify the design you want to update. Do one of the following:

• Select Use Current Schematic Design to use the schematic in

memory as the original design.

• Clear Use Current Schematic Design, and then type or browse
to the original design file. The original design file format can
be binary (.sch) or PADS-format ASCII (.asc) output from the
schematic or layout.

 Restriction:
The original design cannot have the same filename as the new
design.

Specify the design containing the changes you want to place into
the original design. Do one of the following:

• Select Use Current Schematic Design to use the schematic in

memory as the new design.

• Clear Use Current Schematic Design, and then type or browse
to the new design file. The new design file format can be binary
(.sch) or PADS-format ASCII (.asc) output from the schematic
or layout.

 Restriction:
The new design cannot have the same filename as the original
design.

Specifies to create a report file containing a description of the
differences between the two design versions. This file is named
Logic.rep  and is stored in the \SailWind Projects  folder.

Specifies to create an ECO file. Type or browse to the ECO file.
The ECO file contains ECO commands that describe the changes
needed to update the original design to match the new design.

Forward Annotation From SailWind Logic to SailWind Layout

Backward Annotation From SailWind Layout to SailWind Logic

Contents of the Differences Report

506

SailWind Logic Guide

SailWind Logic GUI Reference
Compare/ECO Tools Dialog Box, Comparison Tab

### Compare/ECO Tools Dialog Box, Comparison Tab

To access: Tools  > Compare/ECO  menu item> Comparison  tab

Use the Comparison  tab to specify the design elements to include in the design netlists comparison.

Restriction:
Transferring non-ECO-registered parts and non-electrical parts is constrained. See Options
Dialog Box, Design Category  for details.

Figure 53. Compare/ECO Tools Dialog Box, Comparison Tab

Objects

Table  87. Compare/ECO Tools Dialog Box, Comparison Tab Contents

Name

Description

Comparison Options area

Compare Part Attributes

Comparison includes part attributes. Only part attributes are
compared and updated or reported. Each part receives attributes

SailWind Logic Guide

507

SailWind Logic GUI Reference
Compare/ECO Tools Dialog Box, Comparison Tab

Table  87. Compare/ECO Tools Dialog Box, Comparison Tab Contents  (continued)

Name

Description

from its corresponding Decal and Part Type, but modification is
performed only at the part level.

SailWind Logic categorizes parts that have different attributes as
different part types. Therefore, if you select Include Part Attributes
when you generate the netlist, you must also select Compare Part
Attributes when you perform an ECO comparison of that netlist.
Otherwise the comparison considers the part types to be different
and reports errors.

Compare Net Attributes

Comparison includes net attributes.

SailWind Logic categorizes nets that have different attributes
as different nets. Therefore, if you select Include Net Attributes
when you generate the netlist, you must also select Compare Net
Attributes when you perform an ECO comparison of that netlist.
Otherwise the comparison considers the net types to be different
and reports errors.

Compare PCB Decal Assignments Comparison includes PCB decal assignments.

Compare Design Rules

Comparison includes design rules. Only Default, Net, and Net
Class rules are compared. Rules on other objects in the original
design are preserved where possible.

Name Comparison Options area

Compare Net Names and
Reference Designators. Rename
as Necessary

Compare Net Names and
Reference Designators. Prefer
to Add or Delete Parts Instead of
Renaming

Compare differences using reference designators and net names.

Best used to minimize changes to routed traces. Selecting this
option may result in the positional swapping of parts.

Compare differences using reference designators and net names
on the basis that few reference designators have been renamed
and nets have not been renamed.

Best used to minimize the positional swapping of parts, and the
design disruption that may result.

Compare Connectivity and
Topology (not names). Rename
as necessary.

Compare differences without using reference designators or net
names. Compare differences using pin names, part type names,
and so on.

Best used to compare designs when parts and nets have been
renamed and minimal interconnect changes have been performed.

Unused Pins Net Name area

Ignore the Unused Pins Net

Select the check box and type the name of the unused pins net if
you want the design comparison to exclude the unused pins net in
the original design. The unused pins net contains pins that have no
logical net association. An unused pins net may be created in the
PCB design process.

 Restriction:
Specify a net name of 47 characters or less. Use any
alphanumeric characters except curly braces {}. asterisks *, or
spaces.

508

SailWind Logic Guide

SailWind Logic GUI Reference
Compare/ECO Tools Dialog Box, Comparison Tab

Table  87. Compare/ECO Tools Dialog Box, Comparison Tab Contents  (continued)

Name

Description

 Tip
If you clear this option and you update the PCB layout from
SailWind Logic, the unused pins net may be deleted.

Related Topics

Forward Annotation From SailWind Logic to SailWind Layout

Backward Annotation From SailWind Layout to SailWind Logic

Contents of the Differences Report

SailWind Logic Guide

509

SailWind Logic GUI Reference
Conditional Rule Setup Dialog Box

## Conditional Rule Setup Dialog Box

To access: Setup  > Design Rules  menu item > Conditional Rules  button

Once you set up Clearance rules for a group in the hierarchical order, the rules are applied to all other
objects. Use the Conditional Rule Setup dialog box to apply a third overriding set of rules that apply only
when the item meets other specific levels of the hierarchical order.

Tip
When setting up conditional rules, observe the following:

• You can use a layer as an against object, where rules you set for an object such as a net apply

only when the net is routed on that layer.

• You can further refine this to use another net as an against object and specify a layer to which
the rules to apply. If these two nets meet on this layer, they must adhere to this clearance. You
define these relationships by making conditional rule sets.

Figure 54. Conditional Rule Setup Dialog Box

510

SailWind Logic Guide

SailWind Logic GUI Reference
Conditional Rule Setup Dialog Box

Objects

Table  88. Conditional Rule Setup Dialog Box Contents

Name

Description

Source Rule Object area

Specifies the object you want to use to check rules. Choose
Classes, Nets, or All.

Against Rule Object area

Specifies which object to use to check the rules against. Choose
Layer, Classes, or Nets.

Apply to Layer list

Specifies the layer on which you want the rules to be checked.

Existing Rule Sets list

Lists rule sets that have already been created.

Current Rule Set area

Clearance

Object to Object

Matrix  button

High Speed

Specifies the minimum clearance gap you want the source and
against items to maintain from each other.

Opens the Clearance Rules Dialog Box.

Specifies the clearance values for parallel and tandem checking
for the condition. The source-against entries are used as the
victim-aggressor designations for crosstalk conditions checking.

For more information, see Setting Up High-Speed Rules.

Create  button

Compile the new rule set parameters and adds a description to the
Existing Rule Sets list box.

Delete  button

Removes the selected rule set from the Existing Rule Sets list box

SailWind Logic Guide

511

SailWind Logic GUI Reference
Connect to SailWind Layout Dialog Box

## Connect to SailWind Layout Dialog Box

To access: Tools  > SailWind Layout  menu item

Use the Connect to SailWind Layout dialog box to choose your connection to SailWind Layout. You can
then gain access to the SailWind Layout Link dialog box.

Figure 55. Connect to SailWind Layout Dialog Box

Objects

Table  89. Connect to SailWind Layout Dialog Box Contents

Name

Description

New  button

Opens and connects SailWind Logic to a new session of SailWind Layout then
opens the SailWind Layout Link Dialog Box.

 Tip
If there is a delay in launching and connecting to SailWind Layout, the Server
Busy Dialog Box  may appear. Wait a short time or till SailWind Layout appears
on your Windows Taskbar then click Retry.

Open  button

Opens and connects to an existing design file in a new SailWind Layout session
then opens the SailWind Layout Link Dialog Box.

 Tip
If a prompt window is open in SailWind Layout, the Server Busy Dialog Box
may appear. Click the Switch To  button and take care of the prompt to enable
SailWind Logic to connect to SailWind Layout.

512

SailWind Logic Guide

SailWind Logic GUI Reference
Connect to SailWind Router Dialog Box

## Connect to SailWind Router Dialog Box

To access: Tools  > SailWind Router  menu item

Use the Connect to SailWind Router dialog box to choose your connection to SailWind Router. You can
then gain access to the SailWind Router Link dialog box.

Figure 56. Connect to SailWind Router Dialog Box

Objects

Table  90. Connect to SailWind Router Dialog Box Contents

Name

Description

New  button

Opens and connects SailWind Logic to a new session of SailWind Router then
opens the SailWind Router Link Dialog Box.

 Tip
If there is a delay in launching and connecting to SailWind Router, the Server
Busy Dialog Box  may appear. Wait a short time or till SailWind Router appears
on your Windows Taskbar then click Retry.

Open  button

Opens and connects to an existing design file in a new SailWind Router session
then opens the SailWind Router Link Dialog Box.

 Tip
If a prompt window is open in SailWind Router, the Server Busy Dialog Box
may appear. Click the Switch To  button and take care of the prompt to enable
SailWind Logic to connect to SailWind Router.

SailWind Logic Guide

513

SailWind Logic GUI Reference
Crash Detected Dialog Box

## Crash Detected Dialog Box

To access: This dialog box is inaccessible unless the software crashes and crash detection is enabled in
the software .ini  file.

The Crash Detected dialog box opens at a crash and enables you to save a report of the SailWind
environment as well as pertinent files into a compressed SailWind Dump File for troubleshooting.

Objects

Name

Comments box

Attach BMW data check box

Save  button

Table  91. Crash Detected Dialog Box Contents

Description

You can describe what you were doing when the error occurred
or anything else you can think of that might help when
investigating the crash.

You can include BMW data and your project files. This will enable
customer support to play back what you were doing in your
design that led up to the crash. This check box is unavailable if
the BMW feature is not enabled.

See also BMW and BLT.

You must click the Save  button if you want to create a report file.
When you click the Save  button, you are prompted with a Save
As dialog box. The file that is created is called a Dump File and is
compressed in the .zip  format. This is the file that you must send
to customer support. It will include the report, the BMW data and
the project files.

514

SailWind Logic Guide

SailWind Logic GUI Reference
Create PDF Dialog Box

## Create PDF Dialog Box

To access: File  > Create PDF  menu item > enter filename > Save

You can create an intelligent PDF of your schematic, choosing which sheets you want to share and show
to others in your organization. You can create the PDF in full-color or black and white, with hyperlinks to
part attributes, and with search capabilities, making it easy to locate parts and nets. Once you locate a
net, you can find other instances of it through the entire schematic, even when the net is on a different
page. You can also create a black and white, non-searchable PDF of your schematic.

Restriction:
To search a PDF, you must substitute the Stroke font with a System font.

Tip
Adobe® Acrobat® Distiller™ is not required on your system to create a PDF.

See also Printing to PDF.

Figure 57. Create PDF Dialog Box

SailWind Logic Guide

515

SailWind Logic GUI Reference
Create PDF Dialog Box

Objects

Table  92. Create PDF Dialog Box Contents

Name

Description

Available list

List all of the sheets available to you.

Add >>  Button

Moves the selected sheet to the Sheets to PDF list.

Add All >>  Button

Moves all sheets to the Sheets to PDF list.

<< Remove  button

Moves the selected sheet to the Available list.

<< Remove All  Button

Moves all sheets to the Available list.

Sheets to PDF list

Lists the sheets you want to PDF.

View PDF after creation Specifies to open the PDF after it has been created.

Replace Stroke font with Specifies to replace the Stroke font with a system font. Select the font you

want from the list. Use the Font style buttons to add Bold, Italic, or Underline
styles.

 Restriction:

• You can only search a PDF if you replace the Stroke font with a

System font.

• There is no font size control. Text heights are already set for each text
item in the design. The height will be converted to the nearest point
size in the PDF.

Specifies to create a listing of the part attributes as a hyperlink.

Specifies to create a link to pan to the next instance of that net or bus.

 Restriction:
If the net name is not visible in the schematic, you will not be able to pan
through the nets.

Create hyperlinks
that will display part
attributes

Create hyperlinks that
will pan through nets

Visible rectangle around
objects with hyperlinks

Specifies to create all hyperlinks with visible boxes: yellow around the part
attributes, blue around the net and bus names.

 Restriction:
This check box is only available when one of the two check boxes above
it is clicked.

Color scheme area

Specifies the color scheme you want to use.

 Tip
The colors used in the Color on Black or Color on White schemes are
the same colors currently used in your schematic. The Black on White
scheme shows all currently visible items in the schematic in black.

516

SailWind Logic Guide

SailWind Logic GUI Reference
Customize Dialog Box

## Customize Dialog Box

Use the Commands  tab to add commands to menus or toolbars, or to create custom menus.

To access: Tools  > Customize  menu item

Customize Dialog Box, Commands Tab
Customize Dialog Box, Keyboard and Mouse Tab
Customize Dialog Box, Macro Files Tab
Customize Dialog Box, Options Tab
Customize Dialog Box, Toolbars and Menus Tab

SailWind Logic Guide

517

SailWind Logic GUI Reference
Customize Dialog Box, Commands Tab

### Customize Dialog Box, Commands Tab

To access: Tools  > Customize  menu item > Commands  tab

Use the Commands  tab to add commands to menus or toolbars, or to create custom menus.

Figure 58. Commands Tab

Objects

Name

Categories list

Commands list

Table  93. Command Tab Contents

Description

Narrows down the list of commands.

List of commands available to add to a menu or toolbar.

Add a new command, delete a command you’ve added, or rename
a command you’ve added.

Related Topics

Creating a Custom Command

Creating a Custom Menu

Defining Properties for a New Command

518

SailWind Logic Guide

Editing a Custom Command

Adding Items to Toolbars and Menus

SailWind Logic GUI Reference
Customize Dialog Box, Commands Tab

SailWind Logic Guide

519

SailWind Logic GUI Reference
Customize Dialog Box, Keyboard and Mouse Tab

### Customize Dialog Box, Keyboard and Mouse Tab

To access: Tools  > Customize  menu item > Keyboard and Mouse  tab

Create and customize shortcut keys using the Keyboard and Mouse  tab of the Customize dialog box.

Figure 59. Keyboard and Mouse Tab

Objects

Name

Mode list

Table  94. Keyboard and Mouse Tab Contents

Description

Narrows down the list of commands.

Commands list

The list of commands available for which to assign a shortcut.

Add a new command (opens the Add Command Dialog Box
on page 440), delete a command you’ve added, or rename a
command you’ve added (opens the Edit Command dialog box  on
page 440).

Current shortcuts list

The list of shortcuts assigned to the selected command.

Add a new shortcut (open the Assign Shortcut Dialog Box), or
delete a shortcut you’ve added.

Description

Lists what the selected command does.

520

SailWind Logic Guide

SailWind Logic GUI Reference
Customize Dialog Box, Keyboard and Mouse Tab

Table  94. Keyboard and Mouse Tab Contents  (continued)

Name

Description

Reset All  button

Report  button

Sets the selected toolbar or shortcut menu to the default settings.

Saves a report of all current shortcut commands.

SailWind Logic Guide

521

SailWind Logic GUI Reference

### Customize Dialog Box, Macro Files Tab

Customize Dialog Box, Macro Files Tab
To access: Tools  > Customize  menu item > Macro Files  tab

Create commands from macro files and add them to toolbars and menus using the Macro Files  tab.

Tip
To create a command from a macro command file, the macro command file (.mcr) must already
exist. You can create a macro by recording it in a SailWind tool or scripting it in Macro language.
For more information, see “Macros”  on page 47.

Figure 60. Macro Files Tab

Objects

Table  95. Macro Files Tab Contents

Name

Description

Macro Command Files list

The list of macro files you have opened.

Add a macro to the list (opens the Open Macro dialog box), delete
a macro from the list, or edit the location of a macro you’ve added.

Description

Lists what the selected macro does.

522

SailWind Logic Guide

SailWind Logic GUI Reference
Customize Dialog Box, Options Tab

### Customize Dialog Box, Options Tab

To access: Tools  > Customize  menu item > Options  tab

Customize the SailWind interface by changing the appearance of menus and toolbars using the Options
tab of the Customize dialog box.

Figure 61. Options Tab

Objects

Name

Description

Table  96. Options Tab Contents

Show ToolTips on toolbars

Displays the button name over the toolbar button when you hover
over it with your pointer.

Show shortcuts in ToolTips

In addition to the name in the ToolTip, displays the shortcut for the
button.

Large Icons

Displays icons on the toolbar larger than the default size.

Menu animations list

The type of animation for your menus: None, Unfold, Slide, or
Fade.

Menu shadows

Displays a shadow behind the menu.

SailWind Logic Guide

523

SailWind Logic GUI Reference
Customize Dialog Box, Options Tab

Table  96. Options Tab Contents  (continued)

Name

Description

Wait until <Enter> before
executing long shortcuts

Show recent commands first

Delays the execution of shortcut keys until you press Enter.

Displays your recent menu command selections at the top of the
list.

Show full menus after delay

Displays the full menu after a slight pause.

Reset my usage data button

Restores the default set of commands to the menus and toolbars.

 Tip
This option does not undo any explicit customizations you
made.

Visual Style

Sets the look and feel of your toolbars and title bars.

Interface Language

Specifies the language for all dialog boxes and messages
displayed: English, Chinese Simplified.

Related Topics

Customized Appearance of the Screen

524

SailWind Logic Guide

SailWind Logic GUI Reference
Customize Dialog Box, Toolbars and Menus Tab

### Customize Dialog Box, Toolbars and Menus Tab

To access: Tools  > Customize  menu item > Toolbars and Menus  tab

Use the Toolbars and Menus  tab on the Customize dialog box to create custom toolbars and shortcut
menus.

Tip
To create a custom main menu, use the Commands  tab on the Customize dialog box. See
Creating a Custom Menu.

Figure 62. Toolbars and Menus Tab

Objects

Name

Toolbars list

Table  97. Toolbars and Menus Tab Contents

Description

Specify which toolbars to display in the main window.

Add a new toolbar, delete a toolbar you’ve added, or rename a
toolbar you’ve added.

Show text labels

Shows the text label on the button in addition to the icon.

Select shortcut menus

Specifies the shortcut menu you want to customize.

SailWind Logic Guide

525

SailWind Logic GUI Reference
Customize Dialog Box, Toolbars and Menus Tab

Table  97. Toolbars and Menus Tab Contents  (continued)

Name

Description

 Restriction:
SailWind Router only.

Reset  button

Reset All  button

Sets the selected toolbar or shortcut menu to the default settings.

Sets all toolbars or shortcut menus back to their default settings.

Related Topics

Customizing the SailWind Interface

526

SailWind Logic Guide

SailWind Logic GUI Reference
DC Source Sweep Analysis Dialog Box

## DC Source Sweep Analysis Dialog Box

To access: Tools  > SPICE Netlist  menu item > Simulation Setup  button> DC Sweep  button

Use the DC Source Sweep Analysis dialog box to set options specifically for a DC Sweep analysis.

Figure 63. DC Source Sweep Analysis Dialog Box

Objects

Name

Source

Start

End

Step

Table  98. DC Source Sweep Analysis Dialog Box Contents

Description

Specifies the name of the voltage or current source.

Specifies the starting voltage for the sweep.

Specifies the stopping voltage for the sweep.

Specifies the incrementing values for the sweep.

Related Topics

Creating a SPICE Netlist

Setting Up DC Source Sweep Analysis

SailWind Logic Guide

527

SailWind Logic GUI Reference
Default Rules Dialog Box

## Default Rules Dialog Box

To access: Setup  > Design Rules  menu item > Default  button

Use the Default Rules dialog box to define rules which apply to all objects that are not included in any
other rule within the hierarchy.

Figure 64. Default Rules Dialog Box

Objects

Table  99. Default Rules Dialog Box Contents

Name

Description

Clearance  button

Opens the Clearance Rules Dialog Box.

Routing  button

Hi Speed button

Report  button

Opens the Routing Rules Dialog Box.

Opens the HiSpeed Rules Dialog Box.

Opens the Rules Report Dialog Box.

528

SailWind Logic Guide

SailWind Logic GUI Reference
Differential Pairs Dialog Box

## Differential Pairs Dialog Box

To access: Setup  > Design Rules  menu item > Differential Pairs  button

Use the Differential Pairs dialog box to identify nets or pin pairs that behave electrically as differential
pairs, and to define differential pair design rules.

Figure 65. Differential Pairs Dialog Box

Objects

Name

Available list

Table  100. Differential Pairs Dialog Box Contents

Description

Lists nets that have not been assigned to a differential pair.

SailWind Logic Guide

529

SailWind Logic GUI Reference
Differential Pairs Dialog Box

Table  100. Differential Pairs Dialog Box Contents  (continued)

Name

Selected list

Description

Lists the nests that have been selected.

 Tip
Click Add  to move the selected nets to the Pairs list.

Select >>  button

Moves the selected net to the Selected list.

<<Unselect  button

Moves the net that was previously selected back to the Available
list.

Add>>  button

Moves the two nets in the Selected list to the Pairs list.

<<Remove  button

Moves the two nets in the Pairs list to the Available list.

Pairs list

Lists the differential pairs.

Trace length area

Specifies the minimum and maximum trace length values.

Restrict layer changes during
autorouting

Forces the pair to be routed on a single layer.

 Tip
This setting does not restrict layer changes when routing
interactively.

Properties of the pair table

Sets the width and gap per layer.

Add  button

Delete  button

Obstacles area

Adds a row to the Properties of the pair table.

Removes the selected row from the Properties of the pair table.

Specifies to allow routing around an obstacle in the controlled gap
area by temporarily exceeding the pair routing gap.

 Tip
This setting applies to autorouting and does not restrict splitting
around obstacles when routing interactively.

Also specifies the maximum number of obstacles and the
maximum obstacle size.

 Tip
Obstacles in the start zone  or end zone  are not counted.

Report  button

Opens the Rules Report Dialog Box.

530

SailWind Logic Guide

SailWind Logic GUI Reference
Display Colors Dialog Box

## Display Colors Dialog Box

To access: Setup  > Display Colors  menu item

Use the Display Colors Setup dialog box to Set display colors, save them, and restore them; Change the
color palette; make objects visible; and make objects invisible.

Tip
Changes you make to the color configuration in the Display Colors Setup dialog box do not apply
to disabled layers.

Figure 66. Display Colors Setup Dialog Box

SailWind Logic Guide

531

SailWind Logic GUI Reference
Display Colors Dialog Box

Objects

Table  101. Display Colors Setup Dialog Box Contents

Name

Description

Selected Color area

Select a color from the palette to assign to items on a layer. Once
you select a color here, click the tile in the Color by Layer area of
the item to which you want to assign the color.

Palette  button

Opens the Color dialog box where you can choose to use new
colors or customize colors you want to use.

Default Palette  button

Reassigns all colors and settings to the default settings.

Misc area

Titles area

 Tip
You can change the default settings by saving a configuration
and naming it default.

Apply a color to objects in the Misc area to change the color of that
object in the workspace.

To make a text string visible in the part editor, select the check box
beside the string type in the Titles area.

Configuration list

The list of saved configurations.

Save  button

Delete  button

Opens the Save Configuration Dialog Box.

Removes the selected configuration from the Configuration list.

Related Topics

Display Colors Dialog Box - Part Editor

Setting Display Colors

532

SailWind Logic Guide

SailWind Logic GUI Reference
Display Colors Dialog Box - Part Editor

## Display Colors Dialog Box - Part Editor

To access: In the Part Editor, Setup  > Display Colors  menu item

Use the Display Colors dialog box while in the Part Editor or the CAE Decal Editor to control the colors
of objects and the working area. SailWind Logic saves the color settings for part editor items with the
schematic. This dialog box is similar to the one used in the schematic editor, with check boxes to display
text items.

Figure 67. Display Colors Dialog Box in the Part Editor

Objects

Name

Selected Color

Palette  button

Table  102. Display Colors Dialog Box contents

Description

Select a color in this area to apply to tiles in the Items area.

Click to open the Color dialog box where you can specify new
colors or customize colors that appear in the Selected Color area.

Default Palette  button

Click Default Palette to restore the default color settings in the
Selected Color area.

 Tip
Refer to the Microsoft Windows Help for more information
about changing the Color Palette.

Background

Apply a color to this color tile to change the background color or
work area surface in the Part Editor workspace.

SailWind Logic Guide

533

SailWind Logic GUI Reference
Display Colors Dialog Box - Part Editor

Table  102. Display Colors Dialog Box contents  (continued)

Name

Selections

Items area

Description

 Tip

• To make an item invisible, set it to the background color.
• The color selection for displaying items or making them

invisible does not affect plotting of the schematic.

Apply a color to this color tile to change the color of objects that
you select in the workspace.

Apply a color to objects in the Items area to change the color of
that object in the workspace.

 Tip
Some of the items have a color setting in the Box column. Box
indicates the color of the box that is drawn around the text item.
This box serves two purposes: it indicates the exact size of the
text item when it is plotted, thereby helping you avoid overlaps
while moving the item; and it provides visibility of the text item
at very small zoom levels.

Names area

To make a text string visible in the part editor, select the check box
beside the string type in the Names area.

 Restriction:

• This area is only available when editing a CAE decal, pin

decal, or when editing the graphics of individual connector,
or off-page type symbols.

• When editing a CAE decal - Sheet Number is unavailable.
• When editing a pin decal - Reference Designator, Part-Type
Name, Attribute Labels, and Sheet Number are unavailable.
• When editing the pin decal of an off-page, power or ground
symbol - only Netnames and Sheet Number are available.
• When editing the graphics of a single connector pin - only
Ref Designator, Part-Type Name, and Attribute Labels are
available.

534

SailWind Logic Guide

SailWind Logic GUI Reference
Drafting Properties Dialog Box

## Drafting Properties Dialog Box

To access: Select a drafting object > right-click > Properties  menu item

Use the Drafting Properties dialog box to modify the line width, style, and orientation of selected drafting
objects.

Figure 68. Drafting Properties Dialog Box

Objects

Field

Width

Table  103. Drafting Properties Dialog Box Contents

Description

Specifies the line width for the drafting object. The current line width of the
selected drafting object is automatically displayed, change it if necessary.

 Tip
Use the Line Widths  tab in the Options dialog box to change the
default line width.

Filled

Specifies to create a filled shape from a selected polygon.

 Tip
This option is grayed for circles, paths, and if you used Pull Arc to
modify the polygon.

Style area

Specifies the line style option for the selected drafting object: Solid or
Dotted.

Rotation

Specifies the degree of rotation from the Rotation list.

 Tip

• Rotation can be 0 or 90 degrees.
• The point used when selecting the object is the also the point of

rotation.

Mirror by X

Specifies to mirror the selected drafting object in the X (horizontal)
direction.

Mirror by Y

Specifies to mirror the selected drafting object in the Y (vertical) direction.

SailWind Logic Guide

535

SailWind Logic GUI Reference
Drafting Properties Dialog Box

Related Topics

Modifying Drafting Objects

536

SailWind Logic Guide

SailWind Logic GUI Reference
Edit Button Image Dialog Box

## Edit Button Image Dialog Box

To access: Tools  > Customize  menu item > Commands  tab > New  button > Select User-Defined Image

> New  or Edit  button

Use the Edit Button Image dialog box to create or edit button icons.

Figure 69. Edit Button Image Dialog Box

Objects

Field

Colors area

Tools area

Table  104. Edit Button Image Dialog Box Contents

Description

Select a color to use with the tools

Select a tool to draw/edit the picture or icon of the button

SailWind Logic Guide

537

SailWind Logic GUI Reference
Fields Dialog Box

## Fields Dialog Box

To access: Select nothing or a 2D line object > right-click > Fields  menu item

Use the Fields dialog box to manage multiple fields. You can manage the fields in the entire schematic or
in a 2D line object.

Figure 70. Fields Dialog Box

Objects

Field

System

Table  105. Fields Dialog Box Contents

Description

Displays the name and value for all system fields in the design.

Delete  button

Removes the selected row.

User

Add  button

 Restriction:
System fields can be deleted from 2D line items only.

Displays the name and value for all user fields in the design

Inserts a row at the bottom of the list where you can add a new field.

Delete  button

Removes the selected row.

Edit  button

Makes the selected cell available for editing.

538

SailWind Logic Guide

SailWind Logic GUI Reference
Fields Dialog Box

Table  105. Fields Dialog Box Contents  (continued)

Field

Description

 Tip
You can also double-click a cell to edit the contents.

Related Topics
Managing Fields

SailWind Logic Guide

539

SailWind Logic GUI Reference
Field Properties Dialog Box

## Field Properties Dialog Box

To access: Select a field > right-click > Properties  menu item

Use the Field Properties dialog box to modify a field name or change its text size, orientation, or
justification.

Figure 71. Field Properties Dialog Box

Objects

Name

Name

Value

X/Y

Rotation

Line Width

540

Table  106. Field Properties Dialog Box Contents

Description

The name of the field. Type a new or select an existing field name
to change it.

Specifies the text you want in the schematic.

Type coordinates to place the text in a specified location.

Specifies the rotation of the text: 0 or 90 degrees.

Specifies the line width for stroke fonts only.

SailWind Logic Guide

Table  106. Field Properties Dialog Box Contents  (continued)

Name

Description

SailWind Logic GUI Reference
Field Properties Dialog Box

Size

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

Font Style

Enables you to change the font style to bold, italic, and underlined.

Font list

 Restriction:
System fonts only.

The fonts available to you. This lists either stroke fonts or system
fonts. You choose which type of font to use in the Fonts Dialog
Box.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles: B  for bold, I  for italic, or U  for
underlined.

Horizontal/Vertical Justification

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Related Topics
Modifying Fields

Add Field Dialog Box

SailWind Logic Guide

541

SailWind Logic GUI Reference
Font Replacement Dialog Box

## Font Replacement Dialog Box

To access: When you open a design created with fonts that are not installed on your system, the Font
Replacement dialog box opens automatically.

Use the Font Replacement dialog box to manage how missing fonts are replaced in your design.

Tip
If the design uses fonts or character sets that are not installed on your system, empty boxes will
appear where you expect to find text or symbols. Once the font replacement process completes,
the symbols display properly.

Figure 72. Font Replacement Dialog Box

Objects

Name

Mode

Table  107. Font Replacement Dialog Box Contents

Description

Specifies the mode to replace this font.

• Automatic  — Specifies to replace the font automatically with

the one selected by SailWind Layout.

• Manual  — Specifies to replace the font with one you select

from the Replace with font list.

• Skip  — Specifies to preserve the original font.

542

SailWind Logic Guide

Table  107. Font Replacement Dialog Box Contents  (continued)

SailWind Logic GUI Reference
Font Replacement Dialog Box

Name

Missing font

Replace with font

Description

The name of the font in this design that is missing from your
system.

If you chose Manual, lists the fonts available for you to replace the
missing font.

If you chose Automatic, lists the font SailWind Layout chose to
replace the missing font.

Tip
When replacing fonts, observe the following:

• You can select some fonts for automatic replacement, select others for manual replacement,

and choose that other font replacements be skipped entirely.

• You can have a combination of stroke font and system fonts within the same design.
• You must set up fonts for each text string and/or label you create in your design. Once you set

up fonts for a text string or label, you can then use the Properties dialog to apply a font and font
characteristics to all objects that you select for modification with the Properties dialog box.

Restriction:
When working with fonts note the following restrictions:

• If the design uses fonts or character sets that are not installed on your system, a font

substitution process begins automatically when the file is loaded. During this process, you are
asked to choose fonts to substitute for those that are missing from your system.

• System font text is supported in RS274X Gerber format when Fill mode is on. System font text

is output to Gerber format as a set of filled polygons.

• System fonts are not supported in the RS-274D CAM output format. If you attempt to use this
format with system fonts, the program displays a warning message. If you proceed, system
fonts will not be output. Instead, you should use the 274X format with system fonts.

• Type 1 fonts are not supported.

Related Topics

Managing Font Replacement

SailWind Logic Guide

543

SailWind Logic GUI Reference
Fonts Dialog Box

## Fonts Dialog Box

To access: Setup  > Fonts  menu item

Use the Fonts dialog box to set up or change the fonts to be used in your design.

Restriction:
If the schematic uses fonts or character sets that are not installed on your system, a font
substitution process begins automatically when the file is loaded. During this process, you are
asked to select fonts to substitute for those that are missing from your system.

Tip
If you want to change font sizes, see Modifying Part Type Labels.

Figure 73. Fonts Dialog Box

Objects

Name

Font Style

Table  108. Fonts Dialog Box Contents

Description

The fonts available to you:

• Stroke

• System

Default Font list

Specifies the system font you want to use.

 Tip
You can also click a font style button, or any combination of
styles: B  for bold, I  for italic, or U  for underlined.

Related Topics
Setting Fonts

544

SailWind Logic Guide

SailWind Logic GUI Reference
Get Drafting Items From Library Dialog Box

## Get Drafting Items From Library Dialog Box

To access: Schematic Editing toolbar > Add 2D Line from Library  button

Use the Get Drafting Item from Library dialog box to load a 2D line item from the available libraries to the
current schematic.

Figure 74. Get Drafting Items From Library Dialog Box

Objects

Table  109. Get Drafting Items From Library Dialog Box Contents

Field

Description

Preview area

Displays the selected gate decal

Drafting Items

Lists the drafting items available based on the filter settings.

Library list

Items

Specifies the library you want to use.

Narrows the search. You can use wildcards or expressions  on page 105.
An asterisk (*) displays all parts in the list.

Apply  button

Searches the library for the specified item.

Related Topics

Adding Drafting Items From a Library

SailWind Logic Guide

545

SailWind Logic GUI Reference
Get Gate Decal From Library Dialog Box

## Get Gate Decal From Library Dialog Box

To access: Tools  > Part Editor  menu item > Open  button > Select CAE Decal > OK  button

Use the Get Gate Decal from Library dialog box to open an existing CAE Decal in the Part Editor.

Figure 75. Get Gate Decals From Library Dialog Box

Objects

Table  110. Get Gate Decals From Library Dialog Box Contents

Field

Description

Preview area

Displays the selected gate decal

Gate Decals

Lists the gate decals available based on the filter settings.

Library list

Items

Specifies the library you want to use.

Narrows the search. You can use wildcards or expressions  on page 105.
An asterisk (*) displays all parts in the list.

Apply  button

Searches the library for the specified item.

Related Topics

Getting Gate Decals From the Library

546

SailWind Logic Guide

SailWind Logic GUI Reference
Get PCB Decal From Library Dialog Box

## Get PCB Decal From Library Dialog Box

To access: Select a part > right-click > Properties> PCB Decals button > Browse  button

Use the Get PCB Decal from Library dialog box to search a library for a PCB decal.

Figure 76. Get PCB Decal From Library Dialog Box

Objects

Name

Picture Area

Decals

Library list

Filter

Table  111. Get PCB Decal From Library Dialog Box Contents

Description

Displays the PCBdecal highlighted in the Decals area.

Lists the available PCB decals in the selected library or all libraries.

Lists the libraries available to you.

Searches the chosen library (or libraries) for a specific part or item
name, or names that match a wildcard or expression  on page 105.
Use the Library dropdown list to select specific library directories
or the All Libraries setting. Type * to view all parts or items in the
chosen libraries. Click Apply  to search the libraries and display the
search results.

Related Topics

Searching the Library for a Decal

SailWind Logic Guide

547

SailWind Logic GUI Reference
Hierarchical Symbol Wizard Dialog Box

## Hierarchical Symbol Wizard Dialog Box

To access: Schematic Editing toolbar > New Hierarchical Symbol  button

Use the Hierarchical Symbol Wizard dialog box to create a new hierarchical symbol in either a top-down
or bottom-up design structure. The symbol creation methodology varies, depending on the structure you
use.

Figure 77. Hierarchical Symbol Wizard Dialog Box

Objects

Name

Preview

Pin Parameters area

Table  112. Hierarchical Symbol Wizard Dialog Box Contents

Description

Displays the symbol outline before the symbol appears in the Part Editor.
Display is based on the current settings.

• Pin Length  — Sets the distance from the terminal connection point

and the decal outline. This option does not adjust the length of the pin
decal.

• Pin Spacing  — Specifies the spacing between adjacent pins.

Box Parameters area

• Box Width  — Sets the width of the decal outline. Pin decals are

moved left or right to accommodate the box width.

• Min Box Hgt.  — Sets the minimum height of the decal outline. If you

enter a value larger than needed to accommodate the number of input
or output pins, space is added to the bottom of the decal.

 Tip
Type values or use the arrow buttons.

Input Pins area

• Pin Decal  — Specifies the type of pin decal.

• Pin Count  — Specifies the number of input pins for a hierarchical

symbol of a new sheet during top-down design.

 Tip
Type values or use the arrow buttons.

548

SailWind Logic Guide

SailWind Logic GUI Reference
Hierarchical Symbol Wizard Dialog Box

Table  112. Hierarchical Symbol Wizard Dialog Box Contents  (continued)

Name

Description

Output Pins area

• Pin Decal  — Specifies the type of pin decal.

• Pin Count  — Specifies the number of output pins for a hierarchical

symbol of a new sheet during top-down design.

 Tip
Type values or use the arrow buttons.

Hierarchical Sheet area

• Sheet Number  — Lists the sheets in the set or lists only the <New

Sheet> option for top-down design.

 Restriction:
For bottom-up design, this list never displays the current sheet
since you can place the symbol that represents the current sheet
on the current sheet.

• Sheet-name  — Specifies the name of the hierarchical symbol.

 Restriction:

◦ Sheet Name has a maximum of 37 characters.
◦ You can only use the first 32 characters for the textual portion of
the name, the remaining five are reserved for the numeric potion.

Related Topics

Creating a Top-Down Hierarchy

Creating a Bottom-Up Hierarchy

SailWind Logic Guide

549

SailWind Logic GUI Reference
HiSpeed Rules Dialog Box

## HiSpeed Rules Dialog Box

To access: Setup  > Design Rules  menu item > a rule hierarchy button > HiSpeed  button

Use the HiSpeed Rules dialog box to define rules for Parallelism, Tandem, Shielding, Routed Length,
Stub Length, Delay, Capacitance, Impedance, and Matched Length.

Tip
When working with HiSpeed Rules, observe the following:

• When imported into SailWind, the EDC (Electrodynamic Checking) routine checks to see if

rules are met correctly after routing (except shielding and matched length).

• You can use the Conditional Rule Setup Dialog Box  to save a high speed configuration as

a set, or to apply for a selected item only when it comes in contact with different level of the
hierarchical order  on page 305.

Figure 78. HiSpeed Rules Dialog Box

Objects

Name

Parallelism

Table  113. HiSpeed Rules Dialog Box contents

Description

Restricts the distance that traces in different nets on the same layer
can run together.

 Tip

• Length defines the maximum allowable parallel/tandem

distance.

• Gap defines the minimum gap between traces below which the

parallel/tandem rules apply.

Tandem

Restricts the distance that traces in different nets on different layers
can run together.

550

SailWind Logic Guide

Table  113. HiSpeed Rules Dialog Box contents  (continued)

SailWind Logic GUI Reference
HiSpeed Rules Dialog Box

Name

Description

 Tip

• Length defines the maximum allowable parallel/tandem

distance.

• Gap defines the minimum gap between traces below which the

parallel/tandem rules apply.

Aggressor

Specifies if a net is a source of interference, during parallel/tandem
checks.

Rules area

Specifies the minimum and maximum values for:

• Length  — Defines a minimum and maximum length.

• Stub Length  — Specifies a maximum stub length. The stub length

is the distance from a T-point to the end of the route.

• Delay  — Defines a minimum and maximum delay time in

nanoseconds.

• Capacitance  — Defines a minimum and maximum capacitance in

picofarads.

• Impedance  — Defines a minimum and maximum impedance in

ohms.

 Tip
These text boxes restrict the trace width to a range of values.
Recommended is the width you want to assign to the trace when
routing begins. The Minimum and Maximum values are respected
by routing routines which must use trace width to achieve some
high-speed routing functions, such as impedance matching.

Specifies to arrange certain nets as shielding others; the Net in the
Use Net list box is routed up and down both sides of a selected net to
provide protection from interference.

 Tip
You can only assign nets associated with plane layers in the Layer
Definition dialog box to shield other nets. If there are no plane
layers, the Shield area is grayed out.

Specifies the value of the shield gap.

Specifies the net to use as the shield.

Shield

Gap

Use Net

Match Lengths

Specifies that you want to use Length Matching.

Tolerance

Specifies the maximum difference allowed between the shortest length
and longest length in the matched length group.

Delete  button

Removes this set of High Speed rules from your rules hierarchy.

 Tip
You cannot delete the Default High Speed rules.

SailWind Logic Guide

551

SailWind Logic GUI Reference
HiSpeed Rules Dialog Box

Related Topics

Setting Up High-Speed Rules

552

SailWind Logic Guide

SailWind Logic GUI Reference
Installed Options Dialog Box

## Installed Options Dialog Box

To access: Help  > Installed Options  menu item > License File  tab

Use the License File  tab to select and then view license file information, either the actual license file (for
node-locked licensing) or the feature usage status associated with a server license (for floating licensing).

Figure 79. Installed Options Dialog Box, License File Tab

Objects

Name

License File

Source

View  button

Table  114. Installed Options Dialog Box, License File Tab contents

Description

Displays the location of the license file.

Displays the source of the license.

Specifies to display the selected license file in the view area.

Exception: For Node-locked licenses only.

Status  button

Specifies to display the selected feature usage information.

Exception: For Floating licenses only.

View area

Displays the selected license file information after you click View
(Node-locked license) or Status  (Floating license).

Suite Configuration button

Opens the SailWind Suite Configuration Dialog Box.

 Restriction:
Available only with floating/server-based licenses, a mix of different
SailWind Suites, or a mix of unbundled licenses and suites.

SailWind Logic Guide

553

SailWind Logic GUI Reference
Installed Options Dialog Box

Related Topics

Viewing a License File or License Status

554

SailWind Logic Guide

SailWind Logic GUI Reference
Library List Dialog Box

## Library List Dialog Box

To access: File  > Library  menu item > Manage Lib. List button

When you add a part to the design, you retrieve information about that part from a library. The Library List
dialog box contains a list of libraries to search. The libraries are searched in the order in which they are
listed, beginning with the first library in the list.

Figure 80. Library List Dialog Box

Objects

Name

Library list

Read Only

Shared

Allow Search

Add  button

Remove  button

Table  115. Library List Dialog Box Contents

Description

The libraries currently listed in the Library Manager Library list.

A status indicator only; this box is always unavailable.

Shares the library over the network. This enables more than one
user to access the library file at the same time.

Includes the library when performing operations that involves
libraries, such as adding parts.

Adds a library to the Library list.

Removes a library from the Library list.

Up/Down  buttons

Moves the order of the libraries in the Library list.

Synchronize with SailWind Layout Specifies to push the library settings to SailWind Layout from

SailWind Logic.

SailWind Logic Guide

555

SailWind Logic GUI Reference
Library List Dialog Box

Related Topics

Setting the Library List Order

556

SailWind Logic Guide

SailWind Logic GUI Reference
Library Manager Dialog Box

## Library Manager Dialog Box

To access: File  > Library  menu item

Use the Library Manager to perform operations associated with editing and copying the contents of
libraries.

Figure 81. Library Manager Dialog Box

Objects

Name

Library list

Table  116. Library Manager Dialog Box Contents

Description

The list of libraries available to you.

Create New Lib  button

Opens the New Library window where you can specify a new
library name and location.

Manage Lib. List  button

Opens the Library List Dialog Box.

Attr Manager  button

Opens the Manage Library Attributes Dialog Box.

SailWind Logic Guide

557

SailWind Logic GUI Reference
Library Manager Dialog Box

Name

Preview area

Filter area

Filter list

New  button

Table  116. Library Manager Dialog Box Contents  (continued)

Description

Shows the item selected in the Filter list.

Narrows down the Filter list by Decals, Parts, Lines, or Logic. You
can further narrow the list using wildcards  on page 105 in the Filter
box.

 Tip
Add an asterisk “*” to the box to display all items.

The results from your filter area selections.

The action taken is dependent on the filter.

• Decals  — Opens the PCB Decal Editor on a new decal.

• Parts  — Opens the Part Information Dialog Box, Gates Tab  on

an unnamed part.

• Lines  — Unavailable. There is no special library lines editor.
Use drafting tools to create or edit lines and save them to the
library.

• Logic  — Unavailable. Use SailWind Logic to create or edit CAE

decals.

 Restriction:
This button is unavailable when the Library is set to (All
Libraries).

See also Adding Items to a Library.

Edit  button

The action taken is dependent on the filter.

• Decals  — Opens the PCB Decal Editor on the selected decal.

• Parts  — Opens the Part Information Dialog Box, Gates Tab  on

the selected part.

• Lines  — Unavailable. There is no special library lines editor.
Use drafting tools to create or edit lines and save them to the
library.

• Logic  — Unavailable. Use SailWind Logic to create or edit CAE

decals.

 Restriction:
This button is unavailable when the Library is set to (All
Libraries).

See also Editing Items in a Library.

Delete  button

Removes the selected item from the library.

 Restriction:
This button is unavailable when the Library is set to (All
Libraries).

See also Deleting Items From a Library.

Copy  button

Copies the selected item to another name or another library.

558

SailWind Logic Guide

SailWind Logic GUI Reference
Library Manager Dialog Box

Table  116. Library Manager Dialog Box Contents  (continued)

Name

Description

 Restriction:
This button is unavailable when the Library is set to (All
Libraries).

See also Copying a Library Item.

Import  button

Import library data from an ASCII file. The file type is dependent on
the filter.

 Restriction:
This button is unavailable when the Library is set to (All
Libraries).

See also Importing Library Data.

Export  button

Export library data to an ASCII file. The file type is dependent on
the filter.

 Restriction:
This button is unavailable when the Library is set to (All
Libraries).

See also Exporting Library Data.

List to File  button

The action taken is dependent on the filter.

• Decals  — Generates a list of PCB Decals in a single library.

• Parts  — Generates a list of Parts in a single library or all

libraries along with chosen attributes.

• Lines  — Generates a list of line items in a single library.

• Logic  — Generates a list of CAE decals or Logic symbols in a

single library.

 Restriction:
When the Library is set to (All Libraries), this button is
unavailable for all but Parts.

SailWind Logic Guide

559

SailWind Logic GUI Reference
Log Test Dialog Box

## Log Test Dialog Box

To access: type BLT > press Enter. If nothing happens, close SailWind Logic and restart it.

Use BLT to replay session playback media created by BMW.

Figure 82. Log Test Dialog Box

Objects

Table  117. Log Test Dialog Box contents

Name

Description

Media Directories

Lists the session playback media files.

New name

Specifies to rename the selected media directory.

Rename  button

Renames the selected media directory to the name in the New name
box.

Related Topics

Replaying Session Playback Media With BLT

560

SailWind Logic Guide

SailWind Logic GUI Reference
Logic Families Dialog Box

## Logic Families Dialog Box

To access: Tools  > Part Editor  menu item > Edit Electrical button > General  tab > Families  button

Use the Logic Families dialog box to add, delete, or modify logic family names and default reference
designator prefixes.

Figure 83. Logic Families Dialog Box

Objects

Name

Family column

Prefix column

Add  button

Edit  button

Delete  button

Related Topics

Editing Logic Families

Table  118. Logic Families Dialog Box Contents

Description

Lists the logic family.

Lists the prefix for the logic family

Adds a row to the table.

Makes the selected field editable.

removes the selected row.

SailWind Logic Guide

561

SailWind Logic GUI Reference
Make Field Dialog Box

## Make Field Dialog Box

To access: Select a text string > right-click > Make Field  menu item

Use the Make Field dialog box to change an existing text string into a field.

Figure 84. Make Field Dialog Box

Objects

Name

Name list

Value

X/Y

562

Table  119. Make Field Dialog Box Contents

Description

Lists all of the fields available to you.

The value of the field.

 Restriction:
The Value box is unavailable for system fields since the value
is derived from your system.

Type coordinates to place the field in a specified location.

SailWind Logic Guide

SailWind Logic GUI Reference
Make Field Dialog Box

Table  119. Make Field Dialog Box Contents  (continued)

Name

Description

 Tip
Leave these blank to attach the field to your pointer and click to
indicate the location.

Rotation

Line Width

Specifies the rotation of the text: 0 or 90 degrees.

Specifies the line width for stroke fonts only.

Size

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

Font Style

Enables you to change the font style to bold, italic, and underlined.

Font list

 Restriction:
System fonts only.

The fonts available to you. This lists either stroke fonts or system
fonts. You choose which type of font to use in the Fonts Dialog
Box.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles: B  for bold, I  for italic, or U  for
underlined.

Horizontal/Vertical Justification

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Related Topics

Changing a Text String Into a Field

SailWind Logic Guide

563

SailWind Logic GUI Reference
Manage Library Attributes Dialog Box

## Manage Library Attributes Dialog Box

To access: File  > Library  menu item > Attr Manager  button

Use the Manage Library Attributes dialog box to list the attribute names in your libraries and to add an
attribute to, rename an attribute in, or delete an attribute from, the library.

Figure 85. Manage Library Attributes Dialog Box

Objects

Table  120. Manage Library Attributes Dialog Box Contents

Name

Description

Select Library list

The list of libraries available to you.

Item Types list

Filters the type of items in the Attributes in Library list.

Browse Lib. Attr  button

Opens the Browse Library Attributes Dialog Box.

 Tip
This is available only when an attribute in the New Name
column in the Attributes Selected for Rename list is selected.

Edit New Name  button

Makes the selected attribute Name editable.

 Tip
This is available only when an attribute in the New Name
column in the Attributes Selected for Rename list is selected.

Attributes in Library list

The list of attributes in the selected library.

Add >>  button

Adds the selected attribute to the Rename list.

564

SailWind Logic Guide

SailWind Logic GUI Reference
Manage Library Attributes Dialog Box

Table  120. Manage Library Attributes Dialog Box Contents  (continued)

Name

Description

<< Remove  button

Removes the selected attribute from the Rename list.

<< Remove All  button

Removes all of the attributes from the Rename list.

Attributes Selected for Rename
list

The list of attributes you’ve selected to rename.

Add Attr  button

Opens the Add New Attribute to Library Dialog Box.

Delete Attrs  button

Deletes the selected attribute from the selected library.

Rename Attrs  button

Renames all of the attributes you gave a new name to in the
selected library.

Related Topics

Managing Library Attributes

SailWind Logic Guide

565

SailWind Logic GUI Reference
Manage Schematic Attributes Dialog Box

## Manage Schematic Attributes Dialog Box

To access: Edit  > Attribute Manager  menu item

Use the Manage Schematic Attributes dialog box to manage attributes at the schematic level. You can
create a new attribute and automatically assign it to every part in your design. You can also rename an
attribute in, or delete an attribute from, the schematic. All parts are automatically updated.

Figure 86. Manage Schematic Attributes Dialog Box

Objects

Table  121. Manage Schematic Attributes Dialog Box Contents

Name

Description

Attributes in Schematic list

The list of attributes in the schematic.

Add >>  button

Adds the selected attribute to the Rename list.

<< Remove  button

Removes the selected attribute from the Rename list.

<< Remove All  button

Removes all of the attributes from the Rename list.

Attributes Selected for Rename
list

The list of attributes you’ve selected to rename.

Browse Lib. Attr  button

Opens the Browse Library Attributes Dialog Box.

Edit New Name  button

Makes the selected attribute Name editable.

 Tip
This is available only when an attribute in the New Name
column in the Attributes Selected for Rename list is selected.

566

SailWind Logic Guide

SailWind Logic GUI Reference
Manage Schematic Attributes Dialog Box

Table  121. Manage Schematic Attributes Dialog Box Contents  (continued)

Name

Description

Add Attr  button

Opens the Add New Attribute to Library Dialog Box.

Delete Attrs  button

Deletes the selected attribute from the selected library.

Rename Attrs  button

Renames all of the attributes you gave a new name to in the
selected library.

Related Topics

Manage Attributes in a Schematic

SailWind Logic Guide

567

SailWind Logic GUI Reference
Media Wizard Dialog Box

## Media Wizard Dialog Box

To access: type BMW > press Enter

BMW (Basic Media Wizard) is a tool that you can use to record and play back SailWind Logic, SailWind
Layout and SailWind Router sessions. It is particularly useful as a means of supplying information to
SailWind Technical Support engineers trying to identify and resolve any problematical behavior you may
encounter.

Figure 87. Media Wizard Dialog Box

Objects

Table  122. Media Wizard Dialog Box contents

Name

Description

Media Wizard area

Specifies what you want the Media Wizard to do:

• Create Media from Current Session  — Use this procedure when
the session you are recreating did not cause a SailWind tool crash.

• Create Media from Previous Session  — Use this procedure when
the session you are recreating caused the SailWind tool to crash,
and the automatic procedure described in Automatically Creating
Session Playback Media for a Crashed Session  cannot be used due
to one of the restrictions listed in that section.

• Stop Logging  — Specifies to stop the Media Wizard from logging

any further actions.

User Initials

Specifies your initials. They are included in the playback media
filenames to identify the files as yours.

Delete Actions Before Last
Save

Specifies to delete all entries in the session log file between the first
Open and the last Save command. You can do this to eliminate any
actions you may have performed before beginning the series of actions
that produced the problematical behavior. This makes it easier for the
Tech Support engineer to identify the problem.

Related Topics
BMW and BLT

568

SailWind Logic Guide

SailWind Logic GUI Reference
Modeless Commands and Keyboard Shortcuts

## Modeless Commands and Keyboard Shortcuts

You can set or change some settings and functions at any time using a code letter for the command,
entering the new value, and clicking Enter. This is called a Modeless Command.

Modeless Commands usually apply to values that you change frequently during design. Use the
Modeless Command G, for example, to change the grid setting. Type G, the new setting, and click Enter.
Below is a summary of the Modeless Commands in SailWind Logic:

To show this help topic at any time while SailWind Logic is running, type ? and click Enter.

Tip
(X,Y) = coordinates; (s) = text; (n) = number.

Table  123. Modeless Command and Shortcut Key Table Conventions

Convention

Description

< >

{ }

click

middle-click

right-click

wheel forward

wheel back

A variable, or something you can type.

An optional command argument.

Click the left mouse button.

Click the middle mouse button or wheel.

Click the right mouse button.

Rotate the wheel forward, where the top of the wheel rotates
away from your palm.

Rotate the wheel backward, where the top of the wheel rotates
toward your palm.

Tip
Spaces have significance in modeless commands and shortcut keys. For example, SS W1 and S
SW1 have different meanings. SS W1 means to search for and select W1, while S SW1 means to
search for SW1.

Modeless Commands

The following is a complete list of all of the modeless commands:

Table  124. Modeless Commands for Grid Settings

Name

Command

Description

Global Grid Setting

G<n>

Sets the Design grid, for example G50.

SailWind Logic Guide

569

SailWind Logic GUI Reference
Modeless Commands and Keyboard Shortcuts

Table  124. Modeless Commands for Grid Settings  (continued)

Name

Command

Description

Dot Grid Setting

GD<n>

Sets the Displayed (Dot) grid, for example,
GD100.

Name

Any Angle

Diagonal Angle

Orthogonal Angle

Table  125. Modeless Commands for 2D Line Angles

Command

Description

AA

AD

AO

Any angle mode. Sets the line angle for drafting
objects to Any angle (no angle restrictions).

Diagonal angle mode. Sets the line angle for
drafting objects to Diagonal (45 degree angles
only).

Orthogonal angle mode. Sets the line angle
for drafting objects to Orthogonal (90 degree
angles only).

Table  126. Modeless Commands for Line Width Settings

Name

Command

Description

Set Minimum (Real) Display
Width for Paths

R<width>

Sets the minimum (Real) display width for
paths.

Change Current Line Width

W<width>

Changes the current line width to the number
<n> you enter, for example W 5.

Table  127. Modeless Commands for Searching

Name

Command

Description

Search Absolute

S<x> <y>

Search absolute. Moves the pointer to the
specified X and Y coordinates, for example S
1000 1000.

Search for Named Item
(Pin/Part/Net)

S<string>

Search for named item (pin, part or net), for
example SU1.

Search Relative

SR<x><y>

Search Relative X

SRX<x>

Search Relative Y

SRY<y>

Search relative. Moves the pointer by the
specified X and Y offset, for example SR -100
-50.

Search relative X at current Y. Moves the
pointer by the specified X offset, for example
SRX 300.

Search relative Y at current X. Moves the
pointer by the specified Y offset, for example
SRY 400.

570

SailWind Logic Guide

SailWind Logic GUI Reference
Modeless Commands and Keyboard Shortcuts

Table  127. Modeless Commands for Searching  (continued)

Name

Command

Description

Absolute Move to <n>, Current
Y

SX<x>

Absolute Move to <n>, Current
X

SY<y>

Search absolute X at current Y. Moves the
pointer to the specified X coordinate and the
current Y coordinate, for example SX 300.

Search absolute Y at current X. Moves the
pointer to the specified Y coordinate and the
current X coordinate, for example SY 400

Table  128. Modeless Commands for Drafting Shape Control

Name

Command

Description

Circle shape draw mode.

Path shape draw mode.

Polygon shape draw mode.

Rectangle shape draw mode.

HC

HH

HP

HR

Sets drawing mode to circle shape.

Sets drawing mode to path shape.

Sets drawing mode to polygon shape.

Sets drawing mode to rectangle shape.

Table  129. Modeless Commands for Measurement

Name

Command

Description

Quick Measure

Q

Quick Measure with a dynamic ruler. Attaches
a measurement line to the pointer and displays
dx, dy, and hypotenuse information, depending
on pointer movement.

Place the pointer at the starting point, then type
the “q” modeless command. Drag the pointer
to create a line between the start and end point
of your measurement. Snaps to the design grid
when the Snap to grid is on. Measurements
are gridless when Grid Snap is off. Dynamically
reports delta x, delta y and delta x,y in current
design units.

Table  130. Modeless Commands for Hierarchical Design

Name

Command

Description

Hierarchical Push

Hierarchical Pop

HI

HO

Invokes Hierarchical Push.

Invokes Hierarchical Pop.

SailWind Logic Guide

571

SailWind Logic GUI Reference
Modeless Commands and Keyboard Shortcuts

Name

Undo

Redo

Name

Table  131. Modeless Commands for Undo/Redo

Command

Description

UN

RE

Undo

Redo

Table  132. Miscellaneous Modeless Commands

Command

Description

Open File <name>

F<name>

Open file <name>, where <name> is the path
and name of the file to open (for example, F
demo.eco).

Select Sheet Name or Number

SH<sheet>

Selects the sheet name or number you type, for
example SH3.

Database Integrity Test

Help

I

?

Runs the Database Integrity Test.

Show Help topic.

Table  133. Modeless Commands for Basic Media Wizard/Log Test

Command

Description

Basic Log Test

BLT

Basic Log Test. Opens the Log Test Dialog
Box. BLT finds and runs BMW session playback
media.

See also Crash Detection, BMW and BLT.

Open Basic Media Wizard

BMW

Opens the Basic Media Wizard dialog box.

• BMW records session playback media

for a problematic SailWind Logic session.
It can create playback media based on
your last SailWind Logic session or your
current session. This playback media can be
replayed using the BLT modeless command.

• BMW is also a command line option.

See also Crash Detection, BMW and BLT.

Start BMW Session Logging

BMW ON

Starts BMW session logging.

Stop BMW Session Logging

BMW OFF

Stops BMW session logging.

Function Keys

The following is a complete list of all of the function key command assignments:

572

SailWind Logic Guide

SailWind Logic GUI Reference
Modeless Commands and Keyboard Shortcuts

Table  134. Function Key Command Assignments

Function Key

Description

F1

F2

F3

F4

F5

F6

F7

F8

F9

F10

F11

F12

Open Help (context sensitive)

Add Connection

Unassigned

Unassigned

Unassigned

Unassigned

Unassigned

Unassigned

Unassigned

Unassigned

Unassigned

Unassigned

Keypad Keys

The following is a complete list of all of the keypad key command assignments:

Table  135. Keypad Key Command Assignments

Keypad Keys

Description

(Number Keys) with NumLock On

Keypad (0)

Keypad (1)

Keypad (2)

Keypad (3)

Keypad (4)

Keypad (5)

Keypad (6)

Keypad (7)

Keypad (8)

Center the view using the pointer location

Redraw

Pans the workspace down one increment

Zooms out at the pointer

Pans the workspace left one increment

Starts Zoom from center

Pans the workspace right one increment

Zoom to the Sheet

Pans the workspace up one increment

SailWind Logic Guide

573

SailWind Logic GUI Reference
Modeless Commands and Keyboard Shortcuts

Table  135. Keypad Key Command Assignments  (continued)

Keypad Keys

Description

Keypad (9)

Keypad (.)

Zoom in at the pointer location

Starts Zoom from corner (Zoom Mode only)

(Command Keys) with NumLock Off

Insert

End

Down Arrow

Page Down

Left Arrow

Right Arrow

Home

Up Arrow

Page Up

Delete

Shortcut Keys

Centers the view using the pointer location

Redraw

Moves the pointer down one design grid

Zooms out at the pointer

Moves the pointer left one design grid

Moves the pointer right one design grid

Zooms to the Sheet

Moves the pointer up one design grid

Zooms in at the pointer

Delete the selected object

For mouseless operation, use keyboard shortcuts to start commands for selected items and change some
system settings. Following are the shortcut assignments for SailWind Logic:

Table  136. Keyboard Shortcuts for Panning, Zooming and Navigation

Name

Shortcut Keys

Description

Zoom to Sheet

<home>

Zoom to Sheet

Ctrl + B

Zoom Extents

Ctrl-Alt + E

Zoom Area In/Out

MMB (drag)

Zooms to sheet. Fits the sheet border into the
workspace.

Zooms to sheet. Fits the sheet border into the
workspace.

Zooms to extents. Fits all objects in the design
into the workspace.

Zooms area in or out. Drag pointer up to zoom
in. Drag pointer down to zoom out.

Start Zoom from Corner

Shift + MMB (Drag) Starts Zoom from Corner.

574

SailWind Logic Guide

SailWind Logic GUI Reference
Modeless Commands and Keyboard Shortcuts

Table  136. Keyboard Shortcuts for Panning, Zooming and Navigation  (continued)

Name

Shortcut Keys

Description

Zoom to Selection

Alt + Z

Zooms to selection. Fits the selected objects
into the workspace.

Zoom Mode On/Off

Center View (Using Pointer
Location)

Center View (Using Pointer
Location)

Zoom In at Pointer (Zoom
Mode)

Zoom Out at Pointer (Zoom
Mode)

Zoom In at Pointer (Zoom
Mode)

Ctrl + W

MMB

Toggles Zoom Mode On/Off.

Centers the view at the pointer.

<Insert>

Centers the view at the pointer.

LMB Click

Zooms in at the pointer (zoom mode).

RMB Click

Zooms out at the pointer (zoom mode).

<spacebar>

Zooms in at the pointer (zoom mode).

Zoom In at Pointer

Zoom Out at Pointer

<PgUp>

<PgDn>

Zooms in at the pointer.

Zooms out at the pointer.

Zoom In at Pointer

Ctrl + Wheel Fwd

Zooms in at the pointer.

Zoom Out at Pointer

Ctrl + Wheel Back

Zooms out at the pointer.

Move Pointer Down (One
Design Grid)

Move Pointer Up (One Design
Grid)

Move Pointer Left (One Design
Grid)

Move Pointer Right (One
Design Grid)

<Down Arrow>

Pointer moves down one design grid.

<Up Arrow>

Pointer moves up one design grid.

<Left Arrow>


Pointer moves left one design grid.

<Right Arrow>


Pointer moves right one design grid.

Dynamic Panning

Alt + MMB (Drag)

Pans the sheet area below the pointer to the
center of the workspace.

Pan Workspace Down (One
Line)

Wheel Back

Pans workspace down one line.

Pan Workspace Up (One Line) Wheel Fwd

Pans workspace up one line.

Pan Workspace Right (One
Line)

Shift + Wheel Back Pans workspace right one line.

Pan Workspace Left (One Line) Shift + Wheel Fwd

Pans workspace left one line.

SailWind Logic Guide

575

SailWind Logic GUI Reference
Modeless Commands and Keyboard Shortcuts

Table  136. Keyboard Shortcuts for Panning, Zooming and Navigation  (continued)

Name

Shortcut Keys

Description

Pan Workspace Down (One
Pixel)

Ctrl-Alt + Wheel
Back

Pans workspace down one pixel.

Pan Workspace Up (One Pixel) Ctrl-Alt + Wheel

Fwd

Pans workspace up one pixel.

Pan Workspace Right (One
Pixel)

Alt-Shift + Wheel
Back

Pans workspace right one pixel.

Pan Workspace Left (One
Pixel)

Alt-Shift + Wheel
Fwd

Pans workspace left one pixel.

Name

Filter

Select

Select

Table  137. Keyboard Shortcuts for Selection

Shortcut Keys

Description

Ctrl-Alt + F

Opens the Selection Filter.

LMB Click

Selects an object.

<Spacebar>

Selects an object.

Select All

Ctrl + A

Selects all objects on the current sheet based
upon the selection filter choices.

Select All on Schematic

Ctrl-Shift + A

Selects all objects on the schematic based
upon the selection filter choices.

Area Select

LMB (Start Drag)

Starts an area selection.

Area Complete

LMB (End Drag)

Completes an area selection.

Cancel Area Selection

LMB (Cancel Drag) Cancels area selection.

Toggles/Multiple Selection

Ctrl + LMB Click

Duplicate

Ctrl + LMB (Drag)

Toggles object selection or selects multiple
objects.

Duplicates selected object and attaches to
pointer.

Table  138. Keyboard Shortcuts for File Operations

Name

Shortcut Keys

Description

Create New Design File (Blank) Ctrl + N

Creates a new blank design file.

Open File (Design)

Print/plot

576

Ctrl + O

Ctrl + P

Opens a design file.

Print/plot

SailWind Logic Guide

SailWind Logic GUI Reference
Modeless Commands and Keyboard Shortcuts

Table  138. Keyboard Shortcuts for File Operations  (continued)

Name

Shortcut Keys

Description

Save (Quick Save)

Ctrl + S

Saves the design file

Table  139. Keyboard Shortcuts for Opening Menus and Dialog Boxes

Name

Shortcut Keys

Description

Open File Menu

Open Edit Menu

Open View Menu

Open Setup Menu

Open Tools Menu

Open Help Menu

Open Shortcut Menu

Alt + F

Alt + E

Alt + V

Alt + S

Alt + T

Alt + H

RMB

Opens the File menu.

Opens the Edit menu.

Opens the View menu.

Opens the Setup menu.

Opens the Tools menu.

Opens the Help menu.

Opens the Shortcut menu.

Toggle Menu Bar

Ctrl-Alt + M

Toggles the visibility of the Menu Bar.

Properties (Current Object)

LMB DblClick

Properties (for Selected)

Alt+<Enter>

Properties (for Selected)

Ctrl + Q

Displays Properties for the currently selected
object.

Displays Properties for the currently selected
object.

Displays Properties for the currently selected
object.

Options

Options

Ctrl + <Enter>

Opens the Options dialog box.

Ctrl-Alt + G

Opens the Options dialog box.

Display Colors

Ctrl-Alt + C

Opens the Display Colors dialog box.

Status Window

Ctrl-Alt + S

Opens the Status Window.

Table  140. Keyboard Shortcuts for Placement Operations

Name

Shortcut Keys

Description

Move Selected Object(s)

Ctrl + E

Moves the selected object(s).

Rotate Selected (90)

Flip Selected on X Axis

Ctrl + R

Ctrl + F

Rotates the selected object (90 degrees).

X Mirror (flips selected object on X axis).

SailWind Logic Guide

577

SailWind Logic GUI Reference
Modeless Commands and Keyboard Shortcuts

Table  140. Keyboard Shortcuts for Placement Operations  (continued)

Name

Shortcut Keys

Description

Flip Selected on Y Axis

Ctrl-Shift + F

Y Mirror (flips selected object on Y axis)

Draw Group While in Move
Group Mode

Vertically Justify Text During
Move

Ctrl-Shift + D

Draw Group while in Move Group Mode.

Ctrl-Shift + J

Vertically justify text during move.

Horizontally Justify Text During
Move

Ctrl + J

Horizontally justify text during move.

Connect to Layout for
Cross-Probing

Ctrl-Shift + O

Connect to Layout for cross-probing.

Name

Add Corner

Add Corner

Backup

Complete Bus

Complete Bus

Rename

Reset DxDy

Table  141. Keyboard Shortcuts for Connection Operations

Shortcut Keys

Description

LMB Click

Adds a new connection corner.

<Spacebar>

Adds a new connection corner.

<Backspace>

Removes the last connection corner on a
connection line or the last corner on a 2D line
(in polygon or path drawing mode).

<Enter>

Completes the bus.

LMB DblClick

Completes the bus.

Ctrl + L

Rename.

Crtl + <PgDn>

Reset delta coordinates to measure from
current position.

Add Ground Symbol

Ctrl + <spacebar>

Adds a Ground Symbol while in Add
Connection mode.

Add Power Symbol

Shift + <spacebar> Adds a Power Symbol while in Add Connection

mode.

Add Off-page Symbol

Alt + <spacebar>

Add an Off-page Symbol while in Add
Connection mode.

Cycle Alternate Gate Decals

Ctrl + <Tab>

Cycles through alternate gate decals.

578

SailWind Logic Guide

Name

Cut

Copy

Paste

Redraw

Redraw

Delete

Cancel

Redo

Undo

Name

Next View

Previous View

SailWind Logic GUI Reference
Modeless Commands and Keyboard Shortcuts

Table  142. Keyboard Shortcuts for Editing

Shortcut Keys

Description

Ctrl + X

Ctrl + C

Ctrl + V

<End>

Ctrl + D

<Delete>

<Escape>

Ctrl + Y

Ctrl + Z

Cut

Copy

Paste

Redraw

Redraw

Delete

Cancel

Redo

Undo

Table  143. Keyboard Shortcuts for Viewing

Shortcut Keys

Description

Alt + N

Alt + P

Displays the next view.

Displays the previous view.

Table  144. Mouse Button Substitutions

Name

Shortcut Keys

Description

Activate Right Click Popup
Menu (Right Mouse Button)

M

Activates the shortcut menu for the current
mode. Same as right-click.

Left Mouse Click

<Spacebar>

Activates a left mouse button click (to add
corners, select items, complete, etc.) at the
current pointer location.

SailWind Logic Guide

579

SailWind Logic GUI Reference
Net Attributes Dialog Box

## Net Attributes Dialog Box

To access: Select a net > right-click > Attributes  menu item

Use the Net Attributes dialog box to associate information with a single net or set of nets on the
schematic. Attributes are made of two parts, an attribute name and its corresponding value. If connecting
to SailWind Layout, these attributes are passed along with the rest of the schematic.

Figure 88. Net Attributes Dialog Box

Objects

Name

Description

Table  145. Net Attributes Dialog Box

Attributes table

Lists the name and value of the net selected in the schematic.

Add  button

Delete  button

Edit  button

Adds a new row below the selected row.

Removes the selected row from the Attributes table.

Makes the selected cell available for editing.

Related Topics

Creating Net Attributes

580

SailWind Logic Guide

SailWind Logic GUI Reference
Net Name Properties Dialog Box

## Net Name Properties Dialog Box

To access: Select a net name label > right-click > Properties  menu item

Use the Net Name Properties dialog box to provide or change text and font settings for one or more net
name labels.

Figure 89. Net Name Properties Dialog Box

Objects

Name

Net Name

Rename

Rotation

Size

Table  146. Net Name Properties Dialog Box Contents

Description

The name of the selected net.

Specifies to rename the selected net name or all instances of the
net name.

Specifies the rotation of the label: 0 or 90 degrees.

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

SailWind Logic Guide

581

SailWind Logic GUI Reference
Net Name Properties Dialog Box

Table  146. Net Name Properties Dialog Box Contents  (continued)

Name

Description

Line Width

Specifies the line width for stroke fonts only.

Font list

The fonts available to you. This lists either stroke fonts or system
fonts.

You choose which type of font to use in the Fonts Dialog Box.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles:B  for bold, I  for italic, or U  for
underlined.

Horizontal/Vertical Justification

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Related Topics

Modifying Part Type Labels

582

SailWind Logic Guide

SailWind Logic GUI Reference
Net Properties Dialog Box

## Net Properties Dialog Box

To access: Select a net > right-click > Properties  menu item

Use the Net Properties dialog box to access net specific properties.

Figure 90. Net Properties Dialog Box

Objects

Name

Net Name

Table  147. Net Properties Dialog Box Contents

Description

The name of the selected net. Type or select one from the list to
create a new one.

Rename area

Specifies to rename the selected net or all instances of the net.

 Tip
Selecting This Instance will cause the net to be split into two
separate nets.

Net Name Label

Specifies to add a visible label to the selected net segment.

 Restriction:
You must select the connection segment where it enters
or exits a part, or the Net Name Label check box will be
unavailable.

 Tip
Clearing the Net Name Label check box removes the visible
label. The net and all subnets retain the net name.

Statistics  button

Displays connection information in your default text editor.

SailWind Logic Guide

583

SailWind Logic GUI Reference
Net Properties Dialog Box

Table  147. Net Properties Dialog Box Contents  (continued)

Name

Description

Attributes  button

Opens the Net Attributes Dialog Box.

Rules  button

Opens the Net Rules Dialog Box.

Related Topics
Modifying Nets

584

SailWind Logic Guide

SailWind Logic GUI Reference
Net Rules Dialog Box

## Net Rules Dialog Box

To access:

• Setup  > Design Rules  menu item > Net  button

• Select a net > right-click > Show Rules  menu item

• Select a net > right-click > Properties  > Rules  button

Use the Net Rules dialog box to define design rules that apply to nets.

Figure 91. Net Rules Dialog Box

Objects

Name

Nets list

Table  148. Net Rules Dialog Box

Description

Lists all nets in the design.

Show Nets with rules

Specifies to show only nets that have rules.

Clearance  button

Opens the Clearance Rules Dialog Box.

Routing  button

Opens the Routing Rules Dialog Box.

HiSpeed  button

Opens the HiSpeed Rules Dialog Box.

Report  button

Opens the Rules Report Dialog Box.

Picture below rule button

The picture below each type of rule button identifies which rules
hierarchy level is used for that rule type. The meaning of the picture
corresponds to the button in the Hierarchy area of the Rules dialog box.
For example, if you select a class in the Class list and a green polygon

SailWind Logic Guide

585

SailWind Logic GUI Reference
Net Rules Dialog Box

Table  148. Net Rules Dialog Box  (continued)

Name

Description

appears below the Clearance  button, then the default values apply to
the class.

Selected

Lists the net(s) selected in the Nets list.

Default  button

Removes non-default rules from the selected nets, so that only default
rules apply.

586

SailWind Logic Guide

SailWind Logic GUI Reference
Netlist to PCB Dialog Box

## Netlist to PCB Dialog Box

To access: Tools  > Layout Netlist  menu item

Use the Netlist to PCB dialog box to create a netlist for import to SailWind Layout.

Tip
If you use both SailWind Logic and SailWind Layout on the same computer, there is a more
automated method to pass the netlist. For more information, see the Send Net list  button on the
SailWind Layout Link Dialog Box, Design Tab.

Restriction:
Transferring non-ECO-registered parts and non-electrical parts is constrained by settings in the
Options. See Options Dialog Box, Design Category  on page 591 for details.

Figure 92. Netlist to PCB Dialog Box

SailWind Logic Guide

587

SailWind Logic GUI Reference
Netlist to PCB Dialog Box

Objects

Table  149. Netlist to PCB Dialog Box Contents

Name

Description

Output File Name

Accept the default name, type, or browse to the location and name of the
netlist (.asc) file you are creating.

Select Sheets area

Specifies the schematic sheets to include in the netlist. You can use the
Select All  and Unselect All buttons as shortcuts.

Include Subsheets

Specifies to include any connections to hierarchical symbols in the netlist.

Output Formats

Specifies to output netlists compatible with the latest or older database
formats.

Include Design Rules

Specifies to include design rules and trace width settings in the netlist.

Include Part Attributes

Specifies to include part attributes in the netlist.

Include Net Attributes

Specifies to include net attributes in the netlist

TIP: Run Connectivity
Report to check for possible
connectivity errors

To run the Connectivity Report, in SailWind Logic, click the File  >
Reports  menu item. In the Reports Dialog Box, select the Connectivity
check box and click OK.

588

SailWind Logic Guide

SailWind Logic GUI Reference
Off-Page Properties Dialog Box

## Off-Page Properties Dialog Box

To access: Select an off-sheet label > right-click> Properties  menu item

Use the Off-Page Properties dialog box to set the properties of off-sheet labels.

Figure 93. Off-Page Properties Dialog Box

Objects

Table  150. Off-Page Properties Dialog Box

Name

Description

Maximum sheet numbers per
line

Enter the maximum number of sheet numbers allowed per line.

Rotation

Select 0 or 90 degrees.

SailWind Logic Guide

589

SailWind Logic GUI Reference
Options Dialog Box

## Options Dialog Box

Using the Options dialog box, you can preset options for commands in SailWind Logic, setting up how
those SailWind Logic commands will work and overriding the default settings in the default.txt file. Setting
options enables you to set up a working environment that suits your design and the way you work.

To access: Tools  > Options  menu item

Options Dialog Box, Design Category
Options Dialog Box, General Category
Options Dialog Box, Line Widths Category
Options Dialog Box, Text Category

590

SailWind Logic Guide

SailWind Logic GUI Reference
Options Dialog Box, Design Category

### Options Dialog Box, Design Category

To access: Tools  > Options  menu item > Design  category

There are six categories of general options for the Schematic Editor; they are organized into six areas in
the Design category labeled Parameters, Options, Sheet, Off-sheet Labels, Non-ECO-Registered Parts,
and Non-Electrical Parts.

Figure 94. Options Dialog Box, Design

Objects

Table  151. Options Dialog Box, Design Category

Name

Description

Parameters area

Tie Dot Diameter

Specifies the diameter of tie dots. The value must be from 0 to 100.

Bus Angle Offset

Defines the starting point distance from the bus for the bus tap. The
value must be from 0 to 250.

SailWind Logic Guide

591

SailWind Logic GUI Reference
Options Dialog Box, Design Category

Table  151. Options Dialog Box, Design Category  (continued)

Name

Description

 Tip
The bus tap joins connections to the bus.

Options area

Preserve Ref Des on Paste

Specifies to use a group's current reference designator assignment
when possible.

 Tip
Click to clear this check box to assign the pasted group's reference
designators the first or next available number.

See also Preserving Reference Designators.

Allow Floating Connections

Specifies to create connections without terminations.

Allow Named Subnets without
Labels

 Tip
Click to clear this check box to prevent creating additional Floating
Connections. Disabling the option does not remove existing
Floating Connections.

See also Working With Floating Connections.

Specifies to allow deletion of net name labels in all cases except that of
a power symbol connected to a net that overrides its default net name.
When this box is checked, the current net name is not changed under
any circumstances.

When this box is cleared, you cannot delete labels tied to bus rippers
or off-page symbols. You can delete net labels tied to component pins;
this causes the net to be renamed to a system-generated name, but
only if both the following conditions apply:

• The net is not connected to a bus or off-page symbol.

• The deleted label was the only label on the net.

 Tip
It is possible to have a named subnet without a label even if the
“Allow Named Subnets without Labels” check box is unchecked.
If you change the name of a subnet with a system net name in the
Net Properties dialog box, and click OK  without checking the Net
Labels check box, the result will be a named subnet without a label.

Allow overwriting of attribute
values in design with blank
values from library

Specifies how design attribute values should be handled by operations
that change design part types, such as Update From Library, Update
Selected Part Type from Library, Change Type (in the Part Type
Properties dialog), ECO Import, and automated operations.

• Select the check box to allow the value of an attribute in the design
to be overwritten by a blank value from the library or other update
source.

• Clear it to prevent overwriting these values.

Sheet area

Size list

592

Specifies the size sheet you want.

SailWind Logic Guide

SailWind Logic GUI Reference
Options Dialog Box, Design Category

Table  151. Options Dialog Box, Design Category  (continued)

Name

Description

Sheet border

Specifies the current sheet boarder.

Choose  button

Opens the Get Drafting Item from Library dialog box to change the
sheet boarder.

 Tip
Be sure to select a sheet border that fits within the boundaries of
the selected sheet size.

See also Adding Drafting Items From a Library.

Off-Sheet Labels area

Show Off-page Sheet
Numbers

Displays sheet reference numbers that are adjacent to off-page
reference symbols and bus names.

Separators

Numbers per Line

Specifies the open and close characters you want to enclose sheet
numbers. For example, "" {} or [] .

Specifies how many sheet numbers to display per line. The value must
be from 0 to 99. Depending on the value you specify, you can stack or
line up the sheet number references.

 Tip

• This only applies when Show Off-page Sheet Numbers is

selected.

• The sheet numbers appear on a line below the net name.

Non-ECO-Registered Parts area

Include in Netlist

Specifies to include the part in the netlist.

 Tip
To include a part that is both non-ECO-registered and non-electrical
in a netlist, select the check boxes in both Part areas.

Include in ECO to PCB

Specifies to include a part in the ECO file that is forwarded to the PCB.

 Tip
To include a part that is both non-ECO-registered and non-electrical
in a Forward ECO to PCB, select the check boxes in both Part
areas.

Include in BOM report

Specifies to include a part in the Bill of Materials (BOM) report.

 Tip
To include a part that is both non-ECO-registered and non-electrical
in a BOM report, select the check boxes in both Part areas.

Non-Electrical Parts area

Include in Netlist

Specifies to include the part in the netlist.

SailWind Logic Guide

593

SailWind Logic GUI Reference
Options Dialog Box, Design Category

Table  151. Options Dialog Box, Design Category  (continued)

Name

Description

 Tip
To include a part that is both non-ECO-registered and non-electrical
in a netlist, select the check boxes in both Part areas.

Include in ECO to PCB

Specifies to include a part in the ECO file that is forwarded to the PCB.

 Tip
To include a part that is both non-ECO-registered and non-electrical
in a Forward ECO to PCB, select the check boxes in both Part
areas.

Include in BOM report

Specifies to include a part in the Bill of Materials (BOM) report.

 Tip
To include a part that is both non-ECO-registered and non-electrical
in a BOM report, select the check boxes in both Part areas.

Related Topics

Setting Schematic Editor Options

594

SailWind Logic Guide

SailWind Logic GUI Reference
Options Dialog Box, General Category

### Options Dialog Box, General Category

To access: Tools  > Options  menu item > General  category

There are six categories of general options for the Schematic Editor; they are organized into six areas
in the General category labeled Display, Cursor, Grids, OLE objects, Text Encoding, and Automatic
Backups.

Objects

Name

Display area

Table  152. Options Dialog Box, General Category

Description

Keep view on window resize

Specifies to maintain the area view of the design when you resize the
SailWind Logic window, by automatically zooming in or out.

Minimum display width

Specifies the minimum width, in current design units, of lines you want
to draw at actual width. Lines smaller than this width are drawn only as
centerlines to save memory and redraw time.

SailWind Logic Guide

595

SailWind Logic GUI Reference
Options Dialog Box, General Category

Name

Cursor area

Style list

Grids area

Design

Labels and Text

Display Grid

Table  152. Options Dialog Box, General Category  (continued)

Description

 Tip

• Set this value to zero to display all lines at actual width.
• Larger values reduce redraw times.

Specifies the cursor shape:

• Normal  — Arrow

• Small cross  — Small plus sign +

• Large cross  — Large plus sign +

• Full screen  — Full screen crosshair

 Tip
If you want the cursor resemble an x, select the Diagonal check
box.

Specifies a grid size for the Design grid which determines object
placement. The value must be from 2 to 2000 and a multiple of 2 (for
example, 2, 4, 50, 100).

Specifies a grid size for the Labels and text grid which determines
placement of all labels, fields, names, attributes, and text. The value
must be from 2 to 2000 and a multiple of 2 (for example, 2, 4, 50, 100).

Specifies a grid size for the Display grid which is a visible guide for
drawing lines, decals, connections, and more. The value must be from
10 to 9998 and a multiple of 2 (for example, 2, 4, 50, 100).

 Tip

• The Display grid is independent of the system grid displayed on

the status line.

• If the grid is not visible when the work area is redrawn, you

probably have set an interval that is too small for display at all
zoom levels. You will have to zoom in several times before the
display grid becomes visible.

Snap to Grid

Specifies to snap an item or object to the grid during editing.

See also Work Area and Grid Settings.

OLE Objects area

Display OLE objects

Specifies to display linked and embedded objects in the work area.

 Tip
The OLE display settings affect SailWind Logic only when it is
embedded in another application.

Update on redraw

Specifies to update the SailWind Layout linked or embedded object in
the container application.

596

SailWind Logic Guide

Table  152. Options Dialog Box, General Category  (continued)

Name

Description

SailWind Logic GUI Reference
Options Dialog Box, General Category

 Restriction:
This option applies only when you are editing the SailWind Logic
object in a separate window and you click the Redraw  button in the
separate window.

 Tip

• To increase performance, disable this option.
• The OLE display settings affect SailWind Logic only when it is

embedded in another application.

Draw background

Specifies to draw the SailWind Logic background color in the linked or
embedded SailWind Logic object.

 Tip
When this option is disabled, the background of the SailWind Logic
object is transparent and you can see through the object at the
container application's background.

Text Encoding area

Text Encoding list

Specifies the language encoding to use in text strings and labels
displayed in the design screen.

 Tip
Encoding choices include those supported in the current localized
version of SailWind Logic, plus any default encoding already in use
in the design.

Example:  A letter with a 0x20 code displays as a Latin capitol letter
A with a grave accent in a design using Western encoding, and as a
Cyrillic capital letter A in a design with Cyrillic encoding.

 Restriction:
The default text encoding cannot be changed. It is automatically set
by the Regional and Language settings of the operating system.

Automatic backups area

Interval

Specifies the time in minutes between automatic backups to a file.

Number of backups

Specifies the quantity (1-9) of different backup files to create.

 Tip
Backup files are named <filename>#.sch, where # is a sequential
number. For example, logic1.sch, logic2.sch, and so on.

Backup File  button

Changes the folder or name of the backup file

Use design name in backup
file name

Specifies to use the design name instead of the product name as the
file name.

Example:  preview_logic1.sch, preview_logic2.sch instead of
logic1.sch, logic2.sch.

Create backup files in design
directory

Specifies to place all of your backup files in the same directory as the
design.

SailWind Logic Guide

597

SailWind Logic GUI Reference
Options Dialog Box, General Category

Table  152. Options Dialog Box, General Category  (continued)

Name

Description

 Tip
Click to clear if you want your backup files in one, common backup
directory.

Related Topics

Setting Schematic Editor Options

Creating a Backup File

598

SailWind Logic Guide

SailWind Logic GUI Reference
Options Dialog Box, Line Widths Category

### Options Dialog Box, Line Widths Category

To access: Tools  > Options  menu item > Line Widths  category

Use the Line Widths category to change the size of line widths in the workspace.

Objects

Name

Type

Width

Table  153. Options Dialog Box, Line Widths Category

Description

Lists the types of lines available in the schematic.

Specifies the width of the line type.

Edit  button

Makes the Width column of the selected row editable.

Related Topics

Setting Line Widths

SailWind Logic Guide

599

SailWind Logic GUI Reference
Options Dialog Box, Text Category

### Options Dialog Box, Text Category

To access: Tools  menu item > Text  category

The Text category differs depending on the selection you made in the Fonts dialog box: Stroke or System
font.

Figure 95. Options Dialog Box, Text Page - System Font

600

SailWind Logic Guide

SailWind Logic GUI Reference
Options Dialog Box, Text Category

Figure 96. Options Dialog Box, Text Page - Stroke Font

Objects

Name

Type

Font

B

I

Table  154. Options Dialog Box, Text Category

Description

Displays the type of font used in the schematic.

Specifies the system font used.

 Restriction:
System font only.

Specifies if this font is bold. Click to make the font bold; click to clear to
make it regular weight.

 Restriction:
System font only.

Specifies if this font is italicized. Click to make the font italic; click to
clear to make it regular.

 Restriction:
System font only.

SailWind Logic Guide

601

SailWind Logic GUI Reference
Options Dialog Box, Text Category

Name

U

Size

Width

Table  154. Options Dialog Box, Text Category  (continued)

Description

Specifies if this font is underlined. Click to underline the font; click to
clear to make it regular.

 Restriction:
System font only.

Specifies the size of the font.

 Restriction:
System font only.

Specifies the width of the font.

 Restriction:
Stroke font only.

Edit  button

Makes the selected field editable.

 Restriction:
You cannot edit fields in the Type column.

602

SailWind Logic Guide

SailWind Logic GUI Reference
Options Dialog Box - Part Editor, General Category

## Options Dialog Box - Part Editor, General Category

To access: While in the Schematic Editor, click the Tools  > Part Editor  menu item. In the Part Editor, click
the Edit  > CAE Decal Editor  menu item. In the CAE Decal Editor, click the Tools  > Options menu item,
then click the General  category.

There are four categories of general options for the Part Editor; they are organized into four areas on the
General category labeled Display, Cursor, Grids, and Text Encoding.

Objects

Name

Display area

Table  155. Options Dialog Box - Part Editor, General Category

Description

Keep view on window resize

Specifies to maintain the area view of the design when you resize the
SailWind Logic window, by automatically zooming in or out.

SailWind Logic Guide

603

SailWind Logic GUI Reference
Options Dialog Box - Part Editor, General Category

Table  155. Options Dialog Box - Part Editor, General Category  (continued)

Name

Description

Minimum display width

Specifies the minimum width, in current design units, of lines you want
to draw at actual width. Lines smaller than this width are drawn only as
centerlines to save memory and redraw time.

 Tip

• Set this value to zero to display all lines at actual width.
• Larger values reduce redraw times.

Cursor area

Style list

Grids area

Design

Labels and Text

Display Grid

Specifies the cursor shape:

• Normal  — Arrow

• Small cross  — Small plus sign +

• Large cross  — Large plus sign +

• Full screen  — Full screen crosshair

 Tip
If you want the cursor to resemble an x, select the Diagonal check
box.

Specifies a grid size for the Design grid which determines object
placement. The value must be from 2 to 2000 and a multiple of 2 (for
example, 2, 4, 50, 100).

Specifies a grid size for the Labels and text grid which determines
placement of all labels, fields, names, attributes, and text. The value
must be from 2 to 2000 and a multiple of 2 (for example, 2, 4, 50, 100).

Specifies a grid size for the Display grid which is a visible guide for
drawing lines, decals, connections, and more. The value must be from
10 to 9998 and a multiple of 2 (for example, 2, 4, 50, 100).

 Tip

• The Display grid is independent of the system grid displayed on

the status line.

• If the grid is not visible when the work area is redrawn, you

probably have set an interval that is too small for display at all
zoom levels. You will have to zoom in several times before the
display grid becomes visible.

Snap to Grid

Specifies to snap an item or object to the grid during editing.

See also Work Area and Grid Settings.

Text Encoding area

Text Encoding list

Specifies the language encoding to use in text strings and labels
displayed in the design screen.

604

SailWind Logic Guide

SailWind Logic GUI Reference
Options Dialog Box - Part Editor, General Category

Table  155. Options Dialog Box - Part Editor, General Category  (continued)

Name

Description

 Tip
Encoding choices include those supported in the current localized
version of SailWind Logic, plus any default encoding already in use
in the design.

Example:  A letter with a 0x20 code displays as a Latin capitol letter
A with a grave accent in a design using Western encoding, and as a
Cyrillic capital letter A in a design with Cyrillic encoding.

Related Topics

Setting Part Editor Options

SailWind Logic Guide

605

SailWind Logic GUI Reference
Options Dialog Box - Print/Plot

## Options Dialog Box - Print/Plot

To access:

• File  > Plot  menu item > Options  button

• File  > Print  menu item > Options  button

Use the Options dialog box to set the output options for printing or plotting. Setting options enables you to
set the position, orientation, and color of selected sheets and objects.

Figure 97. Options Dialog Box - Print/Plot

Objects

Table  156. Options Dialog Box - Print/Plot

Name

Description

Available list

Lists the available sheets to print.

Add >>  button

Moves the selected sheet to the Sheets to Print list.

Add All >>  button

Moves all sheets to the Sheets to Print list.

606

SailWind Logic Guide

SailWind Logic GUI Reference
Output Window

Table  156. Options Dialog Box - Print/Plot  (continued)

Name

Description

<< Remove  button

Moves the selected sheet to the Available list.

<< Remove All  button

Moves all sheets to the Available list.

Sheet to Print list

Lists off the sheets you want to print.

Items area

Specifies the items you want to include in your output.

Color Selection area

Specifies the color you want for the different items in the Items area.

Click a color tile, then in the Items area, click the tile to the right of the
item to change its color.

Orientation

Justification

X/Y Offset

Specifies the orientation angle for the output.

Specifies the justification position for the output.

Specifies the offset values.

 Tip

• You can only set offsets if you clicked something other than

Scale to Fit and Centered in the Justification list.

• The print or plot location is calculated after the plot is rotated

and scaled.

Scaling

Specifies the type the plot size to actual size ratio.

Example:  A 2 to 1 scaling results in a printout or plot that is twice the
actual size.

Preview area

Graphically shows the position, orientation, justification, and scaling of
the output.

Plot Job Name

Specifies to output the schematic name, time, and date.

Plot Window

Specifies to print the displayed window.

Preview  button

Opens the Selections Preview Dialog Box.

## Output Window

Use the Output window for displaying reports and session logs, macro editing and debugging, and custom
programming and debugging, as well as CIS configuration.

To access: Click the Output Window  button.

The Output window is located in the lower left section of the display window. You can dock or float the
Output window. You can also open or close the Output window.

The Output window has three tabs described below.

SailWind Logic Guide

607

SailWind Logic GUI Reference
Output Window

Status Tab

The Status  tab displays information about the current session. It specifies the filename of the opened
PCB file and the name of the test integrity file that is saved. It also reports routing statistics and messages
when routing a board.

If the Status  tab is closed, and you get an error while autorouting - or performing other tasks - the Output
window opens with the Status  tab active and the error appearing in red. The Output window reappears in
its most recent state (floating or docked).

• Output Window button > Status tab

Macro Tab

You can edit, run, and debug macro scripts in the Macro  tab. You can open multiple macros and nest
macros using the macro editor.

A macro is any combination of commands, keystrokes, and mouse clicks that you record to replay as a
single action. You can record virtually any set of procedural steps for replay, thereby simplifying redundant
activities, such as setting preferences and layer/display settings.

• Output Window  button > Macro  tab

CIS Tab

The CIS  tab provides a graphic interface to view part information in the database, to which you connect.
You can select and add parts to the design, specify the part information to display, and export database
configuration.

• Output Window  button > CIS  tab

Library Config Dialog Box

Part Manager Dialog Box

608

SailWind Logic Guide

SailWind Logic GUI Reference
Library Config Dialog Box

### Library Config Dialog Box

To access: Output Window  > CIS  tab > New/Edit  button

Use the Library Config dialog box to specify the database from which to load part information and specifc
part information displayed in the CIS  tab.

Figure 98. Library Config Dialog Box

Objects

Table  157. Library Config Dialog Box Contents

Name

Description

ODBC DSN area:

ODBC DSN

Selects the database from which to load part information from the
drop-down list.

 Tip
SailWind StarterLibrary is connected by default.

ODBC Config

Adds a new database.

 Tip
Click Update  to make the newly added database available.

Update

Makes the newly added database available in the ODBC DSN
drop-down list.

Database Tables area

To CIS

Specifies database table(s) to display in the CIS  tab.

SailWind Logic Guide

609

SailWind Logic GUI Reference
Library Config Dialog Box

Table  157. Library Config Dialog Box Contents  (continued)

Name

Description

Table Name

Displays all the table(s) in the selected database.

Table Configuration area

Field Name

Field Type

Field Alias

Lists all fields in the table selected on the left.

Specifies what type the table fields belong to from the drop-down list,
wherein:

• Part_Type is mandatory, based on which to load data into the

CIS tab. Besides, you can see schematic symbol and PCB decal
assigned to the part type in the local libraries from the CIS preview
window.

• Part_Number is mandatory, based on which to check whether part

attribute values in design are identical with those in CIS.

• Category allows to show table structure hierarchically by

subcategories in the CIS tab.

• All field types except Normal must be unique.

Specifies the table heading for each field to display in the CIS  tab.
• Field aliases corresponding to Field Type "Part_Type" and

"Part_Number" are defined by default, and no modification is
allowed.

• If nothing is set, Field Name will be used instead.

Transfer to Design

Specifies to add the Field Name to the part attributes. If yes, you
can see it in the Part Attributes list by checking part properties in the
design.

Visibility in CIS

Key

Browsable

 Tip
When set, Field Alias will be used instead.

Specifies to display Field Name in the CIS  tab. When set, Field Alias
will be used instead.

Reserved

Specifies to add hyperlinks to the field contents in the CIS  tab, which
often links to such reference files as datasheets and drawings.

Property Checking

Specifies attribute(s) to compare for consistency checking in the Part
Manager Dialog Box.

 Tip
No checkbox selected means comparing all attributes by default.

610

SailWind Logic Guide

SailWind Logic GUI Reference
Part Manager Dialog Box

### Part Manager Dialog Box

To access: Output Window  > CIS  tab > Part...  button

Use the Part Manager dialog box to compare part attributes in design with those in CIS for consistency
checking. For the inconsistent attribute values, you can update from CIS with multiple options.

Figure 99. Part Manager Dialog Box

Objects

Name

Filter area

Table  158. Part Manager Dialog Box Contents

Description

• Specifies the search filter. Note that filtering by Component
Name or Part Number is case-sensitive and no wildcard or
expression is currently supported.

• Provides functionality buttons as follows:

• Filter: Used to activate the filter

• Clear: Used to reset the search filter settings

• Show Error Only: Used to show parts found with errors

Part Attribute Info. area

Displays the search result.

For schematic parts whose attributes are not identical with those in
CIS, they are highlighted in red.

Update the Selected  button

Updates the incosistent attributes of the selected schematic part(s)
from CIS.

Takes effect only on schematic parts found with "Attribute is not
equal" error.

Update All  button

Updates incosistent attributes of all schematic parts found with
"Attribute is not equal" error from CIS.

SailWind Logic Guide

611

SailWind Logic GUI Reference
Part Manager Dialog Box

Table  158. Part Manager Dialog Box Contents  (continued)

Name

Refresh  button

Description

Manually updates the comparision result if you change part
attributes in the design.

Comparision Results area

Displays what assigned to the part attributes in design and CIS
respectively, with differences highlighted in red. You can:

• Update the selected attribute: Right-click on the attribute cell

and click the Update Selected Attribute From CIS popup menu
item

• Update all attributes of the schematic part: Right-click and click

the Update Selected Part From CIS popup menu item

612

SailWind Logic Guide

SailWind Logic GUI Reference
SailWind Layout Link Dialog Box

## SailWind Layout Link Dialog Box

The SailWind Layout Link dialog box enables you to connect to SailWind Layout to automate sending
the netlist and passing design change annotations, and cross-probe (receive and send selections). This
feature also automates certain tasks for you, such as netlist comparisons and rules exports. Once you
connect to SailWind Layout, you can select objects in SailWind Layout and the object is automatically
selected and shown on its SailWind Logic schematic sheet (and vice versa).

See also Cross-Probe Between Sailwind Products.

The options you set in the SailWind Layout Link dialog box are saved to the registry. These options are
restored the next time you open the SailWind Layout Link.

Note:
The exception is the selection made in the Sent Selection list on the Selection  tab, and the
document pathname on the Document  tab.

SailWind Layout Link dialog box tabs:

SailWind Layout Link Dialog Box, Design Tab
SailWind Layout Link Dialog Box, Document Tab
SailWind Layout Link Dialog Box, ECO Names Tab
SailWind Layout Link Dialog Box, Preferences Tab
SailWind Layout Link Dialog Box, Selection Tab

SailWind Logic Guide

613

SailWind Logic GUI Reference
SailWind Layout Link Dialog Box, Design Tab

### SailWind Layout Link Dialog Box, Design Tab

To access: Tools  > SailWind Layout  menu item > connect to SailWind Layout using the Connect to
SailWind Layout Dialog Box  > Design  tab

Use the Design  tab of the SailWind Layout Link dialog box to export a netlist to SailWind Layout,
compare the schematic to the layout design, or forward and backward annotate design data.

Objects

Table  159. SailWind Layout Link Dialog Box, Design Tab Contents

Name

Description

Net list area

Send Netlist  button

Exports a netlist from the current schematic to the current SailWind Layout
design.

Results:

• If no errors are found in the netlist, SailWind Layout is updated.

• If errors are found in the netlist, the error report file is displayed in
a Notepad window, a link to the error file is displayed in the Output
Window, and you are asked whether you want to continue.

• If you click Yes, SailWind Layout is updated.

• If you click No, the operation is canceled and SailWind Layout is not

updated.

Include Design Rules in
Netlist check box

Select the check box to include design rules in the exported netlist.

 Tip
Before sending the netlist, run a connectivity report to check for possible
connectivity errors. For information, see Reports Dialog Box.

614

SailWind Logic Guide

Table  159. SailWind Layout Link Dialog Box, Design Tab Contents  (continued)

Name

Description

SailWind Logic GUI Reference
SailWind Layout Link Dialog Box, Design Tab

Compare/ECO area

Compare PCB  button

Compares the netlist of the current SailWind Logic schematic to the netlist of
the current SailWind Layout design.

Results:

• If no errors are found in either of the netlists, any differences are reported

in the default text editor.

• If errors are found in either of the netlists, the error report file is displayed

in a Notepad window, a link to the error file is displayed in the Output
Window, and you are asked whether you want to continue.
• If you click Yes, the comparison operation continues.

• If you click No, the operation is canceled.

See also SailWind Layout Link Dialog Box, Preferences Tab, SailWind
Layout Link Dialog Box, ECO Names Tab.

ECO To PCB  button

Compares the netlist in the current SailWind Logic schematic to the part and
netlist in the current SailWind Layout design.

Results:

• If no errors are found in either of the netlists, the SailWind Layout design

is updated.

 Tip
Overwriting of non-blank attribute values with blank attribute values
from the ECO file is allowed/prevented by the “Allow overwriting of
attribute values in design with blank values from library” check box in
the Design category  on page 591 of the Options dialog box.

• If errors are found in either of the netlists, the error report file is displayed

in a Notepad window, a link to the error file is displayed in the Output
Window, and you are asked whether you want to continue.
• If you click Yes, the SailWind Layout design is updated.

• If you click No, the operation is canceled, and SailWind Layout is not

updated.

See also SailWind Layout Link Dialog Box, Preferences Tab, SailWind
Layout Link Dialog Box, ECO Names Tab.

ECO From PCB  button

Compares the netlist in the current SailWind Logic schematic to the part and
netlist in the current SailWind Layout design.

Results:

• If no errors are found in either of the netlists, the SailWind Logic

schematic is updated.

 Tip
Overwriting of non-blank attribute values with blank attribute values
from the ECO file is allowed/prevented by the “Allow overwriting of
attribute values in design with blank values from library attributes”
check box in the Design category  on page 591 of the Options dialog
box.

SailWind Logic Guide

615

SailWind Logic GUI Reference
SailWind Layout Link Dialog Box, Design Tab

Table  159. SailWind Layout Link Dialog Box, Design Tab Contents  (continued)

Name

Description

• If errors are found in either of the netlists, the error report file is displayed

in a Notepad window, a link to the error file is displayed in the Output
Window, and you are asked whether you want to continue.

• If you click Yes, the SailWind Logic schematic is updated.

• If you click No, the operation is canceled, and SailWind Logic is not

updated.

See also SailWind Layout Link Dialog Box, Preferences Tab, SailWind
Layout Link Dialog Box, ECO Names Tab.

Compare Design Rules
check box

Includes design rules in the comparison that occurs when you select
Compare PCB, ECO to PCB, or ECO from PCB.

Show Net List errors
report check box

Select the check box to open the Net List errors report once it has been
generated. The filename is padsnet.err.

 Tip
If you clear the check box, you can still open the file from the link in the
Output window.

AI layout reference data

Select the check box in order for the AI Intelligent Layout  feature to work in
SailWind Layout.

Disconnect  button

Breaks the connection with SailWind Layout and closes the dialog box.

Related Topics

SailWind Layout Link Dialog Box

616

SailWind Logic Guide

SailWind Logic GUI Reference
SailWind Layout Link Dialog Box, Document Tab

### SailWind Layout Link Dialog Box, Document Tab

To access: Tools  > SailWind Layout  menu item > connect to SailWind Layout using the Connect to
SailWind Layout Dialog Box  > Document  tab

Use the Document  tab of the SailWind Layout Link dialog box to open and connect to a different design
or a new design file within the current SailWind Layout session. The current design path and filename is
listed at the top of this tab.

Figure 100. SailWind Layout Link Dialog Box, Document Tab

Objects

Table  160. SailWind Layout Link Dialog Box, Document Tab Contents

Name

Description

Pathname field

Displays the path and filename of the current SailWind Layout design.

New  button

Creates a new file within the current SailWind Layout session. SailWind Logic
automatically connects to this file.

 Tip
If the current SailWind Layout design has unsaved changes, a prompt
window appears, asking, “Remote PCB document is modified - Do you
want to save it?”.

Open  button

Enables you to locate and open an existing SailWind Layout file. SailWind
Logic automatically connects to this file.

 Tip
If the current SailWind Layout design has unsaved changes, a prompt
window appears, asking, “Remote PCB document is modified - Do you
want to save it?”.

Disconnect  button

Breaks the connection with SailWind Layout and closes the dialog box.

Related Topics

SailWind Layout Link Dialog Box

SailWind Logic Guide

617

SailWind Logic GUI Reference
SailWind Layout Link Dialog Box, ECO Names Tab

### SailWind Layout Link Dialog Box, ECO Names Tab

To access: Tools  > SailWind Layout  menu item > connect to SailWind Layout using the Connect to
SailWind Layout Dialog Box  > ECO Names  tab

Use the ECO Names tab of the SailWind Layout Link dialog box to manage options for the compare and
ECO functions on the Design  tab.

Note:
See also Design tab  on page 614.

Figure 101. SailWind Layout Link Dialog Box, ECO Names Tab

Objects

Table  161. SailWind Layout Link Dialog Box, ECO Names Tab Contents

Name

Description

Compare Names and Rename
Nets and Parts as Necessary

Compare differences using reference designators and net names.

 Tip

• Best used to minimize changes to routed traces.
• Selecting this option may result in the positional swapping of

parts.

Compare Names but Prefer
Add/Delete Parts to Renaming

Compare differences using reference designators and net names
on the basis that few reference designators have been renamed
and nets have not been renamed.

 Tip
Best used to minimize the positional swapping of parts, and the
design disruption that may result.

Compare Topology (not names).
Rename as Necessary.

Compare differences without using reference designators or net
names. Compare differences using pin names, part type names,
and so on.

618

SailWind Logic Guide

SailWind Logic GUI Reference
SailWind Layout Link Dialog Box, ECO Names Tab

Table  161. SailWind Layout Link Dialog Box, ECO Names Tab Contents  (continued)

Name

Description

 Tip
Best used to compare designs when parts and nets have
been renamed, and minimal interconnect changes have been
performed. For example, only an auto renumber has been
performed on the design.

Disconnect  button

Breaks the connection with SailWind Layout and closes the dialog
box.

Related Topics

SailWind Layout Link Dialog Box

SailWind Logic Guide

619

SailWind Logic GUI Reference
SailWind Layout Link Dialog Box, Preferences Tab

### SailWind Layout Link Dialog Box, Preferences Tab

To access: Tools  > SailWind Layout  menu item > connect to SailWind Layout using the Connect to
SailWind Layout Dialog Box  > Preferences  tab

Use the Preferences  tab of the SailWind Layout Link dialog box to manage options for the compare and
ECO functions on the Design  tab.

Note:
See also Design tab  on page 614.

Figure 102. SailWind Layout Link Dialog Box, Preferences Tab

Objects

Table  162. SailWind Layout Link Dialog Box, Preferences Tab Contents

Name

Description

Ignore Unused Pins Net
check box

Select to ignore the unused pins net in the original design and preserve the
existing unused pins net in the design you're updating. \

 Tip

• If you clear this option, the unused pins net may be deleted.
• The unused pins net contains pins that have no logical net

association.

• An unused pins net may be created by other software tools in the

PCB design process.

Name box

Type the name of the unused pins net.

 Restriction:
This box only becomes available if you select the Ignore Unused Pins
Net check box.

620

SailWind Logic Guide

Table  162. SailWind Layout Link Dialog Box, Preferences Tab Contents  (continued)

SailWind Logic GUI Reference
SailWind Layout Link Dialog Box, Preferences Tab

Name

Description

 Tip

• The maximum netname length is 47 characters.
• You can use any alphanumeric characters except curly braces { },

asterisks *, or spaces.

• The default name is NOT_CONNECTED.

Include Attributes area

Parts  — Controls whether part attributes are included in the netlist.

SailWind Logic evaluates parts that have different attributes as different
part types. Therefore, if you select Include Part Attributes when you
generate the netlist, you must also select Include Part Attributes when you
perform an ECO comparison. Otherwise the comparison considers the part
types to be different and reports errors.

Nets  — Controls whether net attributes are included in the netlist.

SailWind Logic checks net names on the schematic against the SailWind
Layout design. Therefore, if you select Include Net Attributes when you
generate the netlist, you must also select Include Net Attributes when you
perform an ECO comparison. Otherwise the comparison considers the net
types to be different and reports errors.

Compare PCB Decal
Assignments

Compares PCB decal assignments between the schematic and the design
in SailWind Layout. Updates decal assignments in SailWind Layout.

Disconnect  button

Breaks the connection with SailWind Layout and closes the dialog box.

SailWind Logic Guide

621

SailWind Logic GUI Reference
SailWind Layout Link Dialog Box, Selection Tab

### SailWind Layout Link Dialog Box, Selection Tab

To access: Tools  > SailWind Layout  menu item > connect to SailWind Layout using the Connect to
SailWind Layout Dialog Box  > Selection  tab

Use the Selection  tab of the SailWind Layout Link dialog box to manage the selections sent to and
received from SailWind Layout.

Figure 103. SailWind Layout Link Dialog Box, Selection Tab

Objects

Table  163. SailWind Layout Link Dialog Box, Selection Tab Contents

Name

Description

Sent Selection list

Contains a list of the objects currently selected in SailWind Logic.

Receive Selections
check box

Select to enable the SailWind Logic to automatically locate the item
corresponding to the SailWind Layout selection by changing schematic
sheets and selecting the item in SailWind Logic.

Disconnect  button

Breaks the connection with SailWind Layout and closes the dialog box.

Related Topics

SailWind Layout Link Dialog Box

622

SailWind Logic Guide

SailWind Logic GUI Reference
SailWind Router Link Dialog Box

## SailWind Router Link Dialog Box

You can link to and cross-probe with SailWind Router using the SailWind Router Link dialog box.
This function enables you to receive and send selections and start a new SailWind Router session or
document. Once you connect to SailWind Router, you can select objects in SailWind Router and the
object is automatically selected and shown on its SailWind Logic schematic sheet (and vice versa).

See also “Cross-Probe Between Sailwind Products”  on page 324.

SailWind Router Link dialog box tabs:

SailWind Router Link Dialog Box, Document Tab
SailWind Router Link Dialog Box, Selection Tab

SailWind Logic Guide

623

SailWind Logic GUI Reference
SailWind Router Link Dialog Box, Document Tab

### SailWind Router Link Dialog Box, Document Tab

To access: Tools  > SailWind Router  menu item > connect to SailWind Router using the Connect to
SailWind Router Dialog Box  > Document  tab

Use the Document  tab of the SailWind Router Link dialog box to open and connect to a different design
or a new design file within the current SailWind Router session. The current design path and filename is
listed at the top of this tab.

Figure 104. SailWind Router Link Dialog Box, Document Tab

Objects

Table  164. SailWind Router Link Dialog Box, Document Tab Contents

Name

Description

Pathname field

Displays the path and filename of the current SailWind Router design.

New  button

Creates a new file within the current SailWind Router session. SailWind Logic
automatically connects to this file.

 Tip
If the current SailWind Router design has unsaved changes, a prompt
window appears, asking, “Remote PCB document is modified - Do you
want to save it?”.

Open  button

Enables you to locate and open an existing SailWind Router file. SailWind
Logic automatically connects to this file.

 Tip
If the current SailWind Router design has unsaved changes, a prompt
window appears, asking, “Remote PCB document is modified - Do you
want to save it?”.

Disconnect  button

Breaks the connection with SailWind Router and closes the dialog box.

Related Topics

SailWind Router Link Dialog Box

624

SailWind Logic Guide

SailWind Logic GUI Reference
SailWind Router Link Dialog Box, Selection Tab

### SailWind Router Link Dialog Box, Selection Tab

To access: Tools  > SailWind Layout  menu item > connect to SailWind Router using the Connect to
SailWind Router Dialog Box  > Selection  tab

Use the Selection  tab of the SailWind Router Link dialog box to manage the selections sent to and
received from SailWind Router.

Figure 105. SailWind Router Link Dialog Box, Selection Tab

Objects

Table  165. SailWind Router Link Dialog Box, Selection Tab Contents

Name

Description

Sent Selection list

Contains a list of the objects currently selected in SailWind Logic.

Receive Selections
check box

Select to enable the SailWind Logic to automatically locate the item
corresponding to the SailWind Router selection by changing schematic
sheets and selecting the item in SailWind Logic.

Disconnect  button

Breaks the connection with SailWind Router and closes the dialog box.

Related Topics

SailWind Router Link Dialog Box

SailWind Logic Guide

625

SailWind Logic GUI Reference
SailWind Suite Configuration Dialog Box

## SailWind Suite Configuration Dialog Box

To access:

• Help  > Installed Options  menu item > Suite Configuration  button

• Optional: Opens on program startup

Use the SailWind Suite Configuration dialog box to manage SailWind Suite (composite) licenses.

Objects

Field

Description

Control suite license checkout and
select from the following list

Enables the Suite License table for you to control checkouts.

Suite Name column

Lists the name of the suite for which the license works.

License Feature column

Lists the specific features available for each license.

License status column

Lists the status of the licenses when you click the Check status
button.

Check Status button

Specifies to check the status of all licenses listed in the table and
displays the status in the License status column.

626

SailWind Logic Guide

Field

Description

Reset List button

Specifies to reset the list of suite licenses to only those detected in
your licensing environment.

SailWind Logic GUI Reference
SailWind Suite Configuration Dialog Box

Move up button

Moves the selected license up one row.

Move down button

Moves the selected license down one row.

Select all button

Selects all of the listed licenses.

Select none button

Deselects all of the listed licenses.

Show this dialog box on program
startup

Specifies to open the SailWind Suite Configuration dialog box
when SailWind Layout starts.

Automatically check license status
on dialog box startup

Specifies to check the status of the licenses when you open the
SailWind Suite Configuration dialog box.

SailWind Logic Guide

627

SailWind Logic GUI Reference
Part Attributes Dialog Box

## Part Attributes Dialog Box

To access: Select a part > right-click > Attributes  menu item

Use the Part Attributes dialog box to assign or modify part attributes, which is information about the part
such as manufacturer and cost.

Tip
Adding or changing attributes in a part at the schematic level does not update the part type (in the
library). Edit the part in the Part Editor to update the library part.

Figure 106. Part Attributes Dialog Box

Objects

Table  166. Part Attributes Dialog Box Contents

Name

Description

Attributes table

Lists the name and value of the attributes of the selected part.

Browse Lib Attr  button

Opens the Browse Library Attributes Dialog Box.

Add  button

Delete  button

Edit  button

Adds a row to the end of the Attributes table where you can add a
new attribute.

Removes the selected row from the Attributes table.

Makes the selected cell available for editing.

Apply update to area

Specifies how parts are updated:

• This Part  — Only updates the selected part.

• All Parts This Type  — Updates all matching parts in the

design

628

SailWind Logic Guide

Related Topics

Modifying Part Attributes

SailWind Logic GUI Reference
Part Attributes Dialog Box

SailWind Logic Guide

629

SailWind Logic GUI Reference
Part Information Dialog Box

## Part Information Dialog Box

Use the part information dialog box to create or edit part types.

Part Information dialog box tabs:

Part Information Dialog Box, Attributes Tab
Part Information Dialog Box, Connector Tab
Part Information Dialog Box, Gates Tab
Part Information Dialog Box, General Tab
Part Information Dialog Box, PCB Decals Tab
Part Information Dialog Box, Pin Mapping Tab
Part Information Dialog Box, Pins Tab

630

SailWind Logic Guide

SailWind Logic GUI Reference
Part Information Dialog Box, Attributes Tab

### Part Information Dialog Box, Attributes Tab

To access: Tools  > Part Editor  menu item > Edit Electrical  button > Attributes  tab

Use the Attributes  tab of the Part Information dialog box to manage attributes for the selected part, and
to define default attributes for new parts.

Figure 107. Part Information Dialog Box - Attributes Tab

Objects

Name

Attribute table

Table  167. Part Information Dialog Box - Attributes Tab Contents

Description

• Attribute column  — The name of the Attribute.

• Value column  — The value of the Attribute.

Save As Default  button

Saves the current attribute list as the default for all new attributes.

 Tip
The Attribute name is saved, but not the Attribute value.

Reset  button

Edit  button

Undoes all changes you made in the Attributes  tab.

Makes the selected cell available for editing.

SailWind Logic Guide

631

SailWind Logic GUI Reference
Part Information Dialog Box, Attributes Tab

Table  167. Part Information Dialog Box - Attributes Tab Contents  (continued)

Name

Description

Result:  The attribute is edited for only the selected part. To
manage attributes design-wide or in all libraries, use the Manage
Library Attributes Dialog Box.

 Tip
You can also double-click a cell to edit its contents.

See also Managing Attributes.

Add  button

Adds a new row for a new attribute at the bottom of the table.

Result:  The new attribute is added to the Part Type Level of the
attribute hierarchy. For more information, see Attribute Hierarchy  in
the SailWind Layout Guide.

 Tip
After you type the new attribute name, press the Tab key or
double-click in the value field to type the value.

Removes the selected row.

Places the selected cell information in the paste buffer.

 Tip
You can also copy from Microsoft Excel.

Pastes the information from the paste buffer. The selected cell in
the table is the paste origin. Data is pasted below and to the right
of the paste origin.

Delete  button

Copy  button

Paste  button

Browse Lib. Attr  button

Opens the Browse Library Attributes Dialog Box  where you can
browse for an existing library attribute.

Check Part  button

Checks for missing or inconsistent information.

 Tip
Even if you don't click the Check Part  button, when you exit
the tab, the assigned decals are checked to ensure that they
contain physical pin numbers for all the gate and signal pins
defined in the Pins  tab.

Related Topics

Managing Attributes

632

SailWind Logic Guide

SailWind Logic GUI Reference
Part Information Dialog Box, Connector Tab

### Part Information Dialog Box, Connector Tab

To access: Tools  > Part Editor  menu item > Edit Electrical  button > Connector  tab

Use the Connector  tab to define the alternate Logic decals to display in a schematic. Decals are referred
to as Special Symbols. You can associate a logical Pin Type with each alternate so that you can have a
graphical indication of the connector pin function in the schematic.

Restriction:
The Connector  tab is available only when you open an existing connector or create a new
connector.

Tip
Many users like to use a different symbol, or decal, to distinguish between input (Source) and
output (Load) pins. You may define multiple symbols for each of the ten different pin types.

Figure 108. Part Information Dialog Box - Connector Tab

SailWind Logic Guide

633

SailWind Logic GUI Reference
Part Information Dialog Box, Connector Tab

Objects

Name

Picture

Attribute table

Table  168. Part Information Dialog Box - Connector Tab Contents

Description

Displays a picture of the selected Special Symbol.

• Special Symbol  — The name of a connector pin decal for use in the

schematic.

• Pin Type  — The function of the special symbol.

Opens the Browse for Special Symbols Dialog Box  where you can browse
for a pin decal.

Reset  button

Undoes all changes you made in the Connector  tab.

Edit  button

Makes the selected cell available for editing.

 Tip
You can also double-click the cell to edit the contents.

Add  button

Adds a new row at the bottom of the table.

Delete  button

Removes the selected row.

Check Part  button

Checks for missing or inconsistent information.

 Tip
Even if you don't click the Check Part  button, when you exit the tab,
the assigned decals are checked to ensure that they contain physical
pin numbers for all the gate and signal pins defined in the Pins  tab.

Related Topics

Assigning Alternate Logic Decals for Connector Symbols

634

SailWind Logic Guide

SailWind Logic GUI Reference
Part Information Dialog Box, Gates Tab

### Part Information Dialog Box, Gates Tab

To access: Tools  > Part Editor  menu item > Edit Electrical  button > Gates  tab

Use the Gates  tab of the Part Information dialog box to assign gate information to a part, including the
number of gates, gate swap information, and CAE Decals for the part.

Tip
A space and a period (.) are illegal characters for pin names.

Figure 109. Part Information Dialog Box - Gates Tab

Objects

Name

Preview area

Reset  button

Edit  button

Table  169. Part Information Dialog Box - Gates Tab Contents

Description

Shows the item selected in the Decal cell.

Undoes all changes you made in the Gates  tab.

Makes the selected cell available for editing. Also displays the
Browse  button.

SailWind Logic Guide

635

SailWind Logic GUI Reference
Part Information Dialog Box, Gates Tab

Table  169. Part Information Dialog Box - Gates Tab Contents  (continued)

Name

Description

Add  button

Delete  button

Gate table

Opens the Assign Decal to Gate Dialog Box.

 Tip
This button is available only in the CAE Decal columns, and
only when the cell is available for editing.

Adds a new row with the next Gate letter at the bottom of the Gate
table.

Removes the selected row from the Gate table.

• Gate column  — Displays the letter of the gate.

• Pins column  — Displays the number of pins for the gate. Gate

pins are added on the Pins  tab.

• Swap column  — Displays the swap ID from 0 to 100. To

uncross connections and facilitate routing, gates with the same
swap ID (except for 0) can be swapped within a part or with
another part of the same type.

To disable swapping, type 0.

• CAE Decal N  column  — Displays the CAE Decal name. The
decal listed for CAE Decal 1 is the default decal and is used
when you add the part to the schematic. Additional decals are
alternates. You can assign up to four CAE decals to a part.

 Tip
Double-click to Type a decal name or click the
“...” (Browse) button to search for a decal from a library

Check Part  button

Checks for missing or inconsistent information.

 Tip
Even if you don't click the Check Part  button, when you exit
the tab, the assigned decals are checked to ensure that they
contain physical pin numbers for all the gate and signal pins
defined in the Pins  tab.

Related Topics

Assigning Gates to Parts

636

SailWind Logic Guide

SailWind Logic GUI Reference
Part Information Dialog Box, General Tab

### Part Information Dialog Box, General Tab

To access: Tools  > Part Editor  menu item > Edit Electrical  button > General  tab

Use the General  tab of the Part Information dialog box to view part statistics and set family information.

Figure 110. Part Information Dialog Box - General Tab

Objects

Table  170. Part Information Dialog Box - General Tab Contents

Name

Description

Part Statistics area

Pin Count

Decal

Gate Count

Displays the total number of pins in the part. Includes gate pins,
signal pins, and unused pins. If multiple decals are assigned with
different pin counts, a range of smallest to largest decal pin counts
is shown.

Displays the name of the decal, as chosen on the PCB Decals  tab.

Displays how many gates exist in the part.

Signal Pin Count

Displays the number of signal pins in the part.

SailWind Logic Guide

637

SailWind Logic GUI Reference
Part Information Dialog Box, General Tab

Table  170. Part Information Dialog Box - General Tab Contents  (continued)

Name

Description

Logic Family area

Logic Family list

Ref Prefix

Families  button

Options area

Specifies the Logic Family (reference designator prefix) to use for
the part. You can also create a new logic family or edit the existing
reference designator prefix designations by clicking the Families...
button.

 Note:
Beginning with PADS 9.0, die parts and flip chips are no longer
identified by their family designations (DIE or FLP), but instead
by the Special Purpose settings on this tab. With this change,
you can assign any reference designator (logic family) to a die
part or flip chip without losing the special properties of these
parts (such as the ability to move the part's substrate bond
pads in the schematic).

Displays the reference designator prefix for the selected logic
family.

Opens the Logic Families dialog box  on page 561where you can
add, edit, or delete a logic family.

Define mapping of Part Type pin
numbers to PCB Decal

Activates the Pin Mapping  tab where you can map logical pin
numbers to different physical pin numbers.

 Restriction:

• The check box is unavailable once you add one or more

alphanumeric decals to the part type. Remove the assigned
alphanumeric decal to make the check box available.
The check box also becomes available if you assign a
numeric decal. However, you will still need to remove the
alphanumeric decal from the list to make the part valid.

• You must assign a decal to use the Pin Mapping  tab.
• Only decals with sequential numerical pin numbers can be

used with pin mapping.

Enables a part to be passed between the design and schematic file
for forward and backward annotation. By default, all existing part
types in your design are ECO registered.

 Tip
Typically you do not select this check box for non-electrical
parts. For example, if you create and add a mounting hole to
your design in the layout software, you would not need the
part (mounting hole) to pass back to your schematic when you
perform a backward annotation of the design.

Specifies to apply the part information edits to other parts in the
library. Type the prefixes and wildcards that match the names of
the other parts to update.

ECO Registered Part

Prefix List

638

SailWind Logic Guide

Table  170. Part Information Dialog Box - General Tab Contents  (continued)

Name

Description

SailWind Logic GUI Reference
Part Information Dialog Box, General Tab

 Note:
Examples:

• Question mark ? in a prefix acts as a wildcard for one

character. The prefix “?4” is the equivalent of “54” or “74”.

• If you type “\02” as the suffix, the edits are applied to all

parts ending in 02.

 Note:
Warning:  The contents of the Prefix List box are applied when
you click OK  or Save As on other tabs in the Part Information
dialog box.

Special Purpose

Identifies the part as one of the following types:

• Connector  — In contrast to other part types, connectors do not

require a prefix list, or gate definitions.

 Restriction:

◦ This check box is automatically selected when you create
or modify connectors. It is unavailable if you open a part
other than a connector.

◦ This check box is unavailable when the part already has

◦ The Gate Decals  tab is unavailable when the Connector

◦ Some Pins  tab controls not applicable to connector parts

gate or pin assignments.

check box is selected.

are disabled.

• Die Part — See the following note.

• Flip Chip  — See the following note.

 Note:
Beginning with PADS 9.0, die parts and flip chips are identified
by the Special Purpose settings in the Part Type rather than by
the DIE and FLP logic families. With this change, any reference
designator (logic family) can be assigned to a die part or flip
chip.

Check Part  button

Checks for missing or inconsistent information.

 Tip
Even if you don't click the Check Part  button, when you exit
the tab, the assigned decals are checked to ensure that they
contain physical pin numbers for all the gate and signal pins
defined in the Pins  tab.

Related Topics

Viewing and Setting General Part Information

SailWind Logic Guide

639

SailWind Logic GUI Reference
Part Information Dialog Box, PCB Decals Tab

### Part Information Dialog Box, PCB Decals Tab

To access: Tools  > Part Editor  menu item > Edit Electrical button > PCB Decals  tab

Use the PCB Decals  tab of the Part Information dialog box to assign decals, or footprints, to library parts.

Figure 111. Part Information Dialog Box - PCB Decals Tab

Objects

Name

Preview area

Library list

Filter

Pin Count

Table  171. Part Information Dialog Box - PCB Decal Tab Contents

Description

Displays the item selected in the Assigned Decals list.

Lists all your available libraries. Filters the Unassigned Decals list
to only the selected library.

Searches the chosen library (or libraries) for a specific part or item
name, or names that match a wildcard or expression  on page 105.
Type * to view all parts or items in the chosen libraries. Click Apply
to search the libraries and display the search results.

Narrows down your unassigned decals list by displaying only the
decals with the specified number of pins.

640

SailWind Logic Guide

SailWind Logic GUI Reference
Part Information Dialog Box, PCB Decals Tab

Table  171. Part Information Dialog Box - PCB Decal Tab Contents  (continued)

Name

Description

 Tip
Delete all numbers in the Pin Count box to display all decals.
This box is always available as a filter to enable decals of
differing pin counts to be assigned.

Show only Decals with pin
numbers matching Part Type

Filters out decals that do not have pin numbers matching existing
gate and signal pins on the Pins  tab, or the physical pin numbers
on the Pin Mapping  tab.

Unassigned Decals list

Lists all of the available decals to assign to the part.

Assign >>  button

Moves the selected decal from the Unassigned Decals list to the
Assigned Decals list.

<< Unassign  button

Assigned Decals list

Assign New  button

 Restriction:

• You must assign a decal with enough pins for all the defined

gate pins and signal pins on the Pins  tab.

• Only decals with sequential numerical pin numbers can be

used with pin mapping.

Moves the selected decal from the Assigned Decals list to the
Unassigned Decals list.

Lists all assigned decals. Assigned PCB decals can have a
different number of pins, but you must assign a decal with enough
pins for all the defined gate pins and signal pins on the Pins  tab.

You can assign up to 16 PCB decals to a part.

 CAUTION:
Decals are switched to alternates using the Component
Properties dialog box and can be changed outside of ECO
mode. An .eco file created by the ECO toolbar will not contain
decal changes to alternates.Use the Compare/ECO dialog box
to create an .eco file that lists changes to alternate decals.

 Tip

• The decal at the top of the list is the default decal and is

used when you add the part to the design.

• When you assign a decal, the pin numbers from the decal
are automatically populated into the Pins  tab table. PCB
Decal pin numbers can be alphanumeric or numeric and the
pin numbers in the PCB Decal must match the pin numbers
listed in the Pins  tab table.

Opens the New PCB Decal dialog box  on page 469where you can
type the name for a decal that does not yet exist in a library. To use
this part in a design, you must either acquire or create this decal.

 Restriction:
When you assign a decal that exists, it pre-populates the Pins
tab  on page 645 with pin numbers. When you assign a new
PCB decal, you must enter the pin numbers manually.

Up/Down  buttons

Moves the selected Decal up or down.

SailWind Logic Guide

641

SailWind Logic GUI Reference
Part Information Dialog Box, PCB Decals Tab

Table  171. Part Information Dialog Box - PCB Decal Tab Contents  (continued)

Name

Description

Check Part button

Checks for missing or inconsistent information.

 Tip
Even if you don't click the Check Part  button, when you exit
the tab, the assigned decals are checked to ensure that they
contain physical pin numbers for all the gate and signal pins
defined in the Pins  tab.

Related Topics

Assigning PCB Decals

642

SailWind Logic Guide

SailWind Logic GUI Reference
Part Information Dialog Box, Pin Mapping Tab

### Part Information Dialog Box, Pin Mapping Tab

To access: Tools  > Part Editor  menu item > Edit Electrical  button > General  tab. On the General  tab,
select the “Define mapping of Part Type pin numbers to PCB Decal” check box to make the Pin Mapping
tab available. On the PCB Decals  tab, assign a decal with sequential numerical pin numbers to use the
Pin Mapping  tab. The decal determines the number of pins in the part.

Use the Pin Mapping  tab of the Part Information dialog box to overlay alphanumeric pin numbers onto
numeric PCB decal pins. Prior to PADS 2007, alphanumeric pin numbers could not be saved in PCB
decals.

Figure 112. Part Information Dialog Box - Pin Mapping Tab

Objects

Name

Decal list

Table  172. Part Information Dialog Box - Pin Mapping Tab Contents

Description

Lists the decals available to you for which you can map
alphanumeric pins.

Reset  button

Undoes all changes you made in the Pin Mapping  tab.

Unmapped Pins list

Lists all unmapped pins available to map in the Mapping table.

Map >> button

Moves the selected pin from the Unmapped pins list to the
selected cell in the Mapping table.

SailWind Logic Guide

643

SailWind Logic GUI Reference
Part Information Dialog Box, Pin Mapping Tab

Table  172. Part Information Dialog Box - Pin Mapping Tab Contents  (continued)

Name

Description

<< Unmap  button

Mapping table

Moves the selected decal number from the Mapping table to the
Unmapped Pins list.

• Decal column  — The number of the Decal.

• Part Type column  — The value of the Attribute.

Edit  button

Makes the selected cell available for editing.

 Tip
You can also double-click the cell to edit the contents.

Copy Map  button

Places the map information into the paste buffer to paste into
Microsoft Excel where you can make mass edits.

 Restriction:
Copy Map  only works with the whole pin mapping table and
not selective rows.

Paste Map  button

Pastes the map information from the paste buffer.

 Restriction:
Paste Map  only works with the whole pin mapping table and
not selective rows.

Preview area

Shows the item selected in the Decal list.

You can assign unmapped pins to decal pins by selecting the pins
in the preview window. Select an alphanumeric in the Unmapped
Pins list and double-click the pin in the decal preview window to
map the alphanumeric to the pin. The next row in the Unmapped
Pins list becomes the next selected alphanumeric for mapping.

In the preview window, you can click and drag to define a zoom
box, or use Shift+click or Shift+right-click to zoom in or out by a
factor of two. You can zoom in up to 16X the original scale. The
preview window will only zoom out to fit the decal entirely in the
view.

Check Part  button

Checks for missing or inconsistent information.

 Tip
Even if you do not click the Check Part  button, when you exit
the tab, the assigned decals are checked to ensure that they
contain physical pin numbers for all the gate and signal pins
defined in the Pins  tab.

Related Topics

Part Information - Pin Mapping

644

SailWind Logic Guide

SailWind Logic GUI Reference
Part Information Dialog Box, Pins Tab

### Part Information Dialog Box, Pins Tab

To access: Tools  > Part Editor  menu item > Edit Electrical  button > Pins  tab

Use the Pins  tab of the Part Information dialog box to assign gate pins, signal pins, and unused pins to
the part. Pin numbers added to the Pins  tab, must match those of the PCB Decal. Use the Pin Mapping
tab to overlay logical (schematic) alphanumeric pin numbers onto the physical numeric PCB decal.

Objects

Name

Pins Table

Description

Double-click a column to sort the column by ascending order.

 Tip
Sorting by pin Sequence number or Pin Group has the same
effect, it sorts by Pin Group and then by sequence number
within each gate.

Pin Group column

Select from Gate, Signal Pin, Connector Pin or Unused Pin.

• Gate Pins  — Assign to gates you’ve added to the part on the

Gates tab  on page 635.

• Signal Pins  — Assign to implicit pins (pins which are not

displayed on any gate in the schematic). Typically, ground and
power pins are the only implicit pins. You are not required to
use Signal Pins. Instead, you can add power and ground pins
to a gate or create a separate gate for power and/or ground

SailWind Logic Guide

645

SailWind Logic GUI Reference
Part Information Dialog Box, Pins Tab

Name

Description

pins. For the parts in the libraries shipped with SailWind Logic,
the standard ground signal name is GND. The standard power
signal name is +5V.

• Connector Pins  — Assign to connector pins instead of using
Gate pins. With a connector, every pin is its own gate in order
to spread each connector pin throughout the schematic as
needed, instead of having to create gates for each pin. You
designate a part type as a connector on the General tab  on
page 637.

• Unused Pins  — You can assign a pin to be an unused pin. An
unused pin is a pin that is defined in a PCB decal but has no
electrical function in the part type. The unused pin information
is not saved in the part type, but is derived automatically based
on the number of assigned gate and signal pins to the number
of pins in the assigned PCB decal.

Number column

Specifies the pin number for the pin.

 Note:
Requirement:  The pin number must match the PCB decal. For
example, alphanumeric to alphanumeric.

Name column

Specifies the pin signal or function name of the pin.

 Note:
Requirement:  The pin must have a name to be valid.

Type column

Specifies the type of pin.

 Tip
This column is used with gate pins only.

Swap column

Specifies an identical number between pins that can be swapped.

Seq. column

Specifies the sequence number.

 Tip
Type 0 to disable swapping.

Reset  button

Edit  button

 Tip
The sequence number determines the mapping of CAE gate
pins to PCB decal pins. The sequence is automatically shared
with alternate CAE decals. For example, it shows how pin
numbers appear on the CAE gate decal; therefore, in Gate A,
sequence number 1 could be pin 1, but in Gate B, sequence
number 1 would be pin 4.

Undoes all changes you made in the Pins  tab.

Makes the selected cell available for editing. Press Ctrl or Shift and
click to select multiple cells from the same column, then click Edit
to make the same changes to the selected cells. The action of the
Edit  button depends on the cells you select:

• Pin Group column  — Opens the Update Pin Gate dialog box.

• Number column  — Opens the Renumber Pins dialog box.

646

SailWind Logic Guide

Name

Description

SailWind Logic GUI Reference
Part Information Dialog Box, Pins Tab

Add Pin  button

• Name column  — Opens the Update Pin Name dialog box.

• Type column  — Opens the Update Pin Type dialog box.

• Swap column  — Opens the Update Pin Swap dialog box.

• Seq. column  — Not available for multiple cell edits.

Adds a new row below the selected row. If it's the first pin to be
added it takes the default of belonging to Gate-A. If pins already
exist, the new pin takes the Pin Group of the currently selected pin.

 Note:
Requirement: You must add a pin number to make the pin
valid.

 Tip

• You can add all pins automatically by adding a decal.
• To add a series of pins, click the Add Pins  button.
• To import pins using a comma separated value (.csv) file,

click the Import CSV  button.

Add Pins  button

Opens the Add Pins Dialog Box.

 Note:
Restriction:  Total pins for the part can not exceed 32,767 pins.

 Tip

• You can add all pins automatically by adding a decal.
• To add a single pin, click the Add Pin  button.
• To import pins using a comma separated value (.csv) file,

click the Import CSV  button.

Delete Pins  button

Removes the selected row.

Renumber  button

Opens the Renumber Pins Dialog Box.

Copy  button

Places the selected cell information in the paste buffer.

Paste  button

 Tip
You can also copy from Microsoft Excel.

Pastes the information from the paste buffer. The selected cell in
the table is the paste origin. Data is pasted below and to the right
of the paste origin.

 Restriction:
When the pasted data includes either Pin Group or Pin Number
data, extra pin rows are added automatically, otherwise the
paste will fail if the number of rows and columns in the pasted
data does not match those available in the table below and to
the right of the paste origin.

Import CSV  button

Opens the Library Import File dialog box where you select the .csv
file to import.

SailWind Logic Guide

647

SailWind Logic GUI Reference
Part Information Dialog Box, Pins Tab

Name

Description

 Tip

• The entire contents of the Pins  tab table is replaced with the

data of the CSV file.

• CSV field names must correspond to the column headers
in the Pins  tab table. Only the first two characters of the
header must match. For example, “Pi” for the Pin Group
column. Gate or “Ga” are acceptable alternatives to the Pin
Group header.

• The sample Part_Pins_Template.csv  file is located in your

Check Part  button

Checks for missing or inconsistent information.

\SailWind Projects\Samples  folder.

 Tip
Even if you don't click the Check Part  button, when you exit
the tab, the assigned decals are checked to ensure that they
contain physical pin numbers for all the gate and signal pins
defined in the Pins  tab.

Related Topics

Part Information - Pins

648

SailWind Logic Guide

SailWind Logic GUI Reference
Part Properties Dialog Box

## Part Properties Dialog Box

To access: Select a part > right-click > Properties  menu item

Use the Part Properties dialog box to create and edit part attributes. You can also define signal pins and
control the visibility of attributes assigned to the part.

Tip
This dialog box contains several sub-dialog boxes. Before using any of these sub-dialog boxes,
changes made in open dialog box must be applied to the design.

Figure 113. Part Properties Dialog Box

Objects

Table  173. Part Properties Dialog Box Contents

Name

Description

Reference Designator

Displays the name of the reference of the selected part.

Rename Gate  button

Opens the Rename Gate Dialog Box.

Rename Part  button

Opens the Rename Part Dialog Box.

Part Type

Displays the type of the selected part.

SailWind Logic Guide

649

SailWind Logic GUI Reference
Part Properties Dialog Box

Table  173. Part Properties Dialog Box Contents  (continued)

Name

Description

Change Type  button

Opens the Change Part Type Dialog Box.

Part Information area

Displays the PCB Decal, pin count, Logic Family, if the part is ECO
registered, the signal pin count, the gate count, and the number of
unused pins.

Statistics  button

Gate Decal list

Displays gate and connection information for the selected part.
This information is displayed in the default text editor so you can
save the contents to a file.

Specifies the gate decal. Select a gate decal name from the Gate
Decal list to change the gate decal of the selected gate or part to
one of the predefined alternate decals

Visibility  button

Opens the Part Text Visibility Dialog Box.

Attributes  button

Opens the Part Attributes Dialog Box.

PCB Decals  button

Opens the PCB Decal Assignment Dialog Box.

SigPins  button

Opens the Part Signal Pins Dialog Box.

Related Topics
Modifying Parts

650

SailWind Logic Guide

SailWind Logic GUI Reference
Part Signal Pins Dialog Box

## Part Signal Pins Dialog Box

To access: Select a part > right-click > Properties  > SigPins button

Use the Part Signal Pins dialog box to assign any unused pins as additional signal pins. When the part
type is created and stored in the library, the standard power and ground pins for part types are defined.
Signal pins assigned during part creation cannot be modified through this dialog box. Instead, use the
Assigning Signal Pin Names to Parts dialog box in the Library Manager.

Tip
The Part Signal Pins dialog box lists pins and their corresponding signal names. A signal pin is a
pin that has a signal net (GND for example) assigned by a schematic capture program during part
type creation.

Figure 114. Part Signal Pins Dialog Box

Objects

Table  174. Part Signal Pins Dialog Box Contents

Name

Description

Unused Pins list

Lists all of the unused pins for the selected part.

Add >>  button

Adds the selected unused pin to the Signal Pins table

<< Remove  button

Removes the selected Signal Pin to the Unused Pins list.

Edit  button

Makes the selected cell available for editing.

Signal Pins table

Lists the signal pin number and corresponding name.

Apply update to area

Specifies how parts are updated:

SailWind Logic Guide

651

SailWind Logic GUI Reference
Part Signal Pins Dialog Box

Table  174. Part Signal Pins Dialog Box Contents  (continued)

Name

Description

• This Part  — Only updates the selected part.

• All Parts This Type  — Updates all matching parts in the

design

Related Topics
Modifying Parts

652

SailWind Logic Guide

SailWind Logic GUI Reference
Part Text Visibility Dialog Box

## Part Text Visibility Dialog Box

To access: Select a part > right-click > Visibility  menu item

Use the Part Text Visibility dialog box to control the display of text associated with the selected part. You
can control the visibility of one part or all parts of the same type.

Figure 115. Part Text Visibility Dialog Box

Objects

Table  175. Part Text Visibility Dialog Box Contents

Name

Description

Item Visibility area

Specifies the visibility of the items: click to make the item visible;
click to clear to make the item invisible.

Attribute Name Display area

Specifies the attribute name option. Display just the attribute's
value or display the attribute name and its value.

• All Off  — Makes all attribute names invisible, displays only the

value.

• No Change  — Keeps the current attribute name visibility

settings.

• All On  — Displays all attribute names and their values.

Apply Update to area

Specifies the selected part update options.

SailWind Logic Guide

653

SailWind Logic GUI Reference
Part Text Visibility Dialog Box

Table  175. Part Text Visibility Dialog Box Contents  (continued)

Name

Description

• This Gate  — Updates the selected gate.

• This Part  — Updates a part or all associated gates of a part.

• All Part This Type  — Updates all matching gates or parts in

the design.

 Restriction:
This area is unavailable when more than one part is selected.

Attributes list

Specifies the attributes you want to display in the schematic.

Related Topics

Controlling Text Visibility for a Part

654

SailWind Logic Guide

SailWind Logic GUI Reference
Part Type Label Properties Dialog Box

## Part Type Label Properties Dialog Box

To access: Select a part type label > right-click > Properties  menu item

Use the Part Type Label Properties dialog box to provide text and font settings for one or more part type
labels.

Figure 116. Part Type Label Properties Dialog Box

Objects

Name

Name

Table  176. Part Type Label Properties Dialog Box Contents

Description

The name of the selected attribute.

Change Type  button

Opens the Change Part Type Dialog Box.

Rotation

Size

Specifies the rotation of the label: 0 or 90 degrees.

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

SailWind Logic Guide

655

SailWind Logic GUI Reference
Part Type Label Properties Dialog Box

Table  176. Part Type Label Properties Dialog Box Contents  (continued)

Name

Description

Line Width

Specifies the line width for stroke fonts only.

Font list

The fonts available to you. This lists either stroke fonts or system
fonts.

You choose which type of font to use in the Fonts Dialog Box.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles: B  for bold, I  for italic, or U  for
underlined.

Horizontal/Vertical Justification

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Related Topics

Modifying Part Type Labels

656

SailWind Logic Guide

SailWind Logic GUI Reference
Pen Plotter Advanced Setup Dialog Box

## Pen Plotter Advanced Setup Dialog Box

To access: File  > Plot  menu item > select Pen Plot > Setup  button > Advanced  button

Use the Pen Plotter Advanced Setup dialog box to add a new pen plotter to the list of available plotters.

Figure 117. Pen Plotter Advanced Setup Dialog Box

Objects

Table  177. Pen Plotter Advanced Setup Dialog Box Contents

Name

Description

Plotter Device Name

Specifies the name of a different pen plotter you want to use.

 Note:
Exception:  Do not reuse one of the existing, supplied device
names.

Device Type list

Specifies the interface language the plotter uses: HPGL or HGML.

Plotter Units area

Specifies the plotter resolution as a scaling ratio using the numbers
in the Multiplier and Divisor boxes. The ratio defined is the scale
factor to convert from mils (0.001 in) to plotter units.

 Note:
Example:  Most Hewlett-Packard plotters have a resolution of
0.025 mm or 1/40 mm. This means that a distance of one inch
(1000 mils) is 1016 plotter units (25.4 X 40). So a ratio of 1016
to 1000 would be defined. The ratio actually used is 254 to 250
which is the same as 1016 to 1000.

Origin at Center

Specifies that the origin of the plotter is at the center of the paper.

 Tip
Clear this check box if the origin is in the lower left corner or
other location.

Related Topics

Pen Plotter Setup Dialog Box

SailWind Logic Guide

657

SailWind Logic GUI Reference
Pen Plotter Setup Dialog Box

## Pen Plotter Setup Dialog Box

To access: File  > Plot  menu item > select Pen Plot > Setup  button

Use the Pen Plotter Setup dialog box to set various options for the plotter.

Figure 118. Pen Plotter Setup Dialog Box

Objects

Table  178. Pen Plotter Setup Dialog Box Contents

Name

Description

Number of Pens

Specifies the number of pens (1-16) in your device.

Pen Line Width

Specifies the pen line width in mils.

Rotate Axis

Pen Colors

Specifies to reverse the X and Y axes of the design.

Specifies the color of each pen.

 Tip
Select the color in the Selected Color area and then click the
tile for each pen number in the Pen Colors area.

Selected Color

The area where you select the color you want for each pen color.

Plotting size area

Specifies the size of the plot. A through E and Other in inches; A4
through A0 and Other in millimeters.

Device

658

 Tip
If you click Other, specify the X and Y dimensions.

Specifies the Plotter device to use.

SailWind Logic Guide

Table  178. Pen Plotter Setup Dialog Box Contents  (continued)

Name

Description

Advanced  button

Opens the Pen Plotter Advanced Setup Dialog Box.

SailWind Logic GUI Reference
Pen Plotter Setup Dialog Box

SailWind Logic Guide

659

SailWind Logic GUI Reference
PCB Decal Assignment Dialog Box

## PCB Decal Assignment Dialog Box

To access: Select a part > right-click > Properties  > PCB Decals  button

Use the PCB Decal Assignment dialog box to assign alternate PCB decals to schematic parts. Decal
names are included in the netlist file to display the proper decal, or footprint, when the file is imported into
the PCB design file. You can select a decal assigned as an alternate during part creation, override the
decal with one from the library, or enter a name for an undefined decal you plan to create later in the PCB
design.

Figure 119. PCB Decal Assignment Dialog Box

Objects

Table  179. PCB Decal Assignment Dialog Box Contents

Name

Description

Assigned in Schematic

Displays the name of the currently selected decal as it is assigned
to the schematic from the current library.

<< Assign  button

Assigns the selected decal in the Alternate in Library list to the
part.

Alternates in Library list

Lists alternate decals in the library.

No specific PCB Decal

Specifies to remove the assigned decal. The default decal
assigned to the part type is used when the netlist is imported to
SailWind Layout; no decal assignment appears in the netlist.

Browse  button

Picture area

Opens the Get PCB Decal From Library Dialog Box.

Displays the selected pin.

Apply update to area

Specifies how parts are updated:

660

SailWind Logic Guide

SailWind Logic GUI Reference
PCB Decal Assignment Dialog Box

Table  179. PCB Decal Assignment Dialog Box Contents  (continued)

Name

Description

• This Part  — Only updates the selected part.

• All Parts This Type  — Updates all matching parts in the

design

Related Topics
Modifying Parts

SailWind Logic Guide

661

SailWind Logic GUI Reference
Photo Plotter Advanced Setup Dialog Box

## Photo Plotter Advanced Setup Dialog Box

To access: File  > Plot  menu item > select Photo Plot > Setup  button > Advanced  button

Use the Photo Plotter Setup dialog box to define the aperture and other photo plotter options.

Figure 120. Photo Plotter Advanced Setup Dialog Box

Objects

Name

Units area

Table  180. Photo Plotter Advanced Setup Dialog Box Contents

Description

Specifies the units to use:

• English  — mils

• Metric  — millimeters

Number of Digits area

Specifies the precision of the output file coordinates:

• Leading — the number of digits that should lead the decimal

point

• Trailing  — the number of digits that should trail the decimal

point

Coordinates area

Specifies the coordinates for the output file:

• Absolute  — absolute coordinates

• Incremental  — relative coordinates

Zero Suppress area

Specifies how to handle zero suppression in the output file:

• None  — retains leading and training zeros

• Leading  — suppresses zeros before the decimal point

• Trailing  — suppresses zeros after the decimal point

662

SailWind Logic Guide

SailWind Logic GUI Reference
Photo Plotter Advanced Setup Dialog Box

Table  180. Photo Plotter Advanced Setup Dialog Box Contents  (continued)

Name

Description

Circular Interpolation area

Specifies how to draw arcs and circles:

• None  — if your photo plotter does not support circular

interpolation. Arcs and circles are drawn as small straight-line
segments

• Quadrant  — if your photo plotter does not support full,

360-degree circular interpolation

• Full  — if your photo plotter supports full, 360-degree circular

interpolation

Plotting Size area

Specifies the size of the plot. A  through E  and Other  in inches; A4
through A0  and Other  in millimeters.

 Tip
If you click Other, specify the X and Y dimensions.

Suppress Repeated Coords

Specifies to eliminate repeated coordinates from the output file.

Related Topics

Photo Plotter Setup Dialog Box

SailWind Logic Guide

663

SailWind Logic GUI Reference
Photo Plotter Setup Dialog Box

## Photo Plotter Setup Dialog Box

To access: File  > Plot  menu item > select Photo Plot > Setup  button

Use the Photo Plotter Advanced Setup dialog box to define the units for the photo plotter to use.

Figure 121. Photo Plotter Setup Dialog Box

Objects

Name

D-Code list

Add  button

Delete  button

Augment  button

Regenerate  button

Table  181. Photo Plotter Setup Dialog Box Contents

Description

Lists the D-codes for the photo plotter.

Opens the CAM Question dialog box where you can name the new
D-Code.

Removes the selected code from the D-Code list.

Automatically generates D-codes for items in the schematic file
that are not in the current list.

Clears the current D-code list and automatically adds D-codes for
all items in the schematic.

Shape area

Specifies the shape for a selected D-code:

• Flash  — sets a flash aperture.

• Line  — set a draw aperture.

Same Aperture for Flashes/Lines

Specifies to draw lines and flashed items with the same aperture.
Round and square shapes for lines will be gray.

Width

Specifies the diameter for round shapes. This box is unavailable if
a width is not appropriate for the specified shape.

Aperture Count

Specifies the maximum aperture count.

664

SailWind Logic Guide

SailWind Logic GUI Reference
Photo Plotter Setup Dialog Box

Table  181. Photo Plotter Setup Dialog Box Contents  (continued)

Name

Description

Augment on-the-fly

Specifies to add apertures to the D-code list when photo plots are
run if any newly created lines were added to the schematic.

Advanced  button

Opens the Photo Plotter Advanced Setup Dialog Box.

SailWind Logic Guide

665

SailWind Logic GUI Reference
Pin Decal Browse Dialog Box

## Pin Decal Browse Dialog Box

To access: Tools  > Part Editor  menu item > Decal Editing Toolbar  button> Add Terminal  or Change
Pin Decal  button

Use the Pin Decal Browse dialog box to add or change a terminal. A terminal consists of a pin decal and
a series of text strings that define the terminal's number, swap data, etc.

Figure 122. Pin Decal Browse Dialog Box

Table  182. Pin Decal Browse Dialog Box Contents

Description

Displays the selected pin.

Displays the available pins.

Objects

Name

Picture area

Pins list

Related Topics
Adding Terminals

Modifying Terminals

666

SailWind Logic Guide

SailWind Logic GUI Reference
Pin Decal List Management Dialog Box

## Pin Decal List Management Dialog Box

To access: Tools  > Part Editor  menu item > Setup  > Pin List Manger  menu item

Use the Pin Decal List Management dialog box to control which decals are displayed in the Pin Decal List.
The pin decal list contains the decals that can be used as terminal graphics when creating gate or part
decals.

Figure 123. Pin Decal List Management Dialog Box

Objects

Name

Library list

Filter

Table  183. Pin Decal List Management Box Contents

Description

Lists the libraries available to you.

Searches the chosen library (or libraries) for a specific part or item
name, or names that match a wildcard or expression  on page 105.
Use the Library dropdown list to select specific library directories
or the All Libraries setting. Type * to view all parts or items in the
chosen libraries. Click Apply  to search the libraries and display the
search results.

Preview Area

Displays the pin decal highlighted in the Unassigned Decals area
or the Pin Decals area.

Unassigned Decals list

Lists the available pin decals in the selected library or all libraries.

Assign>>  button

<<Unassign  button

Moves a decal from the Unassigned Decals list box to the Pin
Decals list. Select a decal, then click Assign.

Moves a decal from the Pin Decals list box to the Unassigned
Decals list box. Select a decal, then click Unassign.

SailWind Logic Guide

667

SailWind Logic GUI Reference
Pin Decal List Management Dialog Box

Table  183. Pin Decal List Management Box Contents  (continued)

Name

Pin Decals list

Description

Lists the pin decals that are displayed in the dialog boxes that
access pin decals, for example, the Pin Decal Browse dialog box.
You can display up to 100 pin decals.

668

SailWind Logic Guide

SailWind Logic GUI Reference
Pin Label Fonts Dialog Box

## Pin Label Fonts Dialog Box

To access: Select a pin > right-click > Properties  menu item > Font  button

Use the Pin Label Fonts dialog box to change the fonts of a pin label.

Figure 124. Pin Label Fonts Dialog Box

Objects

Name

Pin Area

Size

Table  184. Pin Label Fonts Dialog Box Contents

Description

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

Line Width

Specifies the line width for stroke fonts only.

SailWind Logic Guide

669

SailWind Logic GUI Reference
Pin Label Fonts Dialog Box

Table  184. Pin Label Fonts Dialog Box Contents  (continued)

Name

Description

Font list

Justification area

Name Area

Size

The fonts available to you. This lists either stroke fonts or system
fonts.

You choose which type of font to use in the Fonts Dialog Box.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles: B  for bold, I  for italic, or U  for
underlined.

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

Line Width

Specifies the line width for stroke fonts only.

Font list

The fonts available to you. This lists either stroke fonts or system
fonts.

You choose which type of font to use in the Fonts Dialog Box.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles: B  for bold, I  for italic, or U  for
underlined.

670

SailWind Logic Guide

SailWind Logic GUI Reference
Pin Label Fonts Dialog Box

Table  184. Pin Label Fonts Dialog Box Contents  (continued)

Name

Description

Justification area

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Related Topics

Modifying Pin Label Fonts

SailWind Logic Guide

671

SailWind Logic GUI Reference
Pin Properties Dialog Box

## Pin Properties Dialog Box

To access: Select a pin > right-click > Properties  menu item

Use the Pin Properties dialog box to view pin information, to modify parts and nets to which the selected
pin is connected, and also to set font settings for pin number and pin name labels.

Figure 125. Pin Properties Dialog Box

Objects

Name

Pin area

Part area

Table  185. Pin Properties Dialog Box Contents

Description

Displays the information about the selected pin: Pin number,
name, swap number, type, and the net.

Displays the information about the part: reference designator and
gate number.

Part/Gate  button

Opens the Part Properties Dialog Box.

Opens the Net Properties Dialog Box.

Opens the Pin Label Fonts Dialog Box.

Net  button

Font  button

Related Topics
Modifying Pins

672

SailWind Logic Guide

SailWind Logic GUI Reference
Plot Dialog Box

## Plot Dialog Box

To access: File  > Plot  menu item

You can output your designs to pen plotters or photo plotters.

Figure 126. Plot Dialog Box

Objects

Name

Summary

Table  186. Plot Dialog Box Contents

Description

Lists the numbered available sheets you can plot, and the items
contained in the sheets.

Plot What area

Specifies what to plot: Pen or Photo.

File Prefix

Options  button

Setup  button

Preview  button

Run  button

Specifies the prefix name of the file you want to plot.

Opens the Options dialog box  on page 606.

Depending on what you are plotting, opens the Pen Plotter Setup
Dialog Box  or the Photo Plotter Setup Dialog Box.

Opens the Selections Preview Dialog Box.

Runs the Plot with what you’ve set.

SailWind Logic Guide

673

SailWind Logic GUI Reference
Print Dialog Box

## Print Dialog Box

To access: File  > Print  menu item

A standard Microsoft Print dialog box with access to Print Preview and Options.

Objects

Object

Preview  button

Options  button

Description

Opens the “Selections Preview Dialog Box”  on
page 714.

Opens the “Options Dialog Box - Print/Plot”  on
page 606.

## Project Explorer

To open the Project Explorer, click the Project Explorer  button.

The Project Explorer shows a hierarchical structure for the objects in your design. It provides access to
objects and rules. When you update your design, the hierarchical structure is automatically updated to
reflect the changes you make.

674

SailWind Logic Guide

SailWind Logic GUI Reference
Project Explorer

Tip
The Hierarchical structure is available only when a design is open.

Restriction:
The Project Explorer is not available in the Part Editor.

Object Types

Objects in the Project Explorer are placed in object groups. Object groups are of two types: primary and
secondary as shown in the following table.

Restriction:
Observe the following restrictions:

• You cannot remove or rename primary object groups.
• Modification of secondary group items is only available in SailWind Router.

Table  187. Object Groups and Subgroups

Primary Group

Product
Availability

Secondary Group

Description

schematic sheets

SailWind Logic

Sheet names

Lists all parts on the sheet

Layers

SailWind Layout

Electrical layers

SailWind Router

Lists all electrical layers, including
plane layers and routing layers

General layers

Lists all other layers except
electrical

Components

SailWind Logic

Lists all components and pin pairs

SailWind Layout

SailWind Router

Part decals

SailWind Router

Nets

SailWind Logic

SailWind Layout

Lists all part decals in the design
or all components that use the
selected part decal

Lists all nets in the design

Net objects

SailWind Router

Net classes

Lists all nets belonging to net
classes

Matched length net groups Lists all matched length net

groups

Nets

Lists all nets in the design

SailWind Logic Guide

675

SailWind Logic GUI Reference
Project Explorer

Table  187. Object Groups and Subgroups  (continued)

Primary Group

Product
Availability

Secondary Group

Description

Matched length pin pair
groups

Lists all matched length pin pair
groups

Pin pair groups

Lists all nets belonging to pin pair
groups (containing pin pair rules)

Conditional rules

Lists all nets with conditional rules

Differential pairs

Lists all differential pairs

Via types

SailWind Router

CAE decals

SailWind Logic

PCB decals

SailWind Logic

SailWind Layout

Lists the via types used in the
design

Lists the CAE decals used in the
design

Lists the PCB decals used in the
design

676

SailWind Logic Guide

SailWind Logic GUI Reference
Query Hierarchical Component Dialog Box

## Query Hierarchical Component Dialog Box

To access: Select a hierarchical component > right-click > Properties  menu item

Use the Hierarchical Component Properties dialog box to assign a hierarchical component to the next
available sheet number to make it accessible from the Sheet list when a sheet other than the parent sheet
is displayed. Use the Setup  > Sheets  menu item to modify the sheet name or the numeric order.

Figure 127. Query Hierarchical Component Dialog Box

Objects

Name

Name

Visibility

No

Visibility

Numbered

UnNumbered

Table  188. Query Hierarchical Component Dialog Box Contents

Description

The name of the selected component.

Specifies to display the name on top of the hierarchical component
in the schematic.

The assigned sheet number of the selected component.

Specifies to display the sheet number in the schematic.

Specifies to assign the hierarchical component the next available
sheet number.

Specifies to remove a sheet number assignment from a
hierarchical component.

Related Topics

Modifying Hierarchical Components

SailWind Logic Guide

677

SailWind Logic GUI Reference
Reference Designator Properties Dialog Box

## Reference Designator Properties Dialog Box

To access: Select a part type label > right-click > Properties  menu item

Use the Reference Designator Properties dialog box to view and modify label size and justification as well
as text and font settings for one or more reference designator labels.

Figure 128. Reference Designator Properties Dialog Box

Objects

Table  189. Reference Designator Properties Dialog Box Contents

Name

Description

Reference Designator

The name of the selected attribute.

Rename area

Specifies to rename just the gate or the entire part.

Rotation

Size

Specifies the rotation of the label: 0 or 90 degrees.

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

678

SailWind Logic Guide

SailWind Logic GUI Reference
Reference Designator Properties Dialog Box

Table  189. Reference Designator Properties Dialog Box Contents  (continued)

Name

Line Width

Description

Specifies the line width for stroke fonts only.

Font list

The fonts available to you. This lists either stroke fonts or system
fonts.

You choose which type of font to use in the Fonts Dialog Box.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles: B  for bold, I  for italic, or U  for
underlined.

Horizontal/Vertical Justification

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Related Topics

Modifying Reference Designator Labels

SailWind Logic Guide

679

SailWind Logic GUI Reference
Remap Special Symbols Dialog Box

## Remap Special Symbols Dialog Box

To access: Tools > Update from Library  menu item; then, in the Update from Library dialog box, choose
the “Update design from library” option and select the Off-page symbols, Ground symbols, or the Power
symbols check box.

Use the Remap Special Symbols dialog box to make updates to power, ground, or off-page schematic
symbols in your design. You can use this dialog box to update your schematic symbols with changes in
the library or assign a different library symbol to a schematic symbol in the design.

Note:
The specific signal name assigned to special symbols currently used within the schematic are not
modified when performing the “Update from Library” function. For example, the signal name of
a power symbol assigned to +5V is not modified in the schematic if updated with another power
symbol that uses a different default signal name (such as +12V).

Figure 129. The Remap Special Symbols Dialog Box

Objects

Name

Schematic Symbol

Table  190. The Remap Special Symbols Dialog Box Options

Description

Displays the name power, ground, or off-page
symbols currently associated with your design.

680

SailWind Logic Guide

Table  190. The Remap Special Symbols Dialog Box Options  (continued)

SailWind Logic GUI Reference
Remap Special Symbols Dialog Box

Name

Pin Type

Default Signal Name

Library Symbol

Related Topics

The Update From Library Function

Updating Special Symbol Mappings

Description

Displays the function of the pin associated with the
symbol; for example, load, ground, or power.

Displays the name of the signal currently
associated with the symbol (as it originally existed
in the library); for example, +5VCC, or AGND.

This name does not necessarily reflect the signal
name used on specific instances of the symbol in
the schematic.

The symbol mapped to the schematic
symbol. SailWind Layout initially displays the
best-matching symbol in this box, regardless of the
current mapping.

You can change the mapping by double-clicking
in the box to access a dropdown list of available
symbols. You can assign the same library symbol
to more than one schematic symbol.

Only symbols associated with your current library
appear in the list.

The available library symbols in the dropdown list
also depends on the pin type. For example, if the
pin type is “ground,” only ground symbols appear
in the list.

Any additional symbols not specifically mapped to
existing symbols become updated to the design
and available for use.

SailWind Logic Guide

681

SailWind Logic GUI Reference
Rename Gate Dialog Box

## Rename Gate Dialog Box

To access: select a part > right-click > Properties  menu item > Rename Gate  button

Use the Rename Gate dialog box to change the reference designator of the selected gate.

Figure 130. Rename Gate Dialog Box

Objects

Table  191. Rename Gate Dialog Box Contents

Name

Description

Text box

Type the new gate reference designator information.

 Restriction:
You are prevented from assigning an already used reference designator or an
unused gate of a part with a different part type.

682

SailWind Logic Guide

SailWind Logic GUI Reference
Rename Part Dialog Box

## Rename Part Dialog Box

To access: select a part > right-click > Properties  menu item > Rename Part  button

Use the Rename Part dialog box to change the reference designator for the selected part or gate.

Figure 131. Rename Part Dialog Box

Objects

Table  192. Rename Part Dialog Box Contents

Name

Description

Text box

Type the new part reference designator information.

 Restriction:

• All gates are renamed if you change the reference designator of one gate of

a multi-gated part.

• You are prevented from assigning an already used reference designator.

SailWind Logic Guide

683

SailWind Logic GUI Reference
Renumber Pins Dialog Box

## Renumber Pins Dialog Box

To access: Tools  > Part Editor  menu item > Edit Electrical  button > Pins  tab > select pin(s) >
Renumber  button

Use the Renumber Pins dialog box to renumber pins (terminals). You can renumber part type pins on the
Pins  tab of the Part Information dialog box.

Figure 132. Renumber Pins Dialog Box

Objects

Table  193. Renumber Pins Dialog Box Contents

Name

Description

Number of pins

The number of pins available for renumbering.

Prefix/Suffix

For a single pin number, use either Prefix or Suffix box, and void
the other box. Use both boxes if you want to increment one of the
values.

Alphabetic and numeric values can be used in either box.

Pin numbers

A preview of pin numbers based on your prefix/suffix input.

Increment prefix

Sets the prefix as the part of the pin number to increment.

Increment suffix

Sets the suffix as the part of the pin number to increment.

Step value

Sets the step value. Type a positive or negative number by which
to increase or decrease the pin number with consecutive or
stepped values.

684

SailWind Logic Guide

SailWind Logic GUI Reference
Renumber Pins Dialog Box

Table  193. Renumber Pins Dialog Box Contents  (continued)

Name

Description

 Restriction:
Step value must be non-zero and be in the range -10 to +10.
Zero would replicate a single pin number and is not allowed.

Verify valid JEDEC pin numbering

If using alphanumerics, you can select the Verify valid JEDEC pin
numbering check box to ensure that legal alphanumeric values are
used.

SailWind Logic Guide

685

SailWind Logic GUI Reference
Report Manager Dialog Box

## Report Manager Dialog Box

To access: File  > Library  menu item > Parts  button > select a part > List to File  button

Use the Report Manager dialog box to generate a report about the parts in a library. You can specify the
parts and the attributes to include in the report.

Figure 133. Report Manager Dialog Box

Objects

Table  194. Report Manager Dialog Box

Field or Button

Description

Available attributes

All attributes of the part types in the selected library.

Click an attribute in the list of select it. (To select additional attributes, press
CTRL and click each attribute.) Click Include >>  to include selected attributes
in the report.

Selected attributes

Attributes in the report.

Click an attribute in the list of select it. (To select additional attributes,
press CTRL and click each attribute.) Click << Exclude  to remove selected
attributes from the report.

686

SailWind Logic Guide

SailWind Logic GUI Reference
Report Manager Dialog Box

Table  194. Report Manager Dialog Box  (continued)

Field or Button

Description

The order of attributes in the list is the order of columns in the report. Select
an attribute and click Up  or Down  to change the order.

Include >>  button

Includes the selected attributes in the report (moves the attributes to the
Selected attributes list). Select one or more attributes on the Available
attributes list and click Include >>.

<< Exclude  button

Excludes the selected attributes from the report (moves the attributes from
the Selected attributes list back to the Available attributes list).

Select one or more attributes on the Selected attributes list and click <<
Exclude.

Up / Down  buttons

Moves a selected attribute up or down on the Selected attributes list. List
order determines the order in which columns appear in the report.

Part Filter

Specifies the part types to include in the report.

Type a part type name in the field or use wildcards (*) to specify a group of
part types. For example:

* Specifies all part types in the library.

+5* Specifies all part types that begin with the characters +5, such as +5volt
and +5LS07.

Apply  button

Filters the part types.

Parts

Run  button

Lists part types included in the report (as determined by the Part Filter).

Generates the report and lets you save it either in lst for viewing or printing or
in csv format for use with MS Excel.

Close  button

Cancels the operation and closes the dialog box.

Related Topics

Creating a Report of the Parts in a Library

Creating a Report of Decals, Lines or Logic Symbols in a Library

SailWind Logic Guide

687

SailWind Logic GUI Reference
Reports Dialog Box

## Reports Dialog Box

To access: File  > Reports  menu item

Use the Reports dialog box to produce any of six different types of reports on the current schematic. You
can save these reports as text files on your hard disk or output them to a printer.

Figure 134. Reports Dialog Box

Objects

Table  195. Reports Dialog Box Contents

Name

Description

Select Report Files for Output area — Select the report(s) you want to run.

Unused

The Unused report has two parts - the Unused Gate List, followed by the
Unused Pins List. Use this report for troubleshooting and to maximize part
usage.

• Unused Gate List  — lists all part types with multiple gates and if there are
any unused gates, it lists the specific gate(s) under the part type name. If
there are no unused gates then it only lists the part type name.

• Unused Pins List  — lists parts with pins unused in the schematic. It lists

the unused pins under the part type name. If there are no unused pins there
will be no part types listed.

When you run this report, a link to the UnusedGatesPins.rep  appears in the
Output Window. Click the link to open the report in your default text editor.

The Part Statistics report lists information about all parts in the schematic. The
report includes the reference designator name and part type for each part in
the schematic, and for each pin on the part, the pin type, sheet location, and
signal name. Use this report to locate possible errors in the schematic.

When you run this report, a link to the PartStatistics.rep  appears in the Output
Window. Click the link to open the report in your default text editor.

Part Statistics

Net Statistics

The Net Statistics report lists information for each net in the schematic. The
report includes the reference designator name and pin number for all parts in
the net. SailWind Logic flags possible errors (for example, nets with no inputs

688

SailWind Logic Guide

Table  195. Reports Dialog Box Contents  (continued)

Name

Description

SailWind Logic GUI Reference
Reports Dialog Box

Limits

or no outputs, nets with multiple outputs, etc.) for further examination. Use this
report to locate possible errors in the schematic.

Error messages that can occur:

• Net has only one pin: a net going to an off-page flag not connected

elsewhere.

• Net has no defined source: there is no pin in the net that has a pin type of S.

• Net has no defined loads: there is no pin in the net that has a pin type of L.

• Net has multiple sources- be sure they are tieable: the net has more than 1

pin with the pin type S.

When you run this report, a link to the NetStatistics.rep  appears in the Output
Window. Click the link to open the report in your default text editor.

The Limits report indicates the maximum number of each SailWind Logic data
item (parts, nets, text) your system will allow, as well as the current count
of each of these items in the schematic. This limit varies depending on the
amount of virtual memory that is available.

The report has two parts. The first is a list of items whose limits are common to
the entire schematic. The second is a count, for each schematic sheet, of the
items whose limits apply for each sheet.

You should periodically run a Limits report to ensure that you are not
approaching the system’s limit for any item.

If you exceed the Maximum No. of Items for any item, you cannot continue
adding those items to the schematic. The solution is to split the design into
multiple schematics, run separate netlists for each schematic, then merge the
netlists using a text editor.

When you run this report, a link to the DesignLimits.rep  appears in the Output
Window. Click the link to open the report in your default text editor.

Connectivity

The Connectivity report lists the X,Y coordinate location and sheet number of
all off-page, ground, and power symbols in the schematic.

 Tip
Use the report to quickly locate an off-page symbol using the S (Search)
modeless command.

An error message appears when a net contains only one off-page reference.
Subnets tied together without a visible net name are identified by flagging them
as missing an off-page symbol.

When you run this report, a link to the ConnectivityReport.rep  appears in the
Output Window. Click the link to open the report in your default text editor.

Bill of Materials

The Bill of Materials report produces a user-configurable list of the parts
contained in the current schematic. You can direct any part attribute in the
schematic to a Bill of Materials report.

When you run this report, a link to the BillOfMaterials.rep  appears in the Output
Window. Click the link to open the report in your default text editor.

Setup  button

Opens the Bill of Materials Setup dialog box  on page 479. See also Setting up
the Bill of Materials Report  on page 314.

SailWind Logic Guide

689

SailWind Logic GUI Reference
Reports Dialog Box

Related Topics

Generating Reports

690

SailWind Logic Guide

SailWind Logic GUI Reference
Routing Rules Dialog Box

## Routing Rules Dialog Box

To access:

• Setup  > Design Rules  menu item > a rule hierarchy button) > Routing  button

• Select a net, right-click and click Show Rules, then click the Routing  button.

Use the Routing Rules dialog box to specify rules for interactive and automatic routing. You can specify
the default set of routing rules and routing rules for specific nets.

Figure 135. Routing Rules Dialog Box

Objects

Name

Topology Type

Table  196. Routing Rules Dialog Box Contents

Description

Specify the topology type to determine the pin-to-pin order when
routing the net or moving a part. When routing interactively, a
ratsnest guides you as you route from pin to pin.

SailWind Logic Guide

691

SailWind Logic GUI Reference
Routing Rules Dialog Box

Table  196. Routing Rules Dialog Box Contents  (continued)

Name

Description

To specify the topology type, click one of the following options:

• Protected  — Do not change the order of the connectivity in the

net.

Note that this option disables length minimization.

• Minimized  — Order the net by the shortest distance between

pins. Net reorder or reconnect is permitted.

• Serial source  — Order the net in a series order from source

pins to load pins to a terminator.

• Parallel source  — Same as "Serial source" except order the
net with parallel branches for each source-to-load connection.

• Mid-driven  — Divide the net into two branches and order each

branch in a source to load to terminator order.

Routing options

Via

Vias can share copper with another object.

 Restriction:
This rule is used only in SailWind Router, although you can
define this rule in SailWind Logic, SailWind Layout, or SailWind
Router.

692

SailWind Logic Guide

Table  196. Routing Rules Dialog Box Contents  (continued)

Name

Trace

Description

Traces can share copper with another object.

SailWind Logic GUI Reference
Routing Rules Dialog Box

 Restriction:
This rule is used only in SailWind Router, although you can
define this rule in SailWind Logic, SailWind Layout, or SailWind
Router.

Priority

Assign priority from 0 to 100. Nets with higher priority are routed
first.

 Restriction:
SailWind Router does not use the priority value. This rule
applies only to SPECCTRA.

Auto Route

Allow Ripup

Enables the autorouter to route nets.

Unroute existing traces and reroute the nets.

 Tip
Enable this option to rip up traces while DRC Warn or Prevent
is enabled.

Allow Shove

Move unprotected traces aside to create room for new traces.

 Tip
Enable this option to shove traces while DRC Warn or Prevent
is enabled.

Allow Shove Protected

Move protected traces aside to make room for new traces.

Layer biasing

Available Layers

Lists layers, not already in the Selected Layers list, that can be
made available for routing.

SailWind Logic Guide

693

SailWind Logic GUI Reference
Routing Rules Dialog Box

Table  196. Routing Rules Dialog Box Contents  (continued)

Description

Click to move a selected layer from the Available Layers list to the
Selected layers list.

Click to move a selected layer from the Selected Layers list to the
Available layers list.

Lists the layers, that have been selected from all the available
design layers, to be available for routing.

Name

Add >>  button

<< Remove  button

Selected layers

Vias

Use Vias already defined in PCB
Layout design

Select the check box to suppress the via biasing in SailWind Logic.

Clear the check box to specify via biasing for routing.

 Tip

• If vias exist in SailWind Logic that don’t exist in SailWind
Layout, you are prompted to create those vias before
importing the netlist into SailWind Layout.

• Since there is no Pad Stacks Properties facility for creating

vias in SailWind Logic you can only specify the names of via
and you must create those vias in SailWind Layout.

• Since only Default, Net, and Class rules are available in
SailWind Logic, any control of vias at higher levels of the
rules hierarchy must be done in SailWind Layout.

Lists the vias, not already in the Selected Vias list that are
available for routing.

Click to open the Via Setup dialog box to Add, Delete, or Rename
vias available for routing. Since there is no Pad Stacks Properties
facility for creating vias in SailWind Logic, any vias added must be
created in SailWind Layout before importing the netlist in SailWind
Layout.

Click to move a selected via from the Available Vias list to the
Selected Vias list.

Click to move a selected via from the Selected Vias list to the
Available Vias list.

Lists the vias, that have been selected from all the available vias,
to be available for routing.

Click to give the autorouter unrestricted use of vias during
autorouting.

Click to restrict the number of vias the autorouter can add to nets
during autorouting. In the box, type the maximum number of vias
between 0 and 50000. The autorouter considers this to be a hard
rule. Interactive routing and design verification check this rule.

Available vias

Via Definition  button

Add >>  button

<< Remove  button

Selected Vias

Maximum number of vias

Unlimited vias

Maximum of

694

SailWind Logic Guide

SailWind Logic GUI Reference
Routing Rules Dialog Box

Table  196. Routing Rules Dialog Box Contents  (continued)

Name

Description

 Tip
An insufficient maximum number of vias might increase
autorouting runtime and reduce completion rates.

Delete  button

Click to remove the current set of routing rules from the rules
hierarchy for the selected nets.

 Restriction:
The Delete  button is unavailable for the default set of routing
rules. You cannot delete the Default Routing rules.

SailWind Logic Guide

695

SailWind Logic GUI Reference
Rules Dialog Box

## Rules Dialog Box

To access: Setup  > Design Rules  menu item

Use the Rules dialog box to enter item-to-item Clearance rules, routing guidelines, and values for the
optional High Speed checking commands. You can also indicate the unit of measure for passing rules to
SailWind Logic: mils, metric, or inches.

Figure 136. Rules Dialog Box

Objects

Name

Default  button

Class  button

Net  button

Table  197. Rules Dialog Box Contents

Description

Opens the Default Rules Dialog Box.

Opens the Class Rules Dialog Box.

Opens the Net Rules Dialog Box.

Conditional Rules  button

Opens the Conditional Rule Setup Dialog Box.

Differential Pairs  button

Opens the Differential Pairs Dialog Box.

Report  button

Units  button

Opens the Rules Report Dialog Box.

Specifies the units you want: Mils, Metric, or Inches

696

SailWind Logic Guide

SailWind Logic GUI Reference
Rules Report Dialog Box

## Rules Report Dialog Box

To access: Setup  > Design Rules  menu item > Report  button

Use the Rules Report dialog box to produce a report of some or all of the rules you have defined. By
default, a complete report of all rules is reported.

Figure 137. Rules Report Dialog Box

Objects

Table  198. Rules Report Dialog Box Contents

Name

Description

Rule Types area

Nets area

Classes area

Default Rules

Output area

Displays the specified rules for the specified nets and classes.
Click any combination of buttons, including Differential Pairs, to
report net pairs.

Displays the specified rules for every net or selected nets. Click All
Nets or select specific nets in the list box.

Displays the specified rules for every class or selected classes.
Click All Classes or select specific net classes in the list box.

Displays the default rules for the specified nets and classes.

Specifies how you want your output.

• Rule Sets  — display all rules in the current hierarchy that are

unique from the default rules.

• Rule Values  — display all rules in the current hierarchy level,

even if the values are the same as the default rules.

SailWind Logic Guide

697

SailWind Logic GUI Reference
Rules Report Dialog Box

Related Topics

Creating a Rules Report

698

SailWind Logic Guide

SailWind Logic GUI Reference
Save CAE Decal to Library Dialog Box

## Save CAE Decal to Library Dialog Box

To access: File  > Library  menu item > select a library > Logic  filter type > select a CAE decal > Copy
button

Use the Save CAE Decal to Library dialog box to copy a CAE decal to another name or another library.

Figure 138. Save CAE Decal to Library Dialog Box

Objects

Name

Library

Table  199. Save CAE Decal to Library Dialog Box Content

Description

Select the library for the copied CAE decal.

Name of CAE Decal

Type the name for the copied CAE decal.

Related Topics

Copying a Library Item

SailWind Logic Guide

699

SailWind Logic GUI Reference
Save Configuration Dialog Box

## Save Configuration Dialog Box

To access: Setup  > Display Colors  menu item > Save  button

Use the Save Configuration dialog box to save the color assignments and settings you’ve made in the
Display Colors dialog box.

Figure 139. Save (color) configuration Dialog Box

Objects

Name

Text box

Table  200. Save configuration Dialog Box Content

Description

Type the name of the new color configuration. The name will appear in the
Configuration list in the Display Colors Dialog Box.

700

SailWind Logic Guide

SailWind Logic GUI Reference
Save Drafting Item to Library Dialog Box

## Save Drafting Item to Library Dialog Box

To access: Select an item > right-click > Save to Library  menu item

Use the Save Drafting Item to Library dialog box save 2D line items or complex 2D line item in the
schematic to a library.

Figure 140. Save Drafting Item to Library Dialog Box

Objects

Name

Library list

Table  201. Save Drafting Item to Library Dialog Box Contents

Description

Specifies the library you to which you want to save the item.

Name of Item

The name of the item you want to save in the selected library.

Related Topics

Adding Drafting Items to a Library

SailWind Logic Guide

701

SailWind Logic GUI Reference
Save Off-Page to Library Dialog Box

## Save Off-Page to Library Dialog Box

To access: Tools  > Save Off-page to Library  menu item

Use Save Off-page to Library to update the off-page, ground, or power symbols in the library with the
current version(s) in the schematic.

Figure 141. Save Off-page to Library Dialog Box

Objects

Name

Item Type area

Table  202. Save Off-page to Library Dialog Box Contents

Description

Specifies the item you want to update in the library with the current
version in the schematic.

Related Topics

Saving Off-Page to Library

702

SailWind Logic Guide

SailWind Logic GUI Reference
Save Part and Gate Decals As Dialog Box

## Save Part and Gate Decals As Dialog Box

To access: Tools  > Part Editor  menu item > (in the Part Editor) File  > Save as  menu item

The Save Part and Gate Decals As dialog box saves a new or modified part type to the library. You can
also rename a modified decal to prevent other parts that use the same decal from being affected.

Figure 142. Save Part and Gate Decals As Dialog Box

Objects

Table  203. Save Part and Gate Decals As Dialog Box Contents

Name

Description

Name of Part

Defines the part type name in the library.

Library

The library folder to which information is saved.

Name of Gate Decals

Displays the name of decal and any alternate decals associated
with the part type. Select a decal name and click Edit  to rename
the decal.

Edit  button

Makes the highlighted field in the table editable. You can also
double click a text field to edit it.

Related Topics
Saving Part Types

SailWind Logic Guide

703

SailWind Logic GUI Reference
Save Part Types to Library Dialog Box

## Save Part Types to Library Dialog Box

To access: Select a part > right-click > Save to Library  menu item

Use the Save Part Types to Library dialog box to copy the part types of the schematic. If the original part
type is deleted from the library, get another copy from the schematic.

Figure 143. Save Part Types to Library Dialog Box

Objects

Table  204. Save Part Types to Library Dialog Box Contents

Name

Description

Part Types list

The part(s) you selected in the schematic.

Select All  button

Selects all of the items in the Part Types list.

Select Not in Lib  button

Selects only those part types that are not currently saved in the
library.

Unselect All  button

Clears the selection of any or all part types in the Part Types list.

Library list

Specifies the library you to which you want to save the part types.

Related Topics

Saving Part Types to a Library

704

SailWind Logic Guide

SailWind Logic GUI Reference
Save Part Type to Library Dialog Box

## Save Part Type to Library Dialog Box

To access: File  > Library  menu item > select a library > Parts  filter type > select a part type > Copy
button

Use the Save Part Type to Library dialog box to copy a Part Type to another name or another library.

Figure 144. Save Part Type to Library Dialog Box

Objects

Name

Library

Table  205. Save Part Type to Library Dialog Box Content

Description

Select the library for the copied part type.

Name of Part Type

Type the name for the copied Part Type.

Related Topics

Copying a Library Item

SailWind Logic Guide

705

SailWind Logic GUI Reference
Save PCB Decal to Library Dialog Box

## Save PCB Decal to Library Dialog Box

To access: File  > Library  menu item > select a library > Decal  filter type > select a PCB decal > Copy
button

Use the Save PCB Decal to Library dialog box to copy a PCB decal to another name or another library.

Figure 145. Save PCB Decal to Library Dialog Box

Objects

Name

Library

Table  206. Save PCB Decal to Library Dialog Box Content

Description

Select the library for the copied PCB decal.

Name of PCB Decal

Type the name for the copied PCB decal.

Related Topics

Copying a Library Item

706

SailWind Logic Guide

SailWind Logic GUI Reference
Save View Dialog Box

## Save View Dialog Box

To access: View  > Save View  menu item

The Save View dialog box to save a work area view for easy restoration.

Figure 146. Save View Dialog Box

Objects

Name

View Name list

Preview area

Capture  button

Apply  button

Delete  button

Table  207. Save View Dialog Box Contents

Description

The views you have already saved.

Shows you the location of the selected view in relation to the
extents of the design.

Opens the Capture a New View Dialog Box  where you can name
the view you want to save.

 Tip
You can create up to nine views. The view names appear at the
bottom of the View  menu.

Applies the selected, previously saved view to the work area.

Removes the selected view from the View Name list.

Related Topics

Saving and Restoring Views

SailWind Logic Guide

707

SailWind Logic GUI Reference
Select Gate Decal Dialog Box

## Select Gate Decal Dialog Box

To access: Tools  > Part Editor  menu item > open a part type > Edit Graphics  button

Use the Select Gate Decal dialog box to select the gate decal you want to use.

Figure 147. Select Gate Decal Dialog Box

Objects

Name

Gate list

Decal

Table  208. Sheets Decal Dialog Box Contents

Description

Lists the gates available to you.

Displays the decal assigned to the selected gate.

Alternative Decals list

Lists the alternative decals available.

Related Topics

Assigning Pin Information to the CAE Decal

708

SailWind Logic Guide

SailWind Logic GUI Reference
Select Pin Decal Dialog Box

## Select Pin Decal Dialog Box

To access: Tools  > Part Editor  menu item > open an Off-page type (Off-page, Power, or Ground) > Edit
Graphics  button

Use the Select Pin Decal dialog box to access and create graphics for a new Special Symbol. This dialog
box is displayed when you use the Extended Selection command from the popup menu to edit a gate for
a Special Symbol.

Figure 148. Select Pin Decal Dialog Box

Objects

Table  209. Select Pin Decal Dialog Box Contents

Name

Description

Pin Decal list

Lists the Pin Decals available to you.

Related Topics

Creating New Special Symbols

SailWind Logic Guide

709

SailWind Logic GUI Reference
Select Type of Editing Item Dialog Box

## Select Type of Editing Item Dialog Box

To access: Tools  > Part Editor  menu item > New  or Open  button

Use the Select type of editing item dialog box to select the type of library item to create or modify.

Figure 149. Select Type of Editing Item Dialog Box

Objects

Name

Part Type

Connector

CAE Decal

Pin Decal

Off-page

Power

Ground

710

Table  210. Select Type of Editing Item Dialog Box Contents

Description

Click Part Type to create or modify an existing part.

Click Connector to create or modify a connector.

Click CAE Decal to create or modify a new CAE decal.

Click Pin Decal to create or modify a pin decal, the information and
appearance of a terminal pin. A number of different pin decals are
provided.

Click Off-page to modify the off-page reference symbols. SailWind
Logic allows only one part definition in the library for off-page
reference symbols, so this option grays when you select the File

> New  menu item. You can modify the existing symbols or add
> new symbols. Refer to the Special Symbols  on page 167 topic for
> additional information.

Click Power to modify an existing off-page reference symbol.
SailWind Logic allows only one part definition in the library for
power symbols, so this option grays when you select the File

> New  menu item. You can modify the existing symbols or add
> new symbols. Refer to the Special Symbols  on page 167 topic for
> additional information.

Click Ground to modify an existing off-page reference symbol.
SailWind Logic allows only one part definition in the library for
ground symbols, so this option grays when you click the File  >
New  menu item. You can modify the existing symbols or add new
symbols. Refer to the Special Symbols  on page 167 topic for
additional information.

SailWind Logic Guide

Related Topics

Getting Gate Decals From the Library

SailWind Logic GUI Reference
Select Type of Editing Item Dialog Box

SailWind Logic Guide

711

SailWind Logic GUI Reference
Selection Filter Dialog Box

## Selection Filter Dialog Box

To access:

• Edit  > Filter  menu item

• With nothing selected, right-click > Filter  menu item

Use the Selection Filter to specify which objects you can select. Select a check box to enable the object
for selection or clear the check box to disable the object for selection.

Figure 150. Selection Filter Dialog Box

Objects

Name

Design Items

Drafting Items

Table  211. Selection Filter Dialog Box Contents

Description

Specifies the design items you want to be able to select in the
design.

Specifies the design items you want to be able to select in the
design.

Anything  button

Specifies that you want to select anything in the design.

Exception:  Clusters, unions, stitching vias, pin pairs, nets, and
board outline shapes are not selected.

Nothing  button

Specifies that you don’t want to select anything in the design.

712

SailWind Logic Guide

Related Topics

Using the Selection Filter

SailWind Logic GUI Reference
Selection Filter Dialog Box

SailWind Logic Guide

713

SailWind Logic GUI Reference
Selections Preview Dialog Box

## Selections Preview Dialog Box

To access:

• File  > Plot  menu item > Preview  button

• File  > Print  menu item > Preview  button

Use the Selections Preview dialog box to preview your options and output.

Figure 151. Selections Preview Dialog Box

Objects

Table  212. Selections Preview Dialog Box

Name

Description

Sheet  button

Displays the entire sheet in the window.

Extents  button

Zooms to the extents on the sheet.

Selected Sheets list

Specifies the sheet you want to preview.

714

SailWind Logic Guide

SailWind Logic GUI Reference
Selections Preview Dialog Box

Table  212. Selections Preview Dialog Box  (continued)

Name

Description

Options  button

Opens the Options dialog box  on page 606.

Plot/Print  button

Sends the output to the printer or plotter.

Preview area

Graphically shows what you will print or plot.

SailWind Logic Guide

715

SailWind Logic GUI Reference
Server Busy Dialog Box

## Server Busy Dialog Box

To access: There is no sure way to access this dialog box, but it may appear when you attempt to connect
with one of the other SailWind software applications, for example, when you click one of the buttons in the
Connect to SailWind Layout Dialog Box.

The Server Busy dialog box appears when you are launching another application from SailWind Logic
and for some reason, the other application is slow to respond.

Figure 152. Server Busy Dialog Box

Objects

Table  213. Server Busy Dialog Box Contents

Name

Description

Switch To  button

Switches to the application being launched. This is typically required when
a prompt window in the other application is waiting for your input before
you can connect to it with SailWind Logic.

Retry  button

Attempts to connect to the other application again. This is typically required
when there has been a delay in launching the other application.

 Tip
Wait until you see the application appear in your Windows Taskbar
then click Retry.

716

SailWind Logic Guide

SailWind Logic GUI Reference
Sheets Dialog Box

## Sheets Dialog Box

To access: Setup  > Sheets  menu item

Use the Sheets dialog box to edit the sheet set of the current schematic in the work area. Using Sheets
enables you to add and delete sheets from the set and to modify sheet names and the numeric order of
the set. You can create up to 1024 sheets.

Objects

Table  214. Sheets Dialog Box Contents

Name

Description

Numbered Sheets table

• Name  — Type a name for the schematic sheet.

• RefDes Start Value  — The minimum number to use for

reference designators of new components or copied/pasted
components. The first available number equal to or greater than
this value is used.

The RefDes Start Value stays with the sheet if the order
of sheets is changed. For more information, see “Setting
Reference Designators by Sheet in a New Schematic”  on
page 281

Bottom up hierarchy sheets are displayed but Top down hierarchy
sheets are not displayed. If you need to renumber reference
designators on a Top down sheet, see “Automatically Renumbering
Reference Designators”  on page 280.

SailWind Logic Guide

717

SailWind Logic GUI Reference
Sheets Dialog Box

Table  214. Sheets Dialog Box Contents  (continued)

Name

View  button

Description

Specifies to show the selected sheet in the view area.

Up/Down  buttons

Moves the selected sheet up or down in the table.

 Tip
The sheet value changes as you move it up or down.

Rename  button

Makes the selected cell available for editing.

 Tip
Spaces are not valid characters in a sheet name.

Adds a new sheet as a row to the bottom of the table.

Removes the selected sheet.

Add  button

Delete  button

Related Topics
Editing Sheets

718

SailWind Logic Guide

SailWind Logic GUI Reference
Signal Pin Nets Dialog Box

## Signal Pin Nets Dialog Box

To access:

• Edit  > Select Signal Pin Nets  menu item

• With nothing selected > right-click > Select Signal Pin Nets  menu item

Use the Signal Pin Nets dialog box to help you find and select specific signal pins in the schematic.

Figure 153. Signal Pin Nets Dialog Box

Objects

Name

Select Nets list

Refresh  button

Table  215. Signal Pin Nets Dialog Box Contents

Description

Selecting nets in this list box selects signal pin nets within the
schematic across all components and sheets. Using the right-click
menu, you can perform object mode commands on the selected
signal pin nets.

Updates the list of signal pin nets (in the Select Nets list box) to
include any recently created signal pin nets. For example, when
you add part 7400 to an empty design, you create two signal pin
nets: GND and +5V. Selecting Refresh  includes the new signal pin
nets in the Select Nets list box.

SailWind Logic Guide

719

SailWind Logic GUI Reference
Simulation Setup Dialog Box

## Simulation Setup Dialog Box

To access: Tools  > SPICE Netlist  menu item > Simulation Setup  button

After you add parts (with SPICE attributes) to your schematic, or add SPICE attributes to existing parts,
you can create a SPICE netlist in preparation for simulation.

Figure 154. Simulation Setup Dialog Box

Objects

Table  216. Simulation Setup Dialog Box Contents

Name

Description

AC Analysis  button

Opens the AC Analysis Dialog Box.

DC Sweep  button

Opens the DC Source Sweep Analysis Dialog Box.

Transient  button

Operating Point

Opens the Transient Analysis Dialog Box.

Directs the SPICE simulator to determine the DC operating point of
the circuit.

Related Topics

Creating a SPICE Netlist

720

SailWind Logic Guide

SailWind Logic GUI Reference
SPICEnet Dialog Box

## SPICEnet Dialog Box

To access: Tools  > SPICE Netlist  menu item

After you add parts (with SPICE attributes) to your schematic, or add SPICE attributes to existing parts,
you can create a SPICE netlist in preparation for simulation.

Figure 155. SPICEnet Dialog Box

Objects

Table  217. SPICEnet Dialog Box Contents

Name

Description

Output File Name

Specifies the path and name of the SPICE netlist file.

 Tip
Type the path or use the Browse  button to search for a path.

Select Sheets list

Specifies the sheets to include in the SPICE netlist.

Select All  button

Specifies to select all sheets in the Select Sheets list.

Unselect All  button

Specifies to clear all the selected sheets in the Select Sheets list.

Simulation Setup  button

Opens the Simulation Setup Dialog Box.

Include Subsheets

Specifies to include any underlying hierarchy if the design is
hierarchical.

Output Formats list

Specifies the target SPICE software.

Related Topics

Creating a SPICE Netlist

SailWind Logic Guide

721

SailWind Logic GUI Reference
Step and Repeat Dialog Box

## Step and Repeat Dialog Box

To access: Select an object during an add or duplicate operation > right-click > Step and Repeat  menu
item. When adding a new object in the Schematic Editor, you must place the first object manually before
you can use Step and Repeat.

Use Step and Repeat to multiply objects as you place them during an add or duplicate operation. Step
and Repeat is available in the Schematic Editor and the Decal Editor. In the Schematic Editor the Step
and Repeat command copies parts, connections, text, or drafting items. In the Decal Editor the Step and
Repeat command copies terminals, text, or drafting items.

Figure 156. Step and Repeat Dialog Box

Objects

Name

Direction

Count

Distance

Preview  button

Related Topics
Step and Repeat

Table  218. Step and Repeat Dialog Box Contents

Description

Specifies the direction of placement for the array.

Specifies the number of objects to place.

Specifies the distance between objects.

 Tip
If you place a second object and then Step and Repeat, the
spacing between the objects will become the default value in
the Distance box and will repeat the pattern you've started.

Displays the placement of the multiple objects based on the
options you set. The placement of the objects is based on the
location of the original object selected.

 Tip
Zoom Mode is available during Step and Repeat.

722

SailWind Logic Guide

SailWind Logic GUI Reference
Text Properties Dialog Box

## Text Properties Dialog Box

To access: Select text > right-click > Properties  menu item

Use the Text Properties dialog box to edit the properties of free text in the design.

Figure 157. Text Properties Dialog Box

Objects

Name

Text

X/Y

Rotation

Line Width

Table  219. Text Properties Dialog Box Contents

Description

Specifies the text that you are editing.

Type coordinates to place the text in a specified location. Negative
coordinates are not permitted. If you want to place text outside the
sheet, you must move it there with the cursor.

Specifies the rotation of the text: 0 or 90 degrees.

Specifies the line width for stroke fonts only.

SailWind Logic Guide

723

SailWind Logic GUI Reference
Text Properties Dialog Box

Table  219. Text Properties Dialog Box Contents  (continued)

Name

Size

Description

Specifies the size of the font.

Size (pts):  This is font size in points and appears for system fonts

Size (mils):  This is font character height and appears for stroke
fonts. The size refers to the height of the tallest characters.

Font Style

Enables you to change the font style to bold, italic, and underlined.

Font list

 Restriction:
System fonts only.

The fonts available to you. This lists either stroke fonts or system
fonts.

You choose which type of font to use in the Fonts Dialog Box.

 Tip

• Select stroke font or a system font.
• For system fonts, you can also click a font style button, or
any combination of styles: B  for bold, I  for italic, or U  for
underlined.

Horizontal/Vertical Justification

Specifies the horizontal (Right, Center, Left) justification and the
vertical (Up, Center, Down) justification of the text.

Parent  button

Opens the Drafting Properties Dialog Box.

 Restriction:
Available only if the text had been combined with a drafting
object.

Related Topics
Modifying Text

Add Free Text Dialog Box

724

SailWind Logic Guide

SailWind Logic GUI Reference
Transient Analysis Dialog Box

## Transient Analysis Dialog Box

To access: Tools  > SPICE Netlist  menu item > Simulation Setup  button> Transient  button

Use the Transient Analysis dialog box to set options specifically for a Transient analysis.

Figure 158. Transient Analysis Dialog Box

Objects

Table  220. Transient Analysis Dialog Box Contents

Name

Description

Data Step Time

Specifies the increment for the analysis.

Total Analysis Time

Specifies the time to end the analysis.

Time to Start Recording Data

Specifies the time to start recording data from the analysis.

 Tip
Use this if your simulation files become too large and you are
not interested in data from the beginning of the analysis.

Maximum Time Step

Specifies the maximum time step value.

Use Initial Conditions (UIC)

Specifies to use SPICE to solve for the quiescent operating
point before beginning the transient analysis. SPICE uses the
values specified using IC=... on the various elements as the initial
transient condition and proceeds with the analysis.

Related Topics

Creating a SPICE Netlist

Setting Up Transient Analysis

SailWind Logic Guide

725

SailWind Logic GUI Reference
Update From Library Dialog Box

## Update From Library Dialog Box

To access: Tools  > Update from Library  menu item

Use the Update from Library dialog box to update a schematic from the library, or to compare items in a
schematic with those in the library.

Figure 159. Update From Library Dialog Box

Objects

Control

Table  221. Update From Library Dialog Box Controls

Description

Mode area  — Choose compare or update mode.

Generate comparison report

Select this check box to compare library and
schematic items and generate a report file.

726

SailWind Logic Guide

Table  221. Update From Library Dialog Box Controls  (continued)

Control

Description

SailWind Logic GUI Reference
Update From Library Dialog Box

Update design from library

Include items with identical time stamp

Select this check box to compare library and
schematic items, update the schematic from the
library, and generate a report file.

Timestamps are assigned and updated in the
SailWind Logic Library routines, but it is possible
for items with identical timestamps to have
different content in the library and schematic if the
item is edited outside the Library routines.

For example, if you export a schematic to an
ASCII file, manually edit a part type in the ASCII
file, and import the schematic back into SailWind
Logic, the timestamp of the part type will be
unchanged, but the content will be different.

Use this check box to specify whether to
compare/update items whose timestamps are the
same in the library and schematic.

Items with identical timestamps are not  compared
or updated unless this check box is selected.

Report Filtering area  — Specify what you want to see in the report.

Summary and details

Summary only

Hide identical results

Select Summary and details or Summary only.

Select Hide identical results to see only the
differences between library and design items in the
report.

Items area  — Specify the items you want to compare or update.

Part types and attributes

Select this check box to include part types and
their attributes in the comparison or update.

Preserve design attributes not found in library

 Tip

• Attributes don’t have timestamps, so they

can’t be updated independently of their part
types.

• If a schematic attribute’s corresponding
attribute in the library is a placeholder
attribute (with a blank value), it will be
updated only if the “Allow overwriting of
attribute values in design with blank values
from library” check box in the Options
Dialog Box, Design Category.

Use this check box to specify what you want to do
with attributes that are found in the schematic but
not in the library:

• Select the check box to keep these attributes in

the updated parts.

• Clear it to remove them from the updated parts.

SailWind Logic Guide

727

SailWind Logic GUI Reference
Update From Library Dialog Box

Table  221. Update From Library Dialog Box Controls  (continued)

Control

Description

Add new attributes not found in design

Update common attributes

Preserve design attribute properties

Visibility

Label location

Label properties

CAE Decals

Pin Decals

Select Pins Decals List

Use this check box to specify what you want to do
with attributes that are found in the library but not
in the schematic.

• Select the check box to add these attributes to

the updated parts.

• Clear it to not add them to the updated parts.

Use this check box to specify what you want to do
with attributes that are found in both the schematic
and the library.

• Select the check box to update the parts with

the library versions.

• Clear it to leave the part attributes as they are

(that is, do not update them).

Select the attribute properties you want to
preserve in the schematic when updating the
attributes from the library.

Select this check box to include CAE decals in the
comparison/update.

• If you want to update CAE decal assignments
in the part types, you must also select Part
types and attributes.

• Pin decals are updated as part of a CAE decal
update, so when this check box is selected, Pin
Decals is automatically selected also.

Select this check box to include pin decals in the
comparison/update.

 Tip

• Only the decal is updated; pin names and

numbers are not changed.

• Pin decals are updated as part of a CAE
decal update, so when CAE Decals is
selected, this check box is automatically
selected and unavailable.

This list is populated with check boxes
representing each of the pins available for
comparison or update. Enable the check box for
each of the pins you want to compare or update.

728

SailWind Logic Guide

Table  221. Update From Library Dialog Box Controls  (continued)

Control

Description

SailWind Logic GUI Reference
Update From Library Dialog Box

 Tip
Because all  pin decals are compared/updated
as part of a CAE decal update, these check
boxes are unavailable and ignored when CAE
Decals is selected.

Select this check box to include off-page symbols
in the comparison/update. Selecting this check box
opens the Remap Special Symbols Dialog Box.

 Restriction:
The off-page symbol update will fail if there is
not at least one off-page symbol in the current
schematic.

Select this check box to include ground symbols in
the comparison/update. Selecting this check box
opens the Update From Library Dialog Box.

 Restriction:
The ground symbol update will fail if there is
not at least one ground symbol in the current
schematic.

Select this check box to include power symbols in
the comparison/update. Selecting this check box
opens the Update From Library Dialog Box.

 Restriction:
The power symbol update will fail if there is
not at least one power symbol in the current
schematic.

Off-page symbols

Ground symbols

Power symbols

Related Topics

The Update From Library Function

How to Read the Update Report

The Compare/Update Process

Updating a Schematic From the Library

SailWind Logic Guide

729

SailWind Logic GUI Reference
Update Selected CAE Decals From Library Dialog Box

## Update Selected CAE Decals From Library Dialog Box

To access: Select a part > Right-click > Update  > CAE Decal  menu item

Use the Update Selected CAE Decals from Library dialog box to update selected CAE decals in a
schematic from the library. All instances of the selected CAE decals are updated.

Figure 160. Update Selected CAE Decals From Library Dialog Box

Objects

Control

Table  222. Update Selected CAE Decals From Library Dialog Box Controls

Description

Mode area  — Choose compare or update mode.

Generate comparison report

Update design from library

Select this check box to compare library and
design CAE decals and generate a report file.

Select this check box to compare library and
schematic CAE decals, update the schematic from
the library, and generate a report file

730

SailWind Logic Guide

Table  222. Update Selected CAE Decals From Library Dialog Box Controls  (continued)

SailWind Logic GUI Reference
Update Selected CAE Decals From Library Dialog Box

Control

Include items with identical time stamp

Description

 Tip

• This procedure updates the pin

assignments in the selected CAE decals,
but doesn’t update the pin decals
themselves. Use one of the procedures
in Updating Selected Pin Decals From
the Library  to update the pin decals’
geometries.

• As a corollary, if, for instance, CAE decal

X is updated to use PINB instead of PINA,
it uses the version of PINB geometry
currently in the schematic. If there is no
PINB in the schematic, it is installed from
the library.

Timestamps are assigned and updated in the
SailWind Logic Library routines, but it is possible
for items with identical timestamps to have
different content in the library and schematic if the
item is edited outside the Library routines.

For example, if you export a schematic to an
ASCII file, manually edit a CAE decal in the
ASCII file, and import the schematic back into
SailWind Logic, the timestamp of the decal will be
unchanged, but the content will be different.

Use this check box to specify whether to
compare/update items whose timestamps are the
same in the library and schematic.

Items with identical timestamps are not  compared
or updated unless this check box is selected.

Select CAE Decals Area  — Specify which CAE decals to update.

Select CAE Decals List

This list is populated with check boxes
representing each of the selected CAE decals.
Enable the check box for each of the CAE decals
that you would like to update.

Report Filtering area  — Specify what you want to see in the report.

Summary and details

Summary only

Hide identical results

Select Summary and details or Summary only.

Select Hide identical results to see only the
differences between library and schematic items in
the report. This will shorten the report.

Related Topics

The Update From Library Function

How to Read the Update Report

SailWind Logic Guide

731

SailWind Logic GUI Reference
Update Selected CAE Decals From Library Dialog Box

The Compare/Update Process

Updating Selected CAE Decals From the Library

732

SailWind Logic Guide

SailWind Logic GUI Reference

## Update Selected Part Type From Library Dialog Box

Update Selected Part Type From Library
Dialog Box

To access: In the Schematic Editor, select the part types you want to compare/update. Right-click >
Update  > Part Type  menu item

Use the Update Selected Part Type from Library dialog box to update selected parts in a schematic from
the library, or to compare selected parts in a schematic with those in the library.

Objects

Control

Table  223. Update Selected Part Type From Library Dialog Box Controls

Description

Mode area  — Choose compare or update mode.

Generate comparison report

Select this check box to compare library and
schematic part types and generate a report file.

SailWind Logic Guide

733

SailWind Logic GUI Reference
Update Selected Part Type From Library Dialog Box

Table  223. Update Selected Part Type From Library Dialog Box Controls  (continued)

Control

Description

Update design from library

Include items with identical time stamp

Select this check box to compare library and
schematic part types, update the schematic from
the library, and generate a report file.

 Restriction:
All parts having the same part type as a
selected part are updated, but attributes are
updated only for the parts actually selected.

Timestamps are assigned and updated in the
SailWind Logic Library routines, but it is possible
for items with identical timestamps to have
different content in the library and schematic if the
item is edited outside the Library routines.

For example, if you export a schematic to an
ASCII file, manually edit a part type in the ASCII
file, and import the schematic back into SailWind
Logic, the timestamp of the part type will be
unchanged, but the content will be different.

Use this check box to specify whether to
compare/update items whose timestamps are the
same in the library and schematic.

Items with identical timestamps are not  compared
or updated unless this check box is selected.

Report Filtering area  — Specify what you want to see in the report.

Summary and details

Summary only

Hide identical results

Select Summary and details or Summary only.

Select Hide identical results to see only the
differences between library and design items in the
report. This will shorten the report.

Items area  — Specify the items you want to compare or update.

Part types and attributes

Make sure that this check box is selected.

Preserve design attributes not found in library

 Tip

• Attributes don’t have timestamps, so they

can’t be updated independently of their part
types.

• If a schematic attribute’s corresponding
attribute in the library is a placeholder
attribute (with a blank value), it will be
updated only if the Allow overwriting of
attribute values in design with blank values
from library check box in the Options Dialog
Box, Design Category.

Use this check box to specify what you want to do
with attributes that are found in the schematic but
not in the library:

• Select the check box to keep these attributes in

the updated parts.

734

SailWind Logic Guide

SailWind Logic GUI Reference
Update Selected Part Type From Library Dialog Box

Table  223. Update Selected Part Type From Library Dialog Box Controls  (continued)

Control

Description

Add new attributes not found in design

Update common attributes

Preserve design attribute properties

Visibility

Label location

Label properties

• Clear it to remove them from the updated parts.

Use this check box to specify what you want to do
with attributes that are found in the library but not
in the schematic.

• Select the check box to add these attributes to

the updated parts.

• Clear it to not add them to the updated parts.

Use this check box to specify what you want to do
with attributes that are found in both the schematic
and the library.

• Select the check box to update the parts with

the library versions.

• Clear it to leave the part attributes as they are

(that is, do not update them).

Select the attribute properties you want to
preserve in the schematic when updating the
attributes from the library.

Select Part Types Area  — Specify which part types to update.

Select part types list

This list is populated with check boxes
representing each of the selected part types.
Enable the check box for each of the part types
that you would like to update.

Related Topics

The Update From Library Function

How to Read the Update Report

The Compare/Update Process

Updating Selected Part Types From the Library

SailWind Logic Guide

735

SailWind Logic GUI Reference
Update Selected Pin Decals From Library Dialog Box

## Update Selected Pin Decals From Library Dialog Box

To access: Select a pin > Right-click > Update Pin Decal  menu item

Use the Update Selected Pin Decal from Library dialog box to update selected pin decals from the library,
or to compare selected pin decals in a schematic with those in the library. All instances of the selected pin
decals are updated.

Figure 161. Update Selected Pin Decals From Library Dialog Box

Objects

Control

Table  224. Update Selected Pin Decals From Library Dialog Box Controls

Description

Mode area  — Choose compare or update mode.

Generate comparison report

Update design from library

Include items with identical time stamp

Select this check box to compare library and
schematic pin decals and generate a report file.

Select this check box to compare library and
schematic pin decals, update the schematic from
the library, and generate a report file.

Timestamps are assigned and updated in the
SailWind Logic Library routines, but it is possible

736

SailWind Logic Guide

SailWind Logic GUI Reference
Update Selected Pin Decals From Library Dialog Box

Table  224. Update Selected Pin Decals From Library Dialog Box Controls  (continued)

Control

Description

for items with identical timestamps to have
different content in the library and schematic if the
item is edited outside the Library routines.

For example, if you export a schematic to an
ASCII file, manually edit a pin decal in the
ASCII file, and import the schematic back into
SailWind Logic, the timestamp of the decal will be
unchanged, but the content will be different.

Use this check box to specify whether to
compare/update items whose timestamps are the
same in the library and schematic.

Items with identical timestamps are not  compared
or updated unless this check box is selected.

Select Pin Decals Area  — Specify which pin decals to update.

Select Pin Decals List

This list is populated with check boxes
representing each of the selected pin decals.
Enable the check box for each of the pin decals
that you would like to update.

Report Filtering area  — Specify what you want to see in the report.

Select Summary and details or Summary only.

Select Hide identical results to see only the
differences between library and schematic items in
the report. This will shorten the report.

Summary and details

Summary only

Hide identical results

Related Topics

The Update From Library Function

How to Read the Update Report

The Compare/Update Process

Updating Selected Pin Decals From the Library

SailWind Logic Guide

737

SailWind Logic GUI Reference
Update Selected Pin Decals From Library Dialog Box

738