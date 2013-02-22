#!/usr/bin/env python

from sys import argv
from ConfigParser import SafeConfigParser
from ftldat import FTLDatUnpacker as du
from ftldat import FTLDatPacker as dp
from shutil import copy

import Tkinter as tk
import tkMessageBox as msgbox
import tempfile as tf
import zipfile as zf
import shutil as sh
import webbrowser
import platform
import glob
import xml
import sys
import os


progver = "1.6"
progname = "Grognak's Mod Manager v%s" % progver
mergelist = None
modname_list = None


class MainWindow(tk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        self.custom_args = {"title":None}
        for k in self.custom_args.keys():
          if (k in kwargs):
            self.custom_args[k] = kwargs[k]
            del kwargs[k]
        tk.Toplevel.__init__(self, master, *args, **kwargs)

        if (self.custom_args["title"]): self.wm_title(self.custom_args["title"])

        self.button_width = 7
        self.button_padx = "2m"
        self.button_pady = "1m"

        self.oldlist = set()

        self.resizable(False, False)

        # Our topmost frame is called rootframe
        self.rootframe = tk.Frame(self)
        self.rootframe.pack()

        # Top frame (container)
        self.top_frame = tk.Frame(self.rootframe)
        self.top_frame.pack(side="top", fill="both", expand="yes")

        # Top-left frame (mod list)
        self.left_frame = tk.Frame(self.top_frame, #background="red",
            borderwidth=1, relief="ridge",
            width=50, height=250)
        self.left_frame.pack(side="left", fill="both", expand="yes")

        # Top-right frame (buttons)
        self.right_frame = tk.Frame(self.top_frame, width=250)
        self.right_frame.pack(side="right", fill="y", expand="no")

        # Bottom frame (mod descriptions)
        self.bottom_frame = tk.Frame(self.rootframe,
            borderwidth=3, relief="ridge",
            height=50)
        self.bottom_frame.pack(side="top", fill="both", expand="yes")

        # add a listbox to hold the mod names
        self.modlistbox = tk.Listbox(self.left_frame, width=30, height=1, selectmode="multiple") # Height readjusts itself for the button frame
        self.modlistbox.pack(side="left", fill="both", expand="yes")
        self.modscrollbar = tk.Scrollbar(self.left_frame, command=self.modlistbox.yview, orient="vertical")
        self.modscrollbar.pack(side="right", fill="y")
        self.modlistbox.bind("<<ListboxSelect>>", self._on_listbox_select)
        self.modlistbox.configure(yscrollcommand=self.modscrollbar.set)

        # add textbox at bottom to hold mod information
        self.descbox = tk.Text(self.bottom_frame, width=60, height=10, wrap="word")
        self.descbox.pack(fill="both", expand="yes")

        # Set formating tags
        self.descbox.tag_configure("title", font="helvetica 24 bold")

        # now we add the buttons to the buttons_frame
        self.patch_btn = tk.Button(self.right_frame, command=self._patch)
        self.patch_btn.configure(text="Patch")
        self.patch_btn.focus_force()
        self.patch_btn.configure(
            width=self.button_width,
            padx=self.button_padx, pady=self.button_pady)

        self.patch_btn.pack(side="top")
        self.patch_btn.bind("<Return>", lambda e: self._patch())

        self.reorder_btn = tk.Button(self.right_frame, command=self._reorder)
        self.reorder_btn.configure(text="Reorder")
        self.reorder_btn.configure(
            width=self.button_width,
            padx=self.button_padx, pady=self.button_pady,
            state="disabled")

        self.reorder_btn.pack(side="top")
        self.reorder_btn.bind("<Return>", lambda e: self._reorder())

        self.forum_btn = tk.Button(self.right_frame, command=self._browse_forum)
        self.forum_btn.configure(text="Forum")
        self.forum_btn.configure(
            width=self.button_width,
            padx=self.button_padx, pady=self.button_pady)

        self.forum_btn.pack(side="top")
        self.forum_btn.bind("<Return>", lambda e: self._browse_forum())

        self.exit_btn = tk.Button(self.right_frame, command=self._die)
        self.exit_btn.configure(text="Exit")
        self.exit_btn.configure(
            width=self.button_width,
            padx=self.button_padx, pady=self.button_pady)

        self.exit_btn.pack(side="top")
        self.exit_btn.bind("<Return>", lambda e: self._die())

        self._filldata()
        self.wm_protocol("WM_DELETE_WINDOW", self._on_delete)

    def _filldata(self):
        global modname_list

        # Set default description
        self._set_description("Grognak's Mod Manager", "Grognak", progver, "Thanks for using GMM. Make sure to periodically check the forum for updates!")

        # Gets list of mods the player wants to be patched in
        for mod in modname_list:
            self._addmod(mod, False)

    def _on_listbox_select(self, event):
        curlist = self.modlistbox.curselection()
        newset = [x for x in curlist if (x not in self.oldlist)]
        self.oldlist = set(curlist)

        if (len(newset) > 0):
            self._set_description(self.modlistbox.get(newset[0]))

    def _addmod(self, modname, selected):
        # Add a mod name to the list.
        newitem = self.modlistbox.insert(tk.END, modname)
        if (selected):
            self.modlistbox.selection_set(newitem)

    def _set_description(self, title, author=None, version=None, description=None):
        # Changes the description of the currently selected mod
        self.descbox.configure(state="normal")
        self.descbox.delete("1.0", tk.END)
        self.descbox.insert(tk.END, (title +"\n"), "title")
        if (author is not None and version is not None):
            self.descbox.insert(tk.END, "by %s (version %s)\n\n" % (author, str(version)))
        else:
            self.descbox.insert(tk.END, "\n")
        if (description):
            self.descbox.insert(tk.END, description)
        else:
            self.descbox.insert(tk.END, "No description.")
        self.descbox.configure(state="disabled")

    def _patch(self):
        global mergelist
        mergelist = [self.modlistbox.get(modname) for modname in self.modlistbox.curselection()]
        _die()

    def _die(self):
        """Kill the app gracefully by destroying the root window."""
        self._root().destroy()

    def _reorder(self):
        ReorderWindow(root, title=("%s - Reorder" % self.wm_title()))

    def _browse_forum(self):
        webbrowser.open("http://www.ftlgame.com/forum/viewtopic.php?f=12&t=2464")

    def _on_delete(self):
        """When this window is gone, end the mainloop."""
        self._root().quit()


class ReorderWindow(tk.Toplevel):
    # Not completely implemented yet, so button is disabled

    def __init__(self, parent, *args, **kwargs):
        self.custom_args = {"title":None}
        for k in self.custom_args.keys():
          if (k in kwargs):
            self.custom_args[k] = kwargs[k]
            del kwargs[k]
        tk.Toplevel.__init__(self, parent, *args, **kwargs)

        if (self.custom_args["title"]): self.wm_title(self.custom_args["title"])

        self.resizable(False, False)

        self.rootframe = tk.Frame(self)
        self.rootframe.pack()

        button_width = 7
        button_padx = "2m"
        button_pady = "1m"

        # top frame
        self.top_frame = tk.Frame(self.rootframe)
        self.top_frame.pack(side="top", fill="both", expand="yes")

        # left_frame
        self.left_frame = tk.Frame(self.top_frame, #background="red",
            borderwidth=1, relief="ridge",
            width=50, height=250)
        self.left_frame.pack(side="left", fill="both", expand="yes")

        ### right_frame
        self.right_frame = tk.Frame(self.top_frame,
            width=250)
        self.right_frame.pack(side="right", fill="y", expand="no")

        # add a listbox to hold the mod names
        self.modlistbox = tk.Listbox(self.left_frame, width=30, height=1) # Height readjusts itself for the button frame
        self.modlistbox.pack(side="left", fill="both", expand="yes")
        self.modlistbox.bind("<<ListboxSelect>>", self._on_listbox_select)
        self.modscrollbar = tk.Scrollbar(self.left_frame, command=self.modlistbox.yview, orient="vertical")
        self.modscrollbar.pack(side="right", fill="y")
        self.modlistbox.configure(yscrollcommand=self.modscrollbar.set)


        # now we add the buttons to the buttons_frame
        self.okbutton = tk.Button(self.right_frame, command=self._apply)
        self.okbutton.configure(text="OK")
        self.okbutton.focus_force()
        self.okbutton.configure(
            width=button_width,
            padx=button_padx, pady=button_pady)

        self.okbutton.pack(side="top")
        self.okbutton.bind("<Return>", lambda e: self._apply())

        self.upbutton = Button(self.right_frame, command=self._shift_up)
        self.upbutton.configure(text="Move Up")
        self.upbutton.configure(
            width=button_width,
            padx=button_padx, pady=button_pady,
            state="disabled")

        self.upbutton.pack(side="top")
        self.upbutton.bind("<Return>", lambda e: self._shift_up())

        self.downbutton = Button(self.right_frame, command=self._shift_down)
        self.downbutton.configure(text="Move Down")
        self.downbutton.configure(
            width=button_width,
            padx=button_padx, pady=button_pady,
            state="disabled")

        self.downbutton.pack(side="top")
        self.downbutton.bind("<Return>", lambda e: self._shift_down())

    def _adjustPosition(self, index, amount):
        newindex = index + amount
        if (newindex >= 0 and newindex < self.modlistbox.size()):
            item = self.modlistbox.get(index)
            self.modlistbox.delete(index)
            self.modlistbox.insert(newindex, item)
            self.modlistbox.selection_set(newindex)
            scrollfraction = float(newindex-3)/float(self.modlistbox.size())
            self.modlistbox.yview_moveto(scrollfraction)
            self._handleButtons(newindex)

    def _on_listbox_select(self, event):
        cursel = int(self.modlistbox.curselection()[0])
        self._handleButtons(cursel)

    def _handleButtons(self, cursel):
        if (cursel is 0):
            self.upbutton['state'] = "disabled"
            self.downbutton['state'] = "active"
        elif (cursel is self.modlistbox.size()-1):
            self.upbutton['state'] = "active"
            self.downbutton['state'] = "disabled"
        else:
            self.upbutton['state'] = "active"
            self.downbutton['state'] = "active"

    def _apply(self):
        self.destroy()

    def _shift_up(self):
        self._adjustPosition(int(self.modlistbox.curselection()[0]), -1)

    def _shift_down(self):
        self._adjustPosition(int(self.modlistbox.curselection()[0]), 1)


def ftl_path_join(*args):
    """ Joins paths in the way FTL expects them to be in .dat files.
        That is: the UNIX way. """
    return "/".join(args)

def appendfile(src, dst):
    source = open(src, "r")
    target = open(dst, "a")

    target.write(source.read() +"\n")

    source.close()
    target.close()

def mergefile(src, dst):
    pass

def packdat(datafolder, datfile):
    print "\nRepacking %s" % datfile
    print "Listing files to pack ..."
    s = [()]
    files = []
    while s:
        current = s.pop()
        for child in os.listdir(os.path.join(datafolder, *current)):
            full_path = os.path.join(datafolder,
                                        *(current + (child,)))
            if (os.path.isfile(full_path)):
                files.append(current + (child,))
            elif (os.path.isdir(full_path)):
                s.append(current + (child,))
    print "Create datfile ..."
    indexSize = len(files)
    packer = dp(open(datfile, "wb"), indexSize)
    print "Packing ..."
    for _file in files:
        full_path = os.path.join(datafolder, *_file)
        size = os.stat(full_path).st_size
        with open(full_path, "rb") as f:
            packer.add(ftl_path_join(*_file), f, size)

def unpackdat(datafile):
    print "Unpacking %s..." % datafile
    unpacker = du(open(datafile, "rb"))

    for i, filename, size, offset in unpacker:
        target = os.path.join(datafile +"-unpacked", filename)
        if (not os.path.exists(os.path.dirname(target))):
            os.makedirs(os.path.dirname(target))
        with open(target, "wb") as f:
            unpacker.extract_to(filename, f)

def main():
    global mergelist, modname_list, progname

    # Set relative locations
    realpath = os.path.realpath(__file__)
    dir_root = os.path.dirname(realpath)
    dir_mods = os.path.join(dir_root, "mods")
    dir_res = os.path.join(dir_root, "resources")

    print "%s\n" % dir_root

    # Load up config file values
    cfg = SafeConfigParser()
    cfg.read(os.path.join(dir_root, "modman.ini"))

    allowzip = cfg.getboolean("settings", "allowzip")

    # Verify that the user put GMM in the right location
    if (platform.system() == "Windows"):
        if (not os.path.isfile(os.path.join(dir_root, "FTLGame.exe"))):
            msgbox.showerror(progname, "This executable must be in the same folder as FTLGame.exe.")
            sys.exit(0)
    elif (platform.system() == "Linux"):
        if (not os.path.isfile(os.path.join(dir_root, "FTL"))):
            msgbox.showerror(progname, "Grognak's Mod Manager must be located directly above the FTL folder.")
            sys.exit(0)
    elif (platform.system() == "Darwin"):
        steam = msgbox.askyesno(progname, "Did you purchase FTL through Steam?")
        if (steam is True):
            dir_res = os.path.join(os.environ["HOME"], "Library/Application Support/Steam/SteamApps/common/FTL Faster Than Light/FTL.app/Contents/Resources")
        if (steam is False or steam is None):
            if (not os.path.isfile(os.path.join(dir_root, "MacOS", "FTL"))):
                msgbox.showerror(progname, "Grognak's Mod Manager must be located directly above the MacOS folder in FTL.app.")
                sys.exit(0)
            dir_res = os.path.join(dir_root, "Resources")
        os.chdir(dir_root)
        dir_mods = cfg.get("settings", "macmodsdir")
        dir_mods = os.path.expanduser(dir_mods)
        if (not os.path.exists(dir_mods)):
           os.makedirs(dir_mods)
           copy(os.path.join(dir_root, "mods/Beginning Scrap Advantage.ftl"), dir_mods)
           msgbox.showinfo(progname, "A folder has been created in %s. Please place any FTL mods there." % dir_mods)
    else:
        msgbox.showwarning(progname, "Unsupported platform; unexpected behavior may occur.")

    # Loop through the .ftl files, check if on mod list.
    os.chdir(dir_mods)
    modorder = open("modorder.txt", "a+")
    modorder.seek(0)
    modorder_read = modorder.readlines()

    modorder_read = [word.strip() for word in modorder_read]

    for f in glob.glob("*.ftl"):
        if (not f in modorder_read):
            modorder.write(f +"\n")
            print "Added %s" % f

    if (allowzip):
        for f in glob.glob("*.zip"):
            if (not f in modorder_read):
                modorder.write(f +"\n")


    # Check if any mods have beed deleted(are in modorder but not in the mods folder)
    modorder.seek(0)
    modorder_read = modorder.readlines()
    modorder_read = [word.strip() for word in modorder_read]
    for f in modorder_read:
        if (f not in glob.glob("*.ftl")):
            modorder_read.remove(f)
            print "Removed %s" % f

    if (allowzip):
        for f in modorder_read:
            if (not f in glob.glob("*.zip")):
                modorder_read.remove(f)

    modorder.close()
    modorder = open("modorder.txt", "w")
    modorder.write("\n".join(modorder_read) +"\n")
    modorder.close()
    modorder = open("modorder.txt", "a+")


    # Refresh the list
    modorder.seek(0)
    modorder_read = modorder.readlines()
    modorder_read = [word.strip() for word in modorder_read]

    # Mod list sans the .ftl extention
    if (allowzip):
        modname_list = modorder_read
    else:
        modname_list = [word[:-4] for word in modorder_read]

    # Start the GUI
    root = tk.Tk()
    root.withdraw()
    mygui = MainWindow(master=root, title=progname)
    root.mainloop()

    # User hit the X button
    if (mergelist is None):
        sys.exit(0)

    # Create data file backups, if necessary
    os.chdir(dir_res)

    if (not os.path.isfile("data.dat.bak")):
        print "Backing up data.dat"
        sh.copy2("data.dat", "data.dat.bak")

    if (not os.path.isfile("resource.dat.bak")):
        print "Backing up resource.dat\n"
        sh.copy2("resource.dat", "resource.dat.bak")

    # Overwrite old data files with their respective backups
    sh.copy2("data.dat.bak", "data.dat")
    sh.copy2("resource.dat.bak", "resource.dat")

    # Extract both of the backup files
    unpackdat("data.dat")
    unpackdat("resource.dat")

    # Go through each .ftl archive and apply changes
    tmp = tf.mkdtemp()
    if (allowzip):
        modlist = mergelist
    else:
        modlist = [(word +".ftl") for word in mergelist]

    for filename in modlist:
        os.chdir(dir_mods)
        ftl = zf.ZipFile(filename, "r")

        print "\nInstalling %s" % filename

        # Unzip everything into a temporary folder
        for item in ftl.namelist():
            if (item.endswith("/")):
                path = os.path.join(tmp, item)
                if (not os.path.exists(path)):
                    os.makedirs(path)
            else:
                ftl.extract(item, tmp)

        # Go through each directory in the .ftl file
        for directory in os.listdir(tmp):
            if (directory == "data"):
                print " - Merging %s folder" % directory
                for root, dirs, files in os.walk(os.path.join(tmp, directory)):
                    for d in dirs:
                        path = os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], d)
                        if (not os.path.exists(path)):
                            os.makedirs(path)
                    for f in files:
                        if (f.endswith(".append")):
                            appendfile(os.path.join(root, f), os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], f[:-len(".append")]))
                        elif (f.endswith(".append.xml")):
                            appendfile(os.path.join(root, f), os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], f[:-len(".append.xml")]+".xml"))
                        elif (f.endswith(".merge")):
                            mergefile(os.path.join(root, f), os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], f[:-len(".merge")]))
                        elif (f.endswith("merge.xml")):
                            mergefile(os.path.join(root, f), os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], f[:-len(".merge.xml")]+".xml"))
                        else:
                            sh.copy2(os.path.join(root, f), os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], f))

            elif (directory in ("audio", "fonts", "img")):
                print " - Merging %s folder" % directory
                for root, dirs, files in os.walk(os.path.join(tmp, directory)):
                    for d in dirs:
                        path = os.path.join(dir_res, "resource.dat-unpacked", root[len(tmp)+1:], d)
                        if (not os.path.exists(path)):
                            os.makedirs(path)
                    for f in files:
                        if (f.endswith(".append")):
                            appendfile(os.path.join(root, f), os.path.join(dir_res, "resource.dat-unpacked", root[len(tmp)+1:], f[:-len(".append")]))
                        else:
                            sh.copy2(os.path.join(root, f), os.path.join(dir_res, "resource.dat-unpacked", root[len(tmp)+1:], f))

            else:
                print " - WARNING: Unsupported folder: %s" % directory

        # Clean up temporary folder's contents
        for root, dirs, files in os.walk(tmp):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                sh.rmtree(os.path.join(root, d))

    # All the mods are installed, so repack the files.
    os.chdir(dir_res)
    packdat("data.dat-unpacked", "data.dat")
    packdat("resource.dat-unpacked", "resource.dat")

    # All done!
    if (platform.system() == "Windows"):
        if (msgbox.askyesno(progname, "Patching completed successfully. Run FTL now?")):
            os.system("\"%s\"" % os.path.join(dir_root, "FTLGame.exe"))
    else:
        msgbox.showinfo(progname, "Patching completed successfully.")



if (__name__ == "__main__"):
  main()
