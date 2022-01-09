import threading
import datetime
import requests

from mngrs.config_mngr import ConfigMngr
from model.weather_data import WeatherData

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
        with self.cache_lock:
            if city not in self.cache or (datetime.datetime.utcnow() - self.cache[city]["ts"]).total_seconds() > self.config_mngr.interval:
                weather_data = self.get_weather_from_api(city)
                self.cache[city] = {'data': weather_data, 'ts': datetime.datetime.utcnow()}
            return self.cache[city]['data']

    def get_weather_from_api(self, city):
        print(f"\nDebug: Sending request for {city}")
        response = requests.get(
            self.config_mngr.config['urls']['weather'],
            params={
                "q": city,
                "appid": self.config_mngr.config['api_keys']['weather_api_key'],
                "units": "metric"
            })
        if response.status_code == 200:
            return WeatherData(response.json())
