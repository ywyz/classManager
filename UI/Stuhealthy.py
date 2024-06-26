# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/yw980/code/classManager/UI/Stuhealthy.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from Functions.SQLConnect import SQLConnect
import os


class Ui_StuHealthy(object):
    def setupUi(self, StuHealthy):
        StuHealthy.setObjectName("StuHealthy")
        StuHealthy.resize(1581, 900)
        self.widget = QtWidgets.QWidget(StuHealthy)
        self.widget.setGeometry(QtCore.QRect(421, 819, 551, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SaveButton = PrimaryPushButton(self.widget)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout.addWidget(self.SaveButton)
        self.changeButton = PrimaryPushButton(self.widget)
        self.changeButton.setObjectName("changeButton")
        self.horizontalLayout.addWidget(self.changeButton)
        self.returnButton = PrimaryPushButton(self.widget)
        self.returnButton.setObjectName("returnButton")
        self.horizontalLayout.addWidget(self.returnButton)
        self.SaveButton_2 = PrimaryPushButton(self.widget)
        self.SaveButton_2.setObjectName("SaveButton_2")
        self.horizontalLayout.addWidget(self.SaveButton_2)
        self.widget1 = QtWidgets.QWidget(StuHealthy)
        self.widget1.setGeometry(QtCore.QRect(150, 30, 1251, 721))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.YearBox = SpinBox(self.widget1)
        self.YearBox.setMinimum(2020)
        self.YearBox.setMaximum(3096)
        self.YearBox.setProperty("value", 2024)
        self.YearBox.setObjectName("YearBox")
        self.horizontalLayout_2.addWidget(self.YearBox)
        self.queryYearButton = PrimaryPushButton(self.widget1)
        self.queryYearButton.setObjectName("queryYearButton")
        self.horizontalLayout_2.addWidget(self.queryYearButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.queryChildButton = PrimaryPushButton(self.widget1)
        self.queryChildButton.setObjectName("queryChildButton")
        self.horizontalLayout_3.addWidget(self.queryChildButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.TableWidget = TableWidget(self.widget1)
        self.TableWidget.setObjectName("TableWidget")
        self.TableWidget.setColumnCount(0)
        self.TableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.TableWidget, 1, 0, 1, 2)

        self.retranslateUi(StuHealthy)
        self.queryYearButton.clicked.connect(self.loadData)
        QtCore.QMetaObject.connectSlotsByName(StuHealthy)

    def retranslateUi(self, StuHealthy):
        _translate = QtCore.QCoreApplication.translate
        StuHealthy.setWindowTitle(_translate("StuHealthy", "学生体检管理系统"))
        self.SaveButton.setText(_translate("StuHealthy", "保存"))
        self.changeButton.setText(_translate("StuHealthy", "修改"))
        self.returnButton.setText(_translate("StuHealthy", "返回"))
        self.SaveButton_2.setText(_translate("StuHealthy", "导出"))
        self.queryYearButton.setText(_translate("StuHealthy", "查询"))
        self.lineEdit.setText(_translate("StuHealthy", "请输入要查找幼儿的姓名"))
        self.queryChildButton.setText(_translate("StuHealthy", "查询"))

    def handleItemChanged(self, item):
        self.column_to_field = {
            '年度': 'date',
            '学号': 'stu_id',
            '幼儿姓名': 'stu_name',
            '身高': 'stu_height',
            '体重': 'stu_weight',
            '左眼视力': 'stu_visionleft',
            '右眼视力': 'stu_visionright',
            '血红蛋白': 'stu_hmoglobin'
        }
        # 获取修改后的值
        new_value = item.text()
        # 获取行和列
        row = item.row()
        stu_id = self.TableWidget.item(row, 1).text()  # 假设学号在第二列
        date = self.TableWidget.item(row, 0).text()  # 假设日期在第一列
        column = item.column()
        column_name = self.TableWidget.horizontalHeaderItem(column).text()  # 获取列名
        field = self.column_to_field[column_name]  # 获取对应的字段名

        # 创建SQL连接
        sql = SQLConnect(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'])
        sql.connect()

        # 构建更新语句
        update_query = f"UPDATE StudentHealthy SET {field} = '{new_value}' WHERE date = '{date}' AND stu_id = '{stu_id}'"
        sql.execute(update_query)
        sql.commit()  # 提交事务
    def loadData(self):
        sql = SQLConnect(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'])
        sql.connect()
        self.date = self.YearBox.value()

        query = f"select * from StudentHealthy where date = '{self.date}'"
        results = sql.execute(query)
        self.TableWidget.itemChanged.connect(self.handleItemChanged)
        print(f"StudentHealthy results: {results}")  # 打印查询结果以进行检查
        if not results:
            query = f"select stu_id, stu_name from StudentData"
            results = sql.execute(query)
            for result in results:
                result_dict = dict(result)  # 将结果转换为字典
                insert_query = f"""
                insert into StudentHealthy (date, class_name, stu_name, stu_id, stu_height, stu_weight, stu_visionleft, stu_visionright, stu_hmoglobin)
                values ('{self.date}','中二','{result_dict['stu_name']}', '{result_dict['stu_id']}', 100.0, 20.0, 1.0, 1.0, 130.0)"""
                sql.execute(insert_query)
                sql.commit()  # 提交事务

        query = f"select * from StudentDailyAttend where date = '{self.date}'"
        results = sql.execute(query)
        print(f"Updated StudentDailyAttend results: {results}")  # 打印更新后的查询结果以进行检查
        keys = [ 'date', 'stu_id', 'stu_name', 'stu_height', 'stu_weight', 'stu_visionleft', 'stu_visionright', 'stu_hmoglobin']

        query = f"select * from StudentHealthy where date = '{self.date}'"
        results = sql.execute(query)
        print(f"StudentHealthy results: {results}")  # 打印查询结果以进行检查

        # 检查查询结果是否为空
        if not results:
            print("No results found for the given date.")
            return

        # 设置表格的行数和列数
        self.TableWidget.setRowCount(len(results))
        self.TableWidget.setColumnCount(len(keys))

        # 填充表格数据
        for i, result in enumerate(results):
            for j, key in enumerate(keys):
                value = result.get(key)
                if value is not None:
                    self.TableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        self.TableWidget.viewport().update()  # 刷新表格
        print("TableWidget updated")  # 打印表格更新信息
from qfluentwidgets import PrimaryPushButton, SpinBox, TableWidget
