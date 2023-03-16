import sys
from datetime import datetime

from PyQt6 import QtWidgets, QtCore, QtGui

from widgets_templates import *
from widgets import *
from config import *





def get_current_datetime() -> TimeStamp:
    return TimeStamp(*datetime.now().strftime("%m %d %H %M %a").split()) 
    



class Main():

    def __init__(self):
        ...



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AlwaysOnSrcreenWindow()
    window.show()
    app.exec()