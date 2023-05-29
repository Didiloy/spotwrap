import os

from PySide6.QtWidgets import QWidget, QListWidgetItem
from src.views.mainWindow import Ui_MainWindow
from spotdl import Spotdl


class MainWindowController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.spotdl = Spotdl(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
        print(os.getenv("CLIENT_ID"))

