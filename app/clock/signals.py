from PyQt6 import QtCore


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
    """
    iteration is a signal emiting by Cuckoo every <period> seconds
    """
    iteration = QtCore.pyqtSignal()
