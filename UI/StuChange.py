# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/yw980/code/classManager/UI/StuChange.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_StuChange(object):
    def setupUi(self, StuChange):
        StuChange.setObjectName("StuChange")
        StuChange.resize(1400, 900)
        self.widget = QtWidgets.QWidget(StuChange)
        self.widget.setGeometry(QtCore.QRect(100, 50, 1171, 731))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.queryButton = PrimaryPushButton(self.widget)
        self.queryButton.setObjectName("queryButton")
        self.gridLayout.addWidget(self.queryButton, 0, 1, 1, 1)
        self.TableWidget = TableWidget(self.widget)
        self.TableWidget.setObjectName("TableWidget")
        self.TableWidget.setColumnCount(0)
        self.TableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.TableWidget, 1, 0, 1, 2)
        self.widget1 = QtWidgets.QWidget(StuChange)
        self.widget1.setGeometry(QtCore.QRect(420, 810, 471, 51))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.changeButton = PrimaryPushButton(self.widget1)
        self.changeButton.setObjectName("changeButton")
        self.horizontalLayout.addWidget(self.changeButton)
        self.deleteButton = PrimaryPushButton(self.widget1)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.returnButton = PrimaryPushButton(self.widget1)
        self.returnButton.setObjectName("returnButton")
        self.horizontalLayout.addWidget(self.returnButton)

        self.retranslateUi(StuChange)
        QtCore.QMetaObject.connectSlotsByName(StuChange)

    def retranslateUi(self, StuChange):
        _translate = QtCore.QCoreApplication.translate
        StuChange.setWindowTitle(_translate("StuChange", "学籍管理系统"))
        self.lineEdit.setText(_translate("StuChange", "请输入要查找幼儿的姓名"))
        self.queryButton.setText(_translate("StuChange", "查询"))
        self.changeButton.setText(_translate("StuChange", "修改"))
        self.deleteButton.setText(_translate("StuChange", "删除"))
        self.returnButton.setText(_translate("StuChange", "返回"))
from qfluentwidgets import PrimaryPushButton, TableWidget