from PyQt6 import QtWidgets, QtCore, QtGui

from config import SizePolicies


"""
Quik base widgets creation
"""


class HLayout(QtWidgets.QHBoxLayout):
    
    """QHBoxLayout with spacing and margins set to 0"""
    
    def __init__(self, parent, spacing=0, padding=0):
        QtWidgets.QHBoxLayout.__init__(self, parent)
        self.setContentsMargins(padding, padding, padding, padding)
        self.setSpacing(spacing)



class VLayout(QtWidgets.QVBoxLayout):
    
    """QVBoxLayout with spacing and margins set to 0"""
    
    def __init__(self, parent, spacing=0, padding=0):
        QtWidgets.QVBoxLayout.__init__(self, parent)
        self.setContentsMargins(padding, padding, padding, padding)
        self.setSpacing(spacing)



class GLayout(QtWidgets.QGridLayout):
    
    """QGridLayout with spacing and margins set to 0"""
    
    def __init__(self, parent, spacing=0, padding=0):
        QtWidgets.QGridLayout.__init__(self, parent)
        self.setContentsMargins(padding, padding, padding, padding)
        self.setSpacing(spacing)






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

    """places wrapped widget to the center"""

    def __init__(self, widget:QtWidgets.QWidget):
        self.widget = widget
        GFrame.__init__(self)
        self.layout_.addItem(VSpacer(), 1,0,1,1)
        self.layout_.addItem(VSpacer(), 1,2,1,1)
        self.layout_.addItem(HSpacer(), 0,1,1,1)
        self.layout_.addItem(HSpacer(), 0,2,1,1)
        self.layout_.addWidget(widget, 1,1,1,1)


class WrapperTop(VFrame):

    """places wrapped widget to the top"""

    def __init__(self, widget:QtWidgets.QWidget):
        self.widget = widget
        VFrame.__init__(self)
        self.layout_.addWidget(widget)
        self.layout_.addItem(VSpacer())


        
class WrapperBottom(VFrame):

    """places wrapped widget to the bottom"""

    def __init__(self, widget:QtWidgets.QWidget):
        self.widget = widget
        VFrame.__init__(self)
        self.layout_.addItem(VSpacer())
        self.layout_.addWidget(widget)


        
class WrapperLeft(HFrame):

    """places wrapped widget to the Left"""

    def __init__(self, widget:QtWidgets.QWidget):
        self.widget = widget
        HFrame.__init__(self)
        self.layout_.addWidget(widget)
        self.layout_.addItem(HSpacer())


        
class WrapperRight(HFrame):

    """places wrapped widget to the right"""

    def __init__(self, widget:QtWidgets.QWidget):
        self.widget = widget
        HFrame.__init__(self)
        self.layout_.addItem(HSpacer())
        self.layout_.addWidget(widget)

        