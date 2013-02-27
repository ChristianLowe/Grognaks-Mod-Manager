import threading


class KillableThread(threading.Thread):
    """A base class for threads that die on command.
    Subclasses' run() loops test if self.keep_alive is False.

    Instead of sleeping, they should call nap().

    And any subclass method, meant to be called by other
    threads, that interrupts a nap() should include wake_up().
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.snooze_cond = threading.Condition()
        self.keep_alive = True

    def nap(self, seconds):
        """Sleep but stay responsive.

        This sleep is preempted by a call to wake_up().

        According to this site, timeouts for Queues,
        Conditions, etc., can waste CPU cycles polling
        excessively often (20x/sec). But you'd need
        hundreds of threads to have a problem.
        http://blog.codedstructure.net/2011/02/concurrent-queueget-with-timeouts-eats.html

        :param seconds: How long to wait. Or None for indefinite.
        """
        with self.snooze_cond:
            self.snooze_cond.wait(seconds)

    def wake_up(self):
        """Interrupts a nap(). (thread-safe)"""
        with self.snooze_cond:
            self.snooze_cond.notify()

    def stop_living(self):
        """Tells this thread to die. (thread-safe)

        This method is preferred over setting keep_alive directly,
        for the benefit of threads that need to sleep with interruption.
        """
        self.keep_alive = False
        self.wake_up()


class WrapperThread(KillableThread):
    """A thread that runs a payload func and stays killable.
    It manages this by letting the payload know how to
    check keep_alive and how to sleep.
    """

    def __init__(self):
        KillableThread.__init__(self)
        self._payload = None
        self._payload_args = None
        self._payload_kwargs = None

        self._failure_func = None
        self._success_func = None

    def set_payload(self, payload, *args, **kwargs):
        """Sets the payload function.
        All further args will be forwarded to the payload.

        This thread will inject two extra keyword args:
        "keep_alive_func": Callback to check keep_alive.
                           No args.
        "sleep_func": Callback to sleep.
                      A number in seconds.

        So the payload must be capable of accepting those.
        """
        self._payload = payload
        self._payload_args = args
        self._payload_kwargs = kwargs
        self._payload_kwargs["keep_alive_func"] = self.keeping_alive
        self._payload_kwargs["sleep_func"] = self.nap

    def set_failure_func(self, failure_func):
        """Sets a callback to run on failure.
        It will be given 1 arg: an exception.
        """
        self._failure_func = failure_func

    def set_success_func(self, successs_func):
        """Sets a callback to run on success.
        It will be given 1 arg: whatever the payload returned.
        """
        self._success_func = successs_func

    def run(self):
        result = None

        if (self._payload is not None):
            try:
                result = self._payload(*self._payload_args, **self._payload_kwargs)

            except (Exception) as err:
                if (self.keeping_alive()):
                    if (self._failure_func is not None):
                        try:
                            self._failure_func(err)
                        except (Exception) as err:
                            logging.exception(err)
                            self.keep_alive = False
            else:
                if (self.keeping_alive()):
                    if (self._success_func is not None):
                        try:
                            self._success_func(result)
                        except (Exception) as err:
                            logging.exception(err)

        self.keep_alive = False

    def keeping_alive(self):
        """Returns True if this thread should continue, False otherwise."""
        return self.keep_alive
