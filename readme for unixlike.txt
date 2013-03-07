Grognak's Mod Manager
http://www.ftlgame.com/forum/viewtopic.php?f=12&t=2464


About

  Grognak's Mod Manager, or GMM for short, is a program designed to
  make it easy to install multiple mods at the same time. No longer
  do you have to pack and unpack files or swap out each mod you want
  to use one at a time.


Requirements

  Python 2.6 or higher. With 3.x, there may be bugs.
    http://www.python.org/getit/

  FTL (1.01-1.03.1, Windows/OSX/Linux, Steam/GOG/Standalone).
    http://www.ftlgame.com/

  * Linux will need the python-tk package.
  * OSX may need to replace the stock Tcl/Tk from Apple.
    http://www.python.org/download/mac/tcltk/


Setup

  Extract the files from this archive anywhere.

  On the first run, you may be prompted to locate your
  FTL resources. Specifically "data.dat" in the "resources/"
  directory under your FTL install (Mac users can select FTL.app).

  In most cases, this should be located automatically.


Usage

  To add a mod (an *.ftl file) to GMM:
    Put it in the GMM/mods/ folder.

  To Start GMM:
    Double-click modman.command.

  To install mods:
    Select the mods you want to install.
    Mods at the top get clobbered by ones below. Drag names to reorder.
    Click the "Patch" button.
    (Any unselected mods will be omitted/uninstalled.)

  To uninstall all mods:
    Click "Patch" with none selected.

  If you upgrade FTL:
    Delete the outdated files in GMM/Backup/
    If you don't, the game's resources will get corrupted.


Troubleshooting

  If you get permission errors...
    Make sure that your resource.dat and data.dat files are not read-only.

  If the game shows exclamation marks for everything...
    Delete the files in GMM/Backup/
    Steam users:
      Delete the /resources directory and "verify game cache".
        https://support.steampowered.com/kb_article.php?ref=2037-QEUH-3335
    Standalone users:
      Reinstall FTL.

  Other...
    Try deleting modorder.txt from the /mods folder and relaunching GMM.


Changelog

???:
- Added a log warning during patching if a mod gets clobbered

1.7:
- Added a log warning during patching if a mod gets clobbered
- Lowered the required Python version to 2.6
- Added a Linux/Mac launcher (modman.command) to guarantee a terminal
- Added forum-scraped metadata for most mod files (based on their md5)
- Added a right-click clipboard menu to the text area.
- Added ini setting: never_run_ftl
- The ini's ftl_dats_path is ignored if it's invalid
- Added graceful exit on ctrl-c or Windows terminal closing
- Fixed data.dat/FTL.app file chooser, which sometimes left files hidden
- Fixed TclError for non-US locales with commas for decimal points
- Moved dat backups to GMM/backup/ (bak's in the old location will be deleted)
- Made the code tolerable by Python 3.x (hopefully without new 2.x bugs)
- Made the Patch/Toggle/Forum buttons expand to accomodate their text
- Added "Validate" button to check mods for problems
- Added support for appending xml files with unicode UTF-8 BOMs
- Added FTL launching under OSX
- Updated backend (un)packer to ftldat r7 (plus changes for Python 2.6/3.x)

1.6:
- GMM no longer needs to be placed in the FTL directory
- Added ini setting: ftl_dats_path
- Added drag-and-drop mod reordering
- Added "Toggle All" button
- Dats are unpacked to temp folders and deleted after patching
- Added logging
- Deprecated ini setting: macmodsdir
- Deprecated ini setting: highlightall

1.5:
- Added option to select all mods automatically (on by default, changeable in .ini)
- .ini finding improvement (by Jocelyn)

1.4.1:
- Fixed Mac and Linux support
- Fixed slight error in readme (no longer called the OK button)

1.4:
- New custom GUI
- No longer reliant on EasyGUI
- Better ZIP file support
- More relevent error messages
- Now offers the option of running the game after you're done patching (Windows only)
- Now removes deleted mods from modorder.txt
- Now supports .append.xml as well as .xml.append
- Improved Mac OS X support
(Thanks to ser_aerochorro for his contributions!)

1.3:
- Added custom subdirectory support
- Added an option to be able to use .zip files
- Integrated Icehawk78's stability patch
- Now includes modman.ini
- The Scrap Advantage example mod is now functional

1.2:
- Added missing files required for Mac/Linux users

1.1:
- Fixed critical issue with sub-folders
- Experimental Mac/Linux support

1.0:
- Initial release
