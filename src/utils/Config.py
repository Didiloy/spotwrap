import logging
import os
import tempfile

import platformdirs


class Config:
    __instance__ = None

    def __init__(self):
        """ Constructor.
       """
        if Config.__instance__ is None:
            Config.__instance__ = self
            # set up user data path and savepath file
            self.USER_DATA_PATH = platformdirs.user_data_path("spotwrap", "Didiloy")
            if not os.path.exists(self.USER_DATA_PATH):
                os.makedirs(self.USER_DATA_PATH)

            self.SAVE_PATH_FILE = os.path.join(self.USER_DATA_PATH, "savepath.txt")
            if not os.path.exists(self.SAVE_PATH_FILE):
                with open(self.SAVE_PATH_FILE, "w") as f:
                    f.write(platformdirs.user_music_dir())

            with open(self.SAVE_PATH_FILE, "r") as f:
                self.SAVE_PATH = f.read()

            self.SECONDARY_BACKGROUND_COLOR = "rgb(239, 242, 233)"
            logging.basicConfig(filename=f"{self.USER_DATA_PATH}/spotwrap.log", level=logging.DEBUG)
            self.logger = logging.getLogger()
            print(logging.getLoggerClass().root.handlers[0].baseFilename)

            self.TEMP_PATH = tempfile.gettempdir()
        else:
            raise Exception("You cannot create another Config class")

    def saveNewSavePath(self):
        with open(self.SAVE_PATH_FILE, "w") as f:
            f.write(self.SAVE_PATH)

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
       """
        if not Config.__instance__:
            Config()
        return Config.__instance__
