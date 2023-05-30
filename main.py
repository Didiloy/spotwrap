import os
import sys
import threading

import platformdirs
from PySide6.QtWidgets import QApplication
from dotenv import load_dotenv

from src.controllers.MainWindowController import MainWindowController
import qdarktheme

from src.utils.Config import Config
from src.utils.Spotdl import SpotdlSingleton

# load environment variables
load_dotenv()
config = Config.get_instance()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowController()
    # setup stylesheet
    qdarktheme.setup_theme("auto", default_theme="dark")
    window.show()
    # spotdl = SpotdlSingleton.get_instance().spotdl
    # songs = spotdl.search(["https://open.spotify.com/album/5cnpjofSRJPxR22AriH7Q9?si=TiGu-Iw8RqOxpr7yHwYV7w"])
    # songsAndPath = spotdl.download_songs(songs)
    # for song, path in songsAndPath:
    #     print(song, path)
    #     if path is not Config.get_instance().SAVE_PATH:
    #         os.replace(path, Config.get_instance().SAVE_PATH + "/" + song.display_name)
    sys.exit(app.exec())
