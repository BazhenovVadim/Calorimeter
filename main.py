import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMainWindow, QCheckBox
from calorimeter_designer import Ui_MainWindow
#from metods_to_calculate import harris_benedict_metod, mifflin_metod


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
        self.bmr_cal_mifflin = None
        self.bmr_cal_harris = None

    def connection_signals(self):
        self.radioButton_man.toggled.connect(self.check_gender)
        self.radioButton_woman.toggled.connect(self.check_gender)
        self.radioButton_plus_weight.toggled.connect(self.get_purpose)
        self.radioButton_minus_weight.toggled.connect(self.get_purpose)
        self.radioButton_save_weight.toggled.connect(self.get_purpose)
        self.pushButton_calculate_daily_allowance.clicked.connect(self.calculate_day_normal)
        self.pushButton_clear_daily_allowance.clicked.connect(self.calculate_day_normal)
        self.comboBox_your_lifestyle.activated.connect(self.get_lifestyle)
        self.lineEdit_age.editingFinished.connect(self.get_age)
        self.lineEdit_height.editingFinished.connect(self.get_height)
        self.lineEdit_weight.editingFinished.connect(self.get_weight)



    def check_gender(self):
        if self.radioButton_man.isChecked():
            self.gender = self.radioButton_man.text()
        if self.radioButton_woman.isChecked():
            self.gender = self.radioButton_woman.text()

    def get_age(self):
        if self.lineEdit_age.editingFinished:
            self.age = int(self.lineEdit_age.text())

    def get_height(self):
        if self.lineEdit_height.editingFinished:
            self.height = int(self.lineEdit_height.text())

    def get_weight(self):
        if self.lineEdit_weight.editingFinished:
            self.weight = int(self.lineEdit_weight.text())

    def get_lifestyle(self):
        self.lifestyle = self.comboBox_your_lifestyle.currentText()
        self.dict_activity = \
            {
                "Сидячий и малоподвижный": "1.2",
                "Легкая активность(упражнения 1-3 раза в неделю)": "1.55",
                "Средняя активность(упражнения 3-5 раза в неделю)": "1.71",
                "Высокая активность(высокие нагрузки каждый день)": "1.95",
                "Экстримально-высокая нагрузка": "2.1"
            }
        self.coof_activity = float(self.dict_activity[self.lifestyle])

    def get_purpose(self):
        if self.radioButton_minus_weight.isChecked():
            self.purpose = self.radioButton_minus_weight.text()
        if self.radioButton_save_weight.isChecked():
            self.purpose = self.radioButton_save_weight.text()
        if self.radioButton_plus_weight.isChecked():
            self.purpose = self.radioButton_plus_weight.text()

    def mifflin_metod(self):
        if self.gender == "Мужской":
            self.bmr_cal_mifflin = \
                str(((10 * self.weiht) + (6.25 * self.height) - (5 * self.age) + 5) * self.coof_activity)
            return self.bmr_cal_mifflin
        if self.gender == "Женский":
            self.bmr_cal_mifflin = \
                str(((10 * self.weiht) + (6.25 * self.height) - (5 * self.age) - 161) * self.coof_activity)
            return self.bmr_cal_mifflin

    def harris_benedict_metod(self):
        if self.gender == "Мужской":
            self.bmr_cal_harris = \
                str(((13.7516 * self.weiht) + (5.0033 * self.height) -
                     (6.755 * self.age) + 66.473) * self.coof_activity)
            return self.bmr_cal_harris
        if self.gender == "Женский":
            self. bmr_cal_harris = \
                str(((9.5634 * self.weiht) + (1.8496 * self.height) -
                     (4.6756 * self.age) + 655.0955) * self.coof_activity)
            return self.bmr_cal_harris

    def calculate_day_normal(self):
        if self.pushButton_calculate_daily_allowance.clicked:
            self.listWidget_daily_allowance.clear()
            self.listWidget_daily_allowance.addItem("Рассчет суточной нормы калорий : \n")
            self.listWidget_daily_allowance.addItem(f"По формуле Харриса-Бенедикта {self.bmr_cal_harris}")
            self.listWidget_daily_allowance.addItem(f"По формуле Миффлина-Сан Жеора {self.bmr_cal_mifflin}")
            print(self.lifestyle, self.age, self.coof_activity, self.weight, self.height, self.gender, self.purpose)

#TODO: решить проблему с self.bmr и его выводом на экран. Добавить очистку первого таба. Открывать прогу с 1 таба.
#TODO: запретить пользователю вводить пустые поля(диалоговое окно). Добавить к расчету цель(похудеть, набрать)

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
