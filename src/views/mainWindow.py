# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)
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
        icon.addFile(u":/images/images/download_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(MainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.searchTab = QWidget()
        self.searchTab.setObjectName(u"searchTab")
        self.gridLayout_6 = QGridLayout(self.searchTab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_6 = QWidget(self.searchTab)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.progressBarMainWindow = QProgressBar(self.widget_6)
        self.progressBarMainWindow.setObjectName(u"progressBarMainWindow")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBarMainWindow.sizePolicy().hasHeightForWidth())
        self.progressBarMainWindow.setSizePolicy(sizePolicy1)
        self.progressBarMainWindow.setMaximumSize(QSize(16777215, 5))
        self.progressBarMainWindow.setMaximum(0)
        self.progressBarMainWindow.setValue(-1)
        self.progressBarMainWindow.setTextVisible(True)

        self.horizontalLayout_4.addWidget(self.progressBarMainWindow)

        self.menuButton = QPushButton(self.widget_6)
        self.menuButton.setObjectName(u"menuButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy2)
        self.menuButton.setMaximumSize(QSize(25, 25))
        self.menuButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon1)
        self.menuButton.setIconSize(QSize(15, 15))
        self.menuButton.setFlat(True)

        self.horizontalLayout_4.addWidget(self.menuButton, 0, Qt.AlignRight)


        self.gridLayout_5.addWidget(self.widget_6, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.widget = QWidget(self.searchTab)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
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
        sizePolicy2.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy2)
        self.search.setMinimumSize(QSize(50, 0))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon2)
        self.search.setCheckable(False)

        self.horizontalLayout.addWidget(self.search, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.searchTab)
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
        self.labelCoverAlbum.setMargin(4)

        self.gridLayout_2.addWidget(self.labelCoverAlbum, 0, 0, 1, 1)

        self.awidget_4 = QWidget(self.widget_3)
        self.awidget_4.setObjectName(u"awidget_4")
        self.gridLayout_4 = QGridLayout(self.awidget_4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelNbTitle = QLabel(self.awidget_4)
        self.labelNbTitle.setObjectName(u"labelNbTitle")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelNbTitle.sizePolicy().hasHeightForWidth())
        self.labelNbTitle.setSizePolicy(sizePolicy4)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy5)
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.labelTitle.setFont(font1)
        self.labelTitle.setWordWrap(True)

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

        self.labelDownloadFinished = QLabel(self.widget_5)
        self.labelDownloadFinished.setObjectName(u"labelDownloadFinished")

        self.horizontalLayout_3.addWidget(self.labelDownloadFinished)


        self.gridLayout_4.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.awidget_4)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.labelArtistName = QLabel(self.widget_4)
        self.labelArtistName.setObjectName(u"labelArtistName")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.labelArtistName.sizePolicy().hasHeightForWidth())
        self.labelArtistName.setSizePolicy(sizePolicy6)

        self.horizontalLayout_2.addWidget(self.labelArtistName)

        self.labelSeparator = QLabel(self.widget_4)
        self.labelSeparator.setObjectName(u"labelSeparator")
        sizePolicy6.setHeightForWidth(self.labelSeparator.sizePolicy().hasHeightForWidth())
        self.labelSeparator.setSizePolicy(sizePolicy6)

        self.horizontalLayout_2.addWidget(self.labelSeparator)

        self.labelDate = QLabel(self.widget_4)
        self.labelDate.setObjectName(u"labelDate")

        self.horizontalLayout_2.addWidget(self.labelDate)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.comboBoxOutPutType = QComboBox(self.widget_4)
        self.comboBoxOutPutType.setObjectName(u"comboBoxOutPutType")
        self.comboBoxOutPutType.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBoxOutPutType.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_2.addWidget(self.comboBoxOutPutType)

        self.comboBoxQuality = QComboBox(self.widget_4)
        self.comboBoxQuality.setObjectName(u"comboBoxQuality")
        self.comboBoxQuality.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.comboBoxQuality)

        self.buttonPath = QPushButton(self.widget_4)
        self.buttonPath.setObjectName(u"buttonPath")
        self.buttonPath.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonPath.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.buttonPath)

        self.buttonDownloadAll = QPushButton(self.widget_4)
        self.buttonDownloadAll.setObjectName(u"buttonDownloadAll")
        self.buttonDownloadAll.setEnabled(True)
        self.buttonDownloadAll.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.buttonDownloadAll)


        self.gridLayout_4.addWidget(self.widget_4, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.awidget_4, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.labelBigIcon = QLabel(self.widget_2)
        self.labelBigIcon.setObjectName(u"labelBigIcon")
        sizePolicy2.setHeightForWidth(self.labelBigIcon.sizePolicy().hasHeightForWidth())
        self.labelBigIcon.setSizePolicy(sizePolicy2)
        self.labelBigIcon.setMaximumSize(QSize(200, 200))
        self.labelBigIcon.setPixmap(QPixmap(u":/images/images/download_icon.png"))
        self.labelBigIcon.setScaledContents(True)
        self.labelBigIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelBigIcon, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 731, 86))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.listWidget = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setSpacing(0)
        self.listWidget.setViewMode(QListView.ListMode)

        self.gridLayout_3.addWidget(self.listWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.widget_2)


        self.gridLayout_6.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.tabWidget.addTab(self.searchTab, "")
        self.progressTab = QWidget()
        self.progressTab.setObjectName(u"progressTab")
        self.gridLayout_8 = QGridLayout(self.progressTab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.textEditDownloadProgress = QTextEdit(self.progressTab)
        self.textEditDownloadProgress.setObjectName(u"textEditDownloadProgress")
        self.textEditDownloadProgress.setReadOnly(True)

        self.gridLayout_7.addWidget(self.textEditDownloadProgress, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.progressTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SpotWrap", None))
        self.menuButton.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Collez votre lien Spotify...", None))
        self.search.setText("")
        self.labelCoverAlbum.setText("")
        self.labelNbTitle.setText("")
        self.labelTitle.setText("")
        self.labelDownloadFinished.setText("")
        self.labelArtistName.setText("")
        self.labelSeparator.setText("")
        self.labelDate.setText("")
        self.buttonPath.setText("")
        self.buttonDownloadAll.setText(QCoreApplication.translate("MainWindow", u"Tout t\u00e9l\u00e9charger", None))
        self.labelBigIcon.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchTab), QCoreApplication.translate("MainWindow", u"Recherche", None))
        self.textEditDownloadProgress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No current download", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.progressTab), QCoreApplication.translate("MainWindow", u"Progr\u00e8s", None))
    # retranslateUi

