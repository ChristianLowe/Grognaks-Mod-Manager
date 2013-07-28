#
# What follows is a standalone app to scrape the FTL forum's
# Master Mod List for new/updated entries to edit into default_moddb.py...
#
# To use it:
#     Scrape for new entries.
#         cd .../GMM/
#         python -m lib.moddb_updater --scrape
#
#     After a while, a text file will appear in that folder.
#     Compare it with GMM/lib/default_moddb.py to edit in new info.
#     For hashes, download each new mod and either:
#         Run: md5sum -b blah.ftl
#         Or select it in GMM to copy the hash reported by the gui/log.
#
#     Dump the updated database.
#         python -m lib.moddb_updater --dump-json
#
#     A json file will appear in that folder.
#     Copy it to GMM/backup/
#     Commit the json and default_moddb.py to the repository.
#

import hashlib
import os
import re
import sys
import time

from lib import moddb

# Modules that changed in Python 3.x.
try:
    from urllib.request import urlopen
except (ImportError) as err:
    from urllib2 import urlopen

try:
    from urllib.error import HTTPError, URLError
except (ImportError) as err:
    from urllib2 import HTTPError, URLError


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

    mod_ptn = re.compile("(?u)^(?:\\[[A-Za-z0-9 ]+ *\\])?<a href=\"([^\"]+)\"[^>]*>([^>]+)</a> *((?:\\[[A-Za-z0-9 ]+\\])?)(?: (?:.*?))? - Author: <a href=\"[^\"]+\"[^>]*>([^<]+?)</a>")

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
            result["author"] = m.group(4)
            result["wip"] = True if (m.group(3)=="[WIP]") else False
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


def _scrape():
    """Scrapes the forum and write python-serialized code for changed posts to a file."""
    new_db_path = "./new_mod_db.txt"

    ignored_urls = []
    ignored_urls.append("http://www.ftlgame.com/forum/viewtopic.php?f=11&t=11561")
    ignored_urls.append("http://www.ftlgame.com/forum/viewtopic.php?f=12&t=11083")
    ignored_urls.append("http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2938")
    ignored_urls.append("http://www.moddb.com/mods/better-planets-and-backgrounds/downloads/better-asteroids")
    # SpaceDock is an app.
    ignored_urls.append("http://www.ftlgame.com/forum/viewtopic.php?f=11&t=16842");
    # Beginning Scrap Advantage is bundled in GMM.
    ignored_urls.append("http://www.ftlgame.com/forum/viewtopic.php?f=4&t=2464")

    known_db = moddb.create_default_db()

    try:
        os.unlink(new_db_path)
    except(Exception) as err:
        pass

    results = _scrape_master_list(known_db=known_db, ignored_urls=ignored_urls)

    new_db = moddb.ModDB()
    for result in results:
        mod_info = moddb.ModInfo()
        mod_info.set_title(result["title"])
        mod_info.set_author(result["author"])
        mod_info.set_url(result["thread_url"])
        mod_info.set_desc(result["raw_desc"])
        mod_info.put_version("???", "???"+ (" WIP" if result["wip"] else ""))
        mod_info.set_thread_hash(result["thread_hash"])
        new_db.add_mod(mod_info)

    with open(new_db_path, "wb") as f:
        new_db.write_as_code(f)


def _hash_thread(url):
    raw_desc = _get_first_post(url)
    # Encode the str/unicode string to bytes.
    return hashlib.md5(raw_desc.encode("utf-8")).hexdigest()


def _dump_json():
    """Dumps the default moddb to a json file."""
    new_json_path = "./current_catalog.json"

    known_db = moddb.create_default_db()
    json_str = known_db.dump_json()

    with open(new_json_path, "wb") as f:
        f.write(json_str.encode("ascii"))


def main():
    need_help = False

    if (len(sys.argv) > 1):
        if (sys.argv[1] == "--scrape"):
            _scrape()

        elif (len(sys.argv) > 2 and sys.argv[1] == "--hash-thread"):
            sys.stdout.write("%s\n" % _hash_thread(sys.argv[2]))

        elif (sys.argv[1] == "--dump-json"):
            _dump_json()

        elif (sys.argv[1] in ["-h", "--help"]):
            need_help = True
        else:
            need_help = True
    else:
        need_help = True

    if (need_help):
        sys.stderr.write("Usage: python -m lib.moddb_updater [OPTION]\n")
        sys.stderr.write("\n")
        sys.stderr.write("      --scrape           write changed forum posts to a python file\n")
        sys.stderr.write("      --hash-thread URL  print the hash of a specific thread\n")
        sys.stderr.write("      --dump-json        write the current default moddb to a json file\n")
        sys.stderr.write("  -h, --help             display this help and exit\n")
        sys.stderr.write("\n")


if (__name__ == "__main__"):
    main()
