
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class Sitedata(QMainWindow):
    def __init__(self):
        super(Sitedata, self).__init__()

        self.setWindowTitle("Site Data")
        self.setGeometry(200, 200, 300, 300)

        self.layout = QVBoxLayout()
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

        self.createInputFields()
        self.createButtons()
        self.setStyleSheet("background-color: green; color: yellow;")

    def createInputFields(self):
        self.txtFacility2WIn = QLineEdit()
        self.txtB12WIn = QLineEdit()
        self.txtB22WIn = QLineEdit()
        self.txtFacility4WIn = QLineEdit()
        self.txtB14WIn = QLineEdit()
        self.txtB24WIn = QLineEdit()
        self.txtB34WIn = QLineEdit()

        self.txtFacility2WOut = QLineEdit()
        self.txtB12WOut = QLineEdit()
        self.txtB22WOut = QLineEdit()
        self.txtFacility4WOut = QLineEdit()
        self.txtB14WOut = QLineEdit()
        self.txtB24WOut = QLineEdit()
        self.txtB34WOut = QLineEdit()

        self.layout.addWidget(QLabel("2-Wheeler Availability"))
        self.layout.addWidget(QLabel("Facility 2W In:"))
        self.layout.addWidget(self.txtFacility2WIn)
        self.layout.addWidget(QLabel("B1 2W In:"))
        self.layout.addWidget(self.txtB12WIn)
        self.layout.addWidget(QLabel("B2 2W In:"))
        self.layout.addWidget(self.txtB22WIn)

        self.layout.addWidget(QLabel("4-Wheeler Availability"))
        self.layout.addWidget(QLabel("Facility 4W In:"))
        self.layout.addWidget(self.txtFacility4WIn)
        self.layout.addWidget(QLabel("B1 4W In:"))
        self.layout.addWidget(self.txtB14WIn)
        self.layout.addWidget(QLabel("B2 4W In:"))
        self.layout.addWidget(self.txtB24WIn)
        self.layout.addWidget(QLabel("B3 4W In:"))
        self.layout.addWidget(self.txtB34WIn)

        self.layout.addWidget(QLabel("2-Wheeler Out"))
        self.layout.addWidget(QLabel("Facility 2W Out:"))
        self.layout.addWidget(self.txtFacility2WOut)
        self.layout.addWidget(QLabel("B1 2W Out:"))
        self.layout.addWidget(self.txtB12WOut)
        self.layout.addWidget(QLabel("B2 2W Out:"))
        self.layout.addWidget(self.txtB22WOut)

        self.layout.addWidget(QLabel("4-Wheeler Out"))
        self.layout.addWidget(QLabel("Facility 4W Out:"))
        self.layout.addWidget(self.txtFacility4WOut)
        self.layout.addWidget(QLabel("B1 4W Out:"))
        self.layout.addWidget(self.txtB14WOut)
        self.layout.addWidget(QLabel("B2 4W Out:"))
        self.layout.addWidget(self.txtB24WOut)
        self.layout.addWidget(QLabel("B3 4W Out:"))
        self.layout.addWidget(self.txtB34WOut)

    def createButtons(self):
        self.btnIn = QPushButton("Set In Values")
        self.btnOut = QPushButton("Set Out Values")
        self.btnCalculate = QPushButton("Calculate Availability")

        self.layout.addWidget(self.btnIn)
        self.layout.addWidget(self.btnOut)
        self.layout.addWidget(self.btnCalculate)

        self.btnIn.clicked.connect(self.In)
        self.btnOut.clicked.connect(self.Out)
        self.btnCalculate.clicked.connect(self.CalculateAvailability)

    def In(self):
        self.txtFacility2WIn.setText("0")
        self.txtB12WIn.setText("0")
        self.txtB22WIn.setText("0")
        self.txtFacility4WIn.setText("0")
        self.txtB14WIn.setText("0")
        self.txtB24WIn.setText("0")
        self.txtB34WIn.setText("0")

    def Out(self):
        self.txtFacility2WOut.setText("0")
        self.txtB12WOut.setText("0")
        self.txtB22WOut.setText("0")
        self.txtFacility4WOut.setText("0")
        self.txtB14WOut.setText("0")
        self.txtB24WOut.setText("0")
        self.txtB34WOut.setText("0")

    def CalculateAvailability(self):
        available2W = self.FacilityCapacity2W - (int(self.txtFacility2WIn.text()) + int(self.txtB12WIn.text()) + int(self.txtB22WIn.text()) + int(self.txtFacility2WOut.text()) + int(self.txtB12WOut.text()) + int(self.txtB22WOut.text()))
        self.txtAvailable2W.setText(str(available2W))

        available4W = self.FacilityCapacity4W - (int(self.txtFacility4WIn.text()) + int(self.txtB14WIn.text()) + int(self.txtB24WIn.text()) + int(self.txtB34WIn.text()) + int(self.txtFacility4WOut.text()) + int(self.txtB14WOut.text()) + int(self.txtB24WOut.text()) + int(self.txtB34WOut.text()))
        self.txtAvailable4W.setText(str(available4W))


if __name__ == "__main__":
    app = QApplication([])
    window = Sitedata()
    window.show()
    app.exec_()
