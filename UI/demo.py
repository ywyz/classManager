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
from Interface import (StuChangeinterface, StuDailyAttendinterface, StuHealthyinterface, ThingsAddSingleinterface,
                       ThingsQueryinterface, dataManagerinterface, StuAddSingleinterface)
from qfluentwidgets import NavigationItemPosition, FluentWindow, SubtitleLabel, setFont
from qfluentwidgets import FluentIcon as FIF


class Window(FluentWindow):
    def __init__(self):

        super().__init__()
        self.StuAddSingle = StuAddSingleinterface(self)
        self.StuDailyAttend = StuDailyAttendinterface(self)
        self.StuHealthy = StuHealthyinterface(self)
        self.StuChange = StuChangeinterface(self)
        self.ThingsAddSingle = ThingsAddSingleinterface(self)
        self.ThingsQuery = ThingsQueryinterface(self)
        self.dataManager = dataManagerinterface(self)

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

    def initWindow(self):
        self.resize(1400, 900)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('PyQt-Fluent-Widgets')

    def switchTo(self, interface) -> None:
        self.addSubInterface(interface, FIF.PEOPLE, "学生添加")
        self.addSubInterface(interface, FIF.CLOUD, "学生考勤")
        self.addSubInterface(interface, FIF.HEART, "学生健康")
        self.addSubInterface(interface, FIF.EDIT, "学生修改")
        self.addSubInterface(interface, FIF.ADD, "物品添加")
        self.addSubInterface(interface, FIF.SEARCH, "物品查询")
        self.addSubInterface(interface, FIF.FOLDER, "数据管理")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
