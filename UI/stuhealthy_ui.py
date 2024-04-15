# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stuhealthy.ui'
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

from qfluentwidgets import (PrimaryPushButton, PushButton, SpinBox, TableWidget)

class Ui_StuHealthy(object):
    def setupUi(self, StuHealthy):
        if not StuHealthy.objectName():
            StuHealthy.setObjectName(u"StuHealthy")
        StuHealthy.resize(1581, 900)
        self.widget = QWidget(StuHealthy)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(421, 819, 551, 51))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SaveButton = PrimaryPushButton(self.widget)
        self.SaveButton.setObjectName(u"SaveButton")

        self.horizontalLayout.addWidget(self.SaveButton)

        self.changeButton = PrimaryPushButton(self.widget)
        self.changeButton.setObjectName(u"changeButton")

        self.horizontalLayout.addWidget(self.changeButton)

        self.returnButton = PrimaryPushButton(self.widget)
        self.returnButton.setObjectName(u"returnButton")

        self.horizontalLayout.addWidget(self.returnButton)

        self.SaveButton_2 = PrimaryPushButton(self.widget)
        self.SaveButton_2.setObjectName(u"SaveButton_2")

        self.horizontalLayout.addWidget(self.SaveButton_2)

        self.widget1 = QWidget(StuHealthy)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(150, 30, 1251, 721))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.YearBox = SpinBox(self.widget1)
        self.YearBox.setObjectName(u"YearBox")
        self.YearBox.setMinimum(2020)
        self.YearBox.setMaximum(2048)
        self.YearBox.setValue(2024)

        self.horizontalLayout_2.addWidget(self.YearBox)

        self.queryYearButton = PrimaryPushButton(self.widget1)
        self.queryYearButton.setObjectName(u"queryYearButton")

        self.horizontalLayout_2.addWidget(self.queryYearButton)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.queryChildButton = PrimaryPushButton(self.widget1)
        self.queryChildButton.setObjectName(u"queryChildButton")

        self.horizontalLayout_3.addWidget(self.queryChildButton)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.TableWidget = TableWidget(self.widget1)
        self.TableWidget.setObjectName(u"TableWidget")

        self.gridLayout.addWidget(self.TableWidget, 1, 0, 1, 2)


        self.retranslateUi(StuHealthy)

        QMetaObject.connectSlotsByName(StuHealthy)
    # setupUi

    def retranslateUi(self, StuHealthy):
        StuHealthy.setWindowTitle(QCoreApplication.translate("StuHealthy", u"\u5b66\u751f\u4f53\u68c0\u7ba1\u7406\u7cfb\u7edf", None))
        self.SaveButton.setText(QCoreApplication.translate("StuHealthy", u"\u4fdd\u5b58", None))
        self.changeButton.setText(QCoreApplication.translate("StuHealthy", u"\u4fee\u6539", None))
        self.returnButton.setText(QCoreApplication.translate("StuHealthy", u"\u8fd4\u56de", None))
        self.SaveButton_2.setText(QCoreApplication.translate("StuHealthy", u"\u5bfc\u51fa", None))
        self.queryYearButton.setText(QCoreApplication.translate("StuHealthy", u"\u67e5\u8be2", None))
        self.lineEdit.setText(QCoreApplication.translate("StuHealthy", u"\u8bf7\u8f93\u5165\u8981\u67e5\u627e\u5e7c\u513f\u7684\u59d3\u540d", None))
        self.queryChildButton.setText(QCoreApplication.translate("StuHealthy", u"\u67e5\u8be2", None))
    # retranslateUi

