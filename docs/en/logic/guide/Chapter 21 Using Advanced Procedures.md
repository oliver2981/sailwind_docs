# Chapter 21 Using Advanced Procedures  

SailWind Logic supports interaction with advanced procedures such as SPICE Simulation and Basic scripting. You can set up advanced SPICE design simulations to analyze your design behaviors, and use the Basic scripting to automate many repetitive design tasks. You can also view and manage your license file information.  

Spice Simulation   
Basic Scripting   
Managing Licensed Options  

# Spice Simulation  

The Spice simulation in SailWind Logic enables you to set up and analyze your design using advanced procedures including setting up Spice Netlists, AC Analysis, DC Source Sweep Analysis, Transient Analysis, and applying attributes to your analog designs..  

Analog Schematics for Simulation Creating a SPICE Netlist Setting Up AC Analysis Setting Up DC Source Sweep Analysis Setting Up the SPICE Netlister Setting Up Transient Analysis Apply Attributes to Your Analog Design  

# Analog Schematics for Simulation  

You can create analog schematics and generate netlists for SPICE Simulators. Add analog attributes with simulation values to parts and nets for SPICE simulation.  

Several analog parts are supplied in the misc library as examples. In addition, several examples of component simulation models are supplied in the Analog Models subfolder of the library.  

![](/images/89ed1bb695ee4c4af5828a14148c3975367a3c0b06a37ab6c886292356215711.jpg)  

!Note:  

Each SPICE model must have a separate .mod file. A model file can have subcircuit sections, but multiple models cannot be stored in one file since there is no mechanism for the software to extract the different models from within the file.  

Add SPICE Attributes to Library Parts Versus Schematic Parts Adding SPICE Attributes to Schematic Parts or Nets  

# Add SPICE Attributes to Library Parts Versus Schematic Parts  

You can add SPICE attributes to library parts instead of parts in the schematic. When you add attributes to schematic parts, you must add them each time you use the part. When you add attributes to parts in the library; however, you don't have to add them again.  

See also Attributes Overview.  

# Adding SPICE Attributes to Schematic Parts or Nets  

When you add attributes to schematic parts, you must add them each time you use the part. Consider adding the attributes to your library parts.  

**Procedure** 

1. Select a part or a net, right-click and click Attributes.  

2. Add SPICE attributes to the part. You can also click Browse Lib. Attr. to browse the Attribute Dictionary for SPICE attributes.  

See also SPICE Netlist Attribute Glossary in the SailWind Logic Command Reference.  

![](/images/c78facb4d3f5bd06e3746dbccbcd8bdcc6463314bfbb1719f98e5b62d819ab12.jpg)  

!Note:  

Use the MODEL attribute to refer to component simulation models. Models take the device name with a .mod extension. Models are searched in the SailWind installation folder, SailWind libraries folder, SailWind project folder, and finally the library list using the search order. Each SPICE model must have a separate .mod file. A model file can have subcircuit sections, but multiple models cannot be stored in one file since there is no mechanism for the software to extract the different models from within the file.  

**Related Topics**  

Creating a SPICE Netlist  

# Creating a SPICE Netlist  

After you add parts (with SPICE attributes) to your schematic, or add SPICE attributes to existing parts, you can create a SPICE netlist in preparation for simulation.  

**Procedure** 

1. Click the Tools $>$ SPICE Netlist menu item.   
2. In the Output File Name box, use the default or type the path and name of the SPICE netlist file. You can also use the Browse button to search for a path.  

3. In the Select Sheets area, select the sheets to include in the SPICE netlist. You can also use:  

Select All — Selects all sheets in the Select Sheets box.   
• Unselect All — Clears all the selected sheets in the Select Sheets box.  

![](/images/ac1cb0ad1b040d8a1e827221984ace0fedf3a41f8a8d4b7ed24163f92cfb7d2c.jpg)  

Tip Only complete schematic sheets can be simulated.  

4. If the design is hierarchical, select the Include Subsheets check box to include any underlying hierarchy.  

5. In the Output Formats box, select the target SPICE software.  

6. Click Simulation Setup to change or enable the default simulation values.  

0 Tip Your simulation values are saved for future SPICE netlisting.  

See also Setting Up the SPICE Netlister.  

7. Click OK to create the SPICE netlist.  

An output window displays the resulting netlist. All warnings, errors, and comments during netlisting are embedded in the final netlist. You can edit the netlist before starting simulation.  

**Related Topics**  

Analog Schematics for Simulation  

# Setting Up AC Analysis  

As part of setting up your SPICE netlister, you can set options specifically for an AC analysis.  

**Procedure** 

1. Click the Tools $>$ SPICE Netlist menu item.  

2. In the SPICEnet dialog box, click Simulation Setup.  

3. In the Simulation Setup dialog box, click AC Analysis.  

4. In the Interval area, type the number of points and then select your choice of variation: Decade, Octave, or Linear.  

5. In the Frequency area, type a Starting and Ending frequency.  

![](/images/65e0589afa9080912f8732d0ad0f5ab0930543394a82610b052312a0fb29de90.jpg)  

Tip Your simulation setup values are saved for future SPICE netlisting.  

For more information on AC Analysis, see the Help in your SPICE simulator.  

**Related Topics**  

Setting Up the SPICE Netlister  

# Setting Up DC Source Sweep Analysis  

As part of setting up your SPICE netlister, you can set options specifically for a DC Sweep analysis.  

**Procedure** 

1. Click the Tools $>$ SPICE Netlist menu item.   
2. In the SPICEnet dialog box, click Simulation Setup.   
3. On the Simulation Setup dialog box, click DC Sweep.   
4. In the Source box, type the name of the voltage or current source.   
5. In the Start box, type the starting voltage for the sweep.   
6. In the Stop box, type the stopping voltage for the sweep.   
7. In the Step box, type the incrementing values for the sweep.  

!Tip  

Your simulation setup values are saved for future SPICE netlisting.  

For more information on DC Source Sweep Analysis, see the Help in your SPICE simulator.  

**Related Topics**  

Setting Up the SPICE Netlister  

# Setting Up the SPICE Netlister  

After you add parts (with SPICE attributes) to your schematic, or add SPICE attributes to existing parts, you can create a SPICE netlist in preparation for simulation.  

**Procedure** 

1. Click the Tools $>$ SPICE Netlist menu item.  

2. In the SPICEnet dialog box, click Simulation Setup.  

3. Select the check boxes beside any analyses you want to enable.  

4. Click an analysis button to change default simulation values.  

• AC Analysis — Directs the SPICE simulator to perform frequency analyses   
• DC Source Sweep Analysis — Directs the SPICE simulator to perform operating point analyses at specified values   
• Transient Analysis — Directs the SPICE simulator to perform time analyses   
• Operating Point — Directs the SPICE simulator to determine the DC operating point of the circuit  

![](/images/2a6b77ad938afd6b9173318a337dca5d67d48bfc9524e5a663657185cd1fd8a6.jpg)  

Tip Your simulation setup values are saved for future SPICE netlisting.  

For more information on Simulation Setup, see the Help in your SPICE simulator.  

**Related Topics**  

Creating a SPICE Netlist Setting Up AC Analysis Setting Up DC Source Sweep Analysis Setting Up Transient Analysis  

# Setting Up Transient Analysis  

As part of setting up your SPICE netlister, you can set options specifically for a Transient analysis.  

**Procedure** 

1. Click the Tools $>$ SPICE Netlist menu item.   
2. On the Simulation Setup dialog box, click Transient. The Transient Analysis dialog box displays.   
3. In the Data Step Time box, type the increment for the analysis.  

4. In the Total Analysis Time box, type the time to end the analysis.  

5. In the Time to Start Recording Data box, type the time to start recording data from the analysis.  

This is helpful if your simulation files become too large and you are not interested in data from the beginning of the analysis.  

6. In the Maximum Time Step box, type a maximum time step value.  

7. If you do not want SPICE to solve for the quiescent operating point before beginning the transient analysis, select the Use Initial Conditions check box.  

If this option is enabled, SPICE uses the values specified using $1C=\cdots$ on the various elements as the initial transient condition and proceeds with the analysis.  

![](/images/5baa761ad8e46d62d11ec27bd978c591e20d019cad04e1460b837c522a93643d.jpg)  

Tip Your simulation setup values are saved for future SPICE netlisting.  

For more information on Transient Analysis, see the Help in your SPICE simulator.  

**Related Topics**  

Setting Up the SPICE Netlister  

# Apply Attributes to Your Analog Design  

There is a list of attributes that you can apply to your analog design. Review the list and select those attributes that are relevant to your design intent.  

Please see the “SPICE Netlist Attribute Glossary” in the SailWind Logic Command Reference.  

# Basic Scripting  

Basic is a simple scripting language. Like many Windows applications, such as Microsoft Word and Excel, SailWind applications include Basic capabilities to enable users to customize their applications using a standard scripting language.  

Managing Scripts   
Creation of Scripts   
Run Scripts   
Debug Scripts   
Accessing Help on the Basic Language   
Using the Basic Scripts Dialog Box   
Manage the Sax Basic Engine   
Basic Sample Scripts  

# Managing Scripts  

SailWind Logic offers a flexible number of options for managing scripts. You can open existing scripts, manage open scripts, edit scripts, edit user dialog boxes to enable user interaction, find automation statements, and watch variables. This gives you a high level of control over setting up and managing your scripts.  

Opening an Existing Script   
Manage Open Scripts   
Editing a Script   
Editing a User Dialog Box   
Finding an Automation Statement   
Watching a Variable  

# Opening an Existing Script  

Scripts are created in and stored in script files that have a .bas extension. The default location for .bas files is C:\SailWind Projects.  

**Procedure** 

1. Click the Tools $>$ Basic Scripts $>$ Basic Script Editor menu item, then click the Open button.  

2. Select the script and then click Open. You can have up to nine scripts open at the same time.  

Note:   
A selection of sample scripts is available in the C:\SailWind Projects\Samples\Scripts\Logic folder.  

# Manage Open Scripts  

The commands on the Sheet submenu provide script management methods. Since you can have up to nine scripts open at the same time, you can open #uses, close sheets, close multiple sheets, and choose scripts to view and edit.  

# Opening #uses Modules  

#Uses modules are Basic scripts that are called from within other scripts. To open these secondary scripts:  

• In the Basic Script Editor, right-click and select Sheet $>$ Open Uses.  

The #uses modules called in the script appear as script sheets in the Basic Script Editor. They are assigned a numbered tab and you can edit or run them.  

Closing an Open Script  

In the Basic Script Editor, right-click and select Sheet $>$ Close.  

Alternatively, you can double-click the script's numbered tab in the gutter.  

Closing all Open Scripts  

• In the Basic Script Editor, right-click and select Sheet $>$ Close All.  

Viewing a Particular Script  

If you have multiple scripts open, you can view a particular open script. You can have up to nine scripts open at the same time.  

To view a particular script:  

• Right-click and select Sheet. Then click the script you want to view from the list of open scripts on the submenu. Alternatively, you can click the script's numbered tab in the gutter.  

# Editing a Script  

You can copy or cut selected text from the Basic Script Editor to the Clipboard. You can also paste a selection from the Clipboard into the text window. You can also paste text from the Clipboard into other applications.  

**Procedure** 

1. In the Basic Script Editor, select the text you want to copy or cut.  

2. Right-click and click Edit $>$ Copy or Cut.  

3. Right-click and click Edit $>$ Paste to paste the script text.  

Your selection is pasted in the Output window at the insertion point.  

As an alternative, you can click the Copy, Cut, and Paste buttons on the Basic Script Editor toolbar.  

# Editing a User Dialog Box  

A UserDialog is defined by a Begin Dialog...End Dialog block.  

**Procedure** 

1. In the Basic Script Editor, put your cursor in a UserDialog block of the script. 2. Click the Edit UserDialog button. See also Sax Basic Editor On Line Help (C:\<install_folder>\<version>\Programs\sbe5_000.hlp)  

# Finding an Automation Statement  

If you are working with a long script, you can search for particular statements.  

**Procedure** 

1. In the Basic Script Editor, click the Object list and select an object type. The Object list shows all the objects for the current module. The (General) object groups all of the procedures that are not part of any specific object. 2. Click the Procedure list and select a bold procedure. The Procedure list shows all the procedures for the current object. Selecting a procedure that is bold locates the procedure in the script.  

The statement appears in the Basic Script Editor.  

# Watching a Variable  

Quick Watch shows the value of the expression under the cursor in the immediate window.  

**Procedure** 

Right-click and click Quick Watch.   
As an alternative, in the Basic Script Editor, click the Quick Watch button.   
See also Sax Basic Editor Online Help.  

# Creation of Scripts  

You can create scripts to simplify redundant activities.  

Creating a Script   
Inserting an Automation Statement Using the Object and Procedure Lists   
Inserting an Automation Statement Using the ActiveX Automation Members Dialog   
Setting the Next Statement   
Showing the Next Statement  

# Creating a Script  

You can create a script using the Basic Script Editor.  

**Procedure** 

1. Click the Tools $>$ Basic Scripts $>$ Basic Script Editor menu item. In SailWind Layout and SailWind Logic, the SAX Basic Engine dialog box appears.   
2. Click the New button.  

# Inserting an Automation Statement Using the Object and Procedure Lists  

Use the Object and Procedure lists to select and insert a statement. These lists contain the most commonly used statements.  

**Procedure** 

1. Click the Object list and click an object type. The Object list shows all the objects for the current module. The (General) object groups all of the procedures that are not part of any specific object.  

2. Click the Procedure list and click a non-bold procedure to insert. The Procedure list shows all the procedures for the current object. Selecting a procedure that is not bold inserts the proper procedure definition for that procedure.  

The statement appears at the bottom of the script.  

# Inserting an Automation Statement Using the ActiveX Automation Members Dialog  

Use the ActiveX Automation Members dialog box to insert a statement from the extensive list provided.  

**Procedure** 

1. In the Basic Script Editor, right-click and click the Debug $>$ Browse menu item.   
2. Use the ActiveX Automation Members dialog box to select and insert a statement.  

This dialog box contains an extensive list of statements.  

Tip If the pointer is on any line in the script other than the bottom line, the line is overwritten.  

# Setting the Next Statement  

You can force a particular line in a script to run next. You can only select statements in the current subroutine or function.  

**Procedure** 

1. In the Basic Script Editor, put your cursor on the line you want to run next.   
2. Right-click and click the Debug $>$ Set Next Statement menu item.  

An instruction pointer appears next to the selected line. This line, and only this line, will run next. If you go to other parts of the script, you can return to this line by clicking Show Next Statement.  

# Showing the Next Statement  

In the Basic Script Editor, you can navigate the right mouse button menu to initiate the Show Next Statement command.  

**Procedure** 

n the Basic Script Editor, right-click and click Debug $>$ Show Next Statement menu item.  

An instruction pointer indicates the next statement to run.  

i Tip Pausing a running script or setting a statement to run next sets the next statement. You can locate the set statement from anywhere in the script.  

# Run Scripts  

You can run an existing script using Run. Run also resumes the playback of a paused script. When you run a script, you cannot use the mouse in the workspace.  

Running a Script Pausing a Running Script Stopping a Running Script  

# Running a Script  

You can run a script using the Macro command in the Basic Script Editor.  

**Procedure** 

1. In the Basic Script Editor, open a script file.   
2. Right-click and click the Macro $>$ Run menu item. As an alternative, on the Basic Script Editor toolbar, click the Start/Resume button.  

# Pausing a Running Script  

When running a long script, you may need to pause it to perform some other design activity.  

**Procedure** 

1. In the Basic Script Editor, right-click and click the Macro $>$ Pause menu item.  

2. As an alternative, on the Basic Script Editor toolbar, click the Pause button.  

!Tip  

If you paused the script, you can also use Run, Step Over, or Step to Cursor to resume running the script. Right-click and select Run to resume running the script.  

# Stopping a Running Script  

You can stop a running script at any time. However, you cannot resume running a script once you have stopped it. When you click Run, the script starts from the beginning.  

**Procedure** 

In the Basic Script Editor, right-click and click the Macro $>$ End menu item.   
As an alternative, on the Basic Script Editor toolbar, click the Stop button.  

# Debug Scripts  

When running a script, you can run it step-by-step or to a certain location in the script. To perform these debugging tasks, insert breakpoints in the script at the points at which you want the script to stop.  

Setting or Removing the Breakpoints Debug the Scripts Removing All Breakpoints in the Script Correction of Run-Time Errors  

# Setting or Removing the Breakpoints  

The ability to set or remove breakpoints is useful when you debug a script. If the Basic engine encounters a breakpoint when running a script, it pauses the script.  

**Procedure** 

1. Place the cursor on the line to which to add a breakpoint.  

2. On the Basic Script Editor toolbar, click the Toggle Breakpoint button.  

As an alternative, in the Basic Editor, right-click and click the Debug $>$ Toggle Break menu item.  

This action inserts a breakpoint at the current cursor location. A breakpoint marker appears in the gutter area.  

Note:   
When the Basic engine encounters a breakpoint while running a script, it pauses the script. The next line in the script is marked with the instruction pointer.  

# Debug the Scripts  

Once breakpoints are inserted, you can debug scripts using the Debug commands.  

To run a single line of the script:  

On the Basic Script Editor toolbar, click the Step over button.  

To perform a subroutine call on the current line:  

• On the Basic Script Editor toolbar, click the Step into button. As an alternative, in the Basic Script Editor, right-click and click the Debug $>$ Step Into menu item.  

To return from the subroutine to the point from which it was called:  

• On the Basic Script Editor toolbar, click the Step out button.  

To run a script to a point:  

• In the Basic Script Editor, right-click and click the Debug $>$ Step to cursor menu item.  

To continue the execution from the current point:  

• On the Basic Script Editor toolbar, click the Run button. As an alternative, in the Basic Script Editor, right-click and click the Macro $>$ Run menu item.  

# Removing All Breakpoints in the Script  

You have the option to remove all breakpoints instead of single breakpoints.  

**Procedure** 

In the Basic Script Editor, right-click and click the Debug $>$ Clear All Breaks menu item.   
This removes all breakpoints in the script.  

# Correction of Run-Time Errors  

If run-time errors occur, the script debugger switches to step-by-step mode and displays a detailed message on the status bar. The instruction pointer is set on the line that produced the error. After fixing the error, you can resume running the script.  

# Accessing Help on the Basic Language  

While writing or running scripts, you can access Help that provides information and a sample script using the Basic language statements.  

**Procedure** 

Select or click in an item in color in the edit area of the Basic Script Editor and then press F1.   
Help appears for the current statement.  

# Using the Basic Scripts Dialog Box  

The Basic Scripts dialog box provides easy access to your Basic scripts. From there you can edit and debug your scripts.  

**Procedure** 

1. Click the Tools $>$ Basic Scripts menu item, then click Basic Scripts.  

2. Select the script you want to manage.  

3. To run the script, click Run.  

Restriction: You cannot run multiple scripts at the same time.  

0 Tip If the selected script has an error during compilation, it automatically opens in the Basic Script editor for correction.  

4. To edit the script, click Edit. The Sax Basic Engine dialog box appears. See also Manage the Sax Basic Engine.  

5. To add the script to the Basic Scripts menu, click the In Menu check box.  

6. To remove the script from the list, click Unload File.  

7. To add a new script to the list, click Load File.  

!Tip  

When loading scripts, note the following:  

• You can load up to 32,767 scripts. Scripts are not compiled when they are loaded; they are compiled when you run them.   
• The list of scripts you load into this dialog box is saved in the VBScripts.ini file, so they load every time you open the Basic Scripts dialog box.  

**Related Topics**  

Basic Sample Scripts  

# Manage the Sax Basic Engine  

The Sax Basic Engine dialog box provides access to the Sax Basic Engine Script editor. You can design, develop and edit scripts that add to, replace, enhance, or customize existing SailWind Logic features.  

Scripts written in the Basic Script editor comply with all Microsoft requirements in terms of Visual Basic syntax; therefore, you can play these scripts in any other Visual Basic interpreter, such as Word or Excel. However, you cannot run all Basic scripts created outside of the Sax Basic Engine within the Sax Basic Engine because the Sax Basic Engine is a subset of Visual Basic. For example, you cannot run the Automation samples within the Sax Basic Engine.  

• Click the Tools $>$ Basic Scripts $>$ Basic Script Editor menu item, then click New button.  

See also Sax Basic Editor On-line Help.  

There are four types of scripts: scripts, code modules, object modules, and class modules.  

You can create a script that calls another script. For example, ScriptA can call ScriptB.  

You can also create a script that runs a series of scripts, or a "master" script. For example:  

'\$Include: "scriptA.bas" '\$Include: "scriptB.bas" '\$Include: "scriptC.bas" Sub Main  

# Using Advanced Procedures Manage the Sax Basic Engine  

Call scriptA Call scriptB Call scriptC End Sub  

# Editor Colors  

The Basic Script Editor displays source code using different colors. The color is context-sensitive: when you place the cursor on the text and press F1, the correct help file opens to the correct help topic. For example, if the cursor is on a SailWind Logic Automation Object (purple) when you press F1, the Automation Server On-line Help appears.  

Table 42. Basic Script Editor Color Representations   


| Color  | Represents                                   |
|--------|----------------------------------------------|
| Blue   | Basic Keywords                               |
| Black  | User Variables                               |
| Cyan   | Basic Functions                              |
| Purple | SailWind Logic Automation Objects or Members |
| Red    | Errors                                       |
| Green  | Comments                                     |

# Basic Sample Scripts  

To address common design scenarios, and to provide a starting point for the development of custom user scripts, SailWind Logic includes a collection of sample Basic scripts. All sample scripts are commented.  

Basic Sample Scripts 00 Through 11 Basic Sample Scripts — RGL Reports Basic Sample Scripts — Advanced  

# Basic Sample Scripts 00 Through 11  

Samples 00 through 09 provide an overview of Basic if you don't have experience with Basic scripts. Samples 10 and 11 provide small SailWind Logic features that add, enhance, or customize a SailWind Logic feature.  

These files are located in C:\<install_folder>\<version>\Samples\Scripts\Logic\tutorial.  

Table 43. Basic Sample Script Listing   


|  Script Filename                       | Description                                                                                |
|----------------------------------------|--------------------------------------------------------------------------------------------|
| 00 What is a Script.BAS                | Empty script demonstrating what a Basic script is and how to define it.                    |
| 01 Using a Message Box.BAS             | Demonstrates how to display an OK dialog box.                                              |
| 02 Using a Variable.BAS                | Demonstrates a Basic variable: how to assign a value and how to get its value.             |
| 03 Using a Basic Function.BAS          | Demonstrates how to use a standard Basic function and display its result in a message box. |
| 04 Using a SailWind Logic Function.BAS | Demonstrates Basic interaction with a SailWind Logic Automation function.                  |
| 05 Using If and Then Statements.BAS    | Demonstrates the If, Then statements.                                                      |
| 06 Using a Custom Dialog1.BAS          | Demonstrates a simple dialog box using the Basic dialog editor.                            |
| 07 Using a Custom Dialog2.BAS          | Demonstrates a standard dialog box using the Basic dialog box editor.                      |
| 08 Using a Custom Dialog3.BAS          | Demonstrates a complex dialog box using the Basic dialog box editor.                       |

Table 43. Basic Sample Script Listing (continued)   


| Script Filename               | Description                                                                                                                                                  |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 09 Using it All Together.BAS  | Provides a "real life" example. Lists all design files in the default files directory. Selecting a file from the list will open that file in SailWind Logic. |
| 10 List Of Comps and Nets.BAS | Lists all components and nets.                                                                                                                               |
| 11 Select by Pin Count.BAS    | Enables you to enter a number of pins. All parts with that number of pins are selected.                                                                      |

# Basic Sample Scripts — RGL Reports  

Basic scripts are equivalent to existing RGL reports.  

These files are located in C:\<install_folder>\<version>\Samples\Scripts\Logic\rgl samples.  

Table 44. Basic Sample Scripts/RGL Reports Listing   


| Script Filename     | Description                                                                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| RGL.BAS             | Contains a library of functions, which is used by the_ other scripts in this group; the scripts in this group must contain RGL.BAS to function. |
| Net Statistics.BAS  | Lists all nets in the schematic and identifies any questionable nets.                                                                           |
| Part Statistics.BAS | Lists all parts in the schematic.                                                                                                               |
| Unused Gates.BAS    | Lists all unused gates in the schematic.                                                                                                        |
| Unused Pins.BAS     | Lists all unused pins in the schematic.                                                                                                         |
| Unused.BAS          | Lists all unused pins and gates in the schematic.                                                                                               |

# Basic Sample Scripts — Advanced  

Advanced Basic script files are located in C:\<install_folder>\<version $>$ \Samples\Scripts\Logic.  

Table 45. Basic Sample Scripts/Advanced Listing   


| Script Filename       | Description                                                                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Add Part.BAS          | Adds a new gate to the schematic.                                                                                                            |
| Alive Net List.BAS    | Creates a netlist in Excel, which enables you to cross-probe between SailWind Logic objects and the Excel cells containing the object names. |
| Bill of Materials.BAS | Produces a bill of materials in a user-customizable format.                                                                                  |

Table 45. Basic Sample Scripts/Advanced Listing (continued)   


| Script Filename                            | Description                                                                                                                                                 |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Modeless Attributes.BAS                    | Generates a modeless dialog box, which you use to manage part attributes.                                                                                   |
| Modeless QM Part.BAS                       | Generates a modeless dialog box, which you use to manage part and gate properties.                                                                          |
| Modeless Visibility.BAS                    | Generates a modeless dialog box, which you use to manage gate and attribute visibility.                                                                     |
| SailWind Layout Net List Without Rules.BAS | Generates a netlist report in ASCll format.                                                                                                                 |
| SailWind Logic Script Wizard.BAS           | Generates a Wizard dialog box, which you use to create a Basic report.                                                                                      |
| Sheet Hierarchy to Excel.BAS               | Creates a sheet hierarchy report in Excel, which enables you to cross-probe between SaiiWind Logic objects and the Excel cells containing the object names. |

# Managing Licensed Options  

You can view and manage your licensed SailWind Logic options. You can view the available options for node-locked or floating licenses.  

Viewing a License File or License Status License File Definition  

# Viewing a License File or License Status  

If you are using node-locked licensing, you can view the contents of a license file. If you are using floating licenses, you cannot view the actual license file, but you can view the status of the features associated with a server license.  

**Procedure** 

1. Click the Help $>$ Installed Options menu item, then click the License File tab.  

2. Select one of these methods to view the license file:  

• For Node-locked Licenses — To view a license file: i. Select the license file that you want to view from your list of license files. ii. Click View. The bottom portion of the screen displays the contents of the selected file.   
For Floating Licenses — To view the status of the features associated with a server license: i. Select the server license file for which you want to display feature status. ii. Click Status. The feature usage information appears in the bottom portion of the screen.  

**Related Topics**  

Installed Options Dialog Box License File Definition  

# License File Definition  

This section describes the license file and the possible options enabled in it.  

All installed options appear in the Installed Options Dialog Box on page 394.  

# Options  

FEATURE SailWindLogic paizieda \  

Controls entry into the program and provides access to the basic SailWind Logic schematic functions.   
This feature is not listed on the Installed Options dialog.  

