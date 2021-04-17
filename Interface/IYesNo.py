from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class IYesNo(QDialog):
    def __init__(self, function):
        super().__init__()
        loadUi('UI\yes_no.ui', self)
        self.BTN_No.clicked.connect(self.reject)
        self.BTN_Yes.clicked.connect(self.accept)
        self.BTN_Yes.clicked.connect(function)
        self.exec_()
