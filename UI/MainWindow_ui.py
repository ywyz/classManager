'''
Date: 2024-04-06 21:18:30
Author: ywyz
LastModifiedBy: ywyz
Github: https://github.com/ywyz
LastEditors: ywyz
LastEditTime: 2024-04-06 21:24:54
'''
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from LoginUI_ui import Ui_Login_UI
from StuAddSingle_ui import Ui_StuAddSingle
from stuAttend_ui import Ui_StuDailyAttend
from stuhealthy_ui import Ui_StuHealthy
from stuChange_ui import Ui_StuChange
from ThingsAddSingle_ui import Ui_ThingsAddSingle
from Thingsquery_ui import Ui_ThingsQuery
from dataManager_ui import Ui_dataManager
from qfluentwidgets import NavigationItemPosition, FluentWindow, SubtitleLabel, setFont
from qfluentwidgets import FluentIcon as FIF


class Window(FluentWindow):
    def __init__(self):

        super().__init__()
        self.StuAddSingle = Ui_StuAddSingle(self)
        self.StuAddSingle.setObjectName("StuAddSingle")
        self.StuDailyAttend = Ui_StuDailyAttend(self)
        self.StuDailyAttend.setObjectName("StuDailyAttend")
        self.StuHealthy = Ui_StuHealthy(self)
        self.StuHealthy.setObjectName("StuHealthy")
        self.StuChange = Ui_StuChange(self)
        self.StuChange.setObjectName("StuChange")
        self.ThingsAddSingle = Ui_ThingsAddSingle(self)
        self.ThingsAddSingle.setObjectName("ThingsAddSingle")
        self.ThingsQuery = Ui_ThingsQuery(self)
        self.ThingsQuery.setObjectName("ThingsQuery")
        self.dataManager = Ui_dataManager(self)
        self.dataManager.setObjectName("dataManager")
        self.Login_UI = Ui_Login_UI(self)
        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.StuAddSingle, FIF.PEOPLE, "学生添加")
        self.addSubInterface(self.StuDailyAttend, FIF.CLOUD, "学生考勤")
        self.addSubInterface(self.StuHealthy, FIF.HEART, "学生健康")
        self.addSubInterface(self.StuChange, FIF.EDIT, "学生修改")
        self.addSubInterface(self.ThingsAddSingle, FIF.ADD, "物品添加")
        self.addSubInterface(self.ThingsQuery, FIF.SEARCH, "物品查询")
        self.addSubInterface(self.dataManager, FIF.FOLDER, "数据管理")
        self.navigationInterface.addSeparator()

    def initWindow(self):
        self.resize(1920, 1080)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('PyQt-Fluent-Widgets')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
