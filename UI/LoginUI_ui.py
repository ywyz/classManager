# -*- coding: utf-8 -*-


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
                               QVBoxLayout, QWidget)

from qfluentwidgets import (CaptionLabel, CheckBox, DisplayLabel, HyperlinkButton,
                            LineEdit, PasswordLineEdit, PrimaryPushButton, PushButton)
import resource.LoginUI_rc


class Ui_Login_UI(QWidget):
    def setupUi(self, Login_UI):
        if not Login_UI.objectName():
            Login_UI.setObjectName(u"Login_UI")
        Login_UI.resize(1400, 900)
        self.login_pic = QLabel(Login_UI)
        self.login_pic.setObjectName(u"login_pic")
        self.login_pic.setGeometry(QRect(0, 0, 831, 1041))
        self.label = QLabel(Login_UI)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(953, 400, 91, 21))
        self.DisplayLabel = DisplayLabel(Login_UI)
        self.DisplayLabel.setObjectName(u"DisplayLabel")
        self.DisplayLabel.setGeometry(QRect(540, 10, 451, 91))
        font = QFont()
        font.setFamilies([u"\u5e7c\u5706"])
        font.setPointSize(26)
        font.setBold(False)
        self.DisplayLabel.setFont(font)
        self.CheckBox = CheckBox(Login_UI)
        self.CheckBox.setObjectName(u"CheckBox")
        self.CheckBox.setGeometry(QRect(910, 500, 211, 61))
        self.label_2 = QLabel(Login_UI)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1010, 70, 200, 200))
        self.layoutWidget = QWidget(Login_UI)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(910, 350, 351, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.UserName_Label = CaptionLabel(self.layoutWidget)
        self.UserName_Label.setObjectName(u"UserName_Label")
        font1 = QFont()
        font1.setFamilies([u"Adobe Heiti Std"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.UserName_Label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.UserName_Label)

        self.UserNameEdit = LineEdit(self.layoutWidget)
        self.UserNameEdit.setObjectName(u"UserNameEdit")

        self.horizontalLayout_2.addWidget(self.UserNameEdit)

        self.layoutWidget1 = QWidget(Login_UI)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(990, 610, 181, 151))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.PrimaryPushButton = PrimaryPushButton(self.layoutWidget1)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")

        self.verticalLayout.addWidget(self.PrimaryPushButton)

        self.HyperlinkButton = HyperlinkButton(self.layoutWidget1)
        self.HyperlinkButton.setObjectName(u"HyperlinkButton")

        self.verticalLayout.addWidget(self.HyperlinkButton)

        self.layoutWidget2 = QWidget(Login_UI)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(920, 440, 341, 35))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.CaptionLabel_2 = CaptionLabel(self.layoutWidget2)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setFont(font1)

        self.horizontalLayout.addWidget(self.CaptionLabel_2)

        self.PasswordLineEdit = PasswordLineEdit(self.layoutWidget2)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")

        self.horizontalLayout.addWidget(self.PasswordLineEdit)

        self.retranslateUi(Login_UI)

        QMetaObject.connectSlotsByName(Login_UI)

    # setupUi

    def retranslateUi(self, Login_UI):
        Login_UI.setWindowTitle(QCoreApplication.translate("Login_UI", u"\u767b\u5f55\u754c\u9762", None))
        self.login_pic.setText(QCoreApplication.translate("Login_UI",
                                                          u"<html><head/><body><p><img src=\":/door/login (\u81ea\u5b9a\u4e49).jpg\"/></p></body></html>",
                                                          None))
        self.label.setText("")
        self.DisplayLabel.setText(QCoreApplication.translate("Login_UI",
                                                             u"\u6b22\u8fce\u4f7f\u7528\u73ed\u7ea7\u4fdd\u6559\u7ba1\u7406\u7cfb\u7edf",
                                                             None))
        self.CheckBox.setText(QCoreApplication.translate("Login_UI", u"\u8bb0\u4f4f\u6211", None))
        self.label_2.setText(QCoreApplication.translate("Login_UI",
                                                        u"<html><head/><body><p><img src=\":/door/logo (\u81ea\u5b9a\u4e49).png\"/></p></body></html>",
                                                        None))
        self.UserName_Label.setText(QCoreApplication.translate("Login_UI", u"\u7528\u6237\u540d\uff1a", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Login_UI", u"\u767b\u5f55", None))
        self.HyperlinkButton.setText(QCoreApplication.translate("Login_UI", u"\u627e\u56de\u5bc6\u7801", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Login_UI", u"\u5bc6\u7801\uff1a", None))
    # retranslateUi
