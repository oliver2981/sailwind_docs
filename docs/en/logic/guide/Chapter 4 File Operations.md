# Chapter 4 File Operations

Creating a New Schematic File
Saving a Schematic File
Opening a Schematic File
File Import and Export
Archiving Your Schematic
Creating a New Schematic File Saving a Schematic File Opening a Schematic File File Import and Export Archiving Your Schematic  

## Creating a New Schematic File  

You can create a new blank schematic file for your design. SailWind Logic uses previously-defined default settings to define the starting design configuration.  

**Prerequisites**  

• Use the File $>$ New menu item to clear the current schematic from memory and start a new schematic.  

**Procedure** 

1. On the main toolbar, click the New button. The prompt “Save old file before resetting?” displays.  

2. If you click No, a blank drawing sheet representing sheet 1 of the new schematic displays in the work area. If you click Yes, the Saving a Schematic File dialog box appears if the current schematic is untitled.  

As an alternative, you can also create a new file from the popup menu in Microsoft® File Explorer.  

a. In File Explorer, go to the folder where you want to create the file.   
b. Right-click, and then click the New $>$ SailWind Logic Schematic menu item. This action creates a new design file in the current folder.   
c. Type a name for the file and click Enter. Make sure the file has a .sch extension. This creates a zero byte file. When you open this file in SailWind Logic, SailWind Logic recognizes the zero byte file and performs a File $>$ New command using default.txt.  

## Saving a Schematic File  

Use the File $>$ Save (or Save As) menu item to write design information to a file. The File Save As dialog box displays the schematic files contained in the default \SailWind Projects folder. The list of displayed files includes those created in PowerLogic and SailWind Logic.  

Restriction: Files opened by another user are locked to any edits. See Opening a File That is Already in Use.  

The name of the currently open design is displayed in the File Name text box at the bottom of the dialog box. Click Save to save the file. If the filename exists, a prompt is displayed to overwrite the existing file. The filename default is displayed for new designs.  

You can also save a file by clicking the Save button on the Standard toolbar.  

**Related Topics**  

Opening a Schematic File Import File Types Exporting Files  

## Opening a Schematic File  

You can open a schematic file in different ways.  

**Restrictions and Limitations**  

Files opened by another user are locked to any edits. See Opening a File That is Already in Use on page 57.  

**Procedure** 

1. On the toolbar, click the Open button. The File Open dialog box displays the schematic files contained in the default \SailWind Projects folder. The list displays files according to the Files of type setting.   
2. Select “Schematic Files (\*.sch)” from the “Files of type” dropdown list.   
3. Select a schematic file and then click Open to load the design into SailWind Logic. As an alternative, you can also open a file by dragging the file from Windows Explorer and dropping it into the SailWind Logic window.  

**Related Topics**  

Creating a New Schematic File   
Import File Types   
Exporting Files  

## File Import and Export  

Using SailWind Logic, you can import different file types, including data from schematics created with other tools. You can extract design information from an open schematic and save it in an ASCII format compatible with the previous or current software version.  

Import File Types   
Importing a File   
Exporting Files   
OLE Object Import and Export   
ASCII File Format   
Exporting to ASCII Output  

### Import File Types  

SailWind Logic enables you to import different file types, including data from various formats and schematics created with other tools.  

You can use the import functions for the following:  

Insert data from various formats into the current schematic.   
Translate schematics created with other tools, and open them as new SailWind Logic schematics. This function invokes a non-GUI instance of the Symbol and Schematic Translator to translate a single design, using the default mapping files located in C:\<install_folder>\<version>\Settings (cadstar2pl.cnv, orcad2pl.cnv, pcad2pl.cnv, and protel2pl.cnv).  

For information on more complex translations, such as translating only selected files from a .DDB container, or translating with special mappings, see the SailWind Symbol and Schematic Translator Guide.  

Table 7. File Types Imported into the Current Schematic   


<table><tr><td>File Type</td><td>Description</td></tr><tr><td rowspan="2">ASCll File Format (*.txt)</td><td>PADS-format ASCll. The ASCll files you can import include those created from PowerLogic and SailWind Logic. Note: Beginning with PADS 9.0, die parts and flip chips are identified by</td></tr><tr><td>the Special Purpose settings in the Part Type rather than being designated by the DiE and FLP logic families. When you import an ASCll file created by a previous PADS version, these Special Purpose setings are automatically set for parts having the logic family DIE or FLP. The part's family designation remains the same.</td></tr><tr><td>OLE Import/Export on page 65(*.ole)</td><td>SailWind Logic enables you to embed files from other applications as OLE objects in your schematic using Edit/lnsert New Object. Once you have an OLE object in your design, you can export the object as a singular item to an .ole file using File Export (see</td></tr></table>  

Table 7. File Types Imported into the Current Schematic (continued)   


<table><tr><td>File Type</td><td>Description</td></tr><tr><td></td><td>Exporting Files). You can then import the .o/e file into other SailWind Logic schematics.</td></tr><tr><td>ECO files (*eco)</td><td>Similar to PADS-format ASCll. Each type of data begins with a header line with a key word surrounded by asterisks (*).</td></tr><tr><td>(.asc) files</td><td>SailWind Layout rules.</td></tr></table>  

Table 8. File Types Opened as New Schematics   


<table><tr><td>File Type</td><td>Description</td></tr><tr><td>CAD .csa files</td><td>CADSTAR Archive files (ASCII)</td></tr><tr><td>CADSTAR .scm files</td><td>CADSTAR Schematic files (binary)</td></tr><tr><td>OrCAD .dsn files</td><td>OrCAD Capture files</td></tr><tr><td>P-CAD .sch files</td><td>P-CAD Schematic files (ASCll & binary) generated in P-CAD 2002 & newer</td></tr><tr><td>Protel .sch files</td><td>Protel 99 Schematic files (ASCll & binary)</td></tr><tr><td>Protel .schdoc files</td><td>Protel DXP/Altium Designer Schematic files (ASCll & binary)</td></tr><tr><td>Protel .prjpcb files</td><td>Protel combined design/schematic files</td></tr></table>  

### Importing a File  

SailWind Logic supports the importing of different file types into the design environment.  

**Procedure** 

1. Click the File $>$ Import menu item.   
2. In the displayed prompt, Click Yes to save the existing design before importing the file, or No to import the file without saving changes.   
3. From the “Files of type” dropdown list, select the type of file you want to import.   
4. Select the file you want to import, then click Open. Import progress is reported in the Status bar, and logging messages and links to log files are displayed in the Output Window.  

**Related Topics**  

Exporting Files Opening a Schematic File Import Rules from PCB  

### Exporting Files  

Extract design information from an open schematic file and save it in an ASCII format compatible with the previous or current software version. You can also use Export to create default startup conditions for SailWind Logic.  

!Note:  

You can save all or some of the open design in ASCII format.  

**Procedure** 

1. Click the File $>$ Export menu item.   
2. From the “Save as type” dropdown list, select the type of file you want to export to.   
3. Type a name for the ASCII file in the File Name text box. The default is the name of the currently open design.  
4. Click Save.  

This opens the Exporting to ASCII Output Dialog Box. Select the appropriate check boxes to indicate the information that you want to write to the ASCII file.  

!Note:  

SailWind Logic enables you to embed files from other applications as OLE objects in your design by clicking the Edit $>$ Insert New Object menu item. After you have an OLE object in your design, you can export the object as a singular item to an .ole file.  

5. Select the SailWind Logic output version for your exported file.  

Beginning with PADS 9.0, die parts and flip chips are identified by the Special Purpose settings in the Part Type rather than being designated by the DIE and FLP logic families. With this change, the following changes occur when you export a design to an ASCII file of a previous PADS version:  

• The Special Purpose settings of any die parts and flip chips are cleared.   
• Die parts and flip chips having a family designation other than DIE and FLP lose their die part or flip chip special purpose and become normal parts.   
• Any normal parts that have the DIE or FLP family designation are treated as die parts or flip chips in the previous PADS version. For more information, see OLE Object Import and Export.  

**Related Topics**  

Import File Types Opening a Schematic File  

Saving a Schematic File Export Rules to PCB  

### OLE Object Import and Export  

You can import and export .ole files in SailWind Logic to add images, text files, and other objects created in other programs and link to or embed them into your design. You can also export images and objects from SailWind Logic so that they can be included in documentation or reports.  

Importing OLE Files Exporting OLE Files  

#### Importing OLE Files  

You can import an .ole file containing OLE objects into a SailWind Logic schematic, and you can export an OLE object from a schematic to an .ole file.  

**Procedure** 

1. Click the File $>$ Import menu item.   
2. Click Yes at the prompt to save your current design changes or click No to discard them.   
3. In the File Import dialog box, select “OLE Files (\*.ole)” as the file type to import.   
4. Browse to and select the file you want to open.   
5. Click Open and then click Yes at the prompt.   
   The OLE objects import into the current schematic.  

**Results**  

OLE objects are placed on the sheet on which they were created. For example, if you originally placed an OLE object on Sheet 1 and a second object on Sheet 2, these OLE objects are placed on Sheets 1 and 2 when imported.  

If some of the OLE objects you want to import exist on sheets that do not exist in the current schematic, these objects are deleted. For example, you originally created OLE objects on Sheets 1, 2, and 3. The schematic you are importing the OLE objects into only has Sheets 1 and 2. The OLE objects from Sheet 3 are deleted.  

#### Exporting OLE Files  

You can export OLE objects from SailWind Logic so that they can be utilized by other programs or other SailWind Logic design sessions.  

0 Tip Handles appear around the object when it is selected.  

**Procedure** 

1. Select an OLE object and click the File $>$ Export menu item.   
2. In the File Export dialog box, select OLE (\*.ole) as the file type.  

3. Name the file and select a location in which to save the file.  

4. Click Save. The .ole file is created and is available for import into other SailWind Logic schematics.  

0 Tip You can also import application files from other sources using the Edit $>$ Insert New Object menu item. You cannot import an .ole file.  

### ASCII File Format  

You can export SailWind design files to the ASCII file format to edit information outside of the SailWind design environment. The ASCII files for SailWind Logic are organized into sections, beginning with a keyword enclosed with an asterisk.  

The first section starts with $^{\star}\mathsf{S}\mathsf{C}\mathsf{H}$ , and gives the system setup parameters for the circuit.  

The second section, starting with $^{\star}{\mathsf{C A M}}$ , lists the default settings for the plot and printing outputs  

Following this, all of the data for each sheet is grouped together in the $^{\star}\mathsf{S H T}^{\star}$ section. This data starts with $^{\star}{\mathsf{C A E}}^{\star}$ , listing the window zoom setting and cursor location for the sheet.  

Table 9. ASCII File Formatting Sections   


<table><tr><td>Option</td><td>Description</td></tr><tr><td>*TXT*</td><td>Free text items in the sheet.</td></tr><tr><td>*LINES*</td><td>2D line items, including library entry.</td></tr><tr><td>*CAEDECAL*</td><td>Description of the CAE symbol decals for all parts in the sheet.</td></tr><tr><td>*PARTTYPE*</td><td>Description of the part types that appear in the sheet.</td></tr><tr><td>*BUSSES*</td><td>Description of buses in the sheet, including the name and location.</td></tr><tr><td>*PART*</td><td>List of all parts, including their atributes, which appear in the sheet. Gates and connector pins are each listed separately.</td></tr><tr><td>*OFFPAGE REFS*</td><td>List of all off-page flags in the sheet. This includes power and ground symbols and bus connections.</td></tr><tr><td>*TIE-DOTS*</td><td>List of all tie-dots in the sheet.</td></tr><tr><td>*CONNECTION*</td><td>List of the connections in the sheet, with the signal name and path.</td></tr><tr><td>*NETNAMES*</td><td>List of all net names that are displayed in the schematic.</td></tr></table>

After all sheets are listed, the file ends with \*END\*.  

### Exporting to ASCII Output  

Define what information you want to write to an ASCII file.  

**Procedure** 

1. Click the File $>$ Export menu item.  

2. Type a name for the output file, and then click Save.  

!Tip  

The filename and path appear at the bottom of the ASCII Output dialog box.  

3. In the ASCII Output Dialog Box, select items in the “Select Sections to Output” area to appear in the ASCII file.  

You can click Select All to select all items, or click Unselect All to clear all selections.  

4. In the SailWind Logic Output Version area, select the appropriate version of the software you are using from the list.   
5. Click OK.  

## Archiving Your Schematic  

You can create a folder, a PDF, and/or a .zip file that contains all of your schematic files and supporting files. This includes the schematic itself, a design file, libraries, and any additional files or folders you want. You choose what to archive; all fields are optional.  

**Procedure** 

1. Open the schematic you want to archive.   
2. Click the File $>$ Archive menu item.   
3. Select the files and folders you want to archive in the Archiver Dialog Box.   
4. Click OK.  

**Results**  

An archive folder that contains the design and/or schematic files, the libraries, and any additional files and folders you have indicated is created.  

If you chose to compress the files, the .zip file is the only file in this folder.  

If you chose to create a PDF, the file is created using the schematic name and placed in the archive folder.  

If you chose to compress the files using the zip format, a .zip file is created in the following format:  

<project_name>YYYYMMDDHHMMSS.zip  

File Operations Archiving Your Schematic  

Where YYYY is the year, MM is the month, DD is the day, HH is the hour (using a 24-hour format), MM is the minute, and SS is the second of the exact time you created the file. The file contains the same folder structure as the archive folder.  

