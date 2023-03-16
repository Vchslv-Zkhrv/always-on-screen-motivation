import asyncio
import sys
import os
from datetime import datetime
from dataclasses import dataclass, fields
from typing import Literal, TypedDict

import screeninfo
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtWidgets import QSizePolicy

from widgets_templates import *




PATH = os.getcwd() 
TODAY_FORMAT = "%m.%d\n%H:%M\n %a"
SCREEN = (screeninfo.get_monitors()[0].width, screeninfo.get_monitors()[0].height)


weekday_ = Literal["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]





class SizePolicy(QtWidgets.QSizePolicy):
    
    def __init__(self, horizontal:QSizePolicy.Policy, vertical:QSizePolicy.Policy):
        QtWidgets.QSizePolicy.__init__(self, horizontal, vertical)
        self.setHorizontalStretch(0)
        self.setVerticalStretch(0)






class MonospaceFont(QtGui.QFont):

    """Обычный шрифт"""

    def __init__(self, size:int):
        id_ = QtGui.QFontDatabase.addApplicationFont(f"{PATH}\\fonts\\lucon.ttf")
        families = QtGui.QFontDatabase.applicationFontFamilies(id_)
        QtGui.QFont.__init__(self, families[0], size)
        # self.setWeight(60)



@dataclass
class SizePolicies():
    expanding = SizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    fixed = SizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    shrinking = SizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    row = SizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
    column = SizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)



@dataclass
class TimeStamp():

    """
    Datetime values: month, day, hour, minute, short weekday name.
    Call __str__ to get CSS
    Call __iter__ to get values in that order
    """

    month: int
    day: int
    hour: int
    minute: int
    weekday: weekday_

    def __iter__(self):
        return iter((self.month, self.day, self.hour, self.minute, self.weekday))



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

