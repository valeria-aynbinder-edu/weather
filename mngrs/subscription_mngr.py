import threading
import copy

"""
Manage users and subscriptions (cities per user + files)
"""
#singleton
class SubscriptionMngr:

    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        if SubscriptionMngr.__instance:
            raise Exception("Singleton! Use get_instance() instead")
        SubscriptionMngr.__instance = self

        self.subscriptions = {}
        # {"London": ["valeria", "ravit"],
        # "Tel Aviv":["ravit"]}

        self.subscriptions_lock = threading.Lock()

    @staticmethod
    def get_instance():
        if not SubscriptionMngr.__instance:
            with SubscriptionMngr.__lock:
                if not SubscriptionMngr.__instance:
                    SubscriptionMngr()
        return SubscriptionMngr.__instance

    def get_subscriptions(self):
        with self.subscriptions_lock:
            return copy.deepcopy(self.subscriptions)

    def subscribe(self, user, cities):
        with self.subscriptions_lock:
            for city in cities:
                if city not in self.subscriptions:
                    self.subscriptions[city] = set()
                self.subscriptions[city].add(user)

    def unsubscribe(self, user, city):
        #todo: implement
        pass
