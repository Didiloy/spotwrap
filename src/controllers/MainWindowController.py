import asyncio
import os
import threading
from datetime import time, datetime
from typing import List

import requests
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QListWidgetItem, QFileDialog
from spotdl import Song, Spotdl

from src.controllers.SongController import SongController
from src.utils.Config import Config
from src.utils.DownloadAllWorker import DownloadAllWorker
from src.utils.SearchWorker import SearchWorker
from src.utils.Spotdl import SpotdlSingleton
from src.views.mainWindow import Ui_MainWindow


class MainWindowController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.buttonDownloadAll.setVisible(False)
        self.ui.buttonPath.setVisible(False)
        self.ui.search.clicked.connect(self.search)
        # connect the enter key to the search button
        self.ui.lineEdit.returnPressed.connect(self.ui.search.click)
        self.ui.buttonPath.clicked.connect(self.select_directory)
        self.ui.buttonDownloadAll.clicked.connect(self.downloadAll)
        self.searchWorker = SearchWorker("")
        self.downloadAllWorker = None
        self.threadpool = QThreadPool()
        self.songs: List[Song] = []
        self.query = ""
        self.ui.progressBar.setVisible(False)

    def search(self):
        self.resetUI()
        if self.ui.lineEdit.text() == "":
            return
        self.query = self.ui.lineEdit.text()
        self.ui.lineEdit.setDisabled(True)
        self.ui.search.setDisabled(True)
        self.searchWorker = SearchWorker(self.query)
        self.searchWorker.signals.result.connect(self.updateUI)
        # Execute
        self.threadpool.start(self.searchWorker)

    def updateUI(self, songs):
        self.ui.lineEdit.setText("")
        self.songs = songs
        song = songs[0]
        self.ui.labelTitle.setText(song.album_name)
        self.ui.labelArtistName.setText(song.artist)
        self.ui.labelSeparator.setText("-")
        self.ui.labelDate.setText(song.date.split("-")[0])
        self.ui.labelNbTitle.setText(f"{len(songs)} tracks")
        self.getAndSetImageFromUrl(song.cover_url)
        self.ui.buttonDownloadAll.setVisible(True)
        self.ui.buttonPath.setVisible(True)
        self.ui.lineEdit.setDisabled(False)
        self.ui.search.setDisabled(False)
        songs = self.sortSongs(songs)
        for song in songs:
            songItem = SongController(song)
            item = QListWidgetItem(self.ui.listWidget)
            item.setSizeHint(songItem.sizeHint())
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, songItem)

    def getAndSetImageFromUrl(self, imageURL):
        request = requests.get(imageURL)
        pixmap = QPixmap(150, 150)
        pixmap.loadFromData(request.content)
        pixmap = pixmap.scaledToWidth(200)
        self.ui.labelCoverAlbum.setPixmap(pixmap)

    def resetUI(self):
        self.songs = []
        self.ui.labelTitle.setText("")
        self.ui.labelArtistName.setText("")
        self.ui.labelSeparator.setText("")
        self.ui.labelDate.setText("")
        self.ui.labelNbTitle.setText("")
        self.ui.labelCoverAlbum.setPixmap(QPixmap())
        self.ui.buttonPath.setVisible(False)
        self.ui.buttonDownloadAll.setVisible(False)
        self.ui.listWidget.clear()
        self.ui.progressBar.setVisible(False)
        self.ui.lineEdit.setDisabled(False)
        self.ui.search.setDisabled(False)

    def select_directory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.Option.DontUseNativeDialog

        directory = QFileDialog.getExistingDirectory(
            self, "Select Directory", dir=Config.get_instance().SAVE_PATH, options=options
        )
        if directory == "" or directory is None:
            return
        if directory != Config.get_instance().SAVE_PATH:
            Config.get_instance().SAVE_PATH = directory
            Config.get_instance().saveNewSavePath()

    def sortSongs(self, songs: List[Song]):
        return sorted(songs, key=lambda song: song.track_number)

    def downloadAll(self):
        if self.songs == []:
            return
        self.ui.lineEdit.setDisabled(True)
        self.ui.search.setDisabled(True)
        self.ui.progressBar.setVisible(True)
        self.downloadAllWorker = DownloadAllWorker(self.query)
        self.downloadAllWorker.signals.result.connect(self.resetUI)
        # Execute
        self.threadpool.start(self.downloadAllWorker)


    # @QtCore.Slot()
    # def updateSpinnerAnimation(self):
    #     # 'hide' the text of the button
    #     self.ui.search.setText("")
    #     self.ui.search.setIcon(QtGui.QIcon(self.animated_spinner.currentPixmap()))
