import datetime
import time
import threading


class Sampler:

    def __init__(self):
        self.subscription_mngr = None
        self.cache_mngr = None
        self.config_mngr = None

        self.interrupt = False
        # self.last_update = None

    def interrupt(self):
        self.interrupt = True

    def _run_once(self):
        print("Inside run_once")
        if not self.interrupt():
            timer = threading.Timer(5, self._run_once)
            timer.start()
        # check all the subscriptions and call get_weather where needed

    # def start(self):
    #
    #     timer = threading.Timer(5, self._run_once)
    #     timer.start()
        # while True:
        #     time.sleep(300)
        #     # if (datetime.datetime.now() - self.last_update).total_seconds >= 300:
        #     self._run_once()
        #     self.last_update = datetime.datetime.now()

