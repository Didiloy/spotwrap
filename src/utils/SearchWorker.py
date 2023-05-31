from PySide6.QtCore import Signal, QRunnable, Slot, QObject
from src.utils.Spotdl import SpotdlSingleton


class WorkerSignals(QObject):
    result = Signal(object)
    failed = Signal(object)


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
        spotdl = SpotdlSingleton.get_instance().spotdl
        try:
            songs = spotdl.search([self.search])
            self.signals.result.emit(songs)  # Return the result of the processing
        except:
            self.signals.failed.emit("Failed")
