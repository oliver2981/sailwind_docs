# Chapter 13 Connections  

Connections are the heart of your design and enable you to capture and convey the interconnectivity of your design. SailWind Logic offers a robust selection of commands for working with adding, naming and connecting nets. You can fully connect you design objects, or use floating connections as placeholders for future design decisions. You can add, move split nets or segments. You can also swap pins on your parts as needed. There are also a powerful set of commands available for creating, editing, and managing buses.  

Adding Connections   
Naming a Connection   
Net Attributes Overview   
Creating Net Attributes   
Default Attributes for Nets   
Adding Power and Ground Connections   
Working With Floating Connections   
Editing Off-Page Symbol Sheet Numbers Per Line   
Changing a Connection   
Moving Connections   
Splitting a Connection   
Splitting Segments   
Swapping Pins   
Managing Buses   
Deleting Connections   
Detach  

## Adding Connections  

When you add connections, they must have start and end points that are electrically meaningful. Start a connection on either a symbol pin or another connection. End a connection on a symbol pin, another connection, a bus, an off-page reference, or a ground or power symbol. SailWind Logic prevents you from starting or ending a connection just anywhere in the database unless you enable Floating Connections.  

See also Working With Floating Connections.  

**Procedure** 

1. Click the Add Connection button.   
2. Indicate the starting point of the connection. The connection follows the cursor movement. Rightclick and click Angle to specify diagonal segments in the connection.   
3. Indicate corners as needed. Right-click and click Del Corner to back up to the previous corner if necessary.   
4. A connection cannot end in open space. Locate the cursor and double-click to end the connection.  

5. To end a connection with a power, ground, or off-page reference symbol, select the appropriate symbol from the popup menu during the last step of this procedure.  

If you end the connection on a bus, see the remaining steps in the Adding Connections to Buses topic.  

![](/images/e81bf3d9c74ebbb85e48a14d8beee479e38c7f6011db320160e431cba16e7906.jpg)  

!Tip  

Special Symbols in SailWind Logic include power symbols, ground symbols, and off-page reference symbols. For more information, see Special Schematic Symbols.  

![](/images/32459aaa0778a24b44502d96dc3d5d5fa788d7b75b05477e148d315f4e0a6ecb.jpg)  

!Note:  

When you end a connection at another connection, SailWind Logic places a tie dot at the junction. The resulting net name is the name of the added connection, not the existing connection, unless you assign a name to the existing connection.  

6. To assign a fixed net name to a connection, you must first add the connection and then select a segment that is directly attached to a part type pin. Then, you can select the net, right-click and click Properties, and enter the new net name in the Net Properties on page 289 dialog box.  

![](/images/c464ff6378a1639129c9fd84bd51c72589bc804c18bed7c1fd6712d2d842f619.jpg)  

!Tip  

If you select and move a visible net name, with snap to grid enabled, the new net name snaps to the Labels and Text grid. To set the labels and text grid, use the settings on the Tools $>$ Options $>$ General page. See “Options Dialog Box, General Category” on page 595.  

**Related Topics**  

Adding Power and Ground Connections Adding Off-Page References  

## Naming a Connection  

When you add a connection, SailWind Logic automatically assigns a name with the format $\$59$ nnnn, where nnnn is a random number. You can specify a different net name to replace the assigned name.  

**Procedure** 

1. Select a connection segment.   
2. Right-click and click Properties.   
3. Type a new net name in the Net Name box.  

![](/images/b36728ca03c4dfaf9f5a260de0eec0953b2a5fa9205d2071d04ec5649fe87501.jpg)  

!Tip  

The Net Name Label check box exhibits the following behaviors:  

• The Net Name Label check box is only available when you select a connection segment   
that enters or exits a part.   
• Clearing the Net Name Label check box removes the visible label. The net and all subnets retain the net name.  

4. To place a bar over the net name, precede the text with the \ character. To place a bar over only a portion of text, enclose that section with the \ character.  

For example, typing MAIN_\CLK\ places a bar over CLK.  

![](/images/7d1ad0063f43755e6687344636af4bc2e6de240fffd3b174fc2851c553d2957a.jpg)  

The \ character factors into the 47 character limit for the net name.  

**Related Topics**  

Modifying Nets  

## Net Attributes Overview  

Net attributes enable you to associate information with a single net or set of nets on the schematic.   
Attributes are made of two parts, an attribute name and its corresponding value.  

If connecting to SailWind Layout, these attributes are passed along with the rest of the schematic.  

![](/images/eab04590c856356e11074d12f2ca9f7fbabedf08a6465e704300f7b96522c747.jpg)  

!Tip  

When working with attributes, note the following:  

• SailWind Layout checks a limited set of net attributes. See the Default Attributes for Nets topic for more information.   
• To assign attributes to signal pins, see the Signal Pin Nets topic.  

See also Creating Net Attributes.  

## Creating Net Attributes  

You can create net attributes and assign them to specific nets. Once created, the attributes can be edited or deleted.  

**Procedure** 

1. Select a net, right-click and click Attributes.   
2. In the Net Attributes dialog box, click Add to add an attribute.   
3. Click the Name column and type a new attribute name. See also Default Attributes for Nets.  

4. Click the Value column and type an attribute value.   
5. To remove the selected net attribute, click Delete.   
6. To edit the selected name or value, click Edit.   
7. Click OK.  

## Default Attributes for Nets  

Refer to the Listing of Default Attributes for Nets table to determine which net attributes are checked by SailWind Layout for correct values and units.  

0 Tip Some values in the Description and use column are case-sensitive and must be written as such.  

Table 30. Listing of Default Attributes for Nets   


<table><tr><td>Attributes</td><td>Type</td><td>Description and Use</td></tr><tr><td>HyperLynx.Frequency</td><td>Frequency (Measure)</td><td>Lists the working frequency for nets in BoardSim simulations. Range: 0 Hz-1000 GHz Units: Hz kHz MHz GHz (case-sensitive)</td></tr><tr><td>HyperLynx.Duty Cycle</td><td>Percentage (Measure)</td><td>Lists the percent of time the signal is in high state. Used for BoardSim simulations. Range: 0%-100%</td></tr><tr><td>HyperLynx Signal Type</td><td>List</td><td>Lists the signal type. Used in BoardSim simulations. Values (case-insensitive): One of, Clock, Strobe, Data, Address, Power Supply, Analog High Speed, Analog Low Speed, Do Not</td></tr><tr><td>HyperLynx.Default ic.Model</td><td>Free Text</td><td>Analyze Lists the part model in the file used for BoardSim simulations. Values: Text (model name)</td></tr><tr><td>HyperLynx.Default iC.Model File</td><td>Free Text</td><td>Lists the part model file in the file used for BoardSim simulations. Values: Text (filename)</td></tr><tr><td>HyperLynx.Default IC.Model Pin</td><td>Free Text</td><td>Lists the specific pin for the model in the above attribute, if applicable. Used in BoardSim simulations.</td></tr><tr><td>PowerGround</td><td>Yes/No</td><td>Values: Text (pin name or number) Identifies nets as Ground and Power nets.</td></tr></table>  

Table 30. Listing of Default Attributes for Nets (continued)   


<table><tr><td>Attributes</td><td> Type</td><td>Description and Use</td></tr><tr><td></td><td></td><td>Values: Yes or No (case-insensitive)</td></tr><tr><td>Voltage</td><td>Measure</td><td>Describes the voltage of the net. Range: -100kV-100kV (-100,000-100,000V) Units: nV uV mV V kV (case-sensitive)</td></tr><tr><td>DFT.Nail Count Per Net</td><td>Number</td><td>Indicates the ID of the probe in the test fixture. Values: (integer) O-2000 (all exact limits are allowed; for example, both 0 and 2000 are acceptable)</td></tr></table>  

## Adding Power and Ground Connections  

When you connect a part to ground or power nets, the normal convention is to use a special symbol to represent the net. The ground symbol ties the connection to ground. The power symbol adds voltage to connections.  

**Procedure** 

1. Specify the connection as described in the Adding Connections topic.   
2. Right-click and click Ground or Power. The symbol attaches to the connection and follows the cursor movement. (Optional) You can rotate or mirror the symbol by choosing the appropriate command from the popup menu. You can also modify the symbol representation by right-clicking and clicking Alternate. Right-click and click Display PG Name to toggle the visibility of the net name for the power or ground symbol.   
3. Locate the cursor and double-click to end the connection or right-click and click Complete.   
4. You can create and store a number of ground symbols in the library, each with its own net name. To select the appropriate ground symbol, right-click and click Alternate. Three symbols are available with the standard library. You can modify these or add additional symbols. SailWind Logic assigns the net name associated with the ground symbol to the connection, (for example, GND, Chassis ground, Analog-ground, etc.).   
5. For each alternate power symbol, there is a different signal name: $+5V_{i}$ , $+24\vee$ , etc. To select the appropriate signal name, click Alternate while placing the symbol.  

!Tip  

As you view the power or ground alternates in the working window, you can locate in the status bar the net name to which you want to tie the connection.  

Connections Adding Power and Ground Connections  

**Related Topics**  

Adding Connections Using Alternate Symbols  

## Working With Floating Connections  

Floating Connections add another level of flexibility to designing your schematic. Enable Floating Connections and you can add a connection from a pin to a location where a part doesn't yet exist without requiring an off-page symbol. You can also begin a connection in empty space and connect it later. Unconnected nets are terminated with square markers.  

Enabling Floating Connections   
Disabling Floating Connections and Running the Connectivity Report   
Adding Floating Connections   
Editing Floating Connections   
Duplicating Floating Connections   
Creating Floating Connections When Deleting Objects   
Attaching Objects to Floating Connections   
Adding Off-Page References  

### Enabling Floating Connections  

You can enable floating connections in your design. This enables you to create connections that are unterminated at one or both ends.  

**Procedure** 

1. Click the Tools $>$ Options menu item, and then click the Design category. 2. In the Parameters area, select the Allow Floating Connections check box to enable Floating Connections in the design.  

### Disabling Floating Connections and Running the Connectivity Report  

You can disable floating connections in your design. Once you have finished creating a design with floating connections enabled, you can disable the floating connections and run a connectivity check on the design to assure that all connections have been properly terminated.  

**Procedure** 

1. Click the Tools $>$ Options menu item, and then click the Design category. 2. In the Parameters area, clear the Allow Floating Connections check box to disable Floating Connections in the design. If Floating Connections exist in the design, a warning message appears.  

!Note:  

Warning: Disabling Floating Connections does not remove them from the design. Disabling the preference only prevents additional Floating Connections from being cr Floating Connections are undesirable on a finished schematic. A floating end should either be connected to a pin or terminated on an off-page symbol. Run the Connections Report to find the locations of Floating Connections in your design.  

3. Click the File $>$ Report menu item.  

4. In the Reports dialog box, select the Connectivity check box.  

5. Click OK to create the report.  

!Tip  

Multiple Floating Connections are easily selected for deletion. In the Search and Select box of the Selection Toolbar, type "dangling" to select all the Floating Connections.  

### Adding Floating Connections  

With the Floating Connections preference enabled, you can leave a connection dangling in space for a later connection. You can also start a connection in space in anticipation of a later connection. New parts and connection stubs added automatically through an ECO Import will receive Unconnected Markers instead of off-page symbols. Net stubs added through an ECO Import to existing parts will continue to receive off-page symbols.  

Creating a Dangling Connection Creating a Floating Connection  

#### Creating a Dangling Connection  

A dangling connection is tied to a design object at only one end in anticipation of it being connected at the other end at some future point in the design process.  

**Procedure** 

1. Start a connection on a pin.   
2. Draw the connection.   
3. To end the connection in space, double-click. Alternatively, you can right-click and click End.  

#### Creating a Floating Connection  

A floating connection is not tied at either end. Use floating connections to add connections to your design as placeholders with the intent of completing the connections at some later time in the design process.  

**Procedure** 

1. To start a connection in space, double-click.   
2. Draw the connection.   
3. To end the connection in space, double-click. Alternatively, you can right-click and click End.  

### Editing Floating Connections  

You can add floating connections to your design and connect them at a later time. Once created, you can edit the floating connections in your design.  

• Use Move mode or Add Connection mode to continue a connection from the Unconnected Marker.  

### Duplicating Floating Connections  

With the Floating Connections preference enabled, you can duplicate segments of connections and paste them in space. You are not required to paste them where they will make a pin to pin connection.  

**Procedure** 

1. Select a segment(s) of a connection.   
2. Right-click and click Duplicate.   
3. Position the cursor in the paste location and click. See also Step and Repeat.  

### Creating Floating Connections When Deleting Objects  

With the Floating Connections preference enabled, connections attached to deleted parts are terminated with Unconnected Markers instead of off-page symbols. When a bus is deleted, nets connected to the bus are also terminated with Unconnected Markers instead of off-page symbols.  

### Attaching Objects to Floating Connections  

With the Floating Connections preference enabled, any component pins that touch a floating connection end will automatically connect. A pin that touches another component pin will automatically connect also. Move the components apart to make the connection visible.  

### Adding Off-Page References  

To connect two pins on separate sheets of the schematic, or at opposite ends of the same sheet, without a graphical connection, use an off-page reference with identical net names.  

**Procedure** 

1. Specify the connection as described in the Adding Connections topic.  

2. Right-click and click Off-page.  

The symbol attaches to the connection and follows the cursor movement.  

The default decal with the right pin is defined as a source pin; the alternate decal with the left pin is defined as a load pin. This pin type orientation plays a role when you create a hierarchical symbol of the sheet. All off-page sources are on the left of the hierarchical symbol outline, and all loads are on the right. You can place the default or right-click and click Alternate.  

(Optional) You can rotate or mirror the symbol by using the appropriate command.  

3. Locate the cursor and double-click to end the connection or right-click and click Complete  

4. Type the net name in the dialog box and click OK.  

The sheet number for the connecting symbol appears next to the off-page symbol if the “Show Offpage Sheet Numbers” option is selected in the Options Dialog Box, Design Category.  

## Editing Off-Page Symbol Sheet Numbers Per Line  

The displayed sheet number next to an off-page reference is set by default to enable 5 sheet numbers to be listed in a single text string, separated by commas. You can use Properties mode to edit the number of off-page symbol sheet numbers per line.  

For example, if set to one, and there are two sheets containing the same net, the sheets will be listed in two lines.  

**Procedure** 

1. Select the off-page reference text string.   
2. On the Schematic Editing toolbar, click the Properties button. This displays an information dialog box.   
3. Change the settings for sheet numbers per line.   
4. Click OK. See also Options Dialog Box, Design Category.  

## Changing a Connection  

Use Move to change a connection from one endpoint to another, without deleting the rest of the connection.  

**Procedure** 

1. Select the connection at any point on the segment entering or exiting the part, or where it enters another connection.   
2. Right-click and click Move. The connection follows the cursor movement.   
3. Right-click and click Angle to specify diagonal segments in the connection.   
4. Indicate corners as needed or right-click and click Add Corner. Right-click and clickDel Corner to back up to the previous corner if necessary.   
5. A connection cannot end in open space. Locate the cursor and double-click to end the connection or right-click and click Complete.   
6. To end a connection with a power, ground, or off-page reference symbol, right-click and click the appropriate symbol during the last step of this procedure.  

**Related Topics**  

Adding Connections Adding Power and Ground Connections Adding Off-Page References  

## Moving Connections  

When you move a part, existing part connections follow the part movement. After part repositioning, you might need to move connections to improve the flow.  

You can reposition a connection segment that is not a connection endpoint, or you can reconnect a segment endpoint. Refer to the Changing a Connection topic for information on disconnecting from a part or connection and reconnecting to another part or connection.  

**Related Topics**  

Working With Floating Connections  

## Splitting a Connection  

You can split a connection to create new corners or a 90-degree turn.  

Restrictions and Limitations  

You can not split segments which enter or exit a part.  

**Procedure** 

1. Select a segment, right-click and click Move.   
2. Right-click and click Split Segment. Move the cursor to define the segment length.   
3. Right-click and click Swap Corner to define the endpoint in the opposite direction.   
4. Indicate the endpoint of the new segment to complete the split.  

## Splitting Segments  

Split converts a line segment into two separate segments, joined by a third segment perpendicular to the original segment.  

All line segments in a 2D line must have the same line width and style. If you need to create a 2D element with more than one line width or style, create two separate 2D lines and use the Combine command to join them.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Modify 2D Line button. 2. Select the line to split. 3. Right-click and click Split. The new and divided segments follow the cursor movement. You can right-click and click one of the following when splitting a segment:  

Table 31. Splitting Segments Options   


<table><tr><td>Option</td><td>Description</td></tr><tr><td>Swap Corner</td><td>Selects the other corner or line segment created by the split.</td></tr><tr><td>Del Corner</td><td>Deletes the current corner.</td></tr><tr><td>Width</td><td>Changes the line width of the item.</td></tr><tr><td>Solid Style and Dotted Style</td><td>Changes the line style to a solid or a dashed line. You cannot specify dotted lines for circles or arcs.</td></tr><tr><td>Orthogonal</td><td>Moves are made in 90-degree increments.</td></tr><tr><td>Diagonal</td><td>Moves are made in 45-degree increments.</td></tr><tr><td>Any Angle</td><td>Moves are made at any angle.</td></tr></table>  

4. Indicate the endpoint of the new segment to complete the split.  

## Swapping Pins  

To swap two part pins, you can use the Swap Pins button in the Schematic Editing toolbar or Swap Pins on the popup menu. SailWind Logic swaps the pin number, name, and terminal of the pins you select. You can also swap pins when you place a part using Mirror X and Mirror Y on the popup menu. This is often useful for improving the flow of the schematic.  

Swapping Pins Using the Swap Pins Button in Verb Mode Swapping Pins by Selecting One Pin at a Time Swapping Pins by Selecting Both Pins First  

### Swapping Pins Using the Swap Pins Button in Verb Mode  

You can swap pins using the Swap Pins button. Using this method enables you to initiate the command and then make your pin selections to swap. You can continue to select pin pairs to swap until you cancel the command.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Swap Pins button.   
2. Select the first pin number.   
3. Select the pin number to swap with the first selected pin.   
4. If the pin types you select do not match, the message “Warning, pin swap types don't match…”   
   message appears. Click Yes to continue. Click No to cancel the swap.  

![](/images/fa23a7f30c30d6f1dd5b2dbdcdf1e15c91f23352f159b32885ebc79e015c7d08.jpg)  

!Tip  

The message “Keep connections tied to same electrical pin?” may also appear. Click Yes to preserve the connections with the pin numbers. Click No to reconnect to the renumbered pins.  

To use the popup menu to swap pins, you can either select one pin at a time or select both pins at once:  

### Swapping Pins by Selecting One Pin at a Time  

You can swap pins by selecting one pin at a time. This method enables you to select the first pin, initiate the command and then select the second pin. To create another pin swap, you would repeat the process.  

**Procedure** 

1. Select the first pin number.   
2. Right-click and click Swap Pins.   
3. Select another pin number to complete the swap.  

4. If the pin types you select do not match, the message “Warning, pin swap types don't match…” message appears. Click Yes to continue. Click No to cancel the swap.  

![](/images/eb832081f6b1e7b82309cd2e03ebd83206984239371215e79db5e3f681301d59.jpg)  

!Tip  

The message “Keep connections tied to same electrical pin?” may also appear. Click Yes to preserve the connections with the pin numbers. Click No to reconnect to the renumbered pins.  

### Swapping Pins by Selecting Both Pins First  

You can swap pins by selecting both pins first. After you have selected both pins, you can initiate the command. To create another pin swap, you would repeat the process.  

**Procedure** 

1. Using Ctrl+click, select the pins you want to swap.   
2. Right-click and click Swap Pins. If the message “Swap connected pin?” appears, click Yes to continue. Click No to cancel the swap.   
3. If the pin types you select do not match, the message “Warning, pin swap types don't match…” message appears. Click Yes to continue. Click No to cancel the swap.  

!Tip  

The message “Keep connections tied to same electrical pin?” may also appear. Click Yes to preserve the connections with the pin numbers. Click No to reconnect to the renumbered pins.  

## Managing Buses  

SailWind Logic enables you to create, name, edit, and delete buses in your design using a flexible array of available commands. Using the bus commands enables you to decrease the visual clutter in your design and accurately convey you design intent without having to graphically represent every net as a distinct line.  

Choosing the Bus Type   
Naming Buses   
Adding Buses   
Adding Connections to Buses   
Adding Nets to a Mixed Net Bus   
Extending Buses   
Moving Bus Segments   
Splitting Buses   
Deleting Bus Segments   
Deleting Buses  

### Choosing the Bus Type  

There are two bus types: a bit format bus and a mixed bus. Choose the bus structure that can best visualize your design intent. The bit format bus will display sequential bus nets. The Mixed bus format will enable you to combine sequentially named bit format bus nets along with individual nets.  

A bit format bus contains a series of nets with consecutive net names. For example, the bit format bus AD[0:4] contains nets AD0, AD1, AD2, AD3, and AD4.  

A mixed net bus can contain one or more bit format buses in addition to individual nets that are not necessarily sequential. For example, a mixed net bus BUS1 can contain individual nets named RAS, CAS, and EN as well as the bit format bus AD[0:7].  

0 Tip The Bus Type you select determines which options appear in the Bus Name list. For example, if you select the Bit Format Bus Type, only bit format bus names appear in the Bus Name list.  

### Naming Buses  

SailWind Logic defines a bus that appears on the same sheet, or any other sheet, with an identical name as the same bus.  

Rules for naming bit format and mixed net buses differ as follows:  

### Naming a Bit Format Bus  

The bit format bus name consists of two parts: the prefix and the bit range of the bus. The format is PREFIX[nn:mm] where nn is the lowest bit number and mm is the highest bit number. You can use leading zeros to determine the lowest bit number. For example DD[00:15] enables nets DD00, DD01,...DD15 to connect to the bus; whereas DD[0:15] enables nets DD0, DD1, DD2,...DD15.  

The sheet number also displays with the bus name if the Show Off-Page Reference option is on the Options Dialog Box, Design Category.  

The total bit format bus name - including the prefix, brackets and colon - cannot exceed 47 characters.   
The bit numbers must be in the range of 0 to 32767 and cannot contain alphabetic characters.  

Naming a Mixed Net Bus  

The mixed net bus name can contain up to 47 alphanumeric characters. The mixed format bus name cannot include a bit range suffix or spaces. You cannot create a bus name that is the same as a net name.  

### Adding Buses  

You can add a bus to your design so that you can display a collection of related nets as a single entity.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Add Bus button.   
2. Indicate the starting point. The bus follows the pointer movement.   
3. Indicate bus corners as needed, or right-click and click Add Corner. If you need to back up to the previous corner, right-click and click Del Corner.   
4. Double-click to end the bus in open space or right-click and click Complete.   
5. In the Add Bus dialog box, in the Bus Name box, type a new name for the bus, or select name from the list.  

Restriction: The Rename area is available only in Query mode  

6. Select the Bus Type. The bus type determines which bus names appear in the Bus Name list.  

7. Select the Add Bus Name Label check box to add the bus name as a label to the bus at the end of the bus closest to where you selected it.  

![](/images/f08c90957e01a8eb4b13c25a427db963af4cbad281887474d62906c0ff3ffa6f.jpg)  

!Tip  

When working with bus labels, observe the following:  

• A bus can have two labels, one on each end.   
• The check box is unavailable when the end of the selected bus has a label.   
• A bus label is not required.   
• To delete a bus label, select the label in the schematic and click the Delete button on the standard toolbar.  

8. If the bus is a mixed net bus, add the bus names in the Bus Nets area.  

![](/images/ede2f892169d38ed6bf8da31530106c6690515074b93920d2ebf4a0d56d796ea.jpg)  

Tip   
To rotate the text before you place it, right-click and click Rotate, then indicate the name   
location  

### Adding Connections to Buses  

When connecting to a bus, the connection must be perpendicular to the bus. SailWind Logic adds an angled bus-tap segment at the point of connection and gives the connection the next sequential net name in the bus.  

Confirm or type the net name in the dialog box. The text follows the cursor movement. Position the text and indicate its location. To swap the bus tap angle, right-click and click Swap Angle.  

### Adding Nets to a Mixed Net Bus  

Use the Bus Nets list in the Add Bus dialog box or the Bus Properties dialog box to add nets to a mixed net bus. The Bus Nets area is not available when the Bit Format bus type is selected.  

**Procedure** 

1. After you have added a bus, in the Add Bus dialog box, click Add to add a new row in the Bus Nets list.   
2. Type the bus prefix in the Name/Prefix text box.  

!Tip  

Enter the names as follows:  

• For a single net, type the net name.   
• For a range of sequential nets, type the prefix for the sequence of nets.  

3. In the Start text box, type the starting bit number for a sequence of nets.  

4. In the End text box, type the ending bit number for a sequence of nets.  

5. To add an individual net to the bus, type the net name in the Prefix/Name text box. Do not type Start and End values for a single net that is not sequenced by bit number.  

6. Click Edit to modify a selected cell in the Bus Nets list.  

7. Click Delete to remove a net from the Bus nets list.  

8. Click Down to moves the selected row down one position in the Bus Nets list.  

!Tip  

The order in which nets appear in the Bus Nets list box determines the default order for naming nets as they are connected to a bus.  

9. Click Up to move the selected row up one position in the Bus Nets list.  

### Extending Buses  

If you need more room to fan out bus connections, or need to lengthen the path of an existing bus, you can extend a bus segment.  

**Procedure** 

1. On the Schematic Editing toolbar, click the Extend Bus button.   
2. Select either endpoint of the bus. The end segment follows the pointer movement.   
3. Click to indicate corners as needed for the extension or right-click and click Add Corner.   
4. Double-click to indicate the new endpoint or right-click and click Complete.   
5. You cannot use the Extend Bus command to shorten a bus segment. To shorten a bus, delete the long segment, then use Extend Bus to redefine that segment, or alternately, you could use the Group command to shorten the bus segment. See also Creation of Groups.  

### Moving Bus Segments  

If you need to reposition a bus segment to accommodate additional edits to your schematic, you can move a bus segment.  

**Procedure** 

1. Select a bus segment, right-click and click Move.   
2. Indicate the new location with the pointer and then click to place.  

### Splitting Buses  

If you need to edit a bus, you can create new corners or a 90-degree turn in the bus.  

**Procedure** 

1. Click the Split Bus button.   
2. Select the bus segment. The new and divided segments follow the pointer movement.   
3. Move the pointer to define the segment length. To define the endpoint in the opposite direction,   
   right-click and click Swap Corner.   
4. Indicate the endpoint of the new segment and click to complete the split.  

### Deleting Bus Segments  

As your design progresses, if you determine that you no longer need a bus segment, you can remove a segment of the bus.  

**Procedure** 

1. Select the bus segment.   
2. Right-click and click Delete.  

If the deletion splits the bus into two separate buses, the bus name appears, identifying any unnamed bus segments. Each bus retains the same properties.  

### Deleting Buses  

If you determine that you need to delete a bus that was selected in object mode, you can choose to delete the bus only or the bus and its connections.  

See also Object Select Mode (Select Object First).  

Delete a Bus Only Delete a Bus and Its Connections  

#### Delete a Bus Only  

If you need to delete a bus, you have the option to delete a bus only and leave the connections intact.  

**Procedure** 

1. Select a bus.   
2. If you want to keep connections attached to the bus, right-click and click Preserve Connections to enable it.  

Preserve Connections is enabled by default.  

Tip Preserve Connections is enabled when a check mark appears next to it in the menu.  

3. Right-click and click Delete.  

Connections are left at their original locations.  

#### Delete a Bus and Its Connections  

If you need to delete a bus, you have the option to delete a bus and its connections.  

**Procedure** 

1. Select a bus.   
2. If you want to remove connections attached to the bus, right-click and click Preserve Connections to disable it.  

Preserve Connections is enabled by default.  

Tip   
Preserve Connections is disabled when a check mark does not appear next to it in the menu.  

3. Right-click and click Delete.  

The bus and connections are deleted.  

## Deleting Connections  

You can delete connections, but be aware that when the deleted connections are subnets, the results can differ.  

• Select a connection, right-click and click Delete.   
• When a subnet with a system assigned name is split into two subnets by deleting a connection, one of the subnets is automatically assigned a new system name.   
• When a subnet with a user assigned name is split into two subnets by deleting a connection, both new subnets retain the user assigned name, even if there is no visible net name label.   
• When subnets are joined and both have user assigned names, the user is prompted to select one of the names for the combined net, even if there are no visible net name labels.   
• When a system named subnet is joined with a user named subnet, the combined subnet automatically inherits the user assigned name.   
• When two system named subnets are joined, the combined subnet inherits the name of one of the subnets.  

**Related Topics**  

Splitting a Connection  

## Detach  

Use the detach command to free a gate, part, group of components, or group selection from any attached nets.  

**Procedure** 

1. Make a selection.   
2. Right-click and click Detach.  

All nets are detached. Nets are given unconnected markers or off-page symbols, depending on the Floating Connections preference.  

!Note:  

Warning: A group selection with Preserve by Boundary enabled detaches nets at the boundary and not at net terminations. The Net is split into two instances. Named nets retain their original names on both sides of the split.  

**Related Topics**  

Working With Floating Connections Creation of Groups  

