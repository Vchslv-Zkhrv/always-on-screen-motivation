from abc import abstractmethod

from PyQt6 import QtWidgets, QtCore
from loguru import logger

import config
import clock
import styles
import base_widgets as bw


"""PyQt6 widgets with extended functionality"""


class Window(QtWidgets.QMainWindow):

    """Parses & applies WindowSettings to itself"""

    def __init__(self, settings: config.WindowSettings):
        QtWidgets.QMainWindow.__init__(self)

        logger.debug("Created window")
        style = settings.styles
        self.setStyleSheet(str(style))

        if settings.place:
            self.move(*settings.place)

        if settings.size:
            w, h = settings.size
            if isinstance(w, int):
                self.setFixedWidth(w)
            if isinstance(h, int):
                self.setFixedWidth(h)


class AlwaysOnSrcreenWindow(Window):

    """
    Always-on-screen window with QGridLayout.
    Cannot be closed or moved by user because there is no window frame.
    Use .layout_ to place widgets.
    All the margins and spacings set to 0.
    """

    def __init__(self, settings: config.WindowSettings):

        self.cw = QtWidgets.QWidget()
        Window.__init__(self, settings)

        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint |
            QtCore.Qt.WindowType.Tool)

        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setCentralWidget(self.cw)
        self.setContentsMargins(0, 0, 0, 0)
        self.cw.setContentsMargins(0, 0, 0, 0)
        self.layout_ = bw.GLayout(self.cw)

    def setStyleSheet(self, styleSheet: str) -> None:
        self.cw.setStyleSheet(styleSheet)
        return super().setStyleSheet(styleSheet)


class TimeWindow(AlwaysOnSrcreenWindow):

    """always-on-screen window showing time"""

    def __init__(self,
                 settings: config.WindowSettings,
                 clock: clock.CuckooClock):
        AlwaysOnSrcreenWindow.__init__(self, settings)
        self.clock = clock


class AbstractTimeLabel(QtWidgets.QPushButton):

    """
    Label reacting on CuckooClock tick signals by it's update method
    """

    def __init__(self, clock: clock.CuckooClock):
        QtWidgets.QPushButton.__init__(self)
        self.setFont(styles.Fonts.lucon(config.FONTSIZE))
        clock.signals.tick.connect(self.update)

    @abstractmethod
    def update(self): ...


class TimeStampString(QtWidgets.QLabel):

    """one string in composite label"""

    def __init__(self):
        QtWidgets.QLabel.__init__(self)
        self.setFont(styles.Fonts.lucon(config.FONTSIZE))
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setSizePolicy(bw.SizePolicies.fixed)


class WindowTitle(QtWidgets.QLabel):

    """label in the top of Window"""

    def __init__(self, text: str):
        QtWidgets.QLabel.__init__(self)
        self.setText(text)


class FullscreenTranslucent(AlwaysOnSrcreenWindow):

    """
    Translucent fullscreen window showed above all other windows.
    Can be closed by mouse click
    """

    def __init__(
            self,
            settings: config.NotificationSettings):

        s = config.WindowSettings(
            (0, 0),
            config.SCREEN,
            f"background-color:{settings.back_color}")

        AlwaysOnSrcreenWindow.__init__(self, s)

        opacity = QtWidgets.QGraphicsOpacityEffect()
        opacity.setOpacity(settings.opacity)
        self.setGraphicsEffect(opacity)

        self.cw.setGraphicsEffect(opacity)
        self.button = QtWidgets.QPushButton()
        self.button.setFont(styles.Fonts.raleway(24))
        self.button.setSizePolicy(bw.SizePolicies.expanding)
        self.button.setStyleSheet(f"color: {settings.fore_color}")
        self.button.setText(settings.text)
        self.layout_.addWidget(self.button)
        self.button.clicked.connect(lambda e: self.hide())
        self.show = self.showFullScreen


class RepetitiveNotification(FullscreenTranslucent):

    """
    Fullscreen (very annoying, but effective) notification to do smth.
    Shows itself at the Cuckoo iteration signal, hides by mouse click
    """

    def __init__(self,
                 settings: config.NotificationSettings,
                 clock: clock.CuckooClock):
        FullscreenTranslucent.__init__(self, settings)
        self.cuckoo = clock.get_cuckoo(settings.period)
        self.cuckoo.signals.iteration.connect(self.show)
