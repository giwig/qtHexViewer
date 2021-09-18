import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QRadioButton, QSizePolicy
from hexview import HexViewWidget
from ui.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    buf: bytearray = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.setupUi(self)

        with open("main.py") as f:
            self.buf = f.read()

        btn = QPushButton("LALALA")
        btn.setParent(self.gbRight)
        self.verticalLayout.addWidget(btn)

        hv = HexViewWidget(self.buf)
        hv.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        hv.setParent(self.gbRight)
        self.verticalLayout.addWidget(hv)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
