import sys, pafy, os, urllib.request
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from data.ui.main import Ui_MainWindow


class TubeDownloader(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(TubeDownloader, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)



def main():
    app = QApplication(sys.argv)
    window = TubeDownloader()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
