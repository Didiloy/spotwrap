import asyncio
import os
from datetime import datetime

from PySide6.QtCore import Signal, QRunnable, Slot, QObject

from src.utils.Config import Config
from src.utils.Spotdl import SpotdlSingleton
from spotdl import Spotdl


class WorkerSignals(QObject):
    result = Signal(object)


class DownloadAllWorker(QRunnable):

    def __init__(self, query, *args, **kwargs):
        super(DownloadAllWorker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.query = query
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()  # QtCore.Slot
    def run(self):
        #TODO change the method to use spotdl in the code
        # spotdl: Spotdl = SpotdlSingleton.get_instance().spotdl
        # songsAndPath = spotdl.download_songs(self.songs)
        # for song, path in songsAndPath:
        #     print(song, path)
        #     if path is not Config.get_instance().SAVE_PATH:
        #         os.replace(path, Config.get_instance().SAVE_PATH + "/" + song.display_name)
                # get current path
        path = os.getcwd()
        print(path)
        # get the timestamp
        timestamp = datetime.timestamp(datetime.now())
        # execute a external command
        os.system(f"spotdl \"{self.query}\"")
        # get all the files created after timestamp
        files = [f for f in os.listdir(path) if
                 os.path.isfile(os.path.join(path, f)) and os.path.getctime(os.path.join(path, f)) > timestamp]
        # move all the files to the save path
        for file in files:
            os.replace(os.path.join(path, file), os.path.join(Config.get_instance().SAVE_PATH, file))
        self.signals.result.emit("Done")  # Return the result of the processing
