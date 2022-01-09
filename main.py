from menu.main_menu import MainMenu
from workers.sampler import Sampler

if __name__ == "__main__":

    # New thread for main menu
    main_menu_thread = MainMenu()
    main_menu_thread.start()

    # Init Sampler (will run using timers)
    sampler = Sampler()
    sampler.run()

    # Wait for the app to finish - when user selects "Exit"
    main_menu_thread.join()
    # if we got here - user asked to exit. Let's finalize everything and exit
    # notify other threads to exit
    sampler.stop_execution()
