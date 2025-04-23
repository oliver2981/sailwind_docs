# Chapter 23 Crash Detection, BMW and BLT  

If unexpected behaviors occur with the application, you can use crash detection to capture the crash event. You can then use the Basic Media Wizard and Basic Log Test tools to analyze the event and better understand the circumstances that may have caused the crash. You can capture all of this data into a log file that can be forwarded to SailWind Technical Support for further analysis and support.  

Crash Detection   
BMW and BLT   
Session Log Files   
Session Media Files   
Replaying Session Playback Media With BLT   
The /BMW Command Line Switch   
Scripting and Macros  

# Crash Detection  

The Error Detected dialog box opens at a crash and enables you to save a report of the SailWind environment as well as pertinent files into a compressed Dump File for troubleshooting.  

This Error Detected dialog box is inaccessible unless the software crashes and crash detection is enabled in the software .ini file.  

Crash detection is controlled by the CrashDetection switch in the.ini file; it is turned off by default.  

• If no CrashDetection switch exists in the.ini file or if, in the [General] section of the.ini file, the switch exists with a value of 0 (zero), then crash detection is turned off. No report is created of the environment at the time of the crash. If the CrashDetection switch exists in the [General] section of the.ini file, or if the switch exists with a value of 1, then crashes are detected and the Error Detection dialog box appears.  

# BMW and BLT  

BMW (Basic Media Wizard) and BLT (Basic Log Test) are tools that you can use to record and play back SailWind Logic, SailWind Layout and SailWind Router sessions. They are particularly useful as a means of supplying information to SailWind Software Support engineers trying to identify and resolve any problematical behavior you may encounter.  

If you report problematical behavior for one of the SailWind tools to Technical Support, Tech Support engineers may ask you to use BMW to record session playback media documenting the actions that caused the problem. Tech support engineers can then replay the session with BLT to help them identify and resolve the problem.  

Creation of Session Playback Media With BMW Creating Session Playback Media for a Normal Session Automatically Creating Session Playback Media for a Crashed Session Manually Creating Session Playback Media for a Crashed Session  

# Creation of Session Playback Media With BMW  

To create session playback media, BMW session logging must be enabled when the problem occurs. If session logging was not enabled when you encountered the problem, you must recreate the actions that caused the problem in a new session with session logging enabled.  

Also, depending on whether the problem you want to document caused the SailWind tool to crash, you can create session playback media based on either the current or the immediately previous SailWind tool session.  

The following table specifies which of the procedures described below you must use to create session playback media.  

<html><body><table><tr><td>Was logging enabled?</td><td>Did the SailWind tool crash?</td><td>Then use this procedure.</td></tr><tr><td>Yes</td><td>No</td><td>Creating Session Playback Media for a Normal Session</td></tr><tr><td>No</td><td>No</td><td>Creating Session Playback Media for a Normal Session</td></tr><tr><td>Yes</td><td>Yes</td><td>Automatically Creating Session Playback Media for a Crashed Session</td></tr><tr><td>No</td><td>Yes</td><td>Manually Creating Session Playback Media for a Crashed Session</td></tr></table></body></html>  

# Creating Session Playback Media for a Normal Session  

You can use the Basic Media Wizard (BMW) to create session playback media when the session you are recreating did not cause a SailWind tool crash.  

# Procedure  

1. Start the SailWind tool, but do not open the file which you encountered the problematical behavior. (You must enable session logging before you open the file.)  

2. Type the modeless command BMW ON and press Enter to enable session logging.  

Logging remains enabled for this and all future sessions until you disable it with the BMW OFF command.  

3. Open the file in which you encountered the problematical behavior.  

4. Perform the series of actions that produced the problematical behavior.  

The series of actions, as well as changes to the board or to the configuration, are stored in the Session Log Files for the current session.  

5. Type BMW (the modeless command) and press the Enter key.  

6. In the Media Wizard dialog box, click “Create Media from Current Session”.  

7. Type your initials in the User Initials box. (They are included in the playback media filenames to identify the files as yours.)  

8. To delete all entries in the session log file between the first Open and the last Save command, click “Delete Actions Before Last Save”.  

You can do this to eliminate any actions you may have performed before beginning the series of actions that produced the problematical behavior. This makes it easier for the Tech Support engineer to identify the problem.  

9. Click OK to create the Session Media Files.  

# Automatically Creating Session Playback Media for a Crashed Session  

You can use the Basic Media Wizard (BMW) to create session playback media when the session you are recreating caused the SailWind tool to crash, and none of the listed restrictions applies.  

# Restrictions and Limitations  

• This procedure works only if the previous (crashed) session started with BMW logging already enabled and logging remained enabled throughout the session.   
• This procedure does not give useful results if any additional instance of the SailWind tool ran concurrently (for any period) with the previous (crashed) session.  

# Procedure  

1. Start the SailWind tool, but do not open the file which you encountered the problematic behavior. (You must enable session logging before you open the file.).   
2. Type the modeless command BMW ON and press the Enter key to enable session logging. Logging remains enabled for this and all future sessions until you disable it with the BMW OFF command.  

3. Open the file in which you encountered the problematical behavior.  

4. Perform the series of actions that produced the problematical behavior.  

The series of actions, as well as changes to the board or to the configuration, are stored in the Session Log Files for the current session.  

5. After the crash, restart the SailWind tool.  

A dialog box is displayed asking if you want to save media files for the crashed session. Click Yes to create the Session Media Files.  

# Manually Creating Session Playback Media for a Crashed Session  

You can use the Basic Media Wizard (BMW) to manually create session playback media when the session you are recreating caused the SailWind tool to crash, and the automatic procedure cannot be used due to one of the restrictions listed in that section.  

The automatic procedure is described in Automatically Creating Session Playback Media for a Crashed Session.  

# Procedure  

1. Start the SailWind tool, but do not open the file which you encountered the problematic behavio (You must enable session logging before you open the file.).   
2. Type the modeless command BMW ON and press the Enter key to enable session logging. Logging remains enabled for this and all future sessions until you disable it with the BMW OFF command.   
3. Open the file in which you encountered the problematical behavior.   
4. Perform the series of actions that produced the problematical behavior. The series of actions, as well as changes to the board or to the configuration, are stored in the Session Log Files for the current session.   
5. After the crash, restart the SailWind tool.   
6. Type BMW (the Modeless command) and press Enter.   
7. In the Media Wizard dialog box, click “Create Media from Previous Session”.   
8. Type your initials in the User Initials box to identify your session playback media files.   
9. Click OK to create the Session Media Files.  

# Session Log Files  

Whenever BMW session logging is enabled, two sets of session log files are maintained in the \SailWind Projects folder. These logs record actions performed in the current session, and in the immediately previous session.  

BMW names these files as follows:  

<html><body><table><tr><td>Current Session Log Files</td><td>Previous Session Log Files</td></tr><tr><td><pads_tool>_Next.log</td><td><pads_tool>_NextBak.log</td></tr><tr><td><pads_tool>_Next.reg</td><td><pads_tool>_NextBak.reg</td></tr><tr><td><pads_tool>_Next.ini</td><td><pads_tool>_NextBak.ini</td></tr></table></body></html>  

These files are dynamic; each time you start a session, the current session log files are renamed as the previous session log files, and new current session log files are created. The contents of the old previous session log files are lost.  

Whenever you elect to create session media files for a session, the appropriate set of these log files is saved in a permanent location, as described in Session Media Files.  

![](images/43062625e9a95860585f5443faefecd8708071beed68cbfce7fa37a4039ed0ab.jpg)  

Tip   
You may see a log file named <pads_tool>_Session.log listed in the \SailWind Projects folder. This file is unrelated to the session playback media created by BMW.  

# Session Media Files  

Each time you create session playback media, BMW creates a new session media folder in the \SailWind Projects folder, and copies into it:  

• The .pcb or .sch file for which you are recording the session   
• The Session Log Files for the session. BMW then renames these files based on the session media folder name.  

The session media folder is named <month><day><initials><sequential letter>, where:  

<month><day> is the date.   
<initials> are letters you type in the Media Wizard dialog box to personalize the media files. <sequential letter> is a letter automatically assigned to sequence the directories created on a specific date.  

Example: \SailWind Projects\0530jsb represents a session media folder created on May 30, using the initials js, and that was the second session media folder created on that day.  

When creating the session playback media, the following files are written to the session media folder:  

# Replaying Session Playback Media With BLT  

You can use BLT to replay session playback media created by BMW.  

# Procedure  

1. Type BLT (the Modeless command) and press Enter.  

2. Select the session playback media from the Media Directories list and click OK. The session is replayed.  

![](images/00b21778abc49d1daac1df754da5aa2382906f1bb9ed80762a11669c3498acf2.jpg)  

# Tip  

To personalize the media folder and session playback media filenames, select a media session from the Media Directories list, type the new name into the New name box, and then click Rename.  

# The /BMW Command Line Switch  

You can use a command line switch in the startup options of the software if you want to automatically record every SailWind Layout session.  

If you want BMW to automatically prompt you to create media from the previous session each time you start a SailWind tool, open the SailWind tool using the /BMW command line switch. Or use /BMW-xx (where xx represents your initials, which are used in folder and filenames to identify them as yours).  

When you use BMW as a command line option, it creates media of the previous session; use the BMW modeless command to create media of your current session.  

# Scripting and Macros  

All scripting and macro documentation has been moved into a separate manual.   
It can be found in the SailWind Logic Command Reference Manual.  