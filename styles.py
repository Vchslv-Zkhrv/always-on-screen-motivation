from dataclasses import dataclass
import os

from PyQt6 import QtGui


"""gui settings module"""


@dataclass
class Style():
    bg_color:str
    fore_color:str
    border:str = "none"
    border_radius:str = "5px"

    def __str__(self):
        return f"background-color:{self.bg_color}; color:{self.fore_color}, border:{self.border}; border-radius:{self.border_radius};"
    


class Font(QtGui.QFont):

    """Custom font"""
    
    def __init__(self, filename:str, size:int):
        id_ = QtGui.QFontDatabase.addApplicationFont(f"{os.getcwd()}\\fonts\\{filename}")
        families = QtGui.QFontDatabase.applicationFontFamilies(id_)
        QtGui.QFont.__init__(self, families[0])
        self.setPixelSize(size)


@dataclass
class Fonts():
    lucon = lambda size: Font("lucon.ttf", size)
    raleway = lambda size: Font("raleway.ttf", size)