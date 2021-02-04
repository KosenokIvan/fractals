import sys
from math import sin, cos, radians
from typing import Dict
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPainter, QPixmap, QImage, QPen, QColor
from PyQt5 import uic
from l_system import LSystem


class FractalGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.parser = LStringParser("X", {"X": "-YF+XFX+FY-", "Y": "+XF-YFY-FX+"}, 16)
        self.image = QImage(512, 512, QImage.Format_ARGB32_Premultiplied)
        self.iteration = 0
        self.initUI()

    def initUI(self):
        uic.loadUi("design.ui", self)
        self.next_iteration_btn.clicked.connect(self.next_iteration)
        self.previous_iteration_btn.clicked.connect(self.previous_iteration)
        self.save_image_action.triggered.connect(self.save_in_file)
        self.draw()

    def draw(self):
        self.image = QImage(512, 512, QImage.Format_ARGB32_Premultiplied)
        self.parser.draw(self.iteration, 10, 90, self.image, 10, 502)
        self.image_container.setPixmap(QPixmap.fromImage(self.image))
        self.iteration_count_output.setText(f"Итерация: {self.iteration}")

    def next_iteration(self):
        if self.iteration < 7:
            self.iteration += 1
            self.draw()

    def previous_iteration(self):
        if self.iteration > 0:
            self.iteration -= 1
            self.draw()

    def save_in_file(self):
        filename = QFileDialog.getSaveFileName(self, "Выберите файл", "", "Изображение(*.png)")[0]
        self.image.save(filename)


class LStringParser(LSystem):
    def __init__(self, axiom: str, theorems: Dict[str, str], cash_size: int = 16):
        super().__init__(axiom, theorems, cash_size)

    def draw(self, iteration: int, line_length, delta_angle, canvas, x0, y0):
        save_data = []
        x_coord = x0
        y_coord = y0
        angle = 0
        qp = QPainter()
        qp.begin(canvas)
        qp.setPen(QColor(0, 0, 0))
        for char in self[iteration]:
            if char in ("F", "f", "G", "g"):
                x1 = round(x_coord + line_length * cos(radians(angle)))
                y1 = round(y_coord - line_length * sin(radians(angle)))
                if char in ("F", "G"):
                    qp.drawLine(x_coord, y_coord, x1, y1)
                x_coord, y_coord = x1, y1
            elif char == "+":
                angle -= delta_angle
                angle %= 360
            elif char == "-":
                angle += delta_angle
                angle %= 360
            elif char == "|":
                angle += 180
                angle %= 360
            elif char == "[":
                save_data.append((angle, x_coord, y_coord))
            elif char == "]":
                angle, x_coord, y_coord = save_data.pop()
        qp.end()


def excepthook(cls, value, traceback):
    sys.__excepthook__(cls, value, traceback)


if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = FractalGenerator()
    ex.show()
    sys.exit(app.exec())
