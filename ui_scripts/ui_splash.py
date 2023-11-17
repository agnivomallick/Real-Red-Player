# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashpeqdaI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QStatusBar, QWidget)

class Ui_Splash(object):
    def setupUi(self, Splash):
        if not Splash.objectName():
            Splash.setObjectName(u"Splash")
        Splash.resize(689, 477)
        self.centralwidget = QWidget(Splash)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 50, 581, 351))
        self.frame.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(166, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 40, 415, 61))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT Bold"])
        font.setPointSize(40)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: orangered;")
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(90, 200, 411, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"border: none;\n"
"border-radius: 10px;\n"
"background-color: crimson;\n"
"color: salmon;\n"
"text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"border: none;\n"
"background-color: #800000;\n"
"border-radius: 10px;\n"
"}")
        self.progressBar.setValue(24)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 280, 291, 20))
        self.label_2.setStyleSheet(u"color: white;")
        Splash.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Splash)
        self.statusbar.setObjectName(u"statusbar")
        Splash.setStatusBar(self.statusbar)

        self.retranslateUi(Splash)

        QMetaObject.connectSlotsByName(Splash)
    # setupUi

    def retranslateUi(self, Splash):
        Splash.setWindowTitle(QCoreApplication.translate("Splash", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Splash", u"Real Red Player", None))
        self.label_2.setText(QCoreApplication.translate("Splash", u"Copyright Agnivo's Software Corporation", None))
    # retranslateUi

