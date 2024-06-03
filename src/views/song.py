# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'song.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import assets.ressource

class Ui_song(object):
    def setupUi(self, song):
        if not song.objectName():
            song.setObjectName(u"song")
        song.resize(599, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(song.sizePolicy().hasHeightForWidth())
        song.setSizePolicy(sizePolicy)
        song.setMinimumSize(QSize(0, 80))
        self.horizontalLayout = QHBoxLayout(song)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(song)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 80))
        self.frame_2.setStyleSheet(u"padding: 0px 5px; margin-bottom: 0px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.labelTrackNumber = QLabel(self.frame_2)
        self.labelTrackNumber.setObjectName(u"labelTrackNumber")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelTrackNumber.sizePolicy().hasHeightForWidth())
        self.labelTrackNumber.setSizePolicy(sizePolicy1)
        self.labelTrackNumber.setStyleSheet(u"margin-left: 5px;")

        self.horizontalLayout_2.addWidget(self.labelTrackNumber)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.widget_3.setMinimumSize(QSize(0, 79))
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 29, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.labelAlbumCover = QLabel(self.widget_3)
        self.labelAlbumCover.setObjectName(u"labelAlbumCover")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelAlbumCover.sizePolicy().hasHeightForWidth())
        self.labelAlbumCover.setSizePolicy(sizePolicy3)
        self.labelAlbumCover.setMinimumSize(QSize(70, 70))
        self.labelAlbumCover.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelAlbumCover)

        self.verticalSpacer = QSpacerItem(20, 29, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelSongTitle = QLabel(self.widget)
        self.labelSongTitle.setObjectName(u"labelSongTitle")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelSongTitle.sizePolicy().hasHeightForWidth())
        self.labelSongTitle.setSizePolicy(sizePolicy4)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.labelSongTitle.setFont(font)

        self.verticalLayout.addWidget(self.labelSongTitle)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.labelSongArtists = QLabel(self.widget)
        self.labelSongArtists.setObjectName(u"labelSongArtists")
        sizePolicy4.setHeightForWidth(self.labelSongArtists.sizePolicy().hasHeightForWidth())
        self.labelSongArtists.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setItalic(True)
        self.labelSongArtists.setFont(font1)

        self.verticalLayout.addWidget(self.labelSongArtists)


        self.horizontalLayout_2.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(507, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.labelDuration = QLabel(self.frame_2)
        self.labelDuration.setObjectName(u"labelDuration")

        self.horizontalLayout_2.addWidget(self.labelDuration)

        self.buttonDelete = QPushButton(self.frame_2)
        self.buttonDelete.setObjectName(u"buttonDelete")
        self.buttonDelete.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/images/images/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonDelete.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.buttonDelete)

        self.buttonDownload = QPushButton(self.frame_2)
        self.buttonDownload.setObjectName(u"buttonDownload")
        self.buttonDownload.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonDownload.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.buttonDownload)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setMinimumSize(QSize(90, 10))
        self.progressBar.setMaximumSize(QSize(90, 10))
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.labelDownloadFinished = QLabel(self.frame_2)
        self.labelDownloadFinished.setObjectName(u"labelDownloadFinished")

        self.horizontalLayout_2.addWidget(self.labelDownloadFinished)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(song)

        QMetaObject.connectSlotsByName(song)
    # setupUi

    def retranslateUi(self, song):
        song.setWindowTitle(QCoreApplication.translate("song", u"Form", None))
        self.labelTrackNumber.setText("")
        self.labelAlbumCover.setText("")
        self.labelSongTitle.setText("")
        self.labelSongArtists.setText("")
        self.labelDuration.setText("")
        self.buttonDelete.setText("")
        self.buttonDownload.setText("")
        self.labelDownloadFinished.setText("")
    # retranslateUi

