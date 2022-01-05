"""
Manage users and subscriptions (cities per user + files)
"""
#singleton
class SubscriptionMngr:

    def __init__(self):
        self.subscriptions = {}
        # {"London": ["valeria", "ravit"],
        # "Tel Aviv":["ravit"]}

    def subscribe(self, user, cities):
        pass

    def unsubscribe(self, user, city):
        pass
