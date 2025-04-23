# Chapter 16 Rules

As your design complexity increases, you can use design rules to control the interaction of various design objects with one another. Use design rules to specify clearances between design objects such as pads, coppers and traces. You can also specify design rules for nets, groups of nets, classes, and differential pairs. Use the Rules Report to review your settings. You can also import and export rules between your schematics and your PCB designs.  

Rules Setup   
Setting Up Clearance Rules   
Same Net Matrix   
Routing Rules   
Setting Up High-Speed Rules   
Setting Up Rules   
Rules Hierarchy   
Setting Up Default Rules   
Setting Up Class Rules   
Setting Up Net Rules   
Setting Up Conditional Rules   
Creating Differential Pairs   
Differential Pair Layer Hierarchy   
Creating a Rules Report   
Import Rules from PCB   
Export Rules to PCB  

# Rules Setup  

Design Rules enable you to assign general routing constraints for your design, such as trace width and spacing. An option in the netlist lets you pass established design rules along with the connectivity and parts information to SailWind Layout.  

To access and examine the Design Rules setup, click the Setup $>$ Design Rules menu item.  

# Rule Categories  

Design rules are separated into three categories:  

Setting Up Clearance Rules — Specifies minimum allowable airgap between various object types in the design; trace to trace, via to trace, etc.   
Routing Rules — Assigns or prohibits via types, specifies length minimization types, or allows or prohibits routing.   
Setting Up High-Speed Rules — Specifies minimum and maximum parameters for advanced design rules such as parallelism, delay, capacitance, and others.  

Information for each category is entered and edited in a separate dialog box that you can access through the Design Rules command from the Setup menu.  

# Setting Up Clearance Rules  

Use the Clearance Rules dialog box to define the spacing permitted between objects. When objects are imported, the On-line DRC and Verify Design programs use these rules to check and report clearance violations.  

![](/images/a3968254a66dc45482abf925f25b15eb2d818dc495708bbbd0c495061b025492.jpg)  

!Tip  

You can use the Setting Up Conditional Rules dialog box to save a clearance configuration as a set, to apply to a selected item only when it comes in contact with different level of the hierarchical order on page 305.  

**Procedure** 

. Click the Setup $>$ Design Rules menu item, click a rule hierarchy, then click the Clearance button.  

2. In the Same Net area, define edge-to-edge clearance values between items that are in the same net: To define the minimum spacing between any two objects, type the value in the appropriate text box. To define the same spacing value for all text boxes in one matrix column, press the button above the column and type a value. • To define the same spacing value for all text boxes in one matrix row, press the button in the left column and type a value. To define the same spacing value for all text boxes in the matrix, press the All button and type a value.  

Table 33. Clearance Rules - Same Net - Edge-to-Edge Clearance Options   


<table><tr><td>Clearance</td><td>Description</td></tr><tr><td>SMD to Via</td><td>Minimum spacing between a surface mount pad and escape via.</td></tr><tr><td>SMD to Corner</td><td>Minimum spacing between a surface mount pad and the first trace bend point.</td></tr><tr><td>Via to Via</td><td>Minimum spacing between two vias in the same net.</td></tr><tr><td>Pad to Corner</td><td>Minimum spacing between a through hole pad and the first trace bend point.</td></tr><tr><td>Trace to Corner</td><td>Minimum spacing between a trace and the bend point of another trace; for example, when a trace splits at a T-junction and one of the two traces has a bend point.</td></tr></table>  

3. In the Trace Width area, type values in the text boxes to restrict the trace width to a range of values:  

• In the Recommended box, type the width you want to assign to the trace when routing begins. • In the Minimum and Maximum boxes, values are respected by routing routines that must use trace width to achieve some high-speed routing functions, such as impedance matching.  

4. In the Clearance area, use the Clearance matrix to define edge-to-edge clearances between two object types:  

• To define the minimum spacing between any two objects, type the value in the appropriate text box. To define the same spacing value for all text boxes in one matrix column, press the button above the column and type a value.   
• To define the same spacing value for all text boxes in one matrix row, press the button in the left column and type a value.   
• To define the same spacing value for all text boxes in the matrix, press the All button and type a value.  

5. In the Other area, optionally set other clearance values, which include:  

Table 34. Clearance Rules - Other - Clearance Options  

<table><tr><td>Clearance</td><td>Description</td></tr><tr><td>Drill to Drill</td><td>The minimum edge-to-edge spacing between two drill holes.</td></tr><tr><td>Body to Body</td><td>The minimum edge-to-edge spacing between two component bodies.</td></tr></table>  

6. Click OK, or optionally click Delete to remove this set of Clearance rules from your rules hierarchy.  

i Tip You cannot delete the Default Clearance rules.  

# Same Net Matrix  

Use the Same Net Matrix to define edge-to-edge clearance values between items that are in the same net.  

To define the minimum spacing between any two objects, type the value in the appropriate text   
box.   
To define the same spacing value for all text boxes in one matrix column, press the button above the column. Type a value and click OK.   
• To define the same spacing value for all text boxes in one matrix row, press the button in the left column. Type a value and click OK.   
• To define the same spacing value for all text boxes in the matrix, press the All button. Type a value and click OK.  

Table 35. Same Net Matrix - Clearance Options   


<table><tr><td>Clearance</td><td>Description</td></tr><tr><td>SMD to Via</td><td>Minimum spacing between a surface mount pad and escape via.</td></tr><tr><td>SMD to Corner</td><td>Minimum spacing between a surface mount pad and the first trace bend point.</td></tr><tr><td>Via to Via</td><td>Minimum spacing between two vias in the same net.</td></tr><tr><td>Pad to Corner</td><td>Minimum spacing between a through hole pad and the first trace bend point.</td></tr><tr><td>Trace to Corner</td><td>Minimum spacing between a trace and the bend point of another trace; for example, when a trace splits at a T-junction and one of the two traces has a bend point.</td></tr></table>  

# Routing Rules  

Use the Routing Rules dialog box to specify rules for interactive and automatic routing. You can specify the default set of routing rules and routing rules for specific nets.  

# Setting Up High-Speed Rules  

Use the Hi Speed Rules dialog box to define rules for Parallelism, Tandem, Shielding, Routed Length, Stub Length, Delay, Capacitance, Impedance, and Matched Length.  

![](/images/e3c417e82666cad6fb7d4dcfe9d62c7e900943403d416c6b82cb7c421302b0d0.jpg)  

!Tip  

When working with high-speed rules, observe the following:  

• When imported into SailWind, the EDC (Electrodynamic Checking) routine checks to see if rules are met correctly after routing (except shielding and matched length). • You can use the Setting Up Conditional Rules dialog box to save a high speed configuration as a set, or to apply for a selected item only when it comes in contact with different level of the hierarchical order on page 305.  

**Procedure** 

1. Click the Setup $>$ Design Rules menu item, click a rule level, then click the Hi Speed button.  

2. In the Parallelism area, type a value for length and gap in the parallelism boxes to restrict the distance that traces in different nets on the same layer can run together.  

3. Type a value for length and gap in the tandem boxes to restrict the distance that traces in different nets on different layers can run together.  

Table 36. High-Speed Rule Options   


<table><tr><td>Option</td><td>Description</td></tr><tr><td>Parallelism</td><td>Restricts the distance that traces in different nets on the same layer can run together.</td></tr><tr><td>Tandem</td><td>Restricts the distance that traces in different nets on different layers can run together.</td></tr></table>  

!Tip  

When configuring High-Speed Rule Options, observe these guidelines:  

• These values determine the distance and standoff against the specific item and everything else in the design. To set a narrower check, use Setting Up Conditional Rules to define specific Source and Against items.   
• Length defines the maximum allowable parallel/tandem distance.   
• Gap defines the minimum gap between traces below which the parallel/tandem rules apply.  

4. Click Aggressor to specify if a net is an aggressor, or source of interference, during parallel/tandem checks.  

5. In the Rules area, type minimum and maximum values for:  

Table 37. High-Speed Rules - Minimum/Maximum Values   


<table><tr><td>Rule</td><td>Description</td></tr><tr><td>Length</td><td>Defines a minimum and maximum length.</td></tr><tr><td>Stub Length</td><td>Specifies a maximum stub length. The stub length is the distance from a T-point to the end of the route.</td></tr><tr><td>Delay</td><td>Defines a minimum and maximum delay time in nanoseconds.</td></tr><tr><td>Capacitance</td><td>Defines a minimum and maximum capacitance in picofarads.</td></tr><tr><td>Impedance</td><td>Defines a minimum and maximum impedance in ohms.</td></tr></table>  

!Tip  

These text boxes restrict the trace width to a range of values. Recommended is the width you want to assign to the trace when routing begins. The Minimum and Maximum values are respected by routing routines which must use trace width to achieve some high-speed routing functions, such as impedance matching.  

6. Some routers can arrange certain nets as shielding others if requested; the Net in the Use Net list box is routed up and down both sides of a selected net to provide protection from interference. In the Shielding area, click Shield to invoke the shielding rules.  

![](/images/51d88669a7e4b3c1408b8463f7bbf6dd337c5ed1dcb53d4e1e39ea753736a993.jpg)  

!Tip  

When working with shielding, observe the following guidelines:  

• You can only assign nets associated with plane layers in the Layer Definition dialog box to shield other nets. If there are no plane layers, the Shield area is grayed out. • If your router supports shielding, you can specify the shield gap value and net to use as the shield in the Gap and Use Net text boxes.  

7. (Optional) In the Matching area, select the Match Length check box to invoke the matching rule, and type a tolerance value.  

![](/images/2308363060851c401fe749e423fab2d30ff8f2fc2028196b1c1d4d87e5deffde.jpg)  

!Tip  

When working with Length Matching, observe the following:  

• Length Matching is a same length requirement parameter you can pass on to autorouters that support it.   
• This rule specifies the maximum difference allowed between the shortest length and longest length in the matched length group.  

8. Click OK, or click Delete to remove this set of High Speed rules from your rules hierarchy.  

0 Tip You cannot delete the Default High Speed rules.  

# Setting Up Rules  

Use the Rules dialog box to enter item-to-item Clearance rules, routing guidelines, and values for the optional High Speed checking commands. You can also indicate the unit of measure for passing rules to SailWind Logic: mils, metric, or inches.  

**Procedure** 

1. Click the Setup $>$ Design Rules menu item.  

2. In the Units list box, select Mils, Metric, or Inches.  

3. Select the rules hierarchy level for which you want to set or modify rules.  

!Tip  

When you specify one of the hierarchical levels, you can access the Clearance, Routing, or High Speed forms.  

4. Click the appropriate button to define rules for a particular level in the hierarchy.  

5. (Optional) Click the Report button to access the Rules Report dialog box where you can select a default report of a report for some or all of the rules you have defined.  

# Rules Hierarchy  

In the rules hierarchy, certain rules have precedence over other rules. For example, a net rule overrides a class rule, and a class rule overrides a default rule.  

Table 38. Rule Hierarchy and Order of Precedence   


<table><tr><td>Rules</td><td>Precedence</td><td>Description</td></tr><tr><td>Setting Up DefaultRules</td><td>Least</td><td>Rules that apply to an object if there are no other individually defined rules.</td></tr><tr><td>Setting_ Up Class Rules</td><td></td><td>Rules for a collection of nets, called a class, which needs identical rules.</td></tr><tr><td>Setting Up Net Rules</td><td>Highest</td><td>Rules for a specific net.</td></tr></table>  

# Rules Hierarchy Order of Precedence  

The complete order of precedence for all rules follows, from least to most specific. Default, 1, represents the lowest level of the hierarchy with the least amount of precedence. At the opposite end of the order is Net against Net with Level, which is the highest level of the hierarchy and has the highest possible precedence. It represents the most specific rule you can assign to an object in SailWind Logic.  

1. Default   
2. Default with Level   
3. Class   
4. Class with Level   
5. Net   
6. Net with Level   
7. Class against Class   
8. Class against Class with Level   
9. Net against Class   
10. Net against Class with Level   
11. Net against Net   
12. Net against Net with Level  

See also Setting Up Default Rules, Setting Up Class Rules, Setting Up Net Rules, Creating a Rules Report.  

# Setting Up Default Rules  

Use the Default Rules dialog box to define rules which apply to all objects that are not included in any other rule definitions within the hierarchy.  

**Procedure** 

1. Click the Setup $>$ Design Rules menu item, then click the Default button.   
2. To define default Clearance on page 300, Routing on page 302, or High Speed on page 302 rules, click the appropriate button.   
3. Click the Report on page 310 button to produce a rules report.  

# Setting Up Class Rules  

Use the Class Rules dialog box to define rules that apply to a collection of nets known as a net class and to multiple net classes.  

**Procedure** 

1. Click the Setup $>$ Design Rules menu item, then click the Class button.  

2. In the Class Name list box, select a class name, or specify a new name for which you want to apply rules.  

!Tip  

The Class list box defines net classes by name and parenthetically notes the rules that apply, if any, to the class.  

3. In the Nets area, add or remove selected nets from the net class as follows:  

Select a class in the list box to display nets in the Available and Selected list boxes, or click the Add button to create a new class. • To assign nets to a class, select the net(s) in the Available list box and click Add.  

![](/images/171b74974b5240b4e5e91a864a831231e2ed880b36367cfb86146961ef06c460.jpg)  

Tip   
A net can only belong to one net class. The Available list box only contains nets that do not belong to a net class.  

4. To delete nets from the class, select the net(s) in the Selected list box and click Remove.  

5. (Optional) Select a class name and click Rename to change the class name for the selected class.  

6. (Optional) Select the Show Classes with Rules check box to list only classes with at least one set of rule definitions.  

7. For each class, click the appropriate button to define Clearance, Routing, or High Speed rules for a net class.  

![](/images/5a3835099e88e3ee229a67cfbec1aede00ae6660b007243ac0c52422ca2c919f.jpg)  

!Tip  

When you select a class name, an icon appears below each rule type to indicate the hierarchy level where the rule is defined for that class. For example, a class with only Clearance rules defined would have a Class icon below the Clearance icon and Default icons below the Routing and High Speed icons.  

8. In the corresponding Rules dialog box that displays, supply values for the rules you want to apply, and click OK to return to the Class Rules dialog box.  

9. When you have finished defining all class rules, click OK.  

# Setting Up Net Rules  

Use the Net Rules dialog box to define rules that apply to a single net or multiple nets.  

**Procedure** 

1. Click the Setup $>$ Design Rules menu item, the click the Net button.  

2. Select the net(s) for which you want to define Clearance on page 300, Routing on page 302 and High Speed on page 302 rules.  

![](/images/5d6467ed41a27b1635eb413319eacb76682e7fb9357b9a5478a34e3358e02633.jpg)  

!Tip  

When you select a net name, an icon appears below each rule type to indicate the hierarchy level where the rule is defined for that net. For example, a net with both Clearance and High Speed rules defined would have Net icons below the Clearance and Hi Speed icons and a Default icon below the Routing icon.  

3. (Optional) Select the Show Nets with Rules check box to list only those nets with at least one set of rule definitions.  

4. (Optional) Click the Report button to view a rules report.  

5. Click the Default button to restore the net rules back to the default rules.  

# Setting Up Conditional Rules  

Use the Conditional Rule Setup dialog box to apply a third overriding set of rules that apply only when the item meets other specific levels of the hierarchical order.  

Once you set up Clearance rules for a group in the hierarchical order on page 305, the rules are applied to all other objects.  

![](/images/c5384ae91f9e55ee94020d7c8fd14886198e3eda6252a20521876db9e3f245d1.jpg)  

!Tip  

When working with conditional rules, use the following guidelines:  

• You can use a layer as an against object, where rules you set for an object such as a net apply only when the net is routed on that layer.   
• You can further refine this to use another net as an against object and specify a layer to which the rules to apply. If these two nets meet on this layer, they must adhere to this clearance. You define these relationships by making conditional rule sets.  

**Procedure** 

1. Click the Setup $>$ Design Rules menu item, then click the Conditional Rules button.  

2. In the Source Rule Object area, select Classes, Nets, or All to specify both classes and nets. Then specify the object(s) against which the rule is checked.  

3. In the Against Rule Object area, select Classes, Nets, or Layer, and then specify the object(s) against which the rule is checked.  

!Tip  

Select Layer to use a layer as an against object or to apply an item-to-item rule on a specific layer.  

4. (Optional) In the Define Conditional Objects area, in the Apply to Layer area, select a layer on which you want rules checked.  

5. In the Existing Rule Sets list box, select the rule set to define the appropriate values for specific Clearance or High Speed definition of the selected rule set.  

6. After you create a rule set, in the Current Rule Set area, define the Clearance or High Speed values.  

7. Select Clearance to enter the minimum clearance gap you want the source and against items to maintain from each other, and then click Matrix to enter more item-specific standoffs.  

8. Select High Speed to enter clearance values for parallel and tandem checking on page 302 for the condition. The source-against entries are used as the victim-aggressor designations for crosstalk conditions checking.  

9. Click Create to compile the new rule set parameters and adds a description to the Existing Rule Sets list box, or click Delete to removes the selected rule set from the Existing Rule Sets list box.  

**Related Topics**  

Setting Up Clearance Rules Setting Up High-Speed Rules  

# Creating Differential Pairs  

dentify nets or pin pairs that behave electrically as differential pairs and define rules for them. You can set different properties for differential pairs, which affects how they are routed. Differential pair properties  

determine the gap between the traces in the Controlled Gap Area, the minimum and maximum trace lengths, and how to respond to Obstacles in the controlled gap area.  

# Restrictions and Limitations  

While you can define these rules in SailWind Logic, they are used only in SailWind Router.  

**Procedure** 

1. Click the Setup $>$ Design Rules menu item, the click the Differential Pairs button.  

2. In the Available list, double-click the first net, and then double-click the second net.  

!Tip  

Nets cannot exist in more than one differential pair. The Available list displays only nets that have not been assigned to a differential pair.  

3. Click Add.  

4. Type minimum trace length value in the Minimum box.  

5. Type the maximum trace length value in the Maximum box.  

6. In the Properties of the pair area, type Width and Gap values in the <All layers> row.  

Restriction: You cannot delete the <All layers> row.  

7. To set the width and gap per layer, click Add, click in the Layer cell in the newly added row, and select the layer for which to set width and gap values. Then type Width and Gap values in the appropriate cells.  

!Note:  

When working with differential pairs, observe the following guidelines:  

• Setting the differential pair width and gap per layer enables you to better control   
impedance.   
• The gap rule cancels any other rule defining a clearance between the differential pairs. Therefore, the gap is the minimal clearance and must be provided when possible. • If you select multiple differential pairs, and a layer setting doesn't belong to all of the selected pairs, the Layer column will be unavailable.   
• If you select multiple differential pairs that have the same layer setting, but the Width and Gap values do not match, the Width and Gap cells will appear empty. You can, however, type a new value, and the new will be applied to all selected differential pairs when you click OK or Apply.  

See also Differential Pair Layer Hierarchy.  

8. Click Restrict layer changes during autorouting to force the pair to be routed on a single layer.  

This setting does not restrict layer changes when routing interactively.  

9. Click Allow pair to split around obstacles to allow routing around an obstacle in the controlled gap area by temporarily exceeding the pair routing gap.  

This setting applies to autorouting and does not restrict splitting around obstacles when routing interactively.  

10. Type the maximum number of obstacles to route around in the Maximum number of obstacles box.  

一 Tip Obstacles in the start zone or end zone are not counted.  

11. Type the maximum spacing allowed between traces around obstacles in the Maximum obstacle size box. The size applies to the obstacle's longest horizontal or vertical dimension.  

Tip Obstacle size in the start zone or end zone is not checked.  

12. Click OK.  

# Differential Pair Layer Hierarchy  

You can assign differential pair width and gap values to layers and categories of layers; however, a layer may also fall into one or more categories. For example, Layer 2 may also be a plane layer, and an outer layer.  

Therefore, the following hierarchy is followed to define which layer settings take priority:  

1. All Layers   
2. Plane Layers   
3. Outer Layers   
4. Inner Layers   
5. Individual Layers  

i Tip Individual Layers has highest priority.  

# Creating a Rules Report  

Use the Rules Report dialog box to produce a report of some or all of the rules you have defined. By default, a complete report of all rules is reported.  

**Procedure** 

Click the Setup $>$ Design Rules menu item, the click the Report button. You can produce reports for the following:  

Table 39. Rules Report Types   


<table><tr><td>Report Type</td><td>Description</td></tr><tr><td>Rule types</td><td>Displays the specified rules for the specified nets and classes. Click any combination of buttons, including Differential Pairs, to report net pairs.</td></tr><tr><td>Nets</td><td>Displays the specified rules for every net or selected nets. Click All Nets or select specific nets in the list box.</td></tr><tr><td>Classes</td><td>Displays the specified rules for every class or selected classes. Click All Classes or select specific net classes in the list box.</td></tr><tr><td>Output </td><td>Click Rule Sets to display all rules in the current hierarchy that are unique from the default rules. Click Rule Values to display all rules in the current hierarchy level, even if the values are the same as the default rules.</td></tr><tr><td>Default Rules</td><td>Displays the default rules for the specified nets and classes.</td></tr></table>  

# Import Rules from PCB  

Use the Design Tab of SailWind Layout Link to read design rules from a specified SailWind ASCII file, including layer setups and layer counts, etc.  

**Procedure** 

1. Click the Tools $>$ SailWind Layout menu item.   
2. Click the Design tab.   
3. On the Design tab, select the Compare Design Rules check box.   
4. Click ECO from PCB.  

The netlist in the current SailWind Logic schematic is compared to the part and netlist in the current SailWind Layout design and the schematic is updated.  

# Export Rules to PCB  

Use the Design Tab of SailWind Layout Link to export design rules to a specified SailWind ASCII file, including layer setups and layer counts, etc.  

**Procedure** 

1. Click the Tools $>$ SailWind Layout menu item.   
2. Click the Design tab.  

3. On the Design tab, select the Compare Design Rules check box.  

# 4. Click ECO to PCB.  

The netlist in the current SailWind Logic schematic is compared to the part and netlist in the current SailWind Layout design and the layout design is updated.  

