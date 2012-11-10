#!/usr/bin/env python

from sys import argv
from ConfigParser import SafeConfigParser
from Tkinter import * # I know, I know, bad practice
from ftldat import FTLDatUnpacker as du
from ftldat import FTLDatPacker as dp
from shutil import copy

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

progname = "Grognak's Mod Manager v1.4"
mergelist = None

class MainWindow:
    def __init__(self, parent):
        self.myParent = parent
        
        self.button_width = 7
        
        self.button_padx = "2m" 
        self.button_pady = "1m"
        
        self.buttons_frame_padx =  "3m"
        self.buttons_frame_pady =  "2m"       
        self.buttons_frame_ipadx = "3m"
        self.buttons_frame_ipady = "1m"
        
        self.oldlist = set()
        
        self.start()
        
    def start(self):
        parent = self.myParent
        
        # Our topmost frame is called rootframe
        self.rootframe = Frame(parent)
        self.rootframe.pack()
        
       # Top frame (container)
        self.top_frame = Frame(self.rootframe) 
        self.top_frame.pack(side=TOP,
                fill=BOTH, 
                expand=YES,
                )
        
        # Top-left frame (mod list)       
        self.left_frame = Frame(self.top_frame, #background="red",
            borderwidth=1,  relief=RIDGE,
            height=250, 
            width=50,
            )
        self.left_frame.pack(side=LEFT,
            fill=BOTH, 
            expand=YES,
            )
        
        # Top-right frame (buttons)
        self.right_frame = Frame(self.top_frame, width=250)
        self.right_frame.pack(side=RIGHT,
            fill=Y, 
            expand=NO,
            )
        
        # Bottom frame (mod descriptions)
        self.bottom_frame = Frame(self.rootframe, 
            borderwidth=3,  relief=RIDGE,
            height=50, 
            )
        self.bottom_frame.pack(side=TOP,
            fill=BOTH, 
            expand=YES,
            )
        
        # add a listbox to hold the mod names
        self.modlistbox = Listbox(self.left_frame, width=30, height=1, selectmode="multiple") # Height readjusts itself for the button frame
        self.modlistbox.pack(side=LEFT, fill=BOTH, expand=1)
        self.modscrollbar = Scrollbar(self.left_frame, command=self.modlistbox.yview, orient=VERTICAL)
        self.modscrollbar.pack(side=RIGHT, fill=Y)
        self.modlistbox.bind("<<ListboxSelect>>", self.ListboxSelect)
        self.modlistbox.configure(yscrollcommand=self.modscrollbar.set)
        
        # add textbox at bottom to hold mod information
        self.descbox = Text(self.bottom_frame, width=60, height=10, wrap=WORD)
        self.descbox.pack(fill=BOTH, expand=1)
        
        # Set formating tags
        self.descbox.tag_configure("title", font="helvetica 24 bold")
        
        # now we add the buttons to the buttons_frame   
        self.patchbutton = Button(self.right_frame, command=self.patchbuttonClick)
        self.patchbutton.configure(text="Patch")
        self.patchbutton.focus_force()       
        self.patchbutton.configure( 
                width=self.button_width,  
                padx=self.button_padx,    
                pady=self.button_pady     
                )
        
        self.patchbutton.pack(side=TOP)    
        self.patchbutton.bind("<Return>", self.patchbuttonClick_a)
        
        self.reorderbutton = Button(self.right_frame, command=self.reorderbuttonClick)
        self.reorderbutton.configure(text="Reorder")  
        self.reorderbutton.configure( 
                width=self.button_width,  
                padx=self.button_padx,     
                pady=self.button_pady,
                state=DISABLED
                )
        
        self.reorderbutton.pack(side=TOP)
        self.reorderbutton.bind("<Return>", self.reorderbuttonClick_a)
        
        self.forumbutton = Button(self.right_frame, command=self.forumbuttonClick)
        self.forumbutton.configure(text="Forum")  
        self.forumbutton.configure( 
                width=self.button_width,  
                padx=self.button_padx,     
                pady=self.button_pady     
                )
        
        self.forumbutton.pack(side=TOP)
        self.forumbutton.bind("<Return>", self.forumbuttonClick_a) 
        
        self.exitbutton = Button(self.right_frame, command=self.exitbuttonClick)
        self.exitbutton.configure(text="Exit")  
        self.exitbutton.configure( 
                width=self.button_width,  
                padx=self.button_padx,     
                pady=self.button_pady     
                )
        
        self.exitbutton.pack(side=TOP)
        self.exitbutton.bind("<Return>", self.exitbuttonClick_a)
        
        self.filldata()
        
    def filldata(self):
        # Set default description
        self.changedesc("Grognak's Mod Manager", "Grognak", 1.4, "Thanks for using GMM. Make sure to periodically check the forum for updates!")
        
        # Gets list of mods the player wants to be patched in
        for mod in modname_list:
            self.addmod(mod, False)
            
    def ListboxSelect(self, event):
        curlist = self.modlistbox.curselection()
        newset = [x for x in curlist if x not in self.oldlist]
        self.oldlist = set(curlist)
        
        if len(newset) is not 0:
            self.changedesc(self.modlistbox.get(newset[0]))
        
    def addmod(self, modname, selected):
        # Add a mod name to the list.
        newitem = self.modlistbox.insert(END, modname)
        if selected:
            self.modlistbox.selection_set(newitem)
        
    def changedesc(self, title, author = None, version = None, description = None):
        # Changes the description of the currently selected mod
        self.descbox.configure(state=NORMAL)
        self.descbox.delete('1.0', END)
        self.descbox.insert(END, title + "\n", "title")
        if author is not None and version is not None:
            self.descbox.insert(END, "by " + author + " (version " + str(version) + ")\n\n")
        else:
            self.descbox.insert(END, "\n")
        if description is not None:
            self.descbox.insert(END, description)
        else:
            self.descbox.insert(END, "No description.")
        self.descbox.configure(state=DISABLED)
        
    def patchbuttonClick(self):
        global mergelist
        mergelist = [self.modlistbox.get(modname) for modname in self.modlistbox.curselection()]
        self.myParent.destroy()
        
    def patchbuttonClick_a(self, event):  
        self.patchbuttonClick()
        
    def exitbuttonClick(self):
        sys.exit(0)
        
    def exitbuttonClick_a(self, event): 
        self.exitbuttonClick() 
        
    def reorderbuttonClick(self):
        self.myParent.withdraw()
        root = Tk()
        root.resizable(False, False)
        root.wm_title(progname + " - Reorder")
        ReorderWindow(root)
        root.mainloop()
        self.myParent.update()
        self.myParent.deiconify()
        
    def reorderbuttonClick_a(self, event): 
        self.reorderbuttonClick()
        
    def forumbuttonClick(self): 
        webbrowser.open("http://www.ftlgame.com/forum/viewtopic.php?f=12&t=2464")
        
    def forumbuttonClick_a(self, event): 
        self.forumbuttonClick()

class ReorderWindow:
    # Not completely implemented yet, so button is disabled
    def __init__(self, parent):
        self.myParent = parent
        
        self.rootframe = Frame(parent)
        self.rootframe.pack()
        
        button_width = 7     
        
        button_padx = "2m"    
        button_pady = "1m"   
        
        buttons_frame_padx =  "3m"   
        buttons_frame_pady =  "2m"         
        buttons_frame_ipadx = "3m"   
        buttons_frame_ipady = "1m"         
        
        # top frame
        self.top_frame = Frame(self.rootframe) 
        self.top_frame.pack(side=TOP,
                fill=BOTH, 
                expand=YES,
                ) 
        
        # left_frame        
        self.left_frame = Frame(self.top_frame, #background="red",
            borderwidth=1,  relief=RIDGE,
            height=250, 
            width=50,
            ) 
        self.left_frame.pack(side=LEFT,
            fill=BOTH, 
            expand=YES,
            )  
        
        ### right_frame 
        self.right_frame = Frame(self.top_frame,
            width=250,
            )
        self.right_frame.pack(side=RIGHT,
            fill=Y, 
            expand=NO,
            )  
        
        # add a listbox to hold the mod names
        self.modlistbox = Listbox(self.left_frame, width=30, height=1) # Height readjusts itself for the button frame
        self.modlistbox.pack(side=LEFT, fill=BOTH, expand=1)
        self.modlistbox.bind("<<ListboxSelect>>", self.ListboxSelect)
        self.modscrollbar = Scrollbar(self.left_frame, command=self.modlistbox.yview, orient=VERTICAL)
        self.modscrollbar.pack(side=RIGHT, fill=Y)
        self.modlistbox.configure(yscrollcommand=self.modscrollbar.set)
        
        
        # now we add the buttons to the buttons_frame   
        self.okbutton = Button(self.right_frame, command=self.okbuttonClick)
        self.okbutton.configure(text="OK")
        self.okbutton.focus_force()       
        self.okbutton.configure( 
                width=button_width,  
                padx=button_padx,    
                pady=button_pady     
                )
        
        self.okbutton.pack(side=TOP)    
        self.okbutton.bind("<Return>", self.okbuttonClick_a)
        
        self.upbutton = Button(self.right_frame, command=self.upbuttonClick)
        self.upbutton.configure(text="Move Up")  
        self.upbutton.configure( 
                width=button_width,  
                padx=button_padx,     
                pady=button_pady,
                state=DISABLED,
                )
        
        self.upbutton.pack(side=TOP)
        self.upbutton.bind("<Return>", self.upbuttonClick_a)
        
        self.downbutton = Button(self.right_frame, command=self.downbuttonClick)
        self.downbutton.configure(text="Move Down")  
        self.downbutton.configure( 
                width=button_width,  
                padx=button_padx,     
                pady=button_pady,
                state=DISABLED,
                )
        
        self.downbutton.pack(side=TOP)
        self.downbutton.bind("<Return>", self.downbuttonClick_a)
        
    def adjustPosition(self, index, amount):
        newindex = index + amount
        if newindex >= 0 and newindex < self.modlistbox.size():
            item = self.modlistbox.get(index)
            self.modlistbox.delete(index)
            self.modlistbox.insert(newindex, item)
            self.modlistbox.selection_set(newindex)
            scrollfraction = float(newindex-3)/float(self.modlistbox.size())
            self.modlistbox.yview_moveto(scrollfraction)
            self.handleButtons(newindex)
            
    def ListboxSelect(self, event):
        cursel = int(self.modlistbox.curselection()[0])
        self.handleButtons(cursel)
            
    def handleButtons(self, cursel):
        if cursel is 0:
            self.upbutton['state'] = DISABLED
            self.downbutton['state'] = ACTIVE
        elif cursel is self.modlistbox.size()-1:
            self.upbutton['state'] = ACTIVE
            self.downbutton['state'] = DISABLED
        else:
            self.upbutton['state'] = ACTIVE
            self.downbutton['state'] = ACTIVE
        
    def okbuttonClick(self):      
        self.myParent.destroy()
   
    def okbuttonClick_a(self, event):  
        self.okbuttonClick()
        
    def upbuttonClick(self): 
        self.adjustPosition(int(self.modlistbox.curselection()[0]), -1)
        
    def upbuttonClick_a(self, event): 
        self.upbuttonClick()

    def downbuttonClick(self): 
        self.adjustPosition(int(self.modlistbox.curselection()[0]), 1)
        
    def downbuttonClick_a(self, event): 
        self.downbuttonClick()

def ftl_path_join(*args):
    """ Joins paths in the way FTL expects them to be in .dat files.
        That is: the UNIX way. """
    return '/'.join(args)

def appendfile(src, dst):
    source = open(src, "r")
    target = open(dst, "a")
    
    target.write(source.read() + "\n")
    
    source.close()
    target.close()
    
def mergefile(src, dst):
    pass
    
def packdat(datafolder, datfile):
    print "\nRepacking " + datfile
    print 'Listing files to pack ...'
    s = [()]
    files = []
    while s:
        current = s.pop()
        for child in os.listdir(os.path.join(datafolder, *current)):
            full_path = os.path.join(datafolder,
                                        *(current + (child,)))
            if os.path.isfile(full_path):
                files.append(current + (child,))
            elif os.path.isdir(full_path):
                s.append(current + (child,))
    print 'Create datfile ...'
    indexSize = len(files)
    packer = dp(open(datfile, "wb"), indexSize)
    print 'Packing ...'
    for _file in files:
        full_path = os.path.join(datafolder, *_file)
        size = os.stat(full_path).st_size
        with open(full_path, 'rb') as f:
            packer.add(ftl_path_join(*_file), f, size)

def unpackdat(datafile):
    print "Unpacking %s..." % datafile
    unpacker = du(open(datafile, "rb"))
    
    for i, filename, size, offset in unpacker:
        target = os.path.join(datafile + "-unpacked", filename)
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        with open(target, 'wb') as f:
            unpacker.extract_to(filename, f)

# Set relative locations
realpath = os.path.realpath(__file__)
dir_root = os.path.dirname(realpath)
dir_mods = os.path.join(dir_root, "mods")
dir_res = os.path.join(dir_root, "resources")

print dir_root + "\n"

# Load up config file values
cfg = SafeConfigParser()
cfg.read("modman.ini")

allowzip = cfg.getboolean("settings", "allowzip")

# Verify that the user put GMM in the right location
if platform.system() == "Windows":
    if not os.path.isfile(os.path.join(dir_root, "FTLGame.exe")):
        msgbox.showerror(progname, "This executable must be in the same folder as FTLGame.exe")
        sys.exit(0)
elif platform.system() == "Linux":
    if not os.path.isfile(os.path.join(dir_root, "FTL")):
        msgbox.showerror(progname, "Grognak's Mod Manager must be located directly above the FTL folder")
        sys.exit(0)
elif platform.system() == "Darwin":
    steam = msgbox.askyesno(progname, "Did you purchase FTL through Steam?")
    if steam == True:
        dir_res = os.path.join(os.environ['HOME'], 'Library/Application Support/Steam/SteamApps/common/FTL Faster Than Light/FTL.app/Contents/Resources')
    if steam == False or steam == None:
        if not os.path.isfile(os.path.join(dir_root, "MacOS", "FTL")):
            msgbox.showerror(progname, "Grognak's Mod Manager must be located directly above the MacOS folder in FTL.dat")
            sys.exit(0)
        dir_res = os.path.join(dir_root, 'Resources')
    os.chdir(dir_root)
    dir_mods = cfg.get("settings", "macmodsdir")
    dir_mods = os.path.expanduser(dir_mods)
    if not os.path.exists(dir_mods):
       os.makedirs(dir_mods)
       copy(os.path.join(dir_root, "mods/Beginning Scrap Advantage.ftl"), dir_mods)
       msgbox.showinfo(progname, "A folder has been created in " + dir_mods + ". Please place any FTL mods there.")
else:
    msgbox.showwarning(progname, "Unsupported platform; unexpected behavior may occur.")

# Loop through the .ftl files, check if on mod list.
os.chdir(dir_mods)
modorder = open("modorder.txt", "a+")
modorder.seek(0)
modorder_read = modorder.readlines()

modorder_read = [word.strip() for word in modorder_read]

for f in glob.glob("*.ftl"):
    if not f in modorder_read:
        modorder.write(f + "\n")
        print "Added "+f
        
if allowzip:
    for f in glob.glob("*.zip"):
        if not f in modorder_read:
            modorder.write(f + "\n")
        
        
# Check if any mods have beed deleted(are in modorder but not in the mods folder)
modorder.seek(0)
modorder_read = modorder.readlines()
modorder_read = [word.strip() for word in modorder_read]
for f in modorder_read:
    if f not in glob.glob('*.ftl'):
        modorder_read.remove(f)
        print "Removed "+f
        
if allowzip:
    for f in modorder_read:
        if not f in glob.glob("*.zip"):
            modorder_read.remove(f)
            
modorder.close()
modorder = open('modorder.txt','w')
modorder.write('\n'.join(modorder_read)+'\n')
modorder.close()
modorder = open("modorder.txt", "a+")


# Refresh the list
modorder.seek(0)
modorder_read = modorder.readlines() 
modorder_read = [word.strip() for word in modorder_read]

# Mod list sans the .ftl extention
if allowzip:
    modname_list = modorder_read
else:
    modname_list = [word[:-4] for word in modorder_read]

# Start the GUI
root = Tk()
root.resizable(False, False)
root.wm_title(progname)
MainWindow(root)
root.mainloop()
    
# User hit the X button
if (mergelist == None):
    sys.exit(0) 

# Create data file backups, if necessary
os.chdir(dir_res)

if not os.path.isfile("data.dat.bak"):
    print "Backing up data.dat"
    sh.copy2("data.dat", "data.dat.bak")
    
if not os.path.isfile("resource.dat.bak"):
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
if allowzip:
    modlist = mergelist
else:
    modlist = [word + ".ftl" for word in mergelist]

for filename in modlist:
    os.chdir(dir_mods)
    ftl = zf.ZipFile(filename, 'r')
    
    print "\nInstalling " + filename
    
    # Unzip everything into a temporary folder
    for item in ftl.namelist():
        if item.endswith('/'):
            path = os.path.join(tmp, item)
            if not os.path.exists(path):
                os.makedirs(path)
        else:
            ftl.extract(item, tmp)
    
    # Go through each directory in the .ftl file
    for directory in os.listdir(tmp):
        if directory == "data":
            print " - Merging " + directory + " folder"
            for root, dirs, files in os.walk(os.path.join(tmp, directory)):
                for d in dirs:
                    path = os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], d)
                    if not os.path.exists(path):
                        os.makedirs(path)
                for f in files:
                    if f.endswith(".append"):
                        appendfile(os.path.join(root, f), os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], f[:-len(".append")]))
                    elif f.endswith(".append.xml"):
                        appendfile(os.path.join(root, f), os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], f[:-len(".append.xml")]+".xml"))
                    elif f.endswith(".merge"):
                        mergefile(os.path.join(root, f), os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], f[:-len(".merge")]))
                    elif f.endswith("merge.xml"):
                        mergefile(os.path.join(root, f), os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], f[:-len(".merge.xml")]+".xml"))
                    else:
                        sh.copy2(os.path.join(root, f), os.path.join(dir_res, "data.dat-unpacked", root[len(tmp)+1:], f))
                    
        elif directory in ("audio", "fonts", "img"):
            print " - Merging " + directory + " folder"
            for root, dirs, files in os.walk(os.path.join(tmp, directory)):
                for d in dirs:
                    path = os.path.join(dir_res, "resource.dat-unpacked", root[len(tmp)+1:], d)
                    if not os.path.exists(path):
                        os.makedirs(path)
                for f in files:
                    if f.endswith(".append"):
                        appendfile(os.path.join(root, f), os.path.join(dir_res, "resource.dat-unpacked", root[len(tmp)+1:], f[:-len(".append")]))
                    else:
                        sh.copy2(os.path.join(root, f), os.path.join(dir_res, "resource.dat-unpacked", root[len(tmp)+1:], f))
                        
        else:
            print " - WARNING: Unsupported folder " + directory
        
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
if platform.system() == "Windows":
    if msgbox.askyesno(progname, "Patching completed successfully. Run FTL now?"):
        os.system("\"" + os.path.join(dir_root, "FTLGame.exe") + "\"")
else:
    msgbox.showinfo(progname, "Patching completed successfully.")





