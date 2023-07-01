from PyQt5 import QtCore, QtGui, QtWidgets

class RemoveUser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.username = ""
        self.form_name = ""
        self.activity = ""
        self.usertype = ""

        self.cmd = None
        self.con = None
        self.dr = None

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

        self.userType()
        self.uploadGroup()

    def uploadGroup(self):
        try:
            self.con = None  # Add your database connection here
            self.con.open()

            self.cmd = self.con.cursor()
            self.cmd.execute("SELECT Group_Name FROM tblGroup")
            result = self.cmd.fetchall()

            self.cboGroup.addItems([row[0] for row in result])

            self.con.close()
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", str(ex))

    def userType(self):
        try:
            self.con = None  # Add your database connection here
            self.con.open()

            self.cmd = self.con.cursor()
            self.cmd.execute(f"SELECT GroupName FROM tblUserDetails WHERE UserName='{self.username}'")
            result = self.cmd.fetchone()

            self.usertype = result[0] if result else ""

            self.con.close()
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", str(ex))

    def suspendClicked(self):
        if self.usertype == "Admin" or self.usertype == "admin":
            if self.txtUserName.text() and self.cboGroup.currentText():
                try:
                    self.con = None  # Add your database connection here
                    self.con.open()

                    self.cmd = self.con.cursor()
                    self.cmd.execute(f"DELETE FROM tblUserDetails WHERE UserName='{self.txtUserName.text()}' AND GroupName LIKE '{self.cboGroup.currentText()}'")
                    res = self.cmd.rowcount

                    if res > 0:
                        QtWidgets.QMessageBox.information(self, "Success", "User Deleted Successfully")
                        self.activity = "Suspended a User"
                        self.cmd.execute(f"INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES ('{self.username}', '{self.form_name}', '{QtCore.QDateTime.currentDateTime().toString()}', '{self.activity}')")
                        self.con.commit()
                    else:
                        QtWidgets.QMessageBox.warning(self, "Error", "Failed attempt to suspend a user")
                        self.activity = "Closing the IO Board Connection Page"
                        self.cmd.execute(f"INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES ('{self.username}', '{self.form_name}', '{QtCore.QDateTime.currentDateTime().toString()}', '{self.activity}')")
                        self.con.commit()

                    self.con.close()
                except Exception as ex:
                    QtWidgets.QMessageBox.critical(self, "Error", str(ex))
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Select the Group Name")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "You Are Not Authorized to Perform this Action !!")

    def cancelClicked(self):
        self.close()
        self.activity = "Closing Remove User Page"
        try:
            self.con = None  # Add your database connection here
            self.con.open()

            self.cmd = self.con.cursor()
            self.cmd.execute(f"INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES ('{self.username}', '{self.form_name}', '{QtCore.QDateTime.currentDateTime().toString()}', '{self.activity}')")
            self.con.commit()

            self.con.close()
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", str(ex))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    removeUser = RemoveUser()
    removeUser.show()
    sys.exit(app.exec())
