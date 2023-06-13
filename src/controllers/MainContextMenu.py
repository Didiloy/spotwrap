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
import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QMenu

from src.controllers.AboutController import AboutController
from src.utils.Config import Config


def about():
    about_window = AboutController()
    about_window.show()
    about_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    about_window.exec_()


class MainContextMenu(QMenu):

    def __init__(self):
        super().__init__()
        # add menu actions(Action name, Action function)
        self.menu = QMenu("Language")
        self.menu.addAction("EN", lambda: self.change_locale("en_EN"))
        self.menu.addAction("FR", lambda: self.change_locale("fr_FR"))
        self.addMenu(self.menu)
        self.addAction("About", about)

    def change_locale(self, locale):
        Config.get_instance().LOCALE = locale
        Config.get_instance().saveLocale()
        os.execl(sys.executable, sys.executable, *sys.argv)
