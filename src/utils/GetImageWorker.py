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
