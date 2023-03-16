from PyQt6 import QtWidgets, QtCore, QtGui

from widgets_templates import *
from config import *




class DatetimeLabel(QtWidgets.QPushButton):

    """Label showing time in DatetimeWindow"""

    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setStyleSheet("border: none; color: black; background-color: white; border-radius: 5px")
        self.setFont(MonospaceFont(8))
        self.setSizePolicy(SizePolicies.expanding)
    



