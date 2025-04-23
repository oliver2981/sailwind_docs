# Chapter 19 Plotting and Printing  

Various options are available for plotting and printing your design output. You can choose to print your design on a printer connected to your computer or network for a quick visual design review. You can generate output to a pen plotter or a photo plotter. You can also generate an intelligent PDF file for sharing you design output electronically.  

Setting Printing and Plotting Output Options   
Previewing Your Output   
Creating a PDF   
Plotting Output   
Setting Up a Pen Plotter   
Adding a New Pen Plotter   
Setting Up a Photo Plotter   
Printing Output   
Printing to PDF   
Setting the Printer to Print to a File  

# Setting Printing and Plotting Output Options  

Use the Options dialog box to set the output options for printing or plotting. Setting options enables you to set the position, orientation, and color of selected sheets and objects.  

**Procedure** 

1. In the Print or Plot dialog box, click Options.   
2. In the Sheet Selections area in the Options dialog box, select the name of the available sheets to   
   add to the Sheets to Print list, and click Add.   
3. Select an Orientation angle and a Justification position for the output.   
4. Type an offset value in the X Offset and Y Offset boxes.  

!Tip  

When setting an offset. observe the following:  

• You can only set offsets if you clicked something other than Scale to Fit and Centered in the Justification list. • The print or plot location is calculated after the plot is rotated and scaled.  

5. In the scaling boxes, type the plot size to actual size ratio.  

Example: A 2 to 1 scaling results in a printout or plot that is twice the actual size.  

!Tip  

The Preview area graphically shows the position, orientation, justification, and scaling of the output.  

6. In the Items area, select the check boxes for the items you want to include in your output.  

7. In the Selected Color area, click a color tile, then in the Items area, click the tile to the right of the item to change its color.  

8. Select the Plot Jobname check box to output the schematic name, time, and date.  

9. Select the Print Window check box to print the displayed window.  

10. Click OK to return to the Print or Plot dialog box.  

# Previewing Your Output  

You can use the Selections Preview dialog box to preview your options and output. This enables you to examine the output and determine if you need to make any changes before generating your final output files.  

**Procedure** 

1. Click the File $>$ Plot or the File $>$ Print menu item, then in the Plot or Print dialog box, click the Preview button to open the Selections Preview dialog box and verify the settings for the selected sheets you want to print or plot.  

2. In the Selections Preview dialog box, click Print or Plot to send the output to the printer or plotter.  

![](/images/66f2135aad6ec8f2b37c86a89d407113989700d186d1ec6a392acf23152169a4.jpg)  

!Tip  

You can navigate within the Selections Preview dialog box using the following methods:  

• Zoom into the Sheet or Extents of the selected sheet by clicking the appropriate buttons. • Click the left mouse button in the preview window to zoom in at the cursor location. Click the right mouse button to zoom out.  

# Creating a PDF  

You can create an intelligent PDF of your schematic, choosing which sheets you want to share and show to others in your organization. You can create the PDF in full-color or black and white, with hyperlinks to part attributes, and with search capabilities, making it easy to locate parts and nets. Once you locate a net, you can find other instances of it through the entire schematic, even when the net is on a different page. You can also create a black and white, non-searchable PDF of your schematic.  

See also Printing to PDF.  

![](/images/46335afef92c6ffc08eb546b671f6b8c1c036997540e0153d1ee02c46641dd9e.jpg)  

Tip Adobe® Acrobat® Distiller™ is not required on your system to create a PDF.  

# Restrictions and Limitations  

To search a PDF, you must substitute the Stroke font with a System font.  

**Procedure** 

1. Click the File $>$ Create PDF menu item.  

2. In the File Create PDF file dialog box, type the name of the PDF and then click Save.  

![](/images/37515f2868216eefa7c6dab53d865995fef224553baa23972af02d45c199c8ee.jpg)  

Tip The default name of the file is the name of the schematic with a PDF extension.  

3. In the Create PDF dialog box, in the Sheets to PDF list, select the schematic sheets you do not want to include in the PDF, and then click Remove.  

![](/images/412601df0146bc12349eb0d76e3b0d9a911f17f9768fdbf764456de69c29a784.jpg)  

Tip By default, all schematic sheets are selected for PDF creation.  

4. To automatically open the resulting PDF, select the “View PDF after creation” check box.  

5. To replace a stroke font in your schematic with a system font in the PDF, select the “Replace stroke font with” check box, and then select a font from the list.  

Use the Font style buttons to add Bold, Italic, or Underline styles.  

**Restriction:**  

When replacing stroke fonts, the following restrictions apply:  

• You can only search a PDF if you replace the Stroke font with a System font.   
• There is no font size control. Text heights are already set for each text item in the design. The height will be converted to the nearest point size in the PDF.  

6. To be able to view part attributes such as the reference designator and the part type in the PDF, select the “Create hyperlinks that will display part attributes” check box.  

In the resulting PDF, you will see yellow boxes around each part. If you click inside the box, you will get a listing of the part attributes.  

7. To enable finding the next instance of a net or bus in the PDF, select the “Create hyperlinks that will pan through nets” check box.  

**Restriction:**  

If the net name is not visible in the schematic, you will not be able to pan through the nets.  

In the resulting PDF, you will see blue boxes around each net name and bus name. If you click inside the box, you will pan to the next instance of that net or bus.  

8. To create hyperlinks on parts, net names, and buses without their yellow and blue boxes, clear the “Visible rectangle around objects with hyperlinks” check box.  

In the resulting PDF, the hyperlinks will be invisible.  

9. In the Color Scheme area, click the scheme of your choice.  

!Tip  

The colors used in the Color on Black or Color on White schemes are the same colors currently used in your schematic. The Black on White scheme shows all currently visible items in the schematic in black.  

10. Click OK.  

# Plotting Output  

After you have completed you design you can generate output for design review. You can output your designs to pen plotters or photo plotters.  

**Procedure** 

1. Click the File $>$ Plot menu item.   
2. Choose Pen Plot or Photo Plot.   
3. Set up output options on page 347.   
4. Set up the pen plotter on page 350 or photo plotter on page 352.   
5. Preview your output on page 348.  

6. Click Run.  

!Tip  

The Plot dialog box displays the following information related to the plot configuration:  

• The Summary area lists the numbered available sheets you can plot, and the items contained in the sheets. • The File Prefix box lists the prefix name of the file you want to plot.  

**Related Topics**  

Printing to PDF   
Setting the Printer to Print to a File   
Printing Output  

# Setting Up a Pen Plotter  

Before you can output your design to a pen plotter, specific options need to be configured so that the output is correctly reproduced by the plotting device. Use the Pen Plotter Setup dialog box to set various options for the plotter.  

**Procedure** 

1. Click the File $>$ Plot menu item.   
2. In the Plot dialog box, click Setup.   
3. Type the number of pens (1-16) in your device, and type the pen line width in mils.   
4. Select the Rotate Axis check box to reverse the X and Y axes of the design.   
5. To assign colors, click a Selected Color tile, and then click a pen number in the Pen Colors area. Repeat this step for every pen listed.   
6. Click a Plotting Size button, or click Other to define a custom size. If you click Other, type the X and Y dimensions to use.   
7. In the Device list, select the plotter device to use.  

# Adding a New Pen Plotter  

Use the Pen Plotter Advanced Setup dialog box to add a new pen plotter to the list of available plotters.  

# Restrictions and Limitations  

You can also edit the data for an existing plotter, but only if it is a custom setup.   
• You cannot modify the SailWind-supplied advanced plotter settings.  

**Procedure** 

1. Click the File $>$ Plot menu item.   
2. In the Plot dialog box, click the Setup button.   
3. In the Pen Plotter Setup dialog box, click the Advanced button.   
4. Type the name of a different pen plotter you want to use. Exception: Do not reuse one of the existing, supplied device names.   
5. In the device type list, select the interface language the plotter uses: HPGL or HGML.   
6. Set the plotter resolution by providing a scaling ratio. Type a number in the Multiplier and Divisor boxes. The ratio defined is the scale factor to convert from mils (0.001 in) to plotter units. Example: Most Hewlett-Packard plotters have a resolution of $0.025\mathrm{~mm}$ or $1/40~\mathsf{m m}$ . This means that a distance of one inch (1000 mils) is 1016 plotter units $(25.4\times40)$ . So a ratio of 1016 to 1000 would be defined. The ratio actually used is 254 to 250 which is the same as 1016 to 1000.   
7. Select the Origin at Center check box if the origin of the plotter is at the center of the paper. Clear this check box if the origin is in the lower left corner or other location.   
8. Click OK to return to the Pen Plot Setup dialog box.   
9. Click OK to return to the Plot dialog box.  

**Related Topics**  

Setting Up a Photo Plotter  

# Setting Up a Photo Plotter  

Before you can output your design to a photo plotter, specific options need to be configured so that the output is correctly reproduced by the plotting device. Use the Photo Plotter Setup dialog box to define the aperture and other photo plotter options.  

**Procedure** 

1. Click the File $>$ Plot menu item.  

2. In the Plot dialog box, select Photo Plot, and then click the Setup button.  

3. To add a new D-code to the D-Code list, click Add, type a code, and click OK.  

4. To delete a D-code, select a code in the D-Code list, and click Delete.  

Alternatives:  

• Click the Augment button to automatically generate D-codes for items in the schematic file that are not in the current list. Click the Regenerate button to clear the current D-code list and automatically add D-codes for all items in the schematic.  

5. Set the shape for a selected D-code.  

• Select the Same Aperture for Flashes/Lines check box to draw lines and flashed items with the same aperture. Round and square shapes for lines will be gray.   
• If you clear this check box, then you can click either Flash (to set a flash aperture) or Line (to set a draw aperture).   
• In the Width box, type a diameter for round shapes. This box is unavailable if a width is not appropriate for the specified shape.  

6. In the Aperture Count box, type the maximum aperture count.  

7. Select the Augment on-the-fly check box to add apertures to the D-code list when photo plots are run if any newly created lines were added to the schematic. When you open the Photo Plotter Setup dialog box, the necessary apertures will be present.  

8. In the Photo Plotter Setup dialog box, click the Advanced button.  

9. Click English for mils or Metric for millimeters.  

10. To specify the precision of the output file coordinates, type the number of digits that should lead and trail the decimal point. Type the digits in the Leading and Trailing boxes.  

11. To set the coordinates for the output file, click Absolute for absolute coordinates, or click Incremental for relative coordinates.  

12. Define how to handle zero suppression in the output file:  

• Click None to retain leading and training zeros.   
• Click Leading to suppress zeros before the decimal point. Click Trailing to suppress zeros after the decimal point.  

13. Define how to draw arcs and circles:  

Click None if your photo plotter does not support circular interpolation. Arcs and circles are drawn as small straight-line segments. • Click Quadrant if your photo plotter does not support full, 360-degree circular interpolation. • Click Full if your photo plotter supports full, 360-degree circular interpolation.  

14. To set the plotting size, click a Plotting size button, or click Other to define a custom size. If you click Other, type the X and Y dimensions to use.   
15. Select the Suppress Repeated Coords check box to eliminate repeated coordinates from the output file.   
16. Click OK to return to the Photo Plotter Setup dialog box.   
17. Click OK to return to the Plot dialog box.  

**Related Topics**  

Setting Up a Pen Plotter  

# Printing Output  

You can output your design to any standard printer that is connected to your system. Set up your print options as required by your installed printer driver.  

**Procedure** 

1. Click the File $>$ Print menu item.  

![](/images/cd42e64e4d925febad695dee81dcb33bb9bb67a0084dd1b7bee1f4bb06f86b87.jpg)  

Note: If you have previously set up your printer configuration options, then on the toolbar, click the Print button to immediately print your design using the last saved print configuration.  

2. Select the name of the printer to which you want to print.  

3. Set up print options on page 347.  

4. Click Network to display the Connect to Printer dialog box.   
5. Preview your output on page 348.   
6. Click OK to send the output to the printer.  

**Related Topics**  

Printing to PDF Setting the Printer to Print to a File  

# Printing to PDF  

You can print your schematic sheets to a single PDF. The resulting PDF is a non-searchable, black and white image of your schematic.  

To create a color PDF that is searchable, see the Creating a PDF topic.  

# Restrictions and Limitations  

You must have a PDF generator (such as Adobe PDF, Cute PDF, or Microsoft Print to PDF) installed before you can print to PDF.  

**Procedure** 

1. On the toolbar, click the Print button.   
2. In the Print dialog box, select your preferred PDF generator in the Printer name list.   
3. Click OK.  

**Related Topics**  

Creating a PDF Plotting Output Printing Output  

# Setting the Printer to Print to a File  

SailWind Logic supports PostScript printing to a file through the use of the Windows printer properties.   
Before you create a PostScript file, you must first set up the printer to print to a file.  

**Procedure** 

1. Locate printer information based on your platform:  

For Windows 7 Professional, click Start, click Control Panel, then double-click Devices and Printers. • For Windows 10, click Start, click the Settings icon, click Devices, then click Printers and scanners.  

2. Select the PostScript printer you want to use, then right-click and click Properties.  

3. Click the Ports tab.  

4. In the Port column, select the Print to File check box.  

![](/images/09f2df7ed2484d22c60df3f48e8c6a9d63a728e0aff2e596783043da0ec43989.jpg)  

!Tip  

This procedure works with local printers. If you are using network printers, you may not have access rights to select or change the port information.   
The options on the Ports tab may differ depending upon the specific version of your operating system.  

5. ClickOK.  

**Related Topics**  

Printing to PDF Plotting Output Printing Output  

