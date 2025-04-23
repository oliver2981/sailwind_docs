# Chapter 3 User Interface  

The software interface is robust and configurable. It offers numerous methods for viewing and navigating your designs, as well as extensive capabilities for generating custom macro scripts for playback and debugging.  

View Control   
Project Explorer   
Output Window   
Opening a File That is Already in Use  

# View Control  

You can use several methods to control which portion of the database is visible on the screen.  

View Commands and Scroll Bars Middle Mouse Button Numeric Keypad Saving and Restoring Views  

# View Commands and Scroll Bars  

There are a number of different ways to interact with the design environment to control the view of the design. SailWind Logic provides a comprehensive set of commands to enable you to pan and zoom within the design including using the mouse buttons/wheel, keyboard shortcuts and various items on the View menu.  

To control the view, use the scroll bars or the following commands in the View menu:  

• Click the View $>$ Zoom menu item, or the Zoom button on the toolbar to enter Zoom mode. ◦ To zoom in, position the cursor at the desired view center, and click the left mouse button. ◦ To zoom out, position the cursor at the desired view center, and click the right mouse button. ◦ To define a specific view area, position the cursor at the desired view center, click and drag to define the extents, and release. Click the View $>$ Redraw menu item, or the Refresh button on the toolbar to redraw the current view.   
Click the View $>$ Sheet menu item, or the Sheet button on the toolbar to display the entire sheet.   
Click the View $>$ Extents menu item to resize the view to display all objects in the design.   
• Use the scroll bars to pan the view.  

# Middle Mouse Button  

You can use the middle mouse button to perform a number of viewing operations.  

Use the middle mouse button to perform panning and zooming operations:  

To pan, click the middle mouse button. The view is centered at the cursor. To zoom in, click and hold the middle mouse button. Drag the cursor diagonally up. To adjust the bounding box, move the mouse. When you release the middle mouse button, the area within the bounding box displays.  

To zoom out, click and hold the middle mouse button. Drag the cursor diagonally down. This draws an inner box, representing the current view. Moving the cursor adjusts the outer box, which represents the new view. The relative size of the outer box to the inner box determines how far the view zooms out. Release the middle mouse button to complete the zoom out operation.  

• To view the entire design, click and hold the middle mouse button, drag the cursor horizontally, and release.  

# Numeric Keypad  

Use the numeric keyboard to control the view.  

For more information, see Using the Numeric Keypad to Control the View.  

# Saving and Restoring Views  

If you repeatedly pan or zoom to a particular area of your design, you can save time by saving a work area view so that you can instantly restore it when needed.  

Restriction: Capture is not available while in the Part Editor.  

Saving a View Restoring a View  

# Saving a View  

You can save a view of your design for later recall.  

**Procedure** 

1. Arrange the work area to display the view you want to capture.  

2. Click the View $>$ Save View menu item.  

0 Tip In the Save View dialog box, the preview shows you the location of the selected view in relation to the extents of the design.  

3. In the Save View dialog box, click Capture.  

4. In the “Capture a new view” dialog box, type a new name for the view and then click OK. The new view name is listed in the View Name list.  

![](/images/3edc16b8106f10a910d49ffba7d17b600afa1254fbcd65639a8c1261b5d1b53a.jpg)  

Tip You can create up to nine views. The view names appear at the bottom of the View menu.  

5. Click Close.  

# Restoring a View  

You can restore a previously saved view.  

**Procedure** 

1. Click the View $>$ Save View menu item.   
2. Select a name from the View Name list and click Apply to apply a previously selected view to the work area. Tip   
   When you apply a view, the previous view saves automatically. Click the View $>$ Previous View menu item to restore the view.  

3. Select a name from the View Name list and click Delete to remove it from the View Name list.  

# Project Explorer  

The Project Explorer lists the objects in your design in a hierarchical structure. When you update your design, the hierarchical structure also updates automatically.  

Restriction: The Project Explorer is unavailable in the Part Editor.  

Note: To open the Project Explorer, click the Project Explorer button.  

You can configure the Project Explorer so you can click on a listed object to select it in the workspace, or select it and zoom to it.  

**Procedure** 

1. Right-click in Project Explorer, and click the Allow Selection menu item. A check mark indicates that the functionality is enabled.   
2. If you want to Zoom to the object you select, click the Zoom to selection menu item. A check mark indicates that the functionality is enabled.  

# Output Window  

Use the Output window for viewing reports and session logs, macro editing and debugging, and custom programming and debugging.  

The Output window is located in the lower left section of the display window. You can dock or float the Output window. You can also open or close the Output window.  

The Output window has two tabs:  

• Status Tab — Displays information on the current session.   
Macro Tab — Enables you to run, edit, and debug scripts.   
Session Log Management   
Macros   
Macro Playback   
Macro Script Debug   
Accessing Help on the Macro Language   
CIS  

# Session Log Management  

Various methods are available for managing the session logs, including filtering, viewing, printing and saving the log data.  

Session Log Navigating Pages in the Status Tab Filtering the Status Tab Display Searching in the Status Tab Printing Session Log Messages Viewing and Printing Reports Saving a Session Log to File Clearing the Session Log Display  

# Session Log  

A session log, which appears in the Status tab of the Output window, contains all program output for the current session, including names of open and saved files, integrity test results.  

The session log file messages in the Status tab are color coded by subject. Underlined items are links. The color codes are shown in the following table:  

Table 3. Session Log Text Color Meanings   


<table><tr><td>Color</td><td> Meaning</td></tr><tr><td>Red</td><td>Errors</td></tr><tr><td>Green</td><td>Warnings</td></tr><tr><td>Black</td><td>Messages</td></tr><tr><td>Blue</td><td>Links to files, Web pages, and database objects</td></tr></table>  

# Navigating Pages in the Status Tab  

Use the Status tab toolbar buttons in the Output window to navigate to the previous or next page, and to refresh a display of reports and other pages. You can also stop updates to pages, and return to the session log display.  

To perform these functions, use the following Status tab toolbar buttons:  

Table 4. Status Tab Toolbar Buttons   


<table><tr><td>Command</td><td>Description</td></tr><tr><td>Back</td><td>Displays the previous page.</td></tr><tr><td>Forward</td><td>Displays the next page.</td></tr></table>  

Table 4. Status Tab Toolbar Buttons (continued)   


<table><tr><td>Command</td><td>Description</td></tr><tr><td> Stop</td><td>Stops page updates.</td></tr><tr><td>Refresh</td><td>Refreshes the display of reports and other pages.</td></tr><tr><td>Home</td><td>Returns to the session log.</td></tr></table>  

# Filtering the Status Tab Display  

The session log file messages in the Status tab are color coded by subject. You can choose to view any combination of the color coded messages.  

Use the following procedure to filter the display in the Status tab.  

**Procedure** 

1. Right-click in the Output window and click one of the following commands from the Filter popup menu item:  

Table 5. Filter Submenu Commands   


<table><tr><td>Command</td><td>Description</td></tr><tr><td>Error</td><td>Displays errors.</td></tr><tr><td>Warning</td><td>Displays warnings.</td></tr><tr><td>Message</td><td>Displays messages.</td></tr><tr><td>Show all</td><td>Displays all items (errors, warnings, and messages).</td></tr></table>  

2. Select an item to show it; clear the item to hide it.  

# Searching in the Status Tab  

If you want to locate a specific item or term in the log, you can search for text in the Status tab. There are options available to search for whole word only and specific case matches.  

**Procedure** 

1. Right-click and click the Find popup menu item.   
2. In the Find dialog box, type the text you want to find in the dialog box and complete any other dialog box options.   
3. Click Next. The tab scrolls to the occurrence of the word, highlighting the word.  

# Printing Session Log Messages  

You can print a hard copy of the session log for review purposes.  

**Procedure** 

1. Right-click and click Print.   
2. In the Windows standard Print dialog box, set options as needed.   
3. Click Print.  

# Viewing and Printing Reports  

The session log contains links to reports that you can view and print.  

To view the report, click the link. The report appears replacing the session log as the active page in the Status tab.  

You can print the displayed report.  

**Procedure** 

1. Right-click the displayed report and click Print.  

![](/images/485e025aee2149de661b75e1e0a6bc717e2dec6012511387dc4868d2a60e3877.jpg)  

Tip As an alternative, on the Status tab toolbar, click the Print button.  

2. In the Windows standard Print dialog box change any Print dialog box options as needed.  

3. Click Print.  

# Saving a Session Log to File  

There are times when you might want to refer to something that was documented in the session log (such as when debugging a file or submitting a Support Center request. You can save a session log to a file for future reference.  

**Procedure** 

On the Status toolbar, click the Log to File button to save the session log for future reference.  

If a session log file already exists, new information is appended. If a session log file does not exist, a new file is created.  

The default path for the session log comes from the .ini file entry:  

FileDir $\mathtt{\Gamma}=\mathtt{C}$ :\SailWind Projects  

When you first start the software, the location is set in the following registry key:  

HKEY_CURRENT_USER\Software\Mentor Graphics\<version>\SailWind Layout\Status Window\LastLogName  

# Clearing the Session Log Display  

You can clear a session log when it is no longer needed.  

**Procedure** 

Right-click and click Clear to clear the session log display each time you open a file.  

**Results**  

This prevents you from viewing information from a previously opened file. It does not delete the log file.  

# Macros  

You can create macros to simplify redundant activities. You can record any set of procedural steps for replay as a single action. You can also nest macros.  

![](/images/693e72d7f1168195f68c78815669cc65bc602cb2cbaf444b346c3d237906c74b.jpg)  

!Tip  

Dialog box actions are recorded as results rather than actions, so when you replay, you don't see the dialog boxes in the replay process. Because of this you can't create a macro that stops on an open dialog box; it must follow through to some result or action. For example, you can create a macro that selects the File $>$ Open menu item, selects a file, and selects OK. The macro, when played back, opens a file.  

Creating a New Macro   
Recording Mouse Movements   
Opening an Existing Macro File   
Viewing Multiple Open Macros   
Editing a Macro   
Changing the Default Text Editor   
Saving the Macro  

# Creating a New Macro  

Macros can be very flexible and helpful beyond your current design session. You can create a new macro by recording your keystrokes, mouse movements and commands and then save it for later recall.  

**Procedure** 

1. On the main toolbar, click the Output Window button.   
2. On the Macro tab, click the New button. New macros are given a name of Macro#, where # is a numeric sequence such as Macro1 or Macro2.   
3. If desired, click the Compress mouse moves and/or Relative mouse moves buttons. See Recording Mouse Movements for more information.   
4. On the Macro tab toolbar, click the Record button.   
5. Perform the keystrokes, commands, and mouse clicks to include in the macro.   
6. On the Macro tab toolbar, click the Stop button. Alternatively, you can also script a macro instead of recording mouse actions.  

# Recording Mouse Movements  

Mouse movements are recorded in macros. You can record compressed or uncompressed mouse movements and relative or absolute movements.  

Compress Mouse Mode — Compress mouse mode records only the start point and endpoint of a mouse movement. It does not record any of the intermediate coordinates between the start and end points. Compression is recommended under most circumstances because it significantly reduces the size of your macro file. Recording intermediate mouse movements increases the file size, but documents coordinate information if required for a special application.  

Relative Mouse Mode — Relative mouse mode records the start point and endpoint of a movement in incremental coordinates instead of absolute coordinates.  

# Opening an Existing Macro File  

Macros are created in and stored in macro files that have a .mcr extension. To open an existing macro file (.mcr), you can use the menus or the toolbar.  

You can open multiple macros in the macro editor. The macro editor also supports nested macros.  

**Procedure** 

1. On the main toolbar, click the Output Window button; then, in the Output window, click the Macro tab. 2. Click the Open button, or select the macro file in the Open File dialog box and click Open.  

# Viewing Multiple Open Macros  

You can switch your view between multiple open macros. This enables you move back and forth between more than one macro without having to open and close them individually.  

**Procedure** 

Click a macro in the List of Open Macros area (left-hand pane) of the Macro tab to switch between open macros.  

# Editing a Macro  

You can copy or cut selected text to the Clipboard. You can also paste the selection from the Clipboard into the text window. You can paste text from the Clipboard into other applications. You can also switch between open macros to edit multiple macros.  

![](/images/65a927d196cad38e7667d7905a6818115b8071b09a312de0ca82a2bb618d59cb.jpg)  

**Restriction:**  

If you have Notepad as the default text editor, longer macro files may not be loaded because of size constraints in Notepad. See Changing the Default Text Editor for information on how to change the default text editor.  

**Procedure** 

1. Select the text you want to copy or cut.   
2. On the Macro tab toolbar, click the Copy or Cut buttons.   
3. Place the pointer at the insertion point where you want to place the copied text.  

4. On the Macro tab toolbar, click the Paste button.  

You will see that your selection has been pasted in the Output window at the insertion point.  

As an alternative, right-click in the Output window and click Copy, Cut, or Paste.  

# Changing the Default Text Editor  

To access large files using Edit, you must install an ASCII text editor with a suitable file size capacity.  

**Procedure** 

1. Open the SailWindlogic.ini file in a text editor.   
2. Modify the [general] section, specifying a new text editor executable name. Include the drive and folder if the new editor is not in your Windows folder.   
3. Save the.ini file and close the text editor.  

# Saving the Macro  

Macros are not limited to your current design session. You can save a macro for future recall.  

**Procedure** 

1. Click the Save button.   
2. In the standard Windows “Save As” dialog box, enter a filename, if necessary, and click Save.  

**Related Topics**  

Using Command Line Switches with Macros [SailWind Logic Command Reference Manual]  

# Macro Playback  

You can play back an existing macro using Run. Run also resumes the playback of a paused macro.   
When you play a macro, you cannot use the mouse in the workspace.  

Playing Back a Macro Pausing a Playing Macro Stopping a Playing Macro  

# Playing Back a Macro  

Once a macro has been recorded, you can play it back.  

**Procedure** 

1. On the Macro tab, click the Open button and open a macro (.mcr) file. Recent macros can be found by clicking the Tools $>$ Macros menu item, and then selecting the desired macro from the list.   
2. On the Macro tab toolbar, click the Run button. As an alternative, right-click in the Macro tab and click Run.  

# Pausing a Playing Macro  

You can pause a macro during playback.  

**Procedure** 

1. On the Macro tab toolbar, click the Pause button to pause a playing macro at any time.   
2. Click the Play button to resume playing the macro.  

# Stopping a Playing Macro  

You can stop a macro that is currently playing.  

**Procedure** 

Right-click in the Macro tab and click Stop or on the Macro tab toolbar, click the Stop button to stop a playing macro.  

You cannot resume the playback of the macro once you have stopped it. When you click Run, the macro starts from the beginning.  

**Related Topics**  

Using Command Line Switches with Macros [SailWind Logic Command Reference Manual]  

# Macro Script Debug  

When playing back a macro, you can run it step-by-step, or to a certain location in the script. To perform these debugging tasks, insert breakpoints in the macro at the points at which you want the macro to stop  

Setting or Removing Breakpoints Debugging the Macro Scripts Run-Time Error Correction  

# Setting or Removing Breakpoints  

The ability to set or remove breakpoints is useful when you debug a macro. If the macro engine encounters a breakpoint when playing back a macro, it pauses the macro.  

**Procedure** 

1. Place the cursor on the line in which to add a breakpoint.   
2. Right-click in the Macro tab and click Toggle Break, or as an alternative, on the Macro tab toolbar, click the Toggle Breakpoint button. This inserts a breakpoint at the current cursor location. A breakpoint marker appears in the gutter area. When the macro engine encounters a breakpoint while playing back a macro, it pauses the macro. The next line in the macro is marked with the instruction pointer.  

# Debugging the Macro Scripts  

Once breakpoints are inserted, you can debug macros.  

Play a Single Line of the Macro   
Perform a Subroutine Call on the Current Line   
Play Back a Macro to a Point   
Return From the Subroutine to the Point From Which it was Called   
Continue the Execution From the Current Point  

# Play a Single Line of the Macro  

You can play a single line of a macro by using a button on the Macro tab toolbar or the right mouse button menu command.  

**Procedure** 

Right-click in the Macro tab and click the Step Over menu item, or on the Macro tab toolbar, click the Step Over button  

# Perform a Subroutine Call on the Current Line  

You can perform a subroutine call on the current line by using a button on the Macro tab toolbar or the right mouse button menu command.  

**Procedure** 

Right-click in the Macro tab and click Step Into menu item, or, on the Macro tab toolbar, click the Step into button.  

# Play Back a Macro to a Point  

You can play back a macro to a point by using a button on the Macro tab toolbar or the right mouse button menu command.  

**Procedure** 

Right-click in the Macro tab and click the Step to Cursor menu item, or click the Step to cursor button on the Macro tab toolbar.  

# Return From the Subroutine to the Point From Which it was Called  

You can return from the subroutine to the point from which it was called by using a button on the Macro tab toolbar or the right mouse button menu command.  

**Procedure** 

Right-click in the Macro tab and click the Step Out menu item, or, on the Macro tab toolbar, click the Step out button.  

# Continue the Execution From the Current Point  

You can continue the execution of a macro from the current point by using a button on the Macro tab toolbar or the right mouse button menu command.  

**Procedure** 

Right click in the Macro tab and click the Run menu item, or, on the Macro tab toolbar, click the Run button.  

# Run-Time Error Correction  

If run-time errors occur, the macro debugger switches to step-by-step mode and displays a detailed message on the status bar. The instruction pointer is set on the line that produced the error. After fixing the error, you can resume playback of the macro.  

**Related Topics**  

Using Command Line Switches with Macros [SailWind Logic Command Reference Manual]  

# Accessing Help on the Macro Language  

You can access help on the macro language at any time.  

**Procedure** 

Click in the edit area of the Macro tab and press F1 for information on the term and a sample script.  

# CIS  

The CIS tab displays part information from CIS as indicated. You can:  

1. Speficy a new configuration for data source to use and choose what to display in the CIS tab.   
2. Search and add part(s) from CIS.   
3. Compare part attributes in design with those in CIS to check the consistency.  

Adding a New Configuration   
Adding Parts from CIS   
Comparing Part Attributes for Consistency Checking  

# Adding a New Configuration  

After launch, SailWind Logic automatically connects to the specified data source, from which to load data into the CIS tab.  

Follow the steps below to specify a new configuration and choose what to display in the CIS tab.  

**Procedure** 

1. On the CIS tab toolbar, click the New button.   
2. In the Library Config dailog box, add and connect to the target data source as follows: a. Click ODBC Config. b. Add an ODBC data source to use in the pop-up window. c. Click Update to make the newly added data source active and available in the ODBC DSN list. d. Select the target database from the list to establish connection and load its table list in the Database Tables area.  

3. Select the database table(s) to use by checking the To CIS checkbox.  

Only those selected will be available in the CIS tab.  

4. In the "Table Configuration" area, specify what and how table fields are displayed in the CIS tab. For more information, see the table below.  

Table 6. Table Configuration Description   


<table><tr><td>Name</td><td>Description</td></tr><tr><td>Field Name</td><td>Lists all fields in the table selected on the left.</td></tr><tr><td>Field Type</td><td>Specifies what type the table fields belong to from the drop-down list, wherein:</td></tr></table>  

<table><tr><td> Name</td><td>Description</td></tr><tr><td></td><td>· Part_Type is mandatory, based on which to load data into the CIS tab. Besides, you can see schematic symbol and PCB decal assigned to the part type in the local libraries from the CIS preview window. · Part_Number is mandatory, based on which to check whether part attribute values in design are identical with those in CIS. · Category allows to show table structure hierarchically by subcategories in the CiS tab. · All field types except Normal must be unique.</td></tr><tr><td>Field Alias</td><td>Specifies the table heading for each field to display in the Cis tab. · Field aliases corresponding to Field Type "Part_Type" and "Part_Number" are defined by default, and no modification is allowed. · If nothing is set, Field Name will be used instead.</td></tr><tr><td>Transfer to Design</td><td>Specifies to add the Field Name to the part attributes. If yes, you can see it in the Part Attributes list by checking part properties in the design. Tip</td></tr><tr><td>Visibility in CIS</td><td>When set, Field Alias will be used instead. Specifies to display Field Name in the Cis tab. When set, Field Alias will be used instead.</td></tr><tr><td>Key</td><td>Reserved</td></tr><tr><td>Browsable</td><td>Specifies to add hyperlinks to the field contents in the Cis tab, which often links to such reference files as datasheets and drawings.</td></tr><tr><td>Property Checking</td><td>Specifies attribute(s) to compare in the Part Manager Dialog Box, checking whether the attribute values in design are identical with those in CiS.</td></tr></table>  

5. Click Save to save the configuration.  

SailWind Logic automatically connects to the data source and loads specified information into the CIS tab.  

# Adding Parts from CIS  

After configuring data source as needed, you can check and use CIS data in the design. To locate parts effeciently, SailWind Logic provides you with filter feature. This section dsecribes how to use CIS data.  

**Procedure** 

1. Connect to the target data source and specify the table fields to display, as described in "Adding a New Configuration". 2. In the CIS tab, select a table on the left, and view its part information on the right.  

2. Use the filter to locate parts, and click Search to activate the filter. Parts that match the search filter settings are displayed.  

Filtering by feild name and keyword is supported, whereas wildcard or expression is not currently supported.  

4. Select a part and check its part type (CAE decal) and PCB decal in the preview window.  

5. Add a part to the design as follows:  

a. Double-click the target part in the table. The part attaches to and follows the cursor movement.   
b. Click on the schematic to place the part; another instance attaches to the cursor automatically.   
c. Press the Esc key when you are done adding the part(s).  

6. Select the part in the design, right-click and click the Attributes popup menu item. In the attributes list, you can see attribute(s) added by "Transfer to Design" feature in the Library Config Dialog Box.  

# Comparing Part Attributes for Consistency Checking  

Use the Part Manager to compare part attributes in design with those in CIS to check the consistency. For inconsistent attributes, you can update from CIS with multiple options. You can also specify the attributes to compare.  

**Procedure** 

1. Check that all attributes to compare are selected in the Library Config Dialog Box.  

2. On the CIS tab toolbar, click the Part... button to activate the comparision.  

![](/images/cc9c02e5132a2c05d0426c19f286f07061055e6270efbbf0bf1f326a93024a06.jpg)  

Note: The comparision is conducted on the basis of CIS attribute Part_Number.  

3. Check the search results in the Part Attribute Info. area, where errors are highlighted in red. You can also:  

• Use the filter to search for specific part(s) by the reference designator, schematic sheet, part number, error type, or the Show Error Only button.  

Note:   
Filtering by Component Name or Part Number is case-sensitive and no wildcard or expression is currently supported.  

• Click on any item in the table, and in the "Comparision Results" area see respective attribute values assigned in design and CIS, with differences highlighted in red.  

4. Update inconsistent schematic part attribute(s) from CIS in either of the following ways, which takes effect only on parts found with "Attribute is not equal" error.  

• Click Update All to update all inconsistent part attributes from CIS. Select one or more items in the table, and click Update the Selected to update the inconsistent attributes of the selected parts only. Use Ctrl for multiple selections.   
• Update attribute(s) for a specific part in the "Comparision Results" area, with two available options: • Update the selected attribute: Right-click on the attribute cell and click the Update Selected Attribute From CIS popup menu item • Update all attributes: Right-click and click the Update Selected Part From CIS popup menu item  

# Opening a File That is Already in Use  

The SailWind products help you avoid making changes to a file that is already opened by another user.  

The first user to open a file in a shared location becomes the owner of the file for the duration the file is open; the file is locked to all other users. If you try to open a file that someone else has already opened, you will get a warning message letting you know the current owner and the name of the computer from where the file is locked. You have the option to view a read-only version of the file but you will not be able to update it while the owner still has it open. You can save the file with another name using Save As.  

Use the file operations to create and save a new schematic file. You can also open and save existing designs, import and export files from other file formats, and archive your schematics.  

