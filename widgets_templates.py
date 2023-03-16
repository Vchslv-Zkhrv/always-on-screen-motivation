from PyQt6 import QtWidgets, QtGui, QtCore
from abc import abstractmethod

from config import SizePolicies, WindowSettings
from clock import CuckooClock
from base_widgets import *




class Window(QtWidgets.QMainWindow):

    """Parses & applies WindowSettings to itself"""

    def __init__(self, settings:WindowSettings):
        QtWidgets.QMainWindow.__init__(self)
        self.setStyleSheet(settings.style)
        if settings.place:
            self.move(settings.place)
        if settings.size:
            w, h = settings.size
            if isinstance(w, int): self.setFixedWidth(w)
            if isinstance(h, int): self.setFixedWidth(h)
        


class AlwaysOnSrcreenWindow(Window):

    """
    Always-on-screen window with QGridLayout.
    Cannot be closed or moved by user because there is no window frame.
    Use .layout_ to place widgets. 
    All the margins and spacings set to 0.
    """

    def __init__(self, settings:WindowSettings):

        Window.__init__(self, settings)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |  QtCore.Qt.WindowStaysOnTopHint)  
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.cw = QtWidgets.QWidget()
        self.setCentralWidget(self.cw)
        self.setContentsMargins(0,0,0,0)
        self.cw.setContentsMargins(0,0,0,0)
        self.layout_ = GLayout(self.cw)



class AbstractTimeLabel(QtWidgets.QLabel):

    """
    Label that should be appended to CuckooClock.actions via it's update() method
    
    """

    def __init__(self, clock:CuckooClock):
        QtWidgets.QLabel.__init__(self)
        clock.add_action(self.update)

    @abstractmethod
    def update(self): ...