# Chapter 6 Managing Libraries and Library Data  

With SailWind Logic you can create and modify libraries, set searchability, manage library attributes, import and export libraries, report on contents, and use search parameters.  

The parts, symbols and other items you use to create a schematic in SailWind reside in one or more SailWind libraries. A single SailWind library consists of four files, each containing items of a specific type identified by the filename extension.  

Table 12. SailWind Library Files   


<table><tr><td>File Extension</td><td>File Contents</td></tr><tr><td>.pt </td><td>Parts —— Data about a part, such as a 74LSo2, including logic family, attributes, pins,and gates.</td></tr><tr><td>.pd</td><td>Decals -— The graphical representation of the part when it is drawn. It is often referred to as the footprint.</td></tr><tr><td>.ld</td><td>Logic_—— The graphical representation of a schematic part, such as a NOR gate. This section functions as a part list reader only. Use SailWind Logic to create and modify Logic decals (sometimes called CAE Decals).</td></tr><tr><td>.In</td><td>Lines —— General graphical data you can store in the library, such as a company logo, to use in any design file.</td></tr></table>  

For information on creating PCB decals, see Creation of a New Decal in the SailWind Layout Guide.  

Convert PADS Libraries to the Current Format   
Creating a Library   
Displaying Items in a Library   
Modifying Library Data   
Setting Library Availability and Search Options   
Managing Library Attributes   
Importing and Exporting Libraries   
Creating Library Reports   
Wildcards and Expressions   
Library Search Order  

## Convert PADS Libraries to the Current Format  

You can convert libraries from a previous version of PADS to the current format. This enables you to reuse library content from previous designs and to edit the content in the newer design environment.  

For information on how to convert your older PADS libraries to the current SailWind format, see Converting Your Libraries in the SailWind Netlist Library Converter Guide.  

## Creating a Library  

To add a new library to your library list, you first create a new empty library, and then populate it with content. After adding it, you can reposition it in the library list to the preferred location in the search order.  

For more information, see Adding Libraries to the Library List.  

**Procedure** 

1. Click the File $>$ Library menu item.   
2. In the Library Manager dialog box, click Create New Lib.   
3. In the New Library dialog box, specify the folder and library filename, and then click Save.   
4. Click Close.  

**Results**  

Your library is added to the bottom of the Library list, which is also the last library in the Library Search Order. To move your library up in the library list and search order, see Setting the Library List Order.  

## Displaying Items in a Library  

You can display the items that exist in a library in the Library Manager dialog box. You can choose to view PCB decals, part types, drafting items, or logic CAE decals.  

**Procedure** 

1. Click the File $>$ Library menu item.   
2. In the Library Manager Dialog Box, select a library in the Library list or select All Libraries.  

3. Click one of these buttons to display categories of items in the library:  

• Decals — PCB decals (component footprints)  

Tip Use SailWind Layout to edit PCB decals.  

• Parts — Parts  

Lines — Drafting objects  

• Logic — CAE decals (schematic symbols)  

4. To filter the list, type wildcards or expressions on page 105 in the Filter box, and then click Apply.  

![](/images/0734c80624e8c83f68bef02691185a850e1154417176ec2b0e1091eb51deb40f.jpg)  

!Tip  

An empty filter box yields no results. If you do not want to restrict the results with a filter, but display all items, type \* (asterisk) and click Apply.  

**Results**  

Library item names are displayed in the PCB Decals, Part Types, Line Items, or CAE Decals list. (The list name changes based on the Filter you’ve selected.) The preview window displays a graphic of the library object.  

![](/images/b068539976c9d78c78c209c94effc0e32a6cac46e9b4ff27b4b470300b29713d.jpg)  

!Note:  

Since library Parts have no visual representation, the preview window displays the first CAE decal associated with the part.  

**Related Topics**  

Creating a Report of the Parts in a Library  

Creating a Report of Decals, Lines or Logic Symbols in a Library  

## Modifying Library Data  

You can modify library data by adding, deleting, copying, editing, or transferring data to meet the requirements of your specific design.  

Adding Items to a Library Deleting Items From a Library Copying a Library Item Editing Items in a Library Deleting All Items in a Library Transferring Library Data  

### Adding Items to a Library  

You can add new items to a library. When added to the library, the items are available for the current and future design sessions.  

**Procedure** 

1. Click the File $>$ Library menu item.   
2. In the Library Manager Dialog Box, select a library in the Library list.  

Restriction: If you select (All Libraries), the New button is unavailable.  

3. Click one of these buttons to display categories of items in the library:  

• Decals — PCB decals (component footprints)   
Parts — Parts   
Lines — Drafting objects   
• Logic — CAE decals (schematic symbols)  

4. Click the New button.  

• Decals — Unavailable. The currently assigned PCB decal displays. Use the Library Manager in SailWind Layout to add PCB decals to a library. See also Creation of a New Decal in the SailWind Layout Guide.   
Parts — You will enter the Part Editor. Click the Edit Electrical button. The Part Information dialog box appears so you can define a new part. See also Modifying Electrical Information for a Part.  

Lines — New and Edit are unavailable. Any 2D drafting items appear, for example, drawing formats and title blocks, and you can only copy or delete them. There is no special library lines editor. Use drafting tools to create or edit lines and save them to the library.  

Tip   
To add new drafting items to the library, create and combine on page 237 the items in SailWind Logic, then right-click and click Save to Library.  

See also Creating 2D Line Items, Adding Drafting Items to a Library.  

• Logic — You will enter the CAE Decal Editor. See also Creating a New CAE Decal.  

Related Topics  

Copying a Library Item  

### Deleting Items From a Library  

You can delete one or more selected items from a library. This enables you to purge old or unwanted data from your library and improve library search times.  

**Procedure** 

1. Click the File $>$ Library menu item.  

2. In the Library Manager Dialog Box, select a library in the Library list.  

Restriction: If you select (All Libraries), the Delete button is unavailable.  

3. Click the one of these buttons to display categories of items in the library:  

• Decals — PCB decals (component footprints)   
• Parts — Parts Lines — Drafting objects   
• Logic — CAE decals (schematic symbols)  

4. To filter the list, type wildcards or expressions on page 105 in the Filter box, and then click Apply.  

!Tip  

An empty filter box yields no results. If you do not want to restrict the results with a filter, but display all items, type \* (asterisk) and click Apply.  

5. Select one or more items in the PCB Decals, Part Types, Line Items, or CAE Decals list. (The list name changes based on the Filter you have selected.)  

![](/images/504fa6b22525cfc230c9d37ba2f7298e1cc394b4868cccd6a8d8591a1199ae17.jpg)  

Tip   
Use Ctrl+click to select multiple non-sequential items. Use Shift $^+$ click or drag the cursor to select a range of items.  

6. Click Delete.  

**Related Topics**  

Deleting All Items in a Library  

### Copying a Library Item  

You can copy a selected item to another name or another library.  

**Procedure** 

1. Click the File $>$ Library menu item.   
2. In the Library Manager Dialog Box, select a library in the Library list.  

Restriction: If you select (All Libraries), the Copy button is unavailable.  

3. Click one of these buttons to display categories of items in the library:  

• Decals — PCB decals (component footprints) Parts — Parts Lines — Drafting objects   
• Logic — CAE decals (schematic symbols)  

4. To filter the list, type wildcards or expressions on page 105 in the Filter box, and then click Apply.  

!Tip  

An empty filter box yields no results. If you do not want to restrict the results with a filter, but display all items, type \* (asterisk) and click Apply.  

5. Select an item from the list and click Copy.  

6. In the dialog box that opens, select another library to receive the copy of the item, and/or type a new item name, and then click OK.  

• Decals — Opens the Save PCB Decal to Library Dialog Box • Parts — Opens the Save Part Type to Library Dialog Box Lines — Opens the Save Drafting Item to Library Dialog Box • Logic — Opens the Save CAE Decal to Library Dialog Box  

Related Topics  

Importing and Exporting Libraries  

### Editing Items in a Library  

As library content is frequently changing, you can use the Library Manager to edit items in a library. Select the item that you want to edit, make the desired edits, and then save the edits to the current library item or rename the item as a new library object.  

**Procedure** 

1. Click the File $>$ Library menu item.  

2. In the Library Manager Dialog Box, select a library from the Library list.  

!Tip  

If you select (All Libraries), the Edit button is unavailable.  

3. Click the one of these buttons to display categories of items in the library:  

• Decals — PCB decals (component footprints) Parts — Parts Lines — Drafting objects   
• Logic — CAE decals (schematic symbols)  

4. To filter the list, type wildcards or expressions on page 105 in the Filter box, and then click Apply.  

0 Tip An empty filter box yields no results. If you don’t want to restrict the results with a filter, but display all items, type \* (asterisk) and click Apply.  

5. Select an item in the list and click Edit.  

• Decals — Unavailable. The currently assigned PCB decal appears and you can only copy or delete it. Use the Library Manager in the PCB design program to modify the PCB decal. See Editing a Library Decal in the SailWind Layout Guide.  

• Parts — You enter the Part Editor. Click the Edit Electrical button. The Part Information dialog box appears so you can edit the part. See Modifying Electrical Information for a Part, Part Editor Operations.  

Lines — Unavailable. Any 2D drafting items appear, for example, drawing formats, title blocks, etc. and you can only copy or delete them. There is no special library lines editor. Use drafting tools to create or edit lines and save them to the library.  

![](/images/8369383f543a692aa75267e79ecf503604c10804cb5b12a680d8f42618f16646.jpg)  

!Tip  

To add new drafting items to the library, create and combine on page 237 the items in SailWind Logic, then right-click and click Save to Library.  

• Logic — Opens the CAE Decal Editor with the selected decal. See Creating a New CAE Decal.  

### Deleting All Items in a Library  

When you choose to delete all of the items in a library, the software replaces the existing library with a new empty one of the same name. By doing so, the software ensures that there are no leftover items in your library.  

Restriction: You cannot delete the contents of a read-only library.  

**Procedure** 

1. Click the File $>$ Library menu item.   
2. Click Create New Lib. The New Library dialog box displays.   
3. Select the library file whose contents you want to delete, click Save, and then click Yes when   
   prompted.   
4. Click Close.  

**Related Topics**  

Deleting Items From a Library  

### Transferring Library Data  

There may be times when it is desirable to transfer library objects from one library to another. This may be useful when you want to archive a specific library with a design or for creating libraries with a specific mixture of content for new designs.  

![](/images/c6f954e53fd7effff6d4edbed6500550a7ec12e63e613c49e149c6c3f19606e7.jpg)  

!Tip  

To copy over single items, see Copying a Library Item.  

**Procedure** 

1. Follow the steps to export library data from the library on page 102.   
2. Follow the steps of the Importing Library Data topic of the SailWind Layout Guide to import the library data to another library.  

## Setting Library Availability and Search Options  

Specify the libraries available to the design, the library search order, and other search-related options.   
Operations affect the contents of the Library list in the Library Manager dialog box.  

Adding Libraries to the Library List Removing Libraries From the Library List Library Content and the Search Order Setting the Library List Order Sharing a Library Across a Network Controlling Library Search Access Protecting Library Files Synchronizing With SailWind Layout  

### Adding Libraries to the Library List  

You add libraries to the library list to make their contents available. The library must be listed in the Library Manager to search it and use its parts, decals, or line items in your design.  

**Procedure** 

1. Click the File $>$ Library menu item, then click the Manage Lib. List button.  

2. In the Library List Dialog Box, click Add.  

3. In the Add Library dialog box select a file type:  

• Select Library Files (\*.pt9) from the file type list to add a SailWind Logic library. Select OrCAD Symbol Library Files (\*.olb) from the file type list to add an OrCAD library. The OrCAD library translation may take some time. See the progress indicator in the Status Bar.  

Any errors, warnings, or messages created during the translation display in the Logic.err file, which opens in the default text editor.  

4. Specify the folder and filename of the library to add, and then click Open.  

**Results**  

The library is added beneath the currently selected library in the Library list. If a library is not selected, the new library is added to the bottom of the list.  

### Removing Libraries From the Library List  

If you want to prevent the contents of a library from being used in a design, remove the library from the library list.  

**Procedure** 

1. Click the File $>$ Library menu item, then click the Manage Lib. List button. 2. In the Library List Dialog Box, select one or more libraries from the Library list and then click Remove.  

**Results**  

The library files are removed from the Library List but are not deleted from the computer.  

### Library Content and the Search Order  

Parts, symbols, and decals you create do not have to be located in the same library together. When your part refers to a symbol or decal in a different library, the software automatically picks up the symbol or decal when needed.  

If you have multiple library items of one type and with the same name, the first occurrence of the item is chosen when the library is searched.  

For example, during import of a schematic netlist, the libraries are searched for a 0603 decal. But there are two, each in a different library. The libraries are searched from the first library in the list, to the last library in the list. The first occurrence found will be selected for use to represent the part in the design.  

When you have multiple libraries available, they are processed in their order in the library list whenever the libraries are searched. The libraries are searched during the following procedures:  

• Searching for library items using various dialogs Importing a netlist from the schematic   
• Updating your design from the library   
• Annotating your design with new components from the schematic  

You can change the search order of libraries using the “Library List Dialog Box” on page 555.  

### Setting the Library List Order  

You can specify the order in which libraries are searched. The libraries are searched in the order in which they are listed in the Library list.  

**Procedure** 

1. Click the File $>$ Library menu item, then click the Manage Lib. List button. 2. Select the library from the Library list in the Library List Dialog Box, and then click Up or Down as needed.  

**Results**  

With each click, the library moves up or down one place in the library list. The libraries are searched top to bottom.  

**Related Topics**  

Library Search Order  

### Sharing a Library Across a Network  

You can share a library across a networked environment, to enable more than one user to access the library simultaneously.  

**Procedure** 

1. Click the File $>$ Library menu item, then click the Manage Lib. List button.  

2. In the Library List Dialog Box, in the Library list, select the library.  

![](/images/b9fc3c5735ec03935f8ca3fcdb42d11e51e72e75cd7c19319bde09af6ea6eb8a.jpg)  

Tip You can select multiple libraries using the Shift and Ctrl keys.  

3. Select the Shared check box.  

**Results**  

More than one user can access the library file at the same time.  

### Controlling Library Search Access  

You can enable or disable the searching of a particular library when performing operations that involve libraries, such as adding parts.  

**Procedure** 

1. Click the File $>$ Library menu item, then click the Manage Lib. List button.  

2. In the Library List Dialog Box, in the Library list, select the library.  

Tip You can select multiple libraries using the Shift and Ctrl keys.  

3. Select the “Allow Search” check box.  

### Protecting Library Files  

The Read Only check box is only a status indicator. It is always shaded and unavailable. You can set library read-only status only in the Microsoft Windows File Manager.  

**Restrictions and Limitations**  

To ensure file protection, the system administrator who owns the files is the only one who can control the process.  

**Procedure** 

1. In Windows File Explorer, locate your library files.  

![](/images/431ad5a221392ef8953eb3abe098a4b0938e26dd70f61a12b918709b5cae54f0.jpg)  

Tip   
By default, libraries installed with the software are located at C:\<install_folder>\<version>   
\Libraries  

2. Select all four library files, right-click and click Properties.  

3. In the Properties dialog box, click the General tab and select the “Read-only” check box.  

4. Click OK.  

**Results**  

The library Read-Only check box in the Library List Dialog Box will not update until you reopen the dialog box.  

### Synchronizing With SailWind Layout  

You can enable or disable the synchronizing of library settings between SailWind Logic and SailWind Layout. When the Synchronize with SailWind Layout check box is checked in SailWind Logic, all changes made in the libraries within SailWind Logic are pushed to SailWind Layout.  

![](/images/0376b1b3b30bd70f376a3eeaa82cf1579a1b4058ee56aea547c6823f1fd7e0d8.jpg)  

Tip To ensure a round-trip synchronization, select the same check box in SailWind Layout.  

**Procedure** 

1. Click the File $>$ Library menu item, then click the Manage Lib. List button.   
2. In the Library List Dialog Box, select the Synchronize with SailWind Layout check box.  

## Managing Library Attributes  

Use the Manage Library Attributes dialog box to manage attributes on a library-by-library basis. You can add, delete, and rename attributes for all parts or decals in an individual library or in all libraries. You can also display all the attributes in a library, whether the attributes apply to all items or to individual items.  

![](/images/f16300308d3b1028ca83d387a419dded055c25b7769c1c74870948e8e71ae922.jpg)  

Tip   
This dialog box does not manage attributes in the current design. Use the Manage Schematic Attributes Dialog Box to manage attributes in an open design file.  

Adding an Attribute to Multiple Library Items Deleting Attributes From Library Items Renaming Attributes of Library Items  

### Adding an Attribute to Multiple Library Items  

You can add an attribute to all parts and decals, or just to parts or decals individually, in one or all libraries.  

**Restrictions and Limitations**  

This process will yield no result or warning if the library you are working with is read-only. Check the status of the library in the Library List Dialog Box.  

**Procedure** 

1. Click the File $>$ Library menu item, then, in the Library Manager dialog box, click the Attr Manager button.   
2. In the Manage Library Attributes Dialog Box, in the Select Library list, select an individual library or the (All Libraries) item at the top of the list.   
3. In the Item Types list, choose whether to apply the new attribute to All Items, or only either Part Types or PCB Decals.   
4. Click Add Attr. The Add New Attribute to Library Dialog Box appears.   
5. For the Attribute Name, do one of the following: • Type an attribute name in the box. • Click Browse Lib. Attr to search all libraries for an existing attribute name.  

6. (Optional) Type a value in the Attribute Value box.  

7. Click OK.  

The Attribute Name appears in the Attributes in Library list.  

8. Click Close.  

**Results**  

Your new attribute is added. Check for the new attribute in the Decal Attributes dialog box (for PCB decals) or on the Attributes tab of the Part Information dialog box on page 631 (for Part Types).  

**Related Topics**  

Manage Attributes in a Schematic  

### Deleting Attributes From Library Items  

You can delete one or more attributes from all parts and decals, or just from parts or decals individually, in one or all libraries.  

**Restrictions and Limitations**  

This process will yield no result or warning if the library you are working with is read-only. Check the status of the library in the Library List Dialog Box.  

**Procedure** 

1. Click the File $>$ Library menu item, then, in the Library Manager dialog box, click the Attr Manager button.   
2. In the Manage Library Attributes Dialog Box, in the Select Library list, select an individual library or the (All Libraries) item at the top of the list.   
3. In the Item Types list, choose whether to delete the attribute(s) from All Items, or from either Part Types or PCB Decals.   
4. In the Attributes in Library list, select one or more attributes to delete, and then click Delete Attrs.   
5. In the prompt that appears, click OK.   
6. Click Close.  

**Results**  

Your attribute(s) is deleted. Check for the deleted attribute in the Decal Attributes dialog box (for PCB decals) or on the Attributes tab of the Part Information dialog box on page 631 (for Part Types).  

**Related Topics**  

Manage Attributes in a Schematic  

### Renaming Attributes of Library Items  

You can rename an attributes of all parts and decals, or just of parts or decals individually, in one or all libraries.  

**Restrictions and Limitations**  

This process will yield no result or warning if the library you are working with is read-only. Check the status of the library in the Library List Dialog Box.  

**Procedure** 

1. Click the File $>$ Library menu item, then, in the Library Manager dialog box, click the Attr Manager button.   
2. In the Manage Library Attributes Dialog Box, in the Select Library list, select an individual library or the (All Libraries) item at the top of the list.   
3. In the Item Types list, choose whether to rename the attribute(s) from All Items, or from either Part Types or PCB Decals.   
4. In the Attributes in Library list, select one or more attributes to rename, and then click Add.  

5. Double-click in the New Name cell, type the name, and then click Rename Attrs.  

![](/images/4cdb5230562a29371cbcc94b77acf8549d03d2a6cb19938e8ed280bac788701c.jpg)  

!Tip  

You can specify the name of an existing attribute. No error message appears when you do this. The only time this may have an adverse effect is if both attributes are assigned to a single item, in which case the error is reported in the error file and the rename is not performed for those items where there are conflicts.  

6. Click Close.  

**Results**  

Your attribute is renamed. Check for the renamed attribute in the Decal Attributes dialog box (for PCB decals) or on the Attributes tab of the Part Information dialog box on page 631 (for Part Types).  

**Related Topics**  

Manage Attributes in a Schematic  

## Importing and Exporting Libraries  

Use the Library Manager dialog box to import or export library data in ASCII format.  

Importing Library Data Exporting Library Data  

### Importing Library Data  

You can import library data from a previously-exported library ASCII file. This provides a convenient method for importing library data from another design or from another designer’s library.  

![](/images/9303df268e2e33526194c60791ef809a790f7e6cb5771444568280bee80c1a98.jpg)  

!Tip  

Beginning with PADS 9.0, die parts and flip chips are no longer identified by their family designations (DIE or FLP), but instead by the Special Purpose settings in the General tab of the Part Information dialog box on page 637. When you import an ASCII file created by a previous PADS version, these Special Purpose settings are automatically set for parts having the logic family DIE or FLP. The part’s family designation remains the same.  

**Procedure** 

1. Click the File $>$ Library menu item.  

2. In the Library Manager Dialog Box, in the Library list, select the library to receive the library data.  

3. To import one of the four file types, you must select the matching filter:  

• If the file type is .c, select the Logic filter. This ASCII file contains CAE decals (logic symbols).   
• If the file type is .l, select the Lines filter. This ASCII file contains drafting objects.   
• If the file type is .d, select the Decals filter. This ASCII file contains PCB decals (component footprints).   
• If the file type is .p, select the Parts filter. This ASCII file contains part types.  

4. Click Import.  

![](/images/36d43182006eb369767febef33abd21ed01807f6a130ccd9dd20559beed185ef.jpg)  

Tip Import fails if the library to receive imported items is read-only.  

5. In the Library Import File dialog box, specify the folder and the filename, and then click Open.  

**Related Topics**  

Transferring Library Data  

### Exporting Library Data  

You can export library data into an ASCII file for importing into a library. This provides a convenient method for exporting library data to another design or to another designer’s library.  

**Procedure** 

1. Click the File $>$ Library menu item.   
2. In the Library Manager Dialog Box, in the Library list, select the library whose data you want to export.  

3. Click any of the following:  

• Decals — Exports PCB decals (component footprints)   
• Parts — Exports Components Lines — Exports drafting objects   
• Logic — Exports CAE decals (schematic symbols)  

4. To filter the list, type wildcards or expressions on page 105 in the Filter box, and then click Apply.  

Tip To display all items in the library, type an asterisk (\*) and click Apply.  

5. Select one or more items in the list, and then click Export.  

6. In the Library Export File dialog box, specify the folder, type the filename, and then click Save.  

**Results**  

• The Special Purpose settings of any die parts and flip chips are cleared.   
• Die parts and flip chips having a family designation other than DIE and FLP lose their die part or flip chip special purpose and become normal parts.   
• Any normal parts that have the DIE or FLP family designation are treated as die parts or flip chips in the previous PADS version.  

## Creating Library Reports  

You can create reports from the Library Manager to list any number of library objects. The Parts report can be configured to list the values of attributes that you choose to include in the report.  

Creating a Report of the Parts in a Library Creating a Report of Decals, Lines or Logic Symbols in a Library  

### Creating a Report of the Parts in a Library  

From the Library Manager, you can generate a report about the parts in a single library or all libraries. The report (an ASCII file) lists each part and its associated attributes.  

You can specify the attributes you want reported. Figure 1 and Figure 2 show example parts reports.  

**Procedure** 

1. Click the File $>$ Library menu item.  

2. In the Library Manager Dialog Box, select a library from the Library list, or select All Libraries.  

3. In the Filter area, click Parts. A list of parts in the library (or in all libraries) appears in the Part Types area.  

![](/images/d740f9d45738798ef49256f3b3907a15561c96dbe7fef50d1aa11880d20ae43f.jpg)  

!Tip  

To refine the list, use the filter field. Type a part name in the field or use wildcards $(^{\star})$ to specify a group of parts. Then click Apply.  

4. When you have the list of parts you want to report on, click List to File.  

5. In the Report Manager Dialog Box, specify the part attributes you want to include in the report.  

a. In the Available attributes list, click an attribute to select it.  

b. Click Include>>.  

The attributes appear in the Selected attributes list.  

To remove attributes from the Selected attributes list, select them and click <<Exclude.  

6. (Optional) You can refine the list of parts to report on. In the Part Filter field, type a part name in the field or use wildcards $(^{\star})$ to specify a group of parts, and then click Apply.  

7. Click Run.  

8. In the Library List File dialog box, select a folder and file format for the report.  

You can select either of two formats:  

• Library List format $(.I s t)$ : Information is formatted in columns for viewing or printing. (Figure 1).   
• Comma-separated values format (.csv): format recognized by Microsoft® Excel® (Figure 2).  

9. Click Save.  

10. In the Report Manager dialog box, click Close.  

**Results**  

The Report Manager generates the report and displays a link to it in the Output window. To view or print the report, click the link. Notepad opens and displays the report.  

![](/images/2d3394476a153b12f308ca1a6839a656a6b5119ad6025f6e4e3b67372060331f.jpg)  
Figure 1. Parts Report in .lst Format   
Figure 2. Parts Report in .csv Format  

"Library","Part Name","Part Number","Description","Manufacturer #1","pcB Decal 1" "anlogdeV","AD1315","AD1315KZ","HIGH SPEED ACTIVE LOAD WITH INHIBIT" "ANALOG DEVICES","Z-16A", "anlogdev","AD1321","AD1321KZ","HIGH SPEED PIN DRIVER WITH INHIBIT",“ANALOG DEVICES",“Z-16A"， "anlogdew" "AD1322" "AD13ZZKZ","ULTRAHIGH SPEED PIN DRIVER WITH INHIBIT" "ANALOG DEVICES","Z-16A"， "anlogdev","AD1376","AD1376 (,KD",“HIGH SPEED,16-BIT A/D CONVERTER”,"ANALOG DEVICES",“DH-3ZE", "anlogdev","AD1377","AD1377 (,K)D","HIGH SPEED，16-BIT A/D CONVERTER","ANALOG DEVICES","DH-32E" “anlogdev","AD1382","AD1382KD","16-BIT， 5Q0KHZ， SAMPLING ADC","ANALOG DEVICES","DH-48A"，  

**Related Topics**  

Report Manager Dialog Box   
Creating a Report of Decals, Lines or Logic Symbols in a Library   
Managing Libraries and Library Data  

### Creating a Report of Decals, Lines or Logic Symbols in a Library  

From the Library Manager, you can generate a report listing the decals, lines, or logic symbols in a single library. The report is an ASCII file listing each item’s name and the date and time the item was modified.  

**Procedure** 

1. Click the File $>$ Library menu item.  

2. In the Library Manager Dialog Box, select a library from the Library list.  

![](/images/2c47994329a1fb62d8199c3c91143563c1b99751b84795d1336f74b3869685d6.jpg)  

Restriction:   
The List to File button is unavailable for Decals, Lines, and Logic Symbols if you select All Libraries.  

3. In the Filter area, click either the Decals, Lines, or Logic filter.  

A list of corresponding items from the library appears in the dialog box (in the “PCB Decals,” “Line Items,” or “CAE Decals” area, depending on your filter selection).  

![](/images/59d0a95391f36a51fb7736c49c8830158dcbe5af7200b061d41a913ce67d6bb2.jpg)  

!Tip  

To select one or more specific item, use the filter field. Type an item name in the field or use wildcards $(^{\star})$ to specify a group of items. Then click Apply.  

4. When you have the list you want to report on, click List to File.  

5. In the Library List File dialog box, specify a folder and filename for the report and click Save.  

**Results**  

Notepad appears, displaying a list of the item names and the date and time when each was last modified.   
You can print the list from Notepad.  

**Related Topics**  

Creating a Report of the Parts in a Library Managing Libraries and Library Data  

## Wildcards and Expressions  

You can use wildcards and expressions to filter the information that is displayed. This promotes rapid and precise browsing of library content.  

The filter supports the wildcards and expressions listed in Table 13. Table 14 gives examples of wildcard usage.  

Table 13. Wildcards and Expressions   


<table><tr><td>Expression:</td><td>Use to:</td></tr><tr><td>*</td><td>Match any number of characters.</td></tr><tr><td>？</td><td>Match any one character.</td></tr><tr><td>[set] </td><td>Match any character in the specified set.</td></tr></table>  

Table 13. Wildcards and Expressions (continued)   


<table><tr><td>Expression:</td><td>Use to:</td></tr><tr><td></td><td>Tip: A set is composed of characters or a range of characters; for example, A-Z or 0-9 or a-z.</td></tr><tr><td>[!set] or [^set]</td><td>Match any character not in the specified set.</td></tr><tr><td>一</td><td>Match a special syntactic character exactly, suppressing the special character's syntactic significance. Tip: The following characters need the \ before them: *[*?!^-\'</td></tr></table>  

Table 14. Usage Examples of Wildcards and Expressions   


<table><tr><td>Expression:</td><td>Results in all items that:</td></tr><tr><td>74*</td><td>Start with 74: 7404,74LS04,74622.</td></tr><tr><td>74??</td><td>Start with 74 followed by any two characters: 7404, 74T2, 74TP.</td></tr><tr><td>74??08</td><td>Start with 74, followed by any two characters, and end with 08: 74LS08, 74HC08,744608.</td></tr><tr><td>*08</td><td>Start with any number of characters and end with 08: 2146108, 5408, 54HCT08,744608.</td></tr><tr><td>*08*</td><td>Start with any number of characters, followed by 08, and end with any number of characters: 5408, 5408BE,54HCT08AE,74ABT08CE2, 941M70839.</td></tr><tr><td>[57]*</td><td>Start with 5 or 7 with any number of characters after: 54HCT244, 5968BAE4,74ACT44.</td></tr><tr><td>[5-7]*</td><td>Start with 5, 6, or 7 followed by any number of characters: 54LS08, 6225BE,69TF77,74ALS02.</td></tr><tr><td>[57]4HCT??</td><td>Start with 5 or 7, followed by 4HCT, and end with any two characters: 54HCT04,54HCT74,74HCT27,74HCT84.</td></tr><tr><td>74A[CH]*</td><td>Start with 74A, followed by C or H, and end with any number of characters: 74AC244,74AHCT27.</td></tr><tr><td>74A[!C-H]*</td><td>Start with 74A, followed by any character except the letters C through H, and end with any number of characters: 74ABT44, 74ALS244, 74ABF365.</td></tr><tr><td>[M]*08</td><td>Start with the character\, followed by any number of characters, and end with08: \LS08,\HCT08,\ABT08.</td></tr></table>  

## Library Search Order  

The list of libraries in the Library Manager dialog box displays the library search order. When you have multiple libraries available, they are processed in their order in the library list whenever the libraries are searched.  

The libraries are searched during the following procedures:  

• Searching for library items using various dialogs • Importing a schematic netlist into SailWind Layout • Updating your design from the library • Annotating SailWind Layout with new components from the schematic You can change the search order of libraries using the Library List Dialog Box. See also Setting the Library List Order.  

