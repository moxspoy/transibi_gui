from PyQt5.QtWidgets import QApplication,  QMainWindow
from Ui_mainWindow import Ui_Transibi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Transibi = QMainWindow()
    ui = Ui_Transibi()
    ui.setupUi(Transibi)
    Transibi.show()
    sys.exit(app.exec_())

