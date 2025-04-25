# Chapter 20 Object Linking and Embedding  

SailWind Logic object embedding capabilities enable design engineers to embed an object in a SailWind Logic design file and hold it within its framework. You can also embed a link to an outside object so that the linked object automatically updates each time you open the SailWind Logic database.  

![](/images/ce33b2dfde0e7c441b1c9d2f576c80b64e73b99e44f9b5840befdd87c7e60164.jpg)  

**Restriction:**  

The insertion of SailWind Logic, Layout or Router files as OLE objects in other files (including other SailWind files) is not supported. Any SailWind Logic, Layout or Router file inserted in another file will not behave properly and cannot be edited within the “container” application (Visual Editing).  

You can insert other files or other applications as linked or embedded objects within a SailWind Logic schematic. You can insert a Microsoft Word document, a Microsoft Excel spreadsheet containing a Bill of Materials, video or audio clips, and so forth. SailWind Logic does not need to understand the format of the inserted object; SailWind Logic communicates with the application that created the file and that source application tells SailWind Logic what information to display and how to display it.  

![](/images/3085040a951bf5c84cd15385beca87d94f34c50ffceeed09b431bd9dfd4e1f96.jpg)  

Tip You cannot insert or modify OLE linked or embedded objects in the Part Editor.  

Insertion of OLE Objects in SailWind Logic   
Embedding a Text Document   
Turning Off the Display of OLE Objects   
OLE Object Selection   
Moving and Sizing OLE Objects   
Changing an OLE Object's Icon or Label   
Converting an OLE Object to Another Type   
Edits of OLE Objects   
OLE and Print/Plot   
Deleting OLE Objects   
Redraws of a Screen Containing OLE Objects   
OLE and View Menu Commands   
Changing the OLE Object Background Color   
Saving OLE Objects  

## Insertion of OLE Objects in SailWind Logic

When you insert an OLE object in a SailWind Logic schematic, you can choose to either embed it or link to it.  

• An embedded object resides in the schematic, and can be accessed only from within SailWind Logic. An embedded Word object, for instance, can be opened and edited only from the schematic it resides in. A linked object resides on disk, and can be opened in its appropriate application either via SailWind Logic or directly from the disk. It is not copied permanently into the schematic, but is read in from disk each time the schematic is opened.  

![](/images/b91ee93636a8d6bdc470b939c7980f9c15264b11fde7d8a6ffa947894d38a93e.jpg)  

**Restriction:**  

Insertion of SailWind Logic, Layout or Router files as OLE objects in other files (including other SailWind files) is not supported. Any SailWind Logic, Layout or Router file inserted in another file will not behave properly and cannot be edited within the “container” application (Visual Editing).  

There are three ways of inserting an OLE object in a SailWind Logic schematic:  

Insert a new (empty) embedded object, and then create the object's content. For instance, insert a new Word document, then edit it with Word from within the schematic. Insert a copy of an existing application or file as an embedded object. Embedded objects are not updated when the original file is updated. • Insert a link to an existing application or file as a linked object. Linked objects are updated whenever the file they link to is updated.  

The following sections of this topic describe how to insert OLE objects in a SailWind schematic:  

Inserting a New Embedded OLE Object Inserting an Existing File as an Embedded Object Inserting an Existing File as a Linked Object  

### Inserting a New Embedded OLE Object

You can insert a new embedded OLE object in a SailWind Logic schematic. By embedding the object, it is not affected by changes made to an external source file.  

**Procedure** 

1. Click the Edit > Insert New Object menu item.   
2. From the Insert Object dialog box, select Create New.   
3. From the Object Type list box, select the type of OLE object you want to create.  

![](/images/32cd8f14450f32dd61014d87ee4a77596b6c24afadce30bba47442304fa4b261.jpg)  

!Tip  

You can only create new OLE objects using applications that are installed and registered on your system and are OLE servers. Most OLE servers are Microsoft products, such as Word or Excel.  

4. To display the new object in the schematic as an icon, check the Display As Icon check box.  

The icon that will be displayed appears beneath the check box.  

Uncheck the check box to display the entire object; for example, to display the actual Word document instead of a Word icon.  

5. Click OK. The application associated with the object type you selected opens, and you can edit on page 364 the new object's content:  

6. If the application is an OLE Linking and Embedding Server, it opens inside SailWind Logic, but runs in the background. The application's toolbar takes over SailWind Logic's toolbar. You can then work with the source application as you would if it was started outside SailWind Logic. This is called Visual Editing.  

Click outside the object, and the SailWind Logic toolbar takes over again. You can continue to design in SailWind Logic. The application continues to run in the background; therefore, you can click on the object and work in the source application at any time.  

If the application associated with the object is not an OLE Linking and Embedding Server, the application opens in a new window.  

7. When you are finished editing, close the object. You can reopen the object at any time by doubleclicking on it.  

### Inserting an Existing File as an Embedded Object

An existing file inserted in a SailWind Logic schematic as an embedded object is a copy of the source file it is created from. It is not linked to the original source file, is not updated when the source file is changed, and can be accessed only from SailWind Logic.  

**Procedure** 

1. Click the Edit > Insert New Object menu item.   
2. From the Insert Object dialog box, select Create from File.   
3. In the File edit box, type the pathname of the file to insert, or click the Browse button to search for the file.   
4. Uncheck the Link checkbox to insert the OLE object as an embedded object.   
5. To display the object as an icon in the schematic, check the Display As Icon check box. The icon that will be displayed appears beneath the check box. Uncheck the check box to display the entire object; for example, to display the actual Word document instead of a Word icon.  

6. Click OK. The object is inserted in the schematic.  

### Inserting an Existing File as a Linked Object

An existing file inserted in a SailWind Logic schematic as a linked object is merely a link to the source file on the disk. The file is not copied permanently into the schematic, but is read in from disk each time the schematic is opened. It can be opened from within SailWind Logic, or directly from the disk.  

**Procedure** 

1. Click the Edit > Insert New Object menu item.   
2. From the Insert Object dialog box, select Create from File.   
3. In the File edit box, type the pathname of the file to insert, or click the Browse button to search for the file.   
4. Check the Link checkbox to insert the OLE object as an linked object.   
5. To display the object as an icon in the schematic, check the Display As Icon check box. The icon that will be displayed appears beneath the check box. Uncheck the check box to display the entire object; for example, to display the actual Word document instead of a Word icon.   
6. Click OK. The object is inserted in the schematic.  

## Embedding a Text Document

Using OLE, you can embed a text document in your schematic to more quickly add multiple lines of text since the Create Text tool on the Schematic Editing Toolbar only allows single lines of text.  

Embedding is recommended over linking since the embedded document will reside inside the .sch file and can’t get lost or accidentally deleted as an external file.  

You can see a sample of this in the preview.sch sample design. See the Notes section on the lower left corner of sheet 1. Double-click the text to activate the Microsoft Word document.  

**Restrictions and Limitations**  

• OLE objects can only be printed. They cannot be plotted by a pen or photo plotter. • OLE objects must be enabled in the print Options dialog box on page 606 to appear in the printout, but they will never be visible when viewing the Print Preview. • OLE objects can only be printed using a zero plot orientation.  

**Procedure** 

Follow the appropriate instructions in Insertion of OLE Objects in SailWind Logic.  

!Tip  

You can resize the object within your design when the object is active for editing.  

## Turning Off the Display of OLE Objects

SailWind Logic does not understand the format of an inserted object; it only communicates with the application that created the OLE linked or embedded object to display the information. If the application that created the linked or embedded OLE object is installed and registered on your system, then SailWind Logic calls upon that application to display the OLE object in SailWind Logic as it would appear in the source application. For example, a Word document can appear within SailWind Logic and the Word toolbars appear within SailWind Logic.  

If the source application is not installed and registered on your system, then SailWind Logic can only display the inserted OLE object as an icon. It cannot open or display the OLE object as it would appear in the source application. SailWind Logic also displays the OLE object as an icon if the object is an application.  

You may want to turn off the display of OLE objects when SailWind Logic contains many linked or embedded objects because the redraw speed can decrease. Redraw speed noticeably decreases if the OLE Linking and Embedding servers, or source applications, which actually display the OLE items are not optimized for remote display.  

**Procedure** 

1. Click the Tools > Options menu item, then in the Options dialog box, click the General category.   
2. Clear the Display OLE Objects check box. See also Options Dialog Box, Design Category.  

## OLE Object Selection

Selection of OLE objects in SailWind Logic operates differently than selection of other objects such as pads, nets, components and so forth.  

The differences are:  

• You cannot select more than one OLE object at a time.   
• You cannot use area select to select OLE objects.   
• Commands apply to selected OLE objects only, even if you also select SailWind Logic objects. OLE objects have selection priority over SailWind Logic components.   
• OLE objects are always on top; to select SailWind Logic items under an OLE object, you must move the OLE object.  

When you click on an OLE object in SailWind Logic, it behaves like a non-text item in a Word file. that is, it becomes a rectangular area with sizing handles to indicate that it is selected. (Sizing handles are small, black squares that appear at the corners and along the sides of a rectangular area surrounding a selected object.)  

Right-click a selected OLE object to access a shortcut menu that lists all commands that you can apply to the OLE object.  

## Moving and Sizing OLE Objects

Move and resize OLE linked or embedded objects just as you resize non-text objects in Word.  

**Procedure** 

Select the object.  

• To move the OLE object, click and hold the left mouse button. Move the cursor to move the object. Release the mouse button once the object is in the correct location.   
• To size an OLE object, click and hold the left mouse button on one of the sizing handles. Move the cursor; the object changes size according to the cursor movements. Release the mouse button when the object is sized correctly.  

## Changing an OLE Object's Icon or Label

You can change the icon that represents an embedded or linked object in your schematic. You can also change the descriptive label that is displayed below the icon.  

**Procedure** 

1. Click on the object to select it.   
2. Right click and select <object_type> > Convert to display the Convert Dialog Box.   
3. Click the Change Icon button to display the Change Icon dialog box.   
4. In the Change Icon dialog box, click an Icon radio button to select the icon for the object:   
5. Leave the Current radio button set if you want to keep the current icon but change the object's label.   
6. Click the Default radio button to change to the default icon.   
7. Click the From File radio button to select the new icon from a file. If no file is shown in the From File edit box, click the Browse button to search for the file containing the icon you want to represent the object. Then click on the desired icon in the list box.   
8. To change the object's label, edit it in the Label edit box.   
9. Click OK to return to the Convert dialog box.   
10. In the Convert dialog box, click OK to save your changes.  

## Converting an OLE Object to Another Type

You can change the file format of an inserted OLE object so that you can open it in the applications you use. You can change the format temporarily--for a single editing session, after which the object is saved in its original format--or permanently, so that the object is converted to--and saved in--the new format.  

**Procedure** 

1. Click on the object to select it.   
2. Right click and select <object_type> > Convert to display the Convert Dialog Box.   
3. In the Object Type list box, click the object type you want to convert the object to.   
4. Click Convert to or Activate as to specify the conversion mode: a. Click Convert to convert the object to the type selected in the Object Type box. The object will be converted to the new object type, and saved. b. Click Activate as to open the object as the type selected in the Object Type box. After you activate and edit the object, it returns to the current type.  

5. To display the inserted object in the schematic as an icon, check the Display As Icon check box.  

The icon that will be displayed appears beneath the check box.  

Uncheck the check box to display the entire object; for example, to display the actual Word document instead of a Word icon.  

!Tip  

If an object's source application is not registered on your system, then the object can be displayed only as an icon.  

## Edits of OLE Objects

You can perform a limited set of edits on an OLE linked or embedded object. These include copy, paste, delete, open, and convert OLE Objects.  

• Cut, Copy, and Paste SailWind Logic OLE Objects • Edit > Delete All OLE Objects — Enables you to remove all of the OLE objects in a design. The prompt, “All current OLE Linked and Embedded objects will be removed from this Design. Do you want to continue?”, appears.  

Edit OLE Links • Open, Edit, Convert OLE Objects • Editing an OLE Object’s Content in SailWind Logic  

Cut, Copy, and Paste SailWind Logic OLE Objects Edit OLE Links Open, Edit, Convert OLE Objects Editing an OLE Object’s Content in SailWind Logic  

### Cut, Copy, and Paste SailWind Logic OLE Objects

Editing an OLE linked or embedded object is similar to editing SailWind Logic objects. You can cut, copy, and paste OLE objects using the Cut, Copy, and Paste commands from the Edit menu. You must select the OLE object before you can edit the object. You can copy objects from one sheet to another.  

0 Tip You cannot cut, copy, or paste OLE objects when in the Part Editor.  

**Procedure** 

1. Copy or cut the OLE object as follows:  

a. Select the OLE object.   
b. Click Edit > Copy menu item (to copy the object) or the Edit > Cut menu item (to cut the object).  

2. Click the Edit > Paste menu item to paste the object.  

3. Relocate the pasted object as necessary.  

**Related Topics**  

Open, Edit, Convert OLE Objects Edit OLE Links  

### Edit OLE Links

You can edit a linked OLE object's link to change the source file, break the link to the source file, specify update options or manually update the linked object.  

• Change the object's source file (that is, link the object to a different file).   
• Break the link with the source file, making the linked object an embedded object.   
• Select the object’s update mode, that is, specify whether the object will be updated automatically (whenever the source file changes), or only when you execute an Update command.   
• Manually update the linked object.  

The following sections of this topic describe how to edit an object’s link:  

Changing a Linked OLE Object's Source File Breaking the Link to a Linked OLE Object's Source File Setting the Update Mode For a Linked OLE Object Manually Updating a Linked OLE Object  

#### Changing a Linked OLE Object's Source File

If your design objectives change, you can change the source file that an object links to.  

**Procedure** 

1. Click the Edit > Links menu item.   
2. From the list in the Links dialog box, select the object whose source file you want to change.   
3. Click the Change Source button.   
4. In the Change Source dialog box, browse for and select the new source file for the object, and click Open. The object is linked to the new source file.  

#### Breaking the Link to a Linked OLE Object's Source File

If you no longer want to be linked to a source object, you can break the link to an object’s source file so that it will not automatically update when the source file changes.  

!Tip  

Once an object's link has been broken, it cannot be reconnected.  

**Procedure** 

1. Click the Edit > Links menu item.   
2. From the list in the Links dialog box, select the object whose link you want to break.   
3. Click the Break Link button, and click Yes in the popup that appears. The link is broken and object becomes an embedded OLE object.  

!Tip  

If the object whose link you broke is iconized, to view the object you must first convert on page 362 it to a Picture object.  

#### Setting the Update Mode For a Linked OLE Object

You can set the update mode for a linked OLE object and choose between automatic or manual updating.  

**Procedure** 

1. Click the Edit > Links menu item.   
2. From the list in the Links dialog box, select the object whose update mode you want to set.   
   . Click the Automatic or Manual radio button to set the update mode: a. Click Automatic to have the object automatically updated when you open the SailWind Logic file, and whenever the source file changes. b. Click Manual to have the object updated only when you execute an Update command for the object.  

#### Manually Updating a Linked OLE Object

You can manually update a linked object whose update mode is set to Manual. (Objects set to Automatic update are automatically updated, so manually updating these objects has no effect.)  

**Procedure** 

1. Click the Edit > Links menu item.   
2. From the list in the Links dialog box, select the object you want to update.   
3. Click the Update Now button; the object is updated.  

**Related Topics**  

Open, Edit, Convert OLE Objects Cut, Copy, and Paste SailWind Logic OLE Objects Editing an OLE Object’s Content in SailWind Logic  

### Open, Edit, Convert OLE Objects

Once you insert an OLE object, the name of the object appears at the bottom of the Edit menu. For example, if you insert a video clip, Video Clip Object appears at the bottom of the Edit menu. If you highlight the Video Clip Object command, another menu appears listing all commands you can perform on the linked or embedded OLE object. For a Video Clip Object, you can click Play, Edit, or Open.  

![](/images/044ef5a05283bb16a7a1494854f2e770283157f8ab5ce245836db7692f77b775.jpg)  

!Tip  

The commands that appear for each object depend on the object type; therefore, a Word object will not have the same options that a video clip has.  

Some of the more common commands you will see relative to OLE objects are:  

Edit — Use Edit to edit the linked or embedded OLE object in SailWind Logic. You can edit the object using all of the source application's commands and tools.   
• Open — Use Open to open the linked or embedded OLE object in the source application. You can then edit the object within the source application.   
• Convert — You can convert an OLE object to another object. You can also convert the OLE object from displaying as an icon to displaying the actual object; for example, the Word documen instead of an icon. UseConvert to convert a linked or embedded OLE object to another type of object; for example, convert a Word document to a Word picture.  

![](/images/a20c16151ce9475a1929e760da52538bc740b29b920ec1634a655a6f7e2737cb.jpg)  

Tip The object's source application determines what the object can be converted to.  

**Related Topics**  

Edit OLE Links   
Edits of OLE Objects   
Cut, Copy, and Paste SailWind Logic OLE Objects Editing an OLE Object’s Content in SailWind Logic  

### Editing an OLE Object’s Content in SailWind Logic

You can edit an object’s content within SailWind Logic (known as in-place visual editing), or in a separate window. In either case, you edit its contents as you normally would using all of the source application's commands and tools.  

**In-place Visual Editing**

Visual Editing occurs when the source application for a linked or embedded OLE object opens within SailWind Logic. You can also edit an OLE object by opening the source application and editing the object in the environment in which it was created.  

To edit an object within SailWind Logic, double-click on the object.  

Click outside of the object to deactivate visual editing. Updates are automatically reflected in the object.  

Restriction: You cannot edit embedded SailWind programs within SailWind Logic with visual editing.  

![](/images/2904b7392dd47fa035eced103d3c88510c816140ecae5665f49b101b9987e62f.jpg)  

!Tip  

When choosing objects for in-place editing, the following exceptions may apply:  

• Linked objects cannot be edited in-place: they open in a separate window for editing. • If the container application does not support in-place visual editing, the object will open in a separate window.  

Separate Window Editing  

You can edit objects outside SailWind Logic, in a separate window. To edit an object outside SailWind Logic:  

Select the SailWind Logic object and click the Edit > (Linked) Document Object > Edit menu item. You can also select the (Linked) Document Object > Edit menu item from the popup menu. • Ctrl $^+$ double-click the OLE object to edit in the source application. The source application opens and you edit the object.  

To update the object in SailWind Logic:  

• Click the File > Update Document menu item. This forces a redraw of the object.  

• Set a preference for SailWind Logic OLE objects in the “Options Dialog Box, General Category” on page 595. When you select the Update on Redraw check box, the object in the container application will update whenever you perform a redraw in the separate editing window.  

For best performance clear this option.  

To return to the container application, select the File > Exit and Return to <host> menu item.  

!Tip  

If you want to save the object you edit in the separate window, you can click the File > Save Copy As menu item. The object is really a copy of the original, and this command lets you save this copy. You cannot open other files, create new files, or save original designs in the separate window.  

**Related Topics**  

Open, Edit, Convert OLE Objects   
Edit OLE Links   
Edits of OLE Objects   
Cut, Copy, and Paste SailWind Logic OLE Objects  

## OLE and Print/Plot

You can print OLE linked or embedded objects to any Windows-supported printer or plotter. You cannot photo plot or pen plot OLE objects. Also, OLE objects do not appear when previewing prints.  

See also Plotting Output.  

**Related Topics**  

Setting Up a Pen Plotter Setting Up a Photo Plotter Printing Output  

## Deleting OLE Objects

If they are no longer needed in your design, you can delete OLE linked or embedded objects.  

**Procedure** 

1. Select the OLE object to delete.   
2. Click the Edit > Delete menu item, or click the Delete key.  

![](/images/2ae1eb13ec1e2e10b48625b2c62eba4b4138050813c13da46e440ee5494fc35e.jpg)  

Tip When you delete a sheet with OLE objects on it, all of the OLE objects are also deleted.  

3. To delete all OLE objects in the design, click the Edit > Delete All OLE Objects menu item.  

This enables you to remove all of the OLE objects in a design.  

The prompt, “All current OLE Linked and Embedded objects will be removed from this Design. Do you want to continue?” appears.  

## Redraws of a Screen Containing OLE Objects

When SailWind Logic redraws, SailWind Logic components are redrawn first, then OLE linked or embedded objects are redrawn. OLE objects always redraw in the same order and always redraw after SailWind Logic objects; therefore, they always appear on top of SailWind Logic components.  

You can also choose to update linked and embedded objects when you redraw the work area using the Redraw OLE Objects check box on the Options > Global category. This option is grayed when no OLE objects exist.  

## OLE and View Menu Commands

You can use all of the View menu commands with OLE linked or embedded objects; you can zoom into and zoom out of the objects.  

## Changing the OLE Object Background Color

OLE linked or embedded objects are displayed with a solid white background. You may, in some cases, prefer to display the OLE object with a transparent background; for example, since a bitmap already contains a background, you may prefer to use a transparent background. If your object is a Word document, then you may prefer a white background because black text on a transparent background results in black on black, or an invisible object.  

**Procedure** 

1. Select the OLE object.   
2. Right-click and click White Background to change the background color. A check next to the command indicates that the object will use a white background.  

## Saving OLE Objects

Linked and embedded objects are automatically saved as part of the schematic when you save a SailWind Logic schematic. If you want to save OLE objects separately, use File > Export to save the objects in an .ole file. You can then use File > Import to import the objects into other designs.  

SailWind Logic .ole files can be opened in other applications that understand the .ole file format. For example, if you insert a Word document into SailWind Logic and then save the Word object, you can later open Word and open the Word documents stored in the SailWind Logic .ole file.  

**Procedure** 

1. Click the File > Export menu item.   
2. In the File Export dialog box,  select the location for the file from the Save in dropdown list.   
3. In the File name edit box, type a name for the OLE file you are saving.   
4. From the Save as type dropdown list box, select OLE Files (\*.ole).   
5. Type a name for the OLE file you are saving.   
6. Click Save.  

## 
