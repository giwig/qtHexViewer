import os.path
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QRadioButton, QSizePolicy, QFileDialog
from hexview import HexViewWidget
from ui.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    buf: bytearray = bytearray(0)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.hv = HexViewWidget(self.buf)
        self.hv.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.hv.setParent(self.gbRight)
        self.verticalLayout.addWidget(self.hv)
        self.binding()

    def binding(self):
        self.actionOpen.triggered.connect(self.on_open_action)

    def on_open_action(self):
        print("Open")
        file, check = QFileDialog.getOpenFileNames(None, 'Open file...', '.')
        if check:
            print(file[0])
            if os.path.isfile(file[0]):
                with open(file[0]) as f:
                    self.buf = f.read()
                self.hv.close()
                self.hv = HexViewWidget(self.buf)
                self.hv.setParent(self.gbRight)
                self.verticalLayout.addWidget(self.hv)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
