import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QTableWidgetItem


class DBSample(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.select_data)
        self.textEdit.setPlainText("SELECT * FROM coffee")
        self.select_data()

    def select_data(self):
        query = self.textEdit.toPlainText()

        cur = self.connection.cursor()

        res = cur.execute(query).fetchall()
        desc = list(map(lambda x: x[0], cur.description))

        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        for i, v in enumerate(desc):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(str(v)))
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()