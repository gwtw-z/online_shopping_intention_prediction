# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QWidget, QTableWidget,
                               QTableWidgetItem, QVBoxLayout)

colors = [("Red", "#FF0000"),
          ("Green", "#00FF00"),
          ("Blue", "#0000FF"),
          ("Black", "#000000"),
          ("White", "#FFFFFF"),
          ("Electric Green", "#41CD52"),
          ("Dark Blue", "#222840"),
          ("Yellow", "#F9E56d")]


def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i + 2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])


class TableData(QWidget):
    def __init__(self, data, parent=None):
        super(TableData, self).__init__(parent)
        self.setWindowTitle("My TableData")

        self.table = QTableWidget()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['序号', '预测概率', '预测结果'])

        for i in range(len(data[0])):
            item_serial_number = QTableWidgetItem(data[0][i])
            item_prob = QTableWidgetItem(data[1][i][1])
            item_out = QTableWidgetItem(data[2][i])
            self.table.setItem(data[0][i], 0, item_serial_number)
            self.table.setItem(data[0][i], 1, item_prob)
            self.table.setItem(data[0][i], 2, item_out)

        layout = QVBoxLayout(self)
        layout.addWidget(self.table)


def show_analysis(data):
    # app = QApplication()
    window = TableData(data)
    window.show()
    window.exec()
    # app.exec()
