import os
from dataclasses import dataclass
from typing import Literal

import screeninfo

from . import styles


PATH = os.getcwd()
TODAY_FORMAT = "%m.%d %a\n%H:%M:%S"
SCREEN = (
    screeninfo.get_monitors()[0].width,
    screeninfo.get_monitors()[0].height)
FONTSIZE = 12
BROWSER_PATH = r"\"C:\Program Files\Google\Chrome\Application\chrome.exe\""

place_ = tuple[int, int]
size_ = int | None
style_ = styles.Style | str
seconds_ = float


class Percent(float):
    def __init__(self, x: float) -> None:
        if x < 0 or x > 1:
            raise ValueError("percent value must be between 0 and 1")
        super().__init__()


@dataclass
class WindowSettings():
    """
    used to adjust window when it created.
    """
    place: place_
    size: tuple[size_, size_] | None
    styles: styles.Personalization


@dataclass
class ApplicationSettings():

    """user-specified settings"""

    styles: styles.Personalization
    position: tuple[int, int]
    alignment: Literal["column", "row"]
    gap: int = 12
    fps: float = 0.5


@dataclass
class NotificationSettings():

    """special settings for each fullscreen notification"""

    text: str
    period: seconds_
    opacity: Percent = 0.5
    fore_color: str = "white"
    back_color: str = "black"
    ttl: seconds_ = None
