# Chapter 2 Getting Started With SailWind Logic  

The SailWind Logic workflow guides you through the steps necessary to create a schematic design.  

SailWind Logic Flow   
Startup Options   
Adding Startup Options to a Shortcut   
SailWind Updates   
Migrating User Settings   
Customizing SailWind Logic Default Settings   
Mouse Button Operations   
Using the Numeric Keypad to Control the View  

## SailWind Logic Flow  

Creating a schematic design of your system requires a number of steps to get from initial concept to completed design. Each step is presented in a logical order so that you can manage the entire process of creating the schematics for your system.  

1. Set up a new design  

◦ Create a new design (See Creating a New Schematic File)   
◦ Select a sheet size (See Setting Schematic Editor Options) Add 2D line objects (See Adding Drafting Items From a Library)   
◦ Set up options • Global (See Options Dialog Box, General Category) Design (See Options Dialog Box, Design Category)  

2. Set up rules and constraints ◦ Decide which design rules you need (See Setting Up Rules) ◦ Set up design rules (See Rules Setup)  

3. Place parts  

◦ Locate parts in the library (See Managing Libraries and Library Data)   
◦ Place parts (See Schematic Parts) Set attributes (See Attributes Overview)  

4. Wire the schematic  

◦ Connect the components (See Connections) ◦ Edit the connections (See Changing a Connection) ◦ Name the connections (See Naming a Connection) ◦ Assign net constraints (design rules) (See Setting Up Net Rules)  

5. Prepare the Design for Layout 。 Output a netlist to SailWind Layout (See Creation of a New PCB Layout from a SailWind Logic Design) Generate reports (See Reports)  

6. Perform Design Annotations Forward annotate design changes to SailWind Layout (See Forward Annotation From SailWind Logic to SailWind Layout) Backward annotate design changes from SailWind Layout (See Backward Annotation Fro SailWind Layout to SailWind Logic)  

## Startup Options  

You can use startup options, known as command line switches, to control the initial SailWind Logic configuration. Use command line switches to enable different options, to open a file, start macros, and record a SailWind Logic session. You can type multiple command line options.  

For instructions to add options to a program shortcut, see “Adding Startup Options to a Shortcut”.  

Table 1. SailWind Logic Command Line Options   

| Option                                                       | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| filename                                                     | Opens the specified design file when you start SailWind Logic. Type the folder path and filename. Use quotation marks for directories or filenames with spaces, |
| for example: "C:\SailWind Projects\Sampleslpreviewpart.sch" Restriction: |                                                              |
| Do not use a forward slash (/ ) before the filename in the command line. |                                                              |

Table 1. SailWind Logic Command Line Options (continued)

| Option         | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| /BMW[initials] | Opens the Media Wizard. Use the Media Wizard to start recording a session log or to convert the previous session log to media that can be replayed by Basic Log Test. To create session media files for the current SailWind Logic session, use the BMW modeless command. To use the BMW command line switch, type /BMW or /BMWxx, where xx is your initials, in the command line. Capitalization. [] represents optional text. This option is associated with another modeless command, BLT. BLT is the Log Test; it finds and runs the session media created by BMW to play back a recorded SailWind Logic session. For information, see Modeless Commands and Keyboard |
| /              | Shortcuts on page 569.                                       |
| /mmacro name   | Opens the last file you had open when you start SailWind Logic. Runs the specified macro in the default macro file. For example, to run the macro |
| /Mmacro file   | MyMacro, type /mMyMacro. Specifies the file to use as the default macro file. For example, to run the macro MyMacro contained in the file user1.mcr, type /Muser1.mcr /mMyMacro. Note the |
| /nc            | required capitalization. Starts SailWind Logic without displaying the splash screen that includes copyright information. |
| /sXXX          | Starts a Basic script when you start SailWind Logic. Use quotation marks for filenames with spaces, for example:/s"C:\\SailWind\Samples\Scripts\Logic\Unsuppo rted\AttributestoExcel.bas" |

  

## Adding Startup Options to a Shortcut  

If you repeatedly start your design sessions with the intention of launching a specific design file or specifying a particular design environment setting, then you can add startup options to the properties of a shortcut.  

![](/images/99632d4f4f470d6fcecedeec68a8df6378fdb2180432bd1781d444962c9c99f5.jpg)  

!Tip  

If you create your own shortcuts, copy the Start menu shortcuts instead of generating them from the executables in the install directory. Start menu shortcuts contain a "wrapper" that enables the proper environment variables to be defined as the program launches.  

**Procedure** 

1. In the shortcut properties, click in the box with the pathname.   
2. Press End, press Spacebar, and then type the command line switch you want to use, and enclose with double quotes " " each string that contains a space.  

When specifying a file to start, do not use a / before the filename. You can specify multiple command line switches. For example, to start the program with preview.sch, the command line might read:  

“\<install_folder>\<version>\Programs\SailWindLogic.exe” “C:\SailWind projects\Samples\preview.sch”  

## SailWind Updates  

The SailWind products automatically check for a new software version when you launch an application. If a new version is detected, a tooltip is displayed in the system tray.  

Downloading the Update Disabling the Check for Updates Checking for Updates Manually  

### Downloading the Update  

When a new version of SailWind is detected, you can download the update.  

**Prerequisites**  

An Internet connection is required for the check.  

**Procedure** 

1. Right-click the icon in the system tray.   
2. Click the Open download page popup menu item.   
3. Follow the instructions on the download page.  

### Disabling the Check for Updates  

If you do not want to check for updates automatically, disable the Check for Updates functionality. You can enable the check at any time, or you can manually check for updates.  

**Procedure** 

1. Click the Help > Check for Updates  menu item.   
2. In the Check for Updates Dialog Box, select the “Disable ‘Check for Updates’ functionality” check box.  

### Checking for Updates Manually  

Do not check for updates manually unless you have disabled the automatic check.  

**Procedure** 

1. Click the Help > Check for Updates menu item.   
2. In the Check for Updates Dialog Box, click Check for Updates.  

## Migrating User Settings  

You can use the SailWind User Settings Migration tool to extract your settings from one installation of SailWind Logic, Layout, and Router and import them into another installation or version.  

For information on how to do this, see User Settings Migration in the SailWind User Settings Migration Guide.  

## Customizing SailWind Logic Default Settings  

Several settings define the default ASCII parameters of operation of SailWind Logic. You can customize the user interface by modifying these system settings and saving the files.  

The file default.txt is a SailWind Logic ASCII file that contains default option settings. It is read into memory when you start SailWind Logic or click the File > New menu item to begin a new design.  

**Procedure** 

1. Click the Tools > Options menu item.   
2. Change the settings as desired using the General and Design categories to change the sheet size and design grid, and so forth.   
3. Click OK to save the changes.   
4. Click the File > Export menu item, and then set the folder to C:\<install_folder>\SailWind<version> \Settings.   
5. Select default.txt from the list of files. Type the name in the File name area if it does not exist.   
6. Click Save. This displays the ASCII Output dialog box.   
7. In the ASCII Output dialog box, click Select All.   
8. Leave the output format at the current setting and click OK.  

## Mouse Button Operations  

SailWind Logic follows Microsoft® Windows® conventions for two-button mouse operations. SailWind Logic also supports the use of a three-button mouse. The middle button provides quick access to the pan and zoom commands.  

Use the middle mouse button to pan (to move the view from side to side or up and down) without changing the size. Click the middle mouse button where you want to center the work area. The screen repaints, placing the point you chose at the center.  

To define a specific area that you want to enlarge, hold the middle mouse button down, and move the mouse diagonally and up across the area you want to zoom. A dynamic rectangle expands with the cursor movement. When you release the middle mouse button, the view zooms to the rectangle.  

To zoom out, press the middle mouse button and drag diagonally and down. When you zoom out, a solid rectangle appears at the cursor. This represents the current view size. The thin line that expands from the  

solid box represents the new view size in proportion to the old. The zoom-out ratio also displays with the cursor.  

## Using the Numeric Keypad to Control the View  

You can control the view using the extended keypad or the numeric keypad, located on the far right of most keyboards. The NumLock light can be on or off except where specified.  

Table 2. Numeric Keypad Functions   

| Click  | To                                                           |
| ------ | ------------------------------------------------------------ |
| Home   | Fits board to the view.                                      |
| End    | Redraws current view.                                        |
| Arrows | With Num Lock On, pans the viewing window. Moves one-half the screen width in the direction of the arrow. With Num Lock Off, moves cursor on grid unit. |
| 5      | With Num Lock On, draws zoom rectangle.                      |
| Pg Up  | Zooms In centered at cursor location.                        |
| Pg Dn  | Zooms Out centered at cursor location.                       |
| Ins    | Centers the view at current cursor location, without zooming. |

