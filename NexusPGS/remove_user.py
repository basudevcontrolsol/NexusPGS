# from PyQt5 import QtCore, QtGui, QtWidgets

# class RemoveUser(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()

#     def setupUi(self):
#         self.setWindowTitle("Remove User")

#         self.cboGroup = QtWidgets.QComboBox(self)
#         self.txtUserName = QtWidgets.QLineEdit(self)
#         self.btnSuspend = QtWidgets.QPushButton("Suspend", self)
#         self.btnCancel = QtWidgets.QPushButton("Cancel", self)

#         self.btnSuspend.clicked.connect(self.suspendClicked)
#         self.btnCancel.clicked.connect(self.cancelClicked)

#         layout = QtWidgets.QVBoxLayout(self)
#         layout.addWidget(QtWidgets.QLabel("Group Name"))
#         layout.addWidget(self.cboGroup)
#         layout.addWidget(QtWidgets.QLabel("User Name"))
#         layout.addWidget(self.txtUserName)
#         layout.addWidget(self.btnSuspend)
#         layout.addWidget(self.btnCancel)

#     def suspendClicked(self):
#         # Add your suspension logic here
#         group_name = self.cboGroup.currentText()
#         username = self.txtUserName.text()

#         # TODO: Perform the suspension action

#         QtWidgets.QMessageBox.information(self, "Success", "User Deleted Successfully")

#     def cancelClicked(self):
#         self.close()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     removeUser = RemoveUser()
#     removeUser.show()
#     sys.exit(app.exec())

from PyQt5 import QtCore, QtGui, QtWidgets

class RemoveUser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Remove User")

        self.cboGroup = QtWidgets.QComboBox(self)
        self.txtUserName = QtWidgets.QLineEdit(self)
        self.btnSuspend = QtWidgets.QPushButton("Suspend", self)
        self.btnCancel = QtWidgets.QPushButton("Cancel", self)

        self.btnSuspend.clicked.connect(self.suspendClicked)
        self.btnCancel.clicked.connect(self.cancelClicked)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel("Group Name"))
        layout.addWidget(self.cboGroup)
        layout.addWidget(QtWidgets.QLabel("User Name"))
        layout.addWidget(self.txtUserName)
        layout.addWidget(self.btnSuspend)
        layout.addWidget(self.btnCancel)

        self.setStyleSheet("background-color: green; color: yellow;")


    def suspendClicked(self):
        # Add your suspension logic here
        group_name = self.cboGroup.currentText()
        username = self.txtUserName.text()

        # TODO: Perform the suspension action

        QtWidgets.QMessageBox.information(self, "Success", "User Deleted Successfully")

    def cancelClicked(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    removeUser = RemoveUser()
    removeUser.show()
    sys.exit(app.exec())
