from PyQt5 import QtCore, QtGui, QtWidgets

class Password(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Password")

        self.txtOldPassword = QtWidgets.QLineEdit(self)
        self.txtNewPassword = QtWidgets.QLineEdit(self)
        self.txtRetypePassword = QtWidgets.QLineEdit(self)
        self.btnSubmit = QtWidgets.QPushButton("Submit", self)
        self.btnCancel = QtWidgets.QPushButton("Cancel", self)

        self.btnSubmit.clicked.connect(self.submitClicked)
        self.btnCancel.clicked.connect(self.cancelClicked)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel("Old Password"))
        layout.addWidget(self.txtOldPassword)
        layout.addWidget(QtWidgets.QLabel("New Password"))
        layout.addWidget(self.txtNewPassword)
        layout.addWidget(QtWidgets.QLabel("Retype Password"))
        layout.addWidget(self.txtRetypePassword)
        layout.addWidget(self.btnSubmit)
        layout.addWidget(self.btnCancel)
        self.setStyleSheet("background-color: green; color: yellow;")
    def submitClicked(self):
        # Add your password update logic here
        old_password = self.txtOldPassword.text()
        new_password = self.txtNewPassword.text()
        retype_password = self.txtRetypePassword.text()

        if new_password == retype_password:
            # TODO: Perform the password update action

            QtWidgets.QMessageBox.information(self, "Success", "Password updated successfully")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Passwords do not match")

    def cancelClicked(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    password = Password()
    password.show()
    sys.exit(app.exec())
