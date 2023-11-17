

from PySide6.QtWidgets import *  # Qt Widgets
from PySide6.QtCore import Qt, QTimer, QUrl  # Some Core tools
from PySide6.QtGui import QIcon  # icons
from PySide6.QtMultimediaWidgets import QVideoWidget  # video widget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput  # media player and audio output helpers


from ui_scripts.ui_splash import Ui_Splash
from ui_scripts.ui_player import Ui_MainWindow
import sys
import os

counter = 0  # progressbar


basedir = os.path.dirname(__file__)

try:
    from ctypes import windll
    myappid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

except ImportError:
    pass


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # some settings
        self.setCentralWidget(self.ui.videocontainer)
        icon = QIcon(os.path.join(basedir, "player_icon.png"))
        self.setWindowIcon(icon)

        self.ui.positionText.setText(str(0) + ":" + str(0) + ":" + str(0))
        self.player = QMediaPlayer()
        self.videoWidget = QVideoWidget()
        self.audioOutput = QAudioOutput()

        self.ui.playButton.setEnabled(False)
        self.ui.stopButton.setEnabled(False)
        self.ui.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.ui.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.ui.openButton.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))

        hbox = QHBoxLayout()
        hbox.addWidget(self.ui.openButton)
        hbox.addWidget(self.ui.playButton)
        hbox.addWidget(self.ui.positionText)
        hbox.addWidget(self.ui.durationslider)
        hbox.addWidget(self.ui.stopButton)

        vbox = QVBoxLayout()
        vbox.addWidget(self.videoWidget)
        vbox.addLayout(hbox)
        self.ui.videocontainer.setLayout(vbox)

        # all the connections (events) attached to the buttons and assigning audio output and video output variables.
        self.player.setAudioOutput(self.audioOutput)
        self.player.setVideoOutput(self.videoWidget)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)
        self.ui.durationslider.sliderMoved.connect(self.sliderMoved)
        self.ui.openButton.clicked.connect(self.openFile)
        self.ui.playButton.clicked.connect(self.playMedia)
        self.ui.stopButton.clicked.connect(self.stopMedia)

    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open Media File", "C:", "All media files (*.ogg *.mp4 *.mp3 *.flac *.ape *.mpe *.wv *.aif)")  # list of formats supported by the player.

        if file == "":
            return

        self.player.setSource(QUrl.fromLocalFile(file))
        self.ui.playButton.setEnabled(True)
        self.ui.playButton.setText("Play")
        self.ui.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def playMedia(self):
        if self.player.source() != QUrl(''):

            self.ui.stopButton.setEnabled(True)

            if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
                self.player.pause()
                self.ui.playButton.setText("Play")
                self.ui.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            else:
                self.player.play()
                self.ui.playButton.setText("Pause")
                self.ui.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

    def stopMedia(self):
        if self.player.source() != QUrl(''):
            self.player.stop()
            self.ui.playButton.setText("Play")
            self.ui.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.player.setSource(QUrl(''))
            self.ui.playButton.setEnabled(False)
            self.ui.stopButton.setEnabled(False)

    def positionChanged(self, position):
        self.ui.durationslider.setValue(position)
        seconds = int((position / 1000) % 60)
        minutes = int((position / (1000 * 60)) % 60)
        hours = int((position / (1000 * 60 * 60)) % 24)

        self.ui.positionText.setText(str(hours) + ":" + str(minutes) + ":" + str(seconds))

    def durationChanged(self, duration):
        self.ui.durationslider.setRange(0, duration)

    def sliderMoved(self, position):
        self.player.setPosition(position)


class SplashScreen(QMainWindow):
    def __init__(self):
        super(SplashScreen, self).__init__()

        self.ui = Ui_Splash()
        self.ui.setupUi(self)

        # remove title bar and window.
        # to show only the frame.
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        icon = QIcon(os.path.join(basedir, "player_icon.png"))
        self.setWindowIcon(icon)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.show()

    def progress(self):
        global counter

        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()

            self.mainWindow = MainWindow()
            self.mainWindow.show()

            self.close()

        counter += 1


if __name__ == '__main__':
    app = QApplication()
    splashscreen = SplashScreen()
    sys.exit(app.exec())
