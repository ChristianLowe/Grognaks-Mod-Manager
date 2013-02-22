Grognak's Mod Manager
http://www.ftlgame.com/forum/viewtopic.php?f=12&t=2464


About

Grognak's Mod Manager, or GMM for short, is a program designed to
make it easy to install multiple mods at the same time. No longer
do you have to pack and unpack files or swap out each mod you want
to use one at a time.


Requirements

  Python 2.7 or higher, but not 3.x.
    http://www.python.org/getit/

  FTL (1.01-1.03.1, Windows/OSX/Linux, Steam/GOG/Standalone).
    http://www.ftlgame.com/

  * Linux will need the python-tk package.
  * OSX may need to replace the stock Tcl/Tk from Apple.
    http://www.python.org/download/mac/tcltk/


Setup

  Unzip all of the files from this archive and move them into:
    Windows: the folder in which FTLGame.exe resides.
    Mac OSX: the folder in which FTL_README.html resides.
    Linux: in the folder which FTL resides.

  For Mac/Linux users:
    Move the contents of src into the same folder as modman.exe.
    (It is safe to delete modman.exe.)


Usage

  To add a mod (an *.ftl file) to GMM:
    Windows/Linux: Put it in the /mods/ folder.
    Mac OSX: Put it in the ~/Documents/FTL Mods/ folder.

  To Start GMM:
    Windows: Run modman.exe.
    Mac/Linux: Run main.py via python.

  To install mods:
    Select the mods you want to be installed.
    Click the "Patch" button.
    (Any unselected mods will be omitted/uninstalled.)

  To uninstall all mods:
    Click "Patch" with none selected.


Troubleshooting

  If you need help installing on Mac...
    Guide
      http://www.ftlgame.com/forum/viewtopic.php?f=12&t=2464&start=450#p30155
    Video tutorials
      http://www.ftlgame.com/forum/viewtopic.php?f=12&t=2464&start=540#p32737

  If you get permission errors...
    Windows: Right-click modman.exe -> "Run as Administrator".
    Mac/Linux: Make sure that your resource.dat and data.dat
      files are not read-only.

  If the game shows exclamation marks for everything...
    Steam users can delete the /resources directory and "verify game cache".
      https://support.steampowered.com/kb_article.php?ref=2037-QEUH-3335
    Standalone users should be fine after reinstalling FTL.

  Other...
    Try deleting modorder.txt from the /mods folder and relaunching GMM.

  When developing a mod, save your text files as ANSI, not UTF-8.


Changelog

1.6:
- Removed option to select all mods

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
