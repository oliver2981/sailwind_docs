# Chapter 18 Working With SailWind Layout and SailWind Router  

Using SailWind Logic, you can seamlessly exchange design data with SailWind Layoutand SailWind Router. This is a bi-directional process that enables you to forward annotate and back annotate your data to keep your design changes synchronized. You can also generate a differences report so that you can compare one design with another and highlight any differences.  

Creation of a New PCB Layout from a SailWind Logic Design   
Cross-Probe Between Sailwind Products   
Forward Annotation From SailWind Logic to SailWind Layout   
Backward Annotation From SailWind Layout to SailWind Logic   
Backward Annotation Results   
Contents of the Differences Report   
ECO File Format  

# Creation of a New PCB Layout from a SailWind Logic Design  

There are two ways to create a new PCB design from a SailWind Logic design: you can use the SailWind Layout Link, or you can manually exchange a netlist between SailWind Logic and SailWind Layout.  

Method 1 — Use if you have both SailWind Logic and SailWind Layout on your computer, use the “Automatic Netlist Process Using the SailWind Layout Link”. This automated method is the simplest.  

• Method 2 — Use if you don’t have both SailWind Logic and SailWind Layout on your computer, use the “Manual Netlist Process Between SailWind Logic and SailWind Layout”. This manual method requires you to manually export the netlist from SailWind Logic and then import it into SailWind Layout.  

Automatic Netlist Process Using the SailWind Layout Link Manual Netlist Process Between SailWind Logic and SailWind Layout Interpreting and Resolving the Netlist Process Error Report  

# Automatic Netlist Process Using the SailWind Layout Link  

If you have both SailWind Logic and SailWind Layout on your computer, you can automatically process a SailWind Logic netlist using the SailWind Layout Link. This automated method is the simplest.  

# Restrictions and Limitations  

• Forward annotation of changes to an existing design requires a different process. See Forward Annotation From SailWind Logic to SailWind Layout.   
• Transferring non-ECO-registered parts and non-electrical parts is constrained by settings in the Options. See the Design Options on page 591 for details.  

# Prerequisites  

You must have both SailWind Logic and SailWind Layout on the same computer.  

**Procedure** 

1. Click the Tools $>$ SailWind Layout menu item.  

0 Tip If SailWind Layout is not already open, the Connect to SailWind Layout Dialog Box appears. Click New to start a new SailWind Layout session.  

2. In the SailWind Layout Link dialog box, click the Preferences Tab on page 620, then set the appropriate options.  

# 3. On the Design Tab: on page 614  

a. If needed, select the Include Design Rules in Net list or the AI layout reference data check box.  

![](/images/c291a64dbf317622e6db70a229ca00781ce551cdd1c638c96ac865c91e943f80.jpg)  

Tip   
The AI layout reference data item must be selected in order for the AI Intelligent Layout feature to work in SailWind Layout.  

b. Click the Send Net List button.  

**Results**  

The import process sources all the part types and decals from the library and stacks the decals at the origin. You can then use the SailWind Layout Tools $>$ Disperse Components menu item to spread out the components.  

If an errors report file (ascii.err) is generated and errors are found in the netlist, see Interpreting and Resolving the Netlist Process Error Report for more information.  

# Manual Netlist Process Between SailWind Logic and SailWind Layout  

If you don’t have both SailWind Logic and SailWind Layout on your computer, you can manually process the netlist. This manual method requires you to manually export the netlist from SailWind Logic and then import it into SailWind Layout.  

# Restrictions and Limitations  

• Forward annotation of changes to an existing design requires a different process. See Forward Annotation From SailWind Logic to SailWind Layout.  

• Transferring non-ECO-registered parts and non-electrical parts is constrained by settings in the Options. See the Design Options on page 591 for details.  

**Procedure** 

1. Click the Tools $>$ Layout Netlist menu item.  

2. To select a different filename or location for the netlist, in the Netlist to PCB dialog box, click Browse.  

0 Tip The default is the design filename with an .asc extension, and is saved in the \SailWind Projects folder.  

3. In the Select Sheets area, select the sheets you want to include in the netlist.  

4. Select the Include Subsheets check box to include any connections to hierarchical symbols in the netlist.  

# Working With SailWind Layout and SailWind Router Interpreting and Resolving the Netlist Process Error Report  

5. Select the format you want from the Output Formats list.   
6. Set the remaining dialog box options.   
7. Click OK to generate the netlist.   
8. Import the netlist into SailWind Layout. For instructions, see the Creating a New PCB Design by   
   Manually Importing the SailWind Logic Netlist topic in the SailWind Layout Guide.  

**Results**  

The import process sources all the part types and decals from the library and stacks the decals at the origin. You can then use the Tools $>$ Disperse Components menu item to spread out the components  

If an errors report file (ascii.err) is generated and errors are found in the netlist, see Interpreting and Resolving the Netlist Process Error Report for more information.  

# Interpreting and Resolving the Netlist Process Error Report  

If errors are found in the netlist import process, an errors report file (ascii.err) is generated, and the error report file is displayed in a Notepad window. No errors file is generated if no errors are found.  

The following are reported in the errors report file:  

• Library issues   
• Single or zero pin nets   
• Totally floating connections or subnets   
• Unnamed dangling connections (one end floating)   
• Power and Ground symbols used on nets whose name is different from the default name on the symbol Multiple subnet nets where one or more subnets is missing an off-page symbol   
• Single subnet nets with an off-page symbol (lonely subnet warning)   
• User named subnets that have no visible net name label  

**Procedure** 

1. In SailWind Layout, click the File $>$ New menu item.   
2. Click No when you are prompted to save the design.   
3. Add any missing components listed in the ascii.err file to your library, either by adding a library which contains the missing components to your library list, or by creating the missing part types and decals. (See Adding Libraries to the Library List, Creating and Modifying Part Types, and Creating and Editing PCB Decals in the SailWind Layout Guide for instructions.)  

4. Resolve any other errors found in the ascii.err file.  

5. When all the errors have been resolved, repeat the procedure you used to pass the netlist from SailWind Logic to SailWind Layout.  

**Related Topics**  

Creation of a New PCB Layout from a SailWind Logic Design  

# Cross-Probe Between Sailwind Products  

You can cross-probe between SailWind Logic and SailWind Layout, or between SailWind Logic and SailWind Router, if the applications are on the same computer. You can cross-probe between only two applications at a time. In SailWind Logic, you can initiate cross-probing whether or not SailWind Layout or SailWind Router are open.  

Through cross-probing, you can select items in both the schematic and design at the same time. For example, if you select objects in SailWind Layout (or SailWind Router), the object is automatically highlighted and centered in the SailWind Logic work area. For SailWind Logic and SailWind Layout only, cross-probing can also automate netlist comparisons and rules exports.  

Cross-Probing With SailWind Layout Cross-Probing With SailWind Router  

# Cross-Probing With SailWind Layout  

Cross-probe with SailWind Layout to make simultaneous selections in both applications. Selecting an object in one of the programs will automatically select the same object in the other program.  

# Restrictions and Limitations  

• The SailWind Logic selection filter on page 712 should be set to parts, gates, nets, or pins before you select items in SailWind Logic. • Some parts may not exist in both of the databases. Non-ECO-registered parts and non-electrical parts may have been constrained. See Options Dialog Box, Design Category for details.  

**Procedure** 

1. Click the Tools $>$ SailWind Layout menu item.  

If SailWind Layout is not open, the Connect to SailWind Layout Dialog Box appears. Do one of the following:  

• Click New to start a new SailWind Layout session with a new, untitled, design. • Click Open to start a new SailWind Layout session with an existing design. In the File Open dialog box, select a design file and click Open.  

2. In the SailWind Layout Link Dialog Box, on the Selection tab, select the Receive Selections check box to enable selections in SailWind Layout to be received in SailWind Logic.  

You can now proceed with cross-probing with SailWind Layout.  

# Cross-Probing With SailWind Router  

Cross-probe with SailWind Router to actively make simultaneous selections in both applications.   
Selecting an object in one of the programs will automatically select the same object in the other program.  

# Restrictions and Limitations  

• The SailWind Logic selection filter on page 712 should be set to parts, gates, nets, or pins before you select items in SailWind Logic. Some parts may not exist in both of the databases. Non-ECO-registered parts and non-electrica parts may have been constrained. See Options Dialog Box, Design Category for details.  

**Procedure** 

1. Click the Tools $>$ SailWind Router menu item.  

If SailWind Router is not open, the Connect to SailWind Router Dialog Box appears. Do one of the following:  

• Click New to start a new SailWind Router session with a new, untitled, design. • Click Open to start a new SailWind Router session with an existing design. In the File Open dialog box, select a design file and click Open.  

2. On the SailWind Router Link Dialog Box, on the Selection tab, select the Receive Selections check box to enable selections in SailWind Router to be received in SailWind Logic.  

You can now proceed with cross-probing with SailWind Router.  

# Forward Annotation From SailWind Logic to SailWind Layout  

You can export your schematic changes “forward” (known as forward annotation) to an existing PCB layout. You can choose between any of the three methods to forward annotate design changes.  

• Method 1 — If you have both SailWind Logic and SailWind Layout on your computer, use the “Automated Forward Annotation Process”. This automated method is the simplest and fastest.  

• Method 2 — If SailWind Layout is on another computer and you want the layout designer to compare the designs to generate the ECO file, and import it into SailWind Layout use the process in “Generating the ECO File in SailWind Layout”. This method is somewhat quicker than Method 3 since the Compare/ECO tool in SailWind Layout can automatically import the file after the designs are compared.  

• Method 3 — If SailWind Layout is on another computer and you want to compare the designs to generate the ECO file within SailWind Logic and send it to the layout designer to import into SailWind Layout, use the process in “Generating the ECO File in SailWind Logic”.  

Automated Forward Annotation Process Generating the ECO File in SailWind Layout Generating the ECO File in SailWind Logic Forward Annotation Results  

# Automated Forward Annotation Process  

If SailWind Logic and SailWind Layout are on the same computer, you can use the SailWind Layout Link dialog box to compare a newer schematic with an older PCB design and update the original design in Layout from the new design in Logic. You can also create a differences report.  

# Restrictions and Limitations  

• If you are creating a new PCB by sending a netlist for the first time, see Creation of a New PCB Layout from a SailWind Logic Design.  

• To avoid unexpected changes during forward annotation, consider comparing data before you forward-annotate.  

• Transferring non-ECO-registered parts and non-electrical parts is constrained. See the override settings in the Options dialog box, Design Category on page 591 for details.  

• You cannot forward annotate changes to SailWind Router. SailWind Router does not import ECO files.  

• During design comparison, a reuse definition is ignored and actual elements in the physical design reuse are used in the comparison.  

# Prerequisites  

You must have both SailWind Logic and SailWind Layout on the same computer.  

**Procedure** 

1. Click the Tools $>$ SailWind Layout menu item to open the SailWind Layout Link dialog box.  

![](/images/a6415d72a5268655466f8d22e837b56a812696257a33e074f343f543f6ed3100.jpg)  

!Tip  

If SailWind Layout is not already open, the Connect to SailWind Layout Dialog Box appears. Click Open to start a new SailWind Layout session with the original design. In the File Open dialog box, select the original design file and click Open.  

2. (Optional) If you want to check the design differences before updating, click the Design Tab on page 614, and then click the Compare PCB button.  

The two versions are compared and differences written to Logic.rep in the \SailWind Projects folder. To see the report, click the logic.rep link in the Output Window.  

3. On the Preferences Tab on page 620, then set the appropriate options.  

4. On the ECO Names Tab on page 618, set the appropriate options.  

5. On the Design Tab: on page 614  

a. If needed, check the Compare Design Rules and Show Net List errors report check boxes.   
b. Click the ECO To PCB button to send the changes. Tip   
While the SailWind Layout Link dialog box is open, you can cross-probe. For more information see Cross-Probe Between Sailwind Products.  

![](/images/0f9beef22f98b226feaf74249e45cf4515b55c24b28e33b074fdceb767208895.jpg)  

See “Forward Annotation Results”.  

# Generating the ECO File in SailWind Layout  

You can create a netlist (.asc file) and send it to the layout designer who can then generate an ECO file by comparing the designs, and then import the changes into SailWind Layout.  

# Restrictions and Limitations  

• If you’re creating a new pcb by sending a netlist for the first time, see Creation of a New PCB Layout from a SailWind Logic Design.  

• To avoid unexpected changes during forward annotation, consider comparing data before you forward-annotate.  

• Transferring non-ECO-registered parts and non-electrical parts is constrained. See the override settings in the Options dialog box, Design Category on page 591 for details.  

• You cannot forward annotate changes to SailWind Router. SailWind Router does not import ECO files.   
• During design comparison, a reuse definition is ignored and actual elements in the physical design reuse are used in the comparison.  

**Procedure** 

1. Click the Tools $>$ Layout Netlist menu item.  

2. To select a different filename or location for the netlist, in the Netlist to PCB dialog box, click Browse.  

!Tip  

The default is the design filename with an .asc extension, and is saved in the \SailWind Projects folder.  

3. In the Select Sheets area, select the sheets you want to include in the netlist.  

4. Select the Include Subsheets check box to include any connections to hierarchical symbols in the netlist.  

5. Select the format you want from the Output Formats list.  

6. Set the remaining dialog box options.  

7. Click OK to generate the netlist.  

8. Send the netlist to the layout designer.  

For the continuation of this process, see Forward Annotating Using an ECO File Generated by SailWind Layout in the SailWind Layout Guide.  

See “Forward Annotation Results”.  

# Generating the ECO File in SailWind Logic  

Use the Compare/ECO dialog box to compare the netlists for a newer schematic and an older PCB design and create an ECO (engineering change order) file for import into the PCB design. You can also create a differences report file.  

# Restrictions and Limitations  

• If you’re creating a new pcb by sending a netlist for the first time, see Creation of a New PCB Layout from a SailWind Logic Design.   
• To avoid unexpected changes during forward annotation, consider comparing data before you forward-annotate.   
• Transferring non-ECO-registered parts and non-electrical parts is constrained. See the override settings in the Options dialog box, Design Category on page 591 for details.   
You cannot forward annotate changes to SailWind Router. SailWind Router does not import ECO files.   
• During design comparison, a reuse definition is ignored and actual elements in the physical design reuse are used in the comparison.  

# Prerequisites  

You must have the .asc file exported from SailWind Layout, and have the schematic open in SailWind Logic.  

**Procedure** 

1. Click the Tools $>$ Compare/ECO menu item.   
2. In the Compare/ECO dialog box, click the Documents Tab on page 505.   
3. In the Original Design to Compare and Update area, browse for the previous netlist .asc file sent to SailWind Layout. (Optional) You can acquire a new Layout .asc file from SailWind Layout to generate the .eco file of design differences.  

!Tip  

As long as the PCB design hasn’t undergone engineering changes, the last .asc file from SailWind Logic can be compared to the current design in SailWind Logic to generate the .eco file of the engineering changes in the design. If the last exported .asc file is lost, you can export an .asc file from SailWind Layout to compare to the current schematic to generate the .eco file that gets imported into SailWind Layout to update the PCB layout. The same effect is created by Generating the ECO File in SailWind Layout and the process is semi-automated by automatically importing the .eco file.  

4. Click the Comparison Tab on page 507, and select the options you want to use for design comparison.  

5. (Optional) If you want to check the design differences before creating the ECO file:  

a. Select the Generate Differences Report check box in the Documents tab.   
b. Clear the Generate ECO File check box.   
c. Click Run. The netlist and PCB files are compared and differences written to Logic.rep in the \SailWind Projects folder. To see the differences, click Show Report in the Process Status dialog box.  

6. Select the Generate ECO File check box, and verify the ECO Filename.  

0 Tip Give the file a unique name to avoid overwriting any existing ECO files.  

7. Click Run.  

Output files are written to the \SailWind Projects folder.  

0 Tip In addition to the files listed above, messages or errors that occur during comparison are also written to Logic_Session.log and Logic.err in the \SailWind Projects folder.  

8. Send the ECO file to the layout designer for import into SailWind Layout.  

For the continuation of this process, see Forward Annotating by Importing an ECO File from SailWind Logic in the SailWind Layout Guide.  

See “Forward Annotation Results”.  

# Forward Annotation Results  

The forward annotation process generates a group of files (even in the background during the automated forward annotation process). These include an ECO file, a differences report, ASCII netlist files, and (optionally) an error report.  

Table 40. Forward Annotation Generated Files   


<table><tr><td><schematic_name>.eco</td><td>The ECO file. Contains ECO commands that describe the changes needed to update the original design to match the new design. Generated when you select Generate ECO File from the Compare/ECO Tools Documents tab. See “ECO File Format" on page 342 for a description of this file.</td></tr><tr><td>Logic.rep</td><td>The Differences Report file. Describes the differences between the “old" and the “new" compared files. Generated when you select Generate Differences Report from the Compare/ECO Tools Documents tab. See "Contents of the Differences Report" on page 340 for a description of this file.</td></tr><tr><td>ecogtmp0.asc ecogtmp1.asc</td><td>Temporary copy of the “old" netlist and a temporary copy of the “new" netlist.</td></tr><tr><td>ecogtmp[ 0|1 ].err</td><td>Generated only if errors are found in the netlist. A link to this file is displayed in the Output Window.</td></tr></table>  

In addition to the files listed above, messages or errors that occur during comparison are also written to logic_session.log and logic.err in the \SailWind Projects folder. The following are reported in the errors report file:  

• Library issues   
• Single or zero pin nets   
• Totally floating connections or subnets   
• Unnamed dangling connections (one end floating)   
• Power and Ground symbols used on nets whose name is different from the default name on the symbol  

Multiple subnet nets where one or more subnets is missing an off-page symbol • Single subnet nets with an off-page symbol (lonely subnet warning) • User named subnets that have no visible net name label  

**Related Topics**  

ECO File Format Contents of the Differences Report  

# Backward Annotation From SailWind Layout to SailWind Logic  

You can export your PCB layout changes “back” (known as backward annotation) to the schematic. You can choose between the three methods to backward annotate design changes.  

You can backward annotate part, gate, pin, net, and attribute changes. For details, see Backward Annotation Results.  

Method 1 — If you have both SailWind Logic and SailWind Layout on your computer, you can use the “Automated Backward Annotation Process”. While this automated method is the simplest and fastest, this method is not recommended because it generates its own .eco file by design comparison. You should use Method 2 to record the .eco file in SailWind Layout and manually import it into SailWind Layout for the best results. For more information, see Recorded Versus Generated ECO Files in the SailWind Layout Guide.  

• Method 2 — If SailWind Layout is on another computer and you want the layout designer to generate the ECO file, follow the process in “Creating the ECO File in SailWind Layout”. This is the most accurate method. You must manually import the .eco file into the SailWind Logic design.  

Method 3 — If SailWind Layout is on another computer and you must compare the designs and generate the ECO file within SailWind Logic, follow the process in “Creating the ECO File in SailWind Logic”. This method is not recommended since you are generating the .eco file by design comparison. You should use Method 2 to record the .eco file in SailWind Layout and manually import it into SailWind Layout for the best results. For more information, see Recorded Versus Generated ECO Files in the SailWind Layout Guide.  

Automated Backward Annotation Process Creating the ECO File in SailWind Layout Creating the ECO File in SailWind Logic  

# Automated Backward Annotation Process  

If SailWind Logic and SailWind Layout are on the same computer, you can use the SailWind Layout Link dialog box to compare a newer PCB design with an older schematic and update the older schematic from the newer PCB design. You can also create a differences report.  

This method generates a new .eco file and does not use a recorded .eco file. Recording the exact changes in an .eco file gives the best back annotation results. Use Method 2 for the best results. For more information, see Recorded Versus Generated ECO Files in the SailWind Layout Guide.  

# Restrictions and Limitations  

Transferring non-ECO-registered parts and non-electrical parts is constrained. See Options dialog box, Design Category on page 591 for details.   
• During design comparison, a reuse definition is ignored and actual elements in the physical design reuse are used in the comparison.   
• You cannot perform backward annotation between SailWind Logic and SailWind Router because SailWind Router does not export ECO files.  

# Prerequisites  

You must have the older schematic open in SailWind Logic, and the newer PCB design open in SailWind Layout.  

**Procedure** 

1. In SailWind Logic, click the Tools $>$ SailWind Layout menu item to open the SailWind Layout Link dialog box.  

![](/images/b0477ffe359f5f2a4f37540c7c67ec521a14371772c1948e2385bc68eab4a144.jpg)  

Tip   
If SailWind Layout is not open, the Connect to SailWind Layout Dialog Box appears. Click Open to open the PCB design you want to annotate from in SailWind Layout. In the File Open dialog box, select the .pcb file and click Open.  

2. (Optional) If you want to check the design differences before updating, click the Design Tab on page 614, and then click the Compare PCB button.  

The two versions are compared and differences written to Logic.rep in the \SailWind Projects folder. To see the report, click the logic.rep link in the Output Window.  

3. On the Preferences Tab on page 620, set the appropriate options.  

4. On the ECO Names Tab on page 618, set the appropriate options.  

5. On the Design Tab: on page 614  

a. If needed, check the Compare Design Rules and Show Net List errors report check boxes.   
b. Click the ECO From PCB button.  

# Creating the ECO File in SailWind Layout  

Create the .eco file of design changes using SailWind Layout and then import it into the SailWind Logic design. This enables you to synchronize changes done in SailWind Layout back to the schematic.  

This procedure only documents recording the .eco file as you made engineering changes to your design, which creates a before and after record of changes. Generating an .eco file by comparing designs will be electrically correct, but it does not create a perfect before and after record of components that are identical in their part types and connections. For more information, see Recorded Versus Generated ECO Files in the SailWind Layout Guide.  

If you neglected to record the .eco changes and you must generate the .eco file by comparing two designs, see Comparing Two Versions of a Design in the SailWind Layout Guide.  

# Restrictions and Limitations  

• Transferring non-ECO-registered parts and non-electrical parts is constrained. See Options dialog box, Design Category on page 591 for details.  

• During design comparison, a reuse definition is ignored and actual elements in the physical design reuse are used in the comparison.  

• You cannot perform backward annotation between SailWind Logic and SailWind Router because SailWind Router does not export ECO files.  

**Procedure** 

1. Record the engineering/netlist changes in an .eco file. For more details, see Recording ECO Changes in the SailWind Layout Guide.  

2. In SailWind Logic, click the Tools $>$ Options menu item, then click the Design category.  

3. Set the “Allow overwriting of attribute values in design with blank values from library attributes” check box appropriately to allow or prevent overwriting of non-blank attribute values with blank (“placeholder”) values from the library.  

4. With your design open in SailWind Logic, click the SailWind Logic File $>$ Import menu item.  

5. In the File Import dialog box, in the Files of Type: list, select ECO Files (\*.eco).  

6. Browse for and select the ECO file to import.  

7. Click Open.  

If no errors occur, the schematic is updated. If errors occur, the schematic is not updated, and the errors, along with a link to the ECO Import errors file, are written to the Output window.  

# Creating the ECO File in SailWind Logic  

Acquire the layout design in an .asc file format, compare it to the schematic design with the SailWind Logic Compare/ECO tools, and then import the .eco file of design changes into the SailWind Logic schematic design.  

This method generates a new .eco file and does not use a recorded .eco file. Recording the exact changes in an .eco file gives the best back annotation results. Use Method 2 for the best results. For more information, see Recorded Versus Generated ECO Files in the SailWind Layout Guide.  

# Restrictions and Limitations  

Transferring non-ECO-registered parts and non-electrical parts is constrained. See Options dialog box, Design Category on page 591 for details.   
• During design comparison, a reuse definition is ignored and actual elements in the physical design reuse are used in the comparison.   
• You cannot perform backward annotation between SailWind Logic and SailWind Router because SailWind Router does not export ECO files.  

# Prerequisites  

You must have an .asc file exported from SailWind Layout. For more details, see Exporting an ASCII File in the SailWind Layout Guide.  

**Procedure** 

1. In SailWind Logic, click the Tools $>$ Options menu item, then click the Design category.   
2. Set the “Allow overwriting of attribute values in design with blank values from library attributes” check box appropriately to allow or prevent overwriting of non-blank attribute values with blank (“placeholder”) values from the library.   
3. In SailWind Logic, click the Tools $>$ Compare/ECO menu item.   
4. In the Compare/ECO dialog box, click the Documents Tab on page 505.   
5. In the Original Design to Compare and Update area, select the Use Current Schematic Design check box.   
6. In the New Schematic Design with Changes area, browse for the new .asc file exported from SailWind Layout.   
7. Click the Comparison Tab on page 507, and select the options you want to use for design comparison.   
8. (Optional) If you want to check the design differences before creating the ECO file: a. Select the Generate Differences Report check box in the Documents tab. b. Clear the Generate ECO File check box. c. Click Run. The netlist and PCB files are compared and differences written to Logic.rep in the \SailWind Projects folder. To see the differences, click Show Report in the Process Status dialog box.  

9. Select the Generate ECO File check box, and verify the ECO Filename.  

Tip Give the file a unique name to avoid overwriting any existing ECO files.  

10. Click Run.  

Output files are written to the \SailWind Projects folder.  

0 Tip In addition to the files listed above, messages or errors that occur during comparison are also written to Logic_Session.log and Logic.err in the \SailWind Projects folder.  

11. Click the SailWind Logic File $>$ Import menu item.  

12. In the File Import dialog box, in the Files of Type: list, select ECO Files (\*.eco).  

13. Browse for and select the ECO file to import.  

14. Click Open.  

If no errors occur, the schematic is updated. If errors occur, the schematic is not updated, and the errors, along with a link to the ECO Import errors file, are written to the Output window.  

**Related Topics**  

Backward Annotation Results  

# Backward Annotation Results  

Backward annotation is supported at multiple levels of design activity. You can use backward annotation to exchange design updates and changes to attributes, parts, gates, nets, and pins. Results are dependent upon the type of design object data that you are updating.  

Attribute Level Backward Annotation Part Level Backward Annotation Gate Level Backward Annotation Net Level Backward Annotation Pin Level Backward Annotation  

# Attribute Level Backward Annotation  

If you add, delete or modify attributes in SailWind Layout, you can backward annotate new attributes and deleted attributes.  

# New Attributes  

A new attribute in a part updates all parts of the same type. If the attribute name does not exist, it is added with the assigned value.   
An error is created if the part does not exist.  

![](/images/1d2b45c84191b52508557125632fbd7fab6974a523544d11e92d1c7c48ebe015.jpg)  

Tip Unsupported attribute types, such as net or net class, are ignored.  

# Deleted Attributes  

• Deleting an attribute for a part-type deletes the attribute on all parts of that type in the design. • An error message is generated if the part or attribute name does not exist. If the attribute command specifies an object type not supported for general attributes, such as net or net class, the attribute command is ignored.  

**Related Topics**  

Creating the ECO File in SailWind Layout  

# Part Level Backward Annotation  

You can backward annotate added parts, changed parts, deleted parts, and the reference designator name.  

# Added Parts  

• A new sheet is created and all new parts are added to the sheet. Parts are placed on a grid so that parts of a medium size do not overlap. No attempt is made to avoid overlapping of larger parts.  

• An error message is generated if the reference designator of the newly added part already exists or if the part does not exist in the Library.  

![](/images/34f0b748ace83aab60ac6c1a557b316acd8a0fae4fe6aa31509814430988377c.jpg)  

Tip The part is not added to the schematic if the reference designator already exists.  

• If the part contains Signal Pins, these pins are included in the add pin function. Backward annotation does not currently support signal pins so an error message is created.  

# Changed Parts  

• If the changed part is a multigate part, all gates are updated to the new part type.  

• An error message is generated if the new part does not exist in the design or in the Library, or if the gate or pin count is incompatible.  

# Deleted Parts  

• If the deleted part is a multigate part, all gates are deleted.   
• An error message is generated if the part is still connected to a net or the part does not exist.  

# Reference Designator Name  

• If the part being renamed is a multigate part, all gates are updated.   
• An error message is generated if the old reference designator does not exist.  

**Related Topics**  

Creating the ECO File in SailWind Layout  

# Gate Level Backward Annotation  

If you swap gates in SailWind Layout to improve your routing, you can backward annotate the swapped gates to the schematic.  

SailWind Logic creates an off-page symbol at each swapped gate. An error message is created if the gate does not exist.  

**Related Topics**  

Creating the ECO File in SailWind Layout  

# Net Level Backward Annotation  

You can backward annotate joined nets, nets created by splitting an existing net, and renamed nets.  

# Joined Nets  

The first net is renamed to be the same name as the second net.  

# Nets Created by Splitting an Existing Net  

• A Delete Pin from Net operation is performed to remove them from the existing net, followed by an Add Pin to Net operation to add the pin to the new net.  

# Renaming Nets  

• All subnets of the old net on all sheets are renamed. If any of the subnets contain Power or Ground symbols without netnames, netnames are added to these symbols.  

• An error message is created if the new net already exists.  

**Related Topics**  

Creating the ECO File in SailWind Layout  

# Pin Level Backward Annotation  

You can backward annotate swapped pins, pins added to a net, and pins disconnected from a net.  

# Swapped Pins  

• SailWind Logic creates an off-page symbol at each swapped pin.  

# Pins Added to a Net  

• A pin can be added only if it is not already connected to another net. If the pin is a gate pin (a visible terminal pin on the gate symbol), an off-page symbol is created.  

• An error is created if pin is already connected or the pin is a signal pin already assigned to a net.  

# Pins Disconnected From a Net  

• If the pin is a gate pin, the connection is deleted if it connects to a tie-dot or off-page symbol. If the connection goes to another gate pin, the connection is broken and, an off-page symbol is added. • This command generates an error message if the pin is not connected to the net in question.  

**Related Topics**  

Creating the ECO File in SailWind Layout  

# Contents of the Differences Report  

When you compare two versions of a design (Tools $>$ Compare/ECO), you can create an output file that lists the differences between the two versions. The report file is named Logic.rep and is written to the \SailWind Projects folder.  

Table 41. Sections of the Difference Report   


<table><tr><td>Option</td><td>Description</td></tr><tr><td>Part differences</td><td>This section of the report includes the reference designator and the part type for both the old and new designs. Parts that exist only in the old design are listed under the New Design column as <none>. Parts that exist only in the new design are listed under the Old Design column as <none>. Parts that have identical reference designators and part types in both designs are not listed.</td></tr><tr><td> Net differences</td><td>This section lists names of the nets that do not exist under two columns: New Design and Old Design. It lists the names of the nets that do not exist in one design or the other. It also lists the nets that match, but that have different names, including nets in the old design that have been split into multiple nets in the new design. A net split operation appears as pin differences. Nets are listed alphabetically under the Old Design column, except where multiple nets are combined, where they are listed in succession. Nets that do not exist in the old design are listed at the end of this section.</td></tr><tr><td>Unmatched net pins in old design</td><td>This section lists any connected pins in the old design that are missing or connected to other nets in the old design. These pins are deleted from nets during the ECO process. This list provides net names in the old design followed by unmatched pins in the net. If the net does not exist in the new design, all pins in the net are listed.</td></tr><tr><td>Unmatched net pins in new design</td><td>This section lists any connected pins in the new design that are missing or connected to other nets in the old design. These pins are added to nets during the ECO process. This list provides net names in the new design followed by unmatched pins in the net. If the net does not exist in the old design, all pins in the net are listed.</td></tr><tr><td>Attribute differences</td><td>This section of the report lists each object under the headings: Atribute Name, Old Value, and New Value. Subheadings, including object type, object name in old design, and object name in new design appear for each object in the list if different.</td></tr></table>  

<table><tr><td colspan="2">Table 41.Sectl terenceReport (cohtihued)</td></tr><tr><td>Option</td><td> Description</td></tr><tr><td></td><td>Attribute differences are included only for objects that exist in both the old and new design. If an attribute is missing in either design, the value is listed as <no attr>. If the attribute exists, but has no value, it is listed as <no value>.</td></tr><tr><td></td><td>This section reports each object or object pair that has rules differences. Each object or object pair has three columns of information (Object Type, Object Name, and Rule Type) and a subheading that lists Rule Name, Old Value, and New Value. If a rule set is missing on an object in either the old or new design, then the old or new values of all missing rule entries are listed as <no rule>. The following example shows a high-speed rule change for net $$$1963 that </td></tr><tr><td>NET MAX_LENGTH MIN_IMPEDANCE</td><td>$$$1963 HIGH_SPEED 50000 20000 50.0 70.0</td></tr><tr><td>Net class differences</td><td>This section reports the names of net classes that: · Do not exist in one design or the other. (Classes that do not exist in the Original Design appear at the end of the section.) · Match but have different names</td></tr><tr><td>Added class nets</td><td>This section reports nets that are not in the Original Design and are added in the New Design. (The net class in the New Design has nets either not included in the Original Design or are included in different net classes in the Original Design.) This section lists: ·Each net class that has added nets in the New Design and the names of the</td></tr><tr><td>Removed class nets</td><td>Original Design) This section reports nets that are in the Original Design but have been removed from the New Design.(The net class in the Original Design has nets either not included in the New Design or included in different net classes in the New Design.) This section lists:</td></tr><tr><td>Pin-pair group differences</td><td>of those removed nets · All of the nets in the net class if the net class does not exist in the New Design This section lists pin-pair groups that: · Do not exist in one design or the other. (Pin-pair groups that do not exist in the</td></tr><tr><td> Removed group</td><td>Original Design appear at the end of the section.) · Match but have different names. This section reports pin-pairs that are in the Original Design but removed from the</td></tr></table>  

Table 41. Sections of the Difference Report (continued)   


<table><tr><td>Option</td><td>Description</td></tr><tr><td></td><td>This section lists: · Each group in the old design from which pin-pairs were removed and the names of its removed pin-pairs · All of the pin-pairs in the group if the group does not exist in the New Design</td></tr><tr><td>Added group pin-pairs</td><td>This section reports pin-pairs in the New Design that are not in the Original Design. (The pin-pair group in the New Design has pin-pairs either not included in the Original Design or included in different groups in the Original Design.) An ECO operation adds these pin-pairs. This section lists: · Each group with added pin-pairs in the New Design and the names of added</td></tr></table>  

**Related Topics**  

Compare/ECO Tools Dialog Box, Documents Tab  

Compare/ECO Tools Dialog Box, Comparison Tab  

# ECO File Format  

The format used is similar to PADS-format ASCII. Each type of data begins with a header line with a key word surrounded by asterisks $(^{\star})$ .  

The first line of the file is formatted:  

\*PADS-ECO\*  

The end of the file (EOF) entry is formatted:  

![](/images/9476f2486c5130c2e7c57a3b37c1827b7e2706aec7bdd131bff1288ea5b5deb0.jpg)  

Add remark lines with the entry:  

\*REMARK\* remark information etc.  

The following are the available ECO commands.  

# Add a Pin to the Net  

The command starts with the format:  

\*NET\*  

A line indicating the net to which the pin is added follows this line:  

\*SIGNAL\* netname 10  

where netname is the net to add the pins to and 10 is the trace width to associate with the connections. If the net name does not currently exist in the design, it will be added. This is followed by the pin(s) to add to the net as shown below:  

ref1.pin1 ref2.pin2  

Add a Part  

The command is formatted:  

<table><tr><td>*PART*</td></tr></table>  

The part entry line is formatted:  

refdes parttype  

where refdes is the part reference name and parttype is the part type name. When parts are added in the PCB, they will be placed at system origin of 0,0. If a board outline is present, the parts are instead placed at the lower left corner of its box.  

# Join Two Nets Together  

The command starts with the format:  

![](/images/dd1204ecb2d380d653b6f449cb622ac345a5028facc3afb2fc19583351ca58e1.jpg)  

This is followed with the line indicating the nets to join:  

OLDNET0 OLDNET1  

where OLDNET0 and OLDNET1 are the names of the nets to combine. The new combined net uses the name of OLDNET1. A connection is added between the nets using two random pins in the selected nets. The trace width of the added connection is the same as that of a connection in the first net (OLDNET0).  

Delete a Part  

The command is formatted:  

<table><tr><td>*DELPART*</td></tr><tr><td></td></tr></table>  

The line is formatted:  

refdes parttype  

where refdes is the part reference name to delete and parttype is the part type name. If all pins of the part to be deleted have not already been disconnected from the connection nets in the design, an error is reported.  

Delete a Pin from a Net  

The command starts with the format:  

![](/images/05ff1286cf353a487dee98b443698eb776e00fbfee2d7c903be63eca5a94adda.jpg)  

This is followed by a list of pins to delete from each net, in the form:  

refdes.pinnumber signame  

where refdes is the part reference name, pinnumber is the pin number to disconnect, and signame is the net of which the pin is currently part.  

# Change a Component's Part Type  

The command is formatted:  

<table><tr><td>*CHGPART*</td></tr></table>  

The change part line is formatted:  

refdes oldparttype newparttype  

where refdes is the reference name of the part to change, oldparttype is the old part type, and newparttype is the new part type.  

Split a Net into Two Nets  

The command starts with the format:  

\*SPLITNET\* SPLIT NET INTO TWO NEW NETS  

Two lines follow, listing the new signal names and the pins:  

\*SIGNAL\* oldsigname ref1.pin1 ref2.pin2 \*SIGNAL\* newsigname1 ref3.pin3 ref4.pin4  

where the pins following the \*SIGNAL\* statement are in the first net, and those following the second line are in the second net.  

Rename a Part  

The command is formatted:  

\*RENPART\*  

The rename line is formatted:  

oldrefdes newrefdes  

where oldrefdes is the old name and newrefdes is the new name. To facilitate the renaming operation, duplicate name checking is not run until after all rename information has been read. This allows the above rename list to run without a conflict. If any error is encountered, no parts in the list are renamed.  

# Rename a Net  

The command is formatted:  

\*RENNET\* RENAME NET  

The rename net entry line is formatted:  

oldname newname  

where oldname is the old net name and newname is the new net name.  

Swap a Gate  

The command is formatted:  

\*SWPGATE\* GATE1 GATE2  

Swap Pins  

The command is formatted:  

\*SWPPINS $\star$ REFDES PIN1.PIN2  