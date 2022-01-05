import threading
import datetime

from mngrs.config_mngr import ConfigMngr

"""
This class should be thread-safe, and singletone
"""
class CacheMngr:

    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        if CacheMngr.__instance:
            raise Exception("Singleton! Use get_instance() instead")
        CacheMngr.__instance = self
        self.cache = {}
        self.cache_lock = threading.Lock()
        self.config_mngr = ConfigMngr.factory()

    @staticmethod
    def get_instance():
        if not CacheMngr.__instance:
            with CacheMngr.__lock:
                if not CacheMngr.__instance:
                    CacheMngr()
        return CacheMngr.__instance

    def get_weather(self, city):
        """
        Check whether there is up-to-date data in cache and return it if so.
        Otherwise, get from the api
        :param city:
        :return:

        """
        print("inside get_weather")
        with self.cache_lock:
            if city in self.cache and (datetime.datetime.utcnow() - self.cache[city]["ts"]).total_seconds() > self.config_mngr.interval:
                pass
