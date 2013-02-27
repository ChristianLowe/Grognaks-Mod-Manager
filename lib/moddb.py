import hashlib
import os
import random  # For debugging.
import re
import sys
import time
import urllib2


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

    def write_as_code(self, f):
        """Serializes the catalog as a python function.

        :param f: A file-like object to write to.
        """
        def slash(s):
            for c in ["\\","\""]:
                s = s.replace(c, "\\" + c)
            return s

        f.write("from lib import moddb\n")
        f.write("\n\n")
        f.write("def populate_catalog(mod_db):\n")

        for mod_info in self.catalog:
            f.write("    mod_info = moddb.ModInfo()\n")
            f.write("    mod_info.set_title( \"%s\" )\n" % slash(mod_info.get_title()))
            f.write("    mod_info.set_author( \"%s\" )\n" % slash(mod_info.get_author()))
            f.write("    mod_info.set_url( \"%s\" )\n" % slash(mod_info.get_url()))

            for (h, v) in mod_info.get_versions().items():
                f.write("    mod_info.put_version( \"%s\", \"%s\" )\n" % (slash(h), slash(v)))

            f.write("    mod_info.set_thread_hash( \"%s\" )\n" % slash(mod_info.get_thread_hash()))
            f.write("\n")
            f.write("    mod_info.set_desc(r\"\"\"%s\"\"\")\n" % mod_info.get_desc())
            f.write("    mod_db.add_mod(mod_info)\n")
            f.write("\n\n")

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


def _get_first_post(url):
    """Extracts the html content of the first post in a forum thread."""
    response = urllib2.urlopen(url, timeout=10)
    html_src = response.read()

    first_post_ptn = re.compile("<div class=\"postbody\"[^>]*>.*?<div class=\"content\"[^>]*>(.*?)</div>\\s*<dl class=\"postprofile\"[^>]*>", flags=re.DOTALL)

    post_content = ""
    m = first_post_ptn.search(html_src)
    if (m):
        post_content = m.group(1)
        post_content = re.sub("\r?\n", "", post_content)

        # Within content, but it counts clicks/views, which throws off hashing.
        post_content = re.sub("(?s)<div class=\"inline-attachment\">.*?</div>", "", post_content)

        # Footer junk.
        post_content = re.sub("(?s)<dl class=\"attachbox\">.*?<dl class=\"file\">.*?</dl>.*?</dl>", "", post_content)
        post_content = re.sub("(?s)<div (?:[^>]+ )?class=\"notice\">.*?</div>", "", post_content)
        post_content = re.sub("(?s)<div (?:[^>]+ )?class=\"signature\">.*?</div>", "", post_content)
        post_content = re.sub("</div>\\s*\\Z", "", post_content)  # From the content div (now that the others are gone).
        post_content = re.sub("\\A\\s+", "", post_content)
        post_content = re.sub("\\s+\\Z", "", post_content)

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

    mod_ptn = re.compile("^<a href=\"([^\"]+)\"[^>]*>([^>]+)</a>(?: *\\[[A-Za-z0-9 ]+\\])?[ -]*?Author: <a href=\"[^\"]+\"[^>]*>([^<]+?)</a> *((?:\\[WIP\\])?)")

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
        #if (random.randint(0,10) < 10): continue  # For debugging.
        if (forum_url_fragment not in results[i]["thread_url"]):
            continue  # Don't bother scraping and hashing non-forum urls.

        time.sleep(2)
        sys.stderr.write("\n")
        sys.stderr.write("Scraping mod %03d/%03d (%s)...\n" % ((i+1), len(results), results[i]["title"]))
        while (True):
            try:
                results[i]["raw_desc"] = _get_first_post(results[i]["thread_url"])
                results[i]["thread_hash"] = hashlib.md5(results[i]["raw_desc"]).hexdigest()
                break
            except (urllib2.HTTPError) as err:
                sys.stderr.write("Request failed: %s\n" % err.code)
            except (urllib2.URLError) as err:
                sys.stderr.write("Request failed: %s\n" % err.reason)
            except (OSError) as err:  # Socket timeout.
                sys.stderr.write("Request failed: %s\n" % err.reason)
            time.sleep(5)

    # Ignore threads whose hashes haven't changed.
    results = [x for x in results if (x["thread_hash"] not in boring_hashes)]

    # Scrub html out of descriptions and scrape download links.
    for result in results:
        post_content = result["raw_desc"]
        post_content = re.sub("<br */>", "\n", post_content)
        post_content = re.sub("<img [^>]*/>", "", post_content)
        post_content = re.sub("<span [^>]*>", "", post_content)
        post_content = re.sub("</span>", "", post_content)
        post_content = re.sub("&quot;", "\"", post_content)
        post_content = re.sub("\xe2\x80[\x98\x99]", "'", post_content)
        post_content = re.sub("&amp;", "&", post_content)
        post_content = re.sub("\xe2\x80\xa2", "-", post_content)
        post_content = re.sub("\xe2\x80\x93", "-", post_content)
        post_content = re.sub("\xc2\xa9", "()", post_content)
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

        post_content = re.sub("\\A\\s+", "", post_content)
        post_content = re.sub("\\s+\\Z", "", post_content)
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

    with open(new_db_path, "w") as f:
        new_db.write_as_code(f)


if (__name__ == "__main__"):
    main()
