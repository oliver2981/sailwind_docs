# Chapter 5 Design Setup  

You can define various options for the initial setup of your design. These include the settings for the schematic editor, the part editor, file backups, the work area and grids. You can also specify colors settings, and fonts for your SailWind Logic schematic design.  

Setting Options   
Setting Display Colors   
Setting Fonts   
Managing Font Replacement  

# Setting Options  

Using the Options dialog box, you can preset options for commands in SailWind Logic, setting up how those SailWind Logic commands will work and overriding the default settings in the default.txt file. Setting options enables you to set up a working environment that suits your design and the way you work.  

You can set options for the Schematic Editor on page 70 and for the Part Editor on page 71.  

Setting Schematic Editor Options Creating a Backup File Setting Part Editor Options Preserving Reference Designators Work Area and Grid Settings  

# Setting Schematic Editor Options  

SailWind Logic includes an extensive set of options for the Schematic Editor. These options enable you complete control over general design properties as well as the appearance of text and line widths.  

**Procedure** 

1. While you are in the Schematic Editor, click the Tools $>$ Options menu item.   
2. In the Options dialog box, select the appropriate category—“General” on page 595, “Design” on page 591, “Text” on page 723, or “Line Widths” on page 599. See also Setting Fonts.   
3. Set the options you want to change.   
4. Click another category to set its options.   
5. When you finish setting options, click OK.  

# Creating a Backup File  

SailWind Logic automatically creates backup files based on the settings you choose. This enables you to choose backup intervals, file naming, the number of backup files desired as well as the storage location.  

**Procedure** 

1. Click the Tools $>$ Options menu item, and then select the General category. 2. In the Interval box (in the “Automatic backups” area), type the time in minutes between automatic backups to a file. 3. In the Number of backups box, type the quantity (1-9) of different backup files to create.  

0 Tip Backup files are named <filename>#.sch, where # is a sequential number. For example, logic1.sch,logic2.sch, and so on.  

4. Perform one of the following:  

• Click Backup File to change the folder or name of the backup file, and then, in the Backup File dialog box, browse to the folder, type the filename, and click Save.  

• Select the “Use design name in backup file name” check box to use the design name instead of the product name as the filename, for example preview_logic1.sch, preview_logic2.sch instead of logic1.sch, logic2.sch  

5. Select the “Create backup files in design directory” check box to place all of your backup files in the same directory as the design.  

![](/images/0ca3c9a14fd8472eafdd444c6d329b6d2d644b018c765d3a75bd1c6603de6a2c.jpg)  

Tip Click to clear if you want your backup files in one, common backup directory.  

6. Click OK.  

**Results**  

Table 10. Backup File Creation   


<table><tr><td colspan="2">If this is selected:</td><td>The Backup File is Saved</td></tr><tr><td>Create backup files in design directory</td><td>Use design Name in backup file name</td><td></td></tr><tr><td></td><td></td><td>in one common directory without the design name.</td></tr><tr><td>X</td><td>X</td><td>in the design directory using the design name.</td></tr><tr><td>X</td><td></td><td>in the design directory without the design name.</td></tr><tr><td></td><td>X</td><td>in one common directory using the design name</td></tr></table>  

# Setting Part Editor Options  

You can set the options for the Part Editor including specific design properties such as cursor style, grids, text heights and line widths.  

**Procedure** 

1. While you are in the Schematic Editor, click the Tools $>$ Part Editor menu item.   
2. In the Part Editor, click the Edit $>$ CAE Decal Editor menu item.  

3. In the CAE Decal Editor, click the Tools $>$ Options menu item.  

4. In the Options dialog box, select the appropriate category— General on page 595, Text on page 600, or Line Widths on page 599. See also Setting Fonts.  

5. Set the options you want to change.  

6. Click another category to set its options.  

7. If you want to save the options you have set as defaults for creating new parts, click the Save As Default button.  

These defaults are used for any new parts (Part Types, Connectors, CAE Decals and Pin Decals) you create, using either the File $>$ New menu item in the Part Editor, or from the Library Manager dialog. (When you edit existing parts, SailWind Logic begins with the options stored with the part.)  

Table 11 lists the options that are saved and set as defaults.  

Table 11. Part Editor Options Saved and Set as Defaults   


<table><tr><td>From the Options Dialog General Category</td><td>From the Options Dialog Text Category</td><td>From Setup menu > Fonts Dialog</td></tr><tr><td>Design grid Labels and Text grid Display grid Snap to Grid</td><td>Font, style and size of: Pin Number Pin Name Ref-Des Part Type</td><td>Current font mode (system or stroke)</td></tr></table>  

8. When you finish setting options, click OK.  

# Preserving Reference Designators  

When you paste a group in a design, SailWind Logic uses the reference designators current in the saved group file. You have the option of enabling or disabling the preservation of group reference designators.  

!Note:  

When reference designators are preserved, if conflicts with current parts exist, SailWind Logic renames the duplicate reference designators and generates an error report containing the renamed parts. The report displays in the default text editor.  

**Procedure** 

1. Click the Tools $>$ Options menu item. In the Options dialog box, select the Design category.  

2. In the Options area, select the “Preserve Ref Des on Paste” check box to preserve group reference designators.  

**Results**  

If you enable preservation of group reference designators, SailWind Logic retains all reference designation when you copy the group. If you disable preservation, after pasting a group into a new design, reference designation starts at the first number; for example, U1. See also Options Dialog Box, Design Category.  

# Work Area and Grid Settings  

The maximum work area is a square 56 inches by 56 inches. The current grid settings appear on the message line at the bottom of the work area, between the current default line width and the current cursor X and Y location. When you move an object or use a drafting command, the grid readout is replaced by a Delta X and Y reading, calculated from the cursor selection point when the command starts. Minus numbers mean left and downward.  

Display Grid Origin and Design Grid Labels and Text Grid  

# Display Grid  

SailWind Logic uses a dot grid as a drafting aid. You can set this field of white dots called the display grid to match your design grid, or set it at larger multiples of the design grid.  

Use the General category in the Options dialog box to set the display grid or use the GD Modeless Command on page 569. If you do not want to display the display grid, set it to 10.  

# Origin and Design Grid  

When you start a new file, the default drawing format is centered in the work area with the origin, or 0,0 point, in the lower left corner. The origin appears as a large white dot. As you move the cursor, its position relative to the origin displays in the lower right corner of the screen. The numbers change in the multiples of the design grid. The minimum design grid increment is 2 mils.  

The design grid intervals begin in all directions from the origin. To set the design grid, use the General category in the Options dialog box or use the G modeless command.  

During design, if you move a part across the board, the cursor may move smoothly but the part snaps from grid point to grid point. When Snap to Grid is checked in the status window, you cannot place a part off of the current design grid.  

To set the origin while in the Part Editor, select Setup/Set Origin on page 131 from the menu. Position the cursor where you want the new origin located and click.  

# Labels and Text Grid  

All labels, fields, names, attributes, and text use the labels and text grid setting. Like the design grid, the minimum grid increment is 2 mils. To set the labels and text grid, use the General category in the Options dialog box.  

# Setting Display Colors  

Use the Display Colors dialog box to control the colors of design objects and the design area. SailWind Logic saves setup information with the schematic.  

**Procedure** 

1. Click the Setup $>$ Display Colors menu item.  

2. In the Selected Color area, select a color to assign to items.  

3. To change the available colors, click Palette. Palette opens the Color dialog box where you can specify new colors or customize colors that appear in the Selected Color area.  

![](/images/58a3e1769347de171404a3ade7cc42c2ca9f64874ad36aaa614dcc588344adc8.jpg)  

#  

Tip Click Default Palette to restore the default color settings in the Selected Color area. Refer to the Microsoft Windows Help for more information on changing the Color Palette.  

4. Click the color box of an object to change the color.  

![](/images/4d06034e5ef0035aa5f8ab16b60cbfc67e8bbb6fe7eb9a898d005268228542e0.jpg)  

!Note:  

Two color box columns appear next to the items in the Titles area. “Frg” indicates the foreground color of the text item. “Box” indicates the color of the box that is drawn around the text item. This box serves two purposes:  

• It indicates the exact size of the text item when it is plotted, thereby helping you avoid overlaps while moving the item.   
• It provides visibility of the text item at very small zoom levels.  

5. To make an item invisible, set the object color to the background color.  

![](/images/44310757748c77bc0e88f081ce0226672e503a4e8faca26dcef49393cff13d34.jpg)  

!Tip  

When working with the color configuration, note the following:  

• The color selection for displaying items or making them invisible does not affect plotting of the schematic.   
• Background sets the color of the work area surface.  

6. To save your color assignments to a file, click Save, and then type the configuration name in the Save Configuration dialog box.  

!Tip  

When saving the color configuration, observe the following:  

• SailWind Logic saves configuration files in the C:\<install_folder>\<version>\Settings folder with a .ccf extension. • The configuration names also appear at the bottom of the Setup menu. • To modify an existing configuration with the current color settings, click Save. The current configuration filename appears in the Save Configuration dialog box. You can overwrite the settings in this file, or specify a different .ccf file, and click OK.  

7. To change the default palette, complete the modifications to the Selected Color area and click Save. Type default in the Save configuration dialog box to override the existing default configuration, and click OK.  

**Related Topics**  

Display Colors Dialog Box - Part Editor  

# Setting Fonts  

You can set up your designs to use stroke font or the system fonts that ship with the Windows operating system. The system fonts installed on your system are available for use.  

**Restriction:**  

If the schematic uses fonts or character sets that are not installed on your system, a font substitution process begins automatically when the file is loaded. During this process, you are asked to select fonts to substitute for those that are missing from your system.  

Use the Fonts dialog box to set up or change the fonts to be used in your design.  

Choosing Stroke Font or System Fonts Setting Stroke Font Options Setting System Font Options Setting Line Widths Converting Stroke-to-System Fonts Converting System-to-Stroke Fonts  

# Choosing Stroke Font or System Fonts  

Depending upon you design and visual style objectives, you can set up your design to use the stroke font or system fonts.  

Stroke Font System Fonts  

# Stroke Font  

Use the Fonts dialog box to set or change the font type in your design. The “stroke” font is a simple font that is represented in SailWind Logic using lines and arcs. It does not depend upon any specific Windows font being on the system. There are some limitations imposed by the use of the stroke font.  

**Restrictions and Limitations**  

Graphical symbols and special characters, such as arrows, check boxes, and bullets are not available in a stroke font.   
Other symbols such as mathematical, technical, and geometrical symbols, plus arrows and dingbat blocks are not available in a stroke font.  

**Procedure** 

1. Click the Setup $>$ Fonts menu item.  

2. In the Fonts dialog box, select “Stroke” to use stroke font in your design then click OK.  

3. Click Yes when asked to verify that you want to change to stroke font.  

!Note:  

When changing the font type, the following conditions may apply:  

• After you confirm your selection, all text in your design changes to the new font type.   
• You cannot undo the changes after you switch font types in your schematic. To revert to a prior font, you must change it to that type.   
• Size and width of text characters in a stroke font are specified in mils; points are used exclusively for system fonts.   
• Bold, underline, and italic font styles cannot be assigned to a stroke font.  

# System Fonts  

You can choose which font to use as the system font. “System” fonts are typically fonts that are resident in your Windows environment and include a large selection of font styles. Be careful to use a font selection that is a standard font so that users on other systems can view your files using the same font.  

**Restrictions and Limitations**  

• Be sure the non-ASCII symbols, such as $+1-$ , ohm, and degrees are available on your system for the fonts you select. If the character sets you select are not available, a blank space or blank text box appears where the symbols should be. In this case, select character sets or fonts that are available on your system, and the symbols will display in your schematic.  

**Procedure** 

1. Click the Setup $>$ Fonts menu item.  

2. In the Fonts dialog box, select “System” to use a system font in your design.  

3. Select the name of the font you want to use from the Default Font dropdown list. The font in use is shown at the top of the list.  

4. Click the button for the font style you want: B for Bold, I for Italic, or U for Underlined.  

!Tip  

You can select any combination of the available styles:  

• For example, you can select Bold and Italic or Italic and Underlined.   
• By default, the style is regular—neither Bold, Italic, nor Underlined.  

5. When you have finished selecting the desired font, click OK.  

6. Click Yes when asked to verify that you want to change the system font.  

!Note:  

When changing the font type, the following conditions may apply:  

• The default font and style in use are displayed in the Default Font area.   
• If you change to system fonts, a verification message displays, asking for confirmation that you want to change to system fonts. After you click OK, all fonts in your design change to the new selection.   
• You cannot undo the change once you switch font styles in your schematic. To revert to a prior font, you must change it to a new font.   
• Non-letter symbols, such as ampersand (&), pound sign (#), and copyright $\left(\odot\right)$ , registered trademark $(\circledast)$ , and trademark (™) symbols, as well as the Euro, Pound, Yen, and Cent are supported in system fonts.  

**Related Topics**  

Setting Fonts  

# Setting Stroke Font Options  

You can set options for the text and line widths of objects in the workspace. The features of these tabs change depending on your use of either stroke font or system fonts for design objects.  

**Procedure** 

1. Click the Tools $>$ Options menu item, and then click the Text category.  

2. To change the size or width of a text item, select a text Type and click the Edit button, and then type a new value in mils in the size or width lists.  

![](/images/b5a39890a322a9b987cfb2d7df8a32e33952f0a89c7f44798331ba1c8956d714.jpg)  

Tip   
You must select a Type and click the Edit button for each attribute you want to change; you cannot edit both size and width simultaneously.  

3. When you have finished making changes, click OK.  

# Setting System Font Options  

You can set the system font options to control how text objects in your design will appear. You can choose the font style, size, and other visual characteristics of the selected font.  

**Procedure** 

1. Click the Tools $>$ Options menu item, then click the Text category.  

2. To change the font for a type of text, select a text Type and click the Edit button, and then select the font you want from the list.  

!Note:  

Fonts are displayed in the list in the following order:  

• The fonts currently used in the design are listed at the top.   
• The available system fonts are listed below the dividing line.  

3. To change the style, select the check boxes in the B, I, or U columns.  

4. To change the text size, select the Size box for the type you want to change, click the Edit button, and type a new value.  

![](/images/d4bd059777603145c5f20ab18ceea3a4d6cfa3f75ccd9efbbe5772122ae1a8c6.jpg)  

Note: System font sizes are whole point sizes.  

5. When you have finished making changes, click OK.  

# Setting Line Widths  

Use the Line Widths category to change the size of line widths in the workspace. This enables the capability for you to add visual emphasis to objects in your design.  

**Procedure** 

1. Click the Tools $>$ Options menu item, and then click the Line Widths category.   
2. Select a line Type and click the Edit button, and then in the Width column, type a new value for the size you want in mils.   
3. When you have finished making changes, click OK.  

# Converting Stroke-to-System Fonts  

If your design or visual style objectives change, you can convert text from stroke to system fonts.  

**Restrictions and Limitations**  

Be sure the non-ASCII symbols, such as $+1-$ , ohm, and degrees are available on your system for the fonts you select. If the character sets you select are not available, a blank space or blank text box appears where the symbols should be. In this case, select character sets or fonts that are available on your system, and the symbols will display in your schematic.  

**Procedure** 

1. Click the Setup $>$ Fonts menu item.   
2. In the Fonts dialog box, click System to use a system font in your design.   
3. Select the name of the font you want to use from the list. The font in use is shown at the top of the list.  

4. Click the button for the font style you want: B for bold, I for Italic, or U for Underlined.  

!Tip  

You can select any combination of the available styles:  

• For example, you can select Bold and Italic or Italic and Underlined.   
• By default, the style is regular—neither bold, italic, nor underlined.  

5. When you have finished selecting the desired font, click OK.  

!Tip  

Certain restrictions apply during the conversion:  

• All text is converted to the nearest whole point size; there is no fractional point size conversion.   
• Stroke font line widths are ignored during conversion.  

6. Click Yes when asked to verify that you want to change the system font.  

# Examples  

A stroke font text string with a size of 125 mils becomes a system font text string with a size of 9 points.   
However, a text string with a size of 100 is rounded to 7 points (97 mils).  

# Converting System-to-Stroke Fonts  

If your design or visual style objectives change, you can convert text from system to stroke fonts.  

**Restrictions and Limitations**  

Graphical symbols and special characters, such as arrows, check boxes, and bullets are not available in a stroke font.   
Other symbols such as mathematical, technical, and geometrical symbols, plus arrows and   
dingbat blocks are not available in a stroke font.  

**Procedure** 

1. Click the Setup $>$ Fonts menu item.  

2. In the Fonts dialog box, select “Stroke” to use stroke font in your design, and then click OK.  

3. Click Yes when asked to verify that you want to change to stroke font.  

!Note:  

When changing the font type, the following conditions may apply:  

• After you confirm your selection, all text in your design changes to the new font type.   
• You cannot undo the changes once you switch font types in your schematic. To revert to a prior font, you must change it to that type.   
• Size and width of text characters in a stroke font are specified in mils; points are used exclusively for system fonts.   
• Bold, underline, and italic font styles cannot be assigned to a stroke font.  

# Examples  

A system font text string with a size of 9 points becomes a stroke font text string with a size of 125 mils, and a text string with a size of 7 points is rounded to 100 mils.  

**Related Topics**  

Setting Fonts  

# Managing Font Replacement  

When you open a design created with fonts that are not installed on your system, the Font Replacement dialog box opens automatically.  

![](/images/9884b40eabcf66cd5b3313ac117dce4f5899a38aafd8810fd25cf4805008c230.jpg)  

!Tip  

If the schematic uses fonts or character sets that are not installed on your system, empty boxes appear where you expect to find text or symbols. Once font replacement process completes, the symbols display properly.  

There are two types of font replacement:  

Automatic Font Replacement Manual Font Replacement  

0 Tip You can select some fonts for automatic replacement, and select others for manual replacement.  

Automatic Font Replacement Manual Font Replacement  

# Automatic Font Replacement  

If the design you are editing uses a font that is not resident on your system, you can use the automatic font replacement feature to substitute the font with one of your available system fonts. This feature uses the standard Windows font substitution routine to propose a suitable replacement font.  

**Procedure** 

1. When a design is opened that contains a font that is not resident on your system, SailWind Logic presents the Windows Font Replacement dialog box. In the Font Replacement dialog box, click in the Mode column and select “Skip” to preserve the original font settings, or select “Auto” to use a standard Windows font substitution.  

![](/images/1701eaa23f0818f452fcf40a5f4445209fa13ea8666d311620ca410c69da38e0.jpg)  

Tip The Design Font column lists the fonts in use.  

2. In the Font column, select the name of the font you want to replace.  

3. Click OK.  

# Manual Font Replacement  

If the design you are editing uses a font that is not resident on your system, you can manually replace it with one of the resident fonts. You can also use this capability to change an existing font if you need to improve legibility or use a compressed font to save space on your schematic sheet.  

**Procedure** 

1. When a design is opened that contains a font that is not resident on your system, SailWind Logic presents the Windows “Font Replacement” dialog box. In the Font Replacement dialog box, click in the Mode box and select “Manual.”  

2. In the Font column, select the name of the font you want to replace.  

![](/images/d7d47ffd296540ffd4b7d917d50d17632c350af3d621f5bff5714e3f994ab3ca.jpg)  

!Note:  

If you need to replace only one font, only one font displays; clicking in the box has no effect.  

3. In the Replacement column, select the font you want to use as a replacement.  

4. Repeat steps 1-3 for all fonts identified for replacement.  

5. Click OK.  

Related Topics Setting Fonts  

