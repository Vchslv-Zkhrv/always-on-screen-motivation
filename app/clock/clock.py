import sys
import time
import threading

from PyQt6 import QtWidgets

from . import signals


class CountDown():
    """
    call like a function to find out if the countdown has expired or not
    """
    def __init__(self, finish: int):
        self.finish = finish

    def __call__(self) -> bool:
        self.finish -= 1
        return self.finish != -1


class Clock(QtWidgets.QWidget):

    """
    Emits tick signals every <period> seconds.
    Be aware that periods will not be very accurate.
    """

    period: float

    def __init__(
            self,
            period: float = 0.5):

        QtWidgets.QWidget.__init__(self)
        self.signals = signals.ClockSignals()
        self.period = period

    def loop(self, exit_condition: callable):
        """
        Calls condition() without arguments at every iteration.
        Runs untill gets True, then exits thread and emits stop signal
        """
        self.signals.start.emit()
        while exit_condition():
            time.sleep(self.period)
            self.signals.tick.emit()
        self.signals.stop.emit()
        sys.exit()

    def run_by_condition(self, condition):
        """launches loop"""
        loop = threading.Thread(
            target=self.loop,
            args=(condition, ),
            daemon=False)
        loop.start()

    def run_forever(self):
        self.run_by_condition(lambda: True)

    def run_fixed_time(self, seconds: float):
        finish = time.time() + seconds
        self.run_by_condition(lambda: time.time() <= finish)

    def run_fixed_times(self, count: int):
        counter = CountDown(count)
        self.run_by_condition(counter)

    def run_until_time(self, epoch: float):
        self.run_by_condition(lambda: time.time() <= epoch)
