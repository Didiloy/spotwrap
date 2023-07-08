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
from PySide6.QtCore import QThreadPool, Signal, Qt, QObject
from PySide6.QtGui import QPainter, QColor, QPaintEvent, QPixmap, QBrush
from PySide6.QtWidgets import QWidget
from spotdl import Song

from src.utils.DownloadAllWorker import DownloadAllWorker
from src.utils.GetImageWorker import GetImageWorker
from src.views.song import Ui_song


class SongSignals(QObject):
    progress = Signal(object)


class SongController(QWidget):
    def __init__(self, song: Song, signals):
        super().__init__()
        self.songSignals = SongSignals()
        self.song = song
        self.signals = signals
        self.signals.quality.connect(self.setQuality)
        self.signals.output_type.connect(self.setOutputType)
        self.quality = "192k"
        self.output_type = "mp3"
        self.ui = Ui_song()
        self.ui.setupUi(self)
        self.ui.labelTrackNumber.setText(f"{self.song.track_number}")
        self.ui.labelSongTitle.setText(f"{self.song.name}")
        artist_name = "/".join(self.song.artists)
        self.ui.labelSongArtists.setText(f"{artist_name}")
        # convert song duration from milliseconds to minutes and seconds
        if self.song.duration < 1000:  # can sometime be in seconds rather than milliseconds
            self.song.duration = self.song.duration * 1000
        minutes, seconds = divmod(self.song.duration / 1000, 60)
        minutes = int(minutes)
        seconds = int(seconds) if seconds > 9 else f"0{int(seconds)}"
        self.ui.labelDuration.setText(f"{minutes}:{seconds}")
        self.ui.progressBar.setVisible(False)
        pixmap = QPixmap(":/images/images/check.png")
        pixmap.scaledToWidth(16)
        self.ui.labelDownloadFinished.setPixmap(pixmap)
        self.ui.labelDownloadFinished.setVisible(False)
        self.ui.buttonDownload.clicked.connect(self.downloadSong)
        self.downloadAllWorker = None
        self.threadpool = QThreadPool()
        self.query = self.song.url
        self.getImageWorker = GetImageWorker(self.song.cover_url)
        # self.getAndSetImageFromUrl(self.song.cover_url)
        self.getImageWorker.signals.result.connect(self.setImage)
        self.threadpool.start(self.getImageWorker)

    def setQuality(self, quality):
        self.quality = quality

    def setOutputType(self, output_type):
        self.output_type = output_type

    def downloadSong(self):
        self.ui.buttonDownload.setDisabled(True)
        self.ui.progressBar.setVisible(True)
        self.ui.labelDownloadFinished.setVisible(False)
        self.downloadAllWorker = DownloadAllWorker(self.query, quality=self.quality, output_format=self.output_type)
        self.downloadAllWorker.signals.result.connect(self.downloadFinished)
        self.downloadAllWorker.signals.failed.connect(self.downloadFailed)
        self.downloadAllWorker.signals.progress.connect(self.emitProgress)
        # Execute
        self.threadpool.start(self.downloadAllWorker)

    def emitProgress(self, progress):
        print("song emit")
        self.songSignals.progress.emit(progress)

    def updateUi(self):
        self.ui.buttonDownload.setDisabled(False)
        self.ui.progressBar.setVisible(False)
        self.ui.labelDownloadFinished.setVisible(True)

    def downloadFinished(self):
        pixmap = QPixmap(":/images/images/check.png")
        pixmap = pixmap.scaledToWidth(16)
        self.ui.labelDownloadFinished.setPixmap(pixmap)
        self.updateUi()

    def downloadFailed(self):
        pixmap = QPixmap(":/images/images/cross.png")
        pixmap = pixmap.scaledToWidth(16)
        self.ui.labelDownloadFinished.setPixmap(pixmap)
        self.updateUi()

    def setImage(self, image):
        pixmap = QPixmap(70, 70)
        pixmap.loadFromData(image)
        pixmap = pixmap.scaledToWidth(70)

        radius = 10

        # create empty pixmap of same size as original
        rounded = QPixmap(pixmap.size())
        rounded.fill(QColor("transparent"))

        # draw rounded rect on new pixmap using original pixmap as brush
        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(pixmap))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(pixmap.rect(), radius, radius)
        painter.end()

        self.ui.labelAlbumCover.setPixmap(rounded)
