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


class dataManagerinterface(Ui_dataManager):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = QWidget(parent)
        self.setupUi(self.widget)
        self.widget.resize(1400, 900)


class ThingsQueryinterface(Ui_ThingsQuery):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = QWidget(parent)
        self.setupUi(self.widget)
        self.widget.resize(1400, 900)


class ThingsAddSingleinterface(Ui_ThingsAddSingle):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = QWidget(parent)
        self.setupUi(self.widget)
        self.widget.resize(1400, 900)


class StuChangeinterface(Ui_StuChange):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = QWidget(parent)
        self.setupUi(self.widget)
        self.widget.resize(1400, 900)


class StuHealthyinterface(Ui_StuHealthy):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = QWidget(parent)
        self.setupUi(self.widget)
        self.widget.resize(1400, 900)


class StuDailyAttendinterface(Ui_StuDailyAttend):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = QWidget(parent)
        self.setupUi(self.widget)
        self.widget.resize(1400, 900)


class StuAddSingleinterface( Ui_StuAddSingle):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = QWidget(parent)
        self.setupUi(self.widget)
        self.widget.resize(1400, 900)
