import sys

from widgets_templates import *
from widgets import *
from config import *




class Main(QtWidgets.QApplication):

    """launches application and connect all the windows to the clock"""

    def __init__(self, settings:ApplicationSettings, *windows:type[TimeWindow]):

        QtWidgets.QApplication.__init__(self, sys.argv)
        self.clock = CuckooClock(0.5)
        self.clock.signals.stop.connect(sys.exit)
        self.windows_types = windows
        self.windows:list[TimeWindow] = []
        self.settings = settings

        self._create_windows()
        logger.debug("windows created")
        self.start()

    def five_seconds(self):
        logger.debug("5-sec iteration")        

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

    def _create_windows(self):
        
        """
        makes & sets personal WindowSettings to each window
        based ApplicationSettings.
        Created windows are in Main.windows
        """

        for i, window in enumerate(self.windows_types):
            place = self._get_window_position()
            settings = WindowSettings(place, None, self.settings.style)
            w = window(settings, self.clock)
            self.windows.append(w)



    def start(self):
        logger.info(str(self.windows))
        for w in self.windows:
            w.show()
        logger.debug("windows showed")
        c = self.clock.get_cuckoo(5)
        c.signals.iteration.connect(self.five_seconds)
        self.clock.run_fixed_time(20)
        self.exec()

        


        




if __name__ == "__main__":
    
    w, h = SCREEN



    settings = ApplicationSettings((w-900,h-300), "row", "background-color:white; color:rgb(20,20,20); border-radius:5px")
    app = Main(settings, CurrentTimeWindow)