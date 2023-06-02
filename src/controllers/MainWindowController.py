from typing import List

import requests
from PySide6.QtCore import QThreadPool, Signal, QObject, Qt
from PySide6.QtGui import QPixmap, QColor, QPainter, QBrush
from PySide6.QtWidgets import QWidget, QListWidgetItem, QFileDialog
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
    QUALITY = ["192K", "WORST", "32K", "96K", "128K", "256K", "320K", "BEST"]
    OUTPUT_FORMAT = ["MP3", "AAC", "FLAC", "M4A", "OPUS", "VORBIS", "WAV"]

    def __init__(self):
        super().__init__()
        self.signals = MainWindowSignals()
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
        self.songs = []
        self.query = ""
        self.ui.progressBar.setVisible(False)
        self.ui.labelCoverAlbum.setStyleSheet("padding-left:10px;")
        self.ui.labelDownloadFinished.setVisible(False)
        self.ui.comboBoxQuality.addItems(MainWindowController.QUALITY)
        self.ui.comboBoxOutPutType.addItems(MainWindowController.OUTPUT_FORMAT)
        self.ui.comboBoxQuality.setVisible(False)
        self.ui.comboBoxOutPutType.setVisible(False)
        self.ui.comboBoxQuality.currentTextChanged.connect(self.qualityChanged)
        self.ui.comboBoxOutPutType.currentTextChanged.connect(self.outputTypeChanged)
        self.materialYouColorPrimary = ""
        self.materialYouOnColorOnPrimary = ""
        self.materialYouColorPrimaryContainer = ""
        self.materialYouOnColorOnPrimaryContainer = ""
        self.materialYouButtonColor = ""
        self.materialYouOnButtonColor = ""

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
        self.searchWorker = SearchWorker(self.query)
        self.searchWorker.signals.failed.connect(self.resetUI())
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
        self.ui.comboBoxQuality.setVisible(True)
        self.ui.comboBoxOutPutType.setVisible(True)
        self.setStyleSheet(f"background-color:{self.materialYouColorPrimary};color:{self.materialYouOnColorOnPrimary};")
        self.ui.widget_3.setStyleSheet(
            f"background-color:{self.materialYouColorPrimaryContainer};color:{self.materialYouOnColorOnPrimaryContainer};border:0px;border-radius:10px;")
        self.ui.scrollArea.setStyleSheet(
            f"background-color:{self.materialYouColorPrimaryContainer};border:0px;border-radius:10px;")
        self.ui.buttonDownloadAll.setStyleSheet(f"background-color:{self.materialYouButtonColor};color:{self.materialYouOnButtonColor};border:none;border-radius:10px;")
        songs = self.sortSongs(songs)
        for song in songs:
            songItem = SongController(song, self.signals)
            songItem.setStyleSheet(
                f"background-color:{self.materialYouColorPrimaryContainer};color:{self.materialYouOnColorOnPrimaryContainer};border:0px;border-radius:10px;")
            hint = songItem.sizeHint()
            hint.setWidth(self.ui.listWidget.width() - 10)
            item = QListWidgetItem(self.ui.listWidget)
            item.setSizeHint(hint)
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, songItem)




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

    def sortSongs(self, songs):
        return sorted(songs, key=lambda song: song.track_number)

    def downloadAll(self):
        if self.songs == []:
            return
        self.ui.labelDownloadFinished.setVisible(False)
        self.ui.lineEdit.setDisabled(True)
        self.ui.search.setDisabled(True)
        self.ui.progressBar.setVisible(True)
        quality = self.ui.comboBoxQuality.currentText()
        if "WORST" or "BEST" not in quality:
            quality = "Q" + quality
        output_format = self.ui.comboBoxOutPutType.currentText()
        if "open.spotify" and "playlist" in self.query:
            download_type = "PLAYLIST"
        else:
            download_type = "ALBUM"
        self.downloadAllWorker = DownloadAllWorker(self.query, quality, output_format, download_type)
        self.downloadAllWorker.signals.result.connect(self.downloadFinished)
        self.downloadAllWorker.signals.failed.connect(self.downloadFailed)
        # Execute
        self.threadpool.start(self.downloadAllWorker)

    def downloadFinished(self):
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
