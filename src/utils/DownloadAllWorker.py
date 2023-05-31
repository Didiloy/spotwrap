from PySide6.QtCore import Signal, QRunnable, Slot, QObject
from savify import Savify, Type
from savify.utils import PathHolder

from src.utils.Config import Config
from src.utils.Spotdl import SpotdlSingleton


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
        savify: Savify = SpotdlSingleton.get_instance().savify
        savify.path_holder = PathHolder(downloads_path=Config.get_instance().SAVE_PATH)
        savify.download(self.query, Type.ALBUM)
        self.signals.result.emit("Done")  # Return the result of the processing
