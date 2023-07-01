import sys
from PyQt5.QtGui import QPixmap, QColor, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget


###
from PyQt5.QtCore import Qt, QRectF, QPointF
from PyQt5.QtGui import QPixmap, QFont, QPainter, QPainterPath, QBitmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget

####



class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: green;")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.lblImage = QLabel(self.centralwidget)
        self.lblImage.setGeometry(160, 10, 200, 80)
        self.lblImage.setObjectName("lblImage")
        self.lblImage.setStyleSheet("color: yellow;")
        self.lblImage.setFont(QFont("Arial", 12))
        pixmap = QPixmap("cps1.jpg")  
        scaled_pixmap = pixmap.scaled(180, 80)
        self.lblImage.setPixmap(scaled_pixmap)

        
        # self.lblImage = RoundedLabel(self.centralwidget)
        # self.lblImage.setGeometry(160, 10, 200, 80)
        # self.lblImage.setObjectName("lblImage")
        # self.lblImage.setStyleSheet("color: yellow;")
        # self.lblImage.setFont(QFont("Arial", 12))
        # pixmap = QPixmap("cps1.jpg")
        # scaled_pixmap = pixmap.scaled(180, 80)
        # self.lblImage.setPixmap(scaled_pixmap)



        self.lblPassword = QLabel("Password:", self.centralwidget)
        self.lblPassword.setGeometry(50, 150, 100, 30)
        self.lblPassword.setObjectName("lblPassword")
        self.lblPassword.setStyleSheet("color: yellow;")
        self.lblPassword.setFont(QFont("Arial", 12))

        self.txtpassword = QLineEdit(self.centralwidget)
        self.txtpassword.setGeometry(160, 150, 180, 30)
        self.txtpassword.setEchoMode(QLineEdit.Password)
        self.txtpassword.setObjectName("txtpassword")



        self.lblUsername = QLabel("Username:", self.centralwidget)
        self.lblUsername.setGeometry(50, 100, 100, 30)
        self.lblUsername.setObjectName("lblUsername")
        self.lblUsername.setStyleSheet("color: yellow;")
        self.lblUsername.setFont(QFont("Arial", 12))

        self.txtusername = QLineEdit(self.centralwidget)
        self.txtusername.setGeometry(160, 100, 180, 30)
        self.txtusername.setObjectName("txtusername")






        self.lblloginverify = QLabel(self.centralwidget)
        self.lblloginverify.setGeometry(160, 200, 180, 30)
        self.lblloginverify.setObjectName("lblloginverify")
        self.lblloginverify.setStyleSheet("color: yellow;")
        self.lblloginverify.setFont(QFont("Arial", 12))

        self.btnLogin = QPushButton("Login", self.centralwidget)
        self.btnLogin.setGeometry(160, 250, 80, 30)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setStyleSheet("background-color: yellow; color: green;")
        self.btnLogin.clicked.connect(self.login)

        self.btnCancel = QPushButton("Cancel", self.centralwidget)
        self.btnCancel.setGeometry(260, 250, 80, 30)
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
