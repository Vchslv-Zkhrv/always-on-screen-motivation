import os
import sys
from dataclasses import dataclass, fields
from typing import Literal

import screeninfo
from PyQt6 import QtGui, QtWidgets, QtCore

from loguru import logger



PATH = os.getcwd() 
TODAY_FORMAT = "%m.%d %a\n%H:%M:%S"
SCREEN = (screeninfo.get_monitors()[0].width, screeninfo.get_monitors()[0].height)


weekday_ = Literal["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]





class SizePolicy(QtWidgets.QSizePolicy):
    
    def __init__(self, horizontal:QtWidgets.QSizePolicy.Policy, vertical:QtWidgets.QSizePolicy.Policy):
        QtWidgets.QSizePolicy.__init__(self, horizontal, vertical)
        self.setHorizontalStretch(0)
        self.setVerticalStretch(0)






class MonospaceFont(QtGui.QFont):

    """Обычный шрифт"""

    def __init__(self, size:int):
        id_ = QtGui.QFontDatabase.addApplicationFont(f"{PATH}\\fonts\\lucon.ttf")
        families = QtGui.QFontDatabase.applicationFontFamilies(id_)
        QtGui.QFont.__init__(self, families[0], size)



@dataclass
class SizePolicies():
    expanding = SizePolicy(
        QtWidgets.QSizePolicy.Policy.Expanding,
        QtWidgets.QSizePolicy.Policy.Expanding)
    fixed = SizePolicy(
        QtWidgets.QSizePolicy.Policy.Fixed,
        QtWidgets.QSizePolicy.Policy.Fixed)
    shrinking = SizePolicy(
        QtWidgets.QSizePolicy.Policy.Minimum,
        QtWidgets.QSizePolicy.Policy.Minimum)
    row = SizePolicy(
        QtWidgets.QSizePolicy.Policy.Expanding,
        QtWidgets.QSizePolicy.Policy.Minimum)
    column = SizePolicy(
        QtWidgets.QSizePolicy.Policy.Minimum,
        QtWidgets.QSizePolicy.Policy.Expanding)



@dataclass
class Style():
    bg_color:str
    fore_color:str
    border:str = "none"
    border_radius:str = "5px"

    def __str__(self):
        return f"background-color:{self.bg_color}; color:{self.fore_color}, border:{self.border}; border-radius:{self.border_radius};"
    


place_ = tuple[int, int]
size_ = int | None
style_ = Style | str



@dataclass
class WindowSettings():

    """
    used to adjust window when it created.
    """

    place: place_
    size: tuple[size_, size_] | None
    style: style_





@dataclass
class ApplicationSettings():
    position: tuple[int, int]
    alignment: Literal["column", "row"]
    style: style_
    gap: int = 12
    fps: float = 0.5