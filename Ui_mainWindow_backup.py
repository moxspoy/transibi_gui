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
from SpeechRecognition import SpeechRecognition


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
        Transibi.resize(579, 377)
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
        self.videoframe.setGeometry(QtCore.QRect(140, 20, 421, 251))
        self.videoframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.videoframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.videoframe.setObjectName("frame")
        self.palette = self.videoframe.palette()
        self.palette.setColor(QtGui.QPalette.Window, QtGui.QColor(0, 200, 200))
        self.videoframe.setPalette(self.palette)
        self.videoframe.setAutoFillBackground(True)

        
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(140, 280, 101, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        
        self.caption = QtWidgets.QLabel(self.centralWidget)
        self.caption.setGeometry(QtCore.QRect(240, 280, 301, 21))
        self.caption.setObjectName("caption")
        
        Transibi.setCentralWidget(self.centralWidget)

        self.retranslateUi(Transibi)
        QtCore.QMetaObject.connectSlotsByName(Transibi)

    def retranslateUi(self, Transibi):
        init_label_text = "lorem lorem ipsum ipsum lorem lorem lorem ipsum ipsumlorem lorem ipsum ipsumlorem ipsum ipsum"
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
        
        end_time = self.get_time()
        int_interval = end_time - start_time
        interval = str(int_interval)
        result = result + ", waktu process " + interval + " ms"
        self.caption.setText(result)
     
    def get_time(self):
        current_time = int(round(time.time() * 1000))
        return current_time

    def open_help(self):
        """ Open help dialog """
        
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

