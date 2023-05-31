from PySide6.QtCore import QThreadPool, Signal
from PySide6.QtGui import QPainter, QColor, QPaintEvent, QPixmap
from PySide6.QtWidgets import QWidget
from spotdl import Song

from src.utils.DownloadAllWorker import DownloadAllWorker
from src.views.song import Ui_song


class SongController(QWidget):
    def __init__(self, song: Song, signals):
        super().__init__()
        self.song = song
        self.signals = signals
        self.signals.quality.connect(self.setQuality)
        self.signals.output_type.connect(self.setOutputType)
        self.quality = "BEST"
        self.output_type = "MP3"
        self.ui = Ui_song()
        self.ui.setupUi(self)
        self.ui.labelTrackNumber.setText(f"{self.song.track_number}")
        self.ui.labelSongTitle.setText(f"{self.song.name}")
        self.ui.widget.setStyleSheet("background-color:rgba(40,40,150,0);border:0px;")
        artist_name = "/".join(self.song.artists)
        self.ui.labelSongArtists.setText(f"{artist_name}")
        #convert song duration from milliseconds to minutes and seconds
        minutes, seconds = divmod(self.song.duration / 1000, 60)
        minutes = int(minutes)
        seconds = int(seconds)
        self.ui.labelDuration.setText(f"{minutes}:{seconds}")
        self.ui.widget_2.setStyleSheet(f"background-color:white;border:0px;border-radius:10px;")
        self.ui.progressBar.setVisible(False)
        pixmap = QPixmap(":/images/images/check.png")
        pixmap.scaledToWidth(16)
        self.ui.labelDownloadFinished.setPixmap(pixmap)
        self.ui.labelDownloadFinished.setVisible(False)
        self.ui.buttonDownload.clicked.connect(self.downloadSong)
        self.downloadAllWorker = None
        self.threadpool = QThreadPool()
        self.query = f"{self.song.name} artist:{self.song.artist} album:{self.song.album_name}"

    def setQuality(self, quality):
        self.quality = quality

    def setOutputType(self, output_type):
        self.output_type = output_type


    def downloadSong(self):
        self.ui.buttonDownload.setDisabled(True)
        self.ui.progressBar.setVisible(True)
        self.ui.labelDownloadFinished.setVisible(False)
        self.downloadAllWorker = DownloadAllWorker(self.query, quality=self.quality, output_format=self.output_type, search_type="TRACK")
        self.downloadAllWorker.signals.result.connect(self.downloadFinished)
        self.downloadAllWorker.signals.failed.connect(self.downloadFailed)
        # Execute
        self.threadpool.start(self.downloadAllWorker)

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

