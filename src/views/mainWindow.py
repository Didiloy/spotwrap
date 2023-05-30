# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import assets.ressource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 574)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/images/download.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 6)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.search = QPushButton(self.widget)
        self.search.setObjectName(u"search")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy2)
        self.search.setMinimumSize(QSize(50, 0))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon1)
        self.search.setCheckable(False)

        self.horizontalLayout.addWidget(self.search, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(MainWindow)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, -1, -1, -1)
        self.labelCoverAlbum = QLabel(self.widget_3)
        self.labelCoverAlbum.setObjectName(u"labelCoverAlbum")
        sizePolicy2.setHeightForWidth(self.labelCoverAlbum.sizePolicy().hasHeightForWidth())
        self.labelCoverAlbum.setSizePolicy(sizePolicy2)
        self.labelCoverAlbum.setMinimumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.labelCoverAlbum, 0, 0, 1, 1)

        self.awidget_4 = QWidget(self.widget_3)
        self.awidget_4.setObjectName(u"awidget_4")
        self.gridLayout_4 = QGridLayout(self.awidget_4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelNbTitle = QLabel(self.awidget_4)
        self.labelNbTitle.setObjectName(u"labelNbTitle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelNbTitle.sizePolicy().hasHeightForWidth())
        self.labelNbTitle.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setItalic(True)
        self.labelNbTitle.setFont(font)

        self.gridLayout_4.addWidget(self.labelNbTitle, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.awidget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.labelTitle = QLabel(self.widget_5)
        self.labelTitle.setObjectName(u"labelTitle")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.labelTitle.setFont(font1)

        self.horizontalLayout_3.addWidget(self.labelTitle)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(self.widget_5)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setMinimumSize(QSize(230, 10))
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.gridLayout_4.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.awidget_4)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.labelArtistName = QLabel(self.widget_4)
        self.labelArtistName.setObjectName(u"labelArtistName")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labelArtistName.sizePolicy().hasHeightForWidth())
        self.labelArtistName.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.labelArtistName)

        self.labelSeparator = QLabel(self.widget_4)
        self.labelSeparator.setObjectName(u"labelSeparator")
        sizePolicy5.setHeightForWidth(self.labelSeparator.sizePolicy().hasHeightForWidth())
        self.labelSeparator.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.labelSeparator)

        self.labelDate = QLabel(self.widget_4)
        self.labelDate.setObjectName(u"labelDate")

        self.horizontalLayout_2.addWidget(self.labelDate)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.buttonPath = QPushButton(self.widget_4)
        self.buttonPath.setObjectName(u"buttonPath")

        self.horizontalLayout_2.addWidget(self.buttonPath)

        self.buttonDownloadAll = QPushButton(self.widget_4)
        self.buttonDownloadAll.setObjectName(u"buttonDownloadAll")
        self.buttonDownloadAll.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.buttonDownloadAll)


        self.gridLayout_4.addWidget(self.widget_4, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.awidget_4, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 779, 324))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.listWidget = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setSpacing(5)

        self.gridLayout_3.addWidget(self.listWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.widget_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SpotWrap", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search..", None))
        self.search.setText("")
        self.labelCoverAlbum.setText("")
        self.labelNbTitle.setText("")
        self.labelTitle.setText("")
        self.labelArtistName.setText("")
        self.labelSeparator.setText("")
        self.labelDate.setText("")
        self.buttonPath.setText(QCoreApplication.translate("MainWindow", u"Emplacement", None))
        self.buttonDownloadAll.setText(QCoreApplication.translate("MainWindow", u"Tout t\u00e9l\u00e9charger", None))
    # retranslateUi

