Mod Developer Notes

Creating an .ftl File

  A .ftl file is simply a renamed .zip with a specific file structure.
  For an example, try renaming and unpacking the example .ftl file that
  comes with the program.

  The root of the ZIP file should contain one or more of these folders:
    data/
    audio/
    fonts/
    img/

  You should ONLY put in the files that you want to modify. This keeps
  mod sizes low and prevents major conflict between mods.


The Append Extension

  Any file in your .ftl with the extension .xml.append will be appended to
  its respective vanilla file. (See the example mod.)

  It is highly recommended that you take advantage of this as much as
  possible. As a rule of thumb, if you're editing an event xml file,
  you're going to want to append your changes rather then flat out replace
  the file. Keep in mind that you can override vanilla events to your
  pleasure by writing an event of the same name. Using .append helps prevent
  mod conflict.


General

  When developing a mod, save your text files as ANSI/ASCII, not UTF-8.

  Unless you're overriding something, try to use unique names in your xml so
  that it won't clobber another mod and vice versa.

  Images should be 32bit PNGs (24bit color + 8bit alpha transparency).
  Things that *should* be opaque rectangles like backgrounds may vary,
  but that would be undesirable for ship floors that should reveal the hull
  under them.


Mac-Specific

  OSX adds a junk to .zip files.
    These commands will address that:
      zip -d mymod.zip __MACOSX/\*
      zip -d mymod.zip \*.DS_Store


Pitfalls

  As of FTL 1.03.1: If a ship is modded to have level 5 shields, asteroid
  storms will be abnormally fast.
  http://www.ftlgame.com/forum/viewtopic.php?f=9&t=11057

  When adding a music track to sounds.xml, the explore and battle theme
  files are played simultaneously as one song (mixing between them when
  entering/exiting combat). They should have similar duration because if one
  is longer than the other, there may be noticable silence at the end of the
  shorter piece.
  http://www.ftlgame.com/forum/viewtopic.php?f=12&t=9111
