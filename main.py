import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class FractalGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("design.ui", self)


def excepthook(cls, value, traceback):
    sys.__excepthook__(cls, value, traceback)


if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = FractalGenerator()
    ex.show()
    sys.exit(app.exec())
