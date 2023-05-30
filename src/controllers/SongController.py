from PySide6.QtGui import QPainter, QColor, QPaintEvent
from PySide6.QtWidgets import QWidget

from src.views.song import Ui_song


class SongController(QWidget):
    def __init__(self, artists, title, track_number):
        super().__init__()
        self.ui = Ui_song()
        self.ui.setupUi(self)
        self.ui.buttonDownloadSingleSong.clicked.connect(self.download)
        self.ui.labelTrackNumber.setText(f"{track_number}")
        self.ui.labelSongTitle.setText(f"{title}")
        self.ui.widget.setStyleSheet("background-color:rgba(40,40,150,0);border:0px;")
        artist_name = "/".join(artists)
        self.ui.labelSongArtists.setText(f"{artist_name}")


    def download(self):
        pass
