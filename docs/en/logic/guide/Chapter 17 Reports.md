# **Chapter 17 Reports**

You can generate reports to view and analyze data related to your design. Available reports include

unused pins, parts statistics, net statistics, limits, connectivity, and a bill of materials. Use these reports to

examine and interpret your design status at any point in the design cycle.

Generating Reports

The Bill of Materials Report

## **Generating Reports**

Use the Reports dialog box to produce any of six different types of reports on the current schematic. You

can save these reports as text files on your hard disk or output them to a printer.

**Procedure**

1. Click the **File > Reports** menu item.
2. In the Reports Dialog Box, select each report you want to generate.
3. To specify or modify the report characteristics of the Bill of Materials report, click **Setup**.

See also The Bill of Materials Report.

4. Click **OK**.

The reports are generated and the dialog box closes.

SailWind Logic Guide 

313Reports

The Bill of Materials Report

## **The Bill of Materials Report**

The Bill of Materials report produces a user-configurable list of the parts contained in the current 

schematic. You can direct any part attribute in the schematic to a Bill of Materials report.

In the Bill of Materials Setup dialog box on page 479 are three different tabs for controlling report

characteristics from which to choose:

Setting Up the Bill of Materials Attributes

Setting Up the Bill of Materials Format

Setting Up the Bill of Materials Configuration

### **Setting Up the Bill of Materials Attributes**

Use the **Attributes** tab to modify the Attribute content, the corresponding column headings, and column 

width of the report.

The attribute order in the content list determines the column arrangement in the BOM report. There is a 

limit of 12 attributes in the Bill of Materials report.

**Restrictions and Limitations**

Including non-ECO-registered parts and non-electrical parts in the bill of materials is constrained. See 

Options Dialog Box, Design Category for details.

**Procedure**

1. Click the **File > Reports** menu item.
2. In the Reports Dialog Box select the Bill of Materials check box and then click **Setup** to specify or 

modify the Bill of Materials report characteristics.

3. In the Bill of Materials Setup dialog box on page 479, click the **Attributes** tab.
4. To add a new attribute to the list, click **Add** and select an attribute from the list in the Part Attribute 

column,

**Tip**

You can list up to twelve attribute names. Each attribute defines a column in the BOM

report.

5. In the Field Header column, specify the column heading for each attribute in the report. You can

specify any character except the colon ( : ).

6. In the Width column, type an integer between 1 and 200 that represents the number of characters 

across the column for each attribute in the report.

**Tip**

SailWind Logic reserves a space to separate columns. Therefore, the actual column width 

is one character less than the specified number.

314 

SailWind Logic GuideReports

Setting Up the Bill of Materials Format

7. To move an attribute up a row, select the attribute to move and click **Up**.
8. To move an attribute down a row, select the attribute to move and click **Down**.
9. To edit an attribute, select the box to edit and click **Edit**.

**Restriction:**

You cannot edit the part attribute name, but you can select a new attribute to replace the

one currently listed.

10. To remove an attribute from the report, select the row and click **Remove**.
11. To restore the default content from the *.ini* file, click **Reset**.
12. Click **OK**.

### **Setting Up the Bill of Materials Format**

Use the **Format** tab to modify the output format of the Bill of Material report. This enables you to specify 

which fields to display and how the information will be displayed in the generated report.

The default settings originate from the *.ini* file.

**Restrictions and Limitations**

Including non-ECO-registered parts and non-electrical parts in the bill of materials is constrained. See 

Options Dialog Box, Design Category for details.

**Procedure**

1. Click the **File > Reports** menu item.
2. In the Reports Dialog Box select the Bill of Materials check box and then click **Setup** to specify or 

modify the Bill of Materials report characteristics.

3. In the Bill of Materials Setup dialog box on page 483, click the **Format** tab.
4. Select the type of delimiter you want to distinguish the report columns.

• **Separator** — places a vertical bar between report fields

• **Tab** — separates columns with a tab spacing

• **Comma** — places a comma character between report fields

• **Custom** — specify any character as a delimiter

5. Type a report title in the Report Title box.

**Tip**

The variable %j is replaced by the filename and %d is replaced by the date.

SailWind Logic Guide 

315Reports

Setting Up the Bill of Materials Configuration

6. Select the Combine Value/Tolerance check box to combine the Value and Tolerance attributes of a

part in the part name.

For example, the 1/4 watt resistor would have a part type name of R1/4W or R1/4W.4.7K,+/-5%.

SailWind Logic evaluates parts that have either a different Value or Tolerance attribute as different

part types.

7. In the Ref. Designator Separation Mode settings choose between giving each component a 

single line (Single Ref. Designator per line) or displaying the reference designators of identical 

components on one line (Multiple Ref. Designators per line).

If you choose multiple reference designators per line, you can also specify to compress ranges of 

reference designators and the delimiter between them.

8. Select an attribute in which to sort the report list in the Sort By list.

**Tip**

Select None to sort by Part Type.

9. Select the output file format from the File Format list.
10. To save report format settings for the current design to a specified file so you can create different

format configurations for different designs, click **Save As** and type a filename the Save Scheme 

dialog box.

SailWind Logic saves BOM format settings files in the \*Settings* folder with a *.bom* extension.

**Tip**

Click **Delete** to remove the selected setting file from the list.

11. To restore the default content from the *.ini* file, click **Reset**.
12. Click **OK**.

### **Setting Up the Bill of Materials Configuration**

Use the **BOM Config** tab to preview the Bill of Materials report format and copy any selected lines of the 

file to a Windows clipboard. You can also export the BOM report to a TXT/CSV file.

The default view orders the attributes by the sort field you specified on the **Format** tab.

**Restrictions and Limitations**

Including non-ECO-registered parts and non-electrical parts in the bill of materials is constrained. See 

Options Dialog Box, Design Category for details.

**Procedure**

1. Click the **File > Reports** menu item.
2. In the Reports Dialog Box select the Bill of Materials check box and then click **Setup** to specify or 

modify the Bill of Materials report characteristics.

3. In the Bill of Materials Setup dialog box, click the **BOM Config** tab.

316 

SailWind Logic GuideReports

Setting Up the Bill of Materials Configuration

4. To sort rows by an attribute other than the one you set on the **Format** tab, click the heading area of 

the attribute you want to sort.

To sort the same column in reverse order, click again.

5. Copy any selected lines of the file to a Windows clipboard:

a. To include the column header information in the report, select the Include table header check

box.

b. Select the rows you want to copy to the clipboard and click **Copy**.

**Tip**

Click **Select All** to select the entire table.

6. Export to a TXT/CSV file.

a. To exclude any row in the report, select the NC checkbox.

b. Click **Export**, and choose the file type in the popup dialog box.

7. Click **OK**.

SailWind Logic Guide 

317Reports

Setting Up the Bill of Materials Configuration

318 

SailWind Logic Guide