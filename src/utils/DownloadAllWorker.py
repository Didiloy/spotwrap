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
import os
import subprocess
import sys

from PySide6.QtCore import Signal, QRunnable, Slot, QObject

from src.utils.Config import Config


class WorkerSignals(QObject):
    result = Signal(object)
    failed = Signal(object)
    progress = Signal(object)


class DownloadAllWorker(QRunnable):

    def __init__(self, query, quality, output_format, *args, **kwargs):
        super(DownloadAllWorker, self).__init__()
        self.query = query
        self.quality = quality
        self.output_format = output_format
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.command = [
            self.resource_path("bin/spotdl"),
            f"{self.query}",
            "--bitrate",
            f"{self.quality}",
            "--format",
            f"{self.output_format}",
            "--output",
            Config.get_instance().SAVE_PATH
        ]

    @Slot()  # QtCore.Slot
    def run(self):
        try:
            self.signals.progress.emit("Starting Download")
            with subprocess.Popen(self.command, stdout=subprocess.PIPE, bufsize=1,
                                  universal_newlines=True) as p:
                for line in p.stdout:
                    self.signals.progress.emit(line)
            self.signals.progress.emit("Done")
            self.signals.result.emit("Done")  # Return the result of the processing
        except Exception as e:
            print(e)
            Config.get_instance().logger.error(e)
            self.signals.failed.emit("Failed")  # Return the result of the processing

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
