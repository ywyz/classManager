# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StuAddSingle.ui'
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

from qfluentwidgets import (BodyLabel, ComboBox, EditableComboBox, ImageLabel,
    LineEdit, PrimaryPushButton, PushButton)

class Ui_StuAddSingle(QWidget):
    def setupUi(self, StuAddSingle):
        if not StuAddSingle.objectName():
            StuAddSingle.setObjectName(u"StuAddSingle")
        StuAddSingle.resize(1400, 900)
        self.layoutWidget = QWidget(StuAddSingle)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 60, 1071, 641))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PictureLabel = ImageLabel(self.layoutWidget)
        self.PictureLabel.setObjectName(u"PictureLabel")

        self.verticalLayout.addWidget(self.PictureLabel)

        self.uploadPicButton = PushButton(self.layoutWidget)
        self.uploadPicButton.setObjectName(u"uploadPicButton")

        self.verticalLayout.addWidget(self.uploadPicButton)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.stuLabel = BodyLabel(self.layoutWidget)
        self.stuLabel.setObjectName(u"stuLabel")

        self.horizontalLayout_9.addWidget(self.stuLabel)

        self.stuName = LineEdit(self.layoutWidget)
        self.stuName.setObjectName(u"stuName")

        self.horizontalLayout_9.addWidget(self.stuName)


        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.bodyLabel_3 = BodyLabel(self.layoutWidget)
        self.bodyLabel_3.setObjectName(u"bodyLabel_3")

        self.horizontalLayout_10.addWidget(self.bodyLabel_3)

        self.stuBirthAddress = LineEdit(self.layoutWidget)
        self.stuBirthAddress.setObjectName(u"stuBirthAddress")

        self.horizontalLayout_10.addWidget(self.stuBirthAddress)


        self.gridLayout.addLayout(self.horizontalLayout_10, 0, 2, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.sexLabel = BodyLabel(self.layoutWidget)
        self.sexLabel.setObjectName(u"sexLabel")

        self.horizontalLayout_8.addWidget(self.sexLabel)

        self.stuSex = ComboBox(self.layoutWidget)
        self.stuSex.setObjectName(u"stuSex")

        self.horizontalLayout_8.addWidget(self.stuSex)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.bodyLabel_4 = BodyLabel(self.layoutWidget)
        self.bodyLabel_4.setObjectName(u"bodyLabel_4")

        self.horizontalLayout_11.addWidget(self.bodyLabel_4)

        self.Country = EditableComboBox(self.layoutWidget)
        self.Country.setObjectName(u"Country")

        self.horizontalLayout_11.addWidget(self.Country)


        self.gridLayout.addLayout(self.horizontalLayout_11, 1, 2, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.bodyLabel = BodyLabel(self.layoutWidget)
        self.bodyLabel.setObjectName(u"bodyLabel")

        self.horizontalLayout_7.addWidget(self.bodyLabel)

        self.stuIDCard = LineEdit(self.layoutWidget)
        self.stuIDCard.setObjectName(u"stuIDCard")

        self.horizontalLayout_7.addWidget(self.stuIDCard)


        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.bodyLabel_5 = BodyLabel(self.layoutWidget)
        self.bodyLabel_5.setObjectName(u"bodyLabel_5")

        self.horizontalLayout_12.addWidget(self.bodyLabel_5)

        self.Nation = EditableComboBox(self.layoutWidget)
        self.Nation.setObjectName(u"Nation")

        self.horizontalLayout_12.addWidget(self.Nation)


        self.gridLayout.addLayout(self.horizontalLayout_12, 2, 2, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bodyLabel_2 = BodyLabel(self.layoutWidget)
        self.bodyLabel_2.setObjectName(u"bodyLabel_2")

        self.horizontalLayout_6.addWidget(self.bodyLabel_2)

        self.stuIDAddress = LineEdit(self.layoutWidget)
        self.stuIDAddress.setObjectName(u"stuIDAddress")

        self.horizontalLayout_6.addWidget(self.stuIDAddress)


        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bodyLabel_6 = BodyLabel(self.layoutWidget)
        self.bodyLabel_6.setObjectName(u"bodyLabel_6")

        self.horizontalLayout_5.addWidget(self.bodyLabel_6)

        self.faName = LineEdit(self.layoutWidget)
        self.faName.setObjectName(u"faName")

        self.horizontalLayout_5.addWidget(self.faName)


        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.bodyLabel_7 = BodyLabel(self.layoutWidget)
        self.bodyLabel_7.setObjectName(u"bodyLabel_7")

        self.horizontalLayout_13.addWidget(self.bodyLabel_7)

        self.moName = LineEdit(self.layoutWidget)
        self.moName.setObjectName(u"moName")

        self.horizontalLayout_13.addWidget(self.moName)


        self.gridLayout.addLayout(self.horizontalLayout_13, 4, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.bodyLabel_8 = BodyLabel(self.layoutWidget)
        self.bodyLabel_8.setObjectName(u"bodyLabel_8")

        self.horizontalLayout_4.addWidget(self.bodyLabel_8)

        self.faIDCard = LineEdit(self.layoutWidget)
        self.faIDCard.setObjectName(u"faIDCard")

        self.horizontalLayout_4.addWidget(self.faIDCard)


        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bodyLabel_9 = BodyLabel(self.layoutWidget)
        self.bodyLabel_9.setObjectName(u"bodyLabel_9")

        self.horizontalLayout_3.addWidget(self.bodyLabel_9)

        self.moIDCard = LineEdit(self.layoutWidget)
        self.moIDCard.setObjectName(u"moIDCard")

        self.horizontalLayout_3.addWidget(self.moIDCard)


        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bodyLabel_10 = BodyLabel(self.layoutWidget)
        self.bodyLabel_10.setObjectName(u"bodyLabel_10")

        self.horizontalLayout_2.addWidget(self.bodyLabel_10)

        self.faTelecom = LineEdit(self.layoutWidget)
        self.faTelecom.setObjectName(u"faTelecom")

        self.horizontalLayout_2.addWidget(self.faTelecom)


        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bodyLabel_11 = BodyLabel(self.layoutWidget)
        self.bodyLabel_11.setObjectName(u"bodyLabel_11")

        self.horizontalLayout.addWidget(self.bodyLabel_11)

        self.moTelecom = LineEdit(self.layoutWidget)
        self.moTelecom.setObjectName(u"moTelecom")

        self.horizontalLayout.addWidget(self.moTelecom)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 2, 1, 1)

        self.widget = QWidget(StuAddSingle)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(340, 780, 511, 41))
        self.horizontalLayout_14 = QHBoxLayout(self.widget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.uploadButton_2 = PrimaryPushButton(self.widget)
        self.uploadButton_2.setObjectName(u"uploadButton_2")

        self.horizontalLayout_14.addWidget(self.uploadButton_2)

        self.uploadButton = PrimaryPushButton(self.widget)
        self.uploadButton.setObjectName(u"uploadButton")

        self.horizontalLayout_14.addWidget(self.uploadButton)

        self.clearButton = PrimaryPushButton(self.widget)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout_14.addWidget(self.clearButton)

        self.returnButton = PrimaryPushButton(self.widget)
        self.returnButton.setObjectName(u"returnButton")

        self.horizontalLayout_14.addWidget(self.returnButton)


        self.retranslateUi(StuAddSingle)

        QMetaObject.connectSlotsByName(StuAddSingle)
    # setupUi

    def retranslateUi(self, StuAddSingle):
        StuAddSingle.setWindowTitle(QCoreApplication.translate("StuAddSingle", u"\u5b66\u7c4d\u7ba1\u7406\u7cfb\u7edf", None))
        self.uploadPicButton.setText(QCoreApplication.translate("StuAddSingle", u"\u4e0a\u4f20\u7167\u7247", None))
        self.stuLabel.setText(QCoreApplication.translate("StuAddSingle", u"\u5e7c\u513f\u59d3\u540d\uff1a", None))
        self.bodyLabel_3.setText(QCoreApplication.translate("StuAddSingle", u"\u51fa\u751f\u5730", None))
        self.sexLabel.setText(QCoreApplication.translate("StuAddSingle", u"\u6027\u522b:", None))
        self.bodyLabel_4.setText(QCoreApplication.translate("StuAddSingle", u"\u56fd\u7c4d", None))
        self.bodyLabel.setText(QCoreApplication.translate("StuAddSingle", u"\u8eab\u4efd\u8bc1\u53f7\u7801", None))
        self.bodyLabel_5.setText(QCoreApplication.translate("StuAddSingle", u"\u6c11\u65cf", None))
        self.bodyLabel_2.setText(QCoreApplication.translate("StuAddSingle", u"\u6237\u7c4d\u5730\u5740", None))
        self.bodyLabel_6.setText(QCoreApplication.translate("StuAddSingle", u"\u7236\u4eb2\u59d3\u540d", None))
        self.bodyLabel_7.setText(QCoreApplication.translate("StuAddSingle", u"\u6bcd\u4eb2\u59d3\u540d", None))
        self.bodyLabel_8.setText(QCoreApplication.translate("StuAddSingle", u"\u7236\u4eb2\u8eab\u4efd\u8bc1", None))
        self.bodyLabel_9.setText(QCoreApplication.translate("StuAddSingle", u"\u6bcd\u4eb2\u8eab\u4efd\u8bc1", None))
        self.bodyLabel_10.setText(QCoreApplication.translate("StuAddSingle", u"\u7236\u4eb2\u8054\u7cfb\u53f7\u7801", None))
        self.bodyLabel_11.setText(QCoreApplication.translate("StuAddSingle", u"\u6bcd\u4eb2\u8054\u7cfb\u53f7\u7801", None))
        self.uploadButton_2.setText(QCoreApplication.translate("StuAddSingle", u"\u6279\u91cf\u6dfb\u52a0", None))
        self.uploadButton.setText(QCoreApplication.translate("StuAddSingle", u"\u63d0\u4ea4", None))
        self.clearButton.setText(QCoreApplication.translate("StuAddSingle", u"\u6e05\u9664", None))
        self.returnButton.setText(QCoreApplication.translate("StuAddSingle", u"\u8fd4\u56de", None))
    # retranslateUi
