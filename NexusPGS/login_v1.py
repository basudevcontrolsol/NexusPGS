import sys
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: green;")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.lblUsername = QLabel("Username:", self.centralwidget)
        self.lblUsername.setGeometry(50, 50, 100, 30)
        self.lblUsername.setObjectName("lblUsername")
        self.lblUsername.setStyleSheet("color: yellow;")
        self.lblUsername.setFont(QFont("Arial", 12))

        self.txtusername = QLineEdit(self.centralwidget)
        self.txtusername.setGeometry(160, 50, 180, 30)
        self.txtusername.setObjectName("txtusername")

        self.lblPassword = QLabel("Password:", self.centralwidget)
        self.lblPassword.setGeometry(50, 100, 100, 30)
        self.lblPassword.setObjectName("lblPassword")
        self.lblPassword.setStyleSheet("color: yellow;")
        self.lblPassword.setFont(QFont("Arial", 12))

        self.txtpassword = QLineEdit(self.centralwidget)
        self.txtpassword.setGeometry(160, 100, 180, 30)
        self.txtpassword.setEchoMode(QLineEdit.Password)
        self.txtpassword.setObjectName("txtpassword")

        self.lblloginverify = QLabel(self.centralwidget)
        self.lblloginverify.setGeometry(160, 150, 180, 30)
        self.lblloginverify.setObjectName("lblloginverify")
        self.lblloginverify.setStyleSheet("color: yellow;")
        self.lblloginverify.setFont(QFont("Arial", 12))

        self.btnLogin = QPushButton("Login", self.centralwidget)
        self.btnLogin.setGeometry(160, 200, 80, 30)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setStyleSheet("background-color: yellow; color: green;")
        self.btnLogin.clicked.connect(self.login)

        self.btnCancel = QPushButton("Cancel", self.centralwidget)
        self.btnCancel.setGeometry(260, 200, 80, 30)
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.setStyleSheet("background-color: yellow; color: green;")
        self.btnCancel.clicked.connect(self.close)

    def login(self):
        username = self.txtusername.text()
        password = self.txtpassword.text()

        if username and password:
            if username == "admin" and password == "password":
                self.lblloginverify.setText("Valid User")
                # Perform necessary actions on successful login
            else:
                self.lblloginverify.setText("Invalid User !!!")
        else:
            self.lblloginverify.setText("Invalid Username or Password")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec_())
