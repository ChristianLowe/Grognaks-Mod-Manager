#!/usr/bin/env python

# Do some basic imports, and set up logging to catch ImportError.
import inspect
import locale
import logging
import os
import sys

if (__name__ == "__main__"):
    global dir_self
    locale.setlocale(locale.LC_ALL, "")

    # Get the un-symlinked, absolute path to this module.
    dir_self = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
    if (dir_self not in sys.path): sys.path.insert(0, dir_self)

    # Go to this module's dir.
    os.chdir(dir_self)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    logstream_handler = logging.StreamHandler()
    logstream_formatter = logging.Formatter("%(levelname)s: %(message)s")
    logstream_handler.setFormatter(logstream_formatter)
    logstream_handler.setLevel(logging.INFO)
    logger.addHandler(logstream_handler)

    logfile_handler = logging.FileHandler(os.path.join(dir_self, "modman-log.txt"), mode="w")
    logfile_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")
    logfile_handler.setFormatter(logfile_formatter)
    logger.addHandler(logfile_handler)

    # __main__ stuff is continued at the end of this file.


# Import everything else (tkinter may be absent in some environments).
try:
    from ConfigParser import SafeConfigParser
    import errno
    import glob
    import platform
    import re
    import shutil as sh
    import tempfile as tf
    import webbrowser
    import zipfile as zf
    import Tkinter as tk
    import tkFileDialog
    import tkMessageBox as msgbox

    # Modules bundled with this script.
    from ftldat import FTLDatUnpacker as du
    from ftldat import FTLDatPacker as dp

except (Exception) as err:
    logging.exception(err)
    sys.exit(1)


# Declare globals.
APP_VERSION = "1.6"
APP_NAME = "Grognak's Mod Manager v%s" % APP_VERSION
allowzip = False
cfg = None
modname_list = None  # Available mod names.
merge_list = None    # Mod names to merge, selected in the GUI.
dir_mods = None
dir_res = None


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

        # Our topmost frame is called rootframe.
        self.rootframe = tk.Frame(self)
        self.rootframe.pack()

        # Top frame (container).
        self.top_frame = tk.Frame(self.rootframe)
        self.top_frame.pack(side="top", fill="both", expand="yes")

        # Top-left frame (mod list).
        self.left_frame = tk.Frame(self.top_frame, #background="red",
            borderwidth=1, relief="ridge",
            width=50, height=250)
        self.left_frame.pack(side="left", fill="both", expand="yes")

        # Top-right frame (buttons).
        self.right_frame = tk.Frame(self.top_frame, width=250)
        self.right_frame.pack(side="right", fill="y", expand="no")

        # Bottom frame (mod descriptions).
        self.bottom_frame = tk.Frame(self.rootframe,
            borderwidth=3, relief="ridge",
            height=50)
        self.bottom_frame.pack(side="top", fill="both", expand="yes")

        # Add a listbox to hold the mod names.
        self.modlistbox = tk.Listbox(self.left_frame, width=30, height=1, selectmode="multiple") # Height readjusts itself for the button frame
        self.modlistbox.pack(side="left", fill="both", expand="yes")
        self.modscrollbar = tk.Scrollbar(self.left_frame, command=self.modlistbox.yview, orient="vertical")
        self.modscrollbar.pack(side="right", fill="y")
        self.modlistbox.bind("<<ListboxSelect>>", self._on_listbox_select)
        self.modlistbox.configure(yscrollcommand=self.modscrollbar.set)

        # Add textbox at bottom to hold mod information.
        self.descbox = tk.Text(self.bottom_frame, width=60, height=10, wrap="word")
        self.descbox.pack(fill="both", expand="yes")

        # Set formating tags.
        self.descbox.tag_configure("title", font="helvetica 24 bold")

        # Add the buttons to the buttons frame.
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
        global APP_VERSION
        global modname_list

        # Set default description.
        self._set_description("Grognak's Mod Manager", "Grognak", APP_VERSION, "Thanks for using GMM. Make sure to periodically check the forum for updates!")

        # Get list of mods the player wants to be patched in.
        for mod in modname_list:
            self._add_mod(mod, False)

    def _on_listbox_select(self, event):
        curlist = self.modlistbox.curselection()
        newset = [x for x in curlist if (x not in self.oldlist)]
        self.oldlist = set(curlist)

        if (len(newset) > 0):
            self._set_description(self.modlistbox.get(newset[0]))

    def _add_mod(self, modname, selected):
        """Add a mod name to the list."""
        newitem = self.modlistbox.insert(tk.END, modname)
        if (selected):
            self.modlistbox.selection_set(newitem)

    def _set_description(self, title, author=None, version=None, description=None):
        """Sets the currently displayed mod description."""
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
        global merge_list
        merge_list = [self.modlistbox.get(mod_name) for mod_name in self.modlistbox.curselection()]
        self._die()

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
    # Not completely implemented yet, so button is disabled.

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

        # Top frame.
        self.top_frame = tk.Frame(self.rootframe)
        self.top_frame.pack(side="top", fill="both", expand="yes")

        # Left frame.
        self.left_frame = tk.Frame(self.top_frame, #background="red",
            borderwidth=1, relief="ridge",
            width=50, height=250)
        self.left_frame.pack(side="left", fill="both", expand="yes")

        # Right frame.
        self.right_frame = tk.Frame(self.top_frame,
            width=250)
        self.right_frame.pack(side="right", fill="y", expand="no")

        # Add a listbox to hold the mod names.
        self.modlistbox = tk.Listbox(self.left_frame, width=30, height=1) # Height readjusts itself for the button frame
        self.modlistbox.pack(side="left", fill="both", expand="yes")
        self.modlistbox.bind("<<ListboxSelect>>", self._on_listbox_select)
        self.modscrollbar = tk.Scrollbar(self.left_frame, command=self.modlistbox.yview, orient="vertical")
        self.modscrollbar.pack(side="right", fill="y")
        self.modlistbox.configure(yscrollcommand=self.modscrollbar.set)


        # Add the buttons to the buttons frame.
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

def packdat(unpack_dir, dat_path):
    logging.info("")
    logging.info("Repacking %s" % os.path.basename(dat_path))
    logging.info("Listing files to pack...")
    s = [()]
    files = []
    while s:
        current = s.pop()
        for child in os.listdir(os.path.join(unpack_dir, *current)):
            full_path = os.path.join(unpack_dir, *(current + (child,)))
            if (os.path.isfile(full_path)):
                files.append(current + (child,))
            elif (os.path.isdir(full_path)):
                s.append(current + (child,))
    logging.info("Creating datfile...")
    index_size = len(files)
    packer = dp(open(dat_path, "wb"), index_size)
    logging.info("Packing...")
    for _file in files:
        full_path = os.path.join(unpack_dir, *_file)
        size = os.stat(full_path).st_size
        with open(full_path, "rb") as f:
            packer.add(ftl_path_join(*_file), f, size)

def unpackdat(dat_path, unpack_dir):
    logging.info("Unpacking %s..." % os.path.basename(dat_path))
    unpacker = du(open(dat_path, "rb"))

    for i, filename, size, offset in unpacker:
        target = os.path.join(unpack_dir, filename)
        if (not os.path.exists(os.path.dirname(target))):
            os.makedirs(os.path.dirname(target))
        with open(target, "wb") as f:
            unpacker.extract_to(filename, f)

def is_dats_path_valid(dats_path):
    """Returns True if the path exists and contains data.dat."""
    return (os.path.isdir(dats_path) and os.path.isfile(os.path.join(dats_path, "data.dat")))

def find_ftl_path():
    """Returns a valid guessed path to FTL resources, or None."""
    steam_chunks = ["Steam","steamapps","common","FTL Faster Than Light","resources"];
    gog_chunks = ["GOG.com","Faster Than Light","resources"];

    home_path = os.path.expanduser("~")

    xdg_data_home = os.getenv("XDG_DATA_HOME")
    if (not xdg_data_home):
        xdg_data_home = os.path.join(home_path, *[".local","share"])

    candidates = []
    # Windows - Steam
    candidates.append(os.path.join(os.getenv("ProgramFiles(x86)", ""), *steam_chunks))
    candidates.append(os.path.join(os.getenv("ProgramFiles", ""), *steam_chunks))
    # Windows - GOG
    candidates.append(os.path.join(os.getenv("ProgramFiles(x86)", ""), *gog_chunks))
    candidates.append(os.path.join(os.getenv("ProgramFiles", ""), *gog_chunks))
    # Linux - Steam
    candidates.append(os.path.join(xdg_data_home, *["Steam","SteamApps","common","FTL Faster Than Light","data","resources"]))
    # OSX - Steam
    candidates.append(os.path.join(home_path, *["Library","Application Support","Steam","SteamApps","common","FTL Faster Than Light","FTL.app","Contents","Resources"]))
    # OSX
    candidates.append(os.path.join("/", *["Applications","FTL.app","Contents","Resources"]))

    result = None
    for c in candidates:
        if (is_dats_path_valid(c)):
            result = c
    return result

def prompt_for_ftl_path():
    """Returns a path to FTL resources chosen by the user, or None."""
    global APP_NAME

    message = ""
    message += "The path to FTL's resources could not be guessed.\n\n";
    message += "You will now be prompted to locate FTL manually.\n";
    message += "Select '(FTL dir)/resources/data.dat'.\n";
    message += "Or 'FTL.app', if you're on OSX.";
    msgbox.showinfo(APP_NAME, message)

    result = tkFileDialog.askopenfilename(title="Find data.dat or FTL.app",
        filetypes=[("data.dat or OSX Bundle", "data.dat;FTL.app")])

    if (result):
        if (os.path.basename(result) == "data.dat"):
            result = os.path.split(result)[0]
        elif (os.path.splitext(result)[1] == ".app" and os.path.isdir(result)):
            if (os.path.isdir(os.path.join(result, *["Contents","Resources"]))):
                result = os.path.join(result, *["Contents","Resources"])
        if (result and is_dats_path_valid(result)):
            return result

    return None

def find_mod(mod_name):
    """Returns the full path to a mod file, or None."""
    global allowzip
    global dir_mods

    suffixes = ["", ".ftl"]
    if (allowzip): suffixes.append(".zip")

    for suffix in suffixes:
        tmp_path = os.path.join(dir_mods, mod_name + suffix)
        if (os.path.isfile(tmp_path)):
            return tmp_path

    logging.debug("Failed to find mod file by name: %s" % mod_name)
    return None

def load_modorder():
    """Reads the modorder, syncs it with existing files, and returns it."""
    global allowzip
    global dir_mods

    modorder_lines = []
    try:
        # Translate mod names to full filenames, temporarily.
        with open(os.path.join(dir_mods, "modorder.txt"), "r") as modorder_file:
            modorder_lines = modorder_file.readlines()
            modorder_lines = [line.strip() for line in modorder_lines]
            modorder_lines = [find_mod(line) for line in modorder_lines]
            modorder_lines = [line for line in modorder_lines if (line is not None)]
            modorder_lines = [os.path.basename(line) for line in modorder_lines]
    except (IOError) as err:
        if (err.errno == errno.ENOENT):  # No such file/dir.
            pass
        else:
            raise

    mod_exts = ["ftl"]
    if (allowzip): mod_exts.append("zip")

    # Get a list of full filenames.
    mod_filenames = []
    for ext in mod_exts:
        ext_filenames = glob.glob(os.path.join(dir_mods, "*."+ext))
        ext_filenames = [os.path.basename(f) for f in ext_filenames]
        mod_filenames.extend(ext_filenames)

    # Purge modorder lines that have no corresponding filename.
    dead_mods = [f for f in modorder_lines if (f not in mod_filenames)]
    for f in dead_mods:
        modorder_lines.remove(f)
        logging.info("Removed %s" % f)

    # Append filenames not mentioned in the modorder.
    new_mods = [f for f in mod_filenames if (f not in modorder_lines)]
    for f in new_mods:
        modorder_lines.append(f)
        logging.info("Added %s" % f)

    # Strip extensions to get mod_names.
    ext_ptn = "[.](?:"+ ("|".join(mod_exts)) +")$"
    modorder_lines = [re.sub(ext_ptn, "", f, flags=re.I) for f in modorder_lines]

    return modorder_lines

def save_modorder(modorder_lines):
    global dir_mods
    with open(os.path.join(dir_mods, "modorder.txt"), "w") as modorder_file:
        modorder_file.write("\n".join(modorder_lines) +"\n")

def patch_dats():
    """Backs up, clobbers, unpacks, merges, and finally packs dats."""
    global allowzip
    global dir_self, dir_mods, dir_res
    global merge_list

    # Get full paths from mod names.
    mod_list = [find_mod(mod_name) for mod_name in merge_list]
    mod_list = [mod_path for mod_path in mod_list if (mod_path is not None)]

    data_dat_path = os.path.join(dir_res, "data.dat")
    resource_dat_path = os.path.join(dir_res, "resource.dat")

    data_bak_path = os.path.join(dir_res, "data.dat.bak")
    resource_bak_path = os.path.join(dir_res, "resource.dat.bak")

    data_unp_path = os.path.join(dir_res, "data.dat-unpacked")
    resource_unp_path = os.path.join(dir_res, "resource.dat-unpacked")

    unp_map = {}
    for x in ["data"]:
        unp_map[x] = data_unp_path
    for x in ["audio", "fonts", "img"]:
        unp_map[x] = resource_unp_path

    tmp = None

    try:
        # Create backup dats, if necessary.
        for (dat_path, bak_path) in [(data_dat_path,data_bak_path), (resource_dat_path,resource_bak_path)]:
            if (not os.path.isfile(bak_path)):
                logging.info("Backing up %s" % os.path.basename(dat_path))
                sh.copy2(dat_path, bak_path)

        # Clobber current dat files with their respective backups.
        for (dat_path, bak_path) in [(data_dat_path,data_bak_path), (resource_dat_path,resource_bak_path)]:
            sh.copy2(bak_path, dat_path)

        if (len(mod_list) == 0):
            return True  # No mods. Skip the repacking.

        # Delete old unpack dirs from previous patching.
        for unpack_dir in (data_unp_path, resource_unp_path):
            sh.rmtree(unpack_dir, ignore_errors=True)
            if (os.path.exists(unpack_dir)):
                logging.warning("Failed to delete existing unpack folder: %s" % unpack_dir)

        # Extract both of the dats.
        unpackdat(data_dat_path, data_unp_path)
        unpackdat(resource_dat_path, resource_unp_path)

        # Extract each mod into a temp dir and merge into unpacked dat dirs.
        for mod_path in mod_list:
            try:
                logging.info("")
                logging.info("Installing mod: %s" % os.path.basename(mod_path))
                tmp = tf.mkdtemp()
                with zf.ZipFile(mod_path, "r") as mod_zip:
                    # Unzip everything into a temporary folder.
                    for item in mod_zip.namelist():
                        if (item.endswith("/")):
                            path = os.path.join(tmp, item)
                            if (not os.path.exists(path)):
                                os.makedirs(path)
                        else:
                            mod_zip.extract(item, tmp)

                # Go through each directory in the mod.
                for directory in os.listdir(tmp):
                    if (directory in unp_map):
                        logging.info("Merging folder: %s" % directory)
                        unpack_dir = unp_map[directory]
                        for root, dirs, files in os.walk(os.path.join(tmp, directory)):
                            for d in dirs:
                                path = os.path.join(unpack_dir, root[len(tmp)+1:], d)
                                if (not os.path.exists(path)):
                                    os.makedirs(path)
                            for f in files:
                                if (f.endswith(".append")):
                                    appendfile(os.path.join(root, f), os.path.join(unpack_dir, root[len(tmp)+1:], f[:-len(".append")]))
                                elif (f.endswith(".append.xml")):
                                    appendfile(os.path.join(root, f), os.path.join(unpack_dir, root[len(tmp)+1:], f[:-len(".append.xml")]+".xml"))
                                elif (f.endswith(".merge")):
                                    mergefile(os.path.join(root, f), os.path.join(unpack_dir, root[len(tmp)+1:], f[:-len(".merge")]))
                                elif (f.endswith("merge.xml")):
                                    mergefile(os.path.join(root, f), os.path.join(unpack_dir, root[len(tmp)+1:], f[:-len(".merge.xml")]+".xml"))
                                else:
                                    sh.copy2(os.path.join(root, f), os.path.join(unpack_dir, root[len(tmp)+1:], f))

                    else:
                        logging.warning("Unsupported folder: %s" % directory)

            finally:
                # Clean up temporary folder's contents.
                if (tmp is not None):
                    sh.rmtree(tmp, ignore_errors=True)
                    tmp = None

        # All the mods are installed, so repack the files.
        packdat(data_unp_path, data_dat_path)
        packdat(resource_unp_path, resource_dat_path)

        return True  # The finally block will still run.

    finally:
        # Delete unpack folders.
        for unpack_dir in (data_unp_path, resource_unp_path):
            sh.rmtree(unpack_dir, ignore_errors=True)
            if (os.path.exists(unpack_dir)):
                logging.warning("Failed to delete unpack folder: %s" % unpack_dir)

    return False


def main():
    global APP_NAME
    global allowzip
    global dir_self, dir_mods, dir_res
    global cfg, modname_list, merge_list

    # dir_self was set earlier.
    dir_mods = os.path.join(dir_self, "mods")
    dir_res = None  # Set this later.

    try:
        logging.info("%s (on %s)" % (APP_NAME, platform.platform(aliased=True, terse=False)))
        logging.info("Rooting at: %s\n" % dir_self)

        # Load up config file values.
        cfg = SafeConfigParser()
        cfg.add_section("settings")

        # Set defaults.
        cfg.set("settings", "allowzip", ("1" if (allowzip is True) else "0"))

        write_config = False
        try:
            with open(os.path.join(dir_self, "modman.ini"), "r") as cfg_file:
                cfg.readfp(cfg_file)
        except (Exception) as err:
            write_config = True

        if (cfg.has_option("settings", "allowzip")):
            allowzip = cfg.getboolean("settings", "allowzip")

        if (cfg.has_option("settings", "ftl_dats_path")):
            dir_res = cfg.get("settings", "ftl_dats_path")

        if (cfg.has_option("settings", "macmodsdir")):  # Deprecated.
            cfg.remove_option("settings", "macmodsdir")

        if (dir_res):
            logging.info("Using FTL dats path from config: %s" % dir_res)
            if (not is_dats_path_valid(dir_res)):
                logging.error("The config's ftlDatsPath does not exist, or it lacks data.dat.")
        else:
            logging.debug("No FTL dats path previously set.")

        # Find/prompt for the path to set in the config.
        if (not dir_res):
            dir_res = find_ftl_path()
            if (dir_res):
                if (not msgbox.askyesno(APP_NAME, "FTL resources were found in:\n%s\nIs this correct?" % dir_res)):
                    dir_res = None

            if (not dir_res):
                logging.debug("FTL dats path was not located automatically. Prompting user for location.")
                dir_res = prompt_for_ftl_path()

            if (dir_res):
                cfg.set("settings", "ftl_dats_path", dir_res)
                write_config = True
                logging.info("FTL dats located at: %s" % dir_res)

        if (not dir_res):
            logging.debug("No FTL dats path found, exiting.")
            sys.exit(1)

        if (write_config):
            with open(os.path.join(dir_self, "modman.ini"), "w") as cfg_file:
                cfg_file.write("#\n")
                cfg_file.write("# allowzip - Sets whether to treat .zip files as .ftl files. Default: 0 (false).\n")
                cfg_file.write("# ftl_dats_path - The path to FTL's resources folder. If invalid, you'll be prompted.\n")
                cfg_file.write("#\n")
                cfg_file.write("# macmodsdir - Deprecated. Each OS keeps mods in GMM/mods/ now.\n")
                cfg_file.write("#\n")
                cfg_file.write("\n")
                cfg.write(cfg_file)

        modname_list = load_modorder()
        save_modorder(modname_list)

        # Start the GUI.
        root = tk.Tk()
        root.withdraw()

        # Tkinter mainloop doesn't normally die and let its exceptions be caught.
        def tk_error_func(exc, val, tb):
            logging.exception("%s" % exc)
            root.destroy()
        root.report_callback_exception = tk_error_func

        mygui = MainWindow(master=root, title=APP_NAME)

        root.mainloop()

        if (merge_list is None):  # User didn't click the "Patch" button.
            sys.exit(0)

        patch_dats()

        # TODO: Move patching into a separate thread with a queued
        # callback on completion, so the GUI thread can stay alive
        # to show the following prompts.

        # All done!
        if (platform.system() == "Windows"):
            if (msgbox.askyesno(APP_NAME, "Patching completed successfully. Run FTL now?")):
                os.system("\"%s\"" % os.path.join(dir_self, "FTLGame.exe"))
        else:
            msgbox.showinfo(APP_NAME, "Patching completed successfully.")

    except (Exception) as err:
        logging.exception(err)


if (__name__ == "__main__"):
    main()
