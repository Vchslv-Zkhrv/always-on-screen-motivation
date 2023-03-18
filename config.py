import os
import sys
from dataclasses import dataclass
from typing import Literal

from loguru import logger
import screeninfo
from PyQt6 import QtGui, QtWidgets, QtCore

from styles import *


PATH = os.getcwd() 
TODAY_FORMAT = "%m.%d %a\n%H:%M:%S"
SCREEN = (screeninfo.get_monitors()[0].width, screeninfo.get_monitors()[0].height)
FONTSIZE = 12

place_ = tuple[int, int]
size_ = int | None
style_ = Style | str
seconds_ = float


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