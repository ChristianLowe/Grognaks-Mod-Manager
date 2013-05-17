Changelog

???:
- Added periodic updates to the catalog of mod metadata
- Added ini setting: update_catalog
- Added a log warning during patching if a mod gets clobbered
- Added a log warning during patching if a modded file's case doesn't match
- Fixed AttributeError after patching, before offering to launch FTL on Mac
- Changed ini encoding to utf-8 to support accented paths
- Fixed Validate encoding errors when non-ascii characters are present
- Added <gmm:blueprintListAppend> tag to *.xml.append files

1.7:
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
