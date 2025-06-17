from PySide6.QtWidgets import QApplication
from login import LoginWindow
from database import init_db
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    init_db()  
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
