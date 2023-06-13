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
from savify import Savify, Type, Quality, Format
from savify.utils import PathHolder

from src.utils.Config import Config
from src.utils.Spotdl import SpotdlSingleton


class WorkerSignals(QObject):
    result = Signal(object)
    failed = Signal(object)


class DownloadAllWorker(QRunnable):

    def __init__(self, query, quality, output_format, search_type, *args, **kwargs):
        super(DownloadAllWorker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.query = query
        self.quality = self.convertStringToQuality(quality)
        self.output_format = self.convertOutputTypeToFormat(output_format)
        self.search_type = self.convertStringToType(search_type)
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()  # QtCore.Slot
    def run(self):
        savify: Savify = SpotdlSingleton.get_instance().savify
        savify.path_holder = PathHolder(downloads_path=Config.get_instance().SAVE_PATH)

        savify.quality = self.quality
        savify.download_format = self.output_format
        try:
            savify.download(self.query, query_type=self.search_type)
            self.signals.result.emit("Done")  # Return the result of the processing
        except:
            self.signals.failed.emit("Failed")  # Return the result of the processing

    def convertStringToQuality(self, quality: str) -> Quality:
        if quality == "WORST":
            return Quality.WORST
        elif quality == "Q32K":
            return Quality.Q32K
        elif quality == "Q96K":
            return Quality.Q96K
        elif quality == "Q128K":
            return Quality.Q128K
        elif quality == "Q192K":
            return Quality.Q192K
        elif quality == "Q256K":
            return Quality.Q256K
        elif quality == "Q320K":
            return Quality.Q320K
        elif quality == "BEST":
            return Quality.BEST
        else:
            return Quality.Q192K

    def convertOutputTypeToFormat(self, output: str) -> Format:
        if output == "MP3":
            return Format.MP3
        elif output == "AAC":
            return Format.AAC
        elif output == "FLAC":
            return Format.FLAC
        elif output == "M4A":
            return Format.M4A
        elif output == "OPUS":
            return Format.OPUS
        elif output == "VORBIS":
            return Format.VORBIS
        elif output == "WAV":
            return Format.WAV
        else:
            return Format.MP3

    def convertStringToType(self, type: str) -> Type:
        if type == "ALBUM":
            return Type.ALBUM
        elif type == "PLAYLIST":
            return Type.PLAYLIST
        elif type == "TRACK":
            return Type.TRACK
        else:
            return Type.ALBUM
