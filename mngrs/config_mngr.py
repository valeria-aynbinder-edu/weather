import json
import os


class ConfigMngr:

    def __init__(self, file_path):
        with open(file_path, "r") as f:
            self.config = json.load(f)
        # add error handling here

    @property
    def interval(self):
        return self.config["up_to_date_in_sec"]


    @staticmethod
    def factory(is_test=False):
        if is_test:
            return ConfigMngr(os.path.join("data", "config_test.json"))
        else:
            return ConfigMngr(os.path.join("data", "config.json"))


