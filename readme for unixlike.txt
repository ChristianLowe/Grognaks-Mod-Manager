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

  Before upgrading GMM:
    Uninstall all mods, so the next GMM can start with a clean game.

  If you upgrade FTL:
    Delete the outdated files in GMM/backup/
    If you don't, the game's resources will get corrupted.


Troubleshooting

* If you get permission errors...
    Make sure that your resource.dat and data.dat files are not read-only.

* If the game shows exclamation marks for everything...
    See the suggestion below for replacing corrupt resources.

* If text in-game is shrunken and moved to the top of the screen...
    FTL was upgraded, but GMM modded using used resources from the old FTL.
    When upgrading FTL in the future, delete what's in GMM/backups/ first.
    See the suggestion below for replacing corrupt resources.

* ERROR: unpack requires a string argument of length 8...
    Seems data.dat or resource.dat had been corrupted somehow.
    The dat file claims to be larger than it really is, and
    GMM reaches the end prematurely, unable to read 8 more bytes.
    See the suggestion below for replacing corrupt resources.

* If FTL's resources are corrupt...
    Delete the files in GMM/backup/
    Steam users:
      Delete FTL's resource directory:
        Linux: "[~/.local/share or $XDG_DATA_HOME]/Steam/SteamApps/common/FTL Faster Than Light/data/resources"
        Mac: "~/Library/Application Support/Steam/SteamApps/common/FTL Faster Than Light/FTL.app"
      Start Steam and "verify game cache".
        https://support.steampowered.com/kb_article.php?ref=2037-QEUH-3335
      Run FTL, which will cause steam to copy fresh resources from its cache.
    Standalone users:
      Reinstall FTL.

* Mac: If you see the following error...
    "Warning: 'as' will become a reserved keyword in Python 2.6"
    This warning comes from python 2.5, which is too old for GMM.
    You probably have several versions installed, and the wrong one is used.

    Open a terminal, and type: man python
    That explains how to set the "system-wide default" version of python.
