# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/transibi/eric_project/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

import platform
import os
import sys
import time
import threading
import vlc

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from SpeechRecognition import SpeechRecognition
from Ui_helpDialog import Ui_Dialog

class Ui_Transibi(object):
    def __init__(self, master=None):
        # Create a basic vlc instance
        self.instance = vlc.Instance()

        self.media = None

        # Create an empty vlc media player
        self.mediaplayer = self.instance.media_player_new()

        self.is_paused = False
        
    def setupUi(self, Transibi):
        Transibi.setObjectName("Transibi")
        Transibi.resize(920, 577)
        self.transibi = Transibi
        self.centralWidget = QtWidgets.QWidget(Transibi)
        self.centralWidget.setObjectName("centralWidget")
        
        self.listenBtn = QtWidgets.QPushButton(self.centralWidget)
        self.listenBtn.setGeometry(QtCore.QRect(10, 70, 101, 51))
        self.listenBtn.setObjectName("listenBtn")
        self.listenBtn.clicked.connect(self.listen_thread)
        
        self.helpBtn = QtWidgets.QPushButton(self.centralWidget)
        self.helpBtn.setGeometry(QtCore.QRect(10, 130, 101, 51))
        self.helpBtn.setObjectName("helpBtn")
        self.helpBtn.clicked.connect(self.open_help)
        
        self.historyBtn = QtWidgets.QPushButton(self.centralWidget)
        self.historyBtn.setGeometry(QtCore.QRect(10, 190, 101, 61))
        self.historyBtn.setObjectName("historyBtn")
        self.historyBtn.clicked.connect(self.open_history)
        
        self.exitBtn = QtWidgets.QPushButton(self.centralWidget)
        self.exitBtn.setGeometry(QtCore.QRect(10, 260, 101, 51))
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtn.clicked.connect(self.exit_from_app)
        
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.videoframe = QtWidgets.QFrame(self.centralWidget)
        self.videoframe.setGeometry(QtCore.QRect(140, 20, 521, 451))
        self.videoframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.videoframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.videoframe.setObjectName("frame")
        self.palette = self.videoframe.palette()
        self.palette.setColor(QtGui.QPalette.Window, QtGui.QColor(0, 200, 200))
        self.videoframe.setPalette(self.palette)
        self.videoframe.setAutoFillBackground(True)

        
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(140, 480, 101, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        
        self.caption = QtWidgets.QLabel(self.centralWidget,  wordWrap = True)
        self.caption.setGeometry(QtCore.QRect(240, 480, 301, 71))
        self.caption.setObjectName("caption")
        self.caption.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        
        self.dikti= QtWidgets.QLabel(self.centralWidget)
        self.dikti.setGeometry(QtCore.QRect(750, 30, 91, 101))
        self.dikti.setText("")
        self.dikti.setPixmap(QtGui.QPixmap("../src/logo_dikti.png"))
        self.dikti.setScaledContents(True)
        self.dikti.setWordWrap(True)
        self.dikti.setObjectName("dikti")
        self.unj = QtWidgets.QLabel(self.centralWidget)
        self.unj.setGeometry(QtCore.QRect(750, 150, 91, 101))
        self.unj.setText("")
        self.unj.setPixmap(QtGui.QPixmap("../src/unj.png"))
        self.unj.setScaledContents(True)
        self.unj.setWordWrap(True)
        self.unj.setObjectName("unj")
        Transibi.setCentralWidget(self.centralWidget)
        
        Transibi.setCentralWidget(self.centralWidget)

        self.retranslateUi(Transibi)
        QtCore.QMetaObject.connectSlotsByName(Transibi)

    def retranslateUi(self, Transibi):
        init_label_text = "Yang anda katakan ada di sini"
        _translate = QtCore.QCoreApplication.translate
        Transibi.setWindowTitle(_translate("Transibi", "Transibi - Penerjemah Suara ke SIBI"))
        self.listenBtn.setText(_translate("Transibi", "Dengarkan"))
        self.helpBtn.setText(_translate("Transibi", "Bantuan"))
        self.historyBtn.setText(_translate("Transibi", "Riwayat"))
        self.exitBtn.setText(_translate("Transibi", "Keluar"))
        self.label.setText(_translate("Transibi", "Menu"))
        self.label_2.setText(_translate("Transibi", "Anda berkata: "))
        self.caption.setText(_translate("Transibi", init_label_text))
        
    def listen_thread(self):
        self.caption.setText("Mendengarkan...")
        t = threading.Thread(target = self.listen_speech)
        t.start()
        
    def listen_speech(self):
        """ Calculate time """
        start_time = self.get_time()
        """ Speech recognition process """
        speech = SpeechRecognition()
        result = speech.listen()
        
        self.play_video_from_words(result)
        
        end_time = self.get_time()
        int_interval = end_time - start_time
        interval = str(int_interval)
        result_log = result + ", waktu process " + interval + " ms"
        self.caption.setText(result_log)
        print(result)
        
    def get_time(self):
        current_time = int(round(time.time() * 1000))
        return current_time
        
    def play_video_from_words(self,  words):
        splitted_words = words.split()
        for m in splitted_words:
            self.caption.setText(m)
            filename = "/home/pi/transibi/src/" + m + ".mp4"
            self.play_video(filename,  m)
    
    def play_video(self,  filename,  basename):
        
        # getOpenFileName returns a tuple, so use only the actual file name
        self.media = self.instance.media_new(filename)

        # Put the media in the media player
        self.mediaplayer.set_media(self.media)

        # Parse the metadata of the file
        self.media.parse()

        # The media player has to be 'connected' to the QFrame (otherwise the
        # video would be displayed in it's own window). This is platform
        # specific, so we must give the ID of the QFrame (or similar object) to
        # vlc. Different platforms have different functions for this
        if platform.system() == "Linux": # for Linux using the X Server
            self.mediaplayer.set_xwindow(int(self.videoframe.winId()))
        elif platform.system() == "Windows": # for Windows
            self.mediaplayer.set_hwnd(int(self.videoframe.winId()))
        elif platform.system() == "Darwin": # for MacOS
            self.mediaplayer.set_nsobject(int(self.videoframe.winId()))
        
        self.mediaplayer.play()
        time.sleep(0.1)
        duration = self.mediaplayer.get_length() / 1000
        time.sleep(duration)
        self.mediaplayer.stop()

    def open_help(self):
        """ Open help dialog """
        self.Dialog = QtWidgets.QDialog()
        self.uiDialog = Ui_Dialog()
        self.uiDialog.setupUi(self.Dialog)
        self.Dialog.show()
    def open_history(self):
        """ Open history dialog """
        
        
    def exit_from_app(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Transibi = QtWidgets.QMainWindow()
    ui = Ui_Transibi()
    ui.setupUi(Transibi)
    Transibi.show()
    sys.exit(app.exec_())

