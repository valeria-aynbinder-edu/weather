from mngrs.cache_mngr import CacheMngr
import threading

if __name__ == "__main__":



    # main thread - runs menu
    while True:
        print("Main menu\n1 - get current weather data\n2 - subscribe for weather data")
        # add here code to get input from the user
        # if user selected 1
        city = "London"
        print(CacheMngr.get_instance().get_weather(city))

        # option 2
        # enter cities (up to 5)
