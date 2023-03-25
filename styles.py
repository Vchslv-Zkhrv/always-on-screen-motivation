from dataclasses import dataclass
from typing import TypedDict
import os

from PyQt6 import QtGui

"""gui settings module"""


class Color():
    r: int
    g: int
    b: int
    a: int = 255

    def __str__(self):
        return f"rgba({self.r},{self.g},{self.b},{self.a})"


@dataclass
class Style():
    fore: Color
    background: Color
    border: str
    radius: int

    def __str__(self):
        return f"""
        color: {self.fore};
        background:{self.background};
        border: {self.border};
        border-radius: {self.radius}px; """


class Theme(TypedDict):
    normal: Style
    contrast: Style
    dimmed: Style
    transparent: Style


class Personalization():

    """
    Manages application appearance
    """

    def __init__(self):
        self.themes = {}

        self.regist_theme(
            "default light",
            Color(255, 255, 255),
            Color(0, 0, 0))

        self.regist_theme(
            "default dark",
            Color(0, 0, 0),
            Color(255, 255, 255))

        self.current_theme = self.themes["default light"]

    def regist_theme(self, name: str, fcolor: Color, bcolor: Color):
        theme = Theme()
        colors = self._generate_colors(fcolor, bcolor)
        theme["contrast"] = Style(*colors["contrast"])
        theme["normal"] = Style(*colors["normal"])
        theme["dimmed"] = Style(*colors["dimmed"])
        theme["transparent"] = Style(*colors["transparent"])
        self.themes[name] = theme

    def _generate_colors(self,
                         fcolor: Color,
                         bcolor: Color) -> dict[str, tuple[Color, Color]]:

        backs = self._generate_backs(bcolor)
        fores = self._generate_fores(fcolor, bcolor)

        colors = {
            "contrast": (backs[0], fores[0]),
            "normal": (backs[1], fores[1]),
            "dimmed": (backs[2], fores[2]),
            "transparent": (backs[3], fores[3])
        }
        return colors

    def _generate_fores(self,
                        fcolor: Color,
                        bcolor: Color) -> tuple[Color, Color, Color, Color]:
        c1, c2, c3, c4 = fcolor, fcolor, bcolor, bcolor
        return c1, c2, c3, c4

    def _generate_backs(self,
                        bcolor: Color) -> tuple[Color, Color, Color, Color]:
        c1, c2, c3, c4 = bcolor, bcolor, bcolor, bcolor
        c2.a = 255
        c2.a = 200
        c3.a = 100
        c4.a = 0
        return c1, c2, c3, c4


@dataclass
class Style():
    bg_color: Color
    fore_color: Color
    border: str = "none"
    border_radius: str = "5px"

    def __str__(self):
        return f"""background-color:{self.bg_color};
        color:{self.fore_color},
        border:{self.border};
        border-radius:{self.border_radius};"""


class Font(QtGui.QFont):

    """Custom font"""

    def __init__(self, filename: str, size: int):
        id_ = QtGui.QFontDatabase.addApplicationFont(
            f"{os.getcwd()}\\fonts\\{filename}")
        families = QtGui.QFontDatabase.applicationFontFamilies(id_)
        QtGui.QFont.__init__(self, families[0])
        self.setPixelSize(size)


def get_font(name):
    return lambda size: Font(name, size)


@dataclass
class Fonts():
    lucon = get_font("lucon.ttf")
    raleway = get_font("raleway.ttf")
