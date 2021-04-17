from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class IError(QDialog):
    def __init__(self, error):
        super().__init__()
        loadUi('UI\error.ui', self)
        self.BTN_Ok.clicked.connect(self.accept)
        self.LINE_Error.setText(error)
        self.exec_()
