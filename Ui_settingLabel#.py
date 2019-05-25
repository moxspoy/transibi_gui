# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/transibi/eric_project/settingLabel#.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Transibi(object):
    def setupUi(self, Transibi):
        Transibi.setObjectName("Transibi")
        Transibi.resize(778, 427)
        self.centralWidget = QtWidgets.QWidget(Transibi)
        self.centralWidget.setObjectName("centralWidget")
        self.listenBtn = QtWidgets.QPushButton(self.centralWidget)
        self.listenBtn.setGeometry(QtCore.QRect(10, 70, 101, 51))
        self.listenBtn.setObjectName("listenBtn")
        self.helpBtn = QtWidgets.QPushButton(self.centralWidget)
        self.helpBtn.setGeometry(QtCore.QRect(10, 130, 101, 51))
        self.helpBtn.setObjectName("helpBtn")
        self.historyBtn = QtWidgets.QPushButton(self.centralWidget)
        self.historyBtn.setGeometry(QtCore.QRect(10, 190, 101, 61))
        self.historyBtn.setObjectName("historyBtn")
        self.exitBtn = QtWidgets.QPushButton(self.centralWidget)
        self.exitBtn.setGeometry(QtCore.QRect(10, 260, 101, 51))
        self.exitBtn.setObjectName("exitBtn")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(140, 20, 421, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(140, 280, 101, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.caption = QtWidgets.QLabel(self.centralWidget)
        self.caption.setGeometry(QtCore.QRect(240, 280, 311, 71))
        self.caption.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.caption.setObjectName("caption")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(140, 310, 67, 21))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(650, 30, 91, 101))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../src/logo_dikti.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(650, 150, 91, 101))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../src/unj.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        Transibi.setCentralWidget(self.centralWidget)

        self.retranslateUi(Transibi)
        QtCore.QMetaObject.connectSlotsByName(Transibi)

    def retranslateUi(self, Transibi):
        _translate = QtCore.QCoreApplication.translate
        Transibi.setWindowTitle(_translate("Transibi", "Transibi - Penerjemah Suara ke SIBI"))
        self.listenBtn.setText(_translate("Transibi", "Dengarkan"))
        self.helpBtn.setText(_translate("Transibi", "Bantuan"))
        self.historyBtn.setText(_translate("Transibi", "Riwayat"))
        self.exitBtn.setText(_translate("Transibi", "Keluar"))
        self.label.setText(_translate("Transibi", "Menu"))
        self.label_2.setText(_translate("Transibi", "Anda berkata: "))
        self.caption.setText(_translate("Transibi", "...."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Transibi = QtWidgets.QMainWindow()
    ui = Ui_Transibi()
    ui.setupUi(Transibi)
    Transibi.show()
    sys.exit(app.exec_())

