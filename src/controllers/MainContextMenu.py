import os
import subprocess
import sys

from PySide6.QtWidgets import QMenu

from src.utils.Config import Config


class MainContextMenu(QMenu):

    def __init__(self):
        super().__init__()
        # add menu actions(Action name, Action function)
        self.menu = QMenu("Language")
        self.menu.addAction("EN", lambda: self.change_locale("en_EN"))
        self.menu.addAction("FR", lambda: self.change_locale("fr_FR"))
        self.addMenu(self.menu)
        self.addAction("About", self.about)

    def about(self):
        print("about")

    def change_locale(self, locale):
        Config.get_instance().LOCALE = locale
        Config.get_instance().saveLocale()
        os.execl(sys.executable, sys.executable, *sys.argv)
