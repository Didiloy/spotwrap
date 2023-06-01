import requests
from PySide6.QtCore import Signal, QRunnable, Slot, QObject

class GetImageSignals(QObject):
    result = Signal(object)
    failed = Signal(object)


class GetImageWorker(QRunnable):

    def __init__(self, url, *args, **kwargs):
        super(GetImageWorker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.url = url
        self.args = args
        self.kwargs = kwargs
        self.signals = GetImageSignals()

    @Slot()  # QtCore.Slot
    def run(self):
        try:
            request = requests.get(self.url)
            self.signals.result.emit(request.content)  # Return the result of the processing
        except:
            self.signals.failed.emit("Failed")  # Return the result of the processing
