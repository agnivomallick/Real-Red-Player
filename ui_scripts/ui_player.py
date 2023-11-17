# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playerDTASrp.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(664, 583)
        MainWindow.setWindowTitle(u"Real Red Player")
        MainWindow.setStyleSheet(u"background-color: red;")
        self.videocontainer = QWidget()
        self.videocontainer.setObjectName(u"videocontainer")
        self.videocontainer.setGeometry(QRect(39, 29, 561, 371))
        self.openButton = QPushButton()
        self.openButton.setObjectName(u"openButton")
        self.openButton.setGeometry(QRect(40, 500, 75, 24))
        self.playButton = QPushButton()
        self.playButton.setObjectName(u"playButton")
        # self.playButton.setEnabled(False)
        self.playButton.setGeometry(QRect(530, 500, 75, 24))
        self.durationslider = QSlider()
        self.durationslider.setObjectName(u"durationslider")
        self.durationslider.setGeometry(QRect(250, 500, 160, 22))
        self.durationslider.setOrientation(Qt.Horizontal)
        self.durationslider.setRange(0, 0)
        self.positionText = QLabel()
        self.positionText.setObjectName(u"positionText")
        self.positionText.setGeometry(QRect(170, 500, 49, 16))
        self.stopButton = QPushButton()
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(470, 490, 75, 24))
        self.stopButton.setText("Stop")
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.positionText.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        pass
    # retranslateUi

