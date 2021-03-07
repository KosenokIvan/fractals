import sys
from math import sin, cos, radians
from typing import Dict
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QPixmap, QImage, QPen, QColor
from PyQt5 import uic
from image_window import Ui_MainWindow as UIImageWindow
from l_system_config_window import Ui_MainWindow as UILSystemConfigWindow
from theorem_widget import Ui_Form as UITheoremWidget
from l_system import LSystem
import constants as cst


class FractalGeneratorWindow(QMainWindow, UIImageWindow):
    def __init__(self):
        super().__init__()
        self.l_config_manager = LSystemConfigManager(self, cst.INIT_AXIOM,
                                                     cst.INIT_THEOREMS,
                                                     cst.INIT_LINE_LENGTH,
                                                     cst.INIT_DELTA_ANGLE)
        self.parser = LStringParser(cst.INIT_AXIOM, cst.INIT_THEOREMS, cst.CASH_SIZE)
        self.image = QImage(512, 512, QImage.Format_ARGB32_Premultiplied)
        self.initUI()

    def initUI(self):
        # self.setupUi(self)
        uic.loadUi("design/image_window.ui", self)
        self.next_iteration_btn.clicked.connect(self.next_iteration)
        self.previous_iteration_btn.clicked.connect(self.previous_iteration)
        self.save_image_action.triggered.connect(self.save_in_file)
        self.configuration_action.triggered.connect(self.open_l_system_config_window)
        self.draw()

    def draw(self):
        self.image = QImage(512, 512, QImage.Format_ARGB32_Premultiplied)
        l_string_length = self.parser.draw(self.l_config_manager.get_iteration(),
                                           self.l_config_manager.get_line_length(),
                                           self.l_config_manager.get_rotate_angle(),
                                           self.image, 10, 502)
        self.l_config_manager.set_l_string_length(l_string_length)
        self.image_container.setPixmap(QPixmap.fromImage(self.image))
        self.iteration_count_output.setText(f"Итерация: {self.l_config_manager.get_iteration()}")

    def next_iteration(self):
        if self.l_config_manager.get_l_string_length() < cst.MAX_STRING_LENGTH:
            self.l_config_manager.set_iteration(self.l_config_manager.get_iteration() + 1)
            self.draw()
        else:
            self.statusbar.showMessage("Слишком большая длина l-строки, "
                                       "увеличение итерации заблокировано",
                                       cst.STATUS_BAR_TIMEOUT)

    def previous_iteration(self):
        if self.l_config_manager.get_iteration() > 0:
            self.l_config_manager.set_iteration(self.l_config_manager.get_iteration() - 1)
            self.draw()
        else:
            self.statusbar.showMessage("Итерация не может быть отрицательной",
                                       cst.STATUS_BAR_TIMEOUT)

    def save_in_file(self):
        filename = QFileDialog.getSaveFileName(self, "Выберите файл", "", "Изображение(*.png)")[0]
        if not filename:
            return
        self.image.save(filename)

    def open_l_system_config_window(self):
        window = LSystemConfigWindow(self, self.l_config_manager)
        window.show()

    def update_l_system_configuration(self):
        self.parser = LStringParser(self.l_config_manager.get_axiom(),
                                    self.l_config_manager.get_theorems(), 16)
        self.l_config_manager.set_iteration(0)
        self.draw()


class LSystemConfigManager:
    def __init__(self, fr_generator: FractalGeneratorWindow, axiom: str,
                 theorems: Dict[str, str], line_length: int, rotate_angle: int):
        self.fr_generator = fr_generator
        self.axiom = axiom
        self.theorems = theorems.copy()
        self.line_length = line_length
        self.rotate_angle = rotate_angle
        self.iteration = 0
        self.l_string_length = 0

    def get_iteration(self):
        return self.iteration

    def set_iteration(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f"Required type: int; Received type: {type(value)}")
        if value < 0:
            raise ValueError(f"Negative value: {value}")
        self.iteration = value

    def get_l_string_length(self):
        return self.l_string_length

    def set_l_string_length(self, value):
        self.l_string_length = value

    def get_axiom(self):
        return self.axiom

    def set_axiom(self, value: str):
        self.axiom = value

    def get_theorems(self):
        return self.theorems.copy()

    def get_theorem(self, key: str):
        return self.theorems.get(key, key)

    def set_theorems(self, theorems: Dict[str, str]):
        self.theorems = theorems.copy()

    def set_theorem(self, key: str, value: str):
        self.theorems[key] = value

    def get_line_length(self):
        return self.line_length

    def set_line_length(self, value: int):
        self.line_length = value

    def get_rotate_angle(self):
        return self.rotate_angle

    def set_rotate_angle(self, value: int):
        self.rotate_angle = value

    def update_generator_configuration(self):
        self.fr_generator.update_l_system_configuration()


class LSystemConfigWindow(QMainWindow, UILSystemConfigWindow):
    def __init__(self, parent, manager: LSystemConfigManager):
        super().__init__(parent)
        self.manager = manager
        self.theorems_list = TheoremsListWidget(self)
        self.initUI()
        self.theorems_sa.setWidget(self.theorems_list)

    def initUI(self):
        # self.setupUi(self)
        uic.loadUi("design/l_system_config_window.ui", self)
        self.add_theorem_btn.clicked.connect(lambda: self.add_theorem())
        self.confirm_btn.clicked.connect(self.update_manager)
        self.axiom_input.setText(self.manager.get_axiom())
        self.rotate_angle_input.setValue(self.manager.get_rotate_angle())
        self.line_length_input.setValue(self.manager.get_line_length())
        for th_input, th_output in self.manager.get_theorems().items():
            self.add_theorem(th_input, th_output)

    def add_theorem(self, th_input="", th_output=""):
        self.theorems_list.add_theorem(th_input, th_output)

    def update_manager(self):
        axiom = self.axiom_input.text().strip()
        if not axiom:
            self.statusbar.showMessage("Не указана аксиома", cst.STATUS_BAR_TIMEOUT)
            return
        theorems = {}
        for theorem_item in self.theorems_list.get_theorems():
            theorem = theorem_item.widget()
            th_input, th_output = map(str.strip, theorem.get_theorem())
            if not th_input:
                self.statusbar.showMessage("Не указаны входные данные теоремы!",
                                           cst.STATUS_BAR_TIMEOUT)
                return
            if th_input in theorems:
                self.statusbar.showMessage("Теоремы с одинаковыми входными данными",
                                           cst.STATUS_BAR_TIMEOUT)
                return
            theorems[th_input] = th_output
        rotate_angle = self.rotate_angle_input.value()
        line_length = self.line_length_input.value()
        self.manager.set_axiom(axiom)
        self.manager.set_theorems(theorems)
        self.manager.set_rotate_angle(rotate_angle)
        self.manager.set_line_length(line_length)
        self.manager.update_generator_configuration()
        self.close()


class TheoremsListWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.theorems_layout = QVBoxLayout()
        self.setLayout(self.theorems_layout)

    def add_theorem(self, th_input="", th_output=""):
        theorem_widget = TheoremWidget(self, th_input, th_output)
        self.theorems_layout.addWidget(theorem_widget)

    def get_theorems(self):
        result = []
        for i in range(len(self.theorems_layout)):
            result.append(self.theorems_layout.itemAt(i))
        return result


class TheoremWidget(QWidget, UITheoremWidget):
    def __init__(self, parent, th_input="", th_output=""):
        super().__init__(parent)
        self.initUI()
        self.theorem_input.setText(th_input)
        self.theorem_output.setText(th_output)

    def initUI(self):
        # self.setupUi(self)
        uic.loadUi("design/theorem_widget.ui", self)
        self.delete_theorem_btn.clicked.connect(self.delete)

    def get_theorem(self):
        return self.theorem_input.text(), self.theorem_output.text()

    def delete(self):
        self.setParent(None)


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
        l_string = self[iteration]
        for char in l_string:
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
        return len(l_string)


def excepthook(cls, value, traceback):
    sys.__excepthook__(cls, value, traceback)


if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = FractalGeneratorWindow()
    ex.show()
    sys.exit(app.exec())
