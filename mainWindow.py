# -*- coding: utf-8 -*-

"""
Module implementing Transibi.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_mainWindow import Ui_Transibi


class Transibi(QMainWindow, Ui_Transibi):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Transibi, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_exitBtn_clicked(self):
        import sys
        sys.exit()
