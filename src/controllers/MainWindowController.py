import os
import requests
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QPixmap, QMovie, QIcon
from PySide6.QtWidgets import QWidget, QListWidgetItem

from src.utils.Search import SearchWorker
from src.views.mainWindow import Ui_MainWindow
import tempfile

TEMP_DIR = tempfile.gettempdir()


class MainWindowController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.search.clicked.connect(self.search)
        # connect the enter key to the search button
        self.ui.lineEdit.returnPressed.connect(self.ui.search.click)
        self.searchWorker = SearchWorker("")
        self.threadpool = QThreadPool()

    def search(self):
        self.resetUI()
        if self.ui.lineEdit.text() == "":
            return
        self.ui.lineEdit.setDisabled(True)
        self.ui.search.setDisabled(True)
        self.searchWorker = SearchWorker(self.ui.lineEdit.text())
        self.searchWorker.signals.result.connect(self.updateUI)
        # Execute
        self.threadpool.start(self.searchWorker)

    def updateUI(self, songs):
        self.ui.lineEdit.setText("")
        song = songs[0]
        self.ui.labelTitle.setText(song.name)
        self.ui.labelArtistName.setText(song.artist)
        self.ui.labelSeparator.setText("-")
        self.ui.labelDate.setText(song.date.split("-")[0])
        self.ui.labelNbTitle.setText(f"{len(songs)} tracks")
        self.getAndSetImageFromUrl(song.cover_url)
        self.ui.lineEdit.setDisabled(False)
        self.ui.search.setDisabled(False)

    def getAndSetImageFromUrl(self, imageURL):
        request = requests.get(imageURL)
        pixmap = QPixmap(150, 150)
        pixmap.loadFromData(request.content)
        pixmap = pixmap.scaledToWidth(200)
        self.ui.labelCoverAlbum.setPixmap(pixmap)

    def resetUI(self):
        self.ui.labelTitle.setText("")
        self.ui.labelArtistName.setText("")
        self.ui.labelSeparator.setText("")
        self.ui.labelDate.setText("")
        self.ui.labelNbTitle.setText("")
        self.ui.labelCoverAlbum.setPixmap(QPixmap())
        self.ui.listWidget.clear()

    # @QtCore.Slot()
    # def updateSpinnerAnimation(self):
    #     # 'hide' the text of the button
    #     self.ui.search.setText("")
    #     self.ui.search.setIcon(QtGui.QIcon(self.animated_spinner.currentPixmap()))
