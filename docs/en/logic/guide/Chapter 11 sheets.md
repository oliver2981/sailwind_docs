# Chapter 11 sheets

You can use sheets to logically partition your design. You can also add custom borders and fields to your sheets.  

Editing Sheets   
Creating a Custom Sheet Border   
Adding a Field   
Changing a Text String Into a Field   
Managing Fields  

# Editing Sheets  

Use the Sheets dialog box to edit the sheet set of the current schematic in the work area. Using Sheets enables you to add and delete sheets from the set and to modify sheet names and the numeric order of the set. You can create up to 1024 sheets.  

**Procedure** 

1. Click the Setup $>$ Sheets menu item.   
2. Click a sheet in the Numbered Sheets list box, and then click View to view it in the work area.   
3. Click Add to add a new sheet to the list. The new sheet displays in the work area.  

4. Click the new sheet in the Numbered Sheets list box, and then click Rename to rename it.  

Tip Spaces are not valid characters in a sheet name.  

5. If desired, perform any of the following additional operations from the Sheets dialog box:  

Click Delete to remove a sheet from the list. • Click Up to change the numbering and position of the sheet. The sheet value changes as n-1. Click Down to change the numbering and position of the sheet. The sheet value changes as n $+1$ .  

# Creating a Custom Sheet Border  

You can create a custom sheet border with a title block using specialized text strings called fields. When you add fields to the title block of a sheet border, these fields are automatically propagated to each new sheet.  

**Procedure** 

1. Draft the 2D line border. (See Creating 2D Line Items.)   
2. Add fields to the 2D line object. (See Adding a Field.)   
3. Save the object to the lines library. (See Adding Drafting Items to a Library.)  

# Adding a Field  

Fields are used as placeholders for data that might change in a document. You can add fields to a schematic or any 2D line object. If you selected a 2D line object, the added field is automatically combined with it upon placement.  

There are two types of fields: system and user. You cannot modify system fields; the value is derived from the system. User fields are custom fields you create. There are no limitations to the name or value strings of user fields. User fields are available only in the schematic in which they are created.  

**Procedure** 

1. Select nothing or a 2D line object, right-click and click the Add Field popup menu item.   
2. In the Name list, select a system field or type a custom field name.   
3. In the Value box, type the value you want displayed. Note that the Value box is unavailable for system fields since the value is derived from your system.   
4. To place the field at a precise X,Y coordinate location, type the value in the X and Y boxes.  

!Tip  

If this is blank when you click OK, the field attaches to the pointer until you click to indicate the location.  

5. In the Rotation list, select the degree of rotation you want.  

0 Tip Rotation can be 0 or 90 degrees.  

6. In the Size box, type the font size you want.  

Stroke font sizes must be between 10 and 1000 mils; system font sizes must be between 1 and 72 points.  

7. For stroke font, in the Line Width box, type the line width.  

8. For system fonts, select the font you want to use in the Font list.  

You can also click a system font style you want applied: B for Bold, I for Italic, or U for Underlined.  

9. To set the Justification, click the Horizontal and Vertical options you want.  

10. Click OK.  

# Related Topics  

Combining 2D Lines and Text  

# Changing a Text String Into a Field  

You can use the Make Field command to change an existing text string into a field.  

**Procedure** 

1. Select a text string, right-click and click Make Field.  

2. In the Name list, type a field name or select a system field.  

3. To place the field at a precise X,Y coordinate location, type the value in the X and Y boxes.  

!Tip  

If this is blank when you click OK, the field attaches to the pointer until you click to indicate the location.  

4. In the Rotation list, select the degree of rotation you want.  

![](/images/8c6f86758be207d59d5d25a3c3e4b059cb322ca8ad8eb47ad30421c48fac9b54.jpg)  

Rotation can be 0 or 90 degrees.  

5. In the Size box, type the font size you want.  

Stroke font sizes must be between 10 and 1000 mils; system font sizes must be between 1 and 72 points.  

6. For stroke font, in the Line Width box, type the line width.  

7. For system fonts, select the font you want to use in the Font list.  

You can also click a system font style you want applied: B for Bold, I for Italic, or U for Underlined.  

8. To set the Justification, click the Horizontal and Vertical options you want.  

9. Click OK.  

# Managing Fields  

Use the Fields dialog box to manage multiple fields. You can manage the fields in the entire schematic or in a 2D line object.  

Managing All Fields in the Schematic Managing the Fields in a 2D Line Item  

# Managing All Fields in the Schematic  

If you selected nothing, the software lists all of the fields used in your schematic. The System fields display in the System area, and the fields you defined display in the User area. You can manage only the User fields.  

**Procedure** 

1. Select nothing or a 2D line object, right-click and click the Fields object.   
2. In the User area, click Add.   
3. Type a name in the Name column.   
4. Type a value in the Value column.   
5. To delete a field from the schematic, select the field name and click Delete. Restriction: You cannot delete a system field from the schematic.  

6. To edit the name or value of a field, select the Name or Value you want to edit and click Edit.  

# Managing the Fields in a 2D Line Item  

If you selected a 2D line object, the software lists all of the fields associated with the object. The System fields display in the System area, and the fields you defined display in the User area. You can delete System fields from the 2D line, but they are still available in the schematic.  

**Procedure** 

1. Select a 2D line item then right-click and click the Fields popup menu item. This opens the Fields dialog box.   
2. To delete a system field from the 2D line item, in the System area, select the field name and click Delete. The system field is still available in the schematic.   
3. To delete a user field from the 2D line item, in the User area, select the field name and click Delete. The field is still available in the schematic.  

4. To edit the value of a user field, select the Value you want to edit and click Edit.  

# Restriction:  

When editing a user field, note the following: • You cannot edit the name of the user field. • You cannot add a field for later use in a 2D line.  

