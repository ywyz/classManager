from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import FluentWindow, NavigationItemPosition, SubtitleLabel, setFont
from LoginUI_ui import Ui_Login_UI
from StuAddSingle_ui import Ui_StuAddSingle
from stuAttend_ui import Ui_StuDailyAttend
from stuhealthy_ui import Ui_StuHealthy
from stuChange_ui import Ui_StuChange
from ThingsAddSingle_ui import Ui_ThingsAddSingle
from Thingsquery_ui import Ui_ThingsQuery
from dataManager_ui import Ui_dataManager


class dataManagerinterface(QWidget, Ui_dataManager):
    def __init__(self, parent=None):
        self.widget = QWidget(parent)
        self.setupUi(self.widget)

class ThingsQueryinterface(QWidget, Ui_ThingsQuery):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class ThingsAddSingleinterface(QWidget, Ui_ThingsAddSingle):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class StuChangeinterface(QWidget, Ui_StuChange):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class StuHealthyinterface(QWidget, Ui_StuHealthy):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class StuDailyAttendinterface(QWidget, Ui_StuDailyAttend):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class StuAddSingleinterface(QWidget, Ui_StuAddSingle):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)