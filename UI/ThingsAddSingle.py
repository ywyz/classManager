# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/yw980/code/classManager/UI/ThingsAddSingle.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_ThingsAddSingle(object):
    def setupUi(self, ThingsAddSingle):
        ThingsAddSingle.setObjectName("ThingsAddSingle")
        ThingsAddSingle.resize(1394, 900)
        self.layoutWidget = QtWidgets.QWidget(ThingsAddSingle)
        self.layoutWidget.setGeometry(QtCore.QRect(450, 650, 511, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.uploadButton = PrimaryPushButton(self.layoutWidget)
        self.uploadButton.setObjectName("uploadButton")
        self.horizontalLayout_14.addWidget(self.uploadButton)
        self.clearButton = PrimaryPushButton(self.layoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_14.addWidget(self.clearButton)
        self.returnButton = PrimaryPushButton(self.layoutWidget)
        self.returnButton.setObjectName("returnButton")
        self.horizontalLayout_14.addWidget(self.returnButton)
        self.widget = QtWidgets.QWidget(ThingsAddSingle)
        self.widget.setGeometry(QtCore.QRect(411, 267, 591, 251))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PictureLabel = ImageLabel(self.widget)
        self.PictureLabel.setObjectName("PictureLabel")
        self.verticalLayout.addWidget(self.PictureLabel)
        self.uploadPicButton = PushButton(self.widget)
        self.uploadPicButton.setObjectName("uploadPicButton")
        self.verticalLayout.addWidget(self.uploadPicButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stuLabel = BodyLabel(self.widget)
        self.stuLabel.setObjectName("stuLabel")
        self.horizontalLayout.addWidget(self.stuLabel)
        self.thingsName = LineEdit(self.widget)
        self.thingsName.setObjectName("thingsName")
        self.horizontalLayout.addWidget(self.thingsName)
        self.bodyLabel_3 = BodyLabel(self.widget)
        self.bodyLabel_3.setObjectName("bodyLabel_3")
        self.horizontalLayout.addWidget(self.bodyLabel_3)
        self.barCode = LineEdit(self.widget)
        self.barCode.setObjectName("barCode")
        self.horizontalLayout.addWidget(self.barCode)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sexLabel = BodyLabel(self.widget)
        self.sexLabel.setObjectName("sexLabel")
        self.horizontalLayout_2.addWidget(self.sexLabel)
        self.Address = LineEdit(self.widget)
        self.Address.setObjectName("Address")
        self.horizontalLayout_2.addWidget(self.Address)
        self.bodyLabel_4 = BodyLabel(self.widget)
        self.bodyLabel_4.setObjectName("bodyLabel_4")
        self.horizontalLayout_2.addWidget(self.bodyLabel_4)
        self.YesBox = CheckBox(self.widget)
        self.YesBox.setObjectName("YesBox")
        self.horizontalLayout_2.addWidget(self.YesBox)
        self.NoBox = CheckBox(self.widget)
        self.NoBox.setObjectName("NoBox")
        self.horizontalLayout_2.addWidget(self.NoBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.retranslateUi(ThingsAddSingle)
        QtCore.QMetaObject.connectSlotsByName(ThingsAddSingle)

    def retranslateUi(self, ThingsAddSingle):
        _translate = QtCore.QCoreApplication.translate
        ThingsAddSingle.setWindowTitle(_translate("ThingsAddSingle", "物品管理系统"))
        self.uploadButton.setText(_translate("ThingsAddSingle", "提交"))
        self.clearButton.setText(_translate("ThingsAddSingle", "清除"))
        self.returnButton.setText(_translate("ThingsAddSingle", "返回"))
        self.uploadPicButton.setText(_translate("ThingsAddSingle", "上传照片"))
        self.stuLabel.setText(_translate("ThingsAddSingle", "物品名称"))
        self.bodyLabel_3.setText(_translate("ThingsAddSingle", "条码"))
        self.sexLabel.setText(_translate("ThingsAddSingle", "目前所在位置"))
        self.bodyLabel_4.setText(_translate("ThingsAddSingle", "是否需要维修"))
        self.YesBox.setText(_translate("ThingsAddSingle", "是"))
        self.NoBox.setText(_translate("ThingsAddSingle", "否"))


from qfluentwidgets import BodyLabel, CheckBox, ImageLabel, LineEdit, PrimaryPushButton, PushButton
