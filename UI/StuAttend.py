# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/yw980/code/classManager/UI/StuAttend.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_StuDailyAttend(object):
    def setupUi(self, StuDailyAttend):
        StuDailyAttend.setObjectName("StuDailyAttend")
        StuDailyAttend.resize(1400, 900)
        self.widget = QtWidgets.QWidget(StuDailyAttend)
        self.widget.setGeometry(QtCore.QRect(120, 60, 1071, 661))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ZhDatePicker = ZhDatePicker(self.widget)
        self.ZhDatePicker.setObjectName("ZhDatePicker")
        self.gridLayout.addWidget(self.ZhDatePicker, 0, 0, 1, 1)
        self.queryDateButton = PrimaryPushButton(self.widget)
        self.queryDateButton.setObjectName("queryDateButton")
        self.gridLayout.addWidget(self.queryDateButton, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.queryChildButton = PrimaryPushButton(self.widget)
        self.queryChildButton.setObjectName("queryChildButton")
        self.gridLayout.addWidget(self.queryChildButton, 0, 3, 1, 1)
        self.TableWidget = TableWidget(self.widget)
        self.TableWidget.setObjectName("TableWidget")
        self.TableWidget.setColumnCount(0)
        self.TableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.TableWidget, 1, 0, 1, 4)
        self.widget1 = QtWidgets.QWidget(StuDailyAttend)
        self.widget1.setGeometry(QtCore.QRect(421, 819, 551, 51))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SaveButton = PrimaryPushButton(self.widget1)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout.addWidget(self.SaveButton)
        self.changeButton = PrimaryPushButton(self.widget1)
        self.changeButton.setObjectName("changeButton")
        self.horizontalLayout.addWidget(self.changeButton)
        self.returnButton = PrimaryPushButton(self.widget1)
        self.returnButton.setObjectName("returnButton")
        self.horizontalLayout.addWidget(self.returnButton)
        self.SaveButton_2 = PrimaryPushButton(self.widget1)
        self.SaveButton_2.setObjectName("SaveButton_2")
        self.horizontalLayout.addWidget(self.SaveButton_2)

        self.retranslateUi(StuDailyAttend)
        QtCore.QMetaObject.connectSlotsByName(StuDailyAttend)

    def retranslateUi(self, StuDailyAttend):
        _translate = QtCore.QCoreApplication.translate
        StuDailyAttend.setWindowTitle(_translate("StuDailyAttend", "学生出勤管理系统"))
        self.queryDateButton.setText(_translate("StuDailyAttend", "查询"))
        self.lineEdit.setText(_translate("StuDailyAttend", "请输入要查找幼儿的姓名"))
        self.queryChildButton.setText(_translate("StuDailyAttend", "查询"))
        self.SaveButton.setText(_translate("StuDailyAttend", "保存"))
        self.changeButton.setText(_translate("StuDailyAttend", "修改"))
        self.returnButton.setText(_translate("StuDailyAttend", "返回"))
        self.SaveButton_2.setText(_translate("StuDailyAttend", "导出"))
from qfluentwidgets import PrimaryPushButton, TableWidget, ZhDatePicker
