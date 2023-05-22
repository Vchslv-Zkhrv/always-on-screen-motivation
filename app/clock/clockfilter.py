from PyQt6.QtWidgets import QWidget

from . import signals
from .clock import Clock


class ClockFilter(QWidget):

    """
    Emits specific signals with a frequency
    different from (and lower than) Clock.
    """

    def __init__(
            self,
            clock: Clock,
            period: float):

        QWidget.__init__(self)
        self.period = period
        self.clock = clock
        self.step = clock.period
        self.signals = signals.CuckooSignals()
        self.clock.signals.tick.connect(self.on_clock_tick)
        self.expired_time = 0

    def on_clock_tick(self):
        self.expired_time += self.step
        if self.expired_time >= self.period:
            self.expired_time = 0
            self.signals.iteration.emit()
