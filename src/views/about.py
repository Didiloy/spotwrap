# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import assets.ressource

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(400, 547)
        icon = QIcon()
        icon.addFile(u":/images/images/download_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        About.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(About)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.labelIcon = QLabel(About)
        self.labelIcon.setObjectName(u"labelIcon")
        self.labelIcon.setScaledContents(False)
        self.labelIcon.setWordWrap(True)

        self.horizontalLayout.addWidget(self.labelIcon)

        self.labelName = QLabel(About)
        self.labelName.setObjectName(u"labelName")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.labelName.setFont(font)

        self.horizontalLayout.addWidget(self.labelName)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.labelVersion = QLabel(About)
        self.labelVersion.setObjectName(u"labelVersion")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setItalic(True)
        self.labelVersion.setFont(font1)

        self.verticalLayout_2.addWidget(self.labelVersion, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelLicence = QLabel(About)
        self.labelLicence.setObjectName(u"labelLicence")
        font2 = QFont()
        font2.setPointSize(12)
        self.labelLicence.setFont(font2)

        self.verticalLayout.addWidget(self.labelLicence)

        self.plainTextEditLicence = QPlainTextEdit(About)
        self.plainTextEditLicence.setObjectName(u"plainTextEditLicence")

        self.verticalLayout.addWidget(self.plainTextEditLicence)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"SpotWrap - About", None))
        self.labelIcon.setText("")
        self.labelName.setText(QCoreApplication.translate("About", u"SpotWrap", None))
        self.labelVersion.setText(QCoreApplication.translate("About", u"Version 1.1", None))
        self.labelLicence.setText(QCoreApplication.translate("About", u"Licence", None))
    # retranslateUi

