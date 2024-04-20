# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stuAttend.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLineEdit, QSizePolicy, QTableWidgetItem, QWidget)

from qfluentwidgets import (DatePicker, PrimaryPushButton, PushButton, TableWidget,
    ZhDatePicker)

class Ui_StuDailyAttend(QWidget):
    def setupUi(self, StuDailyAttend):

        StuDailyAttend.setObjectName(u"StuDailyAttend")
        StuDailyAttend.resize(1400, 900)
        self.widget = QWidget(StuDailyAttend)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(120, 60, 1071, 661))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ZhDatePicker = ZhDatePicker(self.widget)
        self.ZhDatePicker.setObjectName(u"ZhDatePicker")

        self.gridLayout.addWidget(self.ZhDatePicker, 0, 0, 1, 1)

        self.queryDateButton = PrimaryPushButton(self.widget)
        self.queryDateButton.setObjectName(u"queryDateButton")

        self.gridLayout.addWidget(self.queryDateButton, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)

        self.queryChildButton = PrimaryPushButton(self.widget)
        self.queryChildButton.setObjectName(u"queryChildButton")

        self.gridLayout.addWidget(self.queryChildButton, 0, 3, 1, 1)

        self.TableWidget = TableWidget(self.widget)
        self.TableWidget.setObjectName(u"TableWidget")

        self.gridLayout.addWidget(self.TableWidget, 1, 0, 1, 4)

        self.widget1 = QWidget(StuDailyAttend)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(421, 819, 551, 51))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SaveButton = PrimaryPushButton(self.widget1)
        self.SaveButton.setObjectName(u"SaveButton")

        self.horizontalLayout.addWidget(self.SaveButton)

        self.changeButton = PrimaryPushButton(self.widget1)
        self.changeButton.setObjectName(u"changeButton")

        self.horizontalLayout.addWidget(self.changeButton)

        self.returnButton = PrimaryPushButton(self.widget1)
        self.returnButton.setObjectName(u"returnButton")

        self.horizontalLayout.addWidget(self.returnButton)

        self.SaveButton_2 = PrimaryPushButton(self.widget1)
        self.SaveButton_2.setObjectName(u"SaveButton_2")

        self.horizontalLayout.addWidget(self.SaveButton_2)


        self.retranslateUi(StuDailyAttend)

        QMetaObject.connectSlotsByName(StuDailyAttend)
    # setupUi

    def retranslateUi(self, StuDailyAttend):
        StuDailyAttend.setWindowTitle(QCoreApplication.translate("StuDailyAttend", u"\u5b66\u751f\u51fa\u52e4\u7ba1\u7406\u7cfb\u7edf", None))
        self.queryDateButton.setText(QCoreApplication.translate("StuDailyAttend", u"\u67e5\u8be2", None))
        self.lineEdit.setText(QCoreApplication.translate("StuDailyAttend", u"\u8bf7\u8f93\u5165\u8981\u67e5\u627e\u5e7c\u513f\u7684\u59d3\u540d", None))
        self.queryChildButton.setText(QCoreApplication.translate("StuDailyAttend", u"\u67e5\u8be2", None))
        self.SaveButton.setText(QCoreApplication.translate("StuDailyAttend", u"\u4fdd\u5b58", None))
        self.changeButton.setText(QCoreApplication.translate("StuDailyAttend", u"\u4fee\u6539", None))
        self.returnButton.setText(QCoreApplication.translate("StuDailyAttend", u"\u8fd4\u56de", None))
        self.SaveButton_2.setText(QCoreApplication.translate("StuDailyAttend", u"\u5bfc\u51fa", None))
    # retranslateUi
