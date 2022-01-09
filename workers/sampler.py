import threading
import time


# Question: is synchronization needed?
from mngrs.cache_mngr import CacheMngr
from mngrs.config_mngr import ConfigMngr
from mngrs.subscription_mngr import SubscriptionMngr


class Sampler:

    def __init__(self):
        self.subscription_mngr = SubscriptionMngr.get_instance()
        self.cache_mngr = CacheMngr.get_instance()
        self.config_mngr = ConfigMngr.factory()
        self.listeners = []

        self.interrupt = False
        self.timer = None

    def stop_execution(self):
        self.interrupt = True
        if self.timer:
            self.timer.cancel()

    def run(self):
        if not self.interrupt:

            for city, users_set in self.subscription_mngr.get_subscriptions().items():
                weather = self.cache_mngr.get_weather(city)
                for user in users_set:
                    #todo: save data in files
                    print(f"\nSampler: Stored weather data for {city} for user {user}")

            # set a new timer
            self.timer = threading.Timer(self.config_mngr.config['sampling_rate_in_sec'], self.run)
            self.timer.start()
        else:
            print("ending sampling")
        # check all the subscriptions and call get_weather where needed

    #todo - implement adding notifiers or other listeners
    def add_listener(self):
        pass

