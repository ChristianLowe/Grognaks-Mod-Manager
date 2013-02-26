import time


# Global Constants

APP_VERSION = "1.7.0"
APP_NAME = "Grognak's Mod Manager v%s" % APP_VERSION
APP_URL = "http://www.ftlgame.com/forum/viewtopic.php?f=12&t=2464"

allowzip = False
never_run_ftl = False

dir_self = None
dir_mods = None
dir_res = None

_cleanup_handler = None


def set_cleanup_handler(handler):
    """Sets a globally accessable cleanup handler."""
    global _cleanup_handler

    _cleanup_handler = handler

def get_cleanup_handler():
    """Returns a globally accessable cleanup handler."""
    global _cleanup_handler

    return _cleanup_handler

def keeping_alive():
    """Pollable boolean that returns True to interrupt, false otherwise."""
    global _cleanup_handler

    try:
        return _cleanup_handler.is_not_cleaning()
    except (AttributeError) as err:
        return True

def nap(seconds):
    """Sleep N seconds in an interruptable manner."""
    global _cleanup_handler

    try:
        _cleanup_handler.nap(seconds)
    except (AttributeError) as err:
        time.sleep(seconds)
