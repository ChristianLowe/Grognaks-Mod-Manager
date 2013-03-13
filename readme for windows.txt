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
  FTL resources. Specifically "data.dat" in the "resources\"
  directory under your FTL install.

  In most cases, this should be located automatically.


Usage

  To add a mod (an *.ftl file) to GMM:
    Put it in the GMM\mods\ folder.

  To Start GMM:
    Double-click modman.exe.

  To install mods:
    Select the mods you want to install.
    Mods at the top get clobbered by ones below. Drag names to reorder.
    Click the "Patch" button.
    (Any unselected mods will be omitted/uninstalled.)

  To uninstall all mods:
    Click "Patch" with none selected.

  If you upgrade FTL:
    Delete the outdated files in GMM\Backup\
    If you don't, the game's resources will get corrupted.


Troubleshooting

  If you get permission errors...
    Right-click modman.exe -> "Run as Administrator".
    OR
    Start Menu -> Programs -> Accessories.
    Right-click "Command Prompt" to run as an admin.
    cd to the GMM directory.
    Run "main.py"

    Make sure that your resource.dat and data.dat files are not read-only.

  If the game shows exclamation marks for everything...
    Delete the files in GMM/Backup/
    Steam users:
      Delete the /resources directory and "verify game cache".
        https://support.steampowered.com/kb_article.php?ref=2037-QEUH-3335
    Standalone users:
      Reinstall FTL.
