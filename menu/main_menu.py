from threading import Thread

from mngrs.cache_mngr import CacheMngr
from mngrs.subscription_mngr import SubscriptionMngr


class MainMenu(Thread):

    def __init__(self, daemon=None, args=()):

        super().__init__(daemon=daemon, args=args)
        self.MENU_OPTIONS = {
            1: {"action": self.get_data_action, "msg": "1 - Get weather update for specific city"},
            2: {"action": self.subscribe_action, "msg": "2 - Subscribe for weather updates"},
            3: {"action": self.exit_app, "msg": "3 - Exit"}
        }

        self.cache_mngr = CacheMngr.get_instance()
        self.subscription_mngr = SubscriptionMngr.get_instance()

        self.done = False

    def display_main_menu(self):
        print(f"\n****** Main menu ******\n")
        for option_code, option_data in self.MENU_OPTIONS.items():
            print(option_data['msg'])

        selection = int(input("Select an option: "))
        self.MENU_OPTIONS[selection]["action"]()

    def get_data_action(self):
        city = input("\nPlease enter a city: ")
        weather_data = self.cache_mngr.get_weather(city)
        print(f"\nWeather data for {city}: "
              f"\n\tDescription: {weather_data.description}"
              f"\n\tTemperature: {weather_data.temperature}"
              f"\n\tHumidity: {weather_data.humidity}%"
              f"\n\tLast update (utc): {weather_data.update_ts_utc}")

    def subscribe_action(self):
        user = input("\nPlease enter your name: ")
        city = input("\nPlease enter a city: ")
        self.subscription_mngr.subscribe(user, [city])

    def exit_app(self):
        print("Bye-bye")
        self.done = True

    def run(self):
        while not self.done:
            self.display_main_menu()
