from datetime import datetime
import webbrowser

from PyQt6 import QtCore
from loguru import logger

import widgets_templates as wt
import base_widgets as bw
import config
import clock


class CurrentTimeLabel(wt.AbstractTimeLabel):

    """shows current time"""

    def __init__(self, clock: clock.CuckooClock):
        wt.AbstractTimeLabel.__init__(self, clock)

        self.layout_ = wt.VLayout(self, 2)
        self.date = wt.TimeStampString()
        self.time = wt.TimeStampString()
        self.layout_.addWidget(self.date)
        self.layout_.addWidget(self.time)
        self.setSizePolicy(bw.SizePolicies.expanding)
        self.layout_.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def update(self):
        date, time = datetime.now().strftime(config.TODAY_FORMAT).split("\n")
        self.date.setText(date[:-1])
        self.time.setText(time)


class CurrentTimeWindow(wt.TimeWindow):

    """always-on-screen window showing current time"""

    def __init__(self,
                 settings: config.WindowSettings,
                 clock: clock.CuckooClock):

        logger.debug("created CurrentTimeWindow")
        self.label = CurrentTimeLabel(clock)

        wt.TimeWindow.__init__(self, settings, clock)
        self.setFixedSize(75, 40)
        self.layout_.addWidget(self.label, 0, 0, 1, 1)

    def setStyleSheet(self, styleSheet: str) -> None:
        self.label.setStyleSheet(styleSheet)
        return super().setStyleSheet(styleSheet)


class LinksNotification(wt.RepetitiveNotification):

    """
    Opens choosen links in browser when closing.
    Shows every time when Cuckoo emits iteration signal
    """

    def __init__(self,
                 settings: config.NotificationSettings,
                 clock: clock.CuckooClock,
                 links: tuple[str]):
        self.links = links
        wt.RepetitiveNotification.__init__(self, settings, clock)
        self.button.clicked.connect(lambda e: self.open_links())

    def open_links(self):
        for link in self.links:
            webbrowser.get(config.BROWSER_PATH + " %s").open(link)
