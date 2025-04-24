# Glossary

## absolute coordinates  

Coordinates of a location based upon their distance from the origin (coordinates 0,0) of the design area.  

## accelerator keys  

Key sequences used to invoke commands and change system settings without using the mouse.   
Accelerator keys are called shortcut keys in the SailWind product documentation.  

## accessible nets  

Nets for which you can define test points. DFT Audit analyzes all nets. If DFT Audit determines that test probes can access them, the nets are accessible (also called adaptable).  

## accordion  

A trace pattern resembling a signal wave that adds length to traces. The trace patterns are contiguous and do not include layer changes.  

![](/images/81c105ac58c1d23d322bccb06d8b12eed851ceadd999063388109a90a8c2e002.jpg)  

## accordion gap  

The gap of an accordion sets the pitch between chords. The gap is a user-definable number multiplied by the same net trace-to-corner clearance.  

If the same-net trace-to-corner distance equals zero, then Trace Width is used for the gap calculation.  

![](/images/c43704d88fb1b6f4db9074ba8c8d8346a4b00c89285c662077fd5dabcbb69497.jpg)  

See also accordion, amplitude, pair routing gap  

## acid trap  

An acid trap is a location where acid gets trapped in an area due to the surface tension of the etching. This acid causes over-etching, which hurts yield.  

## active component  

The active substituted component in an assembly variant. Active means that this substitution of the component is used in the current variant.  

See also default.asc  

## active layer  

The design layer to which new information is added. You select the active layer by choosing the layer in the Layer list on the Standard Toolbar. You can also do this by using the L modeless command.  

## ACTM##  

The 16-digit number found on your security key.  

## adaptable nets  

See accessible nets  

## adhesive  

A substance used to attach the bodies of devices to a PC board.  

## aggressor nets  

When using the Electrodynamic Checking program (EDC), a net or pin pair that is considered a source of interference.  

## align  

To reposition placed parts to match the alignment of another part.  

## alignment tool  

A small, temporary marker at each location where dimensioning occurs.  

## alpha pins  

Pins with descriptive letters that are substituted for pin numbers. For example, GND for the ground pin. Alphanumeric pin assignments are made in the Library Manager's part type editor.  

## alphanumeric pins  

Pins with alphanumeric pin numbers. An alphanumeric name consists of a prefix and suffix. The prefix or the suffix can contain either alpha letters or numeric numbers. For example, A1, 1A, or even DATA07 (consists of the prefix “DATA” and the suffix “07”).  

## amplitude  

The amplitude of an accordion sets the accordion height (for horizontal accordions) or accordion width (for vertical accordions). The amplitude is a user-definable number, multiplied by the same net trace-to-corner clearance.  

If the same-net trace-to-corner distance equals zero, then Trace Width is used for the amplitude calculation.  

![](/images/511a1428988dcbfacc3c2eca19bc7fbcf1b35767fdfaa96840f8280c97ba0d8d.jpg)  
SNTC $\mathbf{\tau}=\mathbf{\tau}$ same net to trace corner  

See also accordion, gap (accordion)  

## analog board  

A board with mostly discrete components and minimal integrated circuits.  

## analog circuit  

A design composed of discrete components such as capacitors, resistors, and diodes.  

## angstrom  

1/10,000 of a micrometer (10-4um).  

## annotation (forward and backward)  

Forward annotation refers to the process of updating the design file to match the schematic file.   
Backward annotation refers to updating the schematic file to match the design file.  

## annular pad  

A pad shape that enables you to specify an inside and an outside diameter. This creates a donut shape because the inner hole was used to center the drill bit when boards were hand-drilled on a drill press. Though obsolete, the annular pad is still offered for special circumstances.  

## annular ring  

The conductive pad material surrounding the hole. The annular ring radius $\mathbf{\tau}=\mathbf{\tau}$ pad diameter-(finished hole size) / 2.  

## antipad  

For plane layers, a slightly oversized pad diameter that plots as a clearance for through-hole pins that should not connect to the plane.  

## any-angle coupling trace  

Part of a route that connects SBP fanouts to serpentine routes.  

## aperture  

A uniquely shaped window or hole that is attached to an aperture wheel on a photoplotting machine.  

## aperture table  

A table that matches the line widths necessary to print your design with the plotter setup. SailWind Layout can prepare the table automatically, or you can prepare it manually.  

Artwork for printed circuit manufacturing is created by exposing clear film to light that is passed though the aperture. Although the aperture wheel has been made obsolete by laser plotters, an aperture table is still necessary to drive laser plotters.  

## apl.dcr  

A setup file for Novell network security.  

## application-specific integrated circuit  

An IC designed to meet a specific customer requirement.  

## area select  

A method for selecting an object or a group of objects. If you enable area select by clicking Filter on the Edit menu, a selection rectangle is created and all items within the rectangle are selected.  

## array  

A group of items, such as bonding pads, that are arranged in rows and columns.  

## artwork  

Clear film with darkened areas representing pads and connecting traces, and used for manufacturing a printed circuit board. Each layer of a design has its own unique artwork, such as silkscreen and solder mask.  

## .asc  

The file extension used to identify a proprietary PADS-format ASCII file.  

## ASCII format  

A translation format that uses ASCII text to define the PCB design. ASCII format is widely used to list the parts and connections in a design, to import and export design items, and to check the design for binary corruption.  

## ASIC  

An acronym for application-specific integrated circuit.  

## assembly drawing  

A final design document that provides the part name, type, and orientation for each device on a printed circuit board. An assembly drawing is used for assembly of the final product.  

## assembly variant  

A specific manufacturing configuration of a PCB. Assembly variants specify which components are used, which are not used, and which are substituted with a different decal part type. Several assembly variants can exist for a single PCB.  

## associated net  

See electrical net.  

## associating component  

A component through which an electrical net passes.  

## associating copper  

Copper combined with the terminals in the PCB Decal Editor.  

## attribute groups  

A group of structured attributes. For example, the DFT group includes the following attributes:  

DFT.Nail Count Per Net DFT.Nail Number DFT.Nail Diameter  

## attributes  

Attributes contain information you have associated with an object in your design. Attributes contain the types of part information that can be included in the parts library description and exported to a parts list. Examples are part manufacturer, package type, order number, and so on.  

## Auto Dimensioning tab  

The tab on the Options dialog box that determines the appearance of newly created dimensions.  

## automation  

A way for heterogeneous applications to communicate with each other. SailWind products make some data, such as the database in use, and some functionality, such as opening files or selecting objects, available to other applications.  

## autorouter pass types  

Pass types are part of an autorouting strategy that determines how the autorouter routes a design.  

|  Pass    | Description                                                                                                                                                       |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Center   | Places traces equidistant from component pins or vias and each other to evenly distribute any available space in the channel.                                     |
| Fanout   | Places vias for inaccessible SMD component pins and routes from the vias to the pins.                                                                             |
| Miters   | Converts all route corners of a specified angle to diagonal corners.                                                                                              |
| Optimize | Analyzes each trace and tries to improve the quality of the route pattern by removing extra segments, reducing via usage, and shortening trace lengths.           |
| Patterns | Searches for groups of unrouted connections that can be completed using typical C routing patterns, Z routing patterns, and memory patterns and then routes them. |
| Route    | Sequentially routes each unroute until all connections are attempted.                                                                                             |

Glossary axial lead   


| Pass       | Description                                                                                                                                                                       |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Test Point | Analyzes the testability of the design, determines which nets require testing, adjusts the routes, and inserts test points to improve testability.                                |
| Tune       | Adjusts the length of length-controlled traces. The Tune pass tunes all routed traces with length rules, and automatically adjusts length-controlled traces to meet design rules. |

## axial lead  

A connection pin that protrudes straight out from the component body and bends at 90 degrees for insertion into the PC board. An axial lead is usually associated with discrete components such as resistors, capacitors, or diodes.  

## back-annotate  

Update a schematic file to match its design file.  

## ball bonding  

A bonding technique that provides increased contact between a gold wire and a chip bond pad. This method uses thermal compression to melt gold wire to form a ball.  

## ball grid array  

A packaging method that uses a substrate to interconnect one or more die to an array of solder alloy spheres.  

## base option  

The Base Option, in Assembly Variants, contains all of the common components in all of the existing  variants; in other words, it contains a filtered database. If you uninstall or substitute components in a variant, they are removed from the Base Option. Therefore, the Base Option, because it contains only installed options, is also a subset of the raw database. You can use the Base Option to view all of the items in all of the variants, or the base of all variants.  

The Base Option always exists; you cannot delete it.  

## base part  

When making a union, the part type of the first selected part. Base parts can either be left in position and joined by secondary parts, or repositioned to imitate the first selected prototype part.  

## baseline dimensioning  

A type of dimensioning in which a series of dimensions have a common start point, such as datum dimensioning.  

## basic units  

A basic unit is the smallest unit of measurement in a SailWind database. All values in the database are stored in binary format basic unit and are converted to the current user units (mils, mm, or inches) for screen display. If you need to re-import the information to .pcb format, export in basic units.  

Conversions are:  

• $1\mathrm{mil}=38100$ basic units • 1 millimeter $\mathbf{\tau}=\mathbf{\tau}$ 1500000 basic units  

## BGA  

An acronym for ball grid array.  

## BGA fanout  

A single-segment fanout that connects BGA array pads to BGA vias. This single-segment fanout always ends in a via.  

## BGA/PGA decals  

A full matrix decal for BGAs and PGAs, including staggered array patterns.  

## biased pin pair  

A layer biased pin pair is any pin pair with a design rule specifying a layer bias to one or more, but not all, electrical routing layers.  

## blind via  

A via that connects an outer layer to one or more inner layers, without passing through all other layers of a printed circuit board.  

## bmp  

An image file that can be pasted into documents or other programs such as Microsoft Word.   
SailWind products use the Copy Bitmap command to capture these as screen images.  

## board markings  

Designers usually include identification information on a board. These may include the board part number, the assembly part number, the company name, the product name, the revision level, the serial number, the copyright notice, an anti-static symbol, warning messages, UL labels, test labels and many other types of information. This information may be in ink on the silkscreen layers, in copper on the top and/or bottom layer or some combination of the two. These are typically referred to as board markings.  

Add text to an electrical layer and it will be created in copper. Add text to a Fabrication, Assembly, and Documentation Layer and it will be created during the silkscreen process.  

Use the Text command to add board markings to your design.  

See also Adding Free Text  

## board outline  

The actual shape of the printed circuit board, defined by line segments and arcs. The board outline is entered on layer 0 and displayed on all layers.  

## bonding pads  

Metallization areas placed around the perimeter of the integrated circuit die, to which aluminum or gold wires connect the die to the component package.  

## bounding rectangle  

The smallest rectangle that encloses all nontext graphics on all layers.  

## breakpoint marker  

A small brown dot in the Output window gutter that indicates a breakpoint in a script or macro.  

## bumped chip  

A die or chip that has been specifically processed with buffer metals over the I/O pads, followed by an addition of solder or gold bumps to provide bonding areas for direct chip attachment onto a substrate.  

## buried via  

A via that connects only inner layers.  

## bus  

A series of connections that share a common use, such as memory array or data array, and are usually routed parallel to each other.  

## bus routing  

Routing two or more pin pairs simultaneously and in close proximity to each other in neat, flowing patterns.  

## C routing pattern  

A collection of routes that form a pattern resembling the letter C.  

![](/images/6f116c08cc263b6f43d2aa1d77ef0006381d89c3a91bd246c950b03506dfd296.jpg)  

## CAD  

An acronym for Computer-Aided Design or Computer-Aided Drafting.  

## CAE  

An acronym for Computer-Aided Engineering.  

## CAE Decal  

The graphical representation of schematic symbols in SailWind products.  

## CAM  

An acronym for Computer-Aided Manufacturing.  

## CAM document  

A combination of plot type and output device you create and save with the design. For example, you can include "Silkscreen Top, Photoplot" and "Silkscreen Top, Laser Printer" on your CAM Documents List and run them selectively when needed.  

## CAMDir  

The SailWindpcb.ini file entry that enables you to specify the CAM master folder for creating CAM output.  

## capacitance  

The ratio of charge within a trace that is a factor of the trace length and signal delay.  

## CBGA  

An acronym for ceramic ball grid array.  

## CBP  

An acronym for chip bond pad.  

## center pass  

An autorouting pass that places traces equidistant from component pins or vias and each other to evenly distribute any available space in the channel.  

## CGA  

An acronym for column grid array.  

## chamfered  

A rectangle with the square corners cut off to create beveled edges on the corners.  

## chamfered path  

A solid filled copper that, like a trace, acts as a conductor connecting pins and vias similar to a trace. But unlike a trace, which is created with a round aperture producing rounded outside corners, chamfered path copper allows for sharp specific outlines with a filled interior. When creating a chamfered path, you set options to create shapes with square or chamfered corners. The copper created by chamfered path has a Solid Copper property which overrides the Copper Hatch Grid and Drafting Line Width settings to make it a solid fill. Clearance rules for the chamfered path copper are also changed to match the clearance rules of a trace.  

## checking  

Verifying the design meets previously defined rules, such as clearance and connectivity.  

## chip  

An integrated circuit without packaging. A chip is also called a die.  

## chip bond pad  

Interconnect areas on the die on which wire bonds are connected to the substrate.  

## chip carrier  

A square or rectangular IC package, with $1/\mathsf{O}$ connections on four sides.  

## chip on board  

The packaging configuration in which a chip is bonded directly to a circuit board or substrate.  

## Chip Scale Package  

A packaging configuration in which the dimension of the substrate is 1.2 times larger than the die. chord  

Half of an accordion.  

![](/images/89c52cb7defa3d0724d89cf05804cc315423f0ba1c2ad3b1e53a8c67cf883c5f.jpg)  

See also accordion,amplitude, gap (accordion)  

## clam shell fixing  

A test fixture that tests both the top and bottom side of the PCB.  

## class  

A collection of nets with a common set of design rules.  

## clearance  

The measured space between routed objects such as trace-to-trace, trace-to-pad, or pad-to-pad.  

## closed cluster  

Clusters that you cannot delete or replace during automatic cluster creation.  

## cluster  

In Cluster Placement, a group of parts that must be placed close to each other.  

## CMOS  

An acronym for Complementary Metal Oxide Semiconductor.  

## COB  

An acronym for Chip On Board.  

## coefficient of thermal expansion  

A quantity used to determine the length change of a material due to temperature change. Thermal expansion differences between the die and substrate must be considered for quality assurance.  

## collapse  

To relocate the members of a cluster from their current placement to the center of the cluster.  

## column grid array  

Similar to a ball grid array, but columns are used to improve the stresses of different thermal expansion between the board and the component.  

## Com port  

Abbreviation for communications port. This port provides a connection between your computer and peripheral devices, such as plotters, modems, and other computers.  

## combine  

Joining lines, or lines and text, together as one selectable object.  

## component side  

The top or front side of a printed circuit board where devices are normally mounted.  

## composite fanout  

A fanout from a pin that is common to two subnets. Often created by autorouting operations.  

Composite fanouts provide access to component pins that may otherwise be inaccessible.  

See also fanout, subnets  

## composite rule trace  

A trace that is attached to a pin (typically an SMD) shared by two subnets. This type of trace is typically created by autorouting operations.  

See also composite fanout, subnets  

## conditional rules  

Rules placed on a signal that apply only if the signal is routed near another specified signal.   
Conditional rules are also known as against rules.  

## conductor  

A material that causes heat or electrical current flow. For printed circuit design, a conductor is a piece of metal that connects pins of components together.  

## connected islands  

A maximum set of subnet items already connected by a trace, copper unroute, or jumper.  

See also subnets, subnet  

## connections  

Points of connectivity, such as a pin pair or a net.  

## connector  

A unique component used to connect a portion of a printed circuit board with other devices.  

## Constraint Manager  

The Constraint Manager is a separate application used to input rules for SailWind Layout instead of the rules dialogs within the SailWind Layout application. The Constraint Manager is only used in the integrated SailWind Designer project.  

## container application  

An application that can incorporate embedded or linked items into its own documents. The documents managed by a container application must be able to store and display both OLE components, and data created by the application itself. A container application must also allow users to insert new items or edit existing items.  

When you insert objects into a SailWind product, the SailWind product is the container application. When you insert a SailWind file into another application, the other application is the container application.  

## controlled gap area  

The part of the differential pair where the traces are drawn routed in parallel and separated by the pair routing gap. The controlled gap zone area starts at the gathering point and ends at the split point.  

![](/images/a2cdb3780f7a431830645d030f7ca6199540f75e41444d973515507aba2c91f3.jpg)  

See also gathering point, pair routing gap, split point  

## controlled gap length  

For a differential pair, the ratio of the controlled gap area routing length to the overall routing length, in percentage.  

See also differential pairs  

## controlled length net  

A net that has length rules, or contains pin pairs that have length rules.  

The following high-speed rules are net length rules:  

• Minimum/maximum length Matched length Differential pairs  

## converting database  

The process that converts a non-native file, such as an .asc file or a .dxf file, to a SailWind native format, or .pcb, file.  

## copper connectivity  

Means unroutes are always connected to a copper at some point in the copper outline. A copper outline can include arcs. The following graphic illustrates how copper connects to a net.  

![](/images/4070f66710bbda595d0f5f6a0dc2ce80aa44fb243f2cc9389ea051c7a502ff25.jpg)  

See also coppers, overlapping coppers  

## copper plane  

A copper shape with insulation areas around traces and pins that pass through the copper, but are not attached or connected to the copper. Can be placed on any layer, except CAM plane layers.  

## coppers  

Polygons on an electrical layer representing an area of the PCB to fill with metal.  

When a copper is assigned to a net, it is joined to the net with a trace or via. Coppers are obstacles to net objects unless the copper and the net belong to the same net.  

See also overlapping coppers, copper connectivity  

## copy route  

The duplication of a trace or series of traces, using copy and paste.  

## corner  

Point where a trace or line changes direction. The Selection Filter enables or disables picking geometric or route corners.  

## cost  

Reduces usage of a layer. The higher the cost, the less a layer is used for routing.  

## cross-probing  

Uses a link between SailWind programs to reflect, in one SailWind application, selections made in another SailWind application.  

## CSP  

An acronym for chip scale package.  

## CTE  

An acronym for coefficient of thermal expansion. It is also referred to as TCE.  

## cutouts  

A closed polygon in a copper, copper plane, or board outline. In copper or copper planes, a cutout results in an area absent of copper.  

See also overlapping cutouts  

## cycle picking  

To sequentially select objects in the vicinity of the selection point using the Tab key.  

## dangling route  

Dangling routes are stubs or spurs off of traces that are not tied to any pin by a ratsnest. See also partial route.  

## database units  

The use of mils, metric, or inches within a design.  

## datum dimensioning  

A style of dimensioning in which all dimensions are measured from a common starting point. The origin extension line is marked as zero, with each dimension reflecting the measurement from that point.  

See also Creating Baseline Dimensions  

## D-codes  

Specific numbers assigned to photoplot machine apertures for program identification. D-CODES are included in the aperture table.  

## decal  

The physical representation, or footprint, of a part.  

## decal copper  

Open, closed, or associated copper produced within the physical representation of a component.  

## decal text  

Documentation text produced within the physical representation of a component.  

## default component  

The original component, before being replaced in the current assembly variant. The default component is always in the raw database, but not necessarily in the Base Option.  

See also active component  

## default layer mode  

A layer mode in which a design can consist of up to 30 electrical layers, or a combination of electrical and nonelectrical layers. You change from default layer mode to increased layer mode by clicking the Max Layers button in the Layers Setup dialog box.  

## default.asc  

The ASCII file accessed for new file creation. This file provides startup design information such as grid sizes, default colors, or other information.  

## defaults  

Conditions or options that are set when the SailWind product starts.  

## delay  

The time it takes for a signal to travel through a trace.  

## delete  

To remove information from a design.  

## design area  

The actual work area where a design is created.  

## design on the fly  

To use ECO Operations to create a new design without first providing a netlist or parts list from schematic software. This can also be called design.  

## Design category  

The Options category that controls design conditions, general routing conditions, and certain display and part movement method settings.  

## design rules  

Established spacing and general routing constraints for electrical properties, or conductors, which are verified by clicking Verify Design from the Tools menu.  

## devicesn.dat  

A file usually found in the C:\<install_folder>\<version>\Programs folder that contains CAM printer and plotter driver data. This file must exist in the same folder specified by the UserDir SailWindpcb.ini variable.  

## DFM  

An acronym for Design for Manufacturing.  

## DFT Audit  

DFT Audit analyzes every net for accessibility (adaptability) and creates a board report that identifies all inaccessible (non-adaptable) nets.  

## dice  

The plural of die.  

## die  

A single square or rectangular piece of semiconductor material into which a specific electrical circuit has been fabricated.  

## die bonding  

To attach the semiconductor die to the package substrate with epoxy adhesives, gold eutectic, or solder alloy. It is also referred to as Die Attachment.  

## die flag  

Metal shapes placed under a die for thermal management and/or electrical connection; also referred to as a flower pattern.  

## die side of CBP  

The side of the die on which the CBP lies. Usually the die side of the CBP is the same as its fanout side, but in some cases more complex patterns of wire bond fanout may mean that the two sides are not the same.  

## Die Wizard  

This feature creates die part definitions parametrically or imports the die description using GDSII or formatted ASCII files. The Die Wizard replaces Component IQ by providing die capture directly in the Advanced Packaging Toolkit layout editor. This eliminates the need to transfer .ciq files.  

## dielectric  

A non-conductor of current; an insulator.  

## dielectric constant  

A value given for manufacturing materials, such as FR-4, to describe electrical characteristics.  

## differential pairs  

A group of two nets or two pin pairs routed side-by-side and separated by the pair routing gap for as much of the overall length as practical. A differential pair typically transmits two electrical signals that are driven 180 degrees out of phase from each other.  

See also pair routing gap  

## digital board  

A board with mostly integrated circuits in proportion to the analog components.  

## DIP  

An acronym for Dual In-line Package.  

## DisableCaching  

A SailWindpcb.ini file entry that, when set at 1, shuts off graphics optimization and, when set at 0, enables graphics optimization.  

## discrete device  

A device that contains one circuit element. For example, a resistor or toggle switch.  

## disperse  

A command that is active on several levels of Cluster Placement. When selected, it clears the board of all parts or clusters that are not glued down, and arranges them around the outside of the board outline according to decal type.  

## dispersion routes  

Partial routes, ending in vias, which tie surface mount components to plane layers.  

## do file  

The SPECCTRA router ASCII setup file that contains user-defined router commands to initiate batch routing.  

## dock  

To take an isolated application dataset and pull the changes within the dataset into the main design project. Any conflicts with the merged data must be manually resolved.  

## documentation layers  

Layers higher than the electrical layers in a SailWind Layout database that contain text and lines to illustrate assembly, annotation, and provide instructions for manufacturing.  

## double-click  

Two mouse clicks, in immediate succession, that usually initiate an edit action or complete the current action.  

## double-sided board  

A printed circuit board made up of two routing layers, and which has no internal layers.  

## double-sided die  

A die that has substrate bond pads on one side, and a BGA grid array on the other side. The two sides are connected through vias.  

See also single-sided die  

## drafting operations  

Any operation that involves adding nonelectrical information, not associated with placement or routing, to a design.  

## drawn pads  

Photoplot pads, usually finger pads, that are produced by opening the aperture and moving the board, with the aperture remaining open, to produce a pad shape.  

## DRC  

An acronym for Design Rules Check.  

## drill chart  

A diagram, produced on a drill drawing, that shows drill symbols matched with drill hole sizes. This is also referred to as a drill legend.  

## drill oversize  

A factor applied to plated through holes for DRC purposes to account for drill oversizing during the PCB fabrication process.  

## drill pairs  

Primarily for buried and blind vias, drill pairs define which layers are to be drilled and plated together during the fabrication process.  

## drill symbols  

Unique symbols on a drill drawing plot that represent the various drill hole locations and sizes.  

## drill.dat  

A user-definable ASCII file that determines settings for NC Drill output format options. This file must exist in the same folder specified by the UserDir variable in the SailWindpcb.ini.  

## DXF  

An acronym for Data eXchange Format, a standard ASCII format for sharing graphics database files between different environments.  

## dxfset.dat  

A file that contains the information for drill size and library name equivalents in basic units for the DXF Setup dialog box.  

## dynamic route  

To create a route using the Dynamic Route tool, which automatically creates turns and pushes other routes aside to complete the connection.  

## ecad hint.map  

A user-defined text file that you create, edit, and maintain. This file enables the replacement of approximated parts from SailWind Layout, with geometrically accurate components previously modeled in Pro/ENGINEER. This file must exist in either the current working folder or in the Pro/ ENGINEER software loadpoint\text folder.  

## ECO  

An acronym for Engineering Change Order. This refers to a file with netlist changes that needs to be annotated to update either the schematic or layout that has become out of sync with the new design changes.  

## ECO mode  

A mode that SailWind Layout enters when the ECO Toolbar is open. Changes that affect the connection list or parts list can be recorded in a file for backward annotation.  

See also ECO  

## ECO Options  

The setup choices available for the ECO output file in the ECO Options dialog box.  

## ECO registration of attributes  

Only ECO-registered attributes, set on the Objects tab of the Attribute Properties dialog box, can be added, deleted, or changed during the ECO process. Via attributes are not registered attributes and cannot be added, deleted, or changed during the ECO process.  

You can modify ECO-registered attributes only in ECO mode.  

Non-ECO-registered attributes are never recorded in an .eco file during ECO operations.  

To compare ECO-registered attributes, use the Compare Only ECO Registered Attributes option on the Comparison tab in the Compare/ECO Tools dialog box.  

## EDA  

An acronym for Electronic Design Automation.  

## EDC  

An acronym for Electrodynamic Checking.  

## edge  

One side of a polygon.  

## edge die  

The two or three rows of dice along the outer circumference of a wafer.  

## edges  

The Selection Filter preference that enables or disables selection of geometric segments.  

## editing  

Any action that modifies a design.  

## electrical layers  

Layers enabled for routing that are checked by DRC.  

## electrical net  

A series of nets connected by one or more components. Length, differential pair and matched length rules can be applied to an electrical net as though it were a single net.  

## embedded objects  

An object, including all of its data and the information needed to manage the object, that is contained within the framework of, and is a part of, the container application document.  

See also linked objects  

## EnableMacroLanguage  

The SailWindpcb.ini file entry that, when equal to one, enables loading of all macro parameters on startup and, when equal to zero, disables loading of macro parameters upon startup.  

## end component  

A component having at least one pin which is a final pin of an electrical net.  

## end no via  

The mode initiated in the routing shortcut menus that, while routing, ends a partial route without a via.  

## end via  

The mode initiated in the routing shortcut menus that, while routing, ends a partial route with a via.  

## end zone  

The part of the differential pair between the split point and destination pins.  

![](/images/81e108507d178e6b0eee8fd50a44290a9585019eb0a9b4addd6432c61c85ee74.jpg)  

The labels in the above graphic correspond to routing that starts at the left-hand set of pins and ends at the right-hand set of pins. The label positions are reversed if the routing starts at the righthand set of pins.  

See also differential pairs, split point  

## ending layer  

The finishing layer for a drill pair or via definition. Enter information about ending layer in the Pad Stacks Properties dialog box.  

## engineering change order (ECO) operations  

Any processes that modify the connection list or parts list.  

## entry angle  

The angle at which a route enters a pad.  

## Esc  

To use the Escape or Cancel keys to stop a current action.  

## estimated total length  

The trace length monitor calculates estimated length as the combined total of routed length (Rt), plus the routed length for the entire net—including overlapping segments— (Nt), the unrouted length (U1) of the trace being routed, and includes half the Discrete length value of each connected pin of components that have a Discrete length assigned (not shown).  

Overlapping segments are counted only once.  

![](/images/191b16fbd69b11c313a84dc6e82657b436220b8d3aabc0be9faed15db62c4128.jpg)  

See also routed length, unrouted length  

## eutectic solder  

A tin/lead alloy ( $63\%$ tin, $37\%$ lead) that melts at optimum temperatures.  

## export  

The translation command used to convert a design file into PADS-format ASCII or DXF.  

## extended rules  

Clearance, routing, and high-speed rules consisting of classes (one or more nets), groups (one or more pin pairs), individual pin pairs, decals, components and differential pairs. Without the Extended Rules option, you can assign rules on the net level only.  

## extension lines  

Lines extending from the points being measured.  

## extents  

The limits of the $\mathsf{x}$ and y coordinate area that is occupied by all items within a design. This includes information external to the board outline, such as dimensions or fabrication notes.  

## Fabless  

A semiconductor company that subcontracts wafer manufacturing because it does not have its own wafer manufacturing facility.  

## fabrication  

With semiconductor manufacturing, the front-end process of making devices in semiconductor wafers only, not the package assembly or back-end stages.  

## fanout  

A segment of trace or copper shape added to SMD pads to facilitate routing. A fanout typically consists of one or more trace segments connecting a component pad to a via, enabling the signal on an outer layer to connect to one or more internal signal layers or planes. A specialized repeated pattern is often necessary to break out multiple pads on the same component far enough from the component to enable easy routing.  

Use fanouts to:  

enable on-grid access by autorouters that cannot handle off-grid pads.   
make routing easier, and ensure connections are made. connect SMD pins to an inner plane layer using vias.   
connect an SMD pad to an inner signal layer where more routing space is available.  

## fanout pass  

An autorouting pass that places vias for inaccessible SMD component pins and routes, from the vias to the pins.  

## fanout side of CBP  

The side of the SBP Guide to which the CBP should be wire bonded. Usually the fanout side of the CBP is the same as its die side, but in some cases more complex patterns of wire bond fanout may mean that the two sides are not the same.  

## FCBGA  

An acronym for flip chip ball grid array.  

## feature size  

The smallest line width or spacing between lines or features on a semiconductor die.  

## feed-through hole  

A drilled and plated hole that passes conductivity from one layer to another. This is also called a via.  

## fiducials  

Fiducials are alignment marks, a type of target, used for calibration before placing objects.  

There are at least three types of fiducials:  

• Panel fiducials — used for alignment and calibration of images on a multi-board panel.  

Board fiducials — used align components on a specific board (on or off a panel). Fiducials are (typically) round solid targets placed near three corners of each board on each side of the board that will receive components. The pick and place system scans the board for these targets (shiny circles approximately . $040"$ in diameter) and uses them to align the machine before it starts placing parts.  

Component (local) fiducials — used for close tolerance placement of high pin-count components with fine pitch leads. The footprint (PCB decal) of a fine pitch component will typically contain two component fiducials at opposite corners of the footprint. This enables the pick and place machine to align the fine pitch component exactly on the footprint.  

## field upgrade  

Programming options on your security key by entering in a key unlock code using plicense.exe or equivalent.  

## file sharing  

Multiple users accessing the same file or files through a network.  

## file.dir  

The SailWindpcb.ini file entry that specifies the default location of your design files.  

## filter  

A settings dialog box within that controls which types of objects can be selected.  

## find  

The SailWind command that locates, and optionally selects, an object or group of objects in the database.  

## finger pad  

One of many long pads placed in a series to represent an edge connector.  

## finished hole size  

The size of a drilled or routed hole after plating and/or solder reflow has been applied.  

## flashed pads  

Pads produced on a photoplotter by opening the aperture momentarily, without moving the board, to produce a pad shape.  

## flat pack  

A component package where the leads extend away from the component and remain on a parallel plane with the base of the component.  

## flip  

The command that moves the selected items to the opposite side of the board.  

## flip chip  

An IC designed for face-down mounting by means of controlled-collapse solder pillars on a device's I/O bonding pads.  

## floating license  

A method of licensing where a central security server manages a pool of licenses for use by a large number of clients.  

## floating toolbars  

Toolbars you can undock from the sides of the application window and place anywhere on screen.  

## flood  

To fill a previously defined copper plane.  

## flower pattern  

Metal shapes placed under a die for thermal management and/or electrical connection; also referred to as a die flag.  

A ceramic, surface-mounted hermetic package.  

## FlushUndoBeyondSize  

The SailWindpcb.ini file entry that determines the maximum size of the undo buffer before SailWind Layout removes previous commands from the undo buffer to make room for the current command. If adding the current command causes the undo buffer to exceed this maximum size, SailWind Layout removes previous commands until the undo buffer can store the current command.  

## follow route  

The connections or pin pairs that are part of the bus routing, and which are routed following the guide route's path.  

## footprint  

The arrangement of pads for a given part decal. For example, the footprint of a fourteen DIP is two rows of seven pads, spaced 100 mils in the Y direction, and 300 mils in the X direction.  

## forward-annotate  

Update a design file using data from a schematic.  

## FR-4  

An acronym for Fire Retardant Number Four, an epoxy-resin substrate material used in laminate applications.  

## free copper  

Open or closed copper that is not associated to other copper or pads.  

## free disk space  

The physical amount of space available on your hard drive that is available for use by programs.  

## gap (accordion)  

The gap of an accordion sets the pitch between chords. The gap is a user-definable number multiplied by the same net trace-to-corner clearance.  

If the same-net trace-to-corner distance equals zero, then Trace Width is used for the gap calculation.  

![](/images/aa23c5062a138948e5a39e5da14d54a4802e3b9a765e36f180f3208097e45ace.jpg)  

See also accordion, amplitude, pair routing gap  

## gate  

An element of an electronic circuit whereby one or more signals are input, with one output being dependent on the state of the input(s) and the type of logic used to interpret the input.  

Pin swapping involves exchanging like inputs  

Gate swapping involves exchanging the entire element for a like element.  

## gate array  

An IC consisting of a regular arrangement of gates that are interconnected to provide custom functions.  

## gathering point  

The point near the source pins where differential pair traces can start to be routed together at the pair routing gap.  

![](/images/d0e94437ca0dceaf4734342cba9eaeb7c2f59d47061dc0f731130ea14170de84.jpg)  

The labels in the above graphic correspond to routing that starts at the left-hand set of pins and ends at the right-hand set of pins. The label positions are reversed if the routing starts at the righthand set of pins.  

See also differential pairs  

## GDI memory  

Memory reserved for Windows devices and graphics.  

## Geometry.Height  

This attribute is used to indicate the height of the part. The attribute enables SailWind Layout to prevent the component from being placed in an area of the PCB which is height restricted.  

In SailWind Layout, you can set board height restrictions for the top and bottom layers in the Drafting Options or area height restrictions using a Keepout area with a “Component height” restriction. This attribute is also passed from SailWind Layout to mechanical tools where it can be used in 3D simulations to determine whether the part will meet spatial requirements.  

In addition to the value, use one of the following units:  

• Use the quotation symbol " for inches. The SailWind Layout Attribute Dictionary specifies the following limits of acceptable values. Min=0.00000", Max $\c=$ 25.00000". Example: GEOMETRY.HEIGHT $\mathbf{\bar{\rho}}=\mathbf{\rho}$ 3.26548"   
• Use the abbreviation mil in upper or lower case. The SailWind Layout Attribute Dictionary specifies the following limits of acceptable values. Min $_{1=0.00\mathrm{mil}}$ , Max=25000.00mil Example: GEOMETRY.HEIGHT $\mathbf{\bar{\rho}}=\mathbf{\rho}$ 12654.83mil  

• Use the abbreviation mm in upper or lower case. The SailWind Layout Attribute Dictionary specifies the following limits of acceptable values. Min=0.00000mm, Max=635.00000mm.  

Example: GEOMETRY.HEIGHT $\mathbf{\bar{\rho}}=\mathbf{\rho}$ 123.21348mm  

## Gerber  

The language used to drive a photoplot machine. This language is an ASCII file with instructions for selecting an aperture, moving the light source, and turning the light source on and off.  

## Global tab  

Options tab that includes settings that affect an entire design, such as units of measurement and pointer size.  

## Glue  

Anchors component(s) in their current location so they cannot be moved  

## grab bars  

The two vertical or horizontal bars to the left or top of the window.  

## graphics cache  

The SailWind setting used to optimize graphics. This is handled by the DisableCaching entry in the SailWindpcb.ini and SailWindlogic.ini files.  

## green dot  

The status indicator located in the upper left corner of the workspace. It is green when the system is idle or ready for operation. It is red when the workspace cannot receive user input, such as when producing CAM drawings.  

## grid  

A division of the workspace into measurement steps to facilitate accurate spacing between placed parts and routed lines. Also refers to the display; small white dots locating the measurement steps  

## ground plane  

A design layer completely filled with copper, except for clearances around nonconnected pads and vias.  

## group  

A collection of pin pairs that share common design rules.  

## grow  

An cluster placement feature that adds additional parts to an existing cluster.  

## guard band  

An octagonal shape that appears at the end of a trace during routing operations whenever the head of the trace meets a clearance obstacle that it cannot shove. The guard band only appears when online design rules are enabled.  

![](/images/e4cae2516ddfab3d43b37ddcbdd37f0b05c0a8d5a858307c703aa8fe2e8a63f5.jpg)  

## gui  

An acronym for Graphical User Interface. The GUI includes such things as menus and commands that allow for interaction between the user and the software program.  

## guide route  

A route segment that is used for the first connection and that is the lead for laying down two or more pin pairs simultaneously in neat flowing patterns.  

## hard rule  

A rule that is always followed. See also soft rule, and Hard and Soft Rules.  

## hard breakout  

Use of associated copper within a surface mount decal to simulate a dispersion route. The disadvantage to this method is that routing channels will possibly be blocked.  

## hatch  

A copper fill pattern that uses horizontal and vertical lines at a specified width and spacing.  

## HDI  

An acronym for High Density Interconnect.  

## heat dissipating component  

While all components generate heat, these components generally have a published wattage rating. Care must be taken to ensure components or materials adjacent to these heat generating components do not exceed their max temperature ratings. If more than one of these components are used in a design, they should be spread out and should also be positioned to not impede airflow.  

## heat sink  

An assembly that serves to dissipate, carry away, or radiate heat into the surrounding atmosphere.  

## high density interconnect  

A class of packaging involving boards, substrates, and components using extremely small trace and spacing dimensions.  

## highlight  

A user-defined color, usually white, used to denote that an object is selected.  

## high-speed checking  

Using the Electrodynamic Checking utility. A simulator-type check that finds traces that may run parallel to each other close enough, and for a long enough distance, to cause cross talk.  

## hole plating  

A fabrication process where solder flows through a drilled hole to connect the pads on either side of the hole, to provide connectivity between two or more layers.  

## HPGL  

An acronym for Hewlett Packard Graphics Language, a standard pen plotter interface language.  

## IC (Integrated Circuit)  

An acronym for Integrated Circuit.  

## IDF  

Intermediate Data Format. An industry standard format used for exchanging data between electrica and mechanical design systems.  

## IMAPS  

An acronym for International Microelectronics and Packaging Society.  

## impedance  

Resistance to the flow of current in a trace. Measured in ohms.  

## in circuit testing  

An exhaustive and thorough test of a PCB in final production that tests nets and unused pins for such things as correct voltage, correct parts, or bridging. Test point placement is critical for in circuit testing.  

## inaccessible nets  

Nets for which you cannot define test points. DFT Audit analyzes all nets. If DFT Audit determines that test probes cannot access them, the nets are inaccessible (also called non-adaptable).  

## INI file  

An ASCII file, with the .ini filename extension, that contains startup parameters.  

An INI file for Windows might contain the following information: graphics drivers, mouse drivers, fonts, and so on.  

An INI file for programs might contain the following information: folder structure, display colors, default editors, and so on.  

## inner layers  

Design layers other than those on the top or bottom of a printer circuit board. Inner layers may be routing layers, plane layers, or a combination of both.  

## installed options  

SailWind product features that you have bought and installed as part of the software package.  

## instruction pointer  

A small yellow arrow in the Output window gutter that indicates the current line in a script or macro.  

## insulator  

A material used to inhibit heat or electrical properties, such as current flow.  

## integrated SailWind Designer project  

A SailWind Designer to SailWind Layout project that uses a common database to share design information instead of using netlists to pass the design information between the software applications.  

## integrity check  

A database check runs whenever a .job, .dxf, or .asc file loads. You can also initiate an integrity check while you are working. Type the I modeless command, then press the Enter key.  

## intensity  

A value assigned to objects such as vias to weigh decisions made during the autorouting process in SailWind Router. The higher the intensity, the less the item is used. For example, set a high intensity for via usage to minimize the amount of vias added to the design.  

## interconnect  

A conductive connection between two or more circuit elements.  

## IPC  

An acronym for Interprocess Communications within the SailWind product.  

## irregular trace length  

Sections or segments of differential pair traces not routed at the pair routing gap.  

See also differential pairs  

## islands  

Small, isolated sections of copper plane that are not attached to anything.  

![](/images/56fdef11e556dd3bed520b78268402aece7c0b39a7165236c9f22ebf8b3f941d.jpg)  

An acronym for Joint Electron Device Engineering Council.  

## Joint Electron Device Engineering Council  

JEDEC is the semiconductor engineering standardization body of the Electronic Industries Alliance, a trade association that represents all areas of the electronics industry.  

## jumper  

A physical part used to cross over traces on most one layer PCB designs. Jumpers can be 0 Ohm resistors or wires stretched between jumper pads.  

## keepout areas  

Areas that automatically ban objects. Depending on the keepout Properties, these areas may be set to prevent: placement of components, components that exceed a specified height, component drill holes, traces and copper, copper planes, vias and jumpers, and test points.  

## keyview.exe  

An executable file used to list the options programmed into your key. When you run keyview.exe, it creates a file named keyview.txt that contains a listing of your key options.  

## label  

A label is a display instance of a component or jumper attribute. If you want to make an attribute visible in the design, you must instantiate it as a label associated with a component or jumper. You can do this in the Design Editor or the Decal Editor. You can have multiple labels based on the same attribute. An attribute has two parts—a name, and a value. A label of an attribute can have one of four visibility settings—None, Value, Name and Value, and Full Name and Value.  

## Latium rules  

Latium rules are for advanced functionality in SailWind Router. Some constraints that you can set in Layout are only used by SailWind Router. For examples, see the Tune/Diff Pairs options, Fanout Rules, Pad Entry Rules. The Latium checks include:  

component clearance rules component routing rules differential pair rules via at SMD rules  

## layer biased net  

A layer biased net is any net with a design rule specifying a layer bias to one or more, but not all, electrical routing layers  

## layer pair  

The assignment of two routing layers to switch between using the Layer Toggle command. On two layer boards, the toggle is automatically set between 1 (top) and 2 (bottom).  

## layer toggle  

To switch between layer pairs while routing.  

## layers  

A standard CAD database feature that separates graphical information into sheets of similar information such as dimensions, construction lines, or text. For PCB applications, this enables the various fabrication layers to be created and output separately.  

## layout-driven design  

A PCB design process in which no schematic is created, and both the logical (netlist) and physical conformations of the board are defined in a layout tool. Also, a design created using this process. See also schematic-driven design.  

## Layout.rep  

The error report file that is created by the database integrity test and which is written to the \SailWind Projects folder.  

## LCC  

An acronym for Leadless Chip Carrier.  

## lead frame  

A sheet metal framework that is etched to form an array of metal traces.  

## lead pitch  

The sum of the lead width and lead spacing.  

## lead spacing  

The distance between a component's adjacent leads.  

## Leadless Chip Carrier  

(LCC) Ceramic IC package with no physical lead. There are only pads on the bottom of the package around the edges.  

## length matching  

A same-length requirement where the entered value represents a minimum/maximum length tolerance for nets belonging to the same class.  

## length minimization  

A routing feature that configures unroutes to the shortest available distances, or in a specific topology, to facilitate high speed routing.  

## LGA  

An acronym for land grid array.  

## LibDir  

The SailWindpcb.ini file entry that specifies the location of your library files.  

## libraries  

The collection of part types, part decals, and drawn items included with a SailWind product or created by the user.  

## Library Manager  

The SailWind feature that provides access to, and allows for modifying, the library of parts.  

## linked objects  

When an object is linked, a presentation of the object and link to the source is contained within the framework of, and is a part of, the container application document. The object is linked to its source, and the source continues to physically reside wherever it was initially created. Therefore, the file that contains the object is smaller than if the object were and embedded object. See also embedded objects.  

Whenever you open the file that contains the linked object, the object checks the source to see if it changed since you last saved the file. If the source changed, then the linked object automatically updates.  

## LogCompressionMode  

A SailWindpcb.ini file entry that controls recorded mouse movements in a log file. When set to one, the default, recording of compressed mouse movement is enabled. When set to zero, recording of all mouse movement is enabled.  

## logic family  

The assignment of an electrical type by name, such as CAP (capacitor) or RES (resistor), to indicate the appropriate reference designator prefix such as C or R.  

## LOGMode  

A SailWindpcb.ini file entry for online macro recording to a log file. When set to 0, the default, recording is disabled. When set to one, macro recording is enabled, and the next.log file is created.  

## loop  

A pin pair that contains a route that branches off the original route, then branches back into the same route to form a loop.  

## loop routing  

Used to create a loop in an existing route.  

## LPT port  

A parallel printer port, usually referred to as LPT1 or LPT2.  

## macro  

Internal objects that are handled using the macro engine vocabularies, and may or may not have the automation interface.  

## Manhattan distance (delta $\times+$ delta y)  

Used to approximate unrouted net length for BoardSim. Add a percentage multiplier to account for indirect routing paths.  

## masking  

The inhibiting of electrical interference between two traces on different layers due to separation by a ground or power plane.  

## material condition  

There are three material conditions when creating component decals. They are Maximum (providing the most robust solder joint), Nominal (providing a general purpose solder joint) and Minimum (providing the least possible solder joint for very dense designs).  

## MCM  

An acronym for multichip module.  

## memory pattern  

A collection of routes between memory devices that form a distinctly repeatable pattern.  

![](/images/99a3535d7c98d07d5bdae32765a5fbd3a3d3429a9dcb46c7cd6f1cbfd88c9281.jpg)  

## menufile.dat  

The file containing the structure and text of all lists and shortcut menus. The menufile.dat file must be located in the same folder as SailWindPCB.exe.  

## micrometer  

One-millionth $(10^{-6})$ of a meter; about 40 millionths of an inch. Micrometer is synonymous with micron.  

## micron  

A term used for micrometer. One-millionth $(10^{n_{-6}})$ of a meter; 25.4 microns $\mathbf{\Psi}=\mathbf{\Psi}$ 1 mil.  

## microvia  

Vias that have a narrow drill hole. Because of their specific diameter to depth ratio, they are typically blind or buried vias and do not pass through many layers of the design.  

## minimum geometry  

The smallest line width or spacing between lines or features on a semiconductor die.  

## miter  

A diagonal segment or arc that replaces a corner.  

## miters pass  

An autorouting pass that converts all 90 degree route corners to diagonal corners.  

## mixed plane layer  

A plane layer that contains obstacles other than pads, such as routes, copper, or text.  

## modeless command  

A command invoked through the keyboard. Commands include display options, design settings, and mouse click substitutions.  

## modify  

To change information for a selected object.  

## moiré  

Target-shaped objects located in the corners of finished artwork that are used to properly align each layer to others for design verification and fabrication.  

## monolithic device  

A device whose circuitry is completely contained on a single die or chip.  

## mounted side  

The side of the printed circuit board, either front or back, on which components are mounted.  

## mounting holes  

Many (but not all) boards have mounting holes. Mounting holes are typically located around the perimeter of a board (most often in the corners). They are drilled holes, used to mount a printed circuit board to the finished product (for example, a mother board mounted to the computer casing), or used to attach bolt-on components to the printed circuit board (for example, stiffeners and ejector tabs).  

There are two types of mounting holes: plated and non-plated. Plated mounting holes have copper inside the hole and usually have a large annular ring of copper on both sides of the board connected by this copper cylinder (plating) inside the hole. These holes are typically connected to the GROUND bus or plane on the board and provide a method for grounding the board circuitry to the enclosure (for shielding purposes). The mounting hole ring diameter is usually slightly larger than the diameter of the head of the screw that will be used to fasten the board to the mounting device within the enclosure. Non-plated mounting holes are used for the same purpose, the only difference being that they are not internally plated and do not have a copper ring, therefore they are not used for grounding the board to the enclosure.  

Plated mounting holes cannot be used as tooling holes as the thickness of the copper plating can vary and violate the close tolerance required by a tooling hole. Non-plated mounting holes can sometimes work double duty as tooling holes because there is no internal plating, therefore the tolerance of the hole size can be more closely controlled and fit within the requirements of a tooling hole.  

Use the Decal Editor and the Pad Stacks dialog box to create tooling holes. Save the singleterminal object as a part to the library for reuse.  

See also Creating and Adding Board Mounting Holes in the SailWind Layout User’s Guide and Reference Manual  

## multichip module  

A package with multiple dice that is $20\%$ or more silicon, has 100 or more I/O on a substrate, and four or more layers.  

## multilayer PC board  

A design that contains routing and/or plane layers, in addition to those on the front and back side.  

## nail diameter  

The diameter of the test probe.  

## NC drill  

An abbreviation for numerical control drill. This technology involves producing an output file containing the x-y location and drill size for each hole, then feeding this information into a machine for automated hole drilling.  

## negative  

A photographically produced reverse image of a plane layer. This allows cleared areas, or airgaps, to be created using normal drawing techniques. When reversed, all areas not drawn for clearance become the actual planes.  

## nested embedding  

Nested embedding occurs when you insert an object using OLE into another object. For example, inserting a SailWind Logic schematic into your SailWind Layout Design or inserting a Microsoft Word document into a schematic.  

## nested macros  

Macros called from other macros.  

## net  

All pin pairs composing one individual signal. Nets contain at least one subnet, but may contain more than one.  

See also subnets  

## net class  

A collection of nets with a common set of design rules.  

## net length rules  

Rules that control a net's or pin pair's routing length.  

The following high-speed rules are examples of net length rules: minimum/maximum length, matched length, and differential pairs.  

The phrase controlled length net refers to nets that have length rules, or nets with pin pairs that have length rules.  

## net name  

A specific name given to a net to describe its function; for example, GND, PWR, or DATA0.  

The maximum net name length is 47 characters. You can use any alphanumeric characters except $\{\}^{\star}$ and space.  

## netlist  

A point-to-point connection list for each signal in a design, providing the reference designator (part name) and pin number.  

## netlist file  

A SailWind ASCII file containing all of the nets in a design, including all component pins that make up the nets. The file may also contain a list of all parts in a design, and/or the settings that control the substrate bond pad numbers and functions for newly created substrate bond pads.  

## netlist.fmt  

The ASCII setup file for the report format that produces a netlist without pin information.  

## network security  

Use of one security key, programmed with multiple options, for network use with one or more systems at a time.  

## next.ini  

A file produced in the C:\<install_folder>\<version>\Programs folder when the SailWindpcb.ini entry LOGMode is equal to one. The next.ini file is a copy of your SailWindpcb.ini file at the time next.log is written.  

## next.log  

A file produced in the C:\<install_folder>\<version>\Programs folder when the powerpcb.ini entry LOGMode is equal to one. The next.log file records all activities within a SailWind Layout session so that they can be replayed to reproduce a series of steps or used to illustrate a problem.  

## node  

A point along a trace where traces join other traces (T junction), where traces transition to other layers, or where traces end at pins, virtual pins, vias, or floating endpoints. Specifically, a node can be any pin, virtual pin, via, copper, trace junction, virtual point, or trace end.  

See also virtual point  

![](/images/4fe463f69105b1f3b156f1f9c5706157c3abb9256937f65c2b17a91b650c70a0.jpg)  

## node-locked  

A license for a specific Host ID.  

## non-ECO-registered parts  

These parts are found in the schematic and layout design. Parts not selected as an ECORegistered Part on the General tab of the Part Information dialog box are non ECO registered pa  

• A schematic non-ECO-registered part is required in the schematic but has no place in the layout of the circuit board. For example, a chip socket shown in the schematic for inventory tracking in the bill of materials.   
• A layout non-ECO-registered part is required in the layout design but has no place in the schematic. For example, a plated and grounded mounting hole.  

## non-electrical parts  

Parts with no pins. For example, a mounting screw shown in the schematic for inventory tracking in the bill of materials.  

## non-plated holes  

Pads that are not reflowed with solder, usually reserved for mounting holes. Non-plated holes are not drilled with an oversize to accommodate the solder flow.  

To determine plating status, in SailWind Layout, use the Pad Stacks Properties dialog box. In SailWind Router, use the Pad Stack tab in the Pin Properties dialog box.  

## nudge  

A placement feature that relocates parts to make room for new parts being placed. Movement is based on previously defined clearance rules.  

## object  

One discrete item in the design. For example, an object may be a route segment, a part, a drawing line, or a via.  

## object mode  

Start a command by selecting one or more objects and then selecting the command to perform on them.  

See also verb mode  

## obstacles  

Objects that block routing, for example protected pins, vias, traces, keepouts, and board outlines.  

## odd pad shape  

A pad that requires a special aperture, or plot sequence, to create. In SailWind Layout, in the Pad Stacks Properties dialog box, the odd shape setting should not be confused with trying to create a custom shaped pad which is accomplished by drawing copper in the decal and associating it to the pad.  

## offline plot  

A plot that is sent to a file before it is copied to a printer or plotter for processing.  

## offset  

The distance by which rectangular or oval pads are moved away from the electrical center of the pad stack.  

## offset pads  

Rectangular or oval pads moved off the electrical center of the pad stack to facilitate identification/ selection, or for a special design consideration.  

## one pin nets  

A net that contains only one pin. Also called single pin net. In SailWind products, a net must have a minimum of two pins.  

## online DRC  

A SailWind feature that actively checks established-design rules during routing or placement operations.  

## online plot  

A plot sent directly to a printer or plot.  

## open cluster  

Clusters that you can delete or replace during automatic cluster creation.  

## optimization  

Rearranging placed parts and/or swapping pins and gates on parts to minimize trace lengths and reduce the number of vias required for routing.  

## optimize pass  

An autorouting pass that analyzes each route and tries to improve the quality of the route pattern by removing extra segments, reducing via usage, and shortening routed trace lengths. This pass includes glossing and smoothing processes.  

## overlapping coppers  

Overlapping coppers are combined into one copper area, with possible cutouts.  

![](/images/22d45d92f57dc1c8bdf461cfbb1f8692e8afa6b59bff12ae9c8bcd83fad4214d.jpg)  

See also coppers, copper connectivity  

## overlapping cutouts  

Overlapping cutouts are combined into one cutout area.  

![](/images/9523f889149b10e1e1b523c38806e1659d11e2387866aafc77987fb0bd925b3b.jpg)  

See also cutouts  

## overlapping segments  

Multiple trace segments stacked on top of one another on one layer.  

## package  

The protective container for an electronic component with terminals to provide electrical access to the die components inside.  

## pad entry  

The point where a trace entering or exiting a pin first crosses the edge of a pad.  

## pad entry angle  

The command in SailWind Layout and Router that establishes the angle at which a trace enters a pad. This may be orthogonal (90 degrees), diagonal (45 degrees), or any angle.  

## pad function  

The die signal name to which the component bond pad is connected.  

## pad number  

The number of the component bond pad.  

## pad oversize  

On plane layers, pads that are larger than normal, to generate proper clearances when the image of the pad is printed in a negative format.  

Pad oversize is measured from the center of the pad, not the perimeter. For example, if you have a 3 mil oversize, the measurement is actually1.5 mils in each direction from the center of the pad.  

## pad stacks  

The combination of pads, drills, and pastes, for example, on a pin or via, for each layer of a design, stacked directly on top of one another.  

## pair routing gap  

The fixed edge-to-edge clearance between the traces in the controlled gap area for a differential pair.  

![](/images/3d065c9c6974c677187f1ac7644decf8e4e588888f84498b9e5f794281f58ac7.jpg)  

See also controlled gap area, differential pairs.  

## paired layer  

The start and end layers used by the layer toggle command when changing layers while routing. It defines the default layers to use when you make layer changes.  

## palette  

A user-definable color chart in the Display Colors dialog box.  

## pan  

Up and down or side-to-side movement of the screen without zoom or redraw. Use the scroll bars or postage stamp to pan.  

## panning  

Moving the view horizontally or vertically without changing the size of the design on your screen.  

## parallel port  

A printer port, usually referred to as LPT1 or LPT2.  

## parallelism  

Traces on the same layer that are checked for running parallel to each other.  

The traces are subject to crosstalk if they run parallel to each other too long and the gap between them is too short.  

## parasitic  

An undesirable stray capacitance, inductive coupling, resistance leakage, or undesired transistor actions.  

## parent object  

The object to which individual design elements, such as lines, arcs, or corners, belong.  

## part decal  

The physical representation of a part, or footprint, assigned to the part type.  

## part list  

An output listing of all parts belonging to the same design. This normally includes the reference designation, part name, and part type, and total number of each type.  

## part name  

The text for each part that indicates the reference designator.  

## part outline width  

The line width of 2D line shapes, created in the PCB Decal Editor, that represent silkscreen or documentation data within a part decal. The shapes do not include text, reference designators, or copper with the decal.  

## partial route  

Partial routes are uncompleted routes where the ratsnest flightline is still visible. This occurs when you click End while routing or bus routing, or when you delete a trace segment. See also dangling route.  

## partial via  

A via that does not travel through all of the board's electrical layers. The blind via and buried via are both types of partial vias.  

## parts1.fmt  

An ASCII part list format file for the report file generator that consists of a reference designator, part type, and logic type.  

## parts2.fmt  

An ASCII part list format file for the report file generator that consists of a part type, reference designator, and part description.  

## paste  

A substance used to attach each pin of a surface mount device to a PC board.  

## paste mask  

An artwork layer with a paste location for all pads of surface mount components.  

## patterns pass  

An autorouting pass that searches for, and routes, groups of unrouted connections that can be completed using a typical C routing pattern, Z routing pattern, and memory pattern.  

## PBGA  

An acronym for plastic ball grid array.  

## PDF configuration  

A set of PDF Configuration dialog box control settings. A PDF configuration can be saved as a .pdc file and reused to create PDF documents for multiple designs.  

## PGA  

An acronym for pin grid array.  

## photoplotting  

Using a machine to create printed circuit board fabrication artwork. The machine creates artwork by exposing clear film to light or by rasterizing an image onto clear film.  

## physical design reuse  

A collection of design objects that you want to reuse, which are associated with one another. The collection of objects can be saved to a file.  

## physical design reuse elements  

The objects that compose the reuse. They can include components, routes, vias, text items, and other elements.  

## pick and place  

An automatic printed circuit board assembly machine, driven by outputting the part type, location, and orientation of suitable parts from a design.  

## pin  

The through-hole or surface mount terminal that represents a connection to a part. Pins are also referred to as pads in pad stacks.  

## pin array/pin grid array  

A package with pins distributed over much or all of the bottom surface of the package in rows and columns.  

For more information, see Decal Wizard Dialog Box, BGAPGA Tab.  

See also pin types.  

## pin number  

Within a component, the numeric or alphanumeric designation that distinguishes pins from each other.  

In the Status bar, pins are identified using the following format:  

Pin:[Component name].[Pin number].[Pin type]  

For example:  

See also pin types.  

## pin pair  

The combination of a trace or unroute, and the pins on either side. A net can contain one or more pin pairs.  

## pin pair group  

A collection of pin pairs that share common design rules.  

## pin type  

A designation that indicates the electrical characteristics of the pin such as Source (S), Load (L), Terminator (Z), and Undefined (U). For example, U1.1.S may appear on the status bar.  

## pin types  

Pins and pin pairs can be identified by one of the following pin types:  

Source   
Bidirectional   
Open Collector   
Or-Tieable Source   
Tristate  

• Load Terminator Power Ground Nonelectrical  

Pin types make up the last portion of the pin identifier in the Status bar. For example:  

Pin:U10.C.Open Collector  

See also pin number  

## placement check prints  

Generate a CAM Assembly drawing to make a placement check print.  

After the PCB Designer receives a schematic and a netlist from an Engineer, they (typically) place the components onto the board in a manner that best suits the routing of the board. Sometimes, the placement better suits the intentions of the Board Designer than the Engineer, so before routing proceeds, the Engineer will request to see a set of Placement Check Prints. Placement Check Prints show the placement of all components on both sides of the board, so  the Engineer can review the locations and confirm the Designer has correctly placed the components. These Placement Check Prints typically require agreement from both the Designer and the Engineer before routing can proceed.  

## placement operations  

Operations where parts are relocated or added to a design to optimize an existing placement.  

## plane hatch outline  

The outline of a copper plane shape after it has been flooded to differentiate it from the plane pour outline as originally drawn. When you draw the copper plane pour outline and then flood the shape, the outline often changes to accommodate the modeless command PO.  

## plane layers  

A design layer where the entire surface is covered by copper, except for information not connected to the plane.  

## plane nets  

Nets assigned to plane layers.  

## plane pour outline  

The outline of a plane shape after it has been drawn to differentiate it from the plane hatch outline after it has been flooded. You can switch plane display modes using the shortcut modeless command PO.  

## plastic ball grid array  

A surface mount package with an array of solder sphere-shaped interconnects arranged across the bottom surface of the package substrate.  

## plastic leaded chip carrier  

A common surface mount package with leads on all four sides, used as a socket for devices that cannot withstand the heat of the reflow process, and/or to allow for easy component replacement.  

## plated holes  

Drilled holes that have copper covering the inside surface of the hole, and which are connected to a pad on each side. Plated holes pass connectivity from one layer to others.  

## plating tail  

A route that connects BGA vias to a plating bar or bus bar.  

## PLCC  

An acronym for plastic leaded chip carrier.  

## plicense.exe  

The program used to verify and program your security key during a field upgrade process.  

## polar decal  

A single-radius, circular pattern decal with through-hole pins.  

## polar SMD decal  

A single-radius, circular pattern decal with SMD rectangular or finger pads.  

## polygon  

A closed shape consisting of three or more line segments.  

## positive  

An image of a plane layer where cleared areas, or airgaps, are created using normal drawing techniques. When reversed to create a negative, all areas not drawn for clearance become the actual planes.  

## power board  

A board that is designed to control power to other circuit boards.  

## power plane  

The plane layer where power supplied to the printed circuit board is dispersed to the proper pins of each component requiring a power source.  

## SailWindpcb.ini  

The SailWind Layout initialization file for default settings.  

## powerpcb.mdb  

The SailWind Layout message file that contains error messages, prompts, and other miscellaneous text strings. This file must be located in the same folder as SailWindPCB.exe.  

## preferred routing direction  

In the main GUI combo box, the Horizontal [H] or Vertical [V] designation next to a routing layer name. This designation indicates optimal direction for routing completion and can be set by the user or the system.  

## prepreg  

A resin pre-impregnated sheet used to bond substrate laminate-pair layers together when a multilayer board is pressed together.  

## preset files  

Library IQ files that enable you to save the preference settings you have established for a die design and use them in other designs. The Bond Pad Preferences files have a .pre file extension.  

## preview of CBP assignments  

A preview that displays the substrate bond pads and wire bonds created when component bond pads are assigned to rings. This preview appears in the work area when the Assign CBPs to Rings dialog box is active.  

## preview of SBP guides  

A real-time preview that displays any changes made to the number, geometry, or location of SBP guides. This preview appears in the work area when the Wire Bond Wizard dialog box is active.  

well as in the design in which you place the reuse.  

See also private nets  

## primary component side  

The mounted side of the board when using through-hole components. See also secondary component side  

## primary objects  

Primary object groups in the Object View tab of the Project Explorer contain non-removable design elements shown in a high-level object hierarchy. Primary objects are:  

layers   
components part decals   
net objects (including nets and pin pairs)   
via types  

## private nets  

Nets that are contained completely within a physical design reuse.  

See also public nets  

## probing  

The testing of individual IC dice using very fine probes to temporarily connect each to a test computer to verify operation.  

## properties  

A set of dialog boxes used to view or edit information about the selected object.  

## protect  

Glues the routes and attached vias and prevents the autorouter from modifying them in any way.  

## protected routes  

Traces that are placed in a protected state by Route Protection. This means that they cannot be moved or modified.  

## protected traces  

Traces placed in a protected state (cannot be moved, or modified).  

## protected unroutes  

Unrouted connections, or the unrouted portion of a partial route, that are placed in a protected state by the Route Protection feature. This means that they cannot be routed, moved, or modified.  

## public nets  

Nets that are partially contained within a physical design reuse. Public nets exist in the reuse, as preferred routing direction  

In the main GUI combo box, the Horizontal [H] or Vertical [V] designation next to a routing layer name. This designation indicates optimal direction for routing completion and can be set by the user or the system.  

## pulling an arc  

Creating an arc from an existing line segment, where the diameter is derived from the line length.  

## QFP  

An acronym for quad flat package - a surface mount IC with leads on each four sides.  

## quad  

A square-shaped IC with pads on each of its four sides.  

## Quick Filter Settings  

The shortcut menu selections available when no items are selected. These choices set the selection filter for commonly used tasks, enable quick access to the Find command, and Select All items as specified by the Selection Filter.  

## quick measure command  

The Q modeless command which attaches a measurement line to the pointer and displays dx, dy and hypotenuse information, depending on pointer movement.  

## radial lead  

A discrete part with pins that protrude straight down and do not extend beyond the perimeter of the component body. An example of this is a capacitor.  

## RAM  

An acronym for Random Access Memory. The volatile (on chip rather than on disk) memory area available to the system for program operation.  

## range select  

To select a series of geometric or route segments by first clicking on the start segment, then pressing and holding Shift and right-clicking on the end segment.  

## ratsnest  

A term used to describe the display of all of the unrouted connections in a design. Also known as air lines or unroutes.  

## raw database  

The raw database contains all components in the open database, regardless of assembly variants. When created, new assembly variants are based on the raw database, meaning that until you uninstall or substitute, a new assembly variant includes every component in the raw database.  

## read-only attribute  

An attribute whose value cannot be changed in SailWind product dialog boxes. You can, however, modify attribute properties and the Attribute Dictionary entry, and can modify the attribute value in the library.  

## real width  

To display traces at their specified width, as opposed to displaying them as one pixel centerlines.  

## real-time redraw  

A feature that enables active regeneration of objects in the display any time the screen is redrawn. When you disable real-time redraw, regeneration occurs in the background, and the display is refreshed all at once after the background regeneration process is completed. Screen regeneration is quickest when real-time redraw is disabled.  

## record locking  

Allowing two or more users to access the same library component at one time. However, only one user has access to save the component.  

## recover  

Resolving an installation or operational issue, or salvaging a corrupt database by executing a specified series of steps.  

## redo  

Repeats actions which have been undone.  

## redraw  

Refreshes the display of the current screen image and the cursor.  

## reference designator  

An identification assigned to each of a design's parts to distinguish them from other parts of the same type when placed on the printed circuit board. A reference designator is usually in the form of a letter that represents the part type, followed by a number. For example, C2 may represent the second capacitor in the design. SailWind Layout permits you to renumber the reference designators in one of several specific patterns enabling you to quickly find a part among thousands on the manufactured board. The reshuffled numbers that are rearranged in SailWind Layout are backward annotated to the schematic software to keep the designs synchronized.  

## relative coordinates  

Coordinates that are based on a start point instead of the system origin.  

## rename  

To assign a different name to a part or net.  

## reroute  

Specifying that a trace, or a portion of a trace, follow a path different than the one currently being taken.  

## restricted layer  

Layers that are either disabled for routing or have been disallowed by layer biasing rules. When a layer is restricted, routing is not permitted on the layer. Layers can be restricted for specific objects, such as a net or a pin pair.  

## restricted via  

A via that is not permitted for use in the Routing Rules of SailWind Layout or Via Biasing properties in SailWind Router at any level of the rule hierarchy.  

## reuse  

See preview of CBP assignments.  

## reuse definition  

The master copy of the physical design reuse that is saved to a file. The saved version of the physical design reuse is the version you should use in other designs. All resulting instances of the physical design reuse are based on this file.  

## reuse type  

A name that identifies the type of reuse being created. A reuse type is equivalent to a library part type.  

## ring geometry  

The shape of the die flag ring. The following shapes, or ring geometries, are supported: rectangle, rounded rectangle, chamfered rectangle, and arced shape.  

## romansim.fnt  

The default file that contains definitions for the graphics for the SailWind stroke font, used to display text in SailWind products when system fonts are not in use.  

## rotate  

The command that rotates by 90 degrees a component or object around its axis or selection point.  

## route  

To create a metal etch trace of a specified width between pads.  

## route-completion target  

This crosshair or bullseye symbol appears when routing from one pin of a pin pair to another pin or when rerouting a trace segment.  

The partial target appears when you are overtop of an electrically compatible pin, but you have settings that are preventing you from routing to it - for example, the unroute of the pin pair you are routing is protected (you have selected the Protect Unroutes check box in the Pin Pair Properties).  

![](/images/8ddbfcca596f03cfd0319a8a8f67d026e8dae0875a4562ddfbb53e1eadfebe4b.jpg)  

## route loops  

A pin pair that contains a route that branches off the original route, then branches back into the same route to form a loop.  

## route pass  

The autorouting pass that is the core pass that performs the majority of autorouting. During this pass, SailWind Router attempts to sequentially route each unroute until all connections are attempted. The Route pass contains serial, rip up and retry, push and shove, and touch and cross processes.  

## routed length  

The trace length monitor calculates routed length as the cumulative length of the trace. Includes half the Discrete length value of each connected pin of components that have a Discrete length assigned. If you start routing from the endpoint of a partially routed trace, the routed length includes the partially routed trace length. If the trace has branches, then the length is calculated from the branch point.  

See also estimated total length, unrouted length  

## routes  

A series of traces that represents routed connectivity.  

## routing angle  

The angle applied to adjacent segments as new corners are added to traces. For example, an orthogonal routing angle means adjacent segments will be created at 90-degree angles to each other.  

## routing order  

The order in which the autorouter routes components, nets, and net classes.  

## routing pass types  

There are several pass types, each of which is designed to complete a specific task. Each pass may use more than one algorithm and may also perform a number of subpasses.  

| ·center pass    | · patterns pass   |
|-----------------|-------------------|
| ·fanout         | · route pass      |
| · miters pass   | · test point pass |
| · optimize pass | · tune pass       |

## routing strategy  

The collective information SailWind Router uses to autoroute a design. This information includes which pass types SailWind Router should perform, whether to protect the resulting traces, and what intensity to assign to objects.  

## ru.cfg  

A configuration file used by the nrus.exe program for Novell network security support.  

## rule values  

The values of any item, regardless of its default rules or rules set assignments.  

## rules  

An established set of conditions for a given net or design.  

## rules set  

A specific set of user-assigned nondefault rules such as pin pair, groups, or classes.  

## same net checking  

Checks clearances between objects along the same net, as specified in the Clearance Rules dialog box. Object to object checking includes:  

• Pad edge to pad edge.  

![](/images/04d56127eacf4761e270c83d949f9fede33c12b4a08b8302d82e323cd7e22e8b.jpg)  

• Pad edge to inside corner of trace.  

![](/images/0877c686eb40711847d3ab074b0dcee50a62852b26d2fcfabd661f0ae73eed57.jpg)  

• SMD edge to pad edge.  

![](/images/01deabfc8c9e2ff78a20c0bf26571fd0ae97c8e817f120a4d9e767ddf26a3066.jpg)  

• SMD edge to inside corner of trace.  

![](/images/20783ea587e780fd90dbb7b2516a0b6eb2f937230374440f4a8edbb1b18faad1.jpg)  

This check prevents solder bridging during board manufacturing caused by acute angles between conductive objects such as the acute angle between pad and trace shown below.  

![](/images/4df19a649ac147b4a3b59214e7f543e70c73c68e174eaa783573b20a54822f7d.jpg)  

## same net rules  

Specifying conditional settings, such as spacing, for connections belonging to the same signal name or net, rather than against other nets.  

## SBP  

An acronym for Substrate Bond Pad.  

## SBP fanout  

A single-segment fanout that connects SBPs to any-angle coupling traces.  

## SBP guide  

The virtual snap line along which substrate bond pads are aligned during wire bond fanout generation. Each SBP guide determines the alignment of the substrate bond pads that are associated with the SBP ring aligned with this SBP guide.  

## SBP ring  

A set of substrate bond pads aligned along an SBP guide. A substrate bond pad belongs to the ring on which it is aligned. In creating a wire bond fanout, you assign each component bond pad to a specific SBP ring.  

## schematic-driven design  

The “standard” PCB design process, in which a netlist is first created in a schematic tool, and then passed to a layout tool, where the parts are laid out on the board and the connections routed. See also layout-driven design.  

## scribe line or saw line  

The separation between adjacent dies on the wafer. This path is used as the cutting area in sawing a wafer into the individual dies.  

## search  

To locate specified information. One search method is to use the Find command.  

## secondary component side  

The side opposite the mounted side for through-hole components. This side is typically wave soldered.  

See also primary component side  

## secondary objects  

Secondary object groups break primary objects into a more detailed hierarchy. You can add individual items to and remove individual items from secondary groups. Secondary objects include:  

net class   
pin pair group   
conditional rule   
matched length net group   
matched length pin pair group   
differential pair  

## seed  

A part used by Cluster Placement, during cluster building, to search outward for other parts to add to the cluster.  

## segment  

A single drafting line, path, or trace, defined by a beginning x/y coordinate and an ending x/y coordinate.  

## segmentation fault  

The termination of a SailWind product due to a system crash or illegal instruction executed.  

## Select All  

The Edit menu command that lets you select all items of a type specified in the Selection Filter. This option is also accessible from the shortcut menu when nothing is selected.  

## select mode  

Point to the object and click the left mouse button. Select the command to perform on the object.  

## selecting  

To highlight an object for editing, moving, viewing properties, or deleting.  

## selection filter  

The dialog box inhibiting or enabling the selection of specific items.  

## serpentine route  

A route that connects an any-angle coupling trace and a BGA pad, forming a snake-like pattern as it travels through the BGA.  

## session log  

Information on the current session that appears in the Status tab of the Output window.  

## shape  

The Selection Filter setting that enables or disables selection of an entire geometric object, not just its individual segments.  

## shared libraries  

Libraries that can be accessed by more than one user across a network.  

## shielding  

Specifying that one net be routed around another to provide protection from interference.  

## shortcut keys  

A key sequence that starts a command directly from the keyboard and without navigating through menus.  

## shortcut menu  

A menu listing the possible actions to perform, based on the selected object.  

## shoulder  

The part of the differential pair trace between the source pin and the gathering point, or between the split point and the destination pin.  

![](/images/1797747ffec81fb8beff335ea28bdec4123b33934d9f836d3730acc6f78d7a85.jpg)  

See also differential pairs, gathering point, split point.  

## signal  

Voltage or current that is transferred between component pins by an electrical conductor.  

## signal pins  

Pins that have a signal net, such as GND, assigned by the schematic capture program SailWind Logic during part type creation.  

## signal via  

Via used to continue a signal from one layer to another.  

## silkscreen  

An artwork layer containing the reference designator and component outline of all parts, used for the final board fabrication process.  

## single-sided board  

A design where all pads, routing, and parts are placed on one side of the board.  

## single-sided die  

A die that has substrate bond pads and a BGA grid array on the same side of the die.  

See also documentation layers  

## sizing handles  

Small, black squares that appear at the corners and along the sides of a rectangular area that surrounds a selected nontext object.  

## sketch route  

A SailWind Layout command that reroutes existing traces by enabling you to draw a new route path using the pointer.  

## slice  

Another term for wafer.  

## slotted holes  

Oval holes in a printed circuit board, which may be plated or non-plated.  

## SMD  

An acronym for Surface Mounted Device: the pin of a component that is attached to the PCB only on an outer surface and does not require drilled holes for component mounting.  

## smoothing  

A command that automatically removes unneeded corners and segments and centers trace patterns between route obstacles.  

## SMT  

An acronym for Surface Mount Technology.  

## snap modes  

Various modes, available during dimensioning, that force the pointer to pick points based on of the following parameters: intersection, any point on a line, any point in space, entire segments, the center point of an arc, and so on.  

## soft rule  

A rule that is ignored if it alone prevents route completion. See also hard rule, and Hard and Soft Rules, in the SailWind Router User Guide.  

## SOIC  

An acronym for Small-Outline Integrated Circuit.  

## solder  

A metal alloy used to attach each pin of a device to a printed circuit board.  

## solder dam  

A small amount of solder mask used to limit molten solder from spreading further onto solderable conductors, in an area where solder mask is purposefully absent.  

## solder mask  

The artwork layer for a nonconductive material that covers the entire board, except for pad locations. The solder mask provides a protective covering and prevents shorts during wave and reflow solder processes.  

## solder mask reliefs  

Some components have large areas that need to dissipate heat. Others have large metallized areas (that are not pins) that need to be soldered to the board. To expose the copper area beneath these parts for soldering, the solder mask layer must have a cutout representing these areas. These cutouts are called solder mask reliefs. When the distance between pads of a fine pitch component is too small, the webs or fingers of solder mask between pads can break and wander on the board surface. To prevent this, a solder mask relief is applied to entire pad areas of a component. This is commonly called gang relief or a gang opening.  

## solder side  

The back or bottom side of a printed circuit board. Solder side is named for the post assembly process, where the board is run through a special bath to solder all pins.  

## source  

A pin type that indicates a signal radiating from the pin.  

## SPECCTRA  

The product name for the Cadence Design Systems autorouter.  

## special symbols  

Alternate decals that you specify as connectors. You can associate a logical pin type with each alternate to provide a graphical indication of the connector pin function in a schematic.  

## spider bonding  

A method of connecting an integrated circuit die to its package leads. A lead frame is placed over the chip and all connections are made by just one operation of a bonding machine. TAB methods use this approach to interconnection.  

## spin  

The command that rotates a component or object around its axis or selection point.  

## split  

The command that creates a new corner at the pick point of the selected trace, enabling it to be rerouted.  

## split plane  

A solid copper plane layer divided into two or more sections to isolate electrical signals from each other.  

## split point  

The point near the destination pins where differential pair traces are no longer routed together and where the traces are routed individually to completion.  

![](/images/c92c3d0ed9d6f981b189d6a2354e2c73e4c7364bdfc76ae91d4d014c27aef36d.jpg)  

See also differential pairs, pair routing gap  

## ssiact.exe  

A program used to recommend set statement settings to properly adjust port access times for a security key.  

## stackup  

The metal and dielectric layers used to implement the body of a printed circuit board. A signal metal layer carries signal traces. A plane metal layer is tied to a DC voltage. A dielectric layer is made from non-conducting material and separates two metal layers or coats the board surface.  

## start zone  

The part of the differential pair between the source pins and gathering point.  

![](/images/4404b6fd9f2ca203687c104fb285be1c3a6fc3cd0cd4ab6c4e17a77999cc28a5.jpg)  

See also differential pairs, gathering point  

## starting layer  

The first layer in a drill pair or via definition.  

## step-by-step mode  

A mode in which the debugger runs a single line of code at a time.  

## stitching vias  

Any SMD via, through-hole via, or partial via added to nets (on traces or within plane areas) in a repetitive manner. You can add these vias, also called free vias, for various purposes, including current and thermal needs. For example, you can place stitching vias in a plane area to provide conduction between two plane areas. You must assign stitching vias to a net, but they do not have to have traces attached to them.  

## strategy  

A set of options that defines how a board should be autorouted.  

## strong  

Places cluster members as close together as possible during placement operations. The minimum distance for placement is the same as the distance for part clearances in Design Rules.  

## structured attributes  

Attributes that are related to each other by the prefix in their name. For example, the DFT attributes such as DFT.Nail Count Per Net, DFT.Nail Number, and DFT.Nail Diameter are structured attributes. Together, these structured attributes make an attribute group.  

## stub  

A trace that enters another to create a T-junction. Stub lengths can be checked by the EDC program.  

## submicron  

Dimensions smaller than one micron.  

## subnet  

A collection of all traces and vias connecting two pins. Subnets are joined only through their common component pins and not through other nodes, such as a trace junctions, vias, or virtual points.  

Subnets help to avoid errors or confusion caused when pin pairs of a net have unique, rather than common, design rules.  

See also node, subnet, connected islands, virtual point.  

![](/images/f7fb2f90c3c4bc3ea908665d19d2242a6cd17113beb8e5a391fa78f21853728b.jpg)  
Figure 162. One subnet in a net  

## subnets  

If a net has at least one pin pair with a unique design rule, such as a trace width difference, the net is automatically divided into subnets. If two pin pairs having the same rules are separated by at least one pin pair with different rules, the pin pairs are considered separate subnets. Therefore, subnets are islands of pin pairs that form an unbroken fragment within the net, where each fragment has uniform rules.  

See also differential pairs, differential pairs.  

![](/images/e894363830f043720af185bfd66378c97384eb6c414b9e05b9bc6ffb6d4254f0.jpg)  
Figure 163. Multiple subnets in a net  

## substrate  

A material between copper laminate layers that comprise a laminate pair, or a laminate set in the case of completed multilayer boards.  

## substrate bond pads  

Copper areas on the substrate to which a die's wire bonds are connected.  

## surface mount device  

Pads are glued to the board rather than inserted.  

## swap file  

The file created when a program runs out of RAM memory and writes memory to disk.  

## swapping  

A placement optimization process that exchanges pins, gates, or entire parts.  

The product .ini file entry that specifies the path for the SailWind product configuration files.  

## system attribute  

An attribute that is set by, used by, and critical to a SailWind product, an external program, or Automation script (such as Sax Basic). You cannot modify the properties of a system attribute or modify the Attribute Dictionary entry for a system attribute.  

## system toolbars  

System toolbars are specific to the SailWind programs. They feature several system toolbars, such as standard, routing, selection filter.  

## SystemDir  

The product .ini file entry that specifies the path for the SailWind product configuration files.  

## T junction  

A trace that branches into another.  

## TAB  

An acronym for source.  

## tacks  

Small, diamond-shaped objects that anchor traces to their current location. Tacks are automatically generated under certain conditions and may also be manually added to a selected trace.  

![](/images/acdcc625d17a09a05a309bf7442289a538f0efbdae13b5baa9a730181031ce05.jpg)  

## tandem traces  

Traces on different layers that are checked for running parallel to each other.  

The traces are subject to crosstalk if they run parallel to each other too long and the gap between them is too short.  

## Tape Automated Bonding (TAB)  

A packaging method where silicon chips are joined to patterned metal traces, or leads, on polymer tape to form inner lead bonds which are attached to the next level of the assembly, typically a substrate or board.  

## Tape Ball Grid Array (TBGA)  

A TAB packaging method in which tape automated bonding leads are replaced by a ball grid array.  

## TBGA  

An acronym for Tape Ball Grid Array (TBGA).  

## teardrop  

A triangle shape that provides a smooth transition from a trace to a pad.  

## tented vias  

Vias that are covered by solder mask on both sides of the board to seal the hole and protect it from wave solder.  

## terminal  

The electrical center of a pin, as defined in the part decal.  

## terminator  

A pin type for high-speed circuit configurations that indicates a terminating resistor to match impedance of the trace. Terminators are used to reduce signal reflections that cause poor circuit performance.  

## test point  

A test point is a group of objects that serve as a contact between the electrical element of the board and the probe of the testing device. A test point can also be a point on a node of a net, component pin, or via. Test points can also be a point on an unused component pin, such as a component pin that is not incorporated into any net.  

When the via or pin is flagged as a test point, and Show Test Points is checked on the Routing tab of the Options dialog box, a down arrow symbol is drawn on the via or pad in the design:  

![](/images/11718e90e0cd893adf71d29fb6ed057eeb9367ab03ac9a9a3e234b3f30deb5fc.jpg)  

## test point pass  

This autorouting pass analyzes the testability of the design, determines which nets require testing, adjusts the routes, and inserts test points to improve testability. You can select whether to add test points during routing or after routing.  

## testpnts.fmt  

An ASCII file containing information about test points, including the test point name, the signal name, and the x/y coordinates. The report file generator creates this file.  

## thermal  

A multi-spoke connection of a through hole pin pad, via, or surface mount pad to a copper plane.  

## thermal compression bonding  

A method of wire bonding that does not use an intermediary metal or melting, but rather the flow of materials resulting from the combination of heat and pressure. It is also referred to as thermocompression bonding.  

## thermal relief  

A spoke-shaped pattern that connects a via or pin, in the same net as the copper plane, to the surrounding copper. Thermal reliefs provide good pin soldering by preventing heat from dissipating throughout the plane layer.  

## thermal via  

Via used to dissipate heat from an area or component.  

## thick-film process  

A hybrid microelectronic process where conductors, insulators, and passive components are screened from special pastes onto the substrate.  

## thin-film process  

The use of deposited films of conductive or insulating material, which may be patterned to form electronic components and conductors on a substrate or used as insulation material between successive layers of components.  

## three-state check box  

A three-state check box helps to identify the state of the check box in a collection of objects.  

| Check box | Description                                                                                                  |
|-----------|--------------------------------------------------------------------------------------------------------------|
|           | Cleared check box. The item or collection of items all have the check box in the cleared or unchecked state. |
| 中         | Selected check box. The item or collection of items all have the check box in the selected or checked state. |
|           | Indeterminate or mixed state check box. The collection of items have different states of the check box.      |

## through holes  

Although there are non-plated through holes, this term is used interchangeably with plated through holes. It indicates that the hole has internal plating. There are two basic types of components that can be placed on a circuit board: Surface Mount Technology (SMT) where the parts are soldered to the surface of the board, and through hole (TH) components, where the components have wire leads that are soldered into plated holes that go through the board (sometime written as thru-holes).  

## through-hole via  

A via that passes through all electrical layers of the PCB design (as opposed to a partial via).  

This is sometimes also called a through via.  

## tooling holes  

Every board requires at least two tooling holes that the blank board manufacturer uses for layer alignment purposes during the manufacturing process. If you do not include them in the design, the manufacturer will add them to the board. Tooling holes are typically .125" non-plated holes with a tolerance of $+/-.002"$ . If the board is so small that the tooling holes will not fit, the manufacturer will add them to an area outside of the board outline. (These would typically get removed after final assembly.) There are two types of tooling holes: board tooling holes and panel tooling holes. Most boards are manufactured by stepping and repeating the single board image onto a larger panel so that multiple boards can be processed on a single panel. So, the board tooling holes are used for alignment purposes for individual boards, while the panel tooling holes are used for alignment of the entire panel during the manufacturing and assembly processes.  

Use the Decal Editor and the Pad Stacks dialog box to create tooling holes. Save the singleterminal object as a part to the library for reuse.  

See also Editing Pad Stacks  

## ToolTips  

ToolTips appear below buttons and provide a command name or description for the buttons.  

## topology  

The pattern of the trace and the order in which to connect pins in a net.  

## total length  

The current routed length plus the total Manhattan length for remaining unroutes of the electrical net or pin pair. Includes half the Discrete length value of each connected pin of components that have a Discrete length assigned.  

Total length is reported for pin pairs when all the following are true: length rules are defined for the pin pair, the electrical net is a high-speed net, and copper sharing is disabled.  

If pin pair rules are reported, the estimated total length of the pin pair is shown; otherwise, total length for nets is reported.  

## trace  

A line segment that represents physical etch. A trace can appear as a single pixel line or as a double line to indicate its actual width.  

## trace corner  

The vertex at which two trace segments are joined. A trace corner can also be the endpoint of a partially routed trace. The trace segments may be in line.  

![](/images/0e9f337b449e71208839841eca67275bf1a1283dd7523c11388df90a2445d4bd.jpg)  

## trace paths  

A continuous sequence of trace segments in the same trace on the same layer. Paths start and end at nodes, and cannot pass through a node.  

## trace segment  

One section of a trace. A trace segment has one starting point and one ending point. A trace segment can be arced.  

![](/images/f73b8d01e961af85bc6f80fbbcda2c089e773334d3fba53a9aa63dfd448c7e12.jpg)  

Trace segments are contiguous when they are joined end to end, in one continuous path, and belong to the same trace.  

![](/images/9c5a56ff8eea9033e1f755c54567189047b0a0b385052a6054ca65ebcc176f9c.jpg)  

## transparent layers  

The mode that displays layers in a see-through mode so you can view multiple objects stacked upon each another. This is the modeless command T.  

## TrueLayer  

The default mode of operation in SailWind Layout whereby an object on a documentation layer moves with a component if the component is moved from one side of the board to the other. For example, when you place a component on the top layer of the board, the reference designator of that component is visible on the Silkscreen Top layer (the documentation layer associated with the top layer of the board). Moving the component to the bottom side of the board automatically moves the reference designator for the component to the Silkscreen bottom layer.  

TrueLayer also correctly plots paste masks of documentation-level pad shapes in CAM. The layer that the definitions move to is set in the Component Layer Associations dialog box.  

By default, TrueLayer mode is enabled. To disable it, use the /NTL command-line switch. See Software Launch Options.  

## TTL  

Acronym for Transistor-Transistor Logic.  

## tune pass  

This autorouting pass adjusts the length of length-controlled traces. The pass examines trace lengths for only completely routed nets or pin pairs. The pass analyzes the current length of each net or pin pair if length rules and length control are enabled, based on the following conditions:  

• If the cumulative length of the adjacent trace segments is within the range of minimum and maximum trace length, the tune pass skips the trace and does not adjust it.   
• If the trace is longer than the maximum trace length, the tune pass rips it up and places it in a queue for routing.   
• If the trace length is less than the minimum trace length, the tune pass changes the length by adding accordion patterns.  

## ultrasonic bonding  

A wire bonding technique that uses ultrasonic energy and pressure to form the bond without heat.  

## underfill  

Material injected under the die to ensure interconnect reliability against #unique_1408 mismatch between the die and the substrate in a flip chip configuration.  

## undo  

A command that enables you to remove the effects of the last command invoked.  

## undock  

To isolate an application dataset from the main design project so it can be edited regardless of the network or the physical location of the dataset. The isolated dataset has no dependence on the main design project.  

## UndoMemorySize  

The SailWindpcb.ini file entry that limits the maximum size of the buffer that is used to store ECO operations for Undo.  

## unions  

Parts assigned to each other in fixed relative positions using Cluster Placement. These positions are maintained whenever a union is moved in Cluster Placement. A common example is the relationship between bypass capacitors and ICs.  

## units of measure  

A commonly used set of measurements.  

## unroute  

To convert a trace back into a connection.  

## unrouted length  

The trace length monitor calculates unrouted length as the distance from the endpoint of the current trace segment (attached to the pointer) to its destination.  

The unroute length calculation depends on the current routing angle:  

| Routing mode: | The calculation:                                              |
|---------------|---------------------------------------------------------------|
| Orthogonal    | Manhattan Length                                              |
| Diagonal      | The length of the shortest diagonal path between unroute ends |
| Any Angle     | Point-to-point distance                                       |

The unrouted length is recalculated as the unroute dynamically reconnects to connection points.   
The routing angle also effects this calculation.  

See also routed length, estimated total length  

## unroutes  

Thin, straight segments joining pins or coppers to indicate connectivity. Also called a link.  

## unused pins  

Pins that are not connected to a net.  

## UserDir  

An .ini file setting that specifies the path for SailWind product configuration files.  

## verb mode  

Start a command by attaching a command to the pointer and then selecting objects to which you apply the command.  

You can enter verb mode by selecting a command when no objects are selected. A small V attaches to the pointer to show that the selected command is active. The command remains attached to the pointer until you cancel verb mode.  

See also object mode  

## vertex  

A single point in the work area, defined by x and y coordinates.  

## via  

A drilled and plated hole that passes conductivity from one layer to another.  

## via pair  

A pair of vias used to change the routing layer for a differential pair when routing the controlled gap area.  

See also via, differential pairs.  

## via type  

A via or virtual pin padstack definition that is defined and named in SailWind Layout in the Pad Stacks Properties dialog box.  

## victim net  

Nets that are interfered with by those tagged as aggressor nets during High-Speed or Electrodynamic Checking.  

## virtual memory  

Writing memory areas to disk in the form of a swap file when RAM is filled. The size of the swap file is based on the free disk space or the limits imposed by the operating system.  

## virtual pin  

A net object that, like a component pin, serves as a pin pair end, but uses the pad stack of a via.   
The pad stack can be through-hole or partial, or it can be a single-layer pad.  

## virtual point  

A point along a trace segment that identifies a change in design rules, usually between trace rules and component rules. Virtual points are inserted into nets automatically when necessary, usually during autorouting operations. You cannot create, position, or otherwise edit a virtual point.  

See also subnets  

## Visual Basic  

Visual Basic is a scripting language developed by the Microsoft Corporation to enable users to customize applications using a standard scripting language.  

## visual editing  

Visual Editing occurs when the source application for a linked or embedded OLE object opens within the container application.  

## wafer  

A thin disk of semiconductor material (usually silicon) on which many separate chips can be fabricated.  

## wafer sort  

The electrical testing of each die on the wafer while still in wafer form.  

## WB  

An acronym for wire bond.  

## wedge bonding  

A form of thermal compression wire bonding where the bond shapes the wire into a wedge shape.  

## width  

The thickness of a trace or line.  

## wire bond  

Fine wires, usually aluminum or gold, connecting the bonding pads on a die to the component package.  

## Wire Bond Editor  

The Wire Bond Editor opens (explodes) a selected die part, so you can move, add, delete, and edit individual component bond pads and wire bonds in addition to substrate bond pads. You can also edit the die size.  

## wire bond fanout  

A pattern of wires (typically gold) that arc out from component bond pads to substrate bond pads to provide connectivity between the die pins and the substrate package pins.  

## Wire Bond Wizard  

A BGA toolbox feature that creates and places substrate bond pads and generates an automatic wire bond fanout between component bond pads and substrate bond pads.  

## wire bonder  

The machine that connects wires between the chip bond pads and the substrate bond pads.  

## wire bonding  

The process of electrically connecting a chip to the next level package with fine wires. The wires are either gold or aluminum.  

## workspace  

The actual work area where a design is created.  

## yield  

The ratio of the number of acceptable units to the maximum number possible.  

## Z routing pattern  

A collection of routes that form a pattern resembling the letter Z.  

![](/images/ba0b725246783e1e28021a61e3cdbd38483cce02c2db1cdf697931396e627300.jpg)  

## zoom  

Modifying the view to make objects appear larger or smaller. Zooming in or out affects the amount of what can be viewed in the work area.  

See also protect.  

