# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/yw980/code/classManager/UI/LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Login_UI(object):
    def setupUi(self, Login_UI):
        Login_UI.setObjectName("Login_UI")
        Login_UI.resize(1400, 908)
        self.login_pic = QtWidgets.QLabel(Login_UI)
        self.login_pic.setGeometry(QtCore.QRect(0, 0, 831, 1041))
        self.login_pic.setObjectName("login_pic")
        self.label = QtWidgets.QLabel(Login_UI)
        self.label.setGeometry(QtCore.QRect(953, 400, 91, 21))
        self.label.setText("")
        self.label.setObjectName("label")
        self.DisplayLabel = DisplayLabel(Login_UI)
        self.DisplayLabel.setGeometry(QtCore.QRect(540, 10, 451, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(QtGui.QFont.Normal)
        self.DisplayLabel.setFont(font)
        self.DisplayLabel.setObjectName("DisplayLabel")
        self.CheckBox = CheckBox(Login_UI)
        self.CheckBox.setGeometry(QtCore.QRect(910, 500, 211, 61))
        self.CheckBox.setObjectName("CheckBox")
        self.label_2 = QtWidgets.QLabel(Login_UI)
        self.label_2.setGeometry(QtCore.QRect(1010, 70, 200, 200))
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(Login_UI)
        self.layoutWidget.setGeometry(QtCore.QRect(910, 350, 351, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.UserName_Label = CaptionLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(QtGui.QFont.Normal)
        self.UserName_Label.setFont(font)
        self.UserName_Label.setObjectName("UserName_Label")
        self.horizontalLayout_2.addWidget(self.UserName_Label)
        self.UserNameEdit = LineEdit(self.layoutWidget)
        self.UserNameEdit.setObjectName("UserNameEdit")
        self.horizontalLayout_2.addWidget(self.UserNameEdit)
        self.layoutWidget1 = QtWidgets.QWidget(Login_UI)
        self.layoutWidget1.setGeometry(QtCore.QRect(990, 610, 181, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PrimaryPushButton = PrimaryPushButton(self.layoutWidget1)
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")
        self.verticalLayout.addWidget(self.PrimaryPushButton)
        self.HyperlinkButton = HyperlinkButton(self.layoutWidget1)
        self.HyperlinkButton.setObjectName("HyperlinkButton")
        self.verticalLayout.addWidget(self.HyperlinkButton)
        self.layoutWidget2 = QtWidgets.QWidget(Login_UI)
        self.layoutWidget2.setGeometry(QtCore.QRect(920, 440, 341, 35))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CaptionLabel_2 = CaptionLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(QtGui.QFont.Normal)
        self.CaptionLabel_2.setFont(font)
        self.CaptionLabel_2.setObjectName("CaptionLabel_2")
        self.horizontalLayout.addWidget(self.CaptionLabel_2)
        self.PasswordLineEdit = PasswordLineEdit(self.layoutWidget2)
        self.PasswordLineEdit.setObjectName("PasswordLineEdit")
        self.horizontalLayout.addWidget(self.PasswordLineEdit)

        self.retranslateUi(Login_UI)
        QtCore.QMetaObject.connectSlotsByName(Login_UI)

    def retranslateUi(self, Login_UI):
        _translate = QtCore.QCoreApplication.translate
        Login_UI.setWindowTitle(_translate("Login_UI", "登录界面"))
        self.login_pic.setText(_translate("Login_UI", "<html><head/><body><p><img src=\":/door/login (自定义).jpg\"/></p></body></html>"))
        self.DisplayLabel.setText(_translate("Login_UI", "欢迎使用班级保教管理系统"))
        self.CheckBox.setText(_translate("Login_UI", "记住我"))
        self.label_2.setText(_translate("Login_UI", "<html><head/><body><p><img src=\":/door/logo (自定义).png\"/></p></body></html>"))
        self.UserName_Label.setText(_translate("Login_UI", "用户名："))
        self.PrimaryPushButton.setText(_translate("Login_UI", "登录"))
        self.HyperlinkButton.setText(_translate("Login_UI", "找回密码"))
        self.CaptionLabel_2.setText(_translate("Login_UI", "密码："))
from qfluentwidgets import CaptionLabel, CheckBox, DisplayLabel, HyperlinkButton, LineEdit, PasswordLineEdit, PrimaryPushButton
import resource.LoginUI_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_UI = QtWidgets.QWidget()
    ui = Ui_Login_UI()
    ui.setupUi(Login_UI)
    Login_UI.show()
    sys.exit(app.exec_())