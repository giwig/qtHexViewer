import os.path
import sys

import hexview
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QRadioButton, QSizePolicy, QFileDialog
from PyQt5.QtCore import Qt
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
        self.verticalLayout_2.addWidget(self.hv)
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
                self.verticalLayout_2.addWidget(self.hv)
                self.hv.getColorModel().color_region(1, 10, Qt.darkGreen)
                self.hv.getBorderModel().border_region(1, 10, Qt.yellow)
                self.hv.getSelectionModel().bselect(11, 22)
                self.hv.view.viewOptions().font.setFamily("Lucida Console")
                # self.hv.view.off
                print(type(self.hv._buf))
                self.hv._buf.replace(' ', '')
                self.hv.repaint()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
