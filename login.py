from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox
from database import create_connection
from dashboard import Dashboard

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operator Login")
        self.setGeometry(100, 100, 300, 150)
        layout = QVBoxLayout()

        self.user_label = QLabel("Username:")
        self.username_input = QLineEdit()
        layout.addWidget(self.user_label)
        layout.addWidget(self.username_input)

        self.pass_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.pass_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            self.hide()
            self.dashboard = Dashboard()
            self.dashboard.show()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")
