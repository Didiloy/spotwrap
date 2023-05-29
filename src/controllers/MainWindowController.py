import requests
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QListWidgetItem, QFileDialog

from src.controllers.SongController import SongController
from src.utils.Config import Config
from src.utils.Search import SearchWorker
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

        for song in songs:
            songItem = SongController(song.artist, song.name, song.track_number)
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
        self.ui.labelTitle.setText("")
        self.ui.labelArtistName.setText("")
        self.ui.labelSeparator.setText("")
        self.ui.labelDate.setText("")
        self.ui.labelNbTitle.setText("")
        self.ui.labelCoverAlbum.setPixmap(QPixmap())
        self.ui.buttonPath.setVisible(False)
        self.ui.buttonDownloadAll.setVisible(False)
        self.ui.listWidget.clear()

    def select_directory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.Option.DontUseNativeDialog

        directory = QFileDialog.getExistingDirectory(
            self, "Select Directory", options=options
        )
        if directory == "" or directory is None:
            return
        if directory != Config.get_instance().SAVE_PATH:
            Config.get_instance().SAVE_PATH = directory
            Config.get_instance().saveNewSavePath()

    # @QtCore.Slot()
    # def updateSpinnerAnimation(self):
    #     # 'hide' the text of the button
    #     self.ui.search.setText("")
    #     self.ui.search.setIcon(QtGui.QIcon(self.animated_spinner.currentPixmap()))
