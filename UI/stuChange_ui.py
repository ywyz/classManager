# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stuChange.ui'
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

class Ui_StuChange(object):
    def setupUi(self, StuChange):
        if not StuChange.objectName():
            StuChange.setObjectName(u"StuChange")
        StuChange.resize(1400, 900)
        self.widget = QWidget(StuChange)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 50, 1171, 731))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.queryButton = PrimaryPushButton(self.widget)
        self.queryButton.setObjectName(u"queryButton")

        self.gridLayout.addWidget(self.queryButton, 0, 1, 1, 1)

        self.TableWidget = TableWidget(self.widget)
        self.TableWidget.setObjectName(u"TableWidget")

        self.gridLayout.addWidget(self.TableWidget, 1, 0, 1, 2)

        self.widget1 = QWidget(StuChange)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(420, 810, 471, 51))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.changeButton = PrimaryPushButton(self.widget1)
        self.changeButton.setObjectName(u"changeButton")

        self.horizontalLayout.addWidget(self.changeButton)

        self.deleteButton = PrimaryPushButton(self.widget1)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)

        self.returnButton = PrimaryPushButton(self.widget1)
        self.returnButton.setObjectName(u"returnButton")

        self.horizontalLayout.addWidget(self.returnButton)


        self.retranslateUi(StuChange)

        QMetaObject.connectSlotsByName(StuChange)
    # setupUi

    def retranslateUi(self, StuChange):
        StuChange.setWindowTitle(QCoreApplication.translate("StuChange", u"\u5b66\u7c4d\u7ba1\u7406\u7cfb\u7edf", None))
        self.lineEdit.setText(QCoreApplication.translate("StuChange", u"\u8bf7\u8f93\u5165\u8981\u67e5\u627e\u5e7c\u513f\u7684\u59d3\u540d", None))
        self.queryButton.setText(QCoreApplication.translate("StuChange", u"\u67e5\u8be2", None))
        self.changeButton.setText(QCoreApplication.translate("StuChange", u"\u4fee\u6539", None))
        self.deleteButton.setText(QCoreApplication.translate("StuChange", u"\u5220\u9664", None))
        self.returnButton.setText(QCoreApplication.translate("StuChange", u"\u8fd4\u56de", None))
    # retranslateUi
