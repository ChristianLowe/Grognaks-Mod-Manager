import datetime
import json
import logging
import os
import re
import sys

# Modules that changed in Python 3.x.
try:
    from urllib.request import Request
    from urllib.request import urlopen
except (ImportError) as err:
    from urllib2 import Request
    from urllib2 import urlopen

try:
    from urllib.error import HTTPError, URLError
except (ImportError) as err:
    from urllib2 import HTTPError, URLError

from lib import global_config


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

        # A dict of catalog flavors, indexed by a quoted-number.
        # When the structure changes, increment the number.
        # Legacy clients will look for the number they prefer.
        result["catalog_versions"] = {}

        result["catalog_versions"]["1"] = []
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

            result["catalog_versions"]["1"].append(mod_data)

        return json.dumps(result, ensure_ascii=True, allow_nan=False, sort_keys=True)

    def load_json(self, s):
        """Populates the catalog from a serialized json string.
        Call clear() first.

        :raises: ValueError if the json could not be parsed.
        """
        expected_catalog_version = "1"
        json_obj = json.loads(s)

        if ("catalog_versions" not in json_obj): return

        if (expected_catalog_version in json_obj["catalog_versions"]):
            for mod_data in json_obj["catalog_versions"][expected_catalog_version]:
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
            logging.warning("Unable to deserialize catalog version %s" % expected_catalog_version)

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


def fetch_newest_catalog(url, etag=None):
    """Downloads the latest mod catalog.

    :param url: The json catalog's address.
    :param etag: An HTTP header value to track modification; obtained from a previous call.
    :returns: A success boolean, the json string, and an etag string to pass next time, and . Or (False, None, None).
    """
    try:
        request = Request(url)
        if (etag):
            request.add_header("If-None-Match", etag)

        response = urlopen(request, timeout=10)

        response_info = response.info()
        if ((not etag) and "ETag" in response_info):
            etag = response_info["ETag"]

        json_str = response.read().decode("ascii")
        response.close()

        return (True, json_str, etag)

    except (HTTPError) as err:
        if (err.code == 304):  # 304 'Not Modified' is okay.
            logging.debug("The server's catalog has not been modified since the previous check.")
            return (True, None, None)
        else:
            logging.error("Catalog download request failed: HTTP Code %s" % err.code)

    except (URLError) as err:
        logging.error("Catalog download request failed: %s" % err.reason)
    except (OSError) as err:  # Socket timeout.
        logging.error("Catalog download request failed: %s" % err.reason)

    return (False, None, None)


def get_updated_db():
    """Returns a ModDB with the latest catalog, or None.
    If a previously downloaded json file exists, its datestamp will be examined.
    If the date's sufficiently old, a fresh one will be downloaded to overwrite it.
    If there's nothing new to download, the datestamp will be modified.
    Then, if a json file exists, it will be loaded into a new ModDB and returned.

    A text file containing an etag string will be saved alongside the json.
    An etag is a hash used in HTTP requests to avoid redownloading unchanged files.
    """
    json_path = os.path.join(global_config.dir_backup, "current_catalog.json")
    etag_path = os.path.join(global_config.dir_backup, "current_catalog_etag.txt")

    try:
        up_to_date = False
        if (os.path.isfile(json_path)):
            last_modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(json_path))
            logging.debug("Last catalog update: %s (local time)" % last_modified_date.strftime("%Y-%m-%d %H:%M:%S"))
            if (last_modified_date.today() - last_modified_date < global_config.CATALOG_DOWNLOAD_INTERVAL):
                logging.debug("Not bothering to download a newer catalog.")
                up_to_date = True

        if (not up_to_date):
            etag = None
            if (os.path.isfile(json_path) and os.path.isfile(etag_path)):
                try:
                    with open(etag_path, "rb") as etag_file:
                        etag = etag_file.read().decode("ascii")
                except (Exception) as err:
                    logging.debug("Failed to read cached catalog etag: " % str(err))

            logging.debug("Attempting to download a newer catalog...")
            outcome, json_str, etag = fetch_newest_catalog(global_config.CATALOG_URL, etag)

            if (outcome is True):
                if (json_str):
                    with open(json_path, "wb") as json_file:
                        json_file.write(json_str.encode("ascii"))
                if (etag):
                    with open(etag_path, "wb") as etag_file:
                        etag_file.write(etag.encode("ascii"))

                os.utime(json_path, None)  # Set access/modified timestamps to now.

    except (Exception) as err:
        logging.debug("Failed to fetch latest catalog: %s" % str(err))

    try:
        if (os.path.isfile(json_path)):
            json_str = None
            with open(json_path, "rb") as json_file:
                json_str = json_file.read().decode("ascii")

            new_db = ModDB()
            new_db.load_json(json_str)
            return new_db

    except (Exception) as err:
        logging.debug("Failed to load latest catalog: %s" % str(err))

    return None
