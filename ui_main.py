# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainSLFHBi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(619, 453)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 70, 171, 221))
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"\n"
"	background-image: url(:/images/images/morginh1.png);\n"
"	border-radius: 20px;\n"
"	\n"
"	border:none;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.DAY = QLabel(self.frame)
        self.DAY.setObjectName(u"DAY")
        self.DAY.setGeometry(QRect(20, 20, 131, 31))
        self.DAY.setStyleSheet(u"font: 87 12pt \"Raleway\" bold;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(160, 80, 341, 201))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: #222831;\n"
"	border-radius: 20px;\n"
"	\n"
"	border:none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.close = QPushButton(self.frame_2)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(310, 10, 16, 16))
        self.close.setStyleSheet(u"background-color: rgb(192, 28, 40);\n"
"\n"
"\n"
"color: #00AA66;\n"
"border-color: #00AA66;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.DAY.setText(QCoreApplication.translate("MainWindow", u"<strong>DAY</strong>", None))
        self.close.setText("")
    # retranslateUi

