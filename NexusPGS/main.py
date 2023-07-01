import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        
        menu_bar = self.menuBar()
        
        file_menu = menu_bar.addMenu("File")
        
        site_menu = menu_bar.addMenu("Site")
        site_menu.addAction("Site Data")
        site_menu.addAction("Site Configuration")
        site_menu.addAction("Lane Configuration")
        
        io_menu = menu_bar.addMenu("IO Board")
        io_menu.addAction("IO Board Connection 1")
        io_menu.addAction("IO Board Connection 2")
        
        user_menu = menu_bar.addMenu("User")
        user_menu.addAction("Add User")
        user_menu.addAction("Remove User")
        user_menu.addAction("User Group")
        user_menu.addAction("Update Password")
        
        report_menu = menu_bar.addMenu("Reports")
        report_menu.addAction("User Activity Report")
        report_menu.addAction("Occupancy Report")
        
        logout_action = QAction("Logout", self)
        logout_action.triggered.connect(self.logout)
        file_menu.addAction(logout_action)
        
    def logout(self):
        reply = QMessageBox.question(self, "Logout", "Are you sure you want to logout?", 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            login_window = Login()
            login_window.show()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Window")
        
        login_action = QAction("Login", self)
        login_action.triggered.connect(self.login)
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(login_action)
        
    def login(self):
        # Perform login authentication here
        # You can open the main window if login is successful
        main_window = Main()
        main_window.show()
        
app = QApplication(sys.argv)
login_window = Login()
login_window.show()
sys.exit(app.exec_())
