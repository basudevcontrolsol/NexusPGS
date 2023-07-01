# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QMessageBox, QPushButton
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
# import sys
# import datetime
# import pyodbc

# class AddUser(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Add User")
#         self.form_name = ""
#         self.activity = ""
#         self.username = ""
#         self.usertype = ""

#         self.cmd = None
#         # self.con = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;DATABASE=PGSData;Trusted_Connection=yes;")
#         self.dr = None

#         self.init_ui()

#     def init_ui(self):
#         self.form_name = self.objectName()
#         self.username = "Login.username"

#         self.get_data()

#         self.btn_cancel = QPushButton("Cancel", self)
#         self.btn_cancel.clicked.connect(self.cancel_clicked)
#         self.btn_save = QPushButton("Save", self)
#         self.btn_save.clicked.connect(self.save_clicked)

#         layout = QVBoxLayout()
#         layout.addWidget(self.btn_cancel)
#         layout.addWidget(self.btn_save)

#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#     def get_data(self):
#         try:
#             self.con.open()
#             self.cmd = self.con.cursor()
#             self.cmd.execute("SELECT DISTINCT Group_Name FROM tblGroup")
#             groups = [row[0] for row in self.cmd.fetchall()]
#             self.cbo_group.addItems(groups)

#             self.cmd.execute("SELECT GroupName FROM tblUserDetails WHERE UserName = ?", self.username)
#             self.usertype = self.cmd.fetchone()[0]

#             self.con.close()
#         except Exception as ex:
#             QMessageBox.critical(self, "Error", str(ex))

#     def cancel_clicked(self):
#         self.activity = "Closing the Add User Page"
#         try:
#             self.con.open()
#             self.cmd.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, ?, ?)",
#                              self.username, self.form_name, datetime.datetime.now(), self.activity)
#             self.con.commit()
#             self.con.close()
#         except Exception as ex:
#             QMessageBox.critical(self, "Error", str(ex))
#         self.close()

#     def save_clicked(self):
#         if self.usertype == "Admin" or self.usertype == "admin":
#             if not self.txt_name.text():
#                 QMessageBox.warning(self, "Warning", "Enter the Name To Proceed")
#             elif not self.txt_user_name.text():
#                 QMessageBox.warning(self, "Warning", "Enter the User Name To Proceed")
#             elif not self.txt_email.text():
#                 QMessageBox.warning(self, "Warning", "Enter the Email To Proceed")
#             elif not self.txt_phone_no.text():
#                 QMessageBox.warning(self, "Warning", "Enter the Phone Number")
#             elif not self.cbo_group.currentText():
#                 QMessageBox.warning(self, "Warning", "Select The Group to Continue")
#             elif not self.txt_password.text():
#                 QMessageBox.warning(self, "Warning", "Enter the Password To Proceed")
#             elif not self.txt_retype_password.text():
#                 QMessageBox.warning(self, "Warning", "Retype the Password to Proceed")
#             elif self.txt_password.text() == self.txt_retype_password.text():
#                 try:
#                     self.con.open()
#                     self.cmd.execute("INSERT INTO tblUserDetails(GroupName, Name, UserName, Email, Phone_No, Password, Date) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                                      self.cbo_group.currentText(), self.txt_name.text(), self.txt_user_name.text(),
#                                      self.txt_email.text(), self.txt_phone_no.text(), self.txt_retype_password.text(),
#                                      datetime.datetime.now())
#                     self.con.commit()
#                     res = self.cmd.rowcount

#                     if res > 0:
#                         QMessageBox.information(self, "Success", "User Added Successfully")
#                         self.activity = "Adding a new user"
#                         try:
#                             self.con.open()
#                             self.cmd.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, ?, ?)",
#                                              self.username, self.form_name, datetime.datetime.now(), self.activity)
#                             self.con.commit()
#                             self.con.close()
#                         except Exception as ex:
#                             QMessageBox.critical(self, "Error", str(ex))
#                     else:
#                         QMessageBox.warning(self, "Warning", "Unsuccessful Operation")
#                         self.activity = "Unsuccessful Add User Attempt"
#                         try:
#                             self.con.open()
#                             self.cmd.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, ?, ?)",
#                                              self.username, self.form_name, datetime.datetime.now(), self.activity)
#                             self.con.commit()
#                             self.con.close()
#                         except Exception as ex:
#                             QMessageBox.critical(self, "Error", str(ex))

#                     self.con.close()
#                 except Exception as ex:
#                     QMessageBox.critical(self, "Error", str(ex))
#             else:
#                 QMessageBox.warning(self, "Warning", "Passwords do not match")
#         else:
#             QMessageBox.warning(self, "Warning", "You Are Not Authorized to Perform this Action!!")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     add_user = AddUser()
#     add_user.show()
#     sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QMessageBox, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import datetime
import pyodbc

class AddUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add User")

        self.init_ui()

    def init_ui(self):
        self.btn_cancel = QPushButton("Cancel", self)
        self.btn_cancel.clicked.connect(self.cancel_clicked)
        self.btn_save = QPushButton("Save", self)
        self.btn_save.clicked.connect(self.save_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.btn_cancel)
        layout.addWidget(self.btn_save)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def cancel_clicked(self):
        QMessageBox.information(self, "Information", "Cancel button clicked")

    def save_clicked(self):
        QMessageBox.information(self, "Information", "Save button clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    add_user = AddUser()
    add_user.show()
    sys.exit(app.exec_())
