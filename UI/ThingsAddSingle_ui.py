# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ThingsAddSingle.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CheckBox, ImageLabel, LineEdit,
    PrimaryPushButton, PushButton)

class Ui_ThingsAddSingle(object):
    def setupUi(self, ThingsAddSingle):
        if not ThingsAddSingle.objectName():
            ThingsAddSingle.setObjectName(u"ThingsAddSingle")
        ThingsAddSingle.resize(1394, 900)
        self.layoutWidget = QWidget(ThingsAddSingle)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(450, 650, 511, 41))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.uploadButton = PrimaryPushButton(self.layoutWidget)
        self.uploadButton.setObjectName(u"uploadButton")

        self.horizontalLayout_14.addWidget(self.uploadButton)

        self.clearButton = PrimaryPushButton(self.layoutWidget)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout_14.addWidget(self.clearButton)

        self.returnButton = PrimaryPushButton(self.layoutWidget)
        self.returnButton.setObjectName(u"returnButton")

        self.horizontalLayout_14.addWidget(self.returnButton)

        self.widget = QWidget(ThingsAddSingle)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(411, 267, 591, 251))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PictureLabel = ImageLabel(self.widget)
        self.PictureLabel.setObjectName(u"PictureLabel")

        self.verticalLayout.addWidget(self.PictureLabel)

        self.uploadPicButton = PushButton(self.widget)
        self.uploadPicButton.setObjectName(u"uploadPicButton")

        self.verticalLayout.addWidget(self.uploadPicButton)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stuLabel = BodyLabel(self.widget)
        self.stuLabel.setObjectName(u"stuLabel")

        self.horizontalLayout.addWidget(self.stuLabel)

        self.thingsName = LineEdit(self.widget)
        self.thingsName.setObjectName(u"thingsName")

        self.horizontalLayout.addWidget(self.thingsName)

        self.bodyLabel_3 = BodyLabel(self.widget)
        self.bodyLabel_3.setObjectName(u"bodyLabel_3")

        self.horizontalLayout.addWidget(self.bodyLabel_3)

        self.barCode = LineEdit(self.widget)
        self.barCode.setObjectName(u"barCode")

        self.horizontalLayout.addWidget(self.barCode)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sexLabel = BodyLabel(self.widget)
        self.sexLabel.setObjectName(u"sexLabel")

        self.horizontalLayout_2.addWidget(self.sexLabel)

        self.Address = LineEdit(self.widget)
        self.Address.setObjectName(u"Address")

        self.horizontalLayout_2.addWidget(self.Address)

        self.bodyLabel_4 = BodyLabel(self.widget)
        self.bodyLabel_4.setObjectName(u"bodyLabel_4")

        self.horizontalLayout_2.addWidget(self.bodyLabel_4)

        self.YesBox = CheckBox(self.widget)
        self.YesBox.setObjectName(u"YesBox")

        self.horizontalLayout_2.addWidget(self.YesBox)

        self.NoBox = CheckBox(self.widget)
        self.NoBox.setObjectName(u"NoBox")

        self.horizontalLayout_2.addWidget(self.NoBox)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)


        self.retranslateUi(ThingsAddSingle)

        QMetaObject.connectSlotsByName(ThingsAddSingle)
    # setupUi

    def retranslateUi(self, ThingsAddSingle):
        ThingsAddSingle.setWindowTitle(QCoreApplication.translate("ThingsAddSingle", u"\u7269\u54c1\u7ba1\u7406\u7cfb\u7edf", None))
        self.uploadButton.setText(QCoreApplication.translate("ThingsAddSingle", u"\u63d0\u4ea4", None))
        self.clearButton.setText(QCoreApplication.translate("ThingsAddSingle", u"\u6e05\u9664", None))
        self.returnButton.setText(QCoreApplication.translate("ThingsAddSingle", u"\u8fd4\u56de", None))
        self.uploadPicButton.setText(QCoreApplication.translate("ThingsAddSingle", u"\u4e0a\u4f20\u7167\u7247", None))
        self.stuLabel.setText(QCoreApplication.translate("ThingsAddSingle", u"\u7269\u54c1\u540d\u79f0", None))
        self.bodyLabel_3.setText(QCoreApplication.translate("ThingsAddSingle", u"\u6761\u7801", None))
        self.sexLabel.setText(QCoreApplication.translate("ThingsAddSingle", u"\u76ee\u524d\u6240\u5728\u4f4d\u7f6e", None))
        self.bodyLabel_4.setText(QCoreApplication.translate("ThingsAddSingle", u"\u662f\u5426\u9700\u8981\u7ef4\u4fee", None))
        self.YesBox.setText(QCoreApplication.translate("ThingsAddSingle", u"\u662f", None))
        self.NoBox.setText(QCoreApplication.translate("ThingsAddSingle", u"\u5426", None))
    # retranslateUi

