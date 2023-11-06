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

import requests
from PySide6.QtCore import QThreadPool, Signal, QObject, Qt
from PySide6.QtGui import QPixmap, QColor, QPainter, QBrush
from PySide6.QtWidgets import QWidget, QListWidgetItem, QFileDialog, QMenu
from spotdl import Song

from src.controllers.MainContextMenu import MainContextMenu
from src.controllers.SongController import SongController
from src.utils.Colors import Colors
from src.utils.Config import Config
from src.utils.DownloadAllWorker import DownloadAllWorker
from src.utils.SearchWorker import SearchWorker
from src.views.mainWindow import Ui_MainWindow


class MainWindowSignals(QObject):
    quality = Signal(object)
    output_type = Signal(object)


class MainWindowController(QWidget):
    QUALITY = ["320k", "8k", "16k", "32k", "96k", "128k", "160k", "192k", "256k"]
    OUTPUT_FORMAT = ["mp3", "flac", "m4a", "opus", "ogg"]

    def __init__(self):
        super().__init__()
        # defining required class variables
        self.signals = MainWindowSignals()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.searchWorker = SearchWorker("")
        self.downloadAllWorker = None
        self.threadpool = QThreadPool()
        self.songs = []
        self.songs_to_delete_after_download = []
        self.query = ""
        self.materialYouColorPrimary = ""
        self.materialYouOnColorOnPrimary = ""
        self.materialYouColorPrimaryContainer = ""
        self.materialYouOnColorOnPrimaryContainer = ""
        self.materialYouButtonColor = ""
        self.materialYouOnButtonColor = ""
        # setting up the ui
        self._setStateOfStartUi()
        # binding the actions to the buttons
        self._bindButtonsActions()

    def _setStateOfStartUi(self):
        self.ui.buttonDownloadAll.setVisible(False)
        self.ui.buttonPath.setVisible(False)
        self.ui.progressBarMainWindow.setVisible(False)
        main_context_menu = MainContextMenu()
        self.ui.menuButton.setMenu(main_context_menu)
        self.ui.menuButton.menu()
        self.ui.progressBar.setVisible(False)
        self.ui.labelCoverAlbum.setStyleSheet("padding-left:10px;")
        self.ui.labelDownloadFinished.setVisible(False)
        self.ui.comboBoxQuality.addItems(MainWindowController.QUALITY)
        self.ui.comboBoxOutPutType.addItems(MainWindowController.OUTPUT_FORMAT)
        self.ui.comboBoxQuality.setVisible(False)
        self.ui.comboBoxOutPutType.setVisible(False)

    def _bindButtonsActions(self):
        self.ui.search.clicked.connect(self.search)
        # connect the enter key to the search button
        self.ui.lineEdit.returnPressed.connect(self.ui.search.click)
        self.ui.buttonPath.clicked.connect(self.select_directory)
        self.ui.buttonDownloadAll.clicked.connect(self.downloadAll)
        self.ui.comboBoxQuality.currentTextChanged.connect(self.qualityChanged)
        self.ui.comboBoxOutPutType.currentTextChanged.connect(self.outputTypeChanged)

    def qualityChanged(self, quality):
        self.signals.quality.emit(quality)

    def outputTypeChanged(self, output_type):
        self.signals.output_type.emit(output_type)

    def search(self):
        self.resetUI()
        if self.ui.lineEdit.text() == "":
            return
        self.query = self.ui.lineEdit.text()
        self.ui.lineEdit.setDisabled(True)
        self.ui.search.setDisabled(True)
        self.ui.progressBarMainWindow.setVisible(True)
        self.searchWorker = SearchWorker(self.query)
        self.searchWorker.signals.failed.connect(self.resetUI)
        self.searchWorker.signals.result.connect(self.updateUI)
        # Execute
        self.threadpool.start(self.searchWorker)

    def updateUI(self, songs):
        self.ui.lineEdit.setText("")
        self.ui.progressBarMainWindow.setVisible(False)
        self.ui.labelBigIcon.setVisible(False)
        self.songs: [Song] = songs
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
        self.ui.comboBoxQuality.setVisible(True)
        self.ui.comboBoxOutPutType.setVisible(True)
        self.setStyleSheet(f"background-color:{self.materialYouColorPrimary};color:{self.materialYouOnColorOnPrimary};")
        self.ui.widget_3.setStyleSheet(
            f"background-color:{self.materialYouColorPrimaryContainer};color:{self.materialYouOnColorOnPrimaryContainer};border:0px;border-radius:10px;")
        self.ui.scrollArea.setStyleSheet(
            f"background-color:{self.materialYouColorPrimaryContainer};border:0px;border-radius:10px;")
        self.ui.buttonDownloadAll.setStyleSheet(
            f"background-color:{self.materialYouButtonColor};color:{self.materialYouOnButtonColor};border:none;border-radius:10px;")
        songs = self.sortSongs(songs)
        for s in songs:
            songItem = SongController(s, self.signals)
            songItem.setStyleSheet(
                f"background-color:{self.materialYouColorPrimaryContainer};color:{self.materialYouOnColorOnPrimaryContainer};border:0px;border-radius:10px;")
            hint = songItem.sizeHint()
            hint.setWidth(self.ui.listWidget.width() - 10)
            item = QListWidgetItem(self.ui.listWidget)
            item.setText(s.name)
            item.setForeground(QColor("transparent"))
            item.setSizeHint(hint)
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, songItem)
            songItem.songSignals.progress.connect(self.progress)
            songItem.songSignals.deleteSong.connect(self.removeSongFromList)

    def removeSongFromList(self, song):
        self.songs.remove(song)
        self.songs_to_delete_after_download.append(song)
        self.ui.labelNbTitle.setText(f"{len(self.songs)} tracks")
        songItem = self.ui.listWidget.findItems(song.name, Qt.MatchExactly)[0]
        self.ui.listWidget.takeItem(self.ui.listWidget.row(songItem))

    def getAndSetImageFromUrl(self, imageURL):
        request = requests.get(imageURL, stream=True)
        pixmap = QPixmap(150, 150)
        pixmap.loadFromData(request.content)
        pixmap = pixmap.scaledToWidth(200)

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

        self.ui.labelCoverAlbum.setPixmap(rounded)

        # Setting the material you color of the album
        try:
            request = requests.get(imageURL, stream=True)
            color = Colors.get_instance().getDominantColorFromImage(request.raw)
            primaryColor = color["secondary"]
            self.materialYouColorPrimary = f"rgb({primaryColor[0]},{primaryColor[1]},{primaryColor[2]})"
            colorOnPrimary = color["onSecondary"]
            self.materialYouOnColorOnPrimary = f"rgb({colorOnPrimary[0]},{colorOnPrimary[1]},{colorOnPrimary[2]})"
            primaryContainer = color["primaryContainer"]
            self.materialYouColorPrimaryContainer = f"rgb({primaryContainer[0]},{primaryContainer[1]},{primaryContainer[2]})"
            colorOnPrimaryContainer = color["onPrimaryContainer"]
            self.materialYouOnColorOnPrimaryContainer = f"rgb({colorOnPrimaryContainer[0]},{colorOnPrimaryContainer[1]},{colorOnPrimaryContainer[2]})"
            buttonColor = color["primary"]
            self.materialYouButtonColor = f"rgb({buttonColor[0]},{buttonColor[1]},{buttonColor[2]})"
            onButtonColor = color["onPrimary"]
            self.materialYouOnButtonColor = f"rgb({onButtonColor[0]},{onButtonColor[1]},{onButtonColor[2]})"
        except Exception as e:
            print("Error while getting the color of the album: ", e)
            self.materialYouColorPrimary = Colors.get_instance().SECONDARY_BACKGROUND_COLOR
            self.materialYouOnColorOnPrimary = Colors.get_instance().ON_SECONDARY_BACKGROUND_COLOR

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
        self.setStyleSheet("")
        self.ui.widget_3.setStyleSheet("")
        self.ui.scrollArea.setStyleSheet("")
        self.ui.buttonDownloadAll.setStyleSheet("")
        self.ui.progressBar.setVisible(False)
        self.ui.lineEdit.setDisabled(False)
        self.ui.search.setDisabled(False)
        self.ui.labelDownloadFinished.setVisible(False)
        self.ui.comboBoxQuality.setVisible(False)
        self.ui.comboBoxOutPutType.setVisible(False)
        self.ui.progressBarMainWindow.setVisible(False)
        self.ui.labelBigIcon.setVisible(True)
        self.ui.textEditDownloadProgress.setText("")

    def select_directory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.Option.DontUseNativeDialog

        directory = QFileDialog.getExistingDirectory(
            None, "Select Directory", dir=Config.get_instance().SAVE_PATH, options=options
        )
        if directory == "" or directory is None:
            return
        if directory != Config.get_instance().SAVE_PATH:
            Config.get_instance().SAVE_PATH = directory
            Config.get_instance().saveNewSavePath()

    def sortSongs(self, songs):
        return sorted(songs, key=lambda song: song.track_number)

    def downloadAll(self):
        if not self.songs:
            return
        self.ui.labelDownloadFinished.setVisible(False)
        self.ui.lineEdit.setDisabled(True)
        self.ui.search.setDisabled(True)
        self.ui.progressBar.setVisible(True)
        quality = self.ui.comboBoxQuality.currentText()
        output_format = self.ui.comboBoxOutPutType.currentText()
        self.downloadAllWorker = DownloadAllWorker(self.query, quality, output_format)
        self.downloadAllWorker.signals.result.connect(self.downloadFinished)
        self.downloadAllWorker.signals.failed.connect(self.downloadFailed)
        self.downloadAllWorker.signals.progress.connect(self.progress)
        # Execute
        self.threadpool.start(self.downloadAllWorker)

    def progress(self, progress):
        # set color to black
        self.ui.textEditDownloadProgress.setTextColor(QColor(0, 0, 0))
        if "error" in progress:
            # change text color to red
            self.ui.textEditDownloadProgress.setTextColor(QColor(255, 0, 0))
        self.ui.textEditDownloadProgress.append(progress)

    def downloadFinished(self, msg):
        self.deleteUnwantedSongs()
        print("download finished: ", msg)
        pixmap = QPixmap(":/images/images/check.png")
        pixmap = pixmap.scaledToWidth(25)
        self.ui.labelDownloadFinished.setPixmap(pixmap)
        self.ui.labelDownloadFinished.setVisible(True)
        self.ui.progressBar.setVisible(False)
        self.ui.lineEdit.setDisabled(False)
        self.ui.search.setDisabled(False)

    def downloadFailed(self):
        pixmap = QPixmap(":/images/images/cross.png")
        pixmap = pixmap.scaledToWidth(25)
        self.ui.labelDownloadFinished.setPixmap(pixmap)
        self.ui.labelDownloadFinished.setVisible(True)
        self.ui.progressBar.setVisible(False)
        self.ui.lineEdit.setDisabled(False)
        self.ui.search.setDisabled(False)

    def deleteUnwantedSongs(self):
        output_format = self.ui.comboBoxOutPutType.currentText()
        for song in self.songs_to_delete_after_download:
            filename = f"{song.artist} - {song.name}.{output_format}"
            # delete the file that have been download and that the user doesn't want
            try:
                self.progress(f"Deleting {filename}")
                os.remove(os.path.join(f"{Config.get_instance().SAVE_PATH}", filename))
            except Exception as e:
                print("Error while deleting the file: ", e)
                Config.get_instance().logger.error(e)
                self.progress(f"Error while deleting the file: {e}")
        self.songs_to_delete_after_download = []
