import hashlib
import json
import os
import re
import sys
import time

# Modules that changed in Python 3.x.
try:
    from urllib.request import urlopen
except (ImportError) as err:
    from urllib2 import urlopen

try:
    from urllib.error import HTTPError, URLError
except (ImportError) as err:
    from urllib2 import HTTPError, URLError


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
        f.write(buf.encode(enc_type, errors="xmlcharrefreplace"))

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
            buf += "    mod_info.set_desc(r\"\"\"%s\"\"\")\n" % mod_info.get_desc()
            buf += "    mod_db.add_mod(mod_info)\n"
            buf += "\n\n"
            f.write(buf.encode(enc_type, errors="xmlcharrefreplace"))


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


# What follows is a standalone app to scrape the FTL forum's
# Master Mod List for new/updated entries to edit into the default_moddb...
#
# To use it:
#   cd .../GMM/
#   python -m lib.moddb
#   After a while, a text file will appear in that folder.
#   Compare it with GMM/lib/default_moddb.py to edit in new info.
#   For hashes, download each new mod and either:
#       Run: md5sum -b blah.ftl
#       Or select it in GMM to copy the hash reported by the gui/log.


# Make both Python 3.x and 2.x use unicode.
if (sys.hexversion >= 0x030000a0):
    # At least Python 3.0.0 alpha0
    # (aN=alpha #N, cN=candidate #N, f0=final).
    def u(x):
        return x  # It's already unicode.
else:
    # Python 2.x.
    import codecs
    def u(x):
        return codecs.unicode_escape_decode(x)[0]


def _get_first_post(url):
    """Extracts the html content of the first post in a forum thread."""
    # Download and decode bytes as unicode.
    response = urlopen(url, timeout=10)
    html_src = response.read().decode("utf-8")

    first_post_ptn = re.compile("(?u)<div class=\"postbody\"[^>]*>.*?<div class=\"content\"[^>]*>(.*?)</div>\\s*<dl class=\"postprofile\"[^>]*>", flags=re.DOTALL)

    post_content = ""
    m = first_post_ptn.search(html_src)
    if (m):
        post_content = m.group(1)
        post_content = re.sub("(?u)\r?\n", "", post_content)

        # Within content, but it counts clicks/views, which throws off hashing.
        post_content = re.sub("(?su)<div class=\"inline-attachment\">.*?</div>", "", post_content)

        # Footer junk.
        post_content = re.sub("(?su)<dl class=\"attachbox\">.*?<dl class=\"file\">.*?</dl>.*?</dl>", "", post_content)
        post_content = re.sub("(?su)<div (?:[^>]+ )?class=\"notice\">.*?</div>", "", post_content)
        post_content = re.sub("(?su)<div (?:[^>]+ )?class=\"signature\">.*?</div>", "", post_content)
        post_content = re.sub("(?u)</div>\\s*\\Z", "", post_content)  # From the content div (now that the others are gone).
        post_content = re.sub("(?u)\\A\\s+", "", post_content)
        post_content = re.sub("(?u)\\s+\\Z", "", post_content)

    return post_content


def _scrape_master_list(known_db=None, ignored_urls=None):
    """Scrape the Master Mod List on the FTL forum.
    If an existing ModDB is provided, its thread urls will be checked too.

    :param known_db: A ModDB with mods to ignore if thread_hash is unchanged.
    :param ignored_urls: A list of uninteresting thread_urls to ignore.
    :return: A list of result dicts.
    """
    master_list_url = "http://www.ftlgame.com/forum/viewtopic.php?f=11&t=2645"

    mods_header_ptn = re.compile(re.escape("<span style=\"font-weight: bold\"><span style=\"text-decoration: underline\"><span style=\"font-size: 150%; line-height: 116%;\">Mods</span></span></span>"))

    mod_ptn = re.compile("(?u)^<a href=\"([^\"]+)\"[^>]*>([^>]+)</a>(?: *\\[[A-Za-z0-9 ]+\\])?[ -]*?Author: <a href=\"[^\"]+\"[^>]*>([^<]+?)</a> *((?:\\[WIP\\])?)")

    forum_url_fragment = "http://www.ftlgame.com/forum/viewtopic.php"

    boring_hashes = []
    if (known_db is not None):
        for mod_info in known_db.catalog:
            if (mod_info.get_thread_hash() != "???"):
                boring_hashes.append(mod_info.get_thread_hash())

    sys.stderr.write("\n")
    sys.stderr.write("Scraping Master Mod List...\n")
    post_content = _get_first_post(master_list_url)
    post_content = re.sub("<br */>", "\n", post_content)

    lines = post_content.split("\n")
    results = []
    in_mods = False

    for line in lines:
        if (mods_header_ptn.search(line)):
            in_mods = True
            continue
        if (not in_mods): continue

        m = mod_ptn.match(line)
        if (m):
            result = {}
            result["thread_url"] = m.group(1)
            result["title"] = m.group(2)
            result["author"] = m.group(3)
            result["wip"] = True if (m.group(4)=="[WIP]") else False
            result["raw_desc"] = ""
            result["thread_hash"] = "???"

            result["title"] = re.sub("&amp;", "&", result["title"])
            result["thread_url"] = re.sub("&amp;", "&", result["thread_url"])
            results.append(result)

    # Merge extra mods from known_db into the results list to scrape.
    if (known_db is not None):
        pending_urls = [x["thread_url"] for x in results]
        for mod_info in known_db.catalog:
            if (mod_info.get_url() is not "???" and mod_info.get_url() not in pending_urls):
                pending_urls.append(mod_info.get_url())
                new_result = {}
                new_result["thread_url"] = mod_info.get_url()
                new_result["title"] = mod_info.get_title()
                new_result["author"] = mod_info.get_author()
                new_result["wip"] = False  # Shrug
                new_result["raw_desc"] = mod_info.get_desc()
                new_result["thread_hash"] = mod_info.get_thread_hash()
                results.append(new_result)

    # Prune results with boring urls.
    if (ignored_urls):
        results = [x for x in results if (x["thread_url"] not in ignored_urls)]

    # Fetch and hash each thread url.
    for i in range(len(results)):
        if (forum_url_fragment not in results[i]["thread_url"]):
            continue  # Don't bother scraping and hashing non-forum urls.

        time.sleep(2)
        sys.stderr.write("\n")
        sys.stderr.write("Scraping mod %03d/%03d (%s)...\n" % ((i+1), len(results), results[i]["title"]))
        while (True):
            try:
                results[i]["raw_desc"] = _get_first_post(results[i]["thread_url"])
                # Encode the str/unicode string to bytes.
                results[i]["thread_hash"] = hashlib.md5(results[i]["raw_desc"].encode("utf-8")).hexdigest()
                break
            except (HTTPError) as err:
                sys.stderr.write("Request failed: %s\n" % err.code)
            except (URLError) as err:
                sys.stderr.write("Request failed: %s\n" % err.reason)
            except (OSError) as err:  # Socket timeout.
                sys.stderr.write("Request failed: %s\n" % err.reason)
            time.sleep(5)

    # Ignore threads whose hashes haven't changed.
    results = [x for x in results if (x["thread_hash"] not in boring_hashes)]

    # Scrub html out of descriptions and scrape download links.
    for result in results:
        # Unicode reminder: Prepend (?u) before regexes with: \w,\W,\b,\B,\d,\D,\s,\S.
        post_content = result["raw_desc"]
        post_content = re.sub("<br */>", "\n", post_content)
        post_content = re.sub("<img [^>]*/>", "", post_content)
        post_content = re.sub("<span [^>]*>", "", post_content)
        post_content = re.sub("</span>", "", post_content)
        post_content = re.sub("&quot;", "\"", post_content)
        post_content = re.sub(u("\u2018|\u2019"), "'", post_content)
        post_content = re.sub(u("\u2022"), "-", post_content)
        post_content = re.sub(u("\u2013"), "-", post_content)
        post_content = re.sub(u("\u00a9"), "()", post_content)
        post_content = re.sub("&amp;", "&", post_content)
        post_content = re.sub("<a (?:[^>]+ )?href=\"([^\"]+)\"[^>]*>", "<a href=\"\\g<1>\">", post_content)
        post_content = re.sub("<a href=\"[^\"]+/forum/memberlist.php[^\"]+\"[^>]*>([^<]+)</a>", "\\g<1>", post_content)
        post_content = re.sub("<a href=\"http://(?:i.imgur.com/|[^\"]*photobucket.com/|[^\"]*deviantart.com/|www.mediafire.com/view/[?])[^\"]+\"[^>]*>([^<]+)</a>", "\\g<1>", post_content)
        post_content = re.sub("<a href=\"([^\"]+)\"[^>]*>(?:\\1|[^<]+ [.][.][.] [^<]+)</a>", "<a href=\"\\g<1>\">Link</a>", post_content)
        post_content = re.sub("<a href=\"[^\"]+[.](?:jpg|png)(?:[.]html)?\"[^>]*>([^<]*)</a>", "\\g<1>", post_content)
        post_content = re.sub("<a href=\"([^\"]+)\"[^>]*></a>", "\\g<1>", post_content)
        post_content = re.sub("</li><li>", "</li>\n<li>", post_content)
        post_content = re.sub("<li>(.*?)</li>", " - \\g<1>", post_content)
        post_content = re.sub("<li>", " - ", post_content)
        post_content = re.sub("</li>", "", post_content)
        post_content = re.sub("</?ul>", "", post_content)
        post_content = re.sub("(?s)<blockquote [^>]+><div>(.*?)</div></blockquote>", "<blockquote>\\g<1></blockquote>", post_content)
        post_content = re.sub("<!-- [^>]+ -->", "", post_content)

        # Link to GMM Thread
        post_content = re.sub("<a href=\"[^\"]+/forum/viewtopic.php?(?:[^&]+&)*t=2464\"[^>]*>([^<]+)</a>", "\\g<1>", post_content)
        # Link to Superluminal Thread
        post_content = re.sub("<a href=\"[^\"]+/forum/viewtopic.php?(?:[^&]+&)*t=11251\"[^>]*>([^<]+)</a>", "\\g<1>", post_content)
        # Link to FTLEdit Thread
        post_content = re.sub("<a href=\"[^\"]+/forum/viewtopic.php?(?:[^&]+&)*t=2959\"[^>]*>([^<]+)</a>", "\\g<1>", post_content)

        post_content = re.sub("(?u)\\A\\s+", "", post_content)
        post_content = re.sub("(?u)\\s+\\Z", "", post_content)
        result["raw_desc"] = post_content +"\n"  # Triple-quoting looks better with a newline.

    return results


def main():
    new_db_path = "./new_mod_db.txt"

    ignored_urls = []
    ignored_urls.append("http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11561")
    ignored_urls.append("http://www.ftlgame.com/forum/viewtopic.php?f=12&t=11083")
    ignored_urls.append("http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2938")
    ignored_urls.append("http://www.moddb.com/mods/better-planets-and-backgrounds/downloads/better-asteroids")
    # Beginning Scrap Advantage is bundled in GMM.
    ignored_urls.append("http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2464")

    known_db = create_default_db()

    try:
        os.unlink(new_db_path)
    except(Exception) as err:
        pass

    results = _scrape_master_list(known_db=known_db, ignored_urls=ignored_urls)

    new_db = ModDB()
    for result in results:
        mod_info = ModInfo()
        mod_info.set_title(result["title"])
        mod_info.set_author(result["author"])
        mod_info.set_url(result["thread_url"])
        mod_info.set_desc(result["raw_desc"])
        mod_info.put_version("???", "???"+ (" WIP" if result["wip"] else ""))
        mod_info.set_thread_hash(result["thread_hash"])
        new_db.add_mod(mod_info)

    with open(new_db_path, "wb") as f:
        new_db.write_as_code(f)


if (__name__ == "__main__"):
    main()
