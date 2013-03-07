import json
import re
import sys


class ModDB(object):
    def __init__(self):
        self.catalog = []

    def get_mod_info(self, hash=None):
        if (hash is not None):
            for mod_info in self.catalog:
                if (mod_info.get_version(hash) is not None):
                    return mod_info
        return None

    def add_mod(self, mod_info):
        self.catalog.append(mod_info)

    def remove_mod(self, mod_info):
        self.catalog.remove(mod_info)

    def clear(self):
        self.catalog[:] = []

    def dump_json(self):
        """Serializes the catalog to a json string."""
        result = {}
        # An integer to increment when the class structure changes.
        result["catalog_version"] = 1

        result["catalog"] = []
        for mod_info in self.catalog:
            mod_data = {}
            mod_data["title"] = mod_info.get_title()
            mod_data["author"] = mod_info.get_author()
            mod_data["url"] = mod_info.get_url()

            mod_data["versions"] = []
            for (h, v) in mod_info.get_versions().items():
                mod_data["versions"].append({"hash":h, "version":v})

            mod_data["thread_hash"] = mod_info.get_thread_hash()
            mod_data["desc"] = mod_info.get_desc()

            result["catalog"].append(mod_data)

        return json.dumps(result, ensure_ascii=True, allow_nan=False, sort_keys=True)

    def load_json(self, s):
        """Populates the catalog from a serialized json string.
        Call clear() first.
        """
        json_obj = json.loads(s)

        if ("catalog_version" not in json_obj): return

        if (json_obj["catalog_version"] == 1):
            for mod_data in json_obj["catalog"]:
                mod_info = ModInfo()
                mod_info.set_title(mod_data["title"])
                mod_info.set_author(mod_data["author"])
                mod_info.set_url(mod_data["url"])

                for ver_data in mod_data["versions"]:
                    mod_info.put_version(ver_data["hash"], ver_data["version"])

                mod_info.set_thread_hash(mod_data["thread_hash"])
                mod_info.set_desc(mod_data["desc"])

                self.add_mod(mod_info)
        else:
            logging.warning("Unable to deserialize catalog version %s" % json_obj["catalog_version"])

    def write_as_code(self, f):
        """Serializes the catalog as a python function.

        :param f: A file-like object to write to (binary mode).
        """
        def slash(s):
            for c in ["\\","\""]:
                s = s.replace(c, "\\" + c)
            return s

        enc_type = "ascii"
        buf = ""
        buf += "# -*- coding: %s -*-\n" % enc_type
        buf += "# ^ Ascii chars are the norm in Python 2.x source code.\n"
        buf += "# This'll make a 3.x interpreter panic when any unicode sneaks in.\n"
        buf += "\n"
        buf += "from lib import moddb\n"
        buf += "\n\n"
        buf += "def populate_catalog(mod_db):\n"
        f.write(buf.encode(enc_type, "xmlcharrefreplace"))

        for mod_info in self.catalog:
            buf = ""
            buf += "    mod_info = moddb.ModInfo()\n"
            buf += "    mod_info.set_title( \"%s\" )\n" % slash(mod_info.get_title())
            buf += "    mod_info.set_author( \"%s\" )\n" % slash(mod_info.get_author())
            buf += "    mod_info.set_url( \"%s\" )\n" % slash(mod_info.get_url())

            for (h, v) in mod_info.get_versions().items():
                buf += "    mod_info.put_version( \"%s\", \"%s\" )\n" % (slash(h), slash(v))

            buf += "    mod_info.set_thread_hash( \"%s\" )\n" % slash(mod_info.get_thread_hash())
            buf += "\n"

            # Triple-quotes aren't allowed in the raw-string description.
            sanitized_desc = re.sub("\"\"\"", "", mod_info.get_desc())
            buf += "    mod_info.set_desc(r\"\"\"%s\"\"\")\n" % sanitized_desc

            buf += "    mod_db.add_mod(mod_info)\n"
            buf += "\n\n"
            f.write(buf.encode(enc_type, "xmlcharrefreplace"))


class ModInfo(object):
    def __init__(self):
        self._title = "???"
        self._author = "???"
        self._url = "???"
        self._thread_hash = "???"
        self._versions = {}
        self._desc = ""

    def set_title(self, s): self._title = s
    def get_title(self): return self._title

    def set_author(self, s): self._author = s
    def get_author(self): return self._author

    def set_url(self, s): self._url = s
    def get_url(self): return self._url

    def set_thread_hash(self, s): self._thread_hash = s
    def get_thread_hash(self): return self._thread_hash

    def put_version(self, hash, version):
        self._versions[hash] = version

    def get_version(self, hash):
        if (hash in self._versions):
            return self._versions[hash]
        return None

    def get_versions(self):
        """Returns a dict mapping hashes to versions of this mod.

        This method should be avoided to allow for possible
        redesign (as a list, etc.).
        """
        return self._versions

    def set_desc(self, s): self._desc = s
    def get_desc(self): return self._desc


def create_default_db():
    """Returns a ModDB filled with default mods."""
    # Delayed import avoids circular dependency issue.
    # That module imports this one. By now, this one is loaded.
    from lib import default_moddb

    new_db = ModDB()
    default_moddb.populate_catalog(new_db)
    return new_db
