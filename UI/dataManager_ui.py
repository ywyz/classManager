# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataManager.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CaptionLabel, DateEdit, ImageLabel,
    LineEdit, PlainTextEdit, PrimaryPushButton, PushButton)

class Ui_dataManager(object):
    def setupUi(self, dataManager):
        if not dataManager.objectName():
            dataManager.setObjectName(u"dataManager")
        dataManager.resize(1400, 900)
        self.widget = QWidget(dataManager)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 56, 1321, 831))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.DateEdit = DateEdit(self.widget)
        self.DateEdit.setObjectName(u"DateEdit")

        self.horizontalLayout.addWidget(self.DateEdit)

        self.CaptionLabel = CaptionLabel(self.widget)
        self.CaptionLabel.setObjectName(u"CaptionLabel")

        self.horizontalLayout.addWidget(self.CaptionLabel)

        self.BodyLabel = BodyLabel(self.widget)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.horizontalLayout.addWidget(self.BodyLabel)

        self.dataCombo = QComboBox(self.widget)
        self.dataCombo.setObjectName(u"dataCombo")

        self.horizontalLayout.addWidget(self.dataCombo)

        self.dateQueryButton = PrimaryPushButton(self.widget)
        self.dateQueryButton.setObjectName(u"dateQueryButton")

        self.horizontalLayout.addWidget(self.dateQueryButton)

        self.suggestButton = PrimaryPushButton(self.widget)
        self.suggestButton.setObjectName(u"suggestButton")

        self.horizontalLayout.addWidget(self.suggestButton)

        self.SaveButton = PrimaryPushButton(self.widget)
        self.SaveButton.setObjectName(u"SaveButton")

        self.horizontalLayout.addWidget(self.SaveButton)

        self.clearButton = PrimaryPushButton(self.widget)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout.addWidget(self.clearButton)

        self.ImportButton = PrimaryPushButton(self.widget)
        self.ImportButton.setObjectName(u"ImportButton")

        self.horizontalLayout.addWidget(self.ImportButton)

        self.returnButton = PrimaryPushButton(self.widget)
        self.returnButton.setObjectName(u"returnButton")

        self.horizontalLayout.addWidget(self.returnButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BodyLabel_2 = BodyLabel(self.widget)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.horizontalLayout_2.addWidget(self.BodyLabel_2)

        self.NameEdit = LineEdit(self.widget)
        self.NameEdit.setObjectName(u"NameEdit")

        self.horizontalLayout_2.addWidget(self.NameEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BodyLabel_3 = BodyLabel(self.widget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.horizontalLayout_3.addWidget(self.BodyLabel_3)

        self.AddressEdit = LineEdit(self.widget)
        self.AddressEdit.setObjectName(u"AddressEdit")

        self.horizontalLayout_3.addWidget(self.AddressEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BodyLabel_4 = BodyLabel(self.widget)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.horizontalLayout_4.addWidget(self.BodyLabel_4)

        self.GoalEdit = PlainTextEdit(self.widget)
        self.GoalEdit.setObjectName(u"GoalEdit")

        self.horizontalLayout_4.addWidget(self.GoalEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.BodyLabel_5 = BodyLabel(self.widget)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.horizontalLayout_5.addWidget(self.BodyLabel_5)

        self.pointEdit = PlainTextEdit(self.widget)
        self.pointEdit.setObjectName(u"pointEdit")

        self.horizontalLayout_5.addWidget(self.pointEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.BodyLabel_6 = BodyLabel(self.widget)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")

        self.horizontalLayout_6.addWidget(self.BodyLabel_6)

        self.importantedit = LineEdit(self.widget)
        self.importantedit.setObjectName(u"importantedit")

        self.horizontalLayout_6.addWidget(self.importantedit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.BodyLabel_7 = BodyLabel(self.widget)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")

        self.horizontalLayout_8.addWidget(self.BodyLabel_7)

        self.difficultEdit = LineEdit(self.widget)
        self.difficultEdit.setObjectName(u"difficultEdit")

        self.horizontalLayout_8.addWidget(self.difficultEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.BodyLabel_8 = BodyLabel(self.widget)
        self.BodyLabel_8.setObjectName(u"BodyLabel_8")

        self.horizontalLayout_7.addWidget(self.BodyLabel_8)

        self.prepareEdit = PlainTextEdit(self.widget)
        self.prepareEdit.setObjectName(u"prepareEdit")

        self.horizontalLayout_7.addWidget(self.prepareEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 3, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.BodyLabel_9 = BodyLabel(self.widget)
        self.BodyLabel_9.setObjectName(u"BodyLabel_9")

        self.horizontalLayout_9.addWidget(self.BodyLabel_9)

        self.InputEdit = PlainTextEdit(self.widget)
        self.InputEdit.setObjectName(u"InputEdit")

        self.horizontalLayout_9.addWidget(self.InputEdit)


        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 1, 3, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.BodyLabel_11 = BodyLabel(self.widget)
        self.BodyLabel_11.setObjectName(u"BodyLabel_11")

        self.horizontalLayout_11.addWidget(self.BodyLabel_11)

        self.GoalEdit_2 = PlainTextEdit(self.widget)
        self.GoalEdit_2.setObjectName(u"GoalEdit_2")

        self.horizontalLayout_11.addWidget(self.GoalEdit_2)


        self.gridLayout.addLayout(self.horizontalLayout_11, 1, 2, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.BodyLabel_12 = BodyLabel(self.widget)
        self.BodyLabel_12.setObjectName(u"BodyLabel_12")

        self.horizontalLayout_12.addWidget(self.BodyLabel_12)

        self.GoalEdit_3 = PlainTextEdit(self.widget)
        self.GoalEdit_3.setObjectName(u"GoalEdit_3")

        self.horizontalLayout_12.addWidget(self.GoalEdit_3)


        self.gridLayout.addLayout(self.horizontalLayout_12, 2, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.ImageLabel = ImageLabel(self.widget)
        self.ImageLabel.setObjectName(u"ImageLabel")

        self.horizontalLayout_13.addWidget(self.ImageLabel)

        self.ImageLabel_2 = ImageLabel(self.widget)
        self.ImageLabel_2.setObjectName(u"ImageLabel_2")

        self.horizontalLayout_13.addWidget(self.ImageLabel_2)

        self.ImageLabel_3 = ImageLabel(self.widget)
        self.ImageLabel_3.setObjectName(u"ImageLabel_3")

        self.horizontalLayout_13.addWidget(self.ImageLabel_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.uploadButton = PrimaryPushButton(self.widget)
        self.uploadButton.setObjectName(u"uploadButton")

        self.verticalLayout_2.addWidget(self.uploadButton)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 2, 1, 1)


        self.retranslateUi(dataManager)

        QMetaObject.connectSlotsByName(dataManager)
    # setupUi

    def retranslateUi(self, dataManager):
        dataManager.setWindowTitle(QCoreApplication.translate("dataManager", u"\u8d44\u6599\u7ba1\u7406\u7cfb\u7edf", None))
        self.CaptionLabel.setText("")
        self.BodyLabel.setText(QCoreApplication.translate("dataManager", u"\u8d44\u6599\u540d\u79f0", None))
        self.dateQueryButton.setText(QCoreApplication.translate("dataManager", u"\u67e5\u8be2", None))
        self.suggestButton.setText(QCoreApplication.translate("dataManager", u"\u5efa\u8bae", None))
        self.SaveButton.setText(QCoreApplication.translate("dataManager", u"\u4fdd\u5b58", None))
        self.clearButton.setText(QCoreApplication.translate("dataManager", u"\u6e05\u9664", None))
        self.ImportButton.setText(QCoreApplication.translate("dataManager", u"\u5bfc\u51fa", None))
        self.returnButton.setText(QCoreApplication.translate("dataManager", u"\u8fd4\u56de", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("dataManager", u"\u540d\u79f0", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("dataManager", u"\u5730\u70b9", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("dataManager", u"\u76ee\u6807", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("dataManager", u"\u6307\u5bfc\u8981\u70b9", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("dataManager", u"\u91cd\u70b9", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("dataManager", u"\u96be\u70b9", None))
        self.BodyLabel_8.setText(QCoreApplication.translate("dataManager", u"\u51c6\u5907", None))
        self.BodyLabel_9.setText(QCoreApplication.translate("dataManager", u"\u5185\u5bb9", None))
        self.BodyLabel_11.setText(QCoreApplication.translate("dataManager", u"\u8bc4\u4ef7", None))
        self.BodyLabel_12.setText(QCoreApplication.translate("dataManager", u"\u652f\u6301\u7b56\u7565", None))
        self.uploadButton.setText(QCoreApplication.translate("dataManager", u"\u56fe\u7247\u4e0a\u4f20", None))
    # retranslateUi

