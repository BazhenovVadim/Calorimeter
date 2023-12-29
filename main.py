import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, \
    QMessageBox

from data_base import *
from ui_files.calorimeter_designer import Ui_MainWindow


# from metods_to_calculate import harris_benedict_metod, mifflin_metod


class Calorimeter(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection_signals()
        self.age = None
        self.weight = None
        self.height = None
        self.lifestyle = None
        self.gender = None
        self.purpose = None
        self.coof_activity = None
        self.coof_by_purpose = None
        self.bmr_cal_mifflin = None
        self.bmr_cal_harris = None
        self.name_product = None
        self.weight_product = None
        self.calories = None
        self.recomend_text = None
        self.weight_result = 0
        self.proteins_result = 0
        self.fats_result = 0
        self.carbs_result = 0
        self.calories_result = 0
        self.tabWidget.setCurrentWidget(self.tab_daily_allowance)
        self.groop_radiobutton_gender = QButtonGroup()
        self.groop_radiobutton_gender.addButton(self.radioButton_man)
        self.groop_radiobutton_gender.addButton(self.radioButton_woman)
        self.groop_radiobutton_purpose = QButtonGroup()
        self.groop_radiobutton_purpose.addButton(self.radioButton_minus_weight)
        self.groop_radiobutton_purpose.addButton(self.radioButton_plus_weight)
        self.groop_radiobutton_purpose.addButton(self.radioButton_save_weight)

    def connection_signals(self):
        self.radioButton_man.toggled.connect(self.check_gender)
        self.radioButton_woman.toggled.connect(self.check_gender)
        self.radioButton_plus_weight.toggled.connect(self.get_purpose)
        self.radioButton_minus_weight.toggled.connect(self.get_purpose)
        self.radioButton_save_weight.toggled.connect(self.get_purpose)
        self.pushButton_calculate_daily_allowance.clicked.connect(self.calculate_day_normal)
        self.pushButton_clear_daily_allowance.clicked.connect(self.clear_settings_day_normal)
        self.comboBox_your_lifestyle.activated.connect(self.get_lifestyle)
        self.lineEdit_age.editingFinished.connect(self.get_age)
        self.lineEdit_height.editingFinished.connect(self.get_height)
        self.lineEdit_weight.editingFinished.connect(self.get_weight)
        self.lineEdit_write_product.editingFinished.connect(self.get_name_product)
        self.lineEdit_write_weight.editingFinished.connect(self.get_weight_product)
        self.pushButton_add_product.clicked.connect(self.add_product_to_list)
        self.pushButton_clear_product.clicked.connect(self.clear_data_in_lineEdit)
        self.pushButton_2.clicked.connect(self.clear_products_list)
        self.pushButton_table2_clear_all.clicked.connect(self.clear_all_products)
        self.pushButton_add_product.clicked.connect(self.add_result_list)
        self.pushButton_table2_clear_all.clicked.connect(self.clear_result_list_after_clear_all)
        self.pushButton_2.clicked.connect(self.clear_result_list_after_one_clear)
        self.pushButton_table2_hide.clicked.connect(self.hide_list)
        self.pushButton_table2_show.clicked.connect(self.show_list)

    def check_gender(self):
        if self.radioButton_man.isChecked():
            self.gender = self.radioButton_man.text()
        if self.radioButton_woman.isChecked():
            self.gender = self.radioButton_woman.text()

    def get_age(self):
        if self.lineEdit_age.text().isdigit() and self.lineEdit_age.text() != "":
            self.age = int(self.lineEdit_age.text())
        else:
            self.dialog_age = QMessageBox.critical(self, "Трудный возраст",
                                                   "Поле не может быть пустым или содержать буквы")
            self.lineEdit_age.clear()
            self.age = None

    def get_height(self):
        if self.lineEdit_height.text().isdigit() and self.lineEdit_height.text() != "":
            self.height = int(self.lineEdit_height.text())
        else:
            self.dialog_height = QMessageBox.critical(self, "Рост", "Поле не может быть пустым или содержать буквы")
            self.lineEdit_height.clear()
            self.height = None

    def get_weight(self):
        if self.lineEdit_weight.text().isdigit() and self.lineEdit_weight.text() != "":
            self.weight = int(self.lineEdit_weight.text())
        else:
            self.dialog_weight = QMessageBox.critical(self, "Трудный возраст",
                                                      "Поле не может быть пустым или содержать буквы")
            self.lineEdit_weight.clear()
            self.weight = None

    def get_lifestyle(self):
        self.lifestyle = self.comboBox_your_lifestyle.currentText()
        self.dict_activity = \
            {
                "Сидячий и малоподвижный": "1.2",
                "Легкая активность(упражнения 1-3 раза в неделю)": "1.55",
                "Средняя активность(упражнения 3-5 раза в неделю)": "1.71",
                "Высокая активность(высокие нагрузки каждый день)": "1.95",
                "Экстремально-высокая нагрузка": "2.1"
            }

        self.coof_activity = float(self.dict_activity[self.lifestyle])

    def get_purpose(self):
        if self.radioButton_minus_weight.isChecked():
            self.purpose = self.radioButton_minus_weight.text()
        if self.radioButton_save_weight.isChecked():
            self.purpose = self.radioButton_save_weight.text()
        if self.radioButton_plus_weight.isChecked():
            self.purpose = self.radioButton_plus_weight.text()

        self.dict_purpose_cal = \
            {
                "сбросить вес": -500,
                "набрать вес": 300,
                "сохранить вес": 0,
            }
        self.dict_for_list = \
            {
                "сбросить вес": "Рекомендации для потери веса :",
                "набрать вес": "Рекомендации для набора веса :",
                "сохранить вес": "Рекомендации для сохранения веса :",
            }
        self.dict_protein = \
            {
                "сбросить вес": 1.5,
                "набрать вес": 2.5,
                "сохранить вес": 1.1,
            }
        self.dict_carbs = \
            {
                "сбросить вес": 1.5,
                "набрать вес": 4,
                "сохранить вес": 3,
            }
        self.dict_fats = \
            {
                "сбросить вес": 1,
                "набрать вес": 2,
                "сохранить вес": 1.5,
            }
        self.recomend_text = self.dict_for_list[self.purpose]
        if self.weight:
            self.protein = self.weight * self.dict_protein[self.purpose]
            self.carbs = self.weight * self.dict_carbs[self.purpose]
            self.fats = self.weight * 0.5
            self.coof_by_purpose = self.dict_purpose_cal[self.purpose]
        else:
            self.dialog_weight = QMessageBox.critical(self, "Не могу рассчитать параметры",
                                                      "Заполни все предыдущие поля")

    def calculate_day_normal(self):
        if self.pushButton_calculate_daily_allowance.clicked:
            print(self.lifestyle, self.age, self.coof_activity, self.weight, self.height, self.gender, self.purpose,
                  self.coof_by_purpose)
            if (self.age is None or self.weight is None or self.height is None or self.lifestyle is None or
                    self.gender is None or self.purpose is None or self.coof_activity is None or self.coof_by_purpose is None):
                self.dialog = QMessageBox.critical(self, "Ошибка", "Заполните все поля")
            else:
                if self.gender == "Мужской":
                    self.bmr_cal_mifflin = \
                        str(int(((10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5) * self.coof_activity))
                    self.bmr_cal_harris = \
                        str(int(((13.7516 * self.weight) + (5.0033 * self.height) -
                                 (6.755 * self.age) + 66.473) * self.coof_activity))
                if self.gender == "Женский":
                    self.bmr_cal_mifflin = \
                        str(int(
                            ((10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161) * self.coof_activity))
                    self.bmr_cal_harris = \
                        str(int(((9.5634 * self.weight) + (1.8496 * self.height) -
                                 (4.6756 * self.age) + 655.0955) * self.coof_activity))
                self.listWidget_table2_dailynorm.clear()
                self.listWidget_daily_allowance.clear()
                self.listWidget_daily_allowance.addItem("Рассчет суточной нормы калорий : \n")
                self.listWidget_daily_allowance.addItem(f"По формуле Харриса-Бенедикта : \n {self.bmr_cal_harris} ккал")
                self.listWidget_daily_allowance.addItem(
                    f"По формуле Миффлина-Сан Жеора : \n {self.bmr_cal_mifflin} ккал \n")
                self.listWidget_daily_allowance.addItem(self.recomend_text + "\n")
                self.listWidget_daily_allowance.addItem("Суточная норма калорий" +
                                                        str(int(self.bmr_cal_mifflin) - self.coof_by_purpose))
                self.listWidget_daily_allowance.addItem(f"белков {self.protein}")
                self.listWidget_daily_allowance.addItem(f"жиров {self.fats}")
                self.listWidget_daily_allowance.addItem(f"углеводов {self.carbs}")

    def clear_settings_day_normal(self):
        if self.pushButton_clear_daily_allowance.clicked:
            self.groop_radiobutton_gender.setExclusive(False)
            self.radioButton_man.setChecked(False)
            self.radioButton_woman.setChecked(False)
            self.groop_radiobutton_gender.setExclusive(True)
            self.lineEdit_age.clear()
            self.lineEdit_height.clear()
            self.lineEdit_weight.clear()
            self.comboBox_your_lifestyle.setCurrentIndex(0)
            self.groop_radiobutton_purpose.setExclusive(False)
            self.radioButton_minus_weight.setChecked(False)
            self.radioButton_plus_weight.setChecked(False)
            self.radioButton_save_weight.setChecked(False)
            self.groop_radiobutton_purpose.setExclusive(True)
            self.age = None
            self.weight = None
            self.height = None
            self.lifestyle = None
            self.gender = None
            self.purpose = None
            self.coof_activity = None
            self.coof_by_purpose = None
            self.bmr_cal_mifflin = None
            self.bmr_cal_harris = None

    def get_name_product(self):
        if self.lineEdit_write_product.text() != "":
            self.name_product = self.lineEdit_write_product.text().strip().capitalize()
        if self.lineEdit_write_product.text() == "":
            self.dialog_weight_product = QMessageBox.critical(self, "Продукты", "Введите корректное название")
            self.lineEdit_write_weight.clear()
            self.name_product = None

    def get_weight_product(self):
        if self.lineEdit_write_weight.text() != "" and str(self.lineEdit_write_weight.text()).strip().isdigit():
            self.weight_product = int(self.lineEdit_write_weight.text().strip())
        if (self.lineEdit_write_weight.text() == "") or (self.lineEdit_write_weight.text().isdigit() == False):
            self.dialog_weight_product = QMessageBox.critical(self, "Вес продукта", "Введите корректный вес")
            self.lineEdit_write_weight.clear()
            self.weight_product = None

    def get_calories(self):
        session = session_factory()
        if (self.name_product is None) or self.name_product == '':
            self.dialog_weight_product = QMessageBox.critical(self, "Продукты", "Забыли ввести параметры")
            self.lineEdit_write_weight.clear()
        else:
            product = session.query(Products).where(Products.product_name == self.name_product).first()
            self.calories = product.calories * (self.weight_product / 100)

    def add_product_to_list(self):
        session = session_factory()

        self.products_in_database = session.query(Products).all()
        self.products = [str(x) for x in self.products_in_database]

        if self.pushButton_add_product.clicked and (self.name_product in self.products) and (
                self.weight_product is not None) and (self.name_product is not None):
            if len(str(int(self.weight_product))) < 5:
                product = session.query(Products).where(Products.product_name == self.name_product).first()
                self.calories = product.calories * (self.weight_product / 100)
                if len(self.name_product) > 3 and len(self.name_product) <= 10:
                    self.listWidget_spisok_products.addItem(
                        self.name_product + '-' * (35 - len(self.name_product)) + str(self.weight_product) + '-' * (
                                37 - len(str(self.calories))) + str(self.calories))
                if len(self.name_product) <= 3:
                    self.listWidget_spisok_products.addItem(
                        self.name_product + '-' * (37 - len(self.name_product)) + str(self.weight_product) + '-' * (
                                37 - len(str(self.calories))) + str(self.calories))
                if len(self.name_product) > 10 and len(self.name_product) <= 15:
                    self.listWidget_spisok_products.addItem(
                        self.name_product + '-' * (33 - len(self.name_product)) + str(self.weight_product) + '-' * (
                                37 - len(str(self.calories))) + str(self.calories))
                if len(self.name_product) > 15:
                    self.listWidget_spisok_products.addItem(
                        self.name_product + '-' * (29 - len(self.name_product)) + str(self.weight_product) + '-' * (
                                37 - len(str(self.calories))) + str(self.calories))

        else:
            self.dialog_add_product = QMessageBox.critical(self, "Продукты", "Вы что-то не то ввели")
            self.lineEdit_write_product.clear()
            self.name_product = None

    def clear_data_in_lineEdit(self):
        if self.pushButton_clear_product.clicked:
            self.lineEdit_write_product.clear()
            self.lineEdit_write_weight.clear()
            self.name_product = None
            self.weight_product = None

    def clear_products_list(self):
        if self.pushButton_2.clicked:
            if not self.listWidget_spisok_products.selectedItems():
                dialog_row = QMessageBox.critical(self, "Нельзя удалить",
                                                  "Выберите хотя бы одну строку или добавьте продукт")
            current_row = self.listWidget_spisok_products.currentRow()
            if current_row >= 0:
                current_item = self.listWidget_spisok_products.takeItem(current_row)
                del current_item

    def clear_all_products(self):
        if self.pushButton_table2_clear_all.clicked:
            self.listWidget_spisok_products.clear()
            self.weight_result = 0
            self.proteins_result = 0
            self.fats_result = 0
            self.carbs_result = 0
            self.calories_result = 0

    def add_result_list(self):
        session = session_factory()

        if self.pushButton_add_product.clicked and self.name_product is not None and self.name_product != '':
            product = session.query(Products).where(Products.product_name == self.name_product).first()
            self.weight_result += self.weight_product
            self.proteins_result += product.proteins * (self.weight_product / 100)
            self.fats_result += product.fats * (self.weight_product / 100)
            self.carbs_result += product.carbs * (self.weight_product / 100)
            self.calories_result += product.calories * (self.weight_product / 100)
            self.listWidget_result_ration.clear()
            if len(str(int(self.weight_product))) <= 3:
                self.listWidget_result_ration.addItem(
                    str(round(self.weight_result, 1)) + ' ' * 17 + str(round(self.proteins_result, 1)) + ' ' * 22 + str(
                        round(self.fats_result, 1)) + ' ' * 22 + str(round(self.carbs_result, 1)) + ' ' * 23 + str(
                        round(self.calories_result, 1)))
            if len(str(int(self.weight_product))) >= 5:
                self.dialog_result_list = QMessageBox.critical(self, "Ваш рацион",
                                                               "Похоже, вы умерли от переедания")
                self.listWidget_result_ration.clear()
                self.weight_result = 0
                self.proteins_result = 0
                self.fats_result = 0
                self.carbs_result = 0
                self.calories_result = 0
                self.lineEdit_write_weight.clear()
                self.weight_product = None
        session.close()

    def clear_result_list_after_clear_all(self):
        if self.pushButton_table2_clear_all.clicked:
            self.listWidget_result_ration.clear()

    def clear_result_list_after_one_clear(self):
        session = session_factory()
        product = session.query(Products).where(Products.product_name == self.name_product).first()
        self.list = [self.listWidget_spisok_products.item for x in range(self.listWidget_spisok_products.count())]

        if self.pushButton_2.clicked and len(self.list) > 0:
            self.listWidget_result_ration.clear()
            self.weight_result -= self.weight_product
            self.proteins_result -= product.proteins * (self.weight_product / 100)
            self.fats_result -= product.fats * (self.weight_product / 100)
            self.carbs_result -= product.carbs * (self.weight_product / 100)
            self.calories_result -= product.calories * (self.weight_product / 100)
            print(self.weight_result, self.proteins_result)

            print(*self.list)
            if len(str(int(self.weight_product))) <= 4:
                self.listWidget_result_ration.addItem(
                    str(round(self.weight_result, 1)) + ' ' * 17 + str(round(self.proteins_result, 1)) + ' ' * 22 + str(
                        round(self.fats_result, 1)) + ' ' * 22 + str(round(self.carbs_result, 1)) + ' ' * 23 + str(
                        round(self.calories_result, 1)))
            else:
                self.dialog_result_list = QMessageBox.critical(self, "Ваш рацион",
                                                               "Похоже, вы умерли от переедания")
            if self.weight_result == 0:
                self.listWidget_result_ration.clear()
        else:
            self.listWidget_result_ration.clear()

    def show_list(self):
        if self.pushButton_table2_show.clicked:

            if (self.age is None or self.weight is None or self.height is None or self.lifestyle is None or
                    self.gender is None or self.purpose is None or self.coof_activity is None or self.coof_by_purpose is None):
                self.dialog = QMessageBox.critical(self, "Ошибка", "Заполните все поля")

            else:
                self.listWidget_table2_dailynorm.clear()
                self.listWidget_table2_dailynorm.addItem("Рассчет суточной нормы калорий : \n")
                self.listWidget_table2_dailynorm.addItem(
                    f"По формуле Харриса-Бенедикта : \n {self.bmr_cal_harris} ккал")
                self.listWidget_table2_dailynorm.addItem(
                    f"По формуле Миффлина-Сан Жеора : \n {self.bmr_cal_mifflin} ккал \n")
                self.listWidget_table2_dailynorm.addItem(self.recomend_text + "\n")
                self.listWidget_table2_dailynorm.addItem("Суточная норма калорий" +
                                                         str(int(self.bmr_cal_mifflin) - self.coof_by_purpose))
                self.listWidget_table2_dailynorm.addItem(f"белков {self.protein}")
                self.listWidget_table2_dailynorm.addItem(f"жиров {self.fats}")
                self.listWidget_table2_dailynorm.addItem(f"углеводов {self.carbs}")

    def hide_list(self):
        if self.pushButton_table2_hide.clicked:
            if (self.age is None or self.weight is None or self.height is None or self.lifestyle is None or
                    self.gender is None or self.purpose is None or self.coof_activity is None or self.coof_by_purpose is None):
                self.dialog = QMessageBox.critical(self, "Ошибка", "Заполните все поля")

            else:
                self.listWidget_table2_dailynorm.clear()



# TODO привязать кнопки спрятать показать для листа с суточной нормой
# TODO добавить диалоговое окно с предложение заменить если его нет но название похоже. Диалог окно что все поля должны быть заполнены
#
sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calorimeter()
    ex.show()
    sys.exit(app.exec())
