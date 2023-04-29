import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from sys import exit

from PyQt6.QtWidgets import QWidget
from db import Database

class MainWindow (QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.db = Database()

        self.grid = QGridLayout()
        self.render_all()
        self.setLayout(self.grid)
    
    def render_all(self):
        data = self.db.get__all_tasks()

        c = [(x, 0, 1, 2) for x in range(len(data))]

        for row, c in zip(data, c):
            task = QLabel(str(row[0]) + ". " + str(row[1]))

            if row[3] == 0:
                task.setStyleSheet("font-weight: 700;")
            else:
                task.setStyleSheet("color: #333; font-size: 10px")

            self.grid.addWidget(task, c[0], c[1])
            chesk = QCheckBox()           
            self.grid.addWidget(chesk, c[0], c[2])
