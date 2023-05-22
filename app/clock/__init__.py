from . import signals
from .clock import Clock
from .clockfilter import ClockFilter


class CuckooClock(clock.Clock):
    """
    Emits tick signals every <delay> seconds.
    Be aware that delays will not be very accurate.
    """

    cuckoos: list[ClockFilter]

    def __init__(
            self,
            period: float = 0.5):

        clock.Clock.__init__(self, period)
        self.cuckoos = []

    def add_cuckoo(self, period: float) -> ClockFilter:
        cuckoo = ClockFilter(self, period)
        return cuckoo

    def del_cuckoo(self, cuckoo: ClockFilter):
        """
        Turns off and deletes a Cuckoo.
        Cuckoo can be specified directly or via it's period
        """
        cuckoo.destroy()
        self.cuckoos.remove(cuckoo)
