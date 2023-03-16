from PyQt6 import QtWidgets, QtCore, QtGui

from config import SizePolicies


"""
Quik base widgets creation
"""


class HLayout(QtWidgets.QHBoxLayout):
    
    """QHBoxLayout with spacing and margins set to 0"""
    
    def __init__(self, parent):
        QtWidgets.QHBoxLayout.__init__(self, parent)
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)



class VLayout(QtWidgets.QVBoxLayout):
    
    """QVBoxLayout with spacing and marginsc set to 0"""
    
    def __init__(self, parent):
        QtWidgets.QHBoxLayout.__init__(self, parent)
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)



class GLayout(QtWidgets.QGridLayout):

    """QGridLayout with spacing and margins set to 0"""

    def __init__(self, parent):
        QtWidgets.QGridLayout.__init__(self, parent)
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)




class VSpacer(QtWidgets.QSpacerItem):

    """vertical spacer item"""

    def __init__(self, height:int=0):
        QtWidgets.QSpacerItem.__init__(self, 0,height, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)



class HSpacer(QtWidgets.QSpacerItem):

    """horizontal spacer item"""

    def __init__(self, width:int=0):
        QtWidgets.QSpacerItem.__init__(self, width,0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)



class HSpacerWidget(QtWidgets.QFrame):

    """widget-based horizantal spacer"""

    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setSizePolicy(SizePolicies.row)


class VSpacerWidget(QtWidgets.QFrame):

    """widget-based vertical spacer"""

    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setSizePolicy(SizePolicies.column)


class SpacerWidget(QtWidgets.QFrame):

    """widget-based all-direction spacer"""

    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setSizePolicy(SizePolicies.expanding)







class VFrame(QtWidgets.QFrame):

    """
    Frame with VLayout and column-like size policy. 
    All the spacing and margins are set to 0
    """

    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setSizePolicy(SizePolicies.column)
        self.layout_ = VLayout(self)



class HFrame(QtWidgets.QFrame):

    """
    Frame with VLayout and row-like size policy. 
    All the spacing and margins are set to 0
    """

    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setSizePolicy(SizePolicies.row)
        self.layout_ = HLayout(self)



class GFrame(QtWidgets.QFrame):

    """
    Frame with VLayout and expanding size policy in default. 
    All the spacing and margins are set to 0
    """

    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setSizePolicy(SizePolicies.expanding)
        self.layout_ = GLayout(self)



class WrapperCenter(GFrame):

    """places child widget to the center"""

    def __init__(self, widget:QtWidgets.QWidget):
        GFrame.__init__(self)
        self.widget = widget
        self.layout_.addItem(VSpacer(), 1,0,1,1)
        self.layout_.addItem(VSpacer(), 1,2,1,1)
        self.layout_.addItem(HSpacer(), 0,1,1,1)
        self.layout_.addItem(HSpacer(), 0,2,1,1)
        self.layout_.addWidget(widget, 1,1,1,1)

