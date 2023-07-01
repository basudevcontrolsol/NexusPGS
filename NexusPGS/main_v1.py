import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QLabel
from PyQt5.QtCore import QTimer, QDateTime
import pyodbc
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NexuxPro Parking Guidance System")
        self.resize(800, 600)
        self.setStyleSheet("background-color: green; color: yellow;")
        
        self.username = ""
        self.usertype = ""
        self.activity = ""
        self.form_name = ""
        
        # Sql Database object
        # self.con = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;DATABASE=PGSData;Trusted_Connection=yes;")
        # self.cursor = self.con.cursor()

        self.create_menu()
        self.create_status_bar()
        self.create_timer()
        self.username = self.get_current_username()
        self.set_central_widget_background()

    # def set_central_widget_background(self):
    #     # Load the image and add it to a QLabel to set it as the central widget background
    #     image_label = QLabel(self)
    #     pixmap = QPixmap("cps1.jpg")
    #     image_label.setPixmap(pixmap)
    #     image_label.setGeometry(0, 0, pixmap.width(), pixmap.height())
    #     self.setCentralWidget(image_label)


    def set_central_widget_background(self):
            # Load the image
            pixmap = QPixmap("cps1.jpg")

            # Create a QLabel and set the pixmap as its background
            image_label = QLabel(self)
            image_label.setPixmap(pixmap)

            # Create a layout for the central widget
            layout = QVBoxLayout()
            layout.addWidget(image_label)

            # Create a widget to hold the layout
            central_widget = QWidget(self)
            central_widget.setLayout(layout)

            # Set the central widget of the main window
            self.setCentralWidget(central_widget)

            # Center the image label within the central widget
            image_label.setAlignment(Qt.AlignCenter)
    def create_menu(self):
        self.menu = self.menuBar()
        
        self.site_data_menu = self.menu.addMenu("Site Data")
        self.add_menu_action(self.site_data_menu, "Accessing the Facility Data Page", self.open_site_data)
        
        self.logout_menu = self.menu.addMenu("Logout")
        self.add_menu_action(self.logout_menu, "User Logout", self.logout)
        
        self.update_password_menu = self.menu.addMenu("Update Password")
        self.add_menu_action(self.update_password_menu, "Accessing Update Password page", self.open_update_password)
        
        self.add_user_menu = self.menu.addMenu("Add User")
        self.add_menu_action(self.add_user_menu, "Accessing the Add User Page", self.open_add_user)
        
        self.remove_user_menu = self.menu.addMenu("Remove User")
        self.add_menu_action(self.remove_user_menu, "Accessing the Remove User Page", self.open_remove_user)
        
        self.user_group_menu = self.menu.addMenu("User Group")
        self.add_menu_action(self.user_group_menu, "Accessing the Facility Data Page", self.open_user_group)
        
        self.site_config_menu = self.menu.addMenu("Site Configuration")
        self.add_menu_action(self.site_config_menu, "Accessing Site Configuration Page", self.open_site_config)
        
        self.lane_config_menu = self.menu.addMenu("Lane Configuration")
        self.add_menu_action(self.lane_config_menu, "Accessing the Lane Configuration Page", self.open_lane_config)
        
        self.io_board_menu = self.menu.addMenu("IO Board Connection")
        self.add_menu_action(self.io_board_menu, "Accessing the IO Board Connection 1 Page", self.open_io_board_connection1)
        self.add_menu_action(self.io_board_menu, "Accessing the IO Board Connection 2 Page", self.open_io_board_connection2)
        
        self.user_activity_menu = self.menu.addMenu("User Activity")
        self.add_menu_action(self.user_activity_menu, "Accessing the User Activity Report Page", self.open_user_activity_report)
        
        self.occupancy_menu = self.menu.addMenu("Occupancy")
        self.add_menu_action(self.occupancy_menu, "Opening the Occupancy Report page", self.open_occupancy_report)
        
    def create_status_bar(self):
        self.timer_label = QLabel()
        self.statusBar().addWidget(self.timer_label)

    def create_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss.zzz")
        self.timer_label.setText(current_time)

    def get_current_username(self):
        # self.cursor.execute("SELECT GROUPNAME FROM tblUserDetails WHERE UserName = ?", self.username)
        # row = self.cursor.fetchone()
        # if row:
        #     return row[0]
        # return ""
        pass
    
    def add_menu_action(self, menu, activity, slot):
        action = QAction(activity, self)
        action.triggered.connect(slot)
        menu.addAction(action)
        
    def open_site_data(self):
        # self.form_name = "Sitedata"
        # self.activity = "Accessing the Facility Data Page"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        #     s1 = Sitedata()
        #     s1.show()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
        
    def logout(self):
        # self.form_name = "Login"
        # self.activity = "User Logout"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        #     self.close()
        #     l1 = Login()
        #     l1.show()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
        
    def open_update_password(self):
        # self.form_name = "Password"
        # self.activity = "Accessing Update Password page"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        #     p1 = Password()
        #     p1.show()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
        
    def open_add_user(self):
        # self.form_name = "AddUser"
        # self.activity = "Accessing the Add User Page"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        #     au1 = AddUser()
        #     au1.show()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
        
    def open_remove_user(self):
        # ru1 = Remove_User()
        # ru1.exec_()
        # self.form_name = "Remove_User"
        # self.activity = "Accessing the Remove User Page"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
        
    def open_user_group(self):
        # self.form_name = "User_Group"
        # self.activity = "Accessing the Facility Data Page"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        #     ug = User_Group()
        #     ug.show()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
        
    def open_site_config(self):
        # self.form_name = "SiteConfig"
        # self.activity = "Accessing Site Configuration Page"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        #     sc = SiteConfig()
        #     sc.show()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
        
    def open_lane_config(self):
        # self.form_name = "LaneConfig"
        # self.activity = "Accessing the Lane Configuration Page"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        #     lc = LaneConfig()
        #     lc.show()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
        
    def open_io_board_connection1(self):
        # self.form_name = "IOBoardConnection1"
        # self.activity = "Accessing the IO Board Connection 1 Page"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        #     io1 = IOBoardConnection1()
        #     io1.show()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
        
    def open_io_board_connection2(self):
        # self.form_name = "IOBoardConnection2"
        # self.activity = "Accessing the IO Board Connection 2 Page"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        #     io2 = IOBoardConnection2()
        #     io2.show()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
        
    def open_user_activity_report(self):
        # self.form_name = "UserActivity"
        # self.activity = "Accessing the User Activity Report Page"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        #     ua = UserActivity()
        #     ua.show()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
        
    def open_occupancy_report(self):
        # self.form_name = "Occupancy"
        # self.activity = "Opening the Occupancy Report page"
        # try:
        #     self.cursor.execute("INSERT INTO tblUser_Activity(User_Name, Form_Name, Time, Activity) VALUES (?, ?, GETDATE(), ?)",
        #                         self.username, self.form_name, self.activity)
        #     self.con.commit()
        #     oc = Occupancy()
        #     oc.show()
        # except Exception as ex:
        #     QMessageBox.critical(self, "Error", str(ex))
        pass
            

app = QApplication(sys.argv)
main_window = Main()
main_window.show()
sys.exit(app.exec_())
