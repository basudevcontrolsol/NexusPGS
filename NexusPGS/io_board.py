import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QComboBox
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from datetime import datetime

class IO_Board_Connection(QMainWindow):
    def __init__(self):
        super().__init__()
        self.username = ""
        self.form_name = ""
        self.activity = ""

        # Serial Port Initialization
        self.com_port = QSerialPort()
        self.com_port.readyRead.connect(self.port_data_received_2)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("IO Board Connection")
        self.resize(400, 300)

        # ComboBox for Serial Ports
        self.combo_ports = QComboBox(self)
        self.combo_ports.setGeometry(10, 10, 200, 30)
        self.populate_serial_ports()

        # Button to Get Serial Ports
        self.btn_get_serial_ports = QPushButton("Get Serial Ports", self)
        self.btn_get_serial_ports.setGeometry(220, 10, 150, 30)
        self.btn_get_serial_ports.clicked.connect(self.populate_serial_ports)

        # Label for Date and Time
        self.label_datetime = QLabel(self)
        self.label_datetime.setGeometry(10, 50, 380, 30)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)

        # Text Edit for Incoming Data
        self.text_edit_incoming = QTextEdit(self)
        self.text_edit_incoming.setGeometry(10, 90, 380, 150)

        # Label for Result
        self.label_result = QLabel(self)
        self.label_result.setGeometry(10, 250, 380, 30)

    def populate_serial_ports(self):
        self.combo_ports.clear()
        serial_ports = QSerialPortInfo.availablePorts()
        for port in serial_ports:
            self.combo_ports.addItem(port.portName())

    def update_datetime(self):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self.label_datetime.setText(date)

    def port_data_received_2(self):
        input_data = self.com_port.readAll().data().decode()
        self.text_edit_incoming.append(input_data)

    def closeEvent(self, event):
        self.com_port.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IO_Board_Connection()
    window.show()
    sys.exit(app.exec_())
