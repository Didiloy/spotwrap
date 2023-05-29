# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'song.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_song(object):
    def setupUi(self, song):
        if not song.objectName():
            song.setObjectName(u"song")
        song.resize(599, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(song.sizePolicy().hasHeightForWidth())
        song.setSizePolicy(sizePolicy)
        song.setMinimumSize(QSize(0, 100))
        self.horizontalLayout = QHBoxLayout(song)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelTrackNumber = QLabel(song)
        self.labelTrackNumber.setObjectName(u"labelTrackNumber")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelTrackNumber.sizePolicy().hasHeightForWidth())
        self.labelTrackNumber.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.labelTrackNumber)

        self.line_2 = QFrame(song)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.widget = QWidget(song)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelSongTitle = QLabel(self.widget)
        self.labelSongTitle.setObjectName(u"labelSongTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelSongTitle.sizePolicy().hasHeightForWidth())
        self.labelSongTitle.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.labelSongTitle.setFont(font)

        self.verticalLayout.addWidget(self.labelSongTitle)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.labelSongArtists = QLabel(self.widget)
        self.labelSongArtists.setObjectName(u"labelSongArtists")
        sizePolicy2.setHeightForWidth(self.labelSongArtists.sizePolicy().hasHeightForWidth())
        self.labelSongArtists.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setItalic(True)
        self.labelSongArtists.setFont(font1)

        self.verticalLayout.addWidget(self.labelSongArtists)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonDownloadSingleSong = QPushButton(song)
        self.buttonDownloadSingleSong.setObjectName(u"buttonDownloadSingleSong")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttonDownloadSingleSong.sizePolicy().hasHeightForWidth())
        self.buttonDownloadSingleSong.setSizePolicy(sizePolicy3)
        self.buttonDownloadSingleSong.setMinimumSize(QSize(94, 36))

        self.horizontalLayout.addWidget(self.buttonDownloadSingleSong)


        self.retranslateUi(song)

        QMetaObject.connectSlotsByName(song)
    # setupUi

    def retranslateUi(self, song):
        song.setWindowTitle(QCoreApplication.translate("song", u"Form", None))
        self.labelTrackNumber.setText("")
        self.labelSongTitle.setText("")
        self.labelSongArtists.setText("")
        self.buttonDownloadSingleSong.setText(QCoreApplication.translate("song", u"T\u00e9l\u00e9charger", None))
    # retranslateUi

