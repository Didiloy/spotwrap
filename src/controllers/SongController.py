from pathlib import Path
from typing import Tuple, Optional

from PySide6.QtGui import QPainter, QColor, QPaintEvent
from PySide6.QtWidgets import QWidget
from spotdl import Song

from src.utils.Config import Config
from src.utils.Spotdl import SpotdlSingleton
from src.views.song import Ui_song


class SongController(QWidget):
    def __init__(self, song: Song):
        super().__init__()
        self.song = song
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
