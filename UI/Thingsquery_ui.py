# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Thingsquery.ui'
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

from qfluentwidgets import (PrimaryPushButton, PushButton, TableWidget)

class Ui_ThingsQuery(QWidget):
    def setupUi(self, ThingsQuery):

        ThingsQuery.setObjectName(u"ThingsQuery")
        ThingsQuery.resize(1400, 900)
        self.layoutWidget = QWidget(ThingsQuery)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 60, 1071, 661))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.queryChildButton = PrimaryPushButton(self.layoutWidget)
        self.queryChildButton.setObjectName(u"queryChildButton")

        self.gridLayout.addWidget(self.queryChildButton, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.TableWidget = TableWidget(self.layoutWidget)
        self.TableWidget.setObjectName(u"TableWidget")

        self.gridLayout.addWidget(self.TableWidget, 1, 0, 1, 3)

        self.layoutWidget1 = QWidget(ThingsQuery)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(421, 819, 551, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SaveButton = PrimaryPushButton(self.layoutWidget1)
        self.SaveButton.setObjectName(u"SaveButton")

        self.horizontalLayout.addWidget(self.SaveButton)

        self.deleteButton = PrimaryPushButton(self.layoutWidget1)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)

        self.returnButton = PrimaryPushButton(self.layoutWidget1)
        self.returnButton.setObjectName(u"returnButton")

        self.horizontalLayout.addWidget(self.returnButton)

        self.SaveButton_2 = PrimaryPushButton(self.layoutWidget1)
        self.SaveButton_2.setObjectName(u"SaveButton_2")

        self.horizontalLayout.addWidget(self.SaveButton_2)


        self.retranslateUi(ThingsQuery)

        QMetaObject.connectSlotsByName(ThingsQuery)
    # setupUi

    def retranslateUi(self, ThingsQuery):
        ThingsQuery.setWindowTitle(QCoreApplication.translate("ThingsQuery", u"\u7269\u8d44\u7ba1\u7406\u7cfb\u7edf", None))
        self.queryChildButton.setText(QCoreApplication.translate("ThingsQuery", u"\u67e5\u8be2", None))
        self.lineEdit.setText(QCoreApplication.translate("ThingsQuery", u"\u8bf7\u8f93\u5165\u8981\u67e5\u627e\u7269\u54c1\u7684\u540d\u5b57", None))
        self.SaveButton.setText(QCoreApplication.translate("ThingsQuery", u"\u4fdd\u5b58", None))
        self.deleteButton.setText(QCoreApplication.translate("ThingsQuery", u"\u5220\u9664", None))
        self.returnButton.setText(QCoreApplication.translate("ThingsQuery", u"\u8fd4\u56de", None))
        self.SaveButton_2.setText(QCoreApplication.translate("ThingsQuery", u"\u5bfc\u51fa", None))
    # retranslateUi
