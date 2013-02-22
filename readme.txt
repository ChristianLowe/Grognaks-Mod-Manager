To install the mod manager itself, unzip all of the files in the archive and move them into the folder:
Windows: in which FTLGame.exe resides.
Mac OS X: in which FTL_README.html resides.
Linux: in which FTL resides.

For Mac/Linux users: Move the contents of src into the same folder as modman.exe. In order to use GMM, run main.py via python. (It is safe to delete modman.exe.)

Mods come in .ftl files. To make one available to GMM, 
(Windows/Linux) simply drag it into the /mods folder.
(Mac OS X) move it to the ~/Documents/FTL Mods folder.

To install mods, open GMM, select the mods you want to be installed, and hit the button labled "Patch." Please note that you need to re-select mods that you already have installed, otherwise they will uninstall themselves.

In order to completely uninstall all mods, simply start the patching process with nothing selected.

===============
      Changelog
===============

1.5:
- Add option to select all mods automatically (on by default, changeable in .ini)
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