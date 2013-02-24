import ctypes
import errno
import logging
import os
import platform
import re
import signal
import sys
import threading
import time


class CleanupHandler(object):
    """A base class for thread-safe exit/interrupt operations."""

    def __init__(self):
        self.caught_lock = threading.RLock()
        self.caught = False

        # Attach handlers to self, so they won't get garbage collected.

        def signal_handler(signum, stackframe):
            logging.info("Signal handler wants to exit!")
            self.cleanup()
        self.signal_handler = signal_handler

        if (re.search("Windows", platform.system(), re.IGNORECASE)):
            # Handle console window closing.
            #   http://msdn.microsoft.com/en-us/library/ms686016(VS.85).aspx
            #   http://msdn.microsoft.com/en-us/library/ms683242(v=vs.85).aspx
            CTRL_C_EVENT = 0
            CTRL_CLOSE_EVENT = 2

            @ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_uint)
            def win_ctrlhandler(dwCtrlType):
                if (dwCtrlType in [CTRL_C_EVENT, CTRL_CLOSE_EVENT]):
                    logging.info("")
                    logging.info("ConsoleCtrlHandler wants to exit!")
                    self.cleanup()
                    return True  # Consume the event to thwart the default handler.
                return False
            self.win_ctrlhandler = win_ctrlhandler
        else:
            self.win_ctrlhandler = None

    def register(self):
        """Associates handler funcs with signals. Call from MainThread."""
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

        # Linux/OSX? terminal closing.
        # Don't use until confirmed not to leave the app
        # running as a headless zombie process. SIGEXIT maybe?
        #
        # Closing the terminal shouldn't be encouraged unless
        # it's universally supported.
        #
        #if (hasattr(signal, "SIGHUP")):
        #    signal.signal(signal.SIGHUP, self.signal_handler)

        # Windows terminal closing.
        if (re.search("Windows", platform.system(), re.IGNORECASE)):
            ctypes.windll.kernel32.SetConsoleCtrlHandler(self.win_ctrlhandler, 1)

    def cleanup(self):
        """Triggers cleanup. Handlers and Threads call this."""
        with self.caught_lock:
            if (self.caught): return
            self.caught = True

        # If a signal handler called this, we're in MainThread,
        #   blocking mainloop(), so do cleaning up in a separate thread.
        t = threading.Thread(target=self._cleanup, name="CleanupWorker")
        t.daemon = False  # Don't trust inheritance from current thread.
        t.start()

    def _cleanup(self):
        """The actual cleanup code. Subclasses should override this."""
        os._exit(0)


class CustomCleanupHandler(CleanupHandler):
    """A CleanupHandler that understands KillableThreads, sockets,
    subprocess objects, and gui apps.

    :param killable_threads: A list of KillableThread objects.
    :param sockets: A list of socket objects.
    :param procs: A list of subprocess objects.
    :param guis: A list of GuiApp objects.
    """

    def __init__(self, killable_threads=None, sockets=None, procs=None, guis=None):
        CleanupHandler.__init__(self)
        if (not killable_threads): killable_threads = []
        if (not sockets): sockets = []
        if (not procs): procs = []
        if (not guis): guis = []
        self.threads = killable_threads
        self.sockets = sockets
        self.procs = procs
        self.guis = guis
        self._cleaning_event = threading.Event()

    def is_not_cleaning(self):
        """Pollable boolean that returns False to interrupt, True otherwise.
        This value is set during _cleanup() after registered objects are
        sent a kill signal.
        """
        return (not self._cleaning_event.is_set())

    def nap(self, seconds):
        """Sleep in an interruptable manner."""
        self._cleaning_event.wait(seconds)

    def add_thread(self, t):
        with self.caught_lock:
            if (self.caught): self.kill_thread(t)
            elif (t not in self.threads): self.threads.append(t)

    def add_socket(self, s):
        with self.caught_lock:
            if (self.caught): self.kill_socket(s)
            elif (s not in self.sockets): self.sockets.append(s)

    def add_proc(self, p):
        with self.caught_lock:
            if (self.caught): self.kill_proc(p)
            elif (p not in self.procs): self.procs.append(p)

    def add_gui(self, g):
        with self.caught_lock:
            if (self.caught): self.kill_gui(g)
            elif (g not in self.guis): self.guis.append(g)

    def kill_thread(self, t): t.stop_living()
    def kill_socket(self, s):
        try:
            s.shutdown(socket.SHUT_WR)
            s.close()
        except (Exception) as err:
            pass
    def kill_proc(self, p):
        if (p.poll() is None):
            try:
                p.terminate()
            except (Exception) as err:
                pass
    def kill_gui(self, g): g.invoke_later(g.ACTION_DIE, {})

    def _cleanup(self):
        try:
            logging.info("")
            logging.info("Quitting... (ctrl-break to be rude)")
            logging.info("")
            for t in self.threads:
                if (t): self.kill_thread(t)
            for s in self.sockets:
                if (s): self.kill_socket(s)
            for p in self.procs:
                if (p): self.kill_proc(p)
            for g in self.guis:
                if (g): self.kill_gui(g)

            self._cleaning_event.set()

            # Wait for monitored threads to run out (surprise exit() any others).
            still_waiting = True
            first_pass = True
            while (still_waiting):
                still_waiting = False
                for t in self.threads:
                    if (t and t.isAlive() and not t.daemon and t != threading.currentThread()):
                        if (not first_pass): logging.info("Waiting on thread: %s" % str(t))
                        still_waiting = True
                        break
                for g in self.guis:
                    if (g and g.done is False):
                        if (not first_pass): logging.info("Waiting on GUI: %s" % str(g))
                        still_waiting = True
                        break
                if (still_waiting): time.sleep(1)
                first_pass = False

        except (IOError) as err:
            if (err.errno == errno.EINTR):  # Ignore sigint'd sleep() on Windows.
                pass
            else:
                logging.exception(err)

        logging.info("Bye")

        os._exit(0)  # Exit for real, unlike sys.exit().
