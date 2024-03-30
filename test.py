import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import requests


class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Login')
        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText('Username')
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText('Password')
        layout.addWidget(self.password_input)

        login_button = QPushButton('Login', self)
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        response = requests.post("http://127.0.0.1:8000/token", data={"username": username, "password": password})

        if response.status_code == 200:
            token = response.json().get("access_token")
            user_response = requests.get("http://127.0.0.1:8000/user/get_user_id",
                                         headers={"Authorization": f"Bearer {token}"})
            if user_response.status_code == 200:
                current_user = int(user_response.content)
                self.result_label.setText(f"Current User ID: {current_user}")
            else:
                self.result_label.setText("Failed to get current user")
        else:
            self.result_label.setText("Login failed")


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()
    sys.exit(app.exec_())
