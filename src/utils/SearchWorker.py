#     This file is part of SpotWrap.
#     Copyright (C) 2023  Dylan Loya
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
