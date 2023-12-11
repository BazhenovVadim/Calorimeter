# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calorimeter.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 468)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
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
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_choose_ration)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_choose_ration = QtWidgets.QGroupBox(self.tab_choose_ration)
        self.groupBox_choose_ration.setTitle("")
        self.groupBox_choose_ration.setObjectName("groupBox_choose_ration")
        self.widget = QtWidgets.QWidget(self.groupBox_choose_ration)
        self.widget.setGeometry(QtCore.QRect(20, 272, 571, 91))
        self.widget.setObjectName("widget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_result = QtWidgets.QLabel(self.widget)
        self.label_result.setObjectName("label_result")
        self.verticalLayout_14.addWidget(self.label_result)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_weight_ration_result = QtWidgets.QLabel(self.widget)
        self.label_weight_ration_result.setObjectName("label_weight_ration_result")
        self.horizontalLayout_12.addWidget(self.label_weight_ration_result)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.label_protein_result = QtWidgets.QLabel(self.widget)
        self.label_protein_result.setObjectName("label_protein_result")
        self.horizontalLayout_12.addWidget(self.label_protein_result)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.label_fats_result = QtWidgets.QLabel(self.widget)
        self.label_fats_result.setObjectName("label_fats_result")
        self.horizontalLayout_12.addWidget(self.label_fats_result)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.label_carb_result = QtWidgets.QLabel(self.widget)
        self.label_carb_result.setObjectName("label_carb_result")
        self.horizontalLayout_12.addWidget(self.label_carb_result)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.label_calories_result = QtWidgets.QLabel(self.widget)
        self.label_calories_result.setObjectName("label_calories_result")
        self.horizontalLayout_12.addWidget(self.label_calories_result)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.listWidget_result_ration = QtWidgets.QListWidget(self.widget)
        self.listWidget_result_ration.setObjectName("listWidget_result_ration")
        self.verticalLayout_12.addWidget(self.listWidget_result_ration)
        self.verticalLayout_14.addLayout(self.verticalLayout_12)
        self.widget1 = QtWidgets.QWidget(self.groupBox_choose_ration)
        self.widget1.setGeometry(QtCore.QRect(20, 80, 571, 181))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_products = QtWidgets.QLabel(self.widget1)
        self.label_products.setObjectName("label_products")
        self.horizontalLayout_10.addWidget(self.label_products)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.label_weight_products = QtWidgets.QLabel(self.widget1)
        self.label_weight_products.setObjectName("label_weight_products")
        self.horizontalLayout_10.addWidget(self.label_weight_products)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.label_calories_products = QtWidgets.QLabel(self.widget1)
        self.label_calories_products.setObjectName("label_calories_products")
        self.horizontalLayout_10.addWidget(self.label_calories_products)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.listWidget_spisok_products = QtWidgets.QListWidget(self.widget1)
        self.listWidget_spisok_products.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_spisok_products.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget_spisok_products.setObjectName("listWidget_spisok_products")
        self.verticalLayout_13.addWidget(self.listWidget_spisok_products)
        self.widget2 = QtWidgets.QWidget(self.groupBox_choose_ration)
        self.widget2.setGeometry(QtCore.QRect(20, 20, 571, 49))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_write_product = QtWidgets.QLabel(self.widget2)
        self.label_write_product.setObjectName("label_write_product")
        self.verticalLayout_10.addWidget(self.label_write_product)
        self.lineEdit_write_product = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_write_product.setObjectName("lineEdit_write_product")
        self.verticalLayout_10.addWidget(self.lineEdit_write_product)
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_write_weight = QtWidgets.QLabel(self.widget2)
        self.label_write_weight.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_write_weight.setObjectName("label_write_weight")
        self.verticalLayout_11.addWidget(self.label_write_weight)
        self.lineEdit_write_weight = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_write_weight.setObjectName("lineEdit_write_weight")
        self.verticalLayout_11.addWidget(self.lineEdit_write_weight)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_18 = QtWidgets.QLabel(self.widget2)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_15.addWidget(self.label_18)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_clear_product = QtWidgets.QPushButton(self.widget2)
        self.pushButton_clear_product.setObjectName("pushButton_clear_product")
        self.horizontalLayout_9.addWidget(self.pushButton_clear_product)
        self.pushButton_add_product = QtWidgets.QPushButton(self.widget2)
        self.pushButton_add_product.setObjectName("pushButton_add_product")
        self.horizontalLayout_9.addWidget(self.pushButton_add_product)
        self.verticalLayout_15.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11.addLayout(self.verticalLayout_15)
        self.horizontalLayout_8.addWidget(self.groupBox_choose_ration)
        self.tabWidget.addTab(self.tab_choose_ration, "")
        self.tab_history_consumption = QtWidgets.QWidget()
        self.tab_history_consumption.setObjectName("tab_history_consumption")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_history_consumption)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_date = QtWidgets.QLabel(self.tab_history_consumption)
        self.label_date.setObjectName("label_date")
        self.horizontalLayout_14.addWidget(self.label_date)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem10)
        self.label_consumed = QtWidgets.QLabel(self.tab_history_consumption)
        self.label_consumed.setObjectName("label_consumed")
        self.horizontalLayout_14.addWidget(self.label_consumed)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem11)
        self.label_daily_norm = QtWidgets.QLabel(self.tab_history_consumption)
        self.label_daily_norm.setObjectName("label_daily_norm")
        self.horizontalLayout_14.addWidget(self.label_daily_norm)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem12)
        self.label_marks = QtWidgets.QLabel(self.tab_history_consumption)
        self.label_marks.setObjectName("label_marks")
        self.horizontalLayout_14.addWidget(self.label_marks)
        self.verticalLayout_16.addLayout(self.horizontalLayout_14)
        self.listWidget_5 = QtWidgets.QListWidget(self.tab_history_consumption)
        self.listWidget_5.setObjectName("listWidget_5")
        self.verticalLayout_16.addWidget(self.listWidget_5)
        self.verticalLayout_17.addLayout(self.verticalLayout_16)
        self.tabWidget.addTab(self.tab_history_consumption, "")
        self.horizontalLayout_13.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.label_result.setText(_translate("MainWindow", "ИТОГО"))
        self.label_weight_ration_result.setText(_translate("MainWindow", "Вес, гр"))
        self.label_protein_result.setText(_translate("MainWindow", "Белки, гр"))
        self.label_fats_result.setText(_translate("MainWindow", "Жиры, гр"))
        self.label_carb_result.setText(_translate("MainWindow", "Углеводы, гр"))
        self.label_calories_result.setText(_translate("MainWindow", "кКал"))
        self.label_products.setText(_translate("MainWindow", "Продукты"))
        self.label_weight_products.setText(_translate("MainWindow", "Вес, гр"))
        self.label_calories_products.setText(_translate("MainWindow", "Калории"))
        self.label_write_product.setText(_translate("MainWindow", "                      Продукт"))
        self.label_write_weight.setText(_translate("MainWindow", "                       Вес, гр"))
        self.pushButton_clear_product.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_add_product.setText(_translate("MainWindow", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_choose_ration), _translate("MainWindow", "Выбор рациона на день"))
        self.label_date.setText(_translate("MainWindow", "Дата"))
        self.label_consumed.setText(_translate("MainWindow", "Потреблено"))
        self.label_daily_norm.setText(_translate("MainWindow", "Суточная норма"))
        self.label_marks.setText(_translate("MainWindow", "Результат"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_history_consumption), _translate("MainWindow", "История потребеления калорий"))
