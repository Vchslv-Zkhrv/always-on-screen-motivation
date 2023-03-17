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
        

class CuckooClock():

    """
    Emits signals every <delay> seconds.
    Be aware that delays will not be very accurate.
    """

    def __init__(self, delay:float, actions:list[callable]):
        self.delay = delay
        self.actions = actions

    def add_action(self, action:callable):
        self.actions.append(action)

    def del_action(self, action:callable):
        self.actions.remove(action)

    def do(self):
        for act in self.actions: act()

    def loop(self, exit_condition:callable):
        while exit_condition():
            logger.info("loop iteration")
            time.sleep(self.delay)
            self.do()
        logger.debug("loop ended") 
            
    def run_by_condition(self, condition):
        """
        Calls condition() without arguments at every iteration.
        Runs untill gets True
        """
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