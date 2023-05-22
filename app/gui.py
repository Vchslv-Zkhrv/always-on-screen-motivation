import os
from typing import Literal, Any
import json

from PyQt6 import QtGui

from . import config


font_lang = Literal["ru", "en"]
font_kind = Literal[
    "serif",
    "monospace",
    "display",
    "handwriting"
]


class Font(QtGui.QFont):

    def __init__(
            self,
            path: str,
            size: int):

        id_ = QtGui.QFontDatabase.addApplicationFont(path)
        families = QtGui.QFontDatabase.applicationFontFamilies(id_)
        QtGui.QFont.__init__(self, families[0])
        self.setPixelSize(size)


class FontFamily():

    """
    Fonts factory /
    Фабрика шрифтов
    """

    languages: tuple[font_lang]
    kind: font_kind

    def __init__(self, name: str):
        self.path = f"{os.getcwd()}{config.FONTS_PATH}\\{name}"
        self._parse_cheatsheet(name)

    def _parse_cheatsheet(self, name: str) -> None:
        with open(
            f"{os.getcwd()}{config.FONTS_CHEATSHEET_PATH}",
            "r",
            encoding="utf-8"
        ) as file:

            js = json.load(file)[name]
            self.languages = js["languages"]
            self.kind = js["kind"]

    def font(
            self,
            size: int = config.MAIN_FONTSIZE,
            style: str = "Regular",
            **kwargs):

        font = Font(self.path % style, size)

        if "weight" in kwargs:
            font.setWeight(kwargs["weight"])
        if "italic" in kwargs:
            font.setItalic(kwargs["italic"])
        if "bold" in kwargs:
            font.setBold(kwargs["bold"])
        if "underline" in kwargs:
            font.setUnderline(kwargs["underline"])
        if "capitalization" in kwargs:
            font.setCapitalization(kwargs["capitalization"])

        return font
