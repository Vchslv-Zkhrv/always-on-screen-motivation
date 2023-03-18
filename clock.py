import threading
import time
from datetime import datetime
from config import *



class CountDown():

    """call like a function to find out if the countdown has expired or not"""

    def __init__(self, finish:int):
        self.finish = finish

    def __call__(self) -> bool:
        self.finish -= 1
        return self.finish != -1





class ClockSignals(QtCore.QObject):

    """
    Clock widget signals:
    tick: on every iteration
    start: before enter the loop
    stop: on thread exit 
    """
    start = QtCore.pyqtSignal()
    tick = QtCore.pyqtSignal()
    stop = QtCore.pyqtSignal()


class CuckooSignals(QtCore.QObject):
    iteration = QtCore.pyqtSignal()




class Cuckoo(QtWidgets.QWidget):

    """
    Emits specific signals with a frequency different from (and lower than) CuckooClock.
    Can be used to manage rare periodic actions.
    """

    def __init__(self, clock, period:float):
        QtWidgets.QWidget.__init__(self)
        self.period = period
        self.step = clock.delay
        self.signals = CuckooSignals()
        self.clock = clock
        self.clock.signals.tick.connect(self.on_clock_tick)
        self.expired_time = 0

    def on_clock_tick(self):
        self.expired_time += self.step
        if self.expired_time >= self.period:
            logger.debug("cuckoo iteration")
            self.expired_time = 0
            self.signals.iteration.emit()




class CuckooClock(QtWidgets.QWidget):

    """
    Emits tick signals every <delay> seconds.
    Be aware that delays will not be very accurate.
    """

    def __init__(self, delay:float=0.5):
        QtWidgets.QWidget.__init__(self)
        self.signals = ClockSignals()
        self.cuckoos:dict[str, Cuckoo] = {}
        self.delay = delay

    def get_cuckoo(self, period:float) -> Cuckoo:
        """
        Creates Cuckoo object that emits iteration signals in specified frequency.
        Period must be greater than the clock delay (and preferably a multiple of it)
        If Cuckoo with same period already exists, returnes it.
        """
        if str(period) not in self.cuckoos:
            self.cuckoos[str(period)] = Cuckoo(self, period)
        return self.cuckoos[str(period)]
    
    def del_cuckoo(self, cuckoo:Cuckoo|float):
        """
        Turns off and deletes a Cuckoo.
        Cuckoo can be specified directly or via it's period
        """
        
        match cuckoo:
            case isinstance(cuckoo, Cuckoo):
                key = str(cuckoo.period)
            case float:
                key = str(cuckoo)
                
        self.cuckoos[key].destroy()
        self.cuckoos[key] = None


    def loop(self, exit_condition:callable):
        """
        Calls condition() without arguments at every iteration.
        Runs untill gets True, then exits thread and emits stop signal
        """
        self.signals.start.emit()
        logger.debug("clock started")
        while exit_condition():
            time.sleep(self.delay)
            self.signals.tick.emit()
        self.signals.stop.emit()
        logger.debug("clock stopped")
        sys.exit()
            
    def run_by_condition(self, condition):
        """launches loop"""
        loop = threading.Thread(target=self.loop, args=(condition, ), daemon=False)
        loop.start()

    def run_forever(self):
        self.run_by_condition(lambda: True)

    def run_fixed_time(self, seconds:float):
        finish = time.time() + seconds
        self.run_by_condition(lambda: time.time() <= finish)

    def run_fixed_times(self, count:int):
        counter = CountDown(count)
        self.run_by_condition(counter)

    def run_until_time(self, epoch:float):
        self.run_by_condition(lambda: time.time() <= epoch)







if __name__ == "__main__":


    def show_date():
        print(datetime.now().strftime(TODAY_FORMAT))

    def show_time():
        print(datetime.now().strftime("%S.%f"), end="\n\n")

    clock = CuckooClock(1, (show_date, show_time))
    clock.run_fixed_times(10)