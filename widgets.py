from datetime import datetime

from PyQt6 import QtWidgets, QtCore, QtGui

from widgets_templates import *
from config import *



class CurrentTimeLabel(AbstractTimeLabel):

    """shows current time"""

    def __init__(self, clock:CuckooClock):
        AbstractTimeLabel.__init__(self, clock)
        self.layout_ = VLayout(self, 2)
        self.date = TimeStampString()
        self.time = TimeStampString()
        self.layout_.addWidget(self.date)
        self.layout_.addWidget(self.time)
        self.setSizePolicy(SizePolicies.expanding)
        self.layout_.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        print(self.date.styleSheet())

    def update(self):
        date, time = datetime.now().strftime(TODAY_FORMAT).split("\n")
        self.date.setText(date[:-1])
        self.time.setText(time)





class CurrentTimeWindow(TimeWindow):

    """always-on-screen window showing current time"""

    def __init__(self, settings:WindowSettings, clock:CuckooClock):
        logger.debug("created CurrentTimeWindow")
        self.label = CurrentTimeLabel(clock)
        TimeWindow.__init__(self, settings, clock)
        self.setFixedSize(75,40)
        self.layout_.addWidget(self.label,0,0,1,1)
        print(self.pos().x(), self.pos().y())

    def setStyleSheet(self, styleSheet: str) -> None:
        self.label.setStyleSheet(styleSheet)
        return super().setStyleSheet(styleSheet)