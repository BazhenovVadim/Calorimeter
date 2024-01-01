# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calorimeter.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 468)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setStyleSheet("#MainWindow{border-image:url(back.jpg)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_daily_allowance = QtWidgets.QWidget()
        self.tab_daily_allowance.setObjectName("tab_daily_allowance")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_daily_allowance)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_female = QtWidgets.QGroupBox(self.tab_daily_allowance)
        self.groupBox_female.setTitle("")
        self.groupBox_female.setObjectName("groupBox_female")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_female)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_female = QtWidgets.QLabel(self.groupBox_female)
        self.label_female.setObjectName("label_female")
        self.horizontalLayout_5.addWidget(self.label_female)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_man = QtWidgets.QRadioButton(self.groupBox_female)
        self.radioButton_man.setObjectName("radioButton_man")
        self.verticalLayout_4.addWidget(self.radioButton_man)
        self.radioButton_woman = QtWidgets.QRadioButton(self.groupBox_female)
        self.radioButton_woman.setObjectName("radioButton_woman")
        self.verticalLayout_4.addWidget(self.radioButton_woman)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9.addWidget(self.groupBox_female)
        self.groupBox_description_daily_allowance = QtWidgets.QGroupBox(self.tab_daily_allowance)
        self.groupBox_description_daily_allowance.setTitle("")
        self.groupBox_description_daily_allowance.setObjectName("groupBox_description_daily_allowance")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_description_daily_allowance)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_age = QtWidgets.QLabel(self.groupBox_description_daily_allowance)
        self.label_age.setObjectName("label_age")
        self.verticalLayout_2.addWidget(self.label_age)
        self.label_height = QtWidgets.QLabel(self.groupBox_description_daily_allowance)
        self.label_height.setObjectName("label_height")
        self.verticalLayout_2.addWidget(self.label_height)
        self.label_weight = QtWidgets.QLabel(self.groupBox_description_daily_allowance)
        self.label_weight.setObjectName("label_weight")
        self.verticalLayout_2.addWidget(self.label_weight)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_age = QtWidgets.QLineEdit(self.groupBox_description_daily_allowance)
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.verticalLayout.addWidget(self.lineEdit_age)
        self.lineEdit_height = QtWidgets.QLineEdit(self.groupBox_description_daily_allowance)
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.verticalLayout.addWidget(self.lineEdit_height)
        self.lineEdit_weight = QtWidgets.QLineEdit(self.groupBox_description_daily_allowance)
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.verticalLayout.addWidget(self.lineEdit_weight)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.addWidget(self.groupBox_description_daily_allowance)
        self.groupBox_lifestyle = QtWidgets.QGroupBox(self.tab_daily_allowance)
        self.groupBox_lifestyle.setTitle("")
        self.groupBox_lifestyle.setObjectName("groupBox_lifestyle")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_lifestyle)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_lifestyle = QtWidgets.QLabel(self.groupBox_lifestyle)
        self.label_lifestyle.setObjectName("label_lifestyle")
        self.horizontalLayout.addWidget(self.label_lifestyle)
        self.comboBox_your_lifestyle = QtWidgets.QComboBox(self.groupBox_lifestyle)
        self.comboBox_your_lifestyle.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_your_lifestyle.setAutoFillBackground(False)
        self.comboBox_your_lifestyle.setMaxVisibleItems(15)
        self.comboBox_your_lifestyle.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox_your_lifestyle.setObjectName("comboBox_your_lifestyle")
        self.comboBox_your_lifestyle.addItem("")
        self.comboBox_your_lifestyle.addItem("")
        self.comboBox_your_lifestyle.setItemText(1, "Сидячий и малоподвижный")
        self.comboBox_your_lifestyle.addItem("")
        self.comboBox_your_lifestyle.addItem("")
        self.comboBox_your_lifestyle.addItem("")
        self.comboBox_your_lifestyle.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_your_lifestyle)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout_9.addWidget(self.groupBox_lifestyle)
        self.groupBox_purpose = QtWidgets.QGroupBox(self.tab_daily_allowance)
        self.groupBox_purpose.setTitle("")
        self.groupBox_purpose.setObjectName("groupBox_purpose")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_purpose)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_your_purpose = QtWidgets.QLabel(self.groupBox_purpose)
        self.label_your_purpose.setObjectName("label_your_purpose")
        self.horizontalLayout_2.addWidget(self.label_your_purpose)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_minus_weight = QtWidgets.QRadioButton(self.groupBox_purpose)
        self.radioButton_minus_weight.setObjectName("radioButton_minus_weight")
        self.verticalLayout_3.addWidget(self.radioButton_minus_weight)
        self.radioButton_plus_weight = QtWidgets.QRadioButton(self.groupBox_purpose)
        self.radioButton_plus_weight.setObjectName("radioButton_plus_weight")
        self.verticalLayout_3.addWidget(self.radioButton_plus_weight)
        self.radioButton_save_weight = QtWidgets.QRadioButton(self.groupBox_purpose)
        self.radioButton_save_weight.setObjectName("radioButton_save_weight")
        self.verticalLayout_3.addWidget(self.radioButton_save_weight)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addWidget(self.groupBox_purpose)
        self.groupBox_calculate_or_clear_daily_allowance = QtWidgets.QGroupBox(self.tab_daily_allowance)
        self.groupBox_calculate_or_clear_daily_allowance.setTitle("")
        self.groupBox_calculate_or_clear_daily_allowance.setObjectName("groupBox_calculate_or_clear_daily_allowance")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_calculate_or_clear_daily_allowance)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_clear_daily_allowance = QtWidgets.QPushButton(self.groupBox_calculate_or_clear_daily_allowance)
        self.pushButton_clear_daily_allowance.setObjectName("pushButton_clear_daily_allowance")
        self.horizontalLayout_4.addWidget(self.pushButton_clear_daily_allowance)
        self.pushButton_calculate_daily_allowance = QtWidgets.QPushButton(self.groupBox_calculate_or_clear_daily_allowance)
        self.pushButton_calculate_daily_allowance.setObjectName("pushButton_calculate_daily_allowance")
        self.horizontalLayout_4.addWidget(self.pushButton_calculate_daily_allowance)
        self.verticalLayout_9.addWidget(self.groupBox_calculate_or_clear_daily_allowance)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.listWidget_daily_allowance = QtWidgets.QListWidget(self.tab_daily_allowance)
        self.listWidget_daily_allowance.setObjectName("listWidget_daily_allowance")
        self.horizontalLayout_6.addWidget(self.listWidget_daily_allowance)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_daily_allowance, "")
        self.tab_choose_ration = QtWidgets.QWidget()
        self.tab_choose_ration.setObjectName("tab_choose_ration")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.tab_choose_ration)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.groupBox_choose_ration = QtWidgets.QGroupBox(self.tab_choose_ration)
        self.groupBox_choose_ration.setTitle("")
        self.groupBox_choose_ration.setObjectName("groupBox_choose_ration")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_choose_ration)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_write_product = QtWidgets.QLabel(self.groupBox_choose_ration)
        self.label_write_product.setObjectName("label_write_product")
        self.verticalLayout_10.addWidget(self.label_write_product)
        self.lineEdit_write_product = QtWidgets.QLineEdit(self.groupBox_choose_ration)
        self.lineEdit_write_product.setObjectName("lineEdit_write_product")
        self.verticalLayout_10.addWidget(self.lineEdit_write_product)
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_write_weight = QtWidgets.QLabel(self.groupBox_choose_ration)
        self.label_write_weight.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_write_weight.setObjectName("label_write_weight")
        self.verticalLayout_11.addWidget(self.label_write_weight)
        self.lineEdit_write_weight = QtWidgets.QLineEdit(self.groupBox_choose_ration)
        self.lineEdit_write_weight.setObjectName("lineEdit_write_weight")
        self.verticalLayout_11.addWidget(self.lineEdit_write_weight)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_18 = QtWidgets.QLabel(self.groupBox_choose_ration)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_15.addWidget(self.label_18)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_clear_product = QtWidgets.QPushButton(self.groupBox_choose_ration)
        self.pushButton_clear_product.setObjectName("pushButton_clear_product")
        self.horizontalLayout_9.addWidget(self.pushButton_clear_product)
        self.pushButton_add_product = QtWidgets.QPushButton(self.groupBox_choose_ration)
        self.pushButton_add_product.setObjectName("pushButton_add_product")
        self.horizontalLayout_9.addWidget(self.pushButton_add_product)
        self.verticalLayout_15.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11.addLayout(self.verticalLayout_15)
        self.verticalLayout_19.addLayout(self.horizontalLayout_11)
        self.tableWidget_spisok_products = QtWidgets.QTableWidget(self.groupBox_choose_ration)
        self.tableWidget_spisok_products.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_spisok_products.setDragEnabled(False)
        self.tableWidget_spisok_products.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_spisok_products.setObjectName("tableWidget_spisok_products")
        self.tableWidget_spisok_products.setColumnCount(3)
        self.tableWidget_spisok_products.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_spisok_products.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_spisok_products.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_spisok_products.setHorizontalHeaderItem(2, item)
        self.verticalLayout_19.addWidget(self.tableWidget_spisok_products)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem4)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_choose_ration)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_15.addWidget(self.pushButton_2)
        self.pushButton_table2_clear_all = QtWidgets.QPushButton(self.groupBox_choose_ration)
        self.pushButton_table2_clear_all.setObjectName("pushButton_table2_clear_all")
        self.horizontalLayout_15.addWidget(self.pushButton_table2_clear_all)
        self.verticalLayout_19.addLayout(self.horizontalLayout_15)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_result = QtWidgets.QLabel(self.groupBox_choose_ration)
        self.label_result.setObjectName("label_result")
        self.verticalLayout_14.addWidget(self.label_result)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.tableWidget_result_ration = QtWidgets.QTableWidget(self.groupBox_choose_ration)
        self.tableWidget_result_ration.setMaximumSize(QtCore.QSize(16777215, 120))
        self.tableWidget_result_ration.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget_result_ration.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_result_ration.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_result_ration.setObjectName("tableWidget_result_ration")
        self.tableWidget_result_ration.setColumnCount(5)
        self.tableWidget_result_ration.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result_ration.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result_ration.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result_ration.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result_ration.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result_ration.setHorizontalHeaderItem(4, item)
        self.verticalLayout_12.addWidget(self.tableWidget_result_ration)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem5)
        self.pushButton_table2_add_to_table3 = QtWidgets.QPushButton(self.groupBox_choose_ration)
        self.pushButton_table2_add_to_table3.setObjectName("pushButton_table2_add_to_table3")
        self.horizontalLayout_17.addWidget(self.pushButton_table2_add_to_table3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_17)
        self.verticalLayout_14.addLayout(self.verticalLayout_12)
        self.verticalLayout_19.addLayout(self.verticalLayout_14)
        self.horizontalLayout_16.addLayout(self.verticalLayout_19)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_table2_hide = QtWidgets.QPushButton(self.groupBox_choose_ration)
        self.pushButton_table2_hide.setObjectName("pushButton_table2_hide")
        self.horizontalLayout_13.addWidget(self.pushButton_table2_hide)
        self.pushButton_table2_show = QtWidgets.QPushButton(self.groupBox_choose_ration)
        self.pushButton_table2_show.setObjectName("pushButton_table2_show")
        self.horizontalLayout_13.addWidget(self.pushButton_table2_show)
        self.verticalLayout_18.addLayout(self.horizontalLayout_13)
        self.listWidget_table2_dailynorm = QtWidgets.QListWidget(self.groupBox_choose_ration)
        self.listWidget_table2_dailynorm.setObjectName("listWidget_table2_dailynorm")
        self.verticalLayout_18.addWidget(self.listWidget_table2_dailynorm)
        self.horizontalLayout_16.addLayout(self.verticalLayout_18)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_16)
        self.verticalLayout_20.addWidget(self.groupBox_choose_ration)
        self.tabWidget.addTab(self.tab_choose_ration, "")
        self.tab_history_consumption = QtWidgets.QWidget()
        self.tab_history_consumption.setObjectName("tab_history_consumption")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_history_consumption)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_history_consumption)
        self.tableWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_5.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(4)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        self.verticalLayout_16.addWidget(self.tableWidget_5)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem6)
        self.pushButton_table3_clear_one = QtWidgets.QPushButton(self.tab_history_consumption)
        self.pushButton_table3_clear_one.setObjectName("pushButton_table3_clear_one")
        self.horizontalLayout_18.addWidget(self.pushButton_table3_clear_one)
        self.pushButton_table3_clear_all = QtWidgets.QPushButton(self.tab_history_consumption)
        self.pushButton_table3_clear_all.setObjectName("pushButton_table3_clear_all")
        self.horizontalLayout_18.addWidget(self.pushButton_table3_clear_all)
        self.verticalLayout_16.addLayout(self.horizontalLayout_18)
        self.verticalLayout_17.addLayout(self.verticalLayout_16)
        self.tabWidget.addTab(self.tab_history_consumption, "")
        self.verticalLayout_21.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tableWidget_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_result_ration.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_spisok_products.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калориметр"))
        self.label_female.setText(_translate("MainWindow", "Укажите пол:"))
        self.radioButton_man.setText(_translate("MainWindow", "Мужской"))
        self.radioButton_woman.setText(_translate("MainWindow", "Женский"))
        self.label_age.setText(_translate("MainWindow", "Возраст:"))
        self.label_height.setText(_translate("MainWindow", "Рост, см:"))
        self.label_weight.setText(_translate("MainWindow", "Вес, кг:"))
        self.label_lifestyle.setText(_translate("MainWindow", "Образ жизни:"))
        self.comboBox_your_lifestyle.setItemText(0, _translate("MainWindow", "Ваш образ жизни"))
        self.comboBox_your_lifestyle.setItemText(2, _translate("MainWindow", "Легкая активность(упражнения 1-3 раза в неделю)"))
        self.comboBox_your_lifestyle.setItemText(3, _translate("MainWindow", "Средняя активность(упражнения 3-5 раза в неделю)"))
        self.comboBox_your_lifestyle.setItemText(4, _translate("MainWindow", "Высокая активность(высокие нагрузки каждый день)"))
        self.comboBox_your_lifestyle.setItemText(5, _translate("MainWindow", "Экстремально-высокая нагрузка"))
        self.label_your_purpose.setText(_translate("MainWindow", "Ваша цель:"))
        self.radioButton_minus_weight.setText(_translate("MainWindow", "сбросить вес"))
        self.radioButton_plus_weight.setText(_translate("MainWindow", "набрать вес"))
        self.radioButton_save_weight.setText(_translate("MainWindow", "сохранить вес"))
        self.pushButton_clear_daily_allowance.setText(_translate("MainWindow", "Сбросить"))
        self.pushButton_calculate_daily_allowance.setText(_translate("MainWindow", "Расчитать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_daily_allowance), _translate("MainWindow", "Расчет суточной нормы"))
        self.label_write_product.setText(_translate("MainWindow", " Продукт"))
        self.label_write_weight.setText(_translate("MainWindow", "Вес, гр"))
        self.pushButton_clear_product.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_add_product.setText(_translate("MainWindow", "Добавить"))
        item = self.tableWidget_spisok_products.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Продукты"))
        item = self.tableWidget_spisok_products.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Вес, гр"))
        item = self.tableWidget_spisok_products.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Калории"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить выбранную запись"))
        self.pushButton_table2_clear_all.setText(_translate("MainWindow", "Очистить всё"))
        self.label_result.setText(_translate("MainWindow", "ИТОГО"))
        item = self.tableWidget_result_ration.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Вес, гр"))
        item = self.tableWidget_result_ration.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Белки"))
        item = self.tableWidget_result_ration.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Жиры"))
        item = self.tableWidget_result_ration.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Углеводы"))
        item = self.tableWidget_result_ration.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Калории"))
        self.pushButton_table2_add_to_table3.setText(_translate("MainWindow", "Добавить запись в журнал"))
        self.pushButton_table2_hide.setText(_translate("MainWindow", "Скрыть"))
        self.pushButton_table2_show.setText(_translate("MainWindow", "Показать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_choose_ration), _translate("MainWindow", "Выбор рациона на день"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Потреблено калорий"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Суточная норма"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Результат"))
        self.pushButton_table3_clear_one.setText(_translate("MainWindow", "Удалить выбранную запись"))
        self.pushButton_table3_clear_all.setText(_translate("MainWindow", "Очистить всё"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_history_consumption), _translate("MainWindow", "История потребеления калорий"))
