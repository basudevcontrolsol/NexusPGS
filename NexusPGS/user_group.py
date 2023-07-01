import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtCore import QDateTime

class UserGroupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.username = ""
        self.form_name = ""
        self.activity = ""
        self.usertype = ""
        self.initUI()
        self.status()
        self.uploadGroup()
        self.setStyleSheet("background-color: green; color: yellow;")

    def initUI(self):
        self.username = "Username"  # Replace with actual username
        self.form_name = self.__class__.__name__
        self.setWindowTitle("User Group")
        self.setGeometry(100, 100, 400, 300)

        self.cboSuperiorGroup = QComboBox(self)
        self.cboSuperiorGroup.setObjectName("cboSuperiorGroup")
        self.cboSuperiorGroup.setGeometry(10, 10, 150, 25)

        self.cboStatus = QComboBox(self)
        self.cboStatus.setObjectName("cboStatus")
        self.cboStatus.setGeometry(10, 50, 150, 25)

        self.txtGroupName = QLineEdit(self)
        self.txtGroupName.setObjectName("txtGroupName")
        self.txtGroupName.setGeometry(10, 90, 150, 25)

        self.rtbDescription = QTextEdit(self)
        self.rtbDescription.setObjectName("rtbDescription")
        self.rtbDescription.setGeometry(10, 130, 150, 100)

        self.txtSuperiorGroupLevel = QLineEdit(self)
        self.txtSuperiorGroupLevel.setObjectName("txtSuperiorGroupLevel")
        self.txtSuperiorGroupLevel.setGeometry(10, 240, 150, 25)

        self.btnSubmit = QPushButton("Submit", self)
        self.btnSubmit.setGeometry(180, 10, 100, 25)
        self.btnSubmit.clicked.connect(self.btnSubmit_Click)

        self.btnCancel = QPushButton("Cancel", self)
        self.btnCancel.setGeometry(180, 50, 100, 25)
        self.btnCancel.clicked.connect(self.btnCancel_Click)

        self.show()

    def uploadGroup(self):
        # Simulating group upload without database connectivity
        group_names = ["Group 1", "Group 2", "Group 3"]
        self.cboSuperiorGroup.addItems(group_names)

        # Simulating usertype retrieval without database connectivity
        self.usertype = "Admin"

    def status(self):
        self.cboStatus.addItem("Active")
        self.cboStatus.addItem("Inactive")
        self.cboStatus.setCurrentIndex(0)

    def btnSubmit_Click(self):
        if self.txtGroupName.text().isEmpty():
            QMessageBox.warning(self, "Warning", "Enter the Group Name")
        elif self.cboSuperiorGroup.currentIndex() == -1:
            QMessageBox.warning(self, "Warning", "Select a Superior Group")
        else:
            try:
                # Simulating group creation without database connectivity
                QMessageBox.information(self, "Success", "Group Created Successfully !!!")
                self.activity = "Created new group"
                self.txtGroupName.clear()
                self.rtbDescription.clear()
                self.txtSuperiorGroupLevel.clear()
                self.uploadGroup()
            except Exception as ex:
                QMessageBox.critical(self, "Error", str(ex))

    def btnCancel_Click(self):
        self.close()
        self.activity = "Closing the User Group page"
        QMessageBox.information(self, "Information", "User Group page closed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserGroupWindow()
    sys.exit(app.exec_())
