from PyQt6 import QtWidgets, QtGui, QtCore
from abc import abstractmethod

from config import *
from clock import CuckooClock
from base_widgets import *


"""PyQt6 widgets with extended functionality"""



class Window(QtWidgets.QMainWindow):

    """Parses & applies WindowSettings to itself"""

    def __init__(self, settings:WindowSettings):
        QtWidgets.QMainWindow.__init__(self)
        logger.debug("Created window")
        self.setStyleSheet(settings.style)
        if settings.place:
            self.move(*settings.place)
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

        self.cw = QtWidgets.QWidget()
        Window.__init__(self, settings)
        
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint |  QtCore.Qt.WindowType.WindowStaysOnTopHint)  
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setCentralWidget(self.cw)
        self.setContentsMargins(0,0,0,0)
        self.cw.setContentsMargins(0,0,0,0)
        self.layout_ = GLayout(self.cw)

    def setStyleSheet(self, styleSheet: str) -> None:
        self.cw.setStyleSheet(styleSheet)
        return super().setStyleSheet(styleSheet)





class TimeWindow(AlwaysOnSrcreenWindow):

    """always-on-screen window showing time"""

    def __init__(self, settings:WindowSettings, clock:CuckooClock):
        AlwaysOnSrcreenWindow.__init__(self, settings)
        self.clock = clock


class AbstractTimeLabel(QtWidgets.QPushButton):

    """
    Label that should be appended to CuckooClock.actions via it's update() method
    """

    def __init__(self, clock:CuckooClock):
        QtWidgets.QPushButton.__init__(self)
        self.setFont(MonospaceFont(10))
        clock.add_action(self.update)

    @abstractmethod
    def update(self): ...


class TimeStampString(QtWidgets.QLabel):

    """one string in composite label"""

    def __init__(self):
        QtWidgets.QLabel.__init__(self)
        self.setFont(MonospaceFont(9))
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setSizePolicy(SizePolicies.fixed)
        self.setStyleSheet("bacground-color:red")