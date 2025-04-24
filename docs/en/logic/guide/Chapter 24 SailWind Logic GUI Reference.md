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
Options Dialog Box - Part Editor, General Categor   
Options Dialog Box - Print/Plot   
Output Window   
SailWind Layout Link Dialog Box   
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

## AC Analysis Dialog Box

To access: Tools $>$ SPICE Netlist menu item $>$ Simulation Setup button $>$ AC Analysis button  

Set options specifically for an AC analysis.  

![](/images/54d6e4a0ded526dd285adbb7ea271c01a4e9be05d677ea8a6657802a459f6fb3.jpg)  

!Note:  

Pictures in this document are for reference only, to help users better understand the software operation. In the case of interface difference due to version changes, the interface of SailWind Logic in practice shall prevail.  

![](/images/5af88e404aded28368643f4d83290d6961ca2703a40257b734f0da7691631779.jpg)  
Figure 14. AC Analysis Dialog Box  

**Objects**  

Table 48. AC Analysis Fields   


|  Name         | Description                                                                  |
|---------------|------------------------------------------------------------------------------|
| Interval area | Specifies the number of points and the variation: Decade, Octave, or Linear. |
| Frequency     | Specifies the Starting and Ending frequencies.                               |

**Related Topics**  

Creating a SPICE Netlist Setting Up AC Analysis  

## Add Attribute Label Dialog Box

To access:  

• Select a part $>$ right-click $>$ Edit Part menu item $>$ Edit Graphics button $>$ select a gate $>$ Decal Editing Toolbar button $>$ Add Attribute Label button   
• With nothing selected $>$ Tools $>$ Part Editor menu item $>$ Edit Graphics button $>$ Decal Editing Toolbar button $>$ Add Attribute Label button  

Use the Add Attribute Label dialog box to create attribute labels while editing or creating a CAE Decal.  

![](/images/4e02f638dff7b1f8ee27aca0b2c18fecba0b518b79559d42dd12ca357ed6e08c.jpg)  
Figure 15. Add Attribute Label Dialog Box  

**Objects**  

Table 49. Edit Attribute Label Fields   


| Name                              | Description                                                                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Attribute Name list               | Lists all of the attributes available to you. Tip You can type the attribute name or browse the Library                     |
| Browse Lib.Attr.button            | Attributes. Opens the Browse Library Attributes Dialog Box.                                                                 |
| Height                            | Specifies the height of the text.                                                                                           |
| Width                             | Specifies the width of the text.                                                                                            |
| Rotation                          | Specifies the rotation of the text: O or 90 degrees.                                                                        |
| Horizontal/Vertical Justification | Specifies the horizontal (Right, Center, Left) justification and the vertical (Up, Center, Down) justification of the text. |

## Add Bus Dialog Box

To access: Schematic Editing toolbar $>$ Add Bus button $>$ click to indicate starting point $>$ double-click to indicate ending point  

Use the Add Bus dialog box to create attribute labels while editing or creating a CAE Decal.  

![](/images/fc8dac29b7ef4ccb7ee96d76884fd1a19fcad80811438d25c62529cf196c1ede.jpg)  

## Figure 16. Add Bus Dialog Box  

**Objects**  

Table 50. Add Bus Dialog Box Fields   


| Name          |  Description                                                                                              |
|---------------|-----------------------------------------------------------------------------------------------------------|
| Bus Name      | Specifies the name of the bus. Select or type the name you want.                                          |
| Rename area   | Specifies to rename this instance or all instances of the bus. Restriction: Available only in query mode. |
| Bus Type area | Specifies which bus names appear in the Bus Name list.                                                    |

Table 50. Add Bus Dialog Box Fields (continued)   


|  Name                                                                                                                                                                                        | Description                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Add Bus Name Label                                                                                                                                                                           | Select the Add Bus Name Label check box to add the bus name as a label to the bus at the end of the bus closest to where you selected it. |
| Restriction: The check box is unavailable when the end of the selected bus has a label. Tip                                                                                                  |
| · A bus can have two labels, one on each end. · A bus label is not required. · To delete a bus label, select the label in the schematic and click the Delete button on the standard toolbar. |
|                                                                                                                                                                                              | Lists the name or prefix of the bus net, the starting bit number for a sequence of nets, and the ending bit number for a sequence of      |
| nets. Restriction:                                                                                                                                                                           |
| Available only if the bus is a mixed net bus. 1 Tip                                                                                                                                          |
| · For a single net, type the net name.                                                                                                                                                       |
| · For a range of sequential nets, type the prefix for the sequence of nets.                                                                                                                  |
|                                                                                                                                                                                              | Adds a row to the Bus Nets table. Restriction:                                                                                            |
| Available only if the bus is a mixed net bus. Makes the selected row available for editing.                                                                                                  |
|                                                                                                                                                                                              | Restriction:                                                                                                                              |
| Available only if the bus is a mixed net bus. Removes the selected row from the Bus Nets table.                                                                                              |
|                                                                                                                                                                                              | Restriction:                                                                                                                              |
| Available only if the bus is a mixed net bus.                                                                                                                                                |
| Down/Up buttons                                                                                                                                                                              | Moves the selected row up or down in the Bus Nets table.                                                                                  |
| Restriction: Available only if the bus is a mixed net bus.                                                                                                                                   |

**Related Topics**  

Managing Buses

## Add/Edit Command Dialog Box  

To access: Tools $>$ Customize menu item $>$ Commands tab $>$ select a command $>$ New or Edit button  

Use the Add Command dialog box to create commands that you can then use as selections on menus or as buttons on toolbars.  

![](/images/119a0291dd45ca91e0737a0bf78fc71daae6023b12971e5f741ac5e0fdeb0fee.jpg)  
Figure 17. Add Command Dialog Box  

**Objects**  

Table 51. Add/Edit Dialog Box Fields   


|  Name             | Description                                                                                                                                              |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Command name      | The name of the new command. O Tip.                                                                                                                      |
| Based on          | Type an ampersand before the letter you want to use as the Alt keyboard shortcut.                                                                        |
| Arguments         | The command on which you want to base the new command. Any arguments for the new command.                                                                |
|                   | Tip Use a space to separate arguments. If an argument contains a space, enclose the argument in quotation marks (""). Restriction: SailWind Router only. |
| Description       | Lists what the new command does.                                                                                                                         |
| Use Default Image | Use the recommended image.                                                                                                                               |

Table 51. Add/Edit Dialog Box Fields (continued)   


|  Name                     | Description                                                        |
|---------------------------|--------------------------------------------------------------------|
| Select User-defined Image | Select or create your own image to associate with the new command. |
| New button                | Open the Edit Button Image Dialog Box.                             |
| Edit button               | Open a button in the Edit Button Image Dialog Box.                 |

**Related Topics**  

Creating a Custom Command Creating a Custom Menu  

## Add Field Dialog Box  

To access: Select nothing or a 2D line object $>$ right-click $>$ Add Field menu item Use the Add Field dialog box to add a field to your schematic.  

![](/images/c1ef2c5bcf7e102b491e9fb20e7aabf9ab135e795927678eebf9181e012e6f84.jpg)  
Figure 18. Add Field Dialog Box  

**Objects**

Table 52. Add Field Dialog Box Fields   


| Name                                                                                        | Description                                                                        |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Name list                                                                                   | Type the name of a new field or select from a list of the fields available to you. |
| Value                                                                                       | The value of the field.                                                            |
| Restriction:                                                                                |
| The Value box is unavailable for system fields since the value is derived from your system. |
| X/Y                                                                                         | Type coordinates to place the field label in a specified location.                 |

Table 52. Add Field Dialog Box Fields (continued)   


|  Name                             | Description                                                                                                                                                                                                                                          |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                   | Tip Leave these blank to attach the field to your pointer and click to indicate the location.                                                                                                                                                        |
| Rotation                          | Specifies the rotation of the text: O or 90 degrees.                                                                                                                                                                                                 |
| Line Width                        | Specifies the line width for stroke fonts only. text Stroke Line Width                                                                                                                                                                               |
| Size                              | Specifies the size of the font. Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke fonts. The 'size refers to the height of the tallest characters. ↑Gg          |
| Font Style                        | Enables you to change the font style to bold, italic, and underlined. Restriction: System fonts only.                                                                                                                                                |
|                                   | The fonts available to you. This lists either stroke fonts or system fonts. You choose which type of font to use in the Fonts Dialog Box. 1Tip · Select stroke font or a system font. · For system fonts, you can also click a font style button, or |
| Horizontal/Vertical Justification | Specifies the horizontal (Right, Center, Left) justification and the vertical (Up, Center, Down) justification of the text.                                                                                                                          |

**Related Topics**  

Adding a Field  

## Add Free Text Dialog Box  

To access: Schematic Editing toolbar $>$ Create Text button  

Use the Add Free Text dialog box to add free text (not belonging to another object).  

![](/images/06bde94cc59d5c8c67c142f0d317c7da253ad1b13cb90337c79a3727eaf0d01d.jpg)  
Figure 19. Add Free Text Dialog Box  

**Objects**

Table 53. Add Free Text Dialog Box Fields   


|  Name      | Description                                                                                                                                                                                                                                  |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Text       | Type the text you want in the schematic.                                                                                                                                                                                                     |
| X/Y        | Places the text in a specified location. Negative coordinates are not permitted. If you want to place text outside the sheet, you must move it there with the cursor. 1Tip Leave these blank to attach the text to your pointer and click to |
| Rotation   | indicate the location. Specifies the rotation of the text: O or 90 degrees.                                                                                                                                                                  |
| Line Width | Specifies the line width for stroke fonts only.                                                                                                                                                                                              |

Table 53. Add Free Text Dialog Box Fields (continued)   


|  Name                             |  Description                                                                                                                                                                                                                                        |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                   | text Stroke Line Width                                                                                                                                                                                                                              |
|                                   | Specifies the size of the font. Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke fonts. The 'size refers to the height of the tallest characters. Gg          |
| Font Style                        | Enables you to change the font style to bold, italic, and underlined. Restriction: System fonts only.                                                                                                                                               |
| Font list                         | The fonts available to you. This lists either stroke fonts or system fonts. You choose which type of font to use in the Fonts Dialog Box. Tip · Select stroke font or a system font. · For system fonts, you can also click a font style button, or |
| Horizontal/Vertical Justification | Specifies the horizontal (Right, Center, Left) justification and the vertical (Up, Center, Down) justification of the text.                                                                                                                         |

**Related Topics**  

Adding Text  

## Add Net to Class Dialog Box  

To access: With nothing selected, right-click $>$ Select Nets $>$ select one or more nets $>$ right-click $>$ Make Class menu item  

Use the Add Net to Class dialog box to create a new class or to add nets to an existing class.  

![](/images/c82bd3c61b94f4a2251baf225f34b149f32281f806a7bd38eb3e1e54a32f9754.jpg)  
Figure 20. Add Net to Class Dialog Box  

**Objects**  

Table 54. Add Net Class Dialog Box Fields   


| Name                                                                                           | Description                                                             |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Create New Class                                                                               | Specifies to create a new class using the selected net(s).              |
| Add to Existing Class                                                                          | Specifies to add the selected net(s) to an existing class. Restriction: |
| This is unavailable if there are no existing classes.                                          |
| Selected Nets                                                                                  | Lists all of the nets you selected in the schematic.                    |
| Add to Class                                                                                   | Specifies the name of the class. Type a new name or accept the default. |
| Restriction: This is unavailable if you select Add to Existing Class an only one class exists. |
| Existing Classes                                                                               | Lists all of the existing classes in the schematic.                     |

## Add New Attribute Dialog Box  

To access: Edit $>$ Attribute Manager menu item $>$ Add Attr button  

Use the Add New Attribute dialog box to set name and value properties when adding new attributes to the schematic.  

![](/images/7f189f49f8b2a819aa271b06ddb50f150d714726ed34ef177d829470dfb63d03.jpg)  
Figure 21. Add New Attribute Dialog Box  

**Objects**  

Table 55. Add New Attribute Dialog Box Fields   


|  Name                   |  Description                                    |
|-------------------------|-------------------------------------------------|
| Browse Lib. Attr button | Opens the Browse Library Attributes Dialog Box. |
| Attribute Name          | The name of the new attribute.                  |
| Attribute Value         | The value of the new attribute.                 |

**Related Topics**  

Manage Attributes in a Schematic  

## Add New Attribute to Library Dialog Box

To access: File $>$ Library menu item $>$ Library Manager dialog box $>$ Attr Manager button $>$ Add Attr button  

Use the Add New Attribute to Library dialog box to set name and value properties when adding new attributes to libraries.  

![](/images/877132871d70a553eb98d671953c728e4cb7bbeb220f169ca473d152260c1466.jpg)  
Figure 22. Add New Attribute to Library Dialog Box  

**Objects**  

Table 56. Add New Attribute to Dialog Box Fields   


|  Name                   | Description                                     |
|-------------------------|-------------------------------------------------|
| Browse Lib. Attr button | Opens the Browse Library Attributes Dialog Box. |
| Attribute Name          | The name of the new attribute.                  |
| Attribute Value         | The value of the new attribute.                 |

## Add Part From Library Dialog Box

To access: Schematic Editing toolbar $>$ Add Part button  

Use the Add Part from Library dialog box to load a part from a library into the current schematic drawing.   
SailWind Logic automatically assigns a reference designator when you add the part.  

![](/images/f0505a55bd05ab6833c715ef871a8c1e02050a0dbaa65138c57d457d3d6c9ba8.jpg)  
Figure 23. Add Part From Library Dialog Box  

**Objects**  

Table 57. Add Part From Library Dialog Box Fields   


| Name                                                                                                                                           | Description                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Preview area                                                                                                                                   | Shows the selected item.                                                                                              |
| Items                                                                                                                                          | Lists the items in the selected library. The number of objects that appear depends on the filter settings.            |
| Library list                                                                                                                                   | Specifies the library you want to use.                                                                                |
| Items                                                                                                                                          | Narrows the search. You can use wildcards or expressions on page 105. An asterisk (*) displays all parts in the list. |
| Apply button                                                                                                                                   | Searches the library for the specified item.                                                                          |
| Part Name list                                                                                                                                 | Select a recently used part.                                                                                          |
| Tip The sixteen most recently used parts are available in the Part                                                                             |
| Name dropdown list box. You can clear this buffer by removing the entries in the SailWindlogic.ini file, under the [Last Added Parts] heading. |

**Related Topics**  

Adding Parts  

## Add Pins Dialog Box  

To access:  

File $>$ Library menu item $>$ select a Library $>$ Parts button $>$ New button $>$ on the Part Editor Toolbar click Edit Electrical $>$ Pins tab $>$ Add Pins button   
• File $>$ Library menu item> select a Library $>$ Parts button $>$ select a part $>$ Edit button $>$ on the Part Editor Toolbar click Edit Electrical $>$ Pins tab $>$ Add Pins button  

Use the Add Pins dialog box to add pins to a part type.  

![](/images/ffb199a05292422a9a2dfdf2d3b4f56f8b76f15f4ccc93b7df2bb13aa8b16609.jpg)  
Figure 24. Add Pins Dialog Box  

**Objects**  

Table 58. Add Pins Dialog Box Fields   


|  Name                                                                                                                                             | Description                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Number of pins                                                                                                                                    | Specifies the number of pins to add using the Add Pins dialog box. |
| Prefix                                                                                                                                            | The prefix you want for your pins.                                 |
|  Tip                                                                                                                                              |
| · Alphabetic and numeric values can be used. For example A1 or 1A. ·For a single numeric, use either Prefix or Suffx box, and void the other box. |
| Suffix                                                                                                                                            | The suffix you want for your pins.                                 |

Table 58. Add Pins Dialog Box Fields (continued)   


|  Name                             | Description                                                                                                                          |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
|                                   | Tip · Alphabetic and numeric values can be used. For example, A1 or 1A. · For a single numeric, use either Prefix or Suffix box, and |
| Pin numbers                       | void the other box. A preview of pin numbers based on your input in the Prefix and Suffix boxes.                                     |
| Increment prefix/lncrement suffix | Indicates whether you want the prefix or the suffix to increment.                                                                    |
| Step value                        | A positive or negative number by which to increase or decrease the pin numbers with consecutive or stepped values.                   |
| Verify valid JEDEC pin numbering  | Ensures that legal alphanumeric values are used.                                                                                     |

## Archiver Dialog Box  

To access: File $>$ Archive menu item  

Use the Archiver dialog box to create archives of your schematics, designs, files and folders, and libraries.  

![](/images/d8f6b5b967bfc41bc1b95714bee7bfc8b8974588e6045dd1e1274cf0a4c6579e.jpg)  
Figure 25. Archiver Dialog Box  

**Objects**  

Table 59. Archiver Dialog Box Fields   


| Name       | Description                                                                                                                                                                                                 |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCB Design | Specifies the location and name of the PCB design you want to archive. To choose the file you want, type the location or click the Browse button. Select Create PDF to create a PDF file of the PCB design. |

Table 59. Archiver Dialog Box Fields (continued)   


| Name                                                                                                                                     | Description                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schematic                                                                                                                                | Specifies the location and name of the schematic file you want to archive. This is automatically populated with the information from the current design. To change the design, or if no design was opened, type the location or click the Browse button. |
| Specifies to create a PDF file of the schematic file. Restriction:                                                                       |
| Add libraries                                                                                                                            | design. Specifies that you want to include libraries in the archive. · All — Add all of your libraries to the archive.                                                                                                                                   |
| · Select — Add only the libraries you specify. Click the Browse button to open the Archiver Libraries Dialog Box.                        |
| Additional files                                                                                                                         | Specifies that you want to include other files and folders in your archive. Click the Browse button to open the Archiver Additional Files Dialog Box.                                                                                                    |
| Target folder                                                                                                                            | Specifies_where you want the archive to be located. Type the path or click the Browse button. Requirement: The target folder must be empty.                                                                                                              |
| Compress using zip format                                                                                                                | Specifies to create a zip file. The file will be in the following format:                                                                                                                                                                                |
| Where YYYY is the year, MM is the month, DD is the day, HH is the hour - in military time, MM is the minute, and SS is the second of the |

**Related Topics**  

Archiving Your Schematic  

## Archiver Additional Files Dialog Box  

To access: File $>$ Archive menu item $>$ Additional Files check box $>$ Browse button  

Use the Archiver: Additional dialog box to add files and folders to the schematic you want to archive  

![](/images/795c79421468a475f91ecba5fe7794b3fdd3df02c17b4e3d721e16db068d13ac.jpg)  
Figure 26. Archiver Additional Files Dialog Box  

**Objects**  

Table 60. Archiver Additional Fields Dialog Box   


| Name                  | Description                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------|
| Additional files list | Lists the files and folders you want to include in your archive.                                                         |
| Add File button       | Opens the Additional File dialog box where you can select individual files you want to add to the Additional files list. |
| Add folder button     | Opens the Browse for Folder dialog box where you can select an entire folder to add to the Additional files list.        |
| Remove button         | Removes the selected file or folder from the Additional files list.                                                      |
| Remove All button     | Removes all of the files and folders from the Additional files list.                                                     |

**Related Topics**  

Archiving Your Schematic  

## Archiver Libraries Dialog Box  

To access: File $>$ Archive menu item $>$ Add libraries check box $>$ Select $>$ Browse button Use the Archiver: Libraries dialog box to add libraries to the schematic you want to archive.  

![](/images/a7ca6df0b55bfb3250526db6d1877b3dcdc693757b6b23a06817d6aba759aca3.jpg)  
Figure 27. Archiver Libraries Dialog Box  

**Objects**  

Table 61. Archiver Libraries Dialog Box Fields   


|  Name                | Description                                                                                                                                               |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Available libraries  | Lists all of the libraries available for you to add to the archive. Restriction: If your library is not listed in the Library Manager, it will not appear |
| Add >> button        | in this list. Moves the selected library from the Available libraries list to the                                                                         |
| << Remove button     | Selected libraries list. Moves the selected library from the Selected libraries list to the                                                               |
| Add all >> button    | Available libraries list. Moves all of the libraries from the Available libraries list to the Selected                                                    |
| << Remove all button | libraries list.                                                                                                                                           |
|                      | Moves all of the libraries from the Selected libraries list to the Available libraries list.                                                              |

## ASCII Output Dialog Box  

To access: File $>$ Export menu item $>$ type a filename $>$ Save button Use the ASCII Output dialog box to select the sections you want to export to the ASCII file.  

![](/images/5e6d25447c678d8a9e854ce6438c2c23b1fd7f282c4a86824e22b4d3e09cc898.jpg)  
Figure 28. ASCII Output Dialog Box  

**Objects**  

Table 62. ASCII Output Dialog Box Fields   


| Name             | Description                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Schematic Params | Specifies to export the default system settings from the Options tabs.                                                      |
| Sheet Params     | Specifies to export the specific sheet information such as window scale, centering, etc.                                    |
| Text             | Specifies to export the free text together with location, level, and size.                                                  |
| Lines            | Specifies to export the 2D-line items.                                                                                      |
| Plot Params      | Specifies to export the information related to the CAM output settings and configurations generated using the Plot command. |
| Fields           | Specifies to export the fields used in the schematic and their values.                                                      |
| Decals           | Specifies to export the part decals and their contents.                                                                     |
| Part Types       | Specifies to export the library part attributes such as manufacturer, cost, and notes.                                      |

Table 62. ASCII Output Dialog Box Fields (continued)   


|  Name               | Description                                                                                          |
|---------------------|------------------------------------------------------------------------------------------------------|
| Parts               | Specifies to export the parts used in the schematic and their reference designators.                 |
| Connections         | Specifies to export all connections on the schematic, including paths, tie-dots, and off-page flags. |
| Rules               | Specifies to export the clearance, routing, and others specified in Design Rules.                    |
| Select All button   | Selects all items.                                                                                   |
| Unselect All button | Clears all items.                                                                                    |
| Output Version      | Specifies the version of the software you are using.                                                 |
| Filename            | Displays the location and name of the file. This was specified in the File Export dialog box OTip    |

**Related Topics**  

Exporting to ASCII Output  

## Assign Alternatives for Ground Part Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ Part Editor $>$ Open button $>$ Ground $>$ OK button $>$ Edit Electrical button  

Use the Assign Alternatives for Ground Part dialog box to assign or create additional ground symbols.  

Note:   
For additional information on the creation and use of special schematic symbols, see “Special Schematic Symbols” on page 167.  

![](/images/a8533bb088030369e5824c7bd6b13a4eca4d96d04171f63a9ad7c3810ba372d0.jpg)  

Figure 29. Assign Alternatives for Ground Part Dialog Box   


|  Name           | Description                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Picture         | Displays a picture of the selected Special Symbol.                                                                              |
| Attribute table | • Special Symbol — The name of a connector pin decal for use in the schematic. · Pin Type — The function of the special symbol. |
|                 | · Signal Name - The name of the signal. Opens the Browse for Special Symbols Dialog Box.                                        |

**Objects**  

Table 63. Assign Alternatives For Ground Part Dialog Box Fields

Table 63. Assign Alternatives For Ground Part Dialog Box Fields (continued)   


|  Name         | Description                                                                                                         |
|---------------|---------------------------------------------------------------------------------------------------------------------|
|               | OTip This button is available only in the Special Symbols columns, and only when the cell is available for editing. |
| Edit button   | Makes the selected cell available for editing. Tip You can also double-click the cell to edit the contents.         |
| Add button    | Adds a new row at the bottom of the table.                                                                          |
| Delete button | Removes the selected row.                                                                                           |

**Related Topics**  

Assigning Alternate Logic Decals for Connector Symbols Special Schematic Symbols  

## Assign Alternatives for Off-Page Part Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ Open button $>$ Off-page $>$ OK button $>$ Edit Electrical button  

Use the Assign Alternatives for Off-Page Part dialog box to assign or create additional off-page reference symbols.  

Note:   
For additional information on the creation and use of special schematic symbols, see “Special Schematic Symbols” on page 167.  

![](/images/0df3b8802cdf21ef5b97b812a528e1be184a7a858fe98488264dd9cdaf7213e8.jpg)  
Figure 30. Assign Alternatives for Off-Page Part Dialog Box  

**Objects**  

Table 64. Assign Alternatives for Off-Page Part Dialog Box Fields   


|  Name           | Description                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Picture         | Displays a picture of the selected Special Symbol.                                                                              |
| Attribute table | · Special Symbol — The name of a connector pin decal for use in the schematic. · Pin Type — The function of the special symbol. |
|                 | Opens the Browse for Special Symbols Dialog Box.                                                                                |

Table 64. Assign Alternatives for Off-Page Part Dialog Box Fields (continued)   


|  Name         | Description                                                                                                         |
|---------------|---------------------------------------------------------------------------------------------------------------------|
|               | OTip This button is available only in the Special Symbols columns, and only when the cell is available for editing. |
| Edit button   | Makes the selected cell available for editing. Tip You can also double-click the cell to edit the contents.         |
| Add button    | Adds a new row at the bottom of the table.                                                                          |
| Delete button | Removes the selected row.                                                                                           |

**Related Topics**  

Assigning Alternative Symbols for the Off-Page Part Special Schematic Symbols  

## Assign Alternatives for Power Part Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ Open button $>$ Power $>$ OK button $>$ Edit Electrical button  

Use the Assign Alternatives for Power Part dialog box to assign or create additional power symbols.  

Note:   
For additional information on the creation and use of special schematic symbols, see “Special Schematic Symbols” on page 167.  

![](/images/70d0737d7e0042ef14fca9428eea617cfea4dc04c676ef93e79c4771fbc72b8e.jpg)  

**Objects**  

Figure 31. Assign Alternatives for Power Part Dialog Box   
Table 65. Assign Alternatives for Power Part Dialog Box Fields   


| Name            | Description                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Picture         | Displays a picture of the selected Special Symbol.                                                                                                                      |
| Attribute table | · Special Symbol — The name of a connector pin decal for use in the schematic. · Pin Type — The function of the special symbol. · Signal Name — The name of the signal. |
| 口               | Opens the Browse for Special Symbols Dialog Box. 0 Tip This button is available only in the Special Symbols columns, and only when the cell is available for editing.   |

Table 65. Assign Alternatives for Power Part Dialog Box Fields (continued)   


|  Name         | Description                                                                                                  |
|---------------|--------------------------------------------------------------------------------------------------------------|
| Edit button   | Makes the selected cell available for editing. OTip You can also double-click the cell to edit the contents. |
| Add button    | Adds a new row at the bottom of the table.                                                                   |
| Delete button | Removes the selected row.                                                                                    |

**Related Topics**  

Assigning Alternative Symbols for the Power Part Special Schematic Symbols  

## Assign Decal to Gate Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ Edit Electrical button $>$ Gates tab $>$ (if a new part, clic Add) $>$ double-click a CAE Decal cell $>$ Browse button  

Use the Assign Alternatives for Power Part dialog box to assign or create additional power symbols.  

![](/images/0f476e7395c56b3afe7498571d9841087b39d4ef489ef82f11ae1a1f4a44451d.jpg)  
Figure 32. Assign Decal to Gate Dialog Box  

**Objects**  

Table 66. Assign Decal to Gate Dialog Box Fields   


| Name                   | Description                                                                                                                                                                                                                                                           |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Library list           | Lists all your available libraries. Filters the Unassigned Decals list to only the selected library.                                                                                                                                                                  |
| Filter                 | Searches the chosen library (or libraries) for a specific part or item name, or names that match a wildcard or expression on page 105. Type * to view all parts or items in the chosen libraries. Click Apply to search the libraries and display the search results. |
| Preview area           | Displays the item selected in the Assigned Decals list.                                                                                                                                                                                                               |
| Unassigned Decals list | Lists all of the decals that are available to assign.                                                                                                                                                                                                                 |
| Assign New button      | Opens the Assign New Gate Decal Dialog Box.                                                                                                                                                                                                                           |
| Assign >> button       | Moves the decal from the Unassigned Decals list to the Assigned Decals list.                                                                                                                                                                                          |
| << Unassign button     | Moves the decal from the Assigned Decals list to the Unassigned Decals list.                                                                                                                                                                                          |
| Assigned Decals list   | Lists all of the decals that have been assigned.                                                                                                                                                                                                                      |

Table 66. Assign Decal to Gate Dialog Box Fields (continued)   


| Name            | Description                                                      |
|-----------------|------------------------------------------------------------------|
| Up/Down buttons | Moves the selected decal up or down in the Assigned Decals list. |

**Related Topics**  

Assigning CAE Decals to Gates  

## Assign New Gate Decal Dialog Box  

To access: File $>$ Library menu item $>$ select a Library $>$ Parts button $>$ select part $>$ New or Edit button $>$ on Part Editor Toolbar click Edit Electrical $>$ Gates tab $>$ (if new part click Add) $>$ double-click CAE Decal cell $>$ Browse button $>$ Assign New  

Use the Assign New Gate dialog box to assign a new gate decal when it doesn’t yet exist in the Library.  

![](/images/c51fdda6bbc4b59c7b9db681c1f20227203df8c6a56bacb40c5b5cba44e1483b.jpg)  
Figure 33. Assign New Gate Decal Dialog Box  

**Objects**  

Table 67. Assign New Gate Decal Dialog Box Fields   


|  Name    | Description                                                            |
|----------|------------------------------------------------------------------------|
| Text box | Enter the name of the new gate decal you intend to add to the library. |

## Assign New PCB Decal Dialog Box  

To access: File $>$ Library menu item $>$ select a Library $>$ Parts button $>$ select part $>$ New or Edit butto $>$ on Part Editor Toolbar click Edit Electrical $>$ PCB Decals tab $>$ Assign New  

Use the Assign New PCB Decal dialog box to assign a new PCB Decal when it doesn’t yet exist in the Library.  

![](/images/7f67a24380b87ff98779991bb2e0ecddff7ece4a6bac908e5b71083f1a57a333.jpg)  
Figure 34. Assign New PCB Decal Dialog Box  

**Objects**  

Table 68. Assign New PCB Decal Dialog Box Fields   


|  Name    | Description                                                           |
|----------|-----------------------------------------------------------------------|
| Text box | Enter the name of the new PCB decal you intend to add to the library. |

## Assign Shortcut Dialog Box  

To access: Tools $>$ Customize menu item $>$ Keyboard and Mouse tab $>$ select a mode $>$ select a command folder $>$ select a command $>$ New button  

Create a new shortcut key using the Assign Shortcut dialog box.  

![](/images/1714cb783ae5b8a2c3edca31291c8ca3ca03d3fc3187a9c54712df51a86c3c07.jpg)  
Figure 35. Assign Shortcut Dialog Box  

**Objects**  

Table 69. Assign Shortcut Dialog Box Fields   


|  Name                  | Description                                                 |
|------------------------|-------------------------------------------------------------|
| Press new shortcut key | Type the shortcut you want to use.                          |
| Select a pointer event | Set a pointer event shortcut                                |
| Similar shortcuts list | Lists the shortcut keys already assigned to other commands. |

## Attribute Properties Dialog Box  

To access: Select a part attribute label $>$ right-click $>$ Properties menu item  

Use the Attribute Properties dialog box to provide text and font settings for one or more part attribute labels.  

![](/images/1295b792a15ff7406cae3a18e8ca8172f71facd0b0f741503145f693e01750f5.jpg)  
Figure 36. Attribute Properties Dialog Box  

**Objects**  

Table 70. Attribute Properties Dialog Box Fields   


|  Name    | Description                                                                                                                                                                                                                             |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name     | The name of the selected attribute.                                                                                                                                                                                                     |
| Value    | Specifies the label you want in the schematic.                                                                                                                                                                                          |
| Rotation | Specifies the rotation of the label: O or 90 degrees.                                                                                                                                                                                   |
| Size     | Specifies the size of the font. Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke fonts. The 'size refers to the height of the tallest characters. |

Table 70. Attribute Properties Dialog Box Fields (continued)   


|  Name                             | Description                                                                                                                                                                                                                                                                                                          |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                   | tGg Stroke Font - Size                                                                                                                                                                                                                                                                                               |
| Line Width                        | Specifies the line width for stroke fonts only. text Stroke Line Width                                                                                                                                                                                                                                               |
| Font list                         | The fonts available to you. This lists either stroke fonts or system fonts. You choose which type of font to use in the Fonts Dialog Box. 1  Tip · Select stroke font or a system font. · For system fonts, you can also click a font style button, or any combination of styles: B for bold, I for italic, or U for |
| Horizontal/Vertical Justification | underlined. Specifies the horizontal (Right, Center, Left) justification and the vertical (Up, Center, Down) justification of the text.                                                                                                                                                                              |

**Related Topics**  

Modifying Part Attribute Labels  

## Auto Renumber Parts Dialog Box

To access: Schematic Editing toolbar $>$ Auto Renumber Parts button  

Automatically renumber the reference designators on schematic sheets in a pattern. Choose the sheets, reference designator prefixes, pattern and numbering range.  

![](/images/7ecc5e42dab43b0b57e3cd0d37089d381fad3821fbd4c963955f59adf37eff24.jpg)  

**Objects**  

|  Name   | Description                                                                                                            |
|---------|------------------------------------------------------------------------------------------------------------------------|
|  Sheets | Choose which sheets to renumber.                                                                                       |
|         | Hierarchical sheets appear differently depending on whether they have been created from the top down or the bottom up. |

SailWind Logic GUI Reference Basic Script Editor   


|  Name       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|             | · Bottom-up — Sheets display at the primary level instead of being indented in the list. When using Increment Start Value by Sheet, the reference designators are renumbered on each sheet. · Top-down — Sheets are indented to show they are sub-sheets. When using Increment Start Value by Sheet, the sheets inherit the same base level number as the parent sheet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Prefix List | Choose which reference designator families to renumber. The list displays the total number of reference designators in brackets. The prefix types and totals update based on the sheets selected in the Sheets list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Cell size   | Renumbering is applied according to the Precedence pattern within the cell area. Specify the size of cells in which to apply the renumbering pattern. Cells are arranged across the schematic area in selected Precedence pattern. For an illustration explaining cell size, see “Automatically Renumbering Reference Designators" on page 280.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Renumber    | · Start Value — The number to apply to the first of each type of renumbered reference designator. · Increment — The gap in numbers to apply to the reference designator numbers. · Increment Start Value by Sheet —— Use the sheet number as the start number - the sheet number as shown in the Sheets Dialog Box and not the order of the sheet in this dialog. For example, if the Start Value is 101, then sheet number 1 will start with number 101, but sheet 2 will start with number 201. If used in combination with large start values, the reference designator numbers may quickly run into the software limit. For example, if the start value is set to 10oO, and there are 40 schematic sheets, then reference designators on sheet 40 would start at 40,000 - well over the limit of 32,766. Start value and increment are applied to each reference designator family separately. For example, the schematic has the following components: C1, C2, C3, R1, R2. Start Value is 10 and Increment is 5. The result of renumbering is: C10, C15, C20, R10, R15.Parts on sheets are renumbered in the order of the sheets: first, parts from sheet number 1, then from sheet number 2 and so on. If a part belongs to more than one |
| Precedence  | sheet, it gets renumbered on the selected sheet with the lowest number. Specifies the pattern used to renumber parts within a cell area. Also specifies the pattern used for the application of cells to process over the schematic page. Renumbering is performed based upon the first pin of the symbol encountered in the given precedence direction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

**Basic Script Editor**

Basic is a simple scripting language. Like many Windows applications, such as Microsoft Word and Excel, SailWind applications include Basic capabilities to enable users to customize their applications using a standard scripting language.  

You can use the Basic Script Editor to create, edit, run, and troubleshoot Basic scripts from SailWind applications. To open the editor:  

• Tools $>$ Basic Scripts $>$ Basic Script Editor menu item

![](/images/1209b26dfde43c3579cbb23acb54683a7ad688d635b585a3c7e9bf9c4030a951.jpg)  
Figure 37. Basic Script Editor  

## Basic Scripts Dialog Box

To access: Tools $>$ Basic Scripts $>$ Basic Scripts menu item  

The Basic Scripts dialog box provides easy access to your Basic scripts.  

![](/images/2afe961a3cea7985c4cefb6983ced2b736da0a3ec933abfba28cf650b7310e23.jpg)  
Figure 38. Basic Scripts Dialog Box  

**Objects**  

Table 71. Basic Scripts Dialog Box Fields   


| Name                                                                                                                                                                             | Description                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basic Script List                                                                                                                                                                | Lists the scripts available to you.                                                                                                                        |
| X button                                                                                                                                                                         | Specifies to use the smaller dialog box vs. the entire dialog box. To use_the smaller dialog box, select the script you want to run and press Enter. O Tip |
| In Menu                                                                                                                                                                          | Specifies to add the selected script to the Basic Scripts menu.                                                                                            |
| Run button                                                                                                                                                                       | Runs the selected script. Restriction:                                                                                                                     |
| You can not run multiple scripts at the same time. Tip If the selected script has an error during compilation, it automatically opens in the Basic Script editor for correction. |
| Edit button                                                                                                                                                                      | Opens the Sax Basic Engine dialog box with the selected script loaded. See also Managing the Sax Basic Engine on page 389                                  |

Table 71. Basic Scripts Dialog Box Fields (continued)   


| Name             | Description                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Load File button | Adds a new script to the list. Tip · You can load up to 32,767 scripts. Scripts are not compiled when they are loaded; they are compiled when you run them • The list of scripts you load into this dialog box is saved in the |
| Unload button    | Scripts dialog box. Removes the selected script from the list.                                                                                                                                                                 |
| Description area | Displays the location of the selected script.                                                                                                                                                                                  |

**Related Topics**  

Using the Basic Scripts Dialog Box  

## Bill of Materials Setup Dialog Box  

The Bill of Materials report produces a user-configurable list of the parts contained in the current schematic. You can direct any part attribute in the schematic to a Bill of Materials report.  

Restriction:   
Including non-ECO-registered parts and non-electrical parts in the bill of materials is constrained. See Options Dialog Box, Design Category for details.  

To access: File $>$ Reports menu item $>$ Setup button  

Bill of Materials Setup Dialog Box, Attributes Tab Bill of Materials Setup Dialog Box, BOM Config Tab Bill of Materials Setup Dialog Box, Format Tab  

### Bill of Materials Setup Dialog Box, Attributes Tab

To access: File $>$ Reports menu item $>$ Setup button $>$ Attributes tab  

Use the Attributes tab to modify the Attribute content, the corresponding column headings, and column width of the report. The attribute order in the content list determines the column arrangement in the BOM report. There is a limit of 12 attributes in the Bill of Materials report.  

![](/images/fa055dd389384b12f366a4b65429e080e0db4ec70714e6a184ef676517d3cf33.jpg)  
Figure 39. Attributes tab  

**Objects**  

Table 72. Bill of Materials Setup Dialog Box Fields   


|  Name                                                                                                                      | Description                                                             |
|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Attribute table                                                                                                            | Specifies the attributes in, headings for, and width of the BOM report. |
| · Part Attribute column — Specifies the attributes you want in the report. You can list up to twelve attribute names. Each |
| attribute defines a column in the report. · Field Header column — Specifies the column heading for                         |
| each attribute in the report. You can specify any character except the colon (: ).                                         |
| · Width column —— Specifies the number of characters across the column for each attribute in the report: 1 to 200.         |

Table 72. Bill of Materials Setup Dialog Box Fields (continued)   


|  Name         |  Description                                                                                                                                           |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Up button     | Moves the selected row up by one. O Tip                                                                                                                |
| Down button   | arrangement in the BOM report. Moves the selected row down by one. Tip The attribute order in the content list determines the column                   |
| Add button    | Adds a row to the bottom of the table where you can select a new part attribute. Tip You can list up to twelve attribute names. Each attribute defines |
| Edit button   | Makes the selected box editable. Restriction: You cannot edit the part attribute name, but you can select a                                            |
| Remove button | new attribute to replace the one currently listed. Removes the selected row from the table and therefore the                                           |
| Reset button  | attribute from the report. Restores the default content from the .ini file.                                                                            |

**Related Topics**  

The Bill of Materials Report  

### Bill of Materials Setup Dialog Box, BOM Config Tab

To access: File $>$ Reports menu item $>$ Setup button $>$ BOM Config tab  

Use the BOM Config tab to preview the Bill of Materials report format and copy any selected lines of the file to a Windows clipboard. You can also specify rows to export to a TXT/CSV file. The default view orders the attributes by the sort field you specified on the Format tab.  

![](/images/3778d729a6c838398db7fb7e3dc41ba95508dff46c7ec44ce79be915524f3c56.jpg)  

**Objects**  

Figure 40. BOM Config Tab  
Table 73. Bill of Materials Setup Dialog Box-BOM Config Fields  


|  Name                    |  Description                                                                                                                                                                              |  Remark                        |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| Report table             | Displays the BOM report in table format for you to select and copy any row or export to a CSV/TXT file. This table shows the data from the attributes you selected on the Attributes tab. |                                |
| Select All button        |  Selects all rows in the table.                                                                                                                                                           | Use these func selected rows t |
| Copy button              | Specifies to copy the row(s) you've selected to the Windows clipboard.                                                                                                                    |
| Include table header     | Specifies to copy the table header in addition to the row(s) you've selected.                                                                                                             |
| Export button            | Exports the BOM report to a CSV/TXT file. You can exclude the row(s) you don't want by checking the NC checkbox.                                                                          | Use these func allowable rows  |
| Combine Reference button | Specifies to include reference designators sharing identical Part Name in the same cell.                                                                                                  |

Table 73. Bill of Materials Setup Dialog Box-BOM Config Fields (continued)   


|  Name           | Description                                                    | Remark |
|-----------------|----------------------------------------------------------------|--------|
| Clear NC button | Specifies to clear all the NC checkboxes selected in the table |        |

**Related Topics**  

The Bill of Materials Report  

### Bill of Materials Setup Dialog Box, Format Tab

To access: File $>$ Reports menu item $>$ Setup button $>$ Format tab  

Use the Format tab to modify the output format of the Bill of Material report. The default settings originate from the .ini file.  

![](/images/e7155db286912304ec5a17f6bb42992498d3b09685d94eb3c30cf2d652226951.jpg)  

**Objects**  

Table 74. Bill of Materials Setup Dialog Box-Format Tab Fields   


|  Name          | Description                                                                                             |
|----------------|---------------------------------------------------------------------------------------------------------|
| Delimiter area | Specifies the type of delimiter you want to distinguish the report columns. · None — no delimiter used. |

Table 74. Bill of Materials Setup Dialog Box-Format Tab Fields (continued)   


| Name Description                |
|---------------------------------|
|                                 | · Comma — places a comma character between report fields. · Custom — specify any character as a delimiter.                                                                                                                                                  |
| File Format list                |  Specifies the output file format.                                                                                                                                                                                                                          |
| Reset button                    | Restores the default content from the .ini file.                                                                                                                                                                                                            |
| Settings list                   |  Specifies to use a previously saved report format setting.                                                                                                                                                                                                 |
| Save As button                  | Saves report format settings for the current design to a specified file so you can create different format configurations for different                                                                                                                     |
| Delete button                   | designs Removes the selected setting in the Settings list.                                                                                                                                                                                                  |
| Format Options area             |
| Report Title                    |  Specifies the title of the report.                                                                                                                                                                                                                         |
| Combine Value/Tolerance         | Specifies to combine the Value and Tolerance attributes of a part in the part name. Example: The 1/4 watt resistor would have a part type name of                                                                                                           |
| Ref. Designator Separation Mode | R1/4W or R1/4W.4.7K,+/-5%. SailWind Logic evaluates parts that have either a different Value or Tolerance attribute as different part types. · Single Ref. Designator per line — Although some components are identical, display each component instance on |
|                                 | a new line. This increases the BOM report size. · Multiple Ref. Designator per line — Combines identical component instances on one line and lists all reference designators based on the settings below: · Compress Ranges — Displays ranges of components |
|                                 | with a dash between min and max value. For example, if components C1, C2, C3, and C4 are identical, they are displayed as C1-4. This can shorten the list of reference designators listed for a component type.                                             |
|                                 | If you clear this check box, ranges are not compressed and individual reference designators are listed for the line entry. For example, C1,C2,C3,C4. · Ref designator Delimiter — Specify a single character                                                |
|                                 | to place between multiple reference designators. For example, use a comma for "C1,C2,C3", or use an asterisk for "C1*C2*C3". Although you can type multiple characters in this box, only the first character applies.                                       |
| Sort By list                    | Specifies the attribute in which to sort the report list. Tip                                                                                                                                                                                               |

**Related Topics**  

The Bill of Materials Report  

## Browse for Connectors Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ Open button $>$ select Connector $>$ OK button  

Use the Browse for Connectors dialog box to browse a library and select a connector for editing from the library (or libraries) specified in the Library list.  

![](/images/4c083170c630b6ad01140ce27251047c2acbae8e523385ddffe19d80130682d7.jpg)  
Figure 41. Browse for Connectors Dialog Box  

**Objects**  

Table 75. Browse for Connectors Dialog Box Fields   


|  Name        | Description                                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------------------|
| Preview area | Shows the selected part.                                                                                              |
| Part Types   | Lists the items in the selected library. The number of objects that appear depends on the filter settings.            |
| Library list | Specifies the library you want to use.                                                                                |
| Items        | Narrows the search. You can use wildcards or expressions on page 105. An asterisk (*) displays all parts in the list. |
| Apply button | Searches the library for the specified item.                                                                          |

**Related Topics**  

Browsing for Connectors

## Browse for Special Symbols Dialog Box

To access: Tools $>$ Part Editor menu item $>$ open an off-page part $>$ Edit Electrical button $>$ double-click in a field in the Special Symbols column $>$ Browse button  

Use the Browse For Special Symbols dialog box to access the library for decals you want to specify as Special Symbols. Special Symbols are those used to create off-page reference, power and ground symbols, and connectors.  

![](/images/93bf18165a6fc0745aba3542a1038d5fa47bb2ac43149b6bf8d50b0bf120770d.jpg)  
Figure 42. Browse for Special Symbols Dialog Box  

**Objects**  

Table 76. Browse for Special Symbols Dialog Box Fields   


|  Name        | Description                                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------------------|
| Preview area | Shows the selected item.                                                                                              |
| Gate Decals  | Lists the items in the selected library. The number of objects that appear depends on the filter settings.            |
| Library list | Specifies the library you want to use.                                                                                |
| Items        | Narrows the search. You can use wildcards or expressions on page 105. An asterisk (*) displays all parts in the list. |
| Apply button | Searches the library for the specified item.                                                                          |

**Related Topics**  

Assigning Alternative Symbols for the Ground Part Assigning Alternative Symbols for the Off-Page Part  

## Browse Library Attributes Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ Edit Electrical button $>$ Attributes tab $>$ Browse Lib. Attr button  

Use the Browse Library Attributes dialog box to browse and list all attribute names from libraries specifie in the Library List dialog box.  

![](/images/8e871c4c6dbb6954b8235f6e81ae9221c4b0302f123b9a4466523caa0cdb5fae.jpg)  
Figure 43. Browse Library Attributes Dialog Box  

**Objects**  

Table 77. Browse Library Attributes Dialog Box Fields   


|  Name          | Description                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
| Attribute      | Displays the selected attribute.                                                                |
| Group          | Filters the attribute list. (Includes structured attributes.)                                   |
| Refresh button | Manually updates the attribute list if you change the list of libraries in the Library Manager. |

**Related Topics**  

Browsing Library Attributes  

## Bus Name Properties Dialog Box  

To access: Select a bus name label $>$ right-click $>$ Properties menu item  

Use the Bus Name Properties dialog box to provide or change text and font settings for one or more bus name labels.  

![](/images/3006b9d56f8402f4a1649b454b3e0c31e2d80baf1c9bf0410b64d9f24a9e2eb7.jpg)  
Figure 44. Bus Name Properties Dialog Box  

**Objects**  

Table 78. Bus Name Properties Dialog Box FIelds   


|  Name      | Description                                                                                                                                                                                                                            |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name       | The name of the selected bus.                                                                                                                                                                                                          |
| Bus button | Opens the Bus Properties Dialog Box.                                                                                                                                                                                                   |
| Rotation   | Specifies the rotation of the label: O or 90 degrees.                                                                                                                                                                                  |
| Size       | Specifies the size of the font. Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke fonts. The size refers to the height of the tallest characters. |

Table 78. Bus Name Properties Dialog Box FIelds (continued)   


| Name                              | Description                                                                                                                                                                                         |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                   | Gg Stroke Font - Size                                                                                                                                                                               |
| Line Width                        | Specifies the line width for stroke fonts only. text Stroke Line Width                                                                                                                              |
| Font list                         | The fonts available to you. Tip · Select stroke font or a system font. · For system fonts, you can also click a font style button, or any combination of styles: B for bold, I for italic, or U for |
| Font Style                        | Enables you to change the font style to bold, italic, and underlined. Restriction: System fonts only.                                                                                               |
| Horizontal/Vertical Justification | Specifies the horizontal (Right, Center, Left) justification and the vertical (Up, Center, Down) justification of the text.                                                                         |

**Related Topics**  

Modifying Bus Name Labels  

## Bus Properties Dialog Box  

To access: Select a bus $>$ right-click $>$ Properties menu item  

Use the Bus Properties dialog box to change the name of the bus, change the bus type, and manage bus nets.  

![](/images/f1a6d30141ffd828329d7478d64766087ecdb33111962ec44030b6fbbeedc6a1.jpg)  
Figure 45. Bus Properties Dialog Box  

**Objects**  

Table 79. Bus Properties Dialog Box Fields   


| Name               | Description                                                                                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Bus Name           | Specifies the name of the bus. Select or type the name you want.                                                                          |
| Rename area        | Specifies to rename this instance or all instances of the bus.                                                                            |
| Bus Type area      | Specifies which bus names appear in the Bus Name list.                                                                                    |
| Add Bus Name Label | Select the Add Bus Name Label check box to add the bus name as a label to the bus at the end of the bus closest to where you selected it. |

Table 79. Bus Properties Dialog Box Fields (continued)   


|  Name                                                                                                             | Description                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                   | Tip ·A bus can have two labels, one on each end.                                                                                           |
| · The check box is unavailable when the end of the selected bus has a label.                                      |
| ·A bus label is not required. ·To delete a bus label, select the label in the schematic and                       |
| click the Delete button on the standard toolbar.                                                                  |
| Bus Nets table                                                                                                    | Lists the name or prefix of the bus net, the starting bit number for a sequence of nets, and the ending bit number for a sequence of nets. |
| Restriction: Available only if the bus is a mixed net bus.                                                        |
| Tip                                                                                                               |
| · For a single net, type the net name. ·For a range of sequential nets, type the prefix for the sequence of nets. |
| Add button                                                                                                        | Adds a row to the Bus Nets table.                                                                                                          |
| Restriction: Available only if the bus is a mixed net bus.                                                        |
| Edit button                                                                                                       | Makes the selected row available for editing.                                                                                              |
| Restriction: Available only if the bus is a mixed net bus.                                                        |
| Delete button                                                                                                     | Removes the selected row from the Bus Nets table.                                                                                          |
| Restriction: Available only if the bus is a mixed net bus.                                                        |
| Down/Up buttons                                                                                                   | Moves the selected row up or down in the Bus Nets table.                                                                                   |
| Restriction:                                                                                                      |

Related Topics Managing Buses  

## CAE Decal Wizard Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ New button $>$ CAE Decal $>$ OK button $>$ Decal Editing Toolbar button $>$ CAE Decal Wizard button  

Use the Decal Wizard dialog box to automatically create a new CAE decal. You must be in the Decal Editor mode of the Part Editor, and creating gate information, to use this feature.  

![](/images/25ae100b7acc03fdbc008ab39ae27efa7e1e0de57eaf6e54bcc9c73ae77c36bb.jpg)  
Figure 46. CAE Decal Wizard Dialog Box  

**Objects**  

Table 80. CAE Decal Wizard Dialog Box contents   


|  Name                                                                                                                           | Description                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Preview area                                                                                                                    | Displays what the CAE decal looks like based on your settings.                                                                                                                                              |
| Pin Length area                                                                                                                 | Sets the horizontal and vertical distance from the terminal connection point to the decal outline.                                                                                                          |
| Pin Spacing area                                                                                                                | Sets the horizontal and vertical distance between pins.                                                                                                                                                     |
| Box Parameters area                                                                                                             | Sets the width and height of the decal outline.                                                                                                                                                             |
| Tip                                                                                                                             |
| · Pin decals are moved left or right to accommodate the box width. · If you enter a value larger than needed to accommodate the |
| number of input or output pins, space is added to the bottom of the decal.                                                      |
| Left Pins area                                                                                                                  | Specifies the pin decal and pin count for the left, or input, side of the part. · Pin Decal — Specifies the pin decal to use for this side. · Pin Count — Specifies the number of pins to use on this side. |
| Right Pins area                                                                                                                 | Specifies the pin decal and pin count for the right, or output, side of the part.                                                                                                                           |

Table 80. CAE Decal Wizard Dialog Box contents (continued)   


|  Name           | Description                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                 | · Pin Decal — Specifies the pin decal to use for this side. · Pin Count — Specifies the number of pins to use on this side.                                                                       |
| Upper Pins area | Specifies the pin decal and pin count for the upper side of the part. · Pin Decal - Specifies the pin decal to use for this side. · Pin Count — Specifies the number of pins to use on this side. |
| Lower Pins area | Specifies the pin decal and pin count for the lower side of the part. · Pin Decal - Specifies the pin decal to use for this side. · Pin Count — Specifies the number of pins to use on this side. |

**Related Topics**  

Using the Decal Wizard  

## Capture a New View Dialog Box  

To access: View $>$ Save View menu item $>$ Capture button  

Use the Capture a New View dialog box to name the view you want to save.  

![](/images/8162f8d8ef29457749f5f1809b004466f719c4cecbf0314ee93841c549081689.jpg)  
Figure 47. Capture a New View Dialog Box  

**Objects**  

Table 81. Capture a New View Dialog Box contents   


| Name | Description                                                                                                |
|------|------------------------------------------------------------------------------------------------------------|
| Name | Specifies the name you want for the view. View n is the default name where n is the next number available. |
|      | i Tip You can create up to nine views. The view names appear at the bottom of the View menu.               |

**Related Topics**  

Saving and Restoring Views  

## Change Part Type Dialog Box  

To access: Select a part $>$ right-click $>$ Properties $>$ Change Type button  

Use the Change Part Type dialog box to change the selected part to a new part type. The new part type can be one that already exists in the schematic or in the parts library. If multiple parts are selected, all of the selected parts are changed.  

![](/images/61541c9e3853cc6609dec0ac3cfe159f3d61bf3c4d368830b7d20203fe482cb0.jpg)  
Figure 48. Change Part Type Dialog Box  

**Objects**  

Table 82. Change Part Type Dialog Box Contents   


|  Name                                                | Description                                                                                      |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Picture area                                         | Displays the part selected in the Part Types list.                                               |
| Part Types list                                      | Lists all of the part types according to the filter settings.                                    |
| Update attributes common to design and library       | Updates parts having common attributes with the attribute values contained in the new part.      |
| Preserve attributes in design not present in library | Retains attributes that exist in the current part even though they do not exist in the new part. |

Table 82. Change Part Type Dialog Box Contents (continued)   


| Name         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              | Sets how parts are updated in the Apply update to area: · This Gate — Only updates the selected gate. · Selected Gates — Only updates the selected gates. Restriction: Available only when multiple parts are selected. · This Part — Only updates a part or all associated gates of a part. · Selected Parts —— Only updates a part or all associated gates of the selected parts. Restriction: Available only when multiple parts are selected. · All Parts This Type — Updates all matching gates and/or parts in the design. |
|              | Unavailable when multiple parts are selected. Tip · You can update the part definition in the schematic with a modified version in the library. Select the same part name, then click All Parts This Type in the Apply Update to Area. · If you change a part type to one with fewer pins, the                                                                                                                                                                                                                                   |
| Library list | connections going to the missing pins are not deleted. They are attached to automatically generated off-page symbols. You are notified of all disconnected pins.                                                                                                                                                                                                                                                                                                                                                                 |
| Items        | Specifies the library you want to use. Narrows the search. You can use wildcards or expressions on                                                                                                                                                                                                                                                                                                                                                                                                                               |
|              | page 105. An asterisk (*) displays all parts in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

**Related Topics**  

Modifying Parts  

## Check for Updates Dialog Box  

To access: Help $>$ Check for Updates menu item  

Use the Check for Updates dialog box to manually check for a new version of SailWind, and to disable or enable automatic checks.  

![](/images/07ef74cd5d754ca563a40b6cf26d2ad4c2e6ab1ecd57f818fd53d0ae04e28fc3.jpg)  
Figure 49. Check for Updates Dialog Box  

**Objects**  

Table 83. Check for Updates Dialog Box contents   


| Name                                                                                                                                                                  | Description                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Check for Updates button                                                                                                                                              | Manually checks for a new version of the SailWind software.                    |
| Disable“Check for Updates" functionality                                                                                                                              | Determines if SailWind automatically checks for a new version of the software. |
| Click to stop SailWind from automatically checking for a new version of the SailWind products; click to clear to have SailWind automatically check for a new version. |

**Related Topics**  

SailWind Updates  

## Class Rules Dialog Box  

To access: Setup $>$ Design Rules menu item $>$ Class button  

Use the Class Rules dialog box to define rules that apply to a collection of nets known as a net class and to multiple net classes.  

![](/images/198fc690ec87860d6e16039ab8abe373b30ecbab2bbd44b203a09c05c6945f37.jpg)  
Figure 50. Class Rules Dialog Box  

**Objects**  

Table 84. Class Rules Dialog Box Contents   


| Name                                                                                            | Description                                                                                       |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Class Name                                                                                      | Specifies the class name for which you want to apply rules.                                       |
| Class list                                                                                      | Defines net classes by name and parenthetically notes the rules that apply, if any, to the class. |
| Show Classes with Rules                                                                         | Specifies to list only classes with at least one set of rule definitions.                         |
| Add button                                                                                      | Adds a new Class Name to the Class list.                                                          |
| Delete button                                                                                   | Removes the selected Class Name from the Class list.                                              |
| Rename button                                                                                   | Renames the selected Class Name in the Class list.                                                |
| Tip Select the name in the list, type the new name in the Class Name box and then click Rename. |

Table 84. Class Rules Dialog Box Contents (continued)   


| Name             | Description                                                                         |
|------------------|-------------------------------------------------------------------------------------|
| Clearance button | Opens the Clearance Rules Dialog Box.                                               |
| Routing button   | Opens the Routing Rules Dialog Box.                                                 |
| Hi Speed button  | Opens the HiSpeed Rules Dialog Box.                                                 |
| Report button    | Opens the Rules Report Dialog Box.                                                  |
| Available list   | Lists all of the available nets for this Class.                                     |
| Add>> button     | Moves the net from the Available list to the Selected list.                         |
| <<Remove button  | Moves the net from the Selected list to the Available list.                         |
| Selected list    | Lists all of the selected nets for this Class.                                      |
| Default button   | Removes non-default rules from the selected nets, so that only default rules apply. |

## Clearance Rules Dialog Box  

To access: Setup $>$ Design Rules menu item $>$ a rule hierarchy button $>$ Clearance button  

Use the Clearance Rules dialog box to define the spacing permitted between objects. When objects are imported, the On-line DRC and Verify Design programs use these rules to check and report clearance violations.  

![](/images/f896c1069f08cb95bf78aa0ba7fdf990cf08abcfa5d2af5aa76a49a48075b3d2.jpg)  
Figure 51. Clearance Rules Dialog Box  

**Objects**  

Table 85. Clearance Rules Dialog Box contents   


| Name             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Same Net area    | Defines edge-to-edge clearance values between items that are in the same net. Tip · To define the minimum spacing between any two objects, type the value in the corresponding text box. · To define the same spacing value for all text boxes in one matrix column, press the button above the column. Type a value and click OK. · To define the same spacing value for all text boxes in one matrix row, press the button in the left column. Type a value and click OK. · To define the same spacing value for all text boxes in the matrix, press the All button. Type a value and click OK. See also Same NetMatrix |
| Trace Width area | Specifies to restrict the trace width to a range of values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

Table 85. Clearance Rules Dialog Box contents (continued)   


| Name           | Description                                                                                                                                                                                                                                                                                                                                                        |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                | Tip · In the Recommended box, type the width you want to assign to the trace when routing begins. · In the Minimum and Maximum boxes, values are respected                                                                                                                                                                                                         |
| Clearance area | Defines edge-to-edge clearances between two object types: · To define the minimum spacing between any two objects, type the value in the appropriate text box. • To define the same spacing value for all text boxes in one matrix column, press the button above the column and type a value. · To define the same spacing value for all text boxes in one matrix |
| Other area     | Specifies other optional clearance values. · Drill to Drill — The minimum edge-to-edge spacing between two drill holes. · Body to Body — The minimum edge-to-edge spacing between two                                                                                                                                                                              |
| Delete button  | Removes this set of Clearance rules from your rules hierarchy. Tip You cannot delete the Default Clearance rules.                                                                                                                                                                                                                                                  |

**Related Topics**  

Setting Up Clearance Rules  

## Compare/ECO Tools Dialog Box  

When you compare two versions of a design, you can create an output file that lists the differences between the two versions. The report file is named Logic.rep and is written to the \SailWind Projects folder.  

![](/images/79f69c174dc07ea423c67fe75aec4c3d51887f0edb67c963b3a74927594bd2f5.jpg)  

Restriction:   
Transferring non-ECO-registered parts and non-electrical parts is constrained. See Options Dialog Box, Design Category for details.  

To access: Tools $>$ Compare/ECO menu item

Compare/ECO Tools Dialog Box, Documents Tab Compare/ECO Tools Dialog Box, Comparison Tab  

### Compare/ECO Tools Dialog Box, Documents Tab

To access: Tools $>$ Compare/ECO menu item $>$ Documents tab  

Use the Documents tab to specify the design netlists to compare and the files to create.  

![](/images/103a6c417d3bd063a4dba947e09bd153541b965832cf74655a2cd89da07f8507.jpg)  

!Tip  

You can compare designs in any of the following forms:  

• Schematic in memory • Binary schematic file (.sch) • PADS-format ASCII file (.asc)  

Restriction:   
Transferring non-ECO-registered parts and non-electrical parts is constrained. See Options Dialog Box, Design Category for details.  

![](/images/0a00a694ac2e8eee140b03e14585676b09e08e6d2b4e19ea9e4b9824439e9a9d.jpg)  
Figure 52. Compare/ECO Tools Dialog Box, Documents Tab  

**Objects**  

Table 86. Compare/ECO Tools Dialog Box, Documents Tab Contents   


|  Name                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Original Schematic Design to Compare                                                                                                                                                                                 | Specify the design you want to update. Do one of the following: · Select Use Current Schematic Design to use the schematic in memory as the original design. · Clear Use Current Schematic Design, and then type or browse                            |
| to the original design file. The original design file format can be binary (.sch) or PADS-format ASCll (.asc) output from the schematic or layout. Restriction:                                                      |
| New Current Schematic Design                                                                                                                                                                                         | design. Specify the design containing the changes you want to place into the original design. Do one of the following: · Select Use Current Schematic Design to use the schematic in memory as the new design.                                        |
| · Clear Use Current Schematic Design, and then type or browse to the new design file. The new design file format can be binary (.sch) or PADS-format ASCll (.asc) output from the schematic) or layout. Restriction: |
|                                                                                                                                                                                                                      |
| Generate ECO File                                                                                                                                                                                                    | Logic.rep and is stored in the ISailWind Projects folder. Specifies to create an ECO file. Type or browse to the ECO file. The ECO file contains ECO commands that describe the changes needed to update the original design to match the new design. |

**Related Topics**  

Forward Annotation From SailWind Logic to SailWind Layout Backward Annotation From SailWind Layout to SailWind Logic Contents of the Differences Report  

### Compare/ECO Tools Dialog Box, Comparison Tab

To access: Tools $>$ Compare/ECO menu item $>$ Comparison tab  

Use the Comparison tab to specify the design elements to include in the design netlists comparison.  

Restriction:   
Transferring non-ECO-registered parts and non-electrical parts is constrained. See Options Dialog Box, Design Category for details.  

![](/images/c485144f2ad08d9134df143e0509c44d3e62572c3417169af13f0d6fa1199eec.jpg)  
Figure 53. Compare/ECO Tools Dialog Box, Comparison Tab  

**Objects**  

Table 87. Compare/ECO Tools Dialog Box, Comparison Tab Contents   


|  Name                   |  Description                                                                                                                  |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Comparison Options area |                                                                                                                               |
| Compare Part Attributes | Comparison includes part attributes. Only part attributes are compared and updated or reported. Each part receives attributes |

Table 87. Compare/ECO Tools Dialog Box, Comparison Tab Contents (continued)   


|  Name                                                                                                                             |  Description                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                   | from its corresponding Decal and Part Type, but modification is performed only at the part level. SailWind Logic categorizes parts that have different attributes as different part types. Therefore, if you select Include Part Atributes                              |
| Compare Net Attributes                                                                                                            | and reports errors. Comparison includes net attributes. SailWind Logic categorizes nets that have different attributes as different nets. Therefore, if you select Include Net Attributes                                                                               |
| Compare PCB Decal Assignments                                                                                                     | Attributes when you perform an ECO comparison of that netlist. Otherwise the comparison considers the net types to be different and reports errors.                                                                                                                     |
| Compare Design Rules                                                                                                              | Comparison includes PCB decal assignments. Comparison includes design rules. Only Default, Net, and Net                                                                                                                                                                 |
|                                                                                                                                   | Class rules are compared. Rules on other objects in the original design are preserved where possible.                                                                                                                                                                   |
|  Name Comparison Options area                                                                                                     |
| Compare Net Names and Reference Designators. Rename as Necessary                                                                  | Compare differences using reference designators and net names. Best used to minimize changes to routed traces. Selecting this option may result in the positional swapping of parts.                                                                                    |
| Compare Net Names and Reference Designators. Prefer to Add or Delete Parts Instead of Renaming                                    | Compare differences using reference designators and net names on the basis that few reference designators have been renamed and nets have not been renamed. Best used to minimize the positional swapping of parts, and the design disruption that may result.          |
| Compare Connectivity and Topology (not names). Rename as necessary.                                                               | Compare differences without using reference designators or net names. Compare differences using pin names, part type names, and so on. Best used to compare designs when parts and nets have been                                                                       |
| Unused Pins Net Name area                                                                                                         |
| Ignore the Unused Pins Net                                                                                                        | Select the check box and type the name of the unused pins net if you want the design comparison to exclude the unused pins net in the original design. The unused pins net contains pins that have no logical net association. An unused pins net may be created in the |
|                                                                                                                                   | PCB design process.                                                                                                                                                                                                                                                     |
| Restriction: Specify a net name of 47 characters or less. Use any alphanumeric characters except curly braces {}. asterisks *, or |

Table 87. Compare/ECO Tools Dialog Box, Comparison Tab Contents (continued)   


|  Name |                                                                                                                     |
|-------|---------------------------------------------------------------------------------------------------------------------|
|       | Tip If you clear this option and you update the PCB layout from SailWind Logic, the unused pins net may be deleted. |

**Related Topics**  

Forward Annotation From SailWind Logic to SailWind Layout Backward Annotation From SailWind Layout to SailWind Logic Contents of the Differences Report  

## Conditional Rule Setup Dialog Box  

To access: Setup $>$ Design Rules menu item $>$ Conditional Rules button  

Once you set up Clearance rules for a group in the hierarchical order, the rules are applied to all other objects. Use the Conditional Rule Setup dialog box to apply a third overriding set of rules that apply only when the item meets other specific levels of the hierarchical order.  

![](/images/55c16c0fec5786478af9b2727924b3220644d3d6e092888e0aa045aa225f667e.jpg)  

!Tip  

When setting up conditional rules, observe the following:  

• You can use a layer as an against object, where rules you set for an object such as a net apply   
only when the net is routed on that layer.   
• You can further refine this to use another net as an against object and specify a layer to which the rules to apply. If these two nets meet on this layer, they must adhere to this clearance. You define these relationships by making conditional rule sets.  

![](/images/48ad5b938e6b848e006ff288000d1263d40a0ab3c8454d382a7e4a916741457e.jpg)  
Figure 54. Conditional Rule Setup Dialog Box  

**Objects**  

Table 88. Conditional Rule Setup Dialog Box Contents   


| Name                       | Description                                                                                                                                                                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Source Rule Object area    | Specifies the object you want to use to check rules. Choose Classes, Nets, or All.                                                                                                                                                                    |
| Against Rule Object area   | Specifies which object to use to check the rules against. Choose Layer, Classes, or Nets.                                                                                                                                                             |
| Apply to Layer list        | Specifies the layer on which you want the rules to be checked.                                                                                                                                                                                        |
| Existing Rule Sets list    | Lists rule sets that have already been created.                                                                                                                                                                                                       |
| Current Rule Set area      |
| Clearance Object to Object | Specifies the minimum clearance gap you want the source and against items to maintain from each other.                                                                                                                                                |
| Matrix button              | Opens the Clearance Rules Dialog Box.                                                                                                                                                                                                                 |
| High Speed                 | Specifies the clearance values for parallel and tandem checking for the condition. The source-against entries are used as the victim-aggressor designations for crosstalk conditions checking. For more information, see Setting Up High-Speed Rules. |
| Create button              | Compile the new rule set parameters and adds a description to the Existing Rule Sets list box.                                                                                                                                                        |
| Delete button              | Removes the selected rule set from the Existing Rule Sets list box                                                                                                                                                                                    |

## Connect to SailWind Layout Dialog Box  

To access: Tools $>$ SailWind Layout menu item  

Use the Connect to SailWind Layout dialog box to choose your connection to SailWind Layout. You can then gain access to the SailWind Layout Link dialog box.  

![](/images/0baac55d4d7b72f3864278bcfd5522007f40d01ed44f402230a74be25585758c.jpg)  
Figure 55. Connect to SailWind Layout Dialog Box  

**Objects**  

Table 89. Connect to SailWind Layout Dialog Box Contents

|  Name       | Description                                                                                                                                                                                                                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| New button  | Opens and connects SailWind Logic to a new session of SailWind Layout then opens the SailWind Layout Link Dialog Box. Tip If there is a delay in launching and connecting to SailWind Layout, the Server Busy Dialog Box may appear. Wait a short time or till SailWind Layout appears on your Windows Taskbar then click Retry.        |
| Open button | Opens and connects to an existing design file in a new SailWind Layout session then opens the SailWind Layout Link Dialog Box. Tip If a prompt window is open in SailWind Layout, the Server Busy Dialog Box may appear. Click the Switch To button and take care of the prompt to enable SaiiWind Logic to connect to SailWind Layout. |

## Connect to SailWind Router Dialog Box

To access: Tools $>$ SailWind Router menu item  

Use the Connect to SailWind Router dialog box to choose your connection to SailWind Router. You can then gain access to the SailWind Router Link dialog box.  

![](/images/742321e8c19271c45495ea80c0da9e665d441f16efa92605f666a5b85fe89cc5.jpg)  
Figure 56. Connect to SailWind Router Dialog Box  

**Objects**  

Table 90. Connect to SailWind Router Dialog Box Contents

|  Name       | Description                                                                                                                                                                                                                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| New button  | Opens and connects SailWind Logic to a new session of SailWind Router then opens the SailWind Router Link Dialog Box. Tip If there is a delay in launching and connecting to SailWind Router, the Server Busy Dialog Box may appear. Wait a short time or till SailWind Router appears on your Windows Taskbar then click Retry.        |
| Open button | Opens and connects to an existing design file in a new SailWind Router session then opens the SailWind Router Link Dialog Box. Tip If a prompt window is open in SailWind Router, the Server Busy Dialog Box may appear. Click the Switch To button and take care of the prompt to enable SaiiWind Logic to connect to SailWind Router. |

## Crash Detected Dialog Box  

To access: This dialog box is inaccessible unless the software crashes and crash detection is enabled in the software .ini file.  

The Crash Detected dialog box opens at a crash and enables you to save a report of the SailWind environment as well as pertinent files into a compressed SailWind Dump File for troubleshooting.  

**Objects**  

Table 91. Crash Detected Dialog Box Contents   


|  Name                     | Description                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Comments box              | You can describe what you were doing when the error occurred or anything else you can think of that might help when investigating the crash.                                                                                                                                                                                                                  |
| Attach BMW data check box | You can include BMW data and your project files. This will enable customer support to play back what you were doing in your design that led up to the crash. This check box is unavailable if the BMW feature is not enabled. See also BMW and BLT.                                                                                                           |
| Save button               | You must click the Save button if you want to create a report file. When you click the Save button, you are prompted with a Save As dialog box. The file that is created is called a Dump File and is compressed in the .zip format. This is the file that you must send to customer support. it will include the report, the BMW data and the project files. |

## Create PDF Dialog Box  

To access: File $>$ Create PDF menu item $>$ enter filename $>$ Save  

You can create an intelligent PDF of your schematic, choosing which sheets you want to share and show to others in your organization. You can create the PDF in full-color or black and white, with hyperlinks to part attributes, and with search capabilities, making it easy to locate parts and nets. Once you locate a net, you can find other instances of it through the entire schematic, even when the net is on a different page. You can also create a black and white, non-searchable PDF of your schematic.  

Restriction: To search a PDF, you must substitute the Stroke font with a System font  

![](/images/b7061a4275721affa21795fa77dadf53664fe5e59e16e7b8b47042471cfde312.jpg)  

Tip   
Adobe® Acrobat® Distiller™ is not required on your system to create a PDF. See also Printing to PDF.  

![](/images/3487c528c93070513530791875c98f311b4b50ec3f6849f970438b4bb81b885b.jpg)  
Figure 57. Create PDF Dialog Box  

**Objects**  

Table 92. Create PDF Dialog Box Contents   


| Name                                                     | Description                                                                                                                                                                            |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Available list                                           | List all of the sheets available to you.                                                                                                                                               |
| Add >> Button                                            | Moves the selected sheet to the Sheets to PDF list.                                                                                                                                    |
| Add All >> Button                                        | Moves all sheets to the Sheets to PDF list.                                                                                                                                            |
| << Remove button                                         | Moves the selected sheet to the Available list.                                                                                                                                        |
| << Remove All Button                                     | Moves all sheets to the Available list.                                                                                                                                                |
| Sheets to PDF list                                       | Lists the sheets you want to PDF.                                                                                                                                                      |
| View PDF after creation                                  | Specifies to open the PDF after it has been created.                                                                                                                                   |
| Replace Stroke font with                                 | Specifies to replace the Stroke font with a system font. Select the font you want from the list. Use the Font style buttons to add Bold, Italic, or Underline styles.                  |
|                                                          |  Restriction:                                                                                                                                                                          |
|                                                          | · You can only search a PDF if you replace the Stroke font with a System font. There is no font size control. Text heights are already set for each text                               |
| Create hyperlinks                                        | item in the design. The height will be converted to the nearest point size in the PDF. Specifies to create a listing of the part attributes as a hyperlink.                            |
| that will display part attributes Create hyperlinks that |                                                                                                                                                                                        |
| will pan through nets                                    | Specifies to create a link to pan to the next instance of that net or bus. Restriction: If the net name is not visible in the schematic, you will not be able to pan through the nets. |
| Visible rectangle around objects with hyperlinks         | Specifies to create all hyperlinks with visible boxes: yellow around the part attributes, blue around the net and bus names. Restriction:                                              |
| Color scheme area                                        | it is clicked. Specifies the color scheme you want to use. 1 Tip                                                                                                                       |

## Customize Dialog Box  

Use the Commands tab to add commands to menus or toolbars, or to create custom menus.  

To access: Tools $>$ Customize menu item  

Customize Dialog Box, Commands Tab Customize Dialog Box, Keyboard and Mouse Tab Customize Dialog Box, Macro Files Tab Customize Dialog Box, Options Tab Customize Dialog Box, Toolbars and Menus Tab  

### Customize Dialog Box, Commands Tab

To access: Tools $>$ Customize menu item $>$ Commands tab  

Use the Commands tab to add commands to menus or toolbars, or to create custom menus.  

![](/images/f0f338bacd2877508e70fd5c28b34a09607305a3f8ab0a924b8e30c17258a7b3.jpg)  
Figure 58. Commands Tab  

**Objects**  

Table 93. Command Tab Contents   


|  Name           | Description                                                                         |
|-----------------|-------------------------------------------------------------------------------------|
| Categories list | Narrows down the list of commands.                                                  |
| Commands list   | List of commands available to add to a menu or toolbar.                             |
| X/              | Add a new command, delete a command you've added, or rename a command you've added. |

**Related Topics**  

Creating a Custom Command Creating a Custom Menu Defining Properties for a New Command  

### Customize Dialog Box, Keyboard and Mouse Tab

To access: Tools $>$ Customize menu item $>$ Keyboard and Mouse tab Create and customize shortcut keys using the Keyboard and Mouse tab of the Customize dialog box.  

![](/images/1bc47ec1202efbc1dcc0f34e9ac274a0dd1cb80d37b1c3ee2203fac5464492a8.jpg)  
Figure 59. Keyboard and Mouse Tab  

Table 94. Keyboard and Mouse Tab Contents   


| Name | Description |
| --- | --- |
| Mode list | Narrows down the list of commands. |
| Commands list | The list of commands available for which to assign a shortcut. |
|  | Add a new command (opens the Add Command Dialog Box on page 440), delete a command you've added, or rename a command you've added (opens the Edit Command dialog box on page 440). |
| Current shortcuts list | The list of shortcuts assigned to the selected command. |
| X | Add a new shortcut (open the Assign Shortcut Dialog Box), or delete a shortcut you've added. |
| Description | Lists what the selected command does. |  

Table 94. Keyboard and Mouse Tab Contents (continued)   


| Name | Description |
| --- | --- |
| Reset All button | Sets the selected toolbar or shortcut menu to the default settings. |
| Report button | Saves a report of all current shortcut commands. |  

### Customize Dialog Box, Macro Files Tab

To access: Tools $>$ Customize menu item $>$ Macro Files tab  

Create commands from macro files and add them to toolbars and menus using the Macro Files tab.  

![](/images/d6b3c03a2f4b4a4e6e781c6c79b132a6eba484a98c3fcd4facfb1ab960dc7de6.jpg)  

Tip   
To create a command from a macro command file, the macro command file (.mcr) must already exist. You can create a macro by recording it in a SailWind tool or scripting it in Macro language. For more information, see “Macros” on page 47.  

![](/images/05c25f6f816398268175965f3cf9a5039a1d96e8ad6a0b18bf0ce1d332cc3ed3.jpg)  
Figure 60. Macro Files Tab  

**Objects**  

Table 95. Macro Files Tab Contents   


| Name | Description |
| --- | --- |
| Macro Command Files list | The list of macro files you have opened. |
| X/ | Add a macro to the list (opens the Open Macro dialog box), delete a macro from the list, or edit the location of a macro you've added. |
| Description | Lists what the selected macro does. |  

### Customize Dialog Box, Options Tab

To access: Tools $>$ Customize menu item $>$ Options tab  

Customize the SailWind interface by changing the appearance of menus and toolbars using the Options tab of the Customize dialog box.  

![](/images/d9e268c75c41be62ef939d290a94a1632a6cfce7dae202b8446f0292496e40e5.jpg)  
Figure 61. Options Tab  

**Objects**  

Table 96. Options Tab Contents   


| Name | Description |
| --- | --- |
| Show ToolTips on toolbars | Displays the button name over the toolbar button when you hover over it with your pointer. |
| Show shortcuts in ToolTips | In addition to the name in the ToolTip, displays the shortcut for the button. |
| Large lcons | Displays icons on the toolbar larger than the default size. |
| Menu animations list | The type of animation for your menus: None, Unfold, Slide, or Fade. |
| Menu shadows | Displays a shadow behind the menu. |  

Table 96. Options Tab Contents (continued)   


| Name | Description |
| --- | --- |
| Wait until before executing long shortcuts | Delays the execution of shortcut keys until you press Enter. |
| Show recent commands first | Displays your recent menu command selections at the top of the list. |
| Show full menus after delay | Displays the full menu after a slight pause. |
| Reset my usage data button | Restores the default set of commands to the menus and toolbars. O Tip This option does not undo any explicit customizations you made. |
| Visual Style | Sets the look and feel of your toolbars and title bars. |
| Interface Language | Specifies the language for all dialog boxes and messages displayed: English, Chinese Simplified. |  

**Related Topics**  

Customized Appearance of the Screen  

### Customize Dialog Box, Toolbars and Menus Tab

To access: Tools $>$ Customize menu item $>$ Toolbars and Menus tab  

Use the Toolbars and Menus tab on the Customize dialog box to create custom toolbars and shortcut menus.  

Tip   
To create a custom main menu, use the Commands tab on the Customize dialog box. See Creating a Custom Menu.  

![](/images/c4d54772616d975f7932c434fb62ffbf3368aaecab814d2d94ec99a4dba96b2f.jpg)  
Figure 62. Toolbars and Menus Tab  

**Objects**  

Table 97. Toolbars and Menus Tab Contents   


| Name | Description |
| --- | --- |
| Toolbars list | Specify which toolbars to display in the main window. |
| X/ | Add a new toolbar, delete a toolbar you've added, or rename a toolbar you've added. |
| Show text labels | Shows the text label on the button in addition to the icon |
| Select shortcut menus | Specifies the shortcut menu you want to customize. |  

Table 97. Toolbars and Menus Tab Contents (continued)   


|  |  |
| --- | --- |
|  | Restriction: SailWind Router only. |
| Reset button | Sets the selected toolbar or shortcut menu to the default settings. |
| Reset All button | Sets all toolbars or shortcut menus back to their default settings. |  

**Related Topics**  

Customizing the SailWind Interface  

## DC Source Sweep Analysis Dialog Box  

To access: Tools $>$ SPICE Netlist menu item $>$ Simulation Setup button $|>$ DC Sweep button  

Use the DC Source Sweep Analysis dialog box to set options specifically for a DC Sweep analysis.  

![](/images/30dd1d163a7ebd208cf10656f5c2c846cf90df66d055fad90889925bb949b809.jpg)  
Figure 63. DC Source Sweep Analysis Dialog Box  

**Objects**  

Table 98. DC Source Sweep Analysis Dialog Box Contents   


| Name | Description |
| --- | --- |
| Source | Specifies the name of the voltage or current source. |
| Start | Specifies the starting voltage for the sweep. |
| End | Specifies the stopping voltage for the sweep. |
| Step | Specifies the incrementing values for the sweep. |  

**Related Topics**  

Creating a SPICE Netlist Setting Up DC Source Sweep Analysis  

## Default Rules Dialog Box  

To access: Setup $>$ Design Rules menu item $>$ Default button  

Use the Default Rules dialog box to define rules which apply to all objects that are not included in any other rule within the hierarchy.  

![](/images/d849166201546ab8304b3af2ac33c7c15ca814ad8434a0c457af51ce9382f134.jpg)  
Figure 64. Default Rules Dialog Box  

**Objects**  

Table 99. Default Rules Dialog Box Contents   


| Name | Description |
| --- | --- |
| Clearance button | Opens the Clearance Rules Dialog Box. |
| Routing button | Opens the Routing Rules Dialog Box. |
| Hi Speed button | Opens the HiSpeed Rules Dialog Box. |
| Report button | Opens the Rules Report Dialog Box. |  

## Differential Pairs Dialog Box  

To access: Setup $>$ Design Rules menu item $>$ Differential Pairs button  

Use the Differential Pairs dialog box to identify nets or pin pairs that behave electrically as differentia pairs, and to define differential pair design rules.  

![](/images/93cb3391b1b20a250370178a60748ec4df916e70e435c3030b7a41354da6fd1d.jpg)  
Figure 65. Differential Pairs Dialog Box  

**Objects**  

Table 100. Differential Pairs Dialog Box Contents

| Name | Description |
| --- | --- |
| Available list | Lists nets that have not been assigned to a differential pair. |  

Table 100. Differential Pairs Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Selected list | Lists the nests that have been selected. 1Tip |
| Select >> button | Moves the selected net to the Selected list. |
| < Moves the net that was previously selected back to the Available list. | Moves the net that was previously selected back to the Available list. |
| Add>> button | Moves the two nets in the Selected list to the Pairs list. |
| < Moves the two nets in the Pairs list to the Available list. | Moves the two nets in the Pairs list to the Available list. |
| Pairs list | Lists the differential pairs. |
| Trace length area | Specifies the minimum and maximum trace length values. |
| Restrict layer changes during autorouting | Forces the pair to be routed on a single layer. A Tip This setting does not restrict layer changes when routing |
| Properties of the pair table | Sets the width and gap per layer. |
| Add button | Adds a row to the Properties of the pair table. |
| Delete button | Removes the selected row from the Properties of the pair table. |
| Obstacles area | Specifies to allow routing around an obstacle in the controlled gap area by temporarily exceeding the pair routing gap. |
|  | iTip This setting applies to autorouting and does not restrict splitting around obstacles when routing interactively. |
|  | Also specifies the maximum number of obstacles and the maximum obstacle size. |
|  | Tip |
| Report button | Obstacles in the start zone or end zone are not counted. Opens the Rules Report Dialog Box. |  

## Display Colors Dialog Box

To access: Setup $>$ Display Colors menu item  

Use the Display Colors Setup dialog box to Set display colors, save them, and restore them; Change the color palette; make objects visible; and make objects invisible.  

![](/images/d7b97e26bfbef33c2e0294248a9ecb6e6d52b51192c0a45a652faffacb624df0.jpg)  

!Tip  

Changes you make to the color configuration in the Display Colors Setup dialog box do not apply to disabled layers.  

![](/images/5c90595c2b15948313c9de1a9134e0c4463f3074672fe01637b6379f4d92abd1.jpg)  
Figure 66. Display Colors Setup Dialog Box  

**Objects**  

Table 101. Display Colors Setup Dialog Box Contents   


| Name | Description |
| --- | --- |
| Selected Color area | Select a color from the palette to assign to items on a layer. Once you select a color here, click the tile in the Color by Layer area of the item to which you want to assign the color. |
| Palette button | Opens the Color dialog box where you can choose to use new colors or customize colors you want to use. |
| Default Palette button | Reassigns all colors and settings to the default settings. O Tip You can change the default settings by saving a configuration |
| Misc area | and naming it default. Apply a color to objects in the Misc area to change the color of that object in the workspace. |
| Titles area | To make a text string visible in the part editor, select the check box beside the string type in the Titles area. |
| Configuration list | The list of saved configurations. |
| Save button | Opens the Save Configuration Dialog Box. |
| Delete button | Removes the selected configuration from the Configuration list. |  

**Related Topics**  

Display Colors Dialog Box - Part Editor Setting Display Colors  

## Display Colors Dialog Box - Part Editor  

To access: In the Part Editor, Setup $>$ Display Colors menu item  

Use the Display Colors dialog box while in the Part Editor or the CAE Decal Editor to control the colors of objects and the working area. SailWind Logic saves the color settings for part editor items with the schematic. This dialog box is similar to the one used in the schematic editor, with check boxes to display text items.  

![](/images/2844cd561b759d66999b8dd02228d0fa9a5e392450bee619cfb244ebf9429105.jpg)  
Figure 67. Display Colors Dialog Box in the Part Editor  

**Objects**  

Table 102. Display Colors Dialog Box contents   


| Name | Description |
| --- | --- |
| Selected Color | Select a color in this area to apply to tiles in the Items area. |
| Palette button | Click to open the Color dialog box where you can specify new colors or customize colors that appear in the Selected Color area. |
| Default Palette button | Click Default Palette to restore the default color settings in the Selected Color area. Tip Refer to the Microsoft Windows Help for more information i |
| Background | about changing the Color Palette. Apply a color to this color tile to change the background color or work area surface in the Part Editor workspace. |  

Table 102. Display Colors Dialog Box contents (continued)   


| Name | Description |
| --- | --- |
|  | Tip · To make an item invisible, set it to the background color. · The color selection for displaying items or making them invisible does not affect plotting of the schematic. |
| Selections | Apply a color to this color tile to change the color of objects that you select in the workspace. |
| Items area | Apply a color to objects in the ltems area to change the color of that object in the workspace. i Tip Some of the items have a color setting in the Box column. Box indicates the color of the box that is drawn around the text item. This box serves two purposes: it indicates the exact size of the text item when it is plotted, thereby helping you avoid overlaps while moving the item; and it provides visibility of the text item at very small zoom levels. |
| Names area | To make a text string visible in the part editor, select the check box beside the string type in the Names area. Restriction: · This area is only available when editing a CAE decal, pin decal, or when editing the graphics of individual connector, or off-page type symbols. ·When editing a CAE decal - Sheet Number is unavailable. · When editing a pin decal - Reference Designator, Part-Type Name, Attribute Labels, and Sheet Number are unavailable. · When editing the pin decal of an off-page, power or ground symbol - only Netnames and Sheet Number are available. · When editing the_graphics of a single connector pin - only Ref Designator, Part-Type Name, and Attribute Labels are available. |  

## Drafting Properties Dialog Box  

To access: Select a drafting object $>$ right-click $>$ Properties menu item  

Use the Drafting Properties dialog box to modify the line width, style, and orientation of selected drafting objects.  

![](/images/756f731fcb1edbf958883b7c792d11258e286622118a11e4aeeec1aa14329718.jpg)  
Figure 68. Drafting Properties Dialog Box  

**Objects**  

Table 103. Drafting Properties Dialog Box Contents   


| Field | Description |
| --- | --- |
| Width | Specifies the line width for the drafting object. The current line width of the selected drafting object is automatically displayed, change it if necessary. Tip Use the Line Widths tab in the Options dialog box to change the default line width. |
| Filled | Specifies to create a filled shape from a selected polygon. Tip This option is grayed for circles, paths, and if you used Pull Arc to |
| Style area | modify the polygon. Specifies the line style option for the selected drafting object: Solid or Dotted. |
| Rotation | Specifies the degree of rotation from the Rotation list. Tip · Rotation can be O or 90 degrees. |
| Mirror by X | · The point used when selecting the object is the also the point of rotation. Specifies to mirror the selected drafting object in the X (horizontal) |
|  | direction. |
| Mirror by Y | Specifies to mirror the selected drafting object in the Y (vertical) direction. |  

## Edit Button Image Dialog Box  

To access: Tools $>$ Customize menu item $>$ Commands tab $>$ New button $>$ Select User-Defined Image $>$ New or Edit button  

Use the Edit Button Image dialog box to create or edit button icons.  

![](/images/d355d74041a00ca03256f8f174d7ecf1a7dd5dd93ac542b217c61d843fcdbf4f.jpg)  
Figure 69. Edit Button Image Dialog Box  

**Objects**  

Table 104. Edit Button Image Dialog Box Contents   


| Field | Description |
| --- | --- |
| Colors area | Select a color to use with the tools |
| Tools area | Select a tool to draw/edit the picture or icon of the button |  

## Fields Dialog Box  

To access: Select nothing or a 2D line object $>$ right-click $>$ Fields menu item  

Use the Fields dialog box to manage multiple fields. You can manage the fields in the entire schematic or in a 2D line object.  

![](/images/e1171e4db50730461c1a398a901d9be92156e3a291bf3d6c6bf5bc0439c8dcbd.jpg)  
Figure 70. Fields Dialog Box  

**Objects**  

Table 105. Fields Dialog Box Contents   


| Field | Description |
| --- | --- |
| System | Displays the name and value for all system fields in the design. |
| Delete button | Removes the selected row. Restriction: System fields can be deleted from 2D line items only. |
| User | Displays the name and value for all user fields in the design |
| Add button | Inserts a row at the bottom of the list where you can add a new field. |
| Delete button | Removes the selected row. |
| Edit button | Makes the selected cell available for editing. |  

Table 105. Fields Dialog Box Contents (continued)   


| Field | Description |
| --- | --- |
|  | iTip |
|  | You can also double-click a cell to edit the contents. |

Related Topics Managing Fields  

## Field Properties Dialog Box  

To access: Select a field $>$ right-click $>$ Properties menu item  

Use the Field Properties dialog box to modify a field name or change its text size, orientation, or justification.  

![](/images/48b45842106c80c737c035978fd022d67156240e21cede5d6619f32425de979a.jpg)  
Figure 71. Field Properties Dialog Box  

**Objects**  

Table 106. Field Properties Dialog Box Contents   


| Name | Description |
| --- | --- |
| Name | The name of the field. Type a new or select an existing field name to change it. |
| Value | Specifies the text you want in the schematic. |
| XY | Type coordinates to place the text in a specified location. |
| Rotation | Specifies the rotation of the text: O or 90 degrees. |
| Line Width | Specifies the line width for stroke fonts only. |  

Table 106. Field Properties Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | text Stroke Line Width |
|  | Specifies the size of the font. Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke fonts. The size refers to the height of the tallest characters. Gg |
| Font Style | Enables you to change the font style to bold, italic, and underlined. Restriction: System fonts only. |
| Font list | The fonts available to you. This lists either stroke fonts or system fonts. You choose which type of font to use in the Fonts Dialog Box. Tip · Select stroke font or a system font. · For system fonts, you can also click a font style button, or |
| Horizontal/Vertical Justification | Specifies the horizontal (Right, Center, Left) justification and the vertical (Up, Center, Down) justification of the text. |  

**Related Topics**  

Modifying Fields Add Field Dialog Box  

## Font Replacement Dialog Box  

To access: When you open a design created with fonts that are not installed on your system, the Fon Replacement dialog box opens automatically.  

Use the Font Replacement dialog box to manage how missing fonts are replaced in your design.  

![](/images/a5bacc12c3f97acc40c41fdce228dcfdb784ea5cb4926488ecc6867db45bdef4.jpg)  

!Tip  

If the design uses fonts or character sets that are not installed on your system, empty boxes will appear where you expect to find text or symbols. Once the font replacement process completes, the symbols display properly.  

Figure 72. Font Replacement Dialog Box  

![](/images/8cb984f1210ded5544a2bf5e80368df38f7904077a422a7d874994e9443ce655.jpg)  

**Objects**  

Table 107. Font Replacement Dialog Box Contents   


| Name | Description |
| --- | --- |
| Mode | Specifies the mode to replace this font. |
| · Automatic — Specifies to replace the font automatically with the one selected by SailWind Layout. |  |
| · Manual —— Specifies to replace the font with one you select from the Replace with font list. |  |
|  |  |
| · Skip — Specifies to preserve the original font. |  |  

Table 107. Font Replacement Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Missing font | The name of the font in this design that is missing from your system. |
| Replace with font | If you chose Manual, lists the fonts available for you to replace the missing font. If you chose Automatic, lists the font SailWind Layout chose to replace the missing font. |  

!Tip

When replacing fonts, observe the following:  

• You can select some fonts for automatic replacement, select others for manual replacement, and choose that other font replacements be skipped entirely. • You can have a combination of stroke font and system fonts within the same design. • You must set up fonts for each text string and/or label you create in your design. Once you set up fonts for a text string or label, you can then use the Properties dialog to apply a font and font characteristics to all objects that you select for modification with the Properties dialog box.  

**Restriction:**  

When working with fonts note the following restrictions:  

• If the design uses fonts or character sets that are not installed on your system, a font substitution process begins automatically when the file is loaded. During this process, you are asked to choose fonts to substitute for those that are missing from your system.   
• System font text is supported in RS274X Gerber format when Fill mode is on. System font text is output to Gerber format as a set of filled polygons.   
• System fonts are not supported in the RS-274D CAM output format. If you attempt to use this format with system fonts, the program displays a warning message. If you proceed, system fonts will not be output. Instead, you should use the 274X format with system fonts.   
• Type 1 fonts are not supported.  

**Related Topics**  

Managing Font Replacement  

## Fonts Dialog Box

To access: Setup $>$ Fonts menu item  

Use the Fonts dialog box to set up or change the fonts to be used in your design.  

![](/images/a5cb7baf488be75ff67eabf9ba7e03a55c23365b0e6b27a9b885181d00be21e8.jpg)  

**Restriction:**  

If the schematic uses fonts or character sets that are not installed on your system, a font substitution process begins automatically when the file is loaded. During this process, you are asked to select fonts to substitute for those that are missing from your system.  

![](/images/e5c85799729270eab3757e43b8fb794066d81a493c66699d6689c0b809ab9297.jpg)  

Tip If you want to change font sizes, see Modifying Part Type Labels.  

![](/images/79def9ec3426cc5314898cacd971dd7c0b2c713befca5878f245fbec45579ca2.jpg)  
Figure 73. Fonts Dialog Box  

**Objects**  

Table 108. Fonts Dialog Box Contents   


| Name | Description |
| --- | --- |
| Font Style | The fonts available to you: ·Stroke |
| Default Font list | ·System |
| Specifies the system font you want to use. iTip |  |  

**Related Topics**  

Setting Fonts  

## Get Drafting Items From Library Dialog Box  

To access: Schematic Editing toolbar $>$ Add 2D Line from Library button  

Use the Get Drafting Item from Library dialog box to load a 2D line item from the available libraries to the current schematic.  

![](/images/84813cb57564b83b3b1617bde048d114ad2b980905e89900345411e64a0eae33.jpg)  
Figure 74. Get Drafting Items From Library Dialog Box  

**Objects**  

Table 109. Get Drafting Items From Library Dialog Box Contents   


| Field | Description |
| --- | --- |
| Preview area | Displays the selected gate decal |
| Drafting Items | Lists the drafting items available based on the filter settings |
| Library list | Specifies the library you want to use. |
| Items | Narrows the search. You can use wildcards or expressions on page 105. An asterisk (*) displays all parts in the list. |
| Apply button | Searches the library for the specified item. |  

**Related Topics**  

Adding Drafting Items From a Library  

## Get Gate Decal From Library Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ Open button $>$ Select CAE Decal $>$ OK button  

Use the Get Gate Decal from Library dialog box to open an existing CAE Decal in the Part Editor.  

![](/images/3e37ab7dac14c1ba8496251ab4f30bb20a48870e1fd03d3ae6219fa8df9c16ce.jpg)  
Figure 75. Get Gate Decals From Library Dialog Box  

**Objects**  

Table 110. Get Gate Decals From Library Dialog Box Contents   


| Field | Description |
| --- | --- |
| Preview area | Displays the selected gate decal |
| Gate Decals | Lists the gate decals available based on the filter settings. |
| Library list | Specifies the library you want to use. |
| Items | Narrows the search. You can use wildcards or expressions on page 105. An asterisk (*) displays all parts in the list. |
| Apply button | Searches the library for the specified item. |  

**Related Topics**  

Getting Gate Decals From the Library  

## Get PCB Decal From Library Dialog Box  

To access: Select a part $>$ right-click $>$ Properties $>$ PCB Decals button $>$ Browse button Use the Get PCB Decal from Library dialog box to search a library for a PCB decal.  

![](/images/640b031c161aa779e881b9ffc4e58b577121be2debe2d0d535d5f4dfacfd5362.jpg)  
Figure 76. Get PCB Decal From Library Dialog Box  

**Objects**  

Table 111. Get PCB Decal From Library Dialog Box Contents   


| Name | Description |
| --- | --- |
| Picture Area | Displays the PCBdecal highlighted in the Decals area. |
| Decals | Lists the available PCB decals in the selected library or all libraries. |
| Library list | Lists the libraries available to you. |
| Filter | Searches the chosen library (or libraries) for a specific part or item name, or names that match a wildcard or expression on page 105. Use the Library dropdown list to select specific library directories or the All Libraries setting. Type * to view all parts or items in the chosen libraries. Click Apply to search the libraries and display the search results. |  

**Related Topics**  

Searching the Library for a Decal  

## Hierarchical Symbol Wizard Dialog Box  

To access: Schematic Editing toolbar $>$ New Hierarchical Symbol button  

Use the Hierarchical Symbol Wizard dialog box to create a new hierarchical symbol in either a top-down or bottom-up design structure. The symbol creation methodology varies, depending on the structure you use.  

![](/images/cf48c502361934c8318f6ad7248af9cb22dc712017150ef938efe06bf8823e2f.jpg)  
Figure 77. Hierarchical Symbol Wizard Dialog Box  

**Objects**  

Table 112. Hierarchical Symbol Wizard Dialog Box Contents   


| Name | Description |
| --- | --- |
| Preview | Displays the symbol outline before the symbol appears in the Part Editor. Display is based on the current settings. |
| Pin Parameters area | · Pin Length — Sets the distance from the terminal connection point and the decal outline. This option does not adjust the length of the pin decal. · Pin Spacing — Specifies the spacing between adjacent pins. |
| Box Parameters area | · Box Width — Sets the width of the decal outline. Pin decals are moved left or right to accommodate the box width. · Min Box Hgt. - Sets the minimum height of the decal outline. If you enter a value larger than needed to accommodate the number of input or output pins, space is added to the bottom of the decal. OTip Type values or use the arrow buttons. |
| Input Pins area | · Pin Decal — Specifies the type of pin decal. · Pin Count — Specifies the number of input pins for a hierarchical symbol of a new sheet during top-down design. O Tip Type values or use the arrow buttons. |  

Table 112. Hierarchical Symbol Wizard Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Output Pins area | · Pin Decal - Specifies the type of pin decal. · Pin Count — Specifies the number of output pins for a hierarchical symbol of a new sheet during top-down design. 1 Tip |
| Hierarchical Sheet area | Type values or use the arrow buttons. • Sheet Number — Lists the sheets in the set or lists only the option for top-down design. Restriction: For bottom-up design, this list never displays the current sheet since you can place the symbol that represents the current sheet on the current sheet. . Sheet-name —— Specifies the name of the hierarchical symbol. Restriction: |  

**Related Topics**  

Creating a Top-Down Hierarchy Creating a Bottom-Up Hierarchy  

## HiSpeed Rules Dialog Box  

To access: Setup $>$ Design Rules menu item $>$ a rule hierarchy button $>$ HiSpeed button  

Use the HiSpeed Rules dialog box to define rules for Parallelism, Tandem, Shielding, Routed Length, Stub Length, Delay, Capacitance, Impedance, and Matched Length.  

![](/images/03c47e08f977de88dcd72b626d3a18681f472d9917ef2864a09b221481a138f3.jpg)  

!Tip  

When working with HiSpeed Rules, observe the following:  

• When imported into SailWind, the EDC (Electrodynamic Checking) routine checks to see if rules are met correctly after routing (except shielding and matched length). • You can use the Conditional Rule Setup Dialog Box to save a high speed configuration as a set, or to apply for a selected item only when it comes in contact with different level of the hierarchical order on page 305.  

![](/images/37b992b3ea90d10d4add86ad7f1237b96a30c5bf7f31788f98a3ee395db47586.jpg)  
Figure 78. HiSpeed Rules Dialog Box  

**Objects**  

Table 113. HiSpeed Rules Dialog Box contents   


| Name | Description |
| --- | --- |
| Parallelism | Restricts the distance that traces in different nets on the same layer can run together. Tip · Length defines the maximum allowable parallel/tandem distance. · Gap defines the minimum gap between traces below which the |
| Tandem | parallel/tandem rules apply. Restricts the distance that traces in different nets on different layers can run together. |  

| Table 113. HiSpeed Rules Dialog Box contents (continued) |
| --- |
| Name |
|  |
|  |
| Aggressor |
| Rules area |
|  |
|  |
|  |
|  |
|  |
|  |
| Shield |
|  |
| Gap |
| Use Net |
| Match Lengths |
| Tolerance |
| Delete button |  

**Related Topics**  

Setting Up High-Speed Rules  

## Installed Options Dialog Box  

To access: Help $>$ Installed Options menu item $>$ License File tab  

Use the License File tab to select and then view license file information, either the actual license file (for node-locked licensing) or the feature usage status associated with a server license (for floating licensing)  

![](/images/2316a94cf5f1911d83bff3deb4403ce9acb933f3d2935bc8c10031db3604b3d9.jpg)  
Figure 79. Installed Options Dialog Box, License File Tab  

**Objects**  

Table 114. Installed Options Dialog Box, License File Tab contents   


| Name | Description |
| --- | --- |
| License File | Displays the location of the license file. |
| Source | Displays the source of the license. |
| View button | Specifies to display the selected license file in the view area. Exception: For Node-locked licenses only. |
| Status button | Specifies to display the selected feature usage information. Exception: For Floating licenses only. |
| View area | Displays the selected license file information after you click View (Node-locked license) or Status (Floating license). |
| Suite Configuration button | Opens the SailWind Suite Configuration Dialog Box. |
| Restriction: Available only with floating/server-based licenses, a mix of different SailWind Suites, or a mix of unbundled licenses and suites. |  |  

**Related Topics**  

Viewing a License File or License Status  

## Library List Dialog Box  

To access: File $>$ Library menu item $>$ Manage Lib. List button  

When you add a part to the design, you retrieve information about that part from a library. The Library List dialog box contains a list of libraries to search. The libraries are searched in the order in which they are listed, beginning with the first library in the list.  

![](/images/1600061bed93b607e45411c68bcc1df71f4687bf0f785f07a31bc5b90867a911.jpg)  
Figure 80. Library List Dialog Box  

**Objects**  

Table 115. Library List Dialog Box Contents   


| Name | Description |
| --- | --- |
| Library list | The libraries currently listed in the Library Manager Library list. |
| Read Only | A status indicator only; this box is always unavailable. |
| Shared | Shares the library over the network. This enables more than one user to access the library file at the same time. |
| Allow Search | Includes the library when performing operations that involves libraries, such as adding parts. |
| Add button | Adds a library to the Library list. |
| Remove button | Removes a library from the Library list. |
| Up/Down buttons | Moves the order of the libraries in the Library list. |
| Synchronize with SailWind Layout | Specifies to push the library settings to SailWind Layout from SailWind Logic. |  

**Related Topics**  

Setting the Library List Order  

## Library Manager Dialog Box  

To access: File $>$ Library menu item  

Use the Library Manager to perform operations associated with editing and copying the contents of libraries.  

![](/images/90239f48cec1cb84125dc14f7c7db9b339f41b2bfeb8fbe9dc25ca7ec9f89004.jpg)  
Figure 81. Library Manager Dialog Box  

**Objects**  

Table 116. Library Manager Dialog Box Contents   


| Name | Description |
| --- | --- |
| Library list | The list of libraries available to you. |
| Create New Lib button | Opens the New Library window where you can specify a new library name and location. |
| Manage Lib. List button | Opens the Library List Dialog Box. |
| Attr Manager button | Opens the Manage Library Attributes Dialog Box. |  

| Tabie11 ntents (continued) |
| --- |
| Name |
| Preview area |
| Filter area |
|  |
| Filter list |
| New button |
|  |
|  |
|  |
|  |
|  |
|  |
| Edit button |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Delete button |
|  |
|  |
| Copy button |  

Table 116. Library Manager Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | Restriction: |
| Libraries). | See also Copying a Library Item. |
| Import button | Import library data from an ASCll file. The file type is dependent on |
| the filter. Restriction: |  |
| This button is unavailable when the Library is set to (All Libraries). |  |
| Export button | See also Importing Library Data. |
| Export library data to an ASCll file. The file type is dependent on the filter. |  |
| Restriction: This button is unavailable when the Library is set to (All Libraries). |  |
| List to File button | See also Exporting Library Data. |
|  | The action taken is dependent on the filter. |
|  | · Decals — Generates a list of PCB Decals in a single library. |
|  | · Parts — Generates a list of Parts in a single library or all |
|  | libraries along with chosen atributes. |
|  |  |
|  | · Lines — Generates a list of line items in a single library. |
|  | · Logic —— Generates a list of CAE decals or Logic symbols in a single library. |
|  | Restriction: When the Library is set to (All Libraries), this button is |  

## Log Test Dialog Box  

To access: type BLT $>$ press Enter. If nothing happens, close SailWind Logic and restart it.   
Use BLT to replay session playback media created by BMW.  

![](/images/5c496ef8c93e242e67e81f71c4c2d4f93108c7a0c8d811fe9269b1dc7e3388b0.jpg)  
Figure 82. Log Test Dialog Box  

**Objects**  

Table 117. Log Test Dialog Box contents   


| Name | Description |
| --- | --- |
| Media Directories | Lists the session playback media files. |
| New name | Specifies to rename the selected media directory. |
| Rename button | Renames the selected media directory to the name in the New name box. |  

**Related Topics**  

Replaying Session Playback Media With BLT  

## Logic Families Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ Edit Electrical button $>$ General tab $>$ Families button Use the Logic Families dialog box to add, delete, or modify logic family names and default reference designator prefixes.  

![](/images/665e45a5338f550ac4bbfb5e9ce20aabe54033c8d9d52adedb1572b7d0294195.jpg)  
Figure 83. Logic Families Dialog Box  

**Objects**  

Table 118. Logic Families Dialog Box Contents   


| Name | Description |
| --- | --- |
| Family column | Lists the logic family. |
| Prefix column | Lists the prefix for the logic family |
| Add button | Adds a row to the table. |
| Edit button | Makes the selected field editable. |
| Delete button | removes the selected row. |  

**Related Topics**  

Editing Logic Families  

## Make Field Dialog Box  

To access: Select a text string $>$ right-click $>$ Make Field menu item Use the Make Field dialog box to change an existing text string into a field.  

![](/images/95fba7fa46d08c60f61fedb5a1e6ea85a68ce7f85b9c5a4cfb86e47cdc9fd833.jpg)  
Figure 84. Make Field Dialog Box  

**Objects**  

Table 119. Make Field Dialog Box Contents

| Name | Description |
| --- | --- |
| Name list | Lists all of the fields available to you. |
| Value | The value of the field. |
| Restriction: |  |
| The Value box is unavailable for system fields since the value is derived from your system. |  |
| XY | Type coordinates to place the field in a specified location. |  

Table 119. Make Field Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | 0 Tip Leave these blank to attach the field to your pointer and click to indicate the location. |
| Rotation | Specifies the rotation of the text: O or 90 degrees. |
| Line Width | Specifies the line width for stroke fonts only. text Stroke Line Width |
| Size | Specifies the size of the font. Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke fonts. The 'size refers to the height of the tallest characters. Gg |
| Font Style | Enables you to change the font style to bold, italic, and underlined. Restriction: System fonts only. |
| Font list | The fonts available to you. This lists either stroke fonts or system fonts. You choose which type of font to use in the Fonts Dialog Box. 1Tip · Select stroke font or a system font. · For system fonts, you can also click a font style button, or |
| Horizontal/Vertical Justification | underlined. Specifies the horizontal (Right, Center, Left) justification and the vertical (Up, Center, Down) justification of the text. |  

**Related Topics**  

Changing a Text String Into a Field  

## Manage Library Attributes Dialog Box

To access: File $>$ Library menu item $>$ Attr Manager button  

Use the Manage Library Attributes dialog box to list the attribute names in your libraries and to add an attribute to, rename an attribute in, or delete an attribute from, the library.  

![](/images/a03e8ef0ed9dbe97ab556785da764cb7efb90d250690be64d8d94b9cd1c6f711.jpg)  
Figure 85. Manage Library Attributes Dialog Box  

**Objects**  

Table 120. Manage Library Attributes Dialog Box Contents   


| Name | Description |
| --- | --- |
| Select Library list | The list of libraries available to you. |
| Item Types list | Filters the type of items in the Attributes in Library list. |
| Browse Lib. Attr button | Opens the Browse Library Atributes Dialog Box. 1 Tip This is available only when an attribute in the New Name column in the Attributes Selected for Rename list is selected. |
| Edit New Name button | Makes the selected attribute Name editable. Tip This is available only when an attribute in the New Name column in the Attributes Selected for Rename list is selected. |
| Attributes in Library list | The list of atributes in the selected library. |
| Add >> button | Adds the selected attribute to the Rename list. |  

Table 120. Manage Library Attributes Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| << Remove button | Removes the selected attribute from the Rename list. |
| << Remove All button | Removes all of the attributes from the Rename list. |
| Attributes Selected for Rename list | The list of attributes you've selected to rename. |
| Add Attr button | Opens the Add New Atribute to Library Dialog Box. |
| Delete Attrs button | Deletes the selected atribute from the selected library. |
| Rename Attrs button | Renames all of the attributes you gave a new name to in the selected library. |  

**Related Topics**  

Managing Library Attributes  

## Manage Schematic Attributes Dialog Box  

To access: Edit $>$ Attribute Manager menu item  

Use the Manage Schematic Attributes dialog box to manage attributes at the schematic level. You can create a new attribute and automatically assign it to every part in your design. You can also rename an attribute in, or delete an attribute from, the schematic. All parts are automatically updated.  

![](/images/d2e72a24e7ae682e565164aac61169bc86e282e5b7d8d73360035ef45c3106ab.jpg)  
Figure 86. Manage Schematic Attributes Dialog Box  

**Objects**  

Table 121. Manage Schematic Attributes Dialog Box Contents   


| Name | Description |
| --- | --- |
| Attributes in Schematic list | The list of attributes in the schematic. |
| Add >> button | Adds the selected attribute to the Rename list. |
| << Remove button | Removes the selected attribute from the Rename list |
| << Remove All button | Removes all of the attributes from the Rename list. |
| Attributes Selected for Rename list | The list of attributes you've selected to rename. |
| Browse Lib. Attr button | Opens the Browse Library Attributes Dialog Box. |
| Edit New Name button | Makes the selected attribute Name editable. O Tip This is available only when an attribute in the New Name |  

Table 121. Manage Schematic Attributes Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Add Attr button | Opens the Add New Attribute to Library Dialog Box. |
| Delete Attrs button | Deletes the selected atribute from the selected library. |
| Rename Attrs button | Renames all of the attributes you gave a new name to in the selected library. |  

**Related Topics**  

Manage Attributes in a Schematic  

## Media Wizard Dialog Box  

To access: type BMW $>$ press Enter  

BMW (Basic Media Wizard) is a tool that you can use to record and play back SailWind Logic, SailWind Layout and SailWind Router sessions. It is particularly useful as a means of supplying information to SailWind Technical Support engineers trying to identify and resolve any problematical behavior you may encounter.  

![](/images/dde875a570359442e01060b0f33453ca206fc3fa5489f262dcbc36cb6457c9bc.jpg)  
Figure 87. Media Wizard Dialog Box  

**Objects**  

Table 122. Media Wizard Dialog Box contents   


| Name | Description |
| --- | --- |
| Media Wizard area | Specifies what you want the Media Wizard to do: · Create Media from Current Session — Use this procedure when the session you are recreating did not cause a SailWind tool crash. · Create Media from Previous Session — Use this procedure when the session you are recreating caused the SailWind tool to crash, and the automatic procedure described in Automatically Creating Session Playback Media for a Crashed Session cannot be used due to one of the restrictions listed in that section. · Stop Logging.— Specifies to stop the Media Wizard from logging any further actions. |
| User Initials | Specifies your initials. They are included in the playback media filenames to identify the files as yours. |
| Delete Actions Before Last Save | Specifies to delete all entries in the session log file between the first Open and the last Save command. You can do this to eliminate any actions you may have performed before beginning the series of actions that produced the problematical behavior. This makes it easier for the Tech Support engineer to identify the problem. |  

**Related Topics** BMW and BLT  

## Modeless Commands and Keyboard Shortcuts  

You can set or change some settings and functions at any time using a code letter for the command, entering the new value, and clicking Enter. This is called a Modeless Command.  

Modeless Commands usually apply to values that you change frequently during design. Use the Modeless Command G, for example, to change the grid setting. Type G, the new setting, and click Enter. Below is a summary of the Modeless Commands in SailWind Logic:  

To show this help topic at any time while SailWind Logic is running, type ? and click Enter.  

Tip (X,Y) $\mathbf{\tau}=\mathbf{\tau}$ coordinates; (s) $\mathbf{\tau}=\mathbf{\tau}$ text; (n) $\mathbf{\tau}=\mathbf{\tau}$ number.  

Table 123. Modeless Command and Shortcut Key Table Conventions   


| Convention | Description |
| --- | --- |
| ΛV | A variable, or something you can type. |
| {} | An optional command argument. |
| click | Click the left mouse button. |
| middle-click | Click the middle mouse button or wheel. |
| right-click | Click the right mouse button. |
| wheel forward | Rotate the wheel forward, where the top of the wheel rotates away from your palm. |
| wheel back | Rotate the wheel backward, where the top of the wheel rotates toward your palm. |  

!Tip  

Spaces have significance in modeless commands and shortcut keys. For example, SS W1 and S SW1 have different meanings. SS W1 means to search for and select W1, while S SW1 means to search for SW1.  

**Modeless Commands**

The following is a complete list of all of the modeless commands:  

Table 124. Modeless Commands for Grid Settings   


| Name | Command | Description |
| --- | --- | --- |
| Global Grid Setting | G | Sets the Design grid, for example G50. |  

Table 124. Modeless Commands for Grid Settings (continued)   


| Name | Command | Description |
| --- | --- | --- |
| Dot Grid Setting | GD | Sets the Displayed (Dot) grid, for example, GD100. |  

Table 125. Modeless Commands for 2D Line Angles   


| Name | Command | Description |
| --- | --- | --- |
| Any Angle | AA | Any angle mode. Sets the line angle for drafting objects to Any angle (no angle restrictions). |
| Diagonal Angle | AD | Diagonal angle mode. Sets the line angle for drafting objects to Diagonal (45 degree angles only). |
| Orthogonal Angle | AO | Orthogonal angle mode. Sets the line angle for drafting objects to Orthogonal (90 degree angles only). |  

Table 126. Modeless Commands for Line Width Settings   


| Name | Command | Description |
| --- | --- | --- |
| Set Minimum (Real) Display Width for Paths | R | Sets the minimum (Real) display width for paths. |
| Change Current Line Width | W | Changes the current line width to the number you enter, for example W 5. |  

Table 127. Modeless Commands for Searching   


| Name | Command | Description |
| --- | --- | --- |
| Search Absolute | S | Search absolute. Moves the pointer to the specified X and Y coordinates, for example S 1000 1000. |
| Search for Named Item (Pin/Part/Net) | S | Search for named item (pin, part or net), for example SU1. |
| Search Relative | SR | Search relative. Moves the pointer by the specified X and Y offset, for example SR -100 -50. |
| Search Relative X | SRX | Search relative X at current Y. Moves the pointer by the specified X offset, for example SRX 300. |
| Search Relative Y | SRY | Search relative Y at current X. Moves the pointer by the specified Y offset, for example SRY 400. |  

Table 127. Modeless Commands for Searching (continued)   


| Name | Command | Description |
| --- | --- | --- |
| Absolute Move to , Current Y | SX | Search absolute X at current Y. Moves the pointer to the specified X coordinate and the current Y coordinate, for example SX 300. |
| Absolute Move to , Current X | SY | Search absolute Y at current X. Moves the pointer to the specified Y coordinate and the current X coordinate, for example SY 400 |  

Table 128. Modeless Commands for Drafting Shape Control   


| Name | Command | Description |
| --- | --- | --- |
| Circle shape draw mode. | HC | Sets drawing mode to circle shape. |
| Path shape draw mode. | HH | Sets drawing mode to path shape. |
| Polygon shape draw mode. | HP | Sets drawing mode to polygon shape. |
| Rectangle shape draw mode. | HR | Sets drawing mode to rectangle shape. |  

Table 129. Modeless Commands for Measurement   


| Name | Command | Description |
| --- | --- | --- |
| Quick Measure | Q | Quick Measure with a dynamic ruler. Attaches a measurement line to the pointer and displays dx, dy, and hypotenuse information, depending on pointer movement. Place the pointer at the starting point, then type the “q" modeless command. Drag the pointer to create a line between the start and end point of your measurement. Snaps to the design grid when the Snap to grid is on. Measurements are gridless when Grid Snap is off. Dynamically reports delta x, delta y and delta x,y in current design units. |  

Table 130. Modeless Commands for Hierarchical Design   


| Name | Command | Description |
| --- | --- | --- |
| Hierarchical Push | HI | Invokes Hierarchical Push. |
| Hierarchical Pop | HO | Invokes Hierarchical Pop. |  

Table 131. Modeless Commands for Undo/Redo   


| Name | Command | Description |
| --- | --- | --- |
| Undo | UN | Undo |
| Redo | RE | Redo |  

Table 132. Miscellaneous Modeless Commands   


| Name | Command | Description |
| --- | --- | --- |
| Open File | F | Open file , where is the path and name of the file to open (for example, F demo.eco). |
| Select Sheet Name or Number | SH | Selects the sheet name or number you type, for example SH3. |
| Database Integrity Test |  | Runs the Database Integrity Test. |
| Help | ？ | Show Help topic. |  

Table 133. Modeless Commands for Basic Media Wizard/Log Test   


|  | Command | Description |
| --- | --- | --- |
| Basic Log Test | BLT | Basic Log Test. Opens the Log Test Dialog Box. BLT finds and runs BMW session playback media. See also Crash Detection, BMW and BLT. |
| Open Basic Media Wizard | BMW | Opens the Basic Media Wizard dialog box. · BMW records session playback media for a problematic SailWind Logic session. It can create playback media based on your last SailWind Logic session or your current session. This playback media can be replayed using the BLT modeless command. ·BMW is also a command line option. See also Crash Detection, BMW and BLT. |
| Start BMW Session Logging | BMW ON | Starts BMW session logging. |
| Stop BMW Session Logging | BMW OFF | Stops BMW session logging. |  

**Function Keys**

The following is a complete list of all of the function key command assignments:  

Table 134. Function Key Command Assignments   


| Function Key | Description |
| --- | --- |
| F1 | Open Help (context sensitive) |
| F2 | Add Connection |
| F3 | Unassigned |
| F4 | Unassigned |
| F5 | Unassigned |
| F6 | Unassigned |
| F7 | Unassigned |
| F8 | Unassigned |
| F9 | Unassigned |
| F10 | Unassigned |
| F11 | Unassigned |
| F12 | Unassigned |

Keypad Keys  

The following is a complete list of all of the keypad key command assignments:  

Table 135. Keypad Key Command Assignments   


| Keypad Keys | Description |
| --- | --- |
| (Number Keys) with NumLock On |  |
| Keypad (0) | Center the view using the pointer location |
| Keypad (1) | Redraw |
| Keypad (2) | Pans the workspace down one increment |
| Keypad (3) | Zooms out at the pointer |
| Keypad (4) | Pans the workspace left one increment |
| Keypad (5) | Starts Zoom from center |
| Keypad (6) | Pans the workspace right one increment |
| Keypad (7) | Zoom to the Sheet |
| Keypad (8) | Pans the workspace up one increment |  

Table 135. Keypad Key Command Assignments (continued)   


| Keypad Keys | Description |
| --- | --- |
| Keypad (9) | Zoom in at the pointer location |
| Keypad (.) | Starts Zoom from corner (Zoom Mode only) |
| (Command Keys) with NumLock Off |  |
| Insert | Centers the view using the pointer location |
| End | Redraw |
| Down Arrow | Moves the pointer down one design grid |
| Page Down | Zooms out at the pointer |
| Left Arrow | Moves the pointer left one design grid |
| Right Arrow | Moves the pointer right one design grid |
| Home | Zooms to the Sheet |
| Up Arrow | Moves the pointer up one design grid |
| Page Up | Zooms in at the pointer |
| Delete | Delete the selected object |  

**Shortcut Keys**

For mouseless operation, use keyboard shortcuts to start commands for selected items and change some system settings. Following are the shortcut assignments for SailWind Logic:  

Table 136. Keyboard Shortcuts for Panning, Zooming and Navigation   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Zoom to Sheet |  | Zooms to sheet. Fits the sheet border into the workspace. |
| Zoom to Sheet | Ctrl + B | Zooms to sheet. Fits the sheet border into the workspace. |
| Zoom Extents | Ctrl-Alt + E | Zooms to extents. Fits all objects in the design into the workspace. |
| Zoom Area In/Out | MMB (drag) | Zooms area in or out. Drag pointer up to zoom in. Drag pointer down to zoom out. |
| Start Zoom from Corner | Shift + MMB (Drag) | Starts Zoom from Corner. |  

Table 136. Keyboard Shortcuts for Panning, Zooming and Navigation (continued)   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Zoom to Selection | Alt + Z | Zooms to selection. Fits the selected objects into the workspace. |
| Zoom Mode On/Off | Ctrl + W | Toggles Zoom Mode On/Off. |
| Center View (Using Pointer Location) | MMB | Centers the view at the pointer. |
| Center View (Using Pointer Location) |  | Centers the view at the pointer. |
| Zoom In at Pointer (Zoom Mode) | LMB Click | Zooms in at the pointer (zoom mode). |
| Zoom Out at Pointer (Zoom Mode) | RMB Click | Zooms out at the pointer (zoom mode). |
| Zoom In at Pointer (Zoom Mode) |  | Zooms in at the pointer (zoom mode). |
| Zoom In at Pointer |  | Zooms in at the pointer. |
| Zoom Out at Pointer |  | Zooms out at the pointer. |
| Zoom In at Pointer | Ctrl + Wheel Fwd | Zooms in at the pointer. |
| Zoom Out at Pointer | Ctrl + Wheel Back | Zooms out at the pointer. |
| Move Pointer Down (One Design Grid) |  | Pointer moves down one design grid. |
| Move Pointer Up (One Design Grid) |  | Pointer moves up one design grid. |
| Move Pointer Left (One Design Grid) |  | Pointer moves left one design grid. |
| Move Pointer Right (One Design Grid) |  | Pointer moves right one design grid. |
| Dynamic Panning | Alt + MMB (Drag) | Pans the sheet area below the pointer to the center of the workspace. |
| Pan Workspace Down (One Line) | Wheel Back | Pans workspace down one line. |
| Pan Workspace Up (One Line) | Wheel Fwd | Pans workspace up one line. |
| Pan Workspace Right (One Line) | Shift + Wheel Back | Pans workspace right one line. |
| Pan Workspace Left (One Line) | Shift + Wheel Fwd | Pans workspace left one line. |  

Table 136. Keyboard Shortcuts for Panning, Zooming and Navigation (continued)   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Pan Workspace Down (One Pixel) | Ctrl-Alt + Wheel Back | Pans workspace down one pixel. |
| Pan Workspace Up (One Pixel) | Ctrl-Alt + Wheel Fwd | Pans workspace up one pixel. |
| Pan Workspace Right (One Pixel) | Alt-Shift + Wheel Back | Pans workspace right one pixel. |
| Pan Workspace Left (One Pixel) | Alt-Shift + Wheel Fwd | Pans workspace left one pixel. |  

Table 137. Keyboard Shortcuts for Selection   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Filter | Ctrl-Alt + F | Opens the Selection Filter. |
| Select | LMB Click | Selects an object. |
| Select |  | Selects an object. |
| Select All | Ctrl + A | Selects all objects on the current sheet based upon the selection filter choices. |
| Select All on Schematic | Ctrl-Shift + A | Selects all objects on the schematic based upon the selection filter choices. |
| Area Select | LMB (Start Drag) | Starts an area selection. |
| Area Complete | LMB (End Drag) | Completes an area selection. |
| Cancel Area Selection | LMB (Cancel Drag) | Cancels area selection. |
| Toggles/Multiple Selection | Ctrl + LMB Click | Toggles object selection or selects multiple objects. |
| Duplicate | Ctrl + LMB (Drag) | Duplicates selected object and attaches to pointer. |  

Table 138. Keyboard Shortcuts for File Operations   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Create New Design File (Blank) | Ctrl + N | Creates a new blank design file. |
| Open File (Design) | Ctrl +O | Opens a design file. |
| Print/plot | Ctrl + P | Print/plot |  

Table 138. Keyboard Shortcuts for File Operations (continued)   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Save (Quick Save) | Ctrl + S | Saves the design file |  

Table 139. Keyboard Shortcuts for Opening Menus and Dialog Boxes   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Open File Menu | Alt + F | Opens the File menu. |
| Open Edit Menu | Alt +E | Opens the Edit menu. |
| Open View Menu | Alt + V | Opens the View menu. |
| Open Setup Menu | Alt + S | Opens the Setup menu. |
| Open Tools Menu | Alt + T | Opens the Tools menu. |
| Open Help Menu | Alt + H | Opens the Help menu. |
| Open Shortcut Menu | RMB | Opens the Shortcut menu. |
| Toggle Menu Bar | Ctrl-Alt + M | Toggles the visibility of the Menu Bar. |
| Properties (Current Object) | LMB DblClick | Displays Properties for the currently selected object. |
| Properties (for Selected) | Alt+ | Displays Properties for the currently selected object. |
| Properties (for Selected) | Ctrl + Q | Displays Properties for the currently selected object. |
| Options | Ctrl + | Opens the Options dialog box. |
| Options | Ctrl-Alt + G | Opens the Options dialog box. |
| Display Colors | Ctrl-Alt + C | Opens the Display Colors dialog box. |
| Status Window | Ctrl-Alt + S | Opens the Status Window. |  

Table 140. Keyboard Shortcuts for Placement Operations   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Move Selected Object(s) | Ctrl + E | Moves the selected object(s). |
| Rotate Selected (90) | Ctrl + R | Rotates the selected object (90 degrees) |
| Flip Selected on X Axis | Ctrl + F | X Mirror (flips selected object on X axis). |  

Table 140. Keyboard Shortcuts for Placement Operations (continued)   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Flip Selected on Y Axis | Ctrl-Shift + F | Y Mirror (flips selected object on Y axis) |
| Draw Group While in Move Group Mode | Ctrl-Shift + D | Draw Group while in Move Group Mode. |
| Vertically Justify Text During Move | Ctrl-Shift + J | Vertically justify text during move. |
| Horizontally Justify Text During Move | Ctrl + J | Horizontally justify text during move. |
| Connect to Layout for Cross-Probing | Ctrl-Shift + O | Connect to Layout for cross-probing. |  

Table 141. Keyboard Shortcuts for Connection Operations   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Add Corner | LMB Click | Adds a new connection corner. |
| Add Corner |  | Adds a new connection corner. |
| Backup |  | Removes the last connection corner on a connection line or the last corner on a 2D line (in polygon or path drawing mode). |
| Complete Bus |  | Completes the bus. |
| Complete Bus | LMB DblClick | Completes the bus. |
| Rename | Ctrl + L | Rename. |
| Reset DxDy | Crtl + | Reset delta coordinates to measure from current position. |
| Add Ground Symbol | Ctrl + | Adds a Ground Symbol while in Add Connection mode. |
| Add Power Symbol | Shift + | Adds a Power Symbol while in Add Connection mode. |
| Add Off-page Symbol | Alt + | Add an Off-page Symbol while in Add Connection mode. |
| Cycle Alternate Gate Decals | Ctrl + | Cycles through alternate gate decals. |  

Table 142. Keyboard Shortcuts for Editing   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Cut | Ctrl + X | Cut |
| Copy | Ctrl + C | Copy |
| Paste | Ctrl + V | Paste |
| Redraw |  | Redraw |
| Redraw | Ctrl + D | Redraw |
| Delete |  | Delete |
| Cancel |  | Cancel |
| Redo | Ctrl + Y | Redo |
| Undo | Ctrl + Z | Undo |  

Table 143. Keyboard Shortcuts for Viewing   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Next View | Alt + N | Displays the next view. |
| Previous View | Alt + P | Displays the previous view |  

Table 144. Mouse Button Substitutions   


| Name | Shortcut Keys | Description |
| --- | --- | --- |
| Activate Right Click Popup Menu (Right Mouse Button) | M | Activates the shortcut menu for the current mode. Same as right-click. |
| Left Mouse Click |  | Activates a left mouse button click (to add corners, select items, complete, etc.) at the current pointer location. |  

## Net Attributes Dialog Box

To access: Select a net $>$ right-click $>$ Attributes menu item  

Use the Net Attributes dialog box to associate information with a single net or set of nets on the schematic. Attributes are made of two parts, an attribute name and its corresponding value. If connecting to SailWind Layout, these attributes are passed along with the rest of the schematic.  

![](/images/f1a941f5c04048f2a1d78128d72b753b490e4a8d72116c66facf49df3bf6d2b8.jpg)  
Figure 88. Net Attributes Dialog Box  

**Objects**  

Table 145. Net Attributes Dialog Box   


| Name | Description |
| --- | --- |
| Attributes table | Lists the name and value of the net selected in the schematic. |
| Add button | Adds a new row below the selected row. |
| Delete button | Removes the selected row from the Attributes table. |
| Edit button | Makes the selected cell available for editing. |  

**Related Topics**  

Creating Net Attributes  

## Net Name Properties Dialog Box  

To access: Select a net name label $>$ right-click $>$ Properties menu item  

Use the Net Name Properties dialog box to provide or change text and font settings for one or more net name labels.  

![](/images/a28634d097553e9c07fecb4aa54ace56573c4c97590a785d143e42c47d22f408.jpg)  
Figure 89. Net Name Properties Dialog Box  

**Objects**  

Table 146. Net Name Properties Dialog Box Contents   


| Name | Description |
| --- | --- |
| Net Name | The name of the selected net. |
| Rename | Specifies to rename the selected net name or all instances of the net name. |
| Rotation | Specifies the rotation of the label: O or 90 degrees. |
| Size | Specifies the size of the font. Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke |  

Table 146. Net Name Properties Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | tGg Stroke Font - Size |
| Line Width | Specifies the line width for stroke fonts only. text Stroke Line Width |
| Font list | The fonts available to you. This lists either stroke fonts or system fonts. You choose which type of font to use in the Fonts Dialog Box. i Tip · Select stroke font or a system font. · For system fonts, you can also click a font style button, or any combination of styles:B for bold, I for italic, or U for |
| Horizontal/Vertical Justification | underlined. Specifies the horizontal (Right, Center, Left) justification and the vertical (Up, Center, Down) justification of the text. |  

**Related Topics**  

Modifying Part Type Labels  

## Net Properties Dialog Box  

To access: Select a net $>$ right-click $>$ Properties menu item  

Use the Net Properties dialog box to access net specific properties.  

![](/images/1e9a4911e693cd762cb95a432aaf61806c8535234d08720ce7770e4e700186fe.jpg)  
Figure 90. Net Properties Dialog Box  

**Objects**  

Table 147. Net Properties Dialog Box Contents   


| Name | Description |
| --- | --- |
| Net Name | The name of the selected net. Type or select one from the list to create a new one. |
| Rename area | Specifies to rename the selected net or all instances of the net. Selecting This Instance will cause the net to be split into two separate nets. Tip |
| Net Name Label | Specifies to add a visible label to the selected net segment. Restriction: You must select the connection segment where it enters or exits a part, or the Net Name Label check box will be unavailable. 1Tip |
| Statistics button | Displays connection information in your default text editor. |  

Table 147. Net Properties Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Attributes button | Opens the Net Attributes Dialog Box. |
| Rules button | Opens the Net Rules Dialog Box. |  

**Related Topics**  

Modifying Nets  

## Net Rules Dialog Box  

To access:  

• Setup $>$ Design Rules menu item $>$ Net button  

• Select a net $>$ right-click $>$ Show Rules menu item  

• Select a net $>$ right-click $>$ Properties $>$ Rules button  

Use the Net Rules dialog box to define design rules that apply to nets.  

![](/images/3774fee6ca8c6cea715e5681ff69d2c2706070d0e468ef581b94bb163cb51f65.jpg)  
Figure 91. Net Rules Dialog Box  

**Objects**  

Table 148. Net Rules Dialog Box   


| Name | Description |
| --- | --- |
| Nets list | Lists all nets in the design. |
| Show Nets with rules | Specifies to show only nets that have rules. |
| Clearance button | Opens the Clearance Rules Dialog Box. |
| Routing button | Opens the Routing Rules Dialog Box. |
| HiSpeed button | Opens the HiSpeed Rules Dialog Box. |
| Report button | Opens the Rules Report Dialog Box. |
| Picture below rule button | The picture below each type of rule button identifies which rules hierarchy level is used for that rule type. The meaning of the picture corresponds to the button in the Hierarchy area of the Rules dialog box For example, if you select a class in the Class list and a green polygon |  

Table 148. Net Rules Dialog Box (continued)   


| Name | Description |
| --- | --- |
|  | appears below the Clearance button, then the default values apply to the class. |
| Selected | Lists the net(s) selected in the Nets list. |
| Default button | Removes non-default rules from the selected nets, so that only default rules apply. |  

## Netlist to PCB Dialog Box  

To access: Tools $>$ Layout Netlist menu item  

Use the Netlist to PCB dialog box to create a netlist for import to SailWind Layout.  

![](/images/80b553cf14860ae3ff1562e20863721c6a2b470485b11d0085ff832cd99dc6b1.jpg)  

!Tip  

If you use both SailWind Logic and SailWind Layout on the same computer, there is a more automated method to pass the netlist. For more information, see the Send Net list button on the SailWind Layout Link Dialog Box, Design Tab.  

Restriction: Transferring non-ECO-registered parts and non-electrical parts is constrained by settings in the Options. See Options Dialog Box, Design Category on page 591 for details.  

![](/images/0984b6753fac6e052ca7de8af8a8eda1a87b892f2a84713aecaa3de85a8a9acc.jpg)  
Figure 92. Netlist to PCB Dialog Box  

**Objects**  

Table 149. Netlist to PCB Dialog Box Contents   


| Name | Description |
| --- | --- |
| Output File Name | Accept the default name, type, or browse to the location and name of the netlist (.asc) file you are creating. |
| Select Sheets area | Specifies the schematic sheets to include in the netlist. You can use the Select All and Unselect All buttons as shortcuts. |
| Include Subsheets | Specifies to include any connections to hierarchical symbols in the netlist. |
| Output Formats | Specifies to output netlists compatible with the latest or older database formats. |
| Include Design Rules | Specifies to include design rules and trace width settings in the netlist. |
| Include Part Attributes | Specifies to include part attributes in the netlist. |
| Include Net Attributes | Specifies to include net attributes in the netlist |
| TIP: Run Connectivity Report to check for possible connectivity errors | To run the Connectivity Report, in SailWind Logic, click the File > Reports menu item. In the Reports Dialog Box, select the Connectivity check box and click OK. |  

## Off-Page Properties Dialog Box  

To access: Select an off-sheet label $>$ right-click> Properties menu item Use the Off-Page Properties dialog box to set the properties of off-sheet labels.  

![](/images/ccd0d490a9cbaaf77335cc7baec4e2d47217495edb1402b52fafcf3be18f98c3.jpg)  
Figure 93. Off-Page Properties Dialog Box  

**Objects**  

Table 150. Off-Page Properties Dialog Box   


| Name | Description |
| --- | --- |
| Maximum sheet numbers per line | Enter the maximum number of sheet numbers allowed per line. |
| Rotation | Select O or 90 degrees. |  

## Options Dialog Box  

Using the Options dialog box, you can preset options for commands in SailWind Logic, setting up how those SailWind Logic commands will work and overriding the default settings in the default.txt file. Setting options enables you to set up a working environment that suits your design and the way you work.  

To access: Tools $>$ Options menu item  

Options Dialog Box, Design Category Options Dialog Box, General Category Options Dialog Box, Line Widths Category Options Dialog Box, Text Category  

### Options Dialog Box, Design Category

To access: Tools $>$ Options menu item $>$ Design category  

There are six categories of general options for the Schematic Editor; they are organized into six areas in the Design category labeled Parameters, Options, Sheet, Off-sheet Labels, Non-ECO-Registered Parts, and Non-Electrical Parts.  

![](/images/f01e60344346d140ca757aad8a191e1768a0527d745c1093b7514e3728191685.jpg)  
Figure 94. Options Dialog Box, Design  

**Objects**  

Table 151. Options Dialog Box, Design Category   


| Name | Description |
| --- | --- |
| Parameters area |  |
| Tie Dot Diameter | Specifies the diameter of tie dots. The value must be from O to 100. |
| Bus Angle Offset | Defines the starting point distance from the bus for the bus tap. The value must be from O to 250. |  

Table 151. Options Dialog Box, Design Category (continued)   


| Name | Description |
| --- | --- |
|  | Tip The bus tap joins connections to the bus. |
| Options area |  |
| Preserve Ref Des on Paste | Specifies to use a group's current reference designator assignment when possible. Tip Click to clear this check box to assign the pasted group's reference designators the first or next available number. |
| Allow Floating Connections | Specifies to create connections without terminations. Tip Click to clear this check box to prevent creating additional Floating Connections. Disabling the option does not remove existing Floating Connections. See also Working With Floating Connections. |
|  | Specifies to allow deletion of net name labels in all cases except that of a power symbol connected to a net that overrides its default net name. When this box is checked, the current net name is not changed under any circumstances. When this box is cleared, you cannot delete labels tied to bus rippers or off-page symbols. You can delete net labels tied to component pins; this causes the net to be renamed to a system-generated name, but only if both the following conditions apply: · The net is not connected to a bus or off-page symbol. · The deleted label was the only label on the net. |
| Allow overwriting of attribute values in design with blank values from library | If you change the name of a subnet with a system net name in the Net Properties dialog box, and click OK without checking the Net Labels check box, the result will be a named subnet without a label. Specifies how design attribute values should be handled by operations that change design part types, such as Update From Library, Update Selected Part Type from Library, Change Type (in the Part Type Properties dialog), ECO Import, and automated operations. |
|  | to be overwritten by a blank value from the library or other update source. · Clear it to prevent overwriting these values. |
| Sheet area Size list |  |
|  | Specifies the size sheet you want. |  

| Table 151. Options Dialog Box, Design Category (continued) |
| --- |
| Name |
| Sheet border |
| Choose button |
| Off-Sheet Labels area |
| Show Off-page Sheet Numbers |
| Separators |
| Numbers per Line |
| · The sheet numbers appear on a line below the net name. Non-ECO-Registered Parts area |
| Include in Netlist |
| Include in ECO to PCB |
| Include in BOM report |
| Non-Electrical Parts area |
| Include in Netlist |  

Table 151. Options Dialog Box, Design Category (continued)   


| Name | Description |
| --- | --- |
|  | i Tip To include a part that is both non-ECO-registered and non-electrical in a netlist, select the check boxes in both Part areas. |
| Include inECO toPCB | Specifies to include a part in the ECO file that is forwarded to the PCB. Tip To include a part that is both non-ECO-registered and non-electrical in a Forward ECO to PCB, select the check boxes in both Part areas. |
| Include in BOM report | Specifies to include a part in the Bill of Materials (BOM) report. Tip To include a part that is both non-ECO-registered and non-electrical in a BOM report, select the check boxes in both Part areas. |  

**Related Topics**  

Setting Schematic Editor Options  

### Options Dialog Box, General Category

To access: Tools $>$ Options menu item $>$ General category  

There are six categories of general options for the Schematic Editor; they are organized into six areas in the General category labeled Display, Cursor, Grids, OLE objects, Text Encoding, and Automatic Backups.  

![](/images/40313c39192f3bacb04fe95b5d8f5c24e96bd25da0d13d64f7b7efc3b4cc2ec6.jpg)  

**Objects**  

Table 152. Options Dialog Box, General Category   


| Name | Description |
| --- | --- |
| Display area |  |
| Keep view on window resize | Specifies to maintain the area view of the design when you resize the SailWind Logic window, by automatically zooming in or out. |
| Minimum display width | Specifies the minimum width, in current design units, of lines you want to draw at actual width. Lines smaller than this width are drawn only as centerlines to save memory and redraw time. |  

| SailWind Logic GUI Reference Options Dialog Box, General Category |
| --- |
| Table 152. Options Dialog Box, General Category (continued) |
| Name |
|  |
|  |
| Cursor area Style list |
|  |
|  |
|  |
|  |
|  |
|  |
| Grids area box. |
| Design |
| Labels and Text |
| Display Grid |
|  |
| Snap to Grid |
| OLE Objects area |
| Display OLE objects |
|  |
| Update on redraw |  

| Table 152. Options Dialog Box, General Category (continued) |
| --- |
| Name |
|  |
| object in a separate window and you click the Redraw button in the separate window. |
| Tip · To increase performance, disable this option. |
| · The OLE display settings affect SailWind Logic only when it is embedded in another application. |
| Specifies to draw the SailWind Logic background color in the linked or embedded SailWind Logic object. Tip |
| When this option is disabled, the background of the SailWind Logic object is transparent and you can see through the object at the container application's background. |
| Text Encoding area |
| Text Encoding list |
| Tip Encoding choices include those supported in the current localized version of SailWind Logic, plus any default encoding already in use |
| in the design. Example: A letter with a Ox20 code displays as a Latin capitol letter A with a grave accent in a design using Western encoding, and as a |
| Cyrillic capital letter A in a design with Cyrillic encoding. Restriction: The default text encoding cannot be changed. It is automatically set |
| Automatic backups area |
| Interval |
| Number of backups |
| Backup File button |
| Use design name in backup file name |
| Create backup files in design directory |  

Table 152. Options Dialog Box, General Category (continued)   


| Name | Description |
| --- | --- |
|  | Tip |
|  | Click to clear if you want your backup files in one, common backup directory. |  

**Related Topics**  

Setting Schematic Editor Options Creating a Backup File  

### Options Dialog Box, Line Widths Category

To access: Tools $>$ Options menu item $>$ Line Widths category  

Use the Line Widths category to change the size of line widths in the workspace.  

| Options |
| --- |
| General Design Line Widths Text Line Widths Lines: |
|  |
| Type |
| Bus |
|  |
|  |
|  |
|  |
|  |
| 2DItem |
|  |
|  |
|  |
| OK |  

**Objects**  

Table 153. Options Dialog Box, Line Widths Category   


| Name | Description |
| --- | --- |
| Type | Lists the types of lines available in the schematic. |
| Width | Specifies the width of the line type. |
| Edit button | Makes the Width column of the selected row editable. |  

**Related Topics**  

Setting Line Widths  

### Options Dialog Box, Text Category

To access: Tools menu item $>$ Text category  

The Text category differs depending on the selection you made in the Fonts dialog box: Stroke or System font.  

![](/images/7c738bbbc3d43255698832b18123359b1b00205d656ab5ed8b96e87a63fb43ee.jpg)  
Figure 95. Options Dialog Box, Text Page - System Font  

Figure 96. Options Dialog Box, Text Page - Stroke Font   


| Options x |
| --- |
| General Design Text LineWidths |
|  |
| Type |
| Net Name |
| Pin Number |
| Pin Name |
| Ref-Des |
| Ref-Des |
| Ref-Des |
| Part Type |
| Part Type |
| Part Type |
| Attr Label |
| Attr Label |
| Attr Label |
| Edit |
|  |
|  |
| OK |  

**Objects**  

Table 154. Options Dialog Box, Text Category   


| Name | Description |
| --- | --- |
| Type | Displays the type of font used in the schematic. |
| Font | Specifies the system font used. Restriction: System font only. |
| B | Specifies if this font is bold. Click to make the font bold; click to clear to make it regular weight. Restriction: System font only. |
|  | Specifies if this font is italicized. Click to make the font italic; click to clear to make it regular. Restriction: System font only. |  

Table 154. Options Dialog Box, Text Category (continued)   


| Name | Description |
| --- | --- |
| U | Specifies if this font is underlined. Click to underline the font; click to clear to make it regular. Restriction: |
| Size | Specifies the size of the font. Restriction: System font only. |
| Width | Specifies the width of the font. Restriction: Stroke font only. |
| Edit button | Makes the selected field editable. Restriction: You cannot edit fields in the Type column. |  

## Options Dialog Box - Part Editor, General Category  

To access: While in the Schematic Editor, click the Tools $>$ Part Editor menu item. In the Part Editor, click the Edit $>$ CAE Decal Editor menu item. In the CAE Decal Editor, click the Tools $>$ Options menu item, then click the General category.  

There are four categories of general options for the Part Editor; they are organized into four areas on the General category labeled Display, Cursor, Grids, and Text Encoding.  

![](/images/8507f9e7ff5126bf09a2f39716f5d597fd5ed19f243753733d5c11dbdc01b4a0.jpg)  

**Objects**  

Table 155. Options Dialog Box - Part Editor, General Category   


| Name | Description |
| --- | --- |
| Display area |  |
| Keep view on window resize | Specifies to maintain the area view of the design when you resize the SailWind Logic window, by automatically zooming in or out. |  

| eneralCategory |
| --- |
|  |
| Name Minimum display width |
|  |
| Cursor area Style list |
|  |
|  |
|  |
|  |
|  |
|  |
| Grids area Design |
|  |
| Labels and Text |
| Display Grid |
|  |
|  |
| Snap to Grid |
|  |
| Text Encoding area |
| Text Encoding list |  

Table 155. Options Dialog Box - Part Editor, General Category (continued)   


| Name | Description |
| --- | --- |
|  | Tip Encoding_choices include those supported in the current localized version of SailWind Logic, plus any default encoding already in use |
|  | in the design. Example: A letter with a Ox20 code displays as a Latin capitol letter A with a grave accent in a design using Western encoding, and as a Cyrillic capital letter A in a design with Cyrillic encoding. |  

**Related Topics**  

Setting Part Editor Options  

## Options Dialog Box - Print/Plot  

To access:  

• File $>$ Plot menu item $>$ Options button • File $>$ Print menu item $>$ Options button  

Use the Options dialog box to set the output options for printing or plotting. Setting options enables you to set the position, orientation, and color of selected sheets and objects.  

![](/images/e6116fce6d46e34e6865bcce4c5df56518ea8aef726716dfe70e85c368d05583.jpg)  
Figure 97. Options Dialog Box - Print/Plot  

**Objects**  

Table 156. Options Dialog Box - Print/Plot   


| Name | Description |
| --- | --- |
| Available list | Lists the available sheets to print |
| Add >> button | Moves the selected sheet to the Sheets to Print list. |
| Add All >> button | Moves all sheets to the Sheets to Print list. |  

Table 156. Options Dialog Box - Print/Plot (continued)   


| Name | Description |
| --- | --- |
| << Remove button | Moves the selected sheet to the Available list. |
| << Remove All button | Moves all sheets to the Available list. |
| Sheet to Print list | Lists off the sheets you want to print. |
| Items area | Specifies the items you want to include in your output. |
| Color Selection area | Specifies the color you want for the different items in the ltems area. Click a color tile, then in the Items area, click the tile to the right of the item to change its color. |
| Orientation | Specifies the orientation angle for the output. |
| Justification | Specifies the justification position for the output. |
| X/Y Offset | Specifies the offset values. i Tip · You can only set offsets if you clicked something other than |
| Scaling | and scaled. Specifies the type the plot size to actual size ratio. Example: A 2 to 1 scaling results in a printout or plot that is twice the actual size. |
| Preview area | Graphically shows the position, orientation, justification, and scaling of the output. |
| Plot Job Name | Specifies to output the schematic name, time, and date. |
| Plot Window | Specifies to print the displayed window. |
| Preview button | Opens the Selections Preview Dialog Box. |  

## Output Window  

Use the Output window for displaying reports and session logs, macro editing and debugging, and custom programming and debugging, as well as CIS configuration.  

To access: Click the Output Window button.  

The Output window is located in the lower left section of the display window. You can dock or float the Output window. You can also open or close the Output window.  

The Output window has three tabs described below.  

**Status Tab**

The Status tab displays information about the current session. It specifies the filename of the opened PCB file and the name of the test integrity file that is saved. It also reports routing statistics and messages when routing a board.  

If the Status tab is closed, and you get an error while autorouting - or performing other tasks - the Output window opens with the Status tab active and the error appearing in red. The Output window reappears in its most recent state (floating or docked).  

• Output Window button $>$ Status tab  

**Macro Tab**

You can edit, run, and debug macro scripts in the Macro tab. You can open multiple macros and nest macros using the macro editor.  

A macro is any combination of commands, keystrokes, and mouse clicks that you record to replay as a single action. You can record virtually any set of procedural steps for replay, thereby simplifying redundant activities, such as setting preferences and layer/display settings.  

• Output Window button $>$ Macro tab

**CIS Tab**

The CIS tab provides a graphic interface to view part information in the database, to which you connect. You can select and add parts to the design, specify the part information to display, and export database configuration.  

• Output Window button $>$ CIS tab Library Config Dialog Box Part Manager Dialog Box  

### Library Config Dialog Box

To access: Output Window $>$ CIS tab $>$ New/Edit button  

Use the Library Config dialog box to specify the database from which to load part information and specifc part information displayed in the CIS tab.  

![](/images/ee45dea154ff0bbbe8e4acc4dd5f7ce19ccf9cd5fd065df26d74f3e06372edea.jpg)  
Figure 98. Library Config Dialog Box  

**Objects**  

Table 157. Library Config Dialog Box Contents   


| Name | Description |
| --- | --- |
| ODBC DSN area: |  |
| ODBC DSN | Selects the database from which to load part information from the drop-down list. Tip |
| ODBC Config | Adds a new database. OTip Click Update to make the newly added database available. |
| Update | Makes the newly added database available in the ODBC DSN drop-down list. |
| Database Tables area |  |
| To CIS | Specifies database table(s) to display in the Cis tab. |  

Table 157. Library Config Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Table Name | Displays all the table(s) in the selected database. |
| Table Configuration area |  |
| Field Name | Lists all fields in the table selected on the left. |
| Field Type | Specifies what type the table fields belong to from the drop-down list, wherein: · Part_Type is mandatory, based on which to load data into the CIS tab. Besides, you can see schematic symbol and PCB decal assigned to the part type in the local libraries from the CiS preview window. · Part_Number is mandatory, based on which to check whether part attribute values in design are identical with those in CIS. · Category allows to show table structure hierarchically by |
| Field Alias | Specifies the table heading for each field to display in the Cis tab. · Field aliases corresponding to Field Type "Part_Type" and "Part_Number" are defined by default, and no modification is allowed. · If nothing is set, Field Name will be used instead. |
| Transfer to Design | Specifies to add the Field Name to the part attributes. If yes, you can see it in the Part Attributes list by checking part properties in the design. Tip When set, Field Alias will be used instead. |
| Visibility in CIS | Specifies to display Field Name in the Cls tab. When set, Field Alias will be used instead. |
| Key | Reserved |
| Browsable | Specifies to add hyperlinks to the field contents in the Cis tab, which often links to such reference files as datasheets and drawings. |
| Property Checking | Specifies attribute(s) to compare for consistency checking in the Part ManagerDialogBox. Tip No checkbox selected means comparing all attributes by default. |  

### Part Manager Dialog Box

To access: Output Window $>$ CIS tab $>$ Part... button  

Use the Part Manager dialog box to compare part attributes in design with those in CIS for consistency checking. For the inconsistent attribute values, you can update from CIS with multiple options.  

![](/images/66f769750368c45c8bd170d7be1eb8cfed15da3338187cda61c2fea9496a0777.jpg)  
Figure 99. Part Manager Dialog Box  

**Objects**  

Table 158. Part Manager Dialog Box Contents   


| Name | Description |
| --- | --- |
| Filter area | · Specifies the search filter. Note that filtering by Component Name or Part Number is case-sensitive and no wildcard or expression is currently supported. ·Provides functionality buttons as follows: |
|  | ·Filter: Used to activate the filter · Clear: Used to reset the search filter settings · Show Error Only: Used to show parts found with errors |
| Part Attribute Info. area | Displays the search result. |
|  | For schematic parts whose attributes are not identical with those in CIS, they are highlighted in red. |
| Update the Selected button | Updates the incosistent attributes of the selected schematic part(s) |
|  | from CIS. Takes effect only on schematic parts found with "Atribute is not |
| Update All button | equal" error. Updates incosistent attributes of all schematic parts found with |  

Table 158. Part Manager Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Refresh button | Manually updates the comparision result if you change part attributes in the design. |
| Comparision Results area | Displays what assigned to the part attributes in design and CIS respectively, with differences highlighted in red. You can: · Update the selected attribute: Right-click on the attribute cell and click the Update Selected Attribute From CiS popup menu item · Update all attributes of the schematic part: Right-click and click the Update Selected Part From CIS popup menu item |  

## SailWind Layout Link Dialog Box  

The SailWind Layout Link dialog box enables you to connect to SailWind Layout to automate sending the netlist and passing design change annotations, and cross-probe (receive and send selections). This feature also automates certain tasks for you, such as netlist comparisons and rules exports. Once you connect to SailWind Layout, you can select objects in SailWind Layout and the object is automatically selected and shown on its SailWind Logic schematic sheet (and vice versa).  

See also Cross-Probe Between Sailwind Products.

The options you set in the SailWind Layout Link dialog box are saved to the registry. These options are restored the next time you open the SailWind Layout Link.  

![](/images/bab43452945c567f67eed36674a8d0f4c6980fb2d4758018d4c8835ee4ad1787.jpg)  

!Note:  

The exception is the selection made in the Sent Selection list on the Selection tab, and the document pathname on the Document tab.  

SailWind Layout Link dialog box tabs:  

SailWind Layout Link Dialog Box, Design Tab SailWind Layout Link Dialog Box, Document Tab SailWind Layout Link Dialog Box, ECO Names Tab SailWind Layout Link Dialog Box, Preferences Tab SailWind Layout Link Dialog Box, Selection Tab  

### SailWind Layout Link Dialog Box, Design Tab

To access: Tools $>$ SailWind Layout menu item $>$ connect to SailWind Layout using the Connect to SailWind Layout Dialog Box $>$ Design tab  

Use the Design tab of the SailWind Layout Link dialog box to export a netlist to SailWind Layout, compare the schematic to the layout design, or forward and backward annotate design data.  

![](/images/eeb012b31d18e794f3018c510236dd4c20ab314be16b4fd63cd9218a7aa70305.jpg)  

**Objects**  

Table 159. SailWind Layout Link Dialog Box, Design Tab Contents   


| Name | Description |
| --- | --- |
| Net list area |  |
| Send Netlist button | Exports a netlist from the current schematic to the current SailWind Layout design. |
| Results: |  |
| · If no errors are found in the netlist, SailWind Layout is updated. · If errors are found in the netlist, the error report file is displayed in |  |
| a Notepad window, a link to the error file is displayed in the Output Window, and you are asked whether you want to continue. · If you click Yes, SailWind Layout is updated. · If you click No, the operation is canceled and SailWind Layout is not |  |
| Netlist check box |  |  

| Table 159. SailWind Layout Link Dialog Box, Design Tab Contents (continued) |
| --- |
| Name |
| Compare/ECO area |
| Compare PCB button |
|  |
|  |  

Table 159. SailWind Layout Link Dialog Box, Design Tab Contents (continued)   


| Name | Description |
| --- | --- |
|  | · If errors are found in either of the netlists, the error report file is displayed in a Notepad window, a link to the error file is displayed in the Output Window, and you are asked whether you want to continue. · lf you click Yes, the SailWind Logic schematic is updated. · If you click No, the operation is canceled, and SailWind Logic is not updated. See also SailWind Layout Link Dialog Box, Preferences Tab, SailWind |
| Compare Design Rules check box | Layout Link Dialog Box,ECO Names Tab. Includes design rules in the comparison that occurs when you select Compare PCB, ECO to PCB, or ECO from PCB. |
| Show Net List errors report check box | Select the check box to open the Net List errors report once it has been generated. The filename is padsnet.err. Tip |
| Al layout reference data | If you clear the check box, you can still open the file from the link in the Output window. Select the check box in order for the Al Intelligent Layout feature to work in |
| Disconnect button | SailWind Layout. Breaks the connection with SailWind Layout and closes the dialog box. |  

**Related Topics**  

SailWind Layout Link Dialog Box  

### SailWind Layout Link Dialog Box, Document Tab

To access: Tools $>$ SailWind Layout menu item $>$ connect to SailWind Layout using the Connect to SailWind Layout Dialog Box $>$ Document tab  

Use the Document tab of the SailWind Layout Link dialog box to open and connect to a different design or a new design file within the current SailWind Layout session. The current design path and filename is listed at the top of this tab.  

![](/images/cabd93c91f70a126870005ed207cdba58a2c25399dfaaffacb1e4fb1c7be2028.jpg)  

**Objects**  

Figure 100. SailWind Layout Link Dialog Box, Document Tab   
Table 160. SailWind Layout Link Dialog Box, Document Tab Contents   


| Name | Description |
| --- | --- |
| Pathname field | Displays the path and filename of the current SailWind Layout design. |
| New button | Creates a new file within the current SailWind Layout session. SailWind Logic automatically connects to this file. |
| Tip If the current SailWind Layout design has unsaved changes, a prompt window appears, asking, "Remote PCB document is modified - Do you want to save it?". |  |
| Open button | Enables you to locate and open an existing SailWind Layout file. SailWind Logic automatically connects to this file. Tip If the current SailWind Layout design has unsaved changes, a prompt window appears, asking, "Remote PCB document is modified - Do you want to save it?". |
| Disconnect button | Breaks the connection with SailWind Layout and closes the dialog box. |  

**Related Topics**  

SailWind Layout Link Dialog Box  

### SailWind Layout Link Dialog Box, ECO Names Tab

To access: Tools $>$ SailWind Layout menu item $>$ connect to SailWind Layout using the Connect to SailWind Layout Dialog Box $>$ ECO Names tab  

Use the ECO Names tab of the SailWind Layout Link dialog box to manage options for the compare and ECO functions on the Design tab.  

Note: See also Design tab on page 614.  

![](/images/1f15c0a8ccefb344090ee6deeb599dd4acf88d128d712c089fb6fa52e2956202.jpg)  
Figure 101. SailWind Layout Link Dialog Box, ECO Names Tab  

**Objects**  

Table 161. SailWind Layout Link Dialog Box, ECO Names Tab Contents   


| Name | Description |
| --- | --- |
| Compare Names and Rename Nets and Parts as Necessary | Compare differences using reference designators and net names. Tip ·Best used to minimize changes to routed traces. · Selecting this option may result in the positional swapping of parts. |
| Compare Names but Prefer Add/Delete Parts to Renaming | Compare differences using reference designators and net names on the basis that few reference designators have been renamed and nets have not been renamed. Tip Best used to minimize the positional swapping of parts, and the design disruption that may result. |
| Compare Topology (not names). Rename as Necessary. | Compare differences without using reference designators or net names. Compare differences using pin names, part type names, and so on. |  

Table 161. SailWind Layout Link Dialog Box, ECO Names Tab Contents (continued)   


| Name | Description |
| --- | --- |
|  | 1 Tip Best used to compare designs when parts and nets have been renamed, and minimal interconnect changes have been performed. For example, only an auto renumber has been |
| Disconnect button | performed on the design. Breaks the connection with SailWind Layout and closes the dialog box. |  

**Related Topics**  

SailWind Layout Link Dialog Box  

### SailWind Layout Link Dialog Box, Preferences Tab

To access: Tools $>$ SailWind Layout menu item $>$ connect to SailWind Layout using the Connect to SailWind Layout Dialog Box $>$ Preferences tab  

Use the Preferences tab of the SailWind Layout Link dialog box to manage options for the compare and ECO functions on the Design tab.  

Note: See also Design tab on page 614.  

![](/images/535ece359b86efd767db96048dc70dc3e5b61ee4eaea09a4bb557dab58be25c4.jpg)  
Figure 102. SailWind Layout Link Dialog Box, Preferences Tab  

**Objects**  

Table 162. SailWind Layout Link Dialog Box, Preferences Tab Contents   


| Name | Description |
| --- | --- |
| Ignore Unused Pins Net check box | Select to ignore the unused pins net in the original design and preserve the existing unused pins net in the design you're updating. \ 1 Tip • If you clear this option, the unused pins net may be deleted. · The unused pins net contains pins that have no logical net association. |
| Name box | · An unused pins net may be created by other software tools in the PCB design process. Type the name of the unused pins net. Restriction: This box only becomes available if you select the lgnore Unused Pins |  

Table 162. SailWind Layout Link Dialog Box, Preferences Tab Contents (continued)   


| Name | Description |
| --- | --- |
|  | Tip · The maximum netname length is 47 characters. · You can use any alphanumeric characters except curly braces{}, |
| Include Attributes area | · The default name is NOT_CONNECTED. Parts —— Controls whether part attributes are included in the netlist. SailWind Logic evaluates parts that have different attributes as different part types. Therefore, if you select Include Part Attributes when you generate the netlist, you must also select Include Part Atributes when you perform an ECO comparison. Otherwise the comparison considers the part types to be different and reports errors. Nets — Controls whether net attributes are included in the netlist. |
| Compare PCB Decal Assignments | types to be different and reports errors. Compares PCB decal assignments between the schematic and the design in SailWind Layout. Updates decal assignments in SailWind Layout. |
| Disconnect button | Breaks the connection with SailWind Layout and closes the dialog box. |  

### SailWind Layout Link Dialog Box, Selection Tab

To access: Tools $>$ SailWind Layout menu item $>$ connect to SailWind Layout using the Connect to SailWind Layout Dialog Box $>$ Selection tab  

Use the Selection tab of the SailWind Layout Link dialog box to manage the selections sent to and received from SailWind Layout.  

![](/images/aa278590bef34574eb12cc49e0687b82bb1d7d1f518e62fa0045ec690d06a5a6.jpg)  
Figure 103. SailWind Layout Link Dialog Box, Selection Tab  

**Objects**  

Table 163. SailWind Layout Link Dialog Box, Selection Tab Contents   


| Name | Description |
| --- | --- |
| Sent Selection list | Contains a list of the objects currently selected in SailWind Logic. |
| Receive Selections check box | Select to enable the SailWind Logic to automatically locate the item corresponding to the SailWind Layout selection by changing schematic sheets and selecting the item in SailWind Logic. |
| Disconnect button | Breaks the connection with SailWind Layout and closes the dialog box. |  

**Related Topics**  

SailWind Layout Link Dialog Box  

## SailWind Router Link Dialog Box  

You can link to and cross-probe with SailWind Router using the SailWind Router Link dialog box. This function enables you to receive and send selections and start a new SailWind Router session or document. Once you connect to SailWind Router, you can select objects in SailWind Router and the object is automatically selected and shown on its SailWind Logic schematic sheet (and vice versa).  

See also “Cross-Probe Between Sailwind Products” on page 324.  

SailWind Router Link dialog box tabs:  

SailWind Router Link Dialog Box, Document Tab SailWind Router Link Dialog Box, Selection Tab  

### SailWind Router Link Dialog Box, Document Tab

To access: Tools $>$ SailWind Router menu item $>$ connect to SailWind Router using the Connect to SailWind Router Dialog Box $>$ Document tab  

Use the Document tab of the SailWind Router Link dialog box to open and connect to a different design or a new design file within the current SailWind Router session. The current design path and filename is listed at the top of this tab.  

![](/images/fbfec515a10c52a86fc00370cf557c7faf54e9aed09ab0dc9b7453498dcaf16e.jpg)  
Figure 104. SailWind Router Link Dialog Box, Document Tab  

**Objects**  

Table 164. SailWind Router Link Dialog Box, Document Tab Contents   


| Name | Description |
| --- | --- |
| Pathname field | Displays the path and filename of the current SailWind Router design. |
| New button | Creates a new file within the current SailWind Router session. SailWind Logic automatically connects to this file. |
| O Tip If the current SailWind Router design has unsaved changes, a prompt window appears, asking, “Remote PCB document is modified - Do you want to save it?". |  |
| Open button | Enables you to locate and open an existing SailWind Router file. SailWind Logic automatically connects to this file. i Tip |
| If the current SailWind Router design has unsaved changes, a prompt window appears, asking,“Remote PCB document is modified - Do you want to save it?". |  |
| Disconnect button | Breaks the connection with SailWind Router and closes the dialog box. |  

**Related Topics**  

SailWind Router Link Dialog Box  

### SailWind Router Link Dialog Box, Selection Tab

To access: Tools $>$ SailWind Layout menu item $>$ connect to SailWind Router using the Connect to SailWind Router Dialog Box $>$ Selection tab  

Use the Selection tab of the SailWind Router Link dialog box to manage the selections sent to and received from SailWind Router.  

![](/images/90b6cfb529bfc299d05ff9e6bc3fb7ecdedd0efbd4b8228d7a250d9af7560aa9.jpg)  
Figure 105. SailWind Router Link Dialog Box, Selection Tab  

**Objects**  

Table 165. SailWind Router Link Dialog Box, Selection Tab Contents   


| Name | Description |
| --- | --- |
| Sent Selection list | Contains a list of the objects currently selected in SailWind Logic. |
| Receive Selections check box | Select to enable the SailWind Logic to automatically locate the item corresponding to the SailWind Router selection by changing schematic sheets and selecting the item in SailWind Logic. |
| Disconnect button | Breaks the connection with SailWind Router and closes the dialog box. |  

**Related Topics**  

SailWind Router Link Dialog Box  

## SailWind Suite Configuration Dialog Box  

To access:  

• Help $>$ Installed Options menu item $>$ Suite Configuration button • Optional: Opens on program startup the SailWind Suite Configuration dialog box to manage SailWind Suite (composite) licenses.  

SailWind Suite Configuration

![](/images/f90526d8a601480943a0d651c5650f69cb566c5f0f0deace8968528a097c3371.jpg)  

![](/images/aa93fdb78a2337471cfca336f5240cc643c0bc72be591d1daca0bff4584ea9d5.jpg)  

**Objects**  

| Field | Description |
| --- | --- |
| Control suite license checkout and select from the following list | Enables the Suite License table for you to control checkouts. |
| Suite Name column | Lists the name of the suite for which the license works. |
| License Feature column | Lists the specific features available for each license. |
| License status column | Lists the status of the licenses when you click the Check status button. |
| Check Status button | Specifies to check the status of all licenses listed in the table and displays the status in the License status column. |  

| Field | Description |
| --- | --- |
| Reset List button | Specifies to reset the list of suite licenses to only those detected in your licensing environment. |
| Move up button | Moves the selected license up one row. |
| Move down button | Moves the selected license down one row. |
| Select all button | Selects all of the listed licenses. |
| Select none button | Deselects all of the listed licenses. |
| Show this dialog box on program startup | Specifies to open the SailWind Suite Configuration dialog box when SailWind Layout starts. |
| Automatically check license status on dialog box startup | Specifies to check the status of the licenses when you open the SailWind Suite Configuration dialog box. |  

## Part Attributes Dialog Box

To access: Select a part $>$ right-click $>$ Attributes menu item  

Use the Part Attributes dialog box to assign or modify part attributes, which is information about the part such as manufacturer and cost.  

![](/images/dcd60d0867a20d222f9a2e4acfff51c685840451fe61d8ae00a931334853e793.jpg)  

!Tip  

Adding or changing attributes in a part at the schematic level does not update the part type (in the library). Edit the part in the Part Editor to update the library part.  

![](/images/d6c1a488a629cfe73b8833b05c4fc1d4f92d4ab266e4cc033a03ed8497c0dcf9.jpg)  
Figure 106. Part Attributes Dialog Box  

**Objects**  

Table 166. Part Attributes Dialog Box Contents   


| Name | Description |
| --- | --- |
| Attributes table | Lists the name and value of the attributes of the selected part. |
| Browse Lib Attr button | Opens the Browse Library Attributes Dialog Box. |
| Add button | Adds a row to the end of the Attributes table where you can add a new attribute. |
| Delete button | Removes the selected row from the Attributes table. |
| Edit button | Makes the selected cell available for editing. |
| Apply update to area | Specifies how parts are updated: |
| · This Part — Only updates the selected part. |  |
| · All Parts This Type —— Updates all matching parts in the design |  |  

## Part Information Dialog Box  

Use the part information dialog box to create or edit part types.  

Part Information dialog box tabs:  

Part Information Dialog Box, Attributes Tab Part Information Dialog Box, Connector Tab Part Information Dialog Box, Gates Tab Part Information Dialog Box, General Tab Part Information Dialog Box, PCB Decals Tab Part Information Dialog Box, Pin Mapping Tab Part Information Dialog Box, Pins Tab  

### Part Information Dialog Box, Attributes Tab

To access: Tools $>$ Part Editor menu item $>$ Edit Electrical button $>$ Attributes tab  

Use the Attributes tab of the Part Information dialog box to manage attributes for the selected part, and to define default attributes for new parts.  

![](/images/0169f7a2ce7ff01c3d62e65de6c7d77a3cd150fd90b88365bf2f15b2ecc1564a.jpg)  
Figure 107. Part Information Dialog Box - Attributes Tab  

**Objects**  

#Table 167. Part Information Dialog Box - Attributes Tab Contents  

| Name | Description |
| --- | --- |
| Attribute table | · Attribute column — The name of the Attribute. · Value column — The value of the Attribute. |
| Save As Default button | Saves the current attribute list as the default for all new attributes. 1Tip The Attribute name is saved, but not the Attribute value. |
| Reset button | Undoes all changes you made in the Attributes tab. |
| Edit button | Makes the selected cell available for editing. |  

Table 167. Part Information Dialog Box - Attributes Tab Contents (continued)   


| Name | Description |
| --- | --- |
|  | Result: The attribute is edited for only the selected part. To manage attributes_design-wide or in all libraries, use the Manage Library Attributes Dialog Box. Tip You can also double-click a cell to edit its contents. See also Managing Attributes. |
| Add button | Adds a new row for a new attribute at the bottom of the table. Result: The new attribute is added to the Part Type Level of the attribute hierarchy. For more information, see Attribute Hierarchy in the SailWind Layout Guide. O Tip |
| Delete button | double-click in the value field to type the value. Removes the selected row. |
| Copy button | Places the selected cell information in the paste buffer. O Tip You can also copy from Microsoft Excel. |
| Paste button | Pastes the information from the paste buffer. The selected cell in the table is the paste origin. Data is pasted below and to the right of the paste origin. |
| Browse Lib. Attr button | Opens the Browse Library Attributes Dialog Box where you can browse for an existing library attribute. |
| Check Part button | Checks for missing or inconsistent information. OTip Even if you don't click the Check Part button, when you exit |

Related Topics Managing Attributes  

### Part Information Dialog Box, Connector Tab

To access: Tools $>$ Part Editor menu item $>$ Edit Electrical button $>$ Connector tab  

Use the Connector tab to define the alternate Logic decals to display in a schematic. Decals are referred to as Special Symbols. You can associate a logical Pin Type with each alternate so that you can have a graphical indication of the connector pin function in the schematic.  

![](/images/3aaa2286ce0b958f3c26e7005bcde16b704545d147ba83362f61434a74adbd3f.jpg)  

**Restriction:**  

The Connector tab is available only when you open an existing connector or create a new connector.  

![](/images/3a99111983435e8f21d04bbccafdb2038ad6522518212a920e256747d29a8b92.jpg)  

Tip Many users like to use a different symbol, or decal, to distinguish between input (Source) and output (Load) pins. You may define multiple symbols for each of the ten different pin types.  

![](/images/8ad420479af4e162ea2d53f000839015a98d6522138e4c472d7bdcbaa8e2bc30.jpg)  
Figure 108. Part Information Dialog Box - Connector Tab  

**Objects**  

Table 168. Part Information Dialog Box - Connector Tab Contents   


| Name | Description |
| --- | --- |
| Picture | Displays a picture of the selected Special Symbol. |
| Attribute table | · Special Symbol — The name of a connector pin decal for use in the schematic. · Pin Type — The function of the special symbol. |
| 口 | Opens.the Browse for Special Symbols Dialog Box where you can browse for a pin decal. |
| Reset button | Undoes all changes you made in the Connector tab. |
| Edit button | Makes the selected cell available for editing. Tip You can also double-click the cell to edit the contents. |
| Add button | Adds a new row at the bottom of the table. |
| Delete button | Removes the selected row. |
| Check Part button | Checks for missing or inconsistent information. 1Tip Even if you don't click the Check Part button, when you exit the tab, |  

**Related Topics**  

Assigning Alternate Logic Decals for Connector Symbols

### Part Information Dialog Box, Gates Tab

To access: Tools $>$ Part Editor menu item $>$ Edit Electrical button $>$ Gates tab  

Use the Gates tab of the Part Information dialog box to assign gate information to a part, including the number of gates, gate swap information, and CAE Decals for the part.  

Tip A space and a period (.) are illegal characters for pin names.  

![](/images/a0ad727c64b04a2162d809c49af11fff28a0816de7179fe663a5c7a25a39f4fd.jpg)  
Figure 109. Part Information Dialog Box - Gates Tab  

**Objects**  

Table 169. Part Information Dialog Box - Gates Tab Contents   


| Name | Description |
| --- | --- |
| Preview area | Shows the item selected in the Decal cell. |
| Reset button | Undoes all changes you made in the Gates tab. |
| Edit button | Makes the selected cell available for editing. Also displays the Browse button. |  

Table 169. Part Information Dialog Box - Gates Tab Contents (continued)   


| Name | Description |
| --- | --- |
|  | Opens the Assign Decal to Gate Dialog Box. OTip This button is available only in the CAE Decal columns, and only when the cell is available for editing. |
| Add button | Adds a new row with the next Gate letter at the bottom of the Gate table. |
| Delete button | Removes the selected row from the Gate table. |
| Gate table | · Gate column — Displays the letter of the gate. · Pins column — Displays the number of pins for the gate. Gate pins are added on the Pins tab. · Swap column — Displays the swap ID from O to 100. To uncross connections and facilitate routing, gates with the same swap ID (except for 0) can be swapped within a part or with another part of the same type. To disable swapping, type 0. |
|  | Checks for missing or inconsistent information. 1Tip Even if you don't click the Check Part button, when you exit the tab, the assigned decals are checked to ensure that they contain physical pin numbers for all the gate and signal pins |  

**Related Topics**  

Assigning Gates to Parts  

### Part Information Dialog Box, General Tab

To access: Tools $>$ Part Editor menu item $>$ Edit Electrical button $>$ General tab  

Use the General tab of the Part Information dialog box to view part statistics and set family information.  

![](/images/e654d2983aa986045dab1cc67759c604e17f3e2b88628e5e59c8853904f35570.jpg)  
Figure 110. Part Information Dialog Box - General Tab  

**Objects**  

Table 170. Part Information Dialog Box - General Tab Contents   


| Name | Description |
| --- | --- |
| Part Statistics area |  |
| Pin Count | Displays the total number of pins in the part. Includes gate pins, signal pins, and unused pins. If multiple decals are assigned with different pin counts, a range of smallest to largest decal pin counts |
| Decal | Displays the name of the decal, as chosen on the PcB Decals tab. |
| Gate Count | Displays how many gates exist in the part. |
| Signal Pin Count | Displays the number of signal pins in the part. |  

| Table Cohtehts (continued) |
| --- |
| Name |
| Logic Family area Logic Family list |
|  |
| Note: Beginning with PADS 9.0, die parts and flip chips are no longer |
| identified by their family designations (DlE or FLP), but instead by the Special Purpose settings on this tab. With this change, you can assign any reference designator (logic family) to a die part or flip chip without losing the special properties of these parts (such as the ability to move the part's substrate bond pads in the schematic). |
| Ref Prefix |
| Families button |
| Options area |
| Define mapping of Part Type pin numbers to 'PCB Decal |
| Restriction: The check box is unavailable once you add one or more alphanumeric decals to the part type. Remove the assigned alphanumeric decal to make the check box available. The check box also becomes available if you assign a |
| numeric decal. However, you will still need to remove the alphanumeric decal from the list to make the part valid. · You must assign a decal to use the Pin Mapping tab. · Only decals with sequential numerical pin numbers can be used with pin mapping. Enables a part to be passed between the design and schematic file |
| ECO Registered Part |
| Prefix List |  

Table 170. Part Information Dialog Box - General Tab Contents (continued)   


| Name | Description |
| --- | --- |
|  | Note: |
| Examples: |  |
| · Question mark ? in a prefix acts as a wildcard for one character. The prefix “?4" is the equivalent of “54" or “74". · lf you type "\O2" as the suffix, the edits are applied to all parts ending in 02. |  |
| Note: Warning: The contents of the Prefix List box are applied when you click OK or Save As on other tabs in the Part Information |  |
| dialog box. Identifies the part as one of the following types: |  |
|  | · Connector —— In contrast to other part types, connectors do not require a prefix list, or gate definitions. |
| Restriction: This check box is automatically selected when you create or modify connectors. It is unavailable if you open a part |  |
| other than a connector. 。This check box is unavailable when the part already has gate or pin assignments. |  |
| 。 The Gate Decals tab is unavailable when the Connector check box is selected. 。 Some Pins tab controls not applicable to connector parts are disabled. |  |
| · Die Part — See the following note. |  |
| · Flip Chip — See the following note. |  |
| Note: Beginning with PADS 9.0, die parts and flip chips are identified |  |
| by the Special Purpose settings in the Part Type rather than by the DIE and FLP logic families. With this change, any reference designator (logic family) can be assigned to a die part or flip chip. |  |
| Check Part button |  |  

**Related Topics**  

Viewing and Setting General Part Information  

### Part Information Dialog Box, PCB Decals Tab

To access: Tools $>$ Part Editor menu item $>$ Edit Electrical button $>$ PCB Decals tab  

Use the PCB Decals tab of the Part Information dialog box to assign decals, or footprints, to library parts.  

![](/images/b95cfba23744a070bfdbc3a0d061ae7439b1b52e7f7337c51a2e7738a5590b2f.jpg)  
Figure 111. Part Information Dialog Box - PCB Decals Tab  

**Objects**  

Table 171. Part Information Dialog Box - PCB Decal Tab Contents   


| Name | Description |
| --- | --- |
| Preview area | Displays the item selected in the Assigned Decals list. |
| Library list | Lists all your available libraries. Filters the Unassigned Decals list to only the selected library. |
| Filter | Searches the chosen library (or libraries) for a specific part or item name, or names that match a wildcard or expression on page 105. Type * to view all parts or items in the chosen libraries. Click Apply to search the libraries and display the search results. |
| Pin Count | Narrows down your unassigned decals list by displaying only the decals with the specified number of pins. |  

| Table 171. Part Information Dialog Box - PCB Decal Tab Contents (continued) |
| --- |
| Name |
|  |
| Show only Decals with pin numbers matching Part Type |
| Unassigned Decals list |
| Assign >> button |
| << Unassign button |
|  |
|  |
|  |
|  |  

Table 171. Part Information Dialog Box - PCB Decal Tab Contents (continued)   


| Name | Description |
| --- | --- |
| Check Part button | Checks for missing or inconsistent information. |
| iTip |  |
| Even if you don't click the Check Part button, when you exit the tab, the assigned decals are checked to ensure that they |  |
| contain physical pin numbers for all the gate and signal pins |  |
| defined in the Pins tab. |  |  

**Related Topics**  

Assigning PCB Decals  

### Part Information Dialog Box, Pin Mapping Tab

To access: Tools $>$ Part Editor menu item $>$ Edit Electrical button $>$ General tab. On the General tab, select the “Define mapping of Part Type pin numbers to PCB Decal” check box to make the Pin Mapping tab available. On the PCB Decals tab, assign a decal with sequential numerical pin numbers to use the Pin Mapping tab. The decal determines the number of pins in the part.  

Use the Pin Mapping tab of the Part Information dialog box to overlay alphanumeric pin numbers onto numeric PCB decal pins. Prior to PADS 2007, alphanumeric pin numbers could not be saved in PCB decals.  

![](/images/f30ccddfbddeb76f5650f957b1b6f93ed2ac3b79f63cb8b2cba5356f97f25fd3.jpg)  
Figure 112. Part Information Dialog Box - Pin Mapping Tab  

**Objects**  

Table 172. Part Information Dialog Box - Pin Mapping Tab Contents   


| Name | Description |
| --- | --- |
| Decal list | Lists the decals available to you for which you can map alphanumeric pins. |
| Reset button | Undoes all changes you made in the Pin Mapping tab. |
| Unmapped Pins list | Lists all unmapped pins available to map in the Mapping table. |
| Map >> button | Moves the selected pin from the Unmapped pins list to the selected cell in the Mapping table. |  

Table 172. Part Information Dialog Box - Pin Mapping Tab Contents (continued)   


| Name | Description |
| --- | --- |
| << Unmap button | Moves the selected decal number from the Mapping table to the Unmapped Pins list. |
| Mapping table | · Decal column — The number of the Decal. · Part Type column — The value of the Attribute. |
| Edit button | Makes the selected cell available for editing. Tip You can also double-click the cell to edit the contents. |
| Copy Map button | Places the map information into the paste buffer to paste into Microsoft Excel where you can make mass edits. Restriction: Copy Map only works with the whole pin mapping table and |
| Paste Map button | not selective rows. Pastes the map information from the paste buffer. Restriction: Paste Map only works with the whole pin mapping table and |
| Preview area | Shows the item selected in the Decal list. You can assign unmapped pins to decal pins by selecting the pins in the preview window. Select an alphanumeric in the Unmapped Pins list and double-click the pin in the decal preview window to map the alphanumeric to the pin. The next row in the Unmapped Pins list becomes the next selected alphanumeric for mapping. In the preview window, you can click and drag to define a zoom box, or use Shift+click or Shift+right-click to zoom in or out by a |
| Check Part button | Checks for missing or inconsistent information. Tip Even if you do not click the Check Part button, when you exit the tab, the assigned decals are checked to ensure that they |  

**Related Topics**  

Part Information - Pin Mapping  

### Part Information Dialog Box, Pins Tab

To access: Tools $>$ Part Editor menu item $>$ Edit Electrical button $>$ Pins tab  

Use the Pins tab of the Part Information dialog box to assign gate pins, signal pins, and unused pins to the part. Pin numbers added to the Pins tab, must match those of the PCB Decal. Use the Pin Mapping tab to overlay logical (schematic) alphanumeric pin numbers onto the physical numeric PCB decal.  

PartInformation forPart-CD4001B

General PCB Decals Gates Pins Attributes  

Tip: Multiple values in one column can be edited at once by using the Edit button.  

| Pin Group | Number | Name | Type |  | Swap | Seq. | Reset |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gate-A | 1 |  | Load | 1 | 1 |  |  |
| Gate-A | 2 |  | Load | 1 | 2 | Edit |  |
| Gate-A | 3 |  | Source | 0 | 3 |  |  |
| Gate-B | 5 |  | Load | 1 | 1 | Add Pin |  |
| Gate-B | 6 |  | Load | 1 | 2 |  | Add Pins.. |
| Gate-B | 4 |  | Source | 0 | 3 |  |  |
| Gate-C | 8 |  | Load |  | 1 | 1 | Delete Pins |
| Gate-C | 9 |  | Load | 1 | 2 |  |  |
| Gate-C | 10 |  | Source |  | 0 | 3 | Renumber... |
| Gate-D | 12 |  | Load | 1 | 1 |  |  |
| Gate-D | 13 |  | Load |  | 1 | 2 | Copy |
| Gate-D | 11 |  | Source | 0 |  | 3 |  |
| Signal Pin | 7 | GND |  |  |  |  | Paste |
| Signal Pin | 14 | +5V |  |  |  |  |  |
|  |  | Import CSV |  |  |  |  |  |
| Check Part OK | Cancel |  |  |  |  |  |  |  

**Objects**  

| Name | Description |
| --- | --- |
| Pins Table | Double-click a column to sort the column by ascending order. 1 Tip Sorting by pin Sequence number or Pin Group has the same effect, it sorts by Pin Group and then by sequence number within each gate. |
| Pin Group column | Select from Gate, Signal Pin, Connector Pin or Unused Pin. · Gate Pins — Assign to gates you've added to the part on the Gates tab on page 635. · Signal Pins — Assign to implicit pins (pins which are not displayed on any gate in the schematic). Typically, ground and power pins are the only implicit pins. You are not required to |  

| ogD ?， Name |
| --- |
|  |
|  |
|  |
|  |
| Name column |
|  |
| Type column |
| Swap column |
| Seq. column |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Reset button |
|  |
|  |
| Edit button |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |  

| Name | Description |
| --- | --- |
|  | · Name column - Opens the Update Pin Name dialog box. · Type column — Opens the Update Pin Type dialog box. |
|  | · Swap column — Opens the Update Pin Swap dialog box. |
|  | · Seq. column — Not available for multiple cell edits. |
| Add Pin button | Adds a new row below the selected row. If it's the first pin to be added it takes the default of belonging to Gate-A. If pins already |
|  | exist, the new pin takes the Pin Group of the currently selected pin. Note: |
|  | Requirement: You must add a pin number to make the pin valid. |
|  | Tip · You can add all pins automatically by adding a decal. |
|  | · To add a series of pins, click the Add Pins button. · To import pins using a comma separated value (.csv) file, click the Import CsV button. |
| Add Pins button | Opens the Add Pins Dialog Box. Note: |
|  | Restriction: Total pins for the part can not exceed 32,767 pins. |
|  | Tip · You can add all pins automatically by adding a decal. · To add a single pin, click the Add Pin button. |
| Delete Pins button | · To import pins using a comma separated value (.csv) file, click the Import CsV button. |
| Renumber button | Removes the selected row. |
| Copy button | Opens the Renumber Pins Dialog Box. Places the selected cell information in the paste buffer. |
|  | Tip You can also copy from Microsoft Excel. |
| Paste button | Pastes the information from the paste buffer. The selected cell in the table is the paste origin. Data is pasted below and to the right |
|  | of the paste origin. Restriction: |
|  | When the pasted data includes either Pin Group or Pin Number data, extra pin rows are added automatically, otherwise the paste will fail if the number of rows and columns in the pasted |
|  | data does not match those available in the table below and to the right of the paste origin. |
| Import CSV button | Opens the Library lmport File dialog box where you select the .csv file to import. |  

| Name | Description |
| --- | --- |
|  | Tip · The entire contents of the Pins tab table is replaced with the data of the CSV file. · CSV field names must correspond to the column headers in the Pins tab table. Only the first two characters of the header must match. For example, "Pi" for the Pin Group column. Gate or “Ga" are acceptable alternatives to the Pin Group header. · The sample Part_Pins_ Template.csv file is located in your ISailWind ProjectslSamples'folder. |
| Check Part button | Checks for missing or inconsistent information. Tip Even if you don't click the Check Part button, when you exit the tab, the assigned decals are checked to ensure that they contain physical pin numbers for all the gate and signal pins defined in the Pins tab. |  

**Related Topics**  

Part Information - Pins  

## Part Properties Dialog Box

To access: Select a part $>$ right-click $>$ Properties menu item  

Use the Part Properties dialog box to create and edit part attributes. You can also define signal pins and control the visibility of attributes assigned to the part.  

![](/images/f63277e9108ce72f50e8de05b29a41943af23a110f676a535bf5ff077c33b3ca.jpg)  

!Tip  

This dialog box contains several sub-dialog boxes. Before using any of these sub-dialog boxes, changes made in open dialog box must be applied to the design.  

![](/images/5ab1ec285a8d33435797aa611a042310a0cbf93b71f6fa362ab13895296cebc6.jpg)  
Figure 113. Part Properties Dialog Box  

**Objects**  

Table 173. Part Properties Dialog Box Contents   


| Name | Description |
| --- | --- |
| Reference Designator | Displays the name of the reference of the selected part. |
| Rename Gate button | Opens the Rename Gate Dialog Box. |
| Rename Part button | Opens the Rename Part Dialog Box. |
| Part Type | Displays the type of the selected part. |  

Table 173. Part Properties Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Change Type button | Opens the Change Part Type Dialog Box. |
| Part Information area | Displays the PCB Decal, pin count, Logic Family, if the part is ECO registered, the signal pin count, the gate count, and the number of unused pins. |
| Statistics button | Displays gate and connection information for the selected part. This information is displayed in the default text editor so you can save the contents to a file. |
| Gate Decal list | Specifies the gate decal. Select a gate decal name from the Gate Decal list to change the gate decal of the selected gate or part to one of the predefined alternate decals |
| Visibility button | Opens the Part Text Visibility Dialog Box. |
| Attributes button | Opens the Part Attributes Dialog Box. |
| PCB Decals button | Opens the PCB Decal Assignment Dialog Box. |
| SigPins button | Opens the Part Signal Pins Dialog Box. |

Related Topics Modifying Parts  

## Part Signal Pins Dialog Box  

To access: Select a part $>$ right-click $>$ Properties $>$ SigPins button  

Use the Part Signal Pins dialog box to assign any unused pins as additional signal pins. When the part type is created and stored in the library, the standard power and ground pins for part types are defined. Signal pins assigned during part creation cannot be modified through this dialog box. Instead, use the Assigning Signal Pin Names to Parts dialog box in the Library Manager.  

![](/images/70b6d750a50017275757da0feb31221e639efe42fb1f94871d66b9b0524eae53.jpg)  

!Tip  

The Part Signal Pins dialog box lists pins and their corresponding signal names. A signal pin is a pin that has a signal net (GND for example) assigned by a schematic capture program during part type creation.  

![](/images/4d5d45d7374250046e3167ab023b0aebf3350aedb765f679db05e5c167e878e0.jpg)  
Figure 114. Part Signal Pins Dialog Box  

**Objects**  

Table 174. Part Signal Pins Dialog Box Contents   


| Name | Description |
| --- | --- |
| Unused Pins list | Lists all of the unused pins for the selected part. |
| Add >> button | Adds the selected unused pin to the Signal Pins table |
| < Removes the selected Signal Pin to the Unused Pins list. | Removes the selected Signal Pin to the Unused Pins list. |
| Edit button | Makes the selected cell available for editing. |
| Signal Pins table | Lists the signal pin number and corresponding name. |
| Apply update to area | Specifies how parts are updated: |  

Table 174. Part Signal Pins Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | · This Part —— Only updates the selected part. · All Parts This Type — Updates all matching parts in the design |  

**Related Topics**  

Modifying Parts  

## Part Text Visibility Dialog Box  

To access: Select a part $>$ right-click $>$ Visibility menu item  

Use the Part Text Visibility dialog box to control the display of text associated with the selected part. You can control the visibility of one part or all parts of the same type.  

![](/images/3fa0c1486f31634b5b9453f08f2029d90beabc8f1a3cee6f5942dd9e09c34251.jpg)  
Figure 115. Part Text Visibility Dialog Box  

**Objects**  

Table 175. Part Text Visibility Dialog Box Contents   


| Name | Description |
| --- | --- |
| Item Visibility area | Specifies the visibility of the items: click to make the item visible; click to clear to make the item invisible. |
| Attribute Name Display area | Specifies the attribute name option. Display just the attribute's value or display the attribute name and its value. · All Off —— Makes all attribute names invisible, displays only the value. · No Change — Keeps the current attribute name visibility settings. · All On — Displays all attribute names and their values. |
| Apply Update to area | Specifies the selected part update options. |  

Table 175. Part Text Visibility Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | · This Gate — Updates the selected gate. · This Part — Updates a part or all associated gates of a part. · All Part This Type —— Updates all matching gates or parts in the design. Restriction: This area is unavailable when more than one part is selected. Specifies the attributes you want to display in the schematic. |  

**Related Topics**  

Controlling Text Visibility for a Part  

## Part Type Label Properties Dialog Box  

To access: Select a part type label $>$ right-click $>$ Properties menu item  

Use the Part Type Label Properties dialog box to provide text and font settings for one or more part type labels.  

![](/images/1423f88fe72698581e4ac9edd5d54b182ddeb0a30d853c413e93b40b9573a629.jpg)  
Figure 116. Part Type Label Properties Dialog Box  

**Objects**  

Table 176. Part Type Label Properties Dialog Box Contents   


| Name | Description |
| --- | --- |
| Name | The name of the selected attribute. |
| Change Type button | Opens the Change Part Type Dialog Box. |
| Rotation | Specifies the rotation of the label: O or 90 degrees. |
| Size | Specifies the size of the font. Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke fonts. The'size refers to the height of the tallest characters. |  

Table 176. Part Type Label Properties Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | ↑Gg Stroke Font - Size |
| Line Width | Specifies the line width for stroke fonts only. text Stroke Line Width |
| Font list | The fonts available to you. This lists either stroke fonts or system fonts. You choose which type of font to use in the Fonts Dialog Box. i Tip · Select stroke font or a system font. · For system fonts, you can also click a font style button, or any combination of styles: B for bold, I for italic, or U for |
| Horizontal/Vertical Justification | underlined. Specifies the horizontal (Right, Center, Left) justification and the vertical (Up, Center, Down) justification of the text. |  

**Related Topics**  

Modifying Part Type Labels  

## Pen Plotter Advanced Setup Dialog Box  

To access: File $>$ Plot menu item $>$ select Pen Plot $>$ Setup button $>$ Advanced button  

Use the Pen Plotter Advanced Setup dialog box to add a new pen plotter to the list of available plotters  

![](/images/a27c709a199962aab9770c9b5ad9623a5ffd0c419053c8596be1743428801012.jpg)  
Figure 117. Pen Plotter Advanced Setup Dialog Box  

**Objects**  

#Table 177. Pen Plotter Advanced Setup Dialog Box Contents  

| Name | Description |
| --- | --- |
| Plotter Device Name | Specifies the name of a different pen plotter you want to use. Note: Exception: Do not reuse one of the existing, supplied device names. |
| Device Type list | Specifies the interface language the plotter uses: HPGL or HGML. |
| Plotter Units area | Specifies the plotter resolution as a scaling ratio using the numbers in the Multiplier and Divisor boxes. The ratio defined is the scale factor to convert from mils (0.oo1 in) to plotter units. |
| Note: Example: Most Hewlett-Packard plotters have a resolution of 0.025 mm or 1/40 mm. This means that a distance of one inch |  |
| (1000 mils) is 1016 plotter units (25.4 X 40). So a ratio of 1016 to 1000 would be defined. The ratio actually used is 254 to 250 which is the same as 1016 to 1000. |  |
| Origin at Center | Specifies that the origin of the plotter is at the center of the paper. 1Tip Clear this check box if the origin is in the lower left corner or other location. |  

**Related Topics**  

Pen Plotter Setup Dialog Box  

## Pen Plotter Setup Dialog Box  

To access: File $>$ Plot menu item $>$ select Pen Plot $>$ Setup button  

Use the Pen Plotter Setup dialog box to set various options for the plotter.  

![](/images/17474dafbd2072d5b95fd44a225cf953dda76e8e62f2e05c2cd16186f5161346.jpg)  
Figure 118. Pen Plotter Setup Dialog Box  

**Objects**  

Table 178. Pen Plotter Setup Dialog Box Contents   


| Name | Description |
| --- | --- |
| Number of Pens | Specifies the number of pens (1-16) in your device. |
| Pen Line Width | Specifies the pen line width in mils. |
| Rotate Axis | Specifies to reverse the X and Y axes of the design. |
| Pen Colors | Specifies the color of each pen. 1Tip Select the color in the Selected Color area and then click the tile for each pen number in the Pen Colors area. |
| Selected Color | The area where you select the color you want for each pen color. |
| Plotting size area | Specifies the size of the plot. A through E and Other in inches; A4 through A0 and Other in millimeters. O Tip If you click Other, specify the X and Y dimensions. |
| Device | Specifies the Plotter device to use. |  

Table 178. Pen Plotter Setup Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Advanced button | Opens the Pen Plotter Advanced Setup Dialog Box |  

## PCB Decal Assignment Dialog Box  

To access: Select a part $>$ right-click $>$ Properties $>$ PCB Decals button  

Use the PCB Decal Assignment dialog box to assign alternate PCB decals to schematic parts. Decal names are included in the netlist file to display the proper decal, or footprint, when the file is imported into the PCB design file. You can select a decal assigned as an alternate during part creation, override the decal with one from the library, or enter a name for an undefined decal you plan to create later in the PCB design.  

![](/images/725cd6ad404e410ae2454c8958220d52bab83994def16e62524ea4ce4b1d2c5c.jpg)  
Figure 119. PCB Decal Assignment Dialog Box  

**Objects**  

Table 179. PCB Decal Assignment Dialog Box Contents   


| Name | Description |
| --- | --- |
| Assigned in Schematic | Displays the name of the currently selected decal as it is assigned to the schematic from the current library. |
| << Assign button | Assigns the selected decal in the Alternate in Library list to the part. |
| Alternates in Library list | Lists alternate decals in the library. |
| No specific PCB Decal | Specifies to remove the assigned decal. The default decal assigned to the part type is used when the netlist is imported to SailWind Layout; no decal assignment appears in the netlist. |
| Browse button | Opens the Get PCB Decal From Library Dialog Box. |
| Picture area | Displays the selected pin. |
| Apply update to area | Specifies how parts are updated: |  

Table 179. PCB Decal Assignment Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | · This Part —— Only updates the selected part. · All Parts This Type — Updates all matching parts in the design |  

**Related Topics**  

Modifying Parts  

## Photo Plotter Advanced Setup Dialog Box  

To access: File $>$ Plot menu item $>$ select Photo Plot $>$ Setup button $>$ Advanced button  

Use the Photo Plotter Setup dialog box to define the aperture and other photo plotter options.  

![](/images/6737a4b4dcc8478e00491ffe3959e0055451881416e027ef38d7d308a4f22903.jpg)  
Figure 120. Photo Plotter Advanced Setup Dialog Box  

**Objects**  

Table 180. Photo Plotter Advanced Setup Dialog Box Contents   


| Name | Description |
| --- | --- |
| Units area | Specifies the units to use: ·English — mils |
| Number of Digits area | · Metric — millimeters Specifies the precision of the output file coordinates: · Leading — the number of digits that should lead the decimal point |
| Coordinates area | point Specifies the coordinates for the output file: · Absolute — absolute coordinates |
| Zero Suppress area | · Incremental — relative coordinates Specifies how to handle zero suppression in the output file: · None — retains leading and training zeros · Leading —— suppresses zeros before the decimal point |  

Table 180. Photo Plotter Advanced Setup Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Circular Interpolation area | Specifies how to draw arcs and circles: |
| ·None — if your photo plotter does not support circular interpolation. Arcs and circles are drawn as small straight-line segments |  |
| · Quadrant — if your photo plotter does not support full, 360-degree circular interpolation |  |
| · Full — if your photo plotter supports full, 360-degree circular interpolation |  |
| Plotting Size area | Specifies the size of the plot. A through E and Other in inches; A4 through A0 and Other in millimeters. O Tip If you click Other, specify the X and Y dimensions. |
| Suppress Repeated Coords | Specifies to eliminate repeated coordinates from the output file. |  

**Related Topics**  

Photo Plotter Setup Dialog Box  

## Photo Plotter Setup Dialog Box  

To access: File $>$ Plot menu item $>$ select Photo Plot $>$ Setup button  

Use the Photo Plotter Advanced Setup dialog box to define the units for the photo plotter to use.  

![](/images/67382b787278afb01ef35c959b4c08a140d519abc405d7d56b086177b9f7825e.jpg)  
Figure 121. Photo Plotter Setup Dialog Box  

**Objects**  

Table 181. Photo Plotter Setup Dialog Box Contents   


| Name | Description |
| --- | --- |
| D-Code list | Lists the D-codes for the photo plotter. |
| Add button | Opens the CAM Question dialog box where you can name the new D-Code. |
| Delete button | Removes the selected code from the D-Code list. |
| Augment button | Automatically generates D-codes for items in the schematic file that are not in the current list. |
| Regenerate button | Clears the current D-code list and automatically adds D-codes for all items in the schematic. |
| Shape area | Specifies the shape for a selected D-code: · Flash — sets a flash aperture. · Line —— set a draw aperture. |
| Same Aperture for Flashes/Lines | Specifies to draw lines and flashed items with the same aperture. Round and square shapes for lines will be gray. |
| Width | Specifies the diameter for round shapes. This box is unavailable if a width is not appropriate for the specified shape. |
| Aperture Count | Specifies the maximum aperture count. |  

Table 181. Photo Plotter Setup Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Augment on-the-fly | Specifies to add apertures to the D-code list when photo plots are run if any newly created lines were added to the schematic. |
| Advanced button | Opens the Photo Plotter Advanced Setup Dialog Box |  

## Pin Decal Browse Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ Decal Editing Toolbar button $>$ Add Terminal or Change Pin Decal button  

Use the Pin Decal Browse dialog box to add or change a terminal. A terminal consists of a pin decal and a series of text strings that define the terminal's number, swap data, etc.  

![](/images/1e209ed53c62c40a6ea9fc1ac27dd39c0279edcba90d3b57fdd192925a4bb544.jpg)  
Figure 122. Pin Decal Browse Dialog Box  

**Objects**  

Table 182. Pin Decal Browse Dialog Box Contents   


| Name | Description |
| --- | --- |
| Picture area | Displays the selected pin. |
| Pins list | Displays the available pins. |  

**Related Topics**  

Adding Terminals Modifying Terminals  

## Pin Decal List Management Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ Setup $>$ Pin List Manger  menu item  

Use the Pin Decal List Management dialog box to control which decals are displayed in the Pin Decal List. The pin decal list contains the decals that can be used as terminal graphics when creating gate or part decals.  

![](/images/c8c82d71fab24ce8f3de823f8d2e6f8a342897213ef1c8698e6569404ab34b17.jpg)  
Figure 123. Pin Decal List Management Dialog Box  

**Objects**  

Table 183. Pin Decal List Management Box Contents   


| Name | Description |
| --- | --- |
| Library list | Lists the libraries available to you. |
| Filter | Searches the chosen library (or libraries) for a specific part or item name, or names that match a wildcard or expression on page 105. Use the Library dropdown list to select specific library directories or the All Libraries setting. Type * to view all parts or items in the chosen libraries. Click Apply to search the libraries and display the search results. |
| Preview Area | Displays the pin decal highlighted in the Unassigned Decals area or the Pin Decals area. |
| Unassigned Decals list | Lists the available pin decals in the selected library or allibraries. |
| Assign>> button | Moves a decal from the Unassigned Decals list box to the Pin Decals list. Select a decal, then click Assign. |
| < Moves a decal from the Pin Decals list box to the Unassigned Decals list box. Select a decal, then click Unassign. | Moves a decal from the Pin Decals list box to the Unassigned Decals list box. Select a decal, then click Unassign. |  

Table 183. Pin Decal List Management Box Contents (continued)   


| Name | Description |
| --- | --- |
| Pin Decals list | Lists the pin decals that are displayed in the dialog boxes that access pin decals, for example, the Pin Decal Browse dialog box. You can display up to 100 pin decals. |  

## Pin Label Fonts Dialog Box  

To access: Select a pin $>$ right-click $>$ Properties menu item $>$ Font button Use the Pin Label Fonts dialog box to change the fonts of a pin label.  

![](/images/e5cca3379fed8d4d3b5b0c7ee7bc6e91878ff300e4793845867b5089f83ba2a8.jpg)  
Figure 124. Pin Label Fonts Dialog Box  

**Objects**  

Table 184. Pin Label Fonts Dialog Box Contents   


| Name | Description |
| --- | --- |
| Pin Area |  |
| Size | Specifies the size of the font. |
| Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke fonts. The 'size refers to the height of the tallest characters. |  |
| Gg |  |
| Stroke Font - Size |  |
| Line Width | Specifies the line width for stroke fonts only. |  

Table 184. Pin Label Fonts Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | text Stroke Line Width |
| Font list | The fonts available to you. This lists either stroke fonts or system fonts. You choose which type of font to use in the Fonts Dialog Box. :Tip · Select stroke font or a system font. · For system fonts, you can also click a font style button, or |
| Justification area | any combination of styles: B for bold, I for italic, or U for underlined. Specifies the horizontal (Right, Center, Left) justification and the |
| Name Area | Specifies the size of the font. |
| Size | Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke fonts. The 'size refers to the height of the tallest characters. Gg |
| Line Width | Stroke Font - Size Specifies the line width for stroke fonts only. text |
| Font list | Stroke Line Width The fonts available to you. This lists either stroke fonts or system fonts. You choose which type of font to use in the Fonts Dialog Box. |  

Table 184. Pin Label Fonts Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Justification area | Specifies the horizontal (Right, Center, Left) justification and the vertical (Up, Center, Down) justification of the text. |  

**Related Topics**  

Modifying Pin Label Fonts  

## Pin Properties Dialog Box  

To access: Select a pin $>$ right-click $>$ Properties menu item  

Use the Pin Properties dialog box to view pin information, to modify parts and nets to which the selected pin is connected, and also to set font settings for pin number and pin name labels.  

![](/images/12f67e70b89c92a805358ca7f21ca77e25b60f03091f62b3e50fd92ff64ec057.jpg)  
Figure 125. Pin Properties Dialog Box  

**Objects**  

Table 185. Pin Properties Dialog Box Contents   


| Name | Description |
| --- | --- |
| Pin area | Displays the information about the selected pin: Pin number, name, swap number, type, and the net. |
| Part area | Displays the information about the part: reference designator and gate number. |
| Part/Gate button | Opens the Part Properties Dialog Box. |
| Net button | Opens the Net Properties Dialog Box. |
| Font button | Opens the Pin Label Fonts Dialog Box. |  

**Related Topics**  

Modifying Pins  

## Plot Dialog Box  

To access: File $>$ Plot menu item  

You can output your designs to pen plotters or photo plotters.  

![](/images/a498bf8c8bee4a4ca8774339e73aca3f07d31d00167743596afb2c6095da09e4.jpg)  
Figure 126. Plot Dialog Box  

**Objects**  

Table 186. Plot Dialog Box Contents   


| Name | Description |
| --- | --- |
| Summary | Lists the numbered available sheets you can plot, and the items contained in the sheets. |
| Plot What area | Specifies what to plot: Pen or Photo. |
| File Prefix | Specifies the prefix name of the file you want to plot. |
| Options button | Opens the Options dialog box on page 606. |
| Setup button | Depending on what you are plotting, opens the Pen Plotter Setup Dialog Box or the Photo Plotter Setup Dialog Box. |
| Preview button | Opens the Selections Preview Dialog Box. |
| Run button | Runs the Plot with what you've set. |  

## Print Dialog Box  

To access: File $>$ Print menu item  

A standard Microsoft Print dialog box with access to Print Preview and Options.  

![](/images/1d4e70266551f618c90dddc36c7663dd9f3932304301a4475741606e7e542f0f.jpg)  

![](/images/2d60677ae77db6131bbc72454bbad9adf5865b0066f81a7f8fd2675c2a509031.jpg)  

**Objects**  

| Object | Description |
| --- | --- |
| Preview button | Opens the “Selections Preview Dialog Box" on page 714. |
| Options button | Opens the “Options Dialog Box - Print/Plot" on page 606. |  

## Project Explorer  

To open the Project Explorer, click the Project Explorer button.  

The Project Explorer shows a hierarchical structure for the objects in your design. It provides access to objects and rules. When you update your design, the hierarchical structure is automatically updated to reflect the changes you make.  

Tip The Hierarchical structure is available only when a design is open.  

Restriction: The Project Explorer is not available in the Part Editor.  

**Object Types**

Objects in the Project Explorer are placed in object groups. Object groups are of two types: primary and secondary as shown in the following table.  

**Restriction:**  

Observe the following restrictions:  

• You cannot remove or rename primary object groups.   
• Modification of secondary group items is only available in SailWind Router.  

Table 187. Object Groups and Subgroups   


| Primary Group | Pradlability | Secondary Group | Description |
| --- | --- | --- | --- |
| schematic sheets | SailWind Logic | Sheet names | Lists all parts on the sheet |
| Layers | SailWind Layout SailWind Router | Electrical layers | Lists all electrical layers, including plane layers and routing layers |
| General layers | Lists all other layers except electrical |  |  |
| Components | SailWind Logic SailWind Layout SailWind Router |  | Lists all components and pin pairs |
| Part decals | SailWind Router |  | Lists all part decals in the design or all components that use the selected part decal |
| Nets | SailWind Logic SailWind Layout |  | Lists all nets in the design |
| Net objects | SailWind Router | Net classes | Lists all nets belonging to net classes |
| Matched length net groups | Lists all matched length net groups |  |  |
| Nets | Lists all nets in the design |  |  |  

Table 187. Object Groups and Subgroups (continued)   


| Primary Group | Pradlability | Secondary Group | Description |
| --- | --- | --- | --- |
|  |  | Matched length pin pair groups | Lists all matched length pin pair groups |
| Pin pair groups | Lists all nets belonging to pin pair groups (containing pin pair rules) |  |  |
| Conditional rules | Lists all nets with conditional rules |  |  |
| Differential pairs | Lists all differential pairs |  |  |
| Via types | SailWind Router |  | Lists the via types used in the design |
| CAE decals | SailWind Logic |  | Lists the CAE decals used in the design |
| PCB decals | SailWind Logic SailWind Layout |  | Lists the PCB decals used in the design |  

## Query Hierarchical Component Dialog Box

To access: Select a hierarchical component $>$ right-click $>$ Properties menu item  

Use the Hierarchical Component Properties dialog box to assign a hierarchical component to the next available sheet number to make it accessible from the Sheet list when a sheet other than the parent sheet is displayed. Use the Setup $>$ Sheets menu item to modify the sheet name or the numeric order.  

![](/images/110e151d109000f4ae238ff25657ee3214bcc979164538a0df79c4ea263fe941.jpg)  
Figure 127. Query Hierarchical Component Dialog Box  

**Objects**  

Table 188. Query Hierarchical Component Dialog Box Contents   


| Name | Description |
| --- | --- |
| Name | The name of the selected component. |
| Visibility | Specifies to display the name on top of the hierarchical component in the schematic. |
| No | The assigned sheet number of the selected component. |
| Visibility | Specifies to display the sheet number in the schematic. |
| Numbered | Specifies to assign the hierarchical component the next available sheet number. |
| UnNumbered | Specifies to remove a sheet number assignment from a hierarchical component. |  

**Related Topics**  

Modifying Hierarchical Components  

## Reference Designator Properties Dialog Box  

To access: Select a part type label $>$ right-click $>$ Properties menu item  

Use the Reference Designator Properties dialog box to view and modify label size and justification as wel as text and font settings for one or more reference designator labels.  

![](/images/b634d6e564b7dc4ed9dc0959fac1a56c075ca8b121bb33128c0a39fb2ba62880.jpg)  
Figure 128. Reference Designator Properties Dialog Box  

**Objects**  

#Table 189. Reference Designator Properties Dialog Box Contents  

| Name | Description |
| --- | --- |
| Reference Designator | The name of the selected attribute. |
| Rename area | Specifies to rename just the gate or the entire part. |
| Rotation | Specifies the rotation of the label: O or 90 degrees. |
| Size | Specifies the size of the font. Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke fonts. The size refers to the height of the tallest characters. Gg |  

Table 189. Reference Designator Properties Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Line Width | Specifies the line width for stroke fonts only. text Stroke Line Width |
| Font list | The fonts available to you. This lists either stroke fonts or system fonts. You choose which type of font to use in the Fonts Dialog Box. Tip · Select stroke font or a system font. · For system fonts, you can also click a font style button, or any combination of styles: B for bold, I for italic, or U for |
| Horizontal/Vertical Justification | Specifies the horizontal (Right, Center, Left) justification and the vertical (Up, Center, Down) justification of the text. |  

**Related Topics**  

Modifying Reference Designator Labels  

## Remap Special Symbols Dialog Box  

To access: Tools $>$ Update from Library menu item; then, in the Update from Library dialog box, choose the “Update design from library” option and select the Off-page symbols, Ground symbols, or the Power symbols check box.  

Use the Remap Special Symbols dialog box to make updates to power, ground, or off-page schematic symbols in your design. You can use this dialog box to update your schematic symbols with changes in the library or assign a different library symbol to a schematic symbol in the design.  

![](/images/f0a903b4a2c945d7bdfb90a6c7ab52f66d11374d662c2777adc666cb731b4d97.jpg)  

!Note:  

The specific signal name assigned to special symbols currently used within the schematic are not modified when performing the “Update from Library” function. For example, the signal name of a power symbol assigned to $+5V$ is not modified in the schematic if updated with another power symbol that uses a different default signal name (such as $+12V]$ ).  

![](/images/bc7eb2bd7e587eaec94817c9829a9c75aabf9bcafa66e333d43eabb444c053f6.jpg)  

**Objects**  

Figure 129. The Remap Special Symbols Dialog Box   
Table 190. The Remap Special Symbols Dialog Box Options   


| Name | Description |
| --- | --- |
| Schematic Symbol | Displays the name power, ground, or off-page symbols currently associated with your design. |  

Table 190. The Remap Special Symbols Dialog Box Options (continued)   


| Name | Description |
| --- | --- |
| Pin Type | Displays the function of the pin associated with the symbol; for example, load, ground, or power. |
| Default Signal Name | Displays the name of the signal currently associated with the symbol (as it originally existed in the library); for example, +5VCC, or AGND. This name does not necessarily reflect the signal name used on specific instances of the symbol in the schematic. |
| Library Symbol | The symbol mapped to the schematic symbol. SailWind Layout initially displays the best-matching symbol in this box, regardless of the current mapping. |
| You can change the mapping by double-clicking in the box to access a dropdown list of available symbols. You can assign the same library symbol to more than one schematic symbol. |  |
| Only symbols associated with your current library appear in the list. The available library symbols in the dropdown list |  |
| also depends on the pin type. For example, if the pin type is “ground," only ground symbols appear in the list. |  |
| Any additional symbols not specifically mapped to existing symbols become updated to the design and available for use. |  |  

**Related Topics**  

The Update From Library Function Updating Special Symbol Mappings  

## Rename Gate Dialog Box  

To access: select a part $>$ right-click $>$ Properties menu item $>$ Rename Gate button Use the Rename Gate dialog box to change the reference designator of the selected gate.  

![](/images/5bb1d2b4ac1722100eaada8214db1d48925aea1da9fe6c920a3a673028a3d23a.jpg)  
Figure 130. Rename Gate Dialog Box  

**Objects**  

Table 191. Rename Gate Dialog Box Contents   


| Name |  |
| --- | --- |
| Text box | Type the new gate reference designator information. |
|  | Restriction: |
| You are prevented from assigning an already used reference designator or an unused gate of a part with a different part type. |  |  

## Rename Part Dialog Box  

To access: select a part $>$ right-click $>$ Properties menu item $>$ Rename Part button Use the Rename Part dialog box to change the reference designator for the selected part or gate.  

![](/images/4fdd93a11daa3a37e67d869bc083bf74554a09f0d3232894f056948869b7eed0.jpg)  
Figure 131. Rename Part Dialog Box  

**Objects**  

Table 192. Rename Part Dialog Box Contents   


| Name |  |
| --- | --- |
| Text box | Type the new part reference designator information. |
|  | Restriction: |
| · All gates are renamed if you change the reference designator of one gate of a multi-gated part. · You are prevented from assigning an already used reference designator. |  |  

## Renumber Pins Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ Edit Electrical button $>$ Pins tab $>$ select pin(s) > Renumber button  

Use the Renumber Pins dialog box to renumber pins (terminals). You can renumber part type pins on the Pins tab of the Part Information dialog box.  

![](/images/61da65082faa34d5330c7d163acbbca00ccc587958200c48a0c4a7a49e3e9e45.jpg)  
Figure 132. Renumber Pins Dialog Box  

**Objects**  

Table 193. Renumber Pins Dialog Box Contents   


| Name | Description |
| --- | --- |
| Number of pins | The number of pins available for renumbering. |
| Prefix/Suffix | For a single pin number, use either Prefix or Suffix box, and void the other box. Use both boxes if you want to increment one of the values. |
| Pin numbers | Alphabetic and numeric values can be used in either box. |
| Increment prefix | A preview of pin numbers based on your prefix/suffx input. Sets the prefix as the part of the pin number to increment. |
| Increment suffix | Sets the sufix as the part of the pin number to increment. |
| Step value | Sets the step value. Type a positive or negative number by which to increase or decrease the pin number with consecutive or |  

Table 193. Renumber Pins Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | Restriction: Step value must be non-zero and be in the range -10 to +10. |
| Verify valid JEDEC pin numbering | Zero would replicate a single pin number and is not allowed. |
|  | If using alphanumerics, you can select the Verify valid JEDEC pin numbering check box to ensure that legal alphanumeric values are used. |  

## Report Manager Dialog Box  

To access: File $>$ Library menu item $>$ Parts button $>$ select a part $>$ List to File button  

Use the Report Manager dialog box to generate a report about the parts in a library. You can specify the parts and the attributes to include in the report.  

![](/images/0dd2c1123e8b562084d238bbfead498ca149f79e2398da508d33e472b21fa9bb.jpg)  
Figure 133. Report Manager Dialog Box  

**Objects**  

Table 194. Report Manager Dialog Box   


| Field or Button | Description |
| --- | --- |
| Available attributes | All attributes of the part types in the selected library. Click an atribute in the list of select it. (To select additional attributes, press CTRL and click each attribute.) Click Include >> to include selected attributes |
| Selected attributes | in the report. Attributes in the report. |
| Click an attribute in the list of select it. (To select additional attributes, press CTRL and click each attribute.) Click << Exclude to remove selected attributes from the report. |  |  

Table 194. Report Manager Dialog Box (continued)   


| Field or Button | Description |
| --- | --- |
|  | The order of attributes in the list is the order of columns in the report. Select an attribute and click Up or Down to change the order. |
| Include >>button | Includes the selected attributes in the report (moves the attributes to the Selected attributes list). Select one or more attributes on the Available attributes list and click Include >>. |
| << Exclude button | Excludes the selected attributes from the report (moves the atributes from the Selected attributes list back to the Available atributes list). Select one or more atributes on the Selected attributes list and click << Exclude. |
| Up / Down buttons | Moves a selected attribute up or down on the Selected atributes list. List order determines the order in which columns appear in the report. |
| Part Filter | Specifies the part types to include in the report. Type a part_type name in the field or use wildcards (*) to specify a group of part types.For example: * Specifies all part types in the library. +5* Specifies all part types that begin with the characters +5, such as +5volt and +5LS07. |
| Apply button | Filters the part types. |
| Parts | Lists part types included in the report (as determined by the Part Filter). |
| Run button | Generates the report and lets you save it either in lst for viewing or printing or in csv format for use with MS Excel. |
| Close button | Cancels the operation and closes the dialog box. |  

**Related Topics**  

Creating a Report of the Parts in a Library Creating a Report of Decals, Lines or Logic Symbols in a Library  

## Reports Dialog Box  

To access: File $>$ Reports menu item  

Use the Reports dialog box to produce any of six different types of reports on the current schematic. You can save these reports as text files on your hard disk or output them to a printer.  

![](/images/7fa5edf521e0b003b763959c00d598dbae5c4a7ebe724bb815d2163a00082e72.jpg)  
Figure 134. Reports Dialog Box  

**Objects**  

Table 195. Reports Dialog Box Contents   


| Name Description |  |
| --- | --- |
| Select Report Files for Output area — Select the report(s) you want to run. |  |
| Unused | The Unused report has two parts - the Unused Gate List, followed by the Unused Pins List. Use this report for troubleshooting and to maximize part usage. · Unused Gate List — lists all part types with multiple gates and if there are any unused gates, it lists the specific gate(s) under the part type name. If |
| there are no unused gates then it only lists the part type name. • Unused Pins List —lists parts with pins unused in the schematic. It lists the unused pins under the part type name. If there are no unused pins there will be no part types listed. When you run this report, a link to the UnusedGatesPins.rep appears in the |  |
| Part Statistics | The Part Statistics report lists information about all parts in the schematic. The report includes the reference designator name and part type for each part in the schematic, and for each pin on the part, the pin type, sheet location, and signal name. Use this report to locate possible errors in the schematic. When you run this report, a link to the PartStatistics.rep appears in the Output Window. Click the link to open the report in your default text editor. |
| Net Statistics | The Net Statistics report lists information for each net in the schematic. The report includes the reference designator name and pin number for all parts in the net. SailWind Logic flags possible errors (for example, nets with no inputs |  

Table 195. Reports Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | or no outputs, nets with multiple outputs, etc.) for further examination. Use this report to locate possible errors in the schematic. |
| Error messages that can occur: · Net has only one pin: a net going to an off-page flag not connected |  |
| elsewhere. |  |
| · Net has no defined source: there is no pin in the net that has a pin type of S. |  |
| · Net has no defined loads: there is no pin in the net that has a pin type of L. · Net has multiple sources- be sure they are tieable: the net has more than 1 |  |
| pin with the pin type S. When you run this report, a link to the NetStatistics.rep appears in the Output |  |
| Limits | Window. Click the link to open the report in your default text editor. The Limits report indicates the maximum number of each SailWind Logic data item (parts, nets, text) your system will allow, as well as the current count of each of these items in the schematic. This limit varies depending on the |
| amount of virtual memory that is available. The report has two parts. The first is a list of items whose limits are common to the entire schematic. The second is a count, for each schematic sheet, of the |  |
| items whose limits apply for each sheet. You should periodically run a Limits report to ensure that you are not |  |
| approaching the system's limit for any item. If you exceed the Maximum No. of Items for any item, you cannot continue adding those items to the schematic. The solution is to split the design into |  |
| multiple schematics, run separate netlists for each schematic, then merge the netlists using a text editor. When you run this report, a link to the DesignLimits.rep appears in the Output Window. Click the link to open the report in your default text editor. |  |
| The Connectivity report lists the X,Y coordinate location and sheet number of |  |
| Connectivity | all off-page, ground, and power symbols in the schematic. O Tip |
| Use the report to quickly locate an off-page symbol using the S (Search) modeless command. |  |
| An error message appears when.a net contains only one off-page reference. Subnets tied together without a visible net name are identified by flagging them as missing an off-page symbol. |  |
| When you run this report, a link to the ConnectivityReport.rep appears in the Output Window. Click the link to open the report in your default text editor. |  |
| Bill of Materials | The Bill of Materials report produces a user-configurable list of the parts contained in the current schematic. You can direct any part atribute in the schematic to a Bill of Materials report. |
| When you run this report, a link to the BillOfMaterials.rep appears in the Output Window. Click the link to open the report in your default text editor. |  |
| Setup button | Opens the Bill of Materials Setup dialog box on page 479. See also Setting up the Bill of Materials Report on page 314. |  

**Related Topics**  

Generating Reports  

## Routing Rules Dialog Box  

To access:  

• Setup $>$ Design Rules menu item $>$ a rule hierarchy button) $>$ Routing button • Select a net, right-click and click Show Rules, then click the Routing button.  

Use the Routing Rules dialog box to specify rules for interactive and automatic routing. You can specify the default set of routing rules and routing rules for specific nets.  

![](/images/5b94de2de17680bb757f78e033d17668657b663a5f7ecf99e4a8eae2e00943af.jpg)  
Figure 135. Routing Rules Dialog Box  

**Objects**  

Table 196. Routing Rules Dialog Box Contents   


| Name | Description |
| --- | --- |
| Topology Type | Specify the topology type to determine the pin-to-pin order when routing the net or moving a part. When routing interactively, a ratsnest guides you as you route from pin to pin. |  

Table 196. Routing Rules Dialog Box Contents (continued)   


| Name | Description To specify the topology type, click one of the following options: |
| --- | --- |
|  | · Protected — Do not change the order of the connectivity in the net. Note that this option disables length minimization. · Minimized — Order the net by the shortest distance between pins. Net reorder or reconnect is permitted. · Serial source —— Order the net in a series order from source pins to load pins to a terminator. |
|  | · Parallel source — Same as "Serial source" except order the net with parallel branches for each source-to-load connection. · Mid-driven — Divide the net into two branches and order each |
| Routing options Via | branch in a source to load to terminator order. Vias can share copper with another object. |
|  |  |
|  |  |
| Non-shared Via Shared Via One Net Multiple Nets Restriction: This rule is used only in SailWind Router, although you can define this rule in SailWind Logic, SailWind Layout, or SailWind |  |  

Table 196. Routing Rules Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Trace | Traces can share copper with another object. |
|  | No Trace Sharing |
|  | T-Junction |
|  | Trace Sharing |
|  | Restriction: This rule is used only in SailWind Router, although you can |
|  | define this rule in SailWind Logic, SailWind Layout, or SailWind Router. |
| Priority | Assign priority from O to 100. Nets with higher priority are routed |
|  | first. Restriction: |
|  | SailWind Router does not use the priority value. This rule applies only to SPECCTRA. |
| Auto Route | Enables the autorouter to route nets. |
| Allow Ripup | Unroute existing traces and reroute the nets. |
|  | 1Tip Enable this option to rip up traces while DRC Warn or Prevent |
| Allow Shove | is enabled. |
|  | Move unprotected traces aside to create room for new traces. Tip |
|  | Enable this option to shove traces while DRC Warn or Prevent is enabled. |
| Allow Shove Protected | Move protected traces aside to make room for new traces. |
| Layer biasing |  |
| Available Layers | Lists layers, not already in the Selected Layers list, that can be |  

Table 196. Routing Rules Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Add >> button | Click to move a selected layer from the Available Layers list to the Selected layers list. |
| << Remove button | Click to move a selected layer from the Selected Layers list to the Available layers list. |
| Selected layers | Lists the layers, that have been selected from allthe available design layers, to be available for routing. |
| Vias |  |
| Use Vias already defined in PCB Layout design | Select the check box to suppress the via biasing in SailWind Logic. Clear the check box to specify via biasing for routing. Tip · If vias exist in SailWind Logic that don't exist in SailWind Layout, you are prompted to create those vias before importing the netlist into SailWind Layout. · Since there is no Pad Stacks Properties facility for creating. vias in SailWind Logic you can only specify the names of via and you must create those vias in SailWind Layout. · Since only Default, Net, and Class rules are available in |
| Available vias | Lists the vias, not already in the Selected Vias list that are available for routing. |
| Via Definition button | Click to open the Via Setup dialog box to Add, Delete, or Rename vias available for routing. Since there is no Pad Stacks Properties facility for creating vias in SailWind Logic, any vias added must be created in SailWind Layout before importing the netlist in SailWind Layout. |
| Add >> button | Click to move a selected via from the Available Vias list to the Selected Vias list. |
| << Remove button | Click to move a selected via from the Selected Vias list to the Available Vias list. |
| Selected Vias | Lists the vias, that have been selected from all the available vias, to be available for routing. |
| Maximum number of vias |  |
| Unlimited vias | Click to give the autorouter unrestricted use of vias during autorouting. |
| Maximum of | Click to restrict the number of vias the autorouter can add to nets during autorouting. In the box, type the maximum number of vias between O and 5oooo. The autorouter considers this to be a hard rule. Interactive routing and design verification check this rule. |  

Table 196. Routing Rules Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
|  | 1Tip An insufficient maximum number of vias might increase autorouting runtime and reduce completion rates. |
| Delete button | Click to remove the current set of routing rules from the rules hierarchy for the selected nets. |
| Restriction: |  |
| The Delete button is unavailable for the default set of routing rules. You cannot delete the Default Routing rules. |  |  

## Rules Dialog Box  

To access: Setup $>$ Design Rules menu item  

Use the Rules dialog box to enter item-to-item Clearance rules, routing guidelines, and values for the optional High Speed checking commands. You can also indicate the unit of measure for passing rules to SailWind Logic: mils, metric, or inches.  

![](/images/7b00b063840e77c44c4677ecff2263b713af7ead6468cb268179043bbbec3245.jpg)  
Figure 136. Rules Dialog Box  

**Objects**  

Table 197. Rules Dialog Box Contents   


| Name | Description |
| --- | --- |
| Default button | Opens the Default Rules Dialog Box. |
| Class button | Opens the Class Rules Dialog Box. |
| Net button | Opens the Net Rules Dialog Box. |
| Conditional Rules button | Opens the Conditional Rule Setup Dialog Box. |
| Differential Pairs button | Opens the Differential Pairs Dialog Box. |
| Report button | Opens the Rules Report Dialog Box. |
| Units button | Specifies the units you want: Mils, Metric, or Inches |  

## Rules Report Dialog Box  

To access: Setup $>$ Design Rules menu item $>$ Report button  

Use the Rules Report dialog box to produce a report of some or all of the rules you have defined. By default, a complete report of all rules is reported.  

![](/images/ae08e198bb8eb38ac71f801d52b3292e654a7490a55c1b4e353f23c02b0c4259.jpg)  
Figure 137. Rules Report Dialog Box  

**Objects**  

Table 198. Rules Report Dialog Box Contents   


| Name | Description |
| --- | --- |
| Rule Types area | Displays the specified rules for the specified nets and classes. Click any combination of buttons, including Differential Pairs, to report net pairs. |
| Nets area | Displays the specified rules for every net or selected nets. Click All Nets or select specific nets in the list box. |
| Classes area | Displays the specified rules for every class or selected classes. Click All Classes or select specific net classes in the list box. |
| Default Rules | Displays the default rules for the specified nets and classes. |
| Output area | Specifies how you want your output. · Rule Sets — display all rules in the current hierarchy that are |
| unique from the default rules. · Rule Values —— display all rules in the current hierarchy level, even if the values are the same as the default rules. |  |  

**Related Topics**  

Creating a Rules Report  

## Save CAE Decal to Library Dialog Box  

To access: File $>$ Library menu item $>$ select a library $>$ Logic filter type $>$ select a CAE decal $>$ Copy button  

Use the Save CAE Decal to Library dialog box to copy a CAE decal to another name or another library.  

![](/images/da478012bd4d4d4c567f90ef2cc9243001f1de9c23618d283f765f0777aa4b41.jpg)  
Figure 138. Save CAE Decal to Library Dialog Box  

**Objects**  

#Table 199. Save CAE Decal to Library Dialog Box Content  

| Name | Description |
| --- | --- |
| Library | Select the library for the copied CAE decal. |
| Name of CAEDecal | Type the name for the copied CAE decal. |  

**Related Topics**  

Copying a Library Item  

## Save Configuration Dialog Box  

To access: Setup $>$ Display Colors menu item $>$ Save button  

Use the Save Configuration dialog box to save the color assignments and settings you’ve made in the Display Colors dialog box.  

![](/images/29a59635a0451df1048f8a179e767b87c75b4d43acf07d3637219ddc41e4ce5f.jpg)  
Figure 139. Save (color) configuration Dialog Box  

**Objects**  

#Table 200. Save configuration Dialog Box Content  

| Name | Description |
| --- | --- |
| Text box | Type the name of the new color configuration. The name will appear in the Configuration list in the Display Colors Dialog Box. |  

## Save Drafting Item to Library Dialog Box  

To access: Select an item $>$ right-click $>$ Save to Library menu item  

Use the Save Drafting Item to Library dialog box save 2D line items or complex 2D line item in the schematic to a library.  

![](/images/835a054657f5bcd0e960d86280378d298d96b5d7ef95215c519f629647118524.jpg)  
Figure 140. Save Drafting Item to Library Dialog Box  

**Objects**  

#Table 201. Save Drafting Item to Library Dialog Box Contents  

| Name | Description |
| --- | --- |
| Library list | Specifies the library you to which you want to save the item. |
| Name of Item | The name of the item you want to save in the selected library. |  

**Related Topics**  

Adding Drafting Items to a Library  

## Save Off-Page to Library Dialog Box  

To access: Tools $>$ Save Off-page to Library menu item  

Use Save Off-page to Library to update the off-page, ground, or power symbols in the library with the current version(s) in the schematic.  

![](/images/089bd4bb32bef9f652da29aacf89885020612105104d0c64596f8935117b2f47.jpg)  
Figure 141. Save Off-page to Library Dialog Box  

**Objects**  

#Table 202. Save Off-page to Library Dialog Box Contents  

| Name | Description |
| --- | --- |
| Item Type area | Specifies the item you want to update in the library with the current version in the schematic. |  

**Related Topics**  

Saving Off-Page to Library  

## Save Part and Gate Decals As Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ (in the Part Editor) File $>$ Save as menu item  

The Save Part and Gate Decals As dialog box saves a new or modified part type to the library. You can also rename a modified decal to prevent other parts that use the same decal from being affected.  

![](/images/09c034f0eb38eeefd864fb5413ab5ac60914842632417b6cbe1f861968607d6f.jpg)  
Figure 142. Save Part and Gate Decals As Dialog Box  

**Objects**  

Table 203. Save Part and Gate Decals As Dialog Box Contents   


| Name | Description |
| --- | --- |
| Name of Part | Defines the part type name in the library. |
| Library | The library folder to which information is saved. |
| Name of Gate Decals | Displays the name of decal and any alternate decals associated with the part type. Select a decal name and click Edit to rename the decal. |
| Edit button | Makes the highlighted field in the table editable. You can also double click a text field to edit it. |  

**Related Topics**  

Saving Part Types  

## Save Part Types to Library Dialog Box  

To access: Select a part $>$ right-click $>$ Save to Library menu item  

Use the Save Part Types to Library dialog box to copy the part types of the schematic. If the original part type is deleted from the library, get another copy from the schematic.  

![](/images/c13b805d7a7df4e8f1faca8d1ecdb8d9ea9e57f5499a6af8cc08e7bb51a06b05.jpg)  
Figure 143. Save Part Types to Library Dialog Box  

**Objects**  

Table 204. Save Part Types to Library Dialog Box Contents   


| Name | Description |
| --- | --- |
| Part Types list | The part(s) you selected in the schematic. |
| Select All button | Selects all of the items in the Part Types list. |
| Select Not in Lib button | Selects only those part types that are not currently saved in the library. |
| Unselect All button | Clears the selection of any or all part types in the Part Types list. |
| Library list | Specifies the library you to which you want to save the part types. |  

**Related Topics**  

Saving Part Types to a Library  

## Save Part Type to Library Dialog Box  

To access: File $>$ Library menu item $>$ select a library $>$ Parts filter type $>$ select a part type $>$ Copy button  

Use the Save Part Type to Library dialog box to copy a Part Type to another name or another library.  

![](/images/35f5193a4b85b6d3d5781dc6790de77226e234be7b079caae78aac525ec66599.jpg)  
Figure 144. Save Part Type to Library Dialog Box  

**Objects**  

#Table 205. Save Part Type to Library Dialog Box Content  

| Name | Description |
| --- | --- |
| Library | Select the library for the copied part type. |
| Name of Part Type | Type the name for the copied Part Type. |  

**Related Topics**  

Copying a Library Item  

## Save PCB Decal to Library Dialog Box  

To access: File $>$ Library menu item $>$ select a library $>$ Decal filter type $>$ select a PCB decal $>$ Copy button  

Use the Save PCB Decal to Library dialog box to copy a PCB decal to another name or another library.  

![](/images/ad686fa0bfe17fc5edfa6f275a64c69d433bb6ae20dbb5ad2fa39823b6f62ff8.jpg)  
Figure 145. Save PCB Decal to Library Dialog Box  

**Objects**  

#Table 206. Save PCB Decal to Library Dialog Box Content  

| Name | Description |
| --- | --- |
| Library | Select the library for the copied PCB decal. |
| Name of PCB Decal | Type the name for the copied PCB decal. |  

**Related Topics**  

Copying a Library Item  

## Save View Dialog Box  

To access: View $>$ Save View menu item  

The Save View dialog box to save a work area view for easy restoration.  

![](/images/e879ee0978c9235926033a5caf95b13a4bdf193d52dc1361b664dffd93501a1b.jpg)  
Figure 146. Save View Dialog Box  

**Objects**  

Table 207. Save View Dialog Box Contents   


| Name | Description |
| --- | --- |
| View Name list | The views you have already saved. |
| Preview area | Shows you the location of the selected view in relation to the extents of the design. |
| Capture button | Opens the Capture a New View Dialog Box where you can name the view you want to save. Tip You can create up to nine views. The view names appear at the |
| Apply button | bottom of the View menu. Applies the selected, previously saved view to the work area. |
| Delete button | Removes the selected view from the View Name list. |  

**Related Topics**  

Saving and Restoring Views  

## Select Gate Decal Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ open a part type $>$ Edit Graphics button Use the Select Gate Decal dialog box to select the gate decal you want to use.  

![](/images/f2a4fc8983fd161a0d90307a3324404319c013b09e17179c71b33d630a55288d.jpg)  
Figure 147. Select Gate Decal Dialog Box  

**Objects**  

Table 208. Sheets Decal Dialog Box Contents   


| Name | Description |
| --- | --- |
| Gate list | Lists the gates available to you. |
| Decal | Displays the decal assigned to the selected gate. |
| Alternative Decals list | Lists the alternative decals available. |  

**Related Topics**  

Assigning Pin Information to the CAE Decal  

## Select Pin Decal Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ open an Off-page type (Off-page, Power, or Ground) $>$ Edit Graphics button  

Use the Select Pin Decal dialog box to access and create graphics for a new Special Symbol. This dialog box is displayed when you use the Extended Selection command from the popup menu to edit a gate for a Special Symbol.  

![](/images/80217cc8642817ad084f2a33b456c567b68eacde22830b48dec4662fdced956b.jpg)  
Figure 148. Select Pin Decal Dialog Box  

**Objects**  

#Table 209. Select Pin Decal Dialog Box Contents  

| Name | Description |
| --- | --- |
| Pin Decal list | Lists the Pin Decals available to you. |  

**Related Topics**  

Creating New Special Symbols  

## Select Type of Editing Item Dialog Box  

To access: Tools $>$ Part Editor menu item $>$ New or Open button  

Use the Select type of editing item dialog box to select the type of library item to create or modify.  

![](/images/89148bee9a1820b3bfc3c66a2a688c35ac12b6f12c0b5bd6fa402c50aa855ccc.jpg)  
Figure 149. Select Type of Editing Item Dialog Box  

**Objects**  

Table 210. Select Type of Editing Item Dialog Box Contents   


| Name | Description |
| --- | --- |
| Part Type | Click Part Type to create or modify an existing part. |
| Connector | Click Connector to create or modify a connector. |
| CAE Decal | Click CAE Decal to create or modify a new CAE decal. |
| Pin Decal | Click Pin Decal to create or modify a pin decal, the information and appearance of a terminal pin. A number of different pin decals are provided. |
| Off-page | Click Off-page to modify the off-page reference symbols. SailWind Logic allows only one part definition in the library for off-page reference symbols, so this option grays when you select the File > New menu item. You can modify the existing symbols or add new symbols. Refer to the Special Symbols on page 167 topic for additional information. |
| Power | Click Power to modify an existing off-page reference symbol. SailWind Logic allows only one part definition in the library for power symbols, so this option grays when you select the File > New menu item. You can modify the existing symbols or add new symbols. Refer to the Special Symbols on page 167 topic for additional information. |
| Ground | Click Ground to modify an existing off-page reference symbol. SailWind Logic allows only one part definition in the library for ground symbols, so this option grays when you click the File > New menu item. You can modify the existing symbols or add new symbols. Refer to the Special Symbols on page 167 topic for additional information. |  

**Related Topics**  

Getting Gate Decals From the Library  

## Selection Filter Dialog Box  

To access:  

Edit $>$ Filter menu item  

• With nothing selected, right-click $>$ Filter menu item  

Use the Selection Filter to specify which objects you can select. Select a check box to enable the object for selection or clear the check box to disable the object for selection.  

![](/images/d545004818603901bb7c0ae70a975c3f8176a94c91cd0a0a5c4f5e767b035579.jpg)  
Figure 150. Selection Filter Dialog Box  

**Objects**  

Table 211. Selection Filter Dialog Box Contents   


| Name | Description |
| --- | --- |
| Design Items | Specifies the design items you want to be able to select in the design. |
| Drafting Items | Specifies the design items you want to be able to select in the design. |
| Anything button | Specifies that you want to select anything in the design. Exception: Clusters, unions, stitching vias, pin pairs, nets, and board outline shapes are not selected. |
| Nothing button | Specifies that you don't want to select anything in the design. |  

## Selections Preview Dialog Box  

To access:  

• File $>$ Plot menu item $>$ Preview button • File $>$ Print menu item $>$ Preview button Use the Selections Preview dialog box to preview your options and output.  

![](/images/645d42eec822f152a03c81ecdf2f424a068ae617420644f1c2c8ae4575948089.jpg)  
Figure 151. Selections Preview Dialog Box  

**Objects**  

Table 212. Selections Preview Dialog Box   


| Name | Description |
| --- | --- |
| Sheet button | Displays the entire sheet in the window. |
| Extents button | Zooms to the extents on the sheet. |
| Selected Sheets list | Specifies the sheet you want to preview. |  

Table 212. Selections Preview Dialog Box (continued)   


| Name | Description |
| --- | --- |
| Options button | Opens the Options dialog box on page 606. |
| Plot/Print button | Sends the output to the printer or plotter. |
| Preview area | Graphically shows what you will print or plot. |  

## Server Busy Dialog Box  

To access: There is no sure way to access this dialog box, but it may appear when you attempt to connect with one of the other SailWind software applications, for example, when you click one of the buttons in the Connect to SailWind Layout Dialog Box.  

The Server Busy dialog box appears when you are launching another application from SailWind Logic and for some reason, the other application is slow to respond.  

![](/images/0871d07bcebca9cd2a06373df2fea83f0ca99dba60f45b83d74fe13c60237b63.jpg)  
Figure 152. Server Busy Dialog Box  

**Objects**  

Table 213. Server Busy Dialog Box Contents   


| Name | Description |
| --- | --- |
| Switch To button | Switches to the application being launched. This is typically required when a prompt window in the. other application is waiting for your input before you can connect to it with SailWind Logic. |
| Retry button | Attempts to connect to the other application again. This is typically required when there has been a delay in launching the other application. Tip Wait until you see the application appear in your Windows Taskbar then click Retry. |  

## Sheets Dialog Box  

To access: Setup $>$ Sheets menu item  

Use the Sheets dialog box to edit the sheet set of the current schematic in the work area. Using Sheets enables you to add and delete sheets from the set and to modify sheet names and the numeric order of the set. You can create up to 1024 sheets.  

Sheets

![](/images/d27e2fe54b2029c8097e059db20d9380857798f371527c4c9dde5855534ea173.jpg)  

Numbered Sheets:  

| No | Name | Ref Des Start Value |  |
| --- | --- | --- | --- |
|  | LOGIC | 100 | View |
| 2 | POWER | 200 | Up |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  | Rename |  |  |
|  | Add |  |  |
|  |  |  |  |
|  |  |  |  |
|  | Delete |  |  |
|  |  |  |  |
|  | Help |  |  |  

**Objects**  

Table 214. Sheets Dialog Box Contents   


| Name | Description |
| --- | --- |
| Numbered Sheets table | · Name — Type a name for the schematic sheet. |
| · RefDes Start Value — The minimum number to use for reference designators of new components or copied/pasted components. The first available number equal to or greater than this value is used. |  |
| The RefDes Start Value stays with the sheet if the order of sheets is changed. For more information, see “Setting Reference Designators by Sheet in a New Schematic" on |  |
| page281 Bottom up hierarchy sheets are displayed but Top down hierarchy |  |
| sheets are not displayed. If you need to renumber reference designators_on a Top down sheet, see “Automatically Renumbering Reference Designators" on page 280. |  |  

Table 214. Sheets Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| View button | Specifies to show the selected sheet in the view area. |
| Up/Down buttons | Moves the selected sheet up or down in the table. O Tip The sheet value changes as you move it up or down. |
| Rename button | Makes the selected cell available for editing. OTip Spaces are not valid characters in a sheet name. |
| Add button | Adds a new sheet as a row to the bottom of the table. |
| Delete button | Removes the selected sheet. |  

**Related Topics**  

Editing Sheets  

## Signal Pin Nets Dialog Box

To access:  

• Edit $>$ Select Signal Pin Nets menu item  

• With nothing selected $>$ right-click $>$ Select Signal Pin Nets menu item Use the Signal Pin Nets dialog box to help you find and select specific signal pins in the schematic.  

![](/images/9e1d354e882e61342b9f08d452877606b18154a5cd3c0fe559a8f01738af865e.jpg)  
Figure 153. Signal Pin Nets Dialog Box  

**Objects**  

Table 215. Signal Pin Nets Dialog Box Contents   


| Name | Description |
| --- | --- |
| Select Nets list | Selecting nets in this list box selects signal pin nets within the schematic across all components and sheets. Using the right-click menu, you can perform object mode commands on the selected signal pin nets. |
| Refresh button | Updates the list of signal pin nets (in the Select Nets list box) to include any recently created signal pin nets. For example, when you add part 740o to an empty design, you create two signal pin nets: GND and +5V. Selecting Refresh includes the new signal pin nets in the Select Nets list box. |  

## Simulation Setup Dialog Box  

To access: Tools $>$ SPICE Netlist menu item $>$ Simulation Setup button  

After you add parts (with SPICE attributes) to your schematic, or add SPICE attributes to existing parts, you can create a SPICE netlist in preparation for simulation.  

![](/images/694355853fdd1234c9ec2ae4ce6f1f4736613166e3503de1e9ca753c9288fbf8.jpg)  
Figure 154. Simulation Setup Dialog Box  

**Objects**  

Table 216. Simulation Setup Dialog Box Contents   


| Name | Description |
| --- | --- |
| AC Analysis button | Opens the AC Analysis Dialog Box. |
| DC Sweep button | Opens the DC Source Sweep Analysis Dialog Box. |
| Transient button | Opens the Transient Analysis Dialog Box. |
| Operating Point | Directs the SPlCE simulator to determine the DC operating point of the circuit. |  

**Related Topics**  

Creating a SPICE Netlist  

## SPICEnet Dialog Box  

To access: Tools $>$ SPICE Netlist menu item  

After you add parts (with SPICE attributes) to your schematic, or add SPICE attributes to existing parts, you can create a SPICE netlist in preparation for simulation.  

![](/images/68ef6871f2944da4c7ed971d794939ef9c6613d45ca580ed5e45d150f3d7b5f1.jpg)  
Figure 155. SPICEnet Dialog Box  

**Objects**  

Table 217. SPICEnet Dialog Box Contents  


| Name | Description |
| --- | --- |
| Output File Name | Specifies the path and name of the SPlCE netlist file. O Tip Type the path or use the Browse button to search for a path. |
| Select Sheets list | Specifies the sheets to include in the SPiCE netlist. |
| Select All button | Specifies to select all sheets in the Select Sheets list. |
| Unselect All button | Specifies to clear all the selected sheets in the Select Sheets list. |
| Simulation Setup button | Opens the Simulation Setup Dialog Box. |
| Include Subsheets | Specifies to include any underlying hierarchy if the design is hierarchical. |
| Output Formats list | Specifies the target SPiCE software. |  

**Related Topics**  

Creating a SPICE Netlist

## Step and Repeat Dialog Box

To access: Select an object during an add or duplicate operation $>$ right-click $>$ Step and Repeat menu item. When adding a new object in the Schematic Editor, you must place the first object manually before you can use Step and Repeat.  

Use Step and Repeat to multiply objects as you place them during an add or duplicate operation. Step and Repeat is available in the Schematic Editor and the Decal Editor. In the Schematic Editor the Step and Repeat command copies parts, connections, text, or drafting items. In the Decal Editor the Step and Repeat command copies terminals, text, or drafting items.  

![](/images/fa81112ff7fa311dfe3b03a5d2e0d19d5f15b497ffee831e4dfae160ca95dfc5.jpg)  
Figure 156. Step and Repeat Dialog Box  

**Objects**  

#Table 218. Step and Repeat Dialog Box Contents  

| Name | Description |
| --- | --- |
| Direction | Specifies the direction of placement for the array. |
| Count | Specifies the number of objects to place. |
| Distance | Specifies the distance between objects. If you place a second object and then Step and Repeat, the spacing between the objects will become the default value in the Distance box and will repeat the pattern you've started. O Tip |
| Preview button | Displays the placement of the multiple objects based on the options you set. The placement of the objects is based on the location of the original object selected. O Tip Zoom Mode is available during Step and Repeat. |  

**Related Topics**  

Step and Repeat  

## Text Properties Dialog Box

To access: Select text $>$ right-click $>$ Properties menu item  

Use the Text Properties dialog box to edit the properties of free text in the design.  

![](/images/8293805ec9884bd46aa163e5ffa8a2ebca6ddc21c56a68f3152ad4fd3ae86243.jpg)  
Figure 157. Text Properties Dialog Box  

**Objects**  

Table 219. Text Properties Dialog Box Contents   


| Name | Description |
| --- | --- |
| Text | Specifies the text that you are editing. |
| X/Y | Type coordinates to place the text in a specified location. Negative coordinates are not permitted. If you want to place text outside the sheet, you must move it there with the cursor. |
| Rotation | Specifies the rotation of the text: O or 90 degrees. |
| Line Width | Specifies the line width for stroke fonts only. text |  

Table 219. Text Properties Dialog Box Contents (continued)   


| Name | Description |
| --- | --- |
| Size | Specifies the size of the font. Size (pts): This is font size in points and appears for system fonts Size (mils): This is font character height and appears for stroke fonts. The'size refers to the height of the tallest characters. Gg |
| Font Style | Stroke Font - Size Enables you to change the font style to bold, italic, and underlined. Restriction: |
| Font list | System fonts only. The fonts available to you. This lists either stroke fonts or system fonts. You choose which type of font to use in the Fonts Dialog Box. Tip |
|  | · For system fonts, you can also click a font style button, or any combination of styles: B for bold, I for italic, or U for |
|  | vertical (Up, Center, Down) justification of the text. |
|  |  |
|  |  |
| Horizontal/Vertical Justification | underlined. |
|  |  |
|  | Specifies the horizontal (Right, Center, Left) justification and the |
| Parent button |  |
|  | Opens the Drafting Properties Dialog Box. |
|  |  |
|  | Restriction: |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  | Available only if the text had been combined with a drafting |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  | object. |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |  

**Related Topics**  

Modifying Text Add Free Text Dialog Box  

## Transient Analysis Dialog Box  

To access: Tools $>$ SPICE Netlist menu item $>$ Simulation Setup button> Transient button  

Use the Transient Analysis dialog box to set options specifically for a Transient analysis.  

![](/images/a0e4aa391cd571ef23842c6458e0251035dd0efde07b747b37aee36b452a34f1.jpg)  
Figure 158. Transient Analysis Dialog Box  

**Objects**  

#Table 220. Transient Analysis Dialog Box Contents  

| Name | Description |
| --- | --- |
| Data Step Time | Specifies the increment for the analysis. |
| Total Analysis Time | Specifies the time to end the analysis. |
| Time to Start Recording Data | Specifies the time to start recording data from the analysis. 1Tip Use this if your simulation files become too large and you are not interested in data from the beginning of the analysis. |
| Maximum Time Step | Specifies the maximum time step value. |
| Use Initial Conditions (UIC) | Specifies to use SPlCE to solve for the quiescent operating point before beginning the transient analysis. SPiCE uses the values specified using IC=... on the various elements as the initial transient condition and proceeds with the analysis. |  

**Related Topics**  

Creating a SPICE Netlist Setting Up Transient Analysis  

## Update From Library Dialog Box  

To access: Tools $>$ Update from Library menu item  

Use the Update from Library dialog box to update a schematic from the library, or to compare items in a schematic with those in the library.  

![](/images/965127c408bdca3f7eb10bfe670e52e9962d9e66252f2776ece2eb70ae97b20a.jpg)  
Figure 159. Update From Library Dialog Box  

**Objects**  

#Table 221. Update From Library Dialog Box Controls  

| Control | Description |
| --- | --- |
| Mode area — Choose compare or update mode. |  |
| Generate comparison report Select this check box to compare library and schematic items and generate a report file. |  |  

Table 221. Update From Library Dialog Box Controls (continued)   


| Control | Description |
| --- | --- |
| Update design from library | Select this check box to compare library and schematic items, update the schematic from the library, and generate a report file. |
| Include items with identical time stamp | Timestamps are assigned and updated in the SailWind Logic Library routines, but it is possible for items with identical timestamps to have different content in the library and schematic if the item is edited outside the Library routines. For example, if you export a schematic to an ASCIl file, manually edit a part type in the ASCIl file, and import the schematic back into SailWind Logic, the timestamp of the part type will be unchanged, but the content will be different. Use this check box to specify whether to compare/update items whose timestamps are the same in the library and schematic. Items with identical timestamps are not compared |
| Summary and details | Report Filtering area — Specify what you want to see in the report. Select Summary and details or Summary only. |
| Summary only Hide identical results Items area — Specify the items you want to compare or update. | Select Hide identical results to see only the differences between library and design items in the report. |
| Part types and attributes | Select this check box to include part types and their atributes in the comparison or update. Tip · Attributes don't have timestamps, so they can't be updated independently of their part types. · If a schematic attribute's corresponding |
|  | attribute in the library is a placeholder attribute (with a blank value), it will be updated only if the “Allow overwriting of attribute values in design with blank values from library" check box in the Options Dialog Box, Design Category. Use this check box to specify what you want to do |  

Table 221. Update From Library Dialog Box Controls (continued)   


| Control | Description |
| --- | --- |
| Add new attributes not found in design | Use this check box to specify what you want to do with attributes that are found in the library but not in the schematic. · Select the check box to add these attributes to |
| Update common attributes | · Clear it to not add them to the updated parts. Use this check box to specify what you want to do with attributes that are found in both the schematic and the library. |
|  | · Select the check box to update the parts with the library versions. · Clear it to leave the part attributes as they are (that is, do not update them). |
| Visibility Label location Label properties | Select the attribute properties you want to. atriserveinthe schematicwhenupdating the |
|  | comparison/update. · lf you want to update CAE decal assignments in the part types, you must also select Part types and attributes. · Pin decals are updated as part of a CAE decal |
| Pin Decals | Select this check box to include pin decals in the comparison/update. |
|  |  |
|  |  |
|  |  |
|  |  |
|  | i Tip |
|  | · Only the decal is updated; pin names and |
|  | numbers are not changed. · Pin decals are updated as part of a CAE |
|  | decal update, so when CAE Decals is selected, this check box is automatically |
| Select Pins Decals List | selected and unavailable. This list is populated with check boxes |  

Table 221. Update From Library Dialog Box Controls (continued)   


| Control | Description |
| --- | --- |
|  | i Tip Because all pin decals are compared/updated as part of a CAE decal update, these check boxes are unavailable and ignored when CAE Decals is selected. |
| Off-page symbols | Select this check box to include off-page symbols in the comparison/update. Selecting this check box opens the Remap Special Symbols Dialog Box. Restriction: The off-page symbol update will fail if there is not at least one off-page symbol in the current schematic. |
| Ground symbols | Select this check box to include ground symbols in the comparison/update. Selecting this check box opens the Update From Library Dialog Box. Restriction: The ground symbol update will fail if there is not at least one ground symbol in the current schematic. |
| Power symbols | Select this check box to include power symbols in the comparison/update. Selecting this check box opens the Update From Library Dialog Box. Restriction: The power symbol update will fail if there is |  

**Related Topics**  

The Update From Library Function How to Read the Update Report The Compare/Update Process Updating a Schematic From the Library  

## Update Selected CAE Decals From Library Dialog Box  

To access: Select a part $>$ Right-click $>$ Update $>$ CAE Decal menu item  

Use the Update Selected CAE Decals from Library dialog box to update selected CAE decals in a schematic from the library. All instances of the selected CAE decals are updated.  

Figure 160. Update Selected CAE Decals From Library Dialog Box

![](/images/c100d056b2947b4e913ee11ac8e06a7f91cbb3901834dc7f00ba1329f4150680.jpg)  

**Objects**  

Table 222. Update Selected CAE Decals From Library Dialog Box Controls   


| Control | Description |
| --- | --- |
|  |  |
| Generate comparison report | Select this check box to compare library and design CAE decals and generate a report file. |
| Update design from library | Select this check box to compare library and schematic CAE decals, update the schematic from the library, and generate a report file |  

Table 222. Update Selected CAE Decals From Library Dialog Box Controls (continued)   


| Control | Description |
| --- | --- |
|  | Tip This procedure updates the pin assignments in the selected CAE decals, but doesn't update the pin decals themselves. Use one of the procedures in Updating Selected Pin Decals From the Library to update the pin decals' geometries. · As a corollary, if, for instance, CAE decal X is updated to use PlNB instead of PINA, it uses the version of PlNB geometry currently in the schematic. If there is no PINB in the schematic, it is installed from |
| Include items with identical time stamp | Timestamps are assigned and updated in the SailWind Logic Library routines, but it is possible for items with identical timestamps to have different content in the library and schematic if the item is edited outside the Library routines. For example, if you export a schematic to an ASCll file, manually edit a CAE decal in the ASCll file, and import the schematic back into SailWind Logic, the timestamp of the decal will be unchanged, but the content will be different. Use this check box to specify whether to compare/update items whose timestamps are the same in the library and schematic. |
| Select CAE Decals Area — Specify which CAE decals to update. |  |
| Select CAE Decals List | This list is populated with check boxes representing each of the selected CAE decals. Enable the check box for each of the CAE decals that you would like to update. |
| Report Filtering area — Specify what you want to see in the report. |  |
| Summary and details Summary only Hide identical results | Select Summary and details or Summary only. Select Hide identical results to see only the differences between library and schematic items in the report. This will shorten the report. |  

**Related Topics**  

The Update From Library Function How to Read the Update Report  

The Compare/Update Process  

Updating Selected CAE Decals From the Library  

## Update Selected Part Type From Library Dialog Box  

To access: In the Schematic Editor, select the part types you want to compare/update. Right-click $>$ Update $>$ Part Type menu item  

Use the Update Selected Part Type from Library dialog box to update selected parts in a schematic from the library, or to compare selected parts in a schematic with those in the library.  

![](/images/778bb4cc6e8d079e853713da25bed001d81182edeeeafb3094cddff1ebd70b0c.jpg)  

**Objects**  

Table 223. Update Selected Part Type From Library Dialog Box Controls   


| Control | Description |
| --- | --- |
| Mode area — Choose compare or update mode. |  |
| Generate comparison report | Select this check box to compare library and schematic part types and generate a report file. |  

Table 223. Update Selected Part Type From Library Dialog Box Controls (continued)   


| Control | Description |
| --- | --- |
| Update design from library | Select this check box to compare library and schematic part types, update the schematic from the library, and generate a report file. |
| Restriction: All parts having the same part type as a selected part are updated, but attributes are updated only for the parts actually selected. |  |
| Include items with identical time stamp | Timestamps are assigned and updated in the SailWind Logic Library routines, but it is possible for items with identical timestamps to have different content in the library and schematic if the item is edited outside the Library routines. For example, if you export a schematic to an ASCll file, manually edit a part type in the ASCll file, and import the schematic back into SailWind Logic, the timestamp of the part type will be unchanged, but the content will be different. Use this check box to specify whether to compare/update items whose timestamps are the same in the library and schematic. |
| Report Filtering area — Specify what you want to see in the report. |  |
| Summary and details Summary only Hide identical results | Select Summary and details or Summary only. Select Hide identical results to see only the |
| differences between library and design items in the report. This will shorten the report. |  |
| Items area — Specify the items you want to compare or update. Part types and attributes |  |
|  | Make sure that this check box is selected. |
| Tip · Attributes don't have timestamps, so they can't be updated independently of their part types. · If a schematic attribute's corresponding attribute in the library is a placeholder attribute (with a blank value), it will be |  |
| Preserve design attributes not found in library | updated only if the Allow overwriting of. attribute values in design with blank values from library check box in the Options Dialog Box, Design Category. |
| Use this check box to specify what you want to do with attributes that are found in the schematic but not in the library: · Select the check box to keep these attributes in |  |

Table 223. Update Selected Part Type From Library Dialog Box Controls (continued)   


| Control | Description |
| --- | --- |
|  | · Clear it to remove them from the updated parts |
| Add new attributes not found in design | with attributes that are found in the library but not in the schematic. ·Select the check box to add these attributes to the updated parts. · Clear it to not add them to the updated parts. |
|  | Use this check box to specify what you want to do with attributes that are found in both the schematic and the library. · Select the check box to update the parts with the library versions. • Clear it to leave the part attributes as they are (that is, do not update them). |
| Preserve design attribute properties Visibility Label location Label properties | Select the attribute properties you want to preiserve intme schematicwhenupdating the |
| Select Part Types Area — Specify which part types to update. |  |
| Select part types list | This list is populated with check boxes representing each of the selected part types. Enable the check box for each of the part types |  

**Related Topics**  

The Update From Library Function How to Read the Update Report The Compare/Update Process Updating Selected Part Types From the Library  

## Update Selected Pin Decals From Library Dialog Box

To access: Select a pin $>$ Right-click $>$ Update Pin Decal menu item  

Use the Update Selected Pin Decal from Library dialog box to update selected pin decals from the library, or to compare selected pin decals in a schematic with those in the library. All instances of the selected pin decals are updated.  

![](/images/c6a16a901a8f590c3f6fe78e55bdc29f17bf5917657e5aa279762f7279defdf7.jpg)  
Figure 161. Update Selected Pin Decals From Library Dialog Box  

**Objects**  

Table 224. Update Selected Pin Decals From Library Dialog Box Controls   


| Control | Description |
| --- | --- |
| Mode area — Choose compare or update mode. |  |
| Generate comparison report | Select this check box to compare library and schematic pin decals and generate a report file. |
| Update design from library | Select this check box to compare library and schematic pin decals, update the schematic from the library, and generate a report file. |
| Include items with identical time stamp | Timestamps are assigned and updated in the SailWind Logic Library routines, but it is possible |  

Table 224. Update Selected Pin Decals From Library Dialog Box Controls (continued)   


| Control | Description for items with identical timestamps to have |
| --- | --- |
|  | different content in the library and schematic if the item is edited outside the Library routines. For example, if you export a schematic to an ASCll file, manually edit a pin decal in the ASCll file, and import the schematic back into SailWind Logic, the timestamp of the decal will be unchanged, but the content will be different. Use this check box to specify whether to compare/update items whose timestamps are the same in the library and schematic. Items with identical timestamps are not compared or updated unless this check box is selected. |
| Select Pin Decals Area — Specify which pin decals to update. |  |
| Select Pin Decals List | This list is populated with check boxes representing each of the selected pin decals. Enable the check box for each of the pin decals that you would like to update. |
| Report Filtering area — Specify what you want to see in the report. |  |
| Summary and details Summary only Hide identical results | Select Summary and details or Summary only. Select Hide identical results to see only the differences between library and schematic items in the report. This will shorten the report. |  

**Related Topics**  

The Update From Library Function How to Read the Update Report The Compare/Update Process Updating Selected Pin Decals From the Library  

