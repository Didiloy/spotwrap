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
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from src.views import GPL3_LICENCE
from src.views.about import Ui_About

VERSION = "1.2"


class AboutController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_About()
        self.ui.setupUi(self)
        self.ui.labelVersion.setText(f"Version {VERSION}")
        self.ui.plainTextEditLicence.setPlainText(GPL3_LICENCE)
        self.ui.plainTextEditLicence.setReadOnly(True)
        pixmap = QPixmap(":/images/images/download_icon.png")
        pixmap = pixmap.scaledToWidth(40)
        self.ui.labelIcon.setPixmap(pixmap)
