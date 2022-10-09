# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 700)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.stackedWidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 550, 700))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.file_btn = QtWidgets.QPushButton(self.page_1)
        self.file_btn.setGeometry(QtCore.QRect(400, 210, 100, 40))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.file_btn.setFont(font)
        self.file_btn.setObjectName("file_btn")
        self.label_4 = QtWidgets.QLabel(self.page_1)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 221, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.file_path_text = QtWidgets.QTextEdit(self.page_1)
        self.file_path_text.setGeometry(QtCore.QRect(50, 260, 451, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.file_path_text.setFont(font)
        self.file_path_text.setObjectName("file_path_text")
        self.label_6 = QtWidgets.QLabel(self.page_1)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(50, 380, 221, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_1)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(50, 430, 221, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.start_btn = QtWidgets.QPushButton(self.page_1)
        self.start_btn.setGeometry(QtCore.QRect(350, 580, 150, 60))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        self.exit_btn = QtWidgets.QPushButton(self.page_1)
        self.exit_btn.setGeometry(QtCore.QRect(60, 580, 150, 60))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.label_5 = QtWidgets.QLabel(self.page_1)
        self.label_5.setGeometry(QtCore.QRect(50, 90, 221, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.data_type = QtWidgets.QComboBox(self.page_1)
        self.data_type.setGeometry(QtCore.QRect(220, 100, 121, 31))
        self.data_type.setObjectName("data_type")
        self.data_type.addItem("")
        self.data_type.addItem("")
        self.data_type.addItem("")
        self.data_type.addItem("")
        self.label_8 = QtWidgets.QLabel(self.page_1)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(50, 480, 221, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.presc_sheet = QtWidgets.QComboBox(self.page_1)
        self.presc_sheet.setGeometry(QtCore.QRect(250, 390, 121, 31))
        self.presc_sheet.setObjectName("presc_sheet")
        self.presc_sheet.addItem("")
        self.presc_sheet.addItem("")
        self.presc_sheet.addItem("")
        self.presc_sheet.addItem("")
        self.presc_sheet.addItem("")
        self.drug_sheet = QtWidgets.QComboBox(self.page_1)
        self.drug_sheet.setGeometry(QtCore.QRect(250, 440, 121, 31))
        self.drug_sheet.setObjectName("drug_sheet")
        self.drug_sheet.addItem("")
        self.drug_sheet.addItem("")
        self.drug_sheet.addItem("")
        self.drug_sheet.addItem("")
        self.drug_sheet.addItem("")
        self.ddd_sheet = QtWidgets.QComboBox(self.page_1)
        self.ddd_sheet.setEnabled(True)
        self.ddd_sheet.setGeometry(QtCore.QRect(250, 490, 121, 31))
        self.ddd_sheet.setObjectName("ddd_sheet")
        self.ddd_sheet.addItem("")
        self.ddd_sheet.addItem("")
        self.ddd_sheet.addItem("")
        self.ddd_sheet.addItem("")
        self.ddd_sheet.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.page_1)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 530, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.line_2 = QtWidgets.QFrame(self.page_1)
        self.line_2.setGeometry(QtCore.QRect(10, 50, 530, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.page_2.setFont(font)
        self.page_2.setObjectName("page_2")
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(0, 0, 550, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_id = QtWidgets.QLabel(self.frame)
        self.label_id.setObjectName("label_id")
        self.horizontalLayout_2.addWidget(self.label_id)
        self.id = QtWidgets.QLineEdit(self.frame)
        self.id.setObjectName("id")
        self.horizontalLayout_2.addWidget(self.id)
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_2.addWidget(self.label_22)
        self.dep = QtWidgets.QLineEdit(self.frame)
        self.dep.setObjectName("dep")
        self.horizontalLayout_2.addWidget(self.dep)
        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 20)
        self.horizontalLayout_2.setStretch(2, 10)
        self.horizontalLayout_2.setStretch(3, 44)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_16 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_9.addWidget(self.label_16)
        self.name = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setObjectName("name")
        self.horizontalLayout_9.addWidget(self.name)
        self.label_17 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_9.addWidget(self.label_17)
        self.age = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy)
        self.age.setObjectName("age")
        self.horizontalLayout_9.addWidget(self.age)
        self.label_18 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_9.addWidget(self.label_18)
        self.gender = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy)
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        self.horizontalLayout_9.addWidget(self.gender)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_10.addWidget(self.label_19)
        self.diagnosis = QtWidgets.QTextEdit(self.frame)
        self.diagnosis.setObjectName("diagnosis")
        self.horizontalLayout_10.addWidget(self.diagnosis, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_20 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_11.addWidget(self.label_20)
        self.drug_info = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drug_info.sizePolicy().hasHeightForWidth())
        self.drug_info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.drug_info.setFont(font)
        self.drug_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.drug_info.setRowCount(5)
        self.drug_info.setColumnCount(7)
        self.drug_info.setObjectName("drug_info")
        item = QtWidgets.QTableWidgetItem()
        self.drug_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.drug_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.drug_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.drug_info.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.drug_info.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.drug_info.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.drug_info.setHorizontalHeaderItem(6, item)
        self.horizontalLayout_11.addWidget(self.drug_info)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.progress = QtWidgets.QTextBrowser(self.frame)
        self.progress.setObjectName("progress")
        self.horizontalLayout.addWidget(self.progress)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 2)
        self.verticalLayout.setStretch(6, 3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 530, 29))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.line_3 = QtWidgets.QFrame(self.page_3)
        self.line_3.setGeometry(QtCore.QRect(10, 45, 530, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tabWidget = QtWidgets.QTabWidget(self.page_3)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 550, 650))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(0, 39, 450, 581))
        self.tableView.setObjectName("tableView")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 221, 16))
        self.label_11.setObjectName("label_11")
        self.btn_ok = QtWidgets.QPushButton(self.tab)
        self.btn_ok.setGeometry(QtCore.QRect(460, 120, 71, 41))
        self.btn_ok.setObjectName("btn_ok")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(0, 20, 541, 601))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_6.addWidget(self.label_21)
        self.ddd_drug_info = QtWidgets.QTableWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ddd_drug_info.sizePolicy().hasHeightForWidth())
        self.ddd_drug_info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.ddd_drug_info.setFont(font)
        self.ddd_drug_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ddd_drug_info.setRowCount(1)
        self.ddd_drug_info.setColumnCount(5)
        self.ddd_drug_info.setObjectName("ddd_drug_info")
        item = QtWidgets.QTableWidgetItem()
        self.ddd_drug_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ddd_drug_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ddd_drug_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ddd_drug_info.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ddd_drug_info.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_6.addWidget(self.ddd_drug_info)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.ddd_progress = QtWidgets.QTextBrowser(self.widget)
        self.ddd_progress.setObjectName("ddd_progress")
        self.horizontalLayout_7.addWidget(self.ddd_progress)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.page_3)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "抗菌药物监测上报程序"))
        self.file_btn.setText(_translate("MainWindow", "浏览"))
        self.label_4.setText(_translate("MainWindow", "加载Excel文件："))
        self.file_path_text.setToolTip(_translate("MainWindow", "<html><head/><body><p>请选择待上报的Excel文件</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "请选择处方信息页："))
        self.label_7.setText(_translate("MainWindow", "请选择药品信息页："))
        self.start_btn.setText(_translate("MainWindow", "开始填报"))
        self.exit_btn.setText(_translate("MainWindow", "退出程序"))
        self.label_5.setText(_translate("MainWindow", "选择上报类型："))
        self.data_type.setItemText(0, _translate("MainWindow", "点击选择"))
        self.data_type.setItemText(1, _translate("MainWindow", "门诊处方"))
        self.data_type.setItemText(2, _translate("MainWindow", "急诊处方"))
        self.data_type.setItemText(3, _translate("MainWindow", "DDD"))
        self.label_8.setText(_translate("MainWindow", "请选择 DDD信息页："))
        self.presc_sheet.setItemText(0, _translate("MainWindow", "Sheet1"))
        self.presc_sheet.setItemText(1, _translate("MainWindow", "Sheet2"))
        self.presc_sheet.setItemText(2, _translate("MainWindow", "Sheet3"))
        self.presc_sheet.setItemText(3, _translate("MainWindow", "Sheet4"))
        self.presc_sheet.setItemText(4, _translate("MainWindow", "Sheet5"))
        self.drug_sheet.setItemText(0, _translate("MainWindow", "Sheet1"))
        self.drug_sheet.setItemText(1, _translate("MainWindow", "Sheet2"))
        self.drug_sheet.setItemText(2, _translate("MainWindow", "Sheet3"))
        self.drug_sheet.setItemText(3, _translate("MainWindow", "Sheet4"))
        self.drug_sheet.setItemText(4, _translate("MainWindow", "Sheet5"))
        self.ddd_sheet.setItemText(0, _translate("MainWindow", "Sheet1"))
        self.ddd_sheet.setItemText(1, _translate("MainWindow", "Sheet2"))
        self.ddd_sheet.setItemText(2, _translate("MainWindow", "Sheet3"))
        self.ddd_sheet.setItemText(3, _translate("MainWindow", "Sheet4"))
        self.ddd_sheet.setItemText(4, _translate("MainWindow", "Sheet5"))
        self.label_9.setText(_translate("MainWindow", "首页"))
        self.label_3.setText(_translate("MainWindow", "处方上报页"))
        self.label_id.setText(_translate("MainWindow", "处方ID："))
        self.label_22.setText(_translate("MainWindow", "科室："))
        self.label_16.setText(_translate("MainWindow", "姓名："))
        self.label_17.setText(_translate("MainWindow", "年龄："))
        self.label_18.setText(_translate("MainWindow", "性别："))
        self.gender.setItemText(0, _translate("MainWindow", "男"))
        self.gender.setItemText(1, _translate("MainWindow", "女"))
        self.label_19.setText(_translate("MainWindow", "诊断："))
        self.label_20.setText(_translate("MainWindow", "用药："))
        item = self.drug_info.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "药品名称"))
        item = self.drug_info.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "规格"))
        item = self.drug_info.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "用法"))
        item = self.drug_info.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "剂量"))
        item = self.drug_info.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "频率"))
        item = self.drug_info.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "数量"))
        item = self.drug_info.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "金额"))
        self.label.setText(_translate("MainWindow", "进度："))
        self.label_10.setText(_translate("MainWindow", "DDD上报页"))
        self.label_11.setText(_translate("MainWindow", "请选择开始上报的条目："))
        self.btn_ok.setText(_translate("MainWindow", "确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "选择条目"))
        self.label_21.setText(_translate("MainWindow", "药品："))
        item = self.ddd_drug_info.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "药品名称"))
        item = self.ddd_drug_info.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "规格"))
        item = self.ddd_drug_info.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "用量"))
        item = self.ddd_drug_info.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "单价"))
        item = self.ddd_drug_info.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "金额"))
        self.label_2.setText(_translate("MainWindow", "进度："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "进度"))
