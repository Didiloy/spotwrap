from PySide6.QtCore import Signal, QRunnable, Slot, QObject
from src.utils import Spotdl


class WorkerSignals(QObject):
    result = Signal(object)


class SearchWorker(QRunnable):

    def __init__(self, search, *args, **kwargs):
        super(SearchWorker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.search = search
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()  # QtCore.Slot
    def run(self):
        spotdl = Spotdl.SpotdlSingleton.get_instance().spotdl
        songs = spotdl.search([self.search])
        self.signals.result.emit(songs)  # Return the result of the processing
