from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import FluentWindow, NavigationItemPosition, SubtitleLabel, setFont
from LoginUI import Ui_Login_UI
from StuAddSingle import Ui_StuAddSingle
from StuAttend import Ui_StuDailyAttend
from Stuhealthy import Ui_StuHealthy
from StuChange import Ui_StuChange
from ThingsAddSingle import Ui_ThingsAddSingle
from Thingsquery import Ui_ThingsQuery
from DataManager import Ui_dataManager


class dataManagerinterface(QWidget, Ui_dataManager):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class ThingsQueryinterface(QWidget, Ui_ThingsQuery):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class ThingsAddSingleinterface(QWidget, Ui_ThingsAddSingle):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class StuChangeinterface(QWidget, Ui_StuChange):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class StuHealthyinterface(QWidget, Ui_StuHealthy):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class StuDailyAttendinterface(QWidget, Ui_StuDailyAttend):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class StuAddSingleinterface(QWidget, Ui_StuAddSingle):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

