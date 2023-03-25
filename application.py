import sys

from PyQt6 import QtWidgets
from loguru import logger

import widgets_templates as wt
import widgets
import config
import clock


class Main(QtWidgets.QApplication):

    """launches application and connect all the windows to the clock"""

    def __init__(self, settings: config.ApplicationSettings):

        QtWidgets.QApplication.__init__(self, sys.argv)
        self.clock = clock.CuckooClock(0.5)
        self.clock.signals.stop.connect(sys.exit)
        self.windows: list[wt.Window] = []
        self.notifications: list[wt.RepetitiveNotification] = []
        self.settings = settings

    def _get_window_position(self) -> tuple[int, int]:

        """ return position for new window"""

        x, y = self.settings.position

        if self.settings.alignment == "column":
            dx = 0
            dy = sum((w.height()+self.settings.gap for w in self.windows))
        else:
            dx = sum((w.width()+self.settings.gap for w in self.windows))
            dy = 0
        return x+dx, y+dy

    def add_window(self, window: type[widgets.TimeWindow]):
        """
        makes & sets personal WindowSettings to each window
        based ApplicationSettings. Connects windows to main CuckooClock
        """
        place = self._get_window_position()
        settings = config.WindowSettings(place, None, self.settings.styles)
        w = window(settings, self.clock)
        self.windows.append(w)

    def add_notification(self,
                         note: type[wt.RepetitiveNotification],
                         settings: config.NotificationSettings,
                         *args,
                         **kwargs):
        """Creates notification and connects it to main CuckooClock"""
        n = note(settings, self.clock, *args, **kwargs)
        self.notifications.append(n)

    def start(self):
        logger.info(str(self.windows))
        for w in self.windows:
            w.show()
        self.clock.run_forever()
        logger.debug("all ready to start")
        self.exec()


if __name__ == "__main__":
    w, h = config.SCREEN

    settings = config.ApplicationSettings(
        (w-900, h-300),
        "row",
        "background-color: white; color:rgb(20,20,20); border-radius:5px")

    app = Main(settings, widgets.CurrentTimeWindow)
