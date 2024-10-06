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
import sys

from PySide6.QtCore import QTranslator, QCoreApplication, QFile, QTextStream
from PySide6.QtWidgets import QApplication
from dotenv import load_dotenv

from src.controllers.MainWindowController import MainWindowController
from src.utils.Config import Config
import assets.ressource
import psutil


def deleteLater():
    procname = ["SpotWrap", "spotdl", "spotdl.exe"]

    for proc in psutil.process_iter():
        # check whether the process name matches
        for p in procname:
            if proc.name() == p:
                proc.kill()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(deleteLater)
    app.setDesktopFileName("SpotWrap")
    load_dotenv()
    config = Config.get_instance()
    translator = QTranslator()
    translator.load(f':/translations/translations/{config.LOCALE}.qm')  # Path to the compiled .qm file
    QCoreApplication.installTranslator(translator)
    window = MainWindowController()
    # setup stylesheet
    # set stylesheet
    file = QFile(":/stylesheet/stylesheet.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    window.show()
    sys.exit(app.exec())
