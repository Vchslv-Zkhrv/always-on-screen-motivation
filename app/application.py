import sys
from PyQt6 import QtWidgets

from . import clock


class Applcation(QtWidgets.QApplication):

    global_clock: clock.CuckooClock

    def __init__(self):
        QtWidgets.QApplication.__init__(self, sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.global_clock = clock.CuckooClock()
        self.global_clock.signals.tick.connect(self._on_tick)

    def run(self) -> int:
        self.window.show()
        self.global_clock.run_fixed_times(10)
        return self.exec()

    def _on_tick(self):
        print("tick")
