import datetime
import pyodbc
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer

class Sitedata(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sitedata")
        self.username = ""
        self.form_name = ""
        self.activity = ""
        self.con = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=myServerAddress;Database=myDataBase;Uid=myUsername;Pwd=myPassword")
        self.cur = self.con.cursor()

        self.occfacility4W = 0.0
        self.occb14w = 0.0
        self.occb24w = 0.0
        self.occb34w = 0.0
        self.occfacility2W = 0.0
        self.occb12w = 0.0
        self.occb22w = 0.0
        self.FacilityCapacity4W = 0.0
        self.FacilityCapacity2W = 0.0
        self.Unit_Id = ""
        self.Vehicle_Type2W = ""
        self.Vehicle_Type4W = ""
        self.Area_Name = ""
        self.Unit_ID = ""

        self.layout = QVBoxLayout()
        self.label_datetime = QLabel()
        self.layout.addWidget(self.label_datetime)
        self.setLayout(self.layout)

        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timer1_Tick)
        self.timer1.start(1000)

        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.timer2_Tick)
        self.timer2.start(1000)

        self.timer3 = QTimer()
        self.timer3.timeout.connect(self.timer3_Tick)
        self.timer3.start(1000)

    def timer1_Tick(self):
        date = datetime.datetime.now()
        self.label_datetime.setText(date.strftime("%Y-%m-%d %H:%M:%S.%f"))

    def timer2_Tick(self):
        self.CapacityData()
        self.IN()
        self.Out()
        self.CalculateAvailability()

    def timer3_Tick(self):
        self.Occupancy()

    def Vechiletype(self):
        self.cur.execute("SELECT Vehicle_Type FROM tblVehicleType WHERE Sl_No = 1")
        self.Vehicle_Type2W = self.cur.fetchone()[0]

        self.cur.execute("SELECT Vehicle_Type FROM tblVehicleType WHERE Sl_No = 2")
        self.Vehicle_Type4W = self.cur.fetchone()[0]

        self.cur.execute("SELECT TOP 1 Unit_ID FROM tblUnit ORDER BY ModifiedOn DESC")
        self.Unit_Id = self.cur.fetchone()[0]

        self.txt2wVehicletype.setText(self.Vehicle_Type2W)
        self.txtB12WVehicletype.setText(self.Vehicle_Type2W)
        self.txtB22WVehicleType.setText(self.Vehicle_Type2W)
        self.txt4wVehicletype.setText(self.Vehicle_Type4W)
        self.txtB14WVehicleType.setText(self.Vehicle_Type4W)
        self.txtB24WVehicletype.setText(self.Vehicle_Type4W)
        self.txtB34WVehicleType.setText(self.Vehicle_Type4W)

    def CapacityData(self):
        self.cur.execute("SELECT TOP 1 Capacity FROM tblCapacity WHERE Vehicle_type = '4W' AND Area_Name = 'B14w' ORDER BY Date DESC")
        self.txtB14WCapacity.setText(str(self.cur.fetchone()[0]))

        self.cur.execute("SELECT TOP 1 Capacity FROM tblCapacity WHERE Vehicle_type = '4W' AND Area_Name = 'B24w' ORDER BY Date DESC")
        self.txtB24WCapacity.setText(str(self.cur.fetchone()[0]))

        self.cur.execute("SELECT TOP 1 Capacity FROM tblCapacity WHERE Vehicle_type = '4W' AND Area_Name = 'B34w' ORDER BY Date DESC")
        self.txtB34WCapacity.setText(str(self.cur.fetchone()[0]))

        self.cur.execute("SELECT TOP 1 Capacity FROM tblCapacity WHERE Vehicle_type = '2W' AND Area_Name = 'B12w' ORDER BY Date DESC")
        self.txtB12WCapacity.setText(str(self.cur.fetchone()[0]))

        self.cur.execute("SELECT TOP 1 Capacity FROM tblCapacity WHERE Vehicle_type = '2W' AND Area_Name = 'B22w' ORDER BY Date DESC")
        self.txtB22WCapacity.setText(str(self.cur.fetchone()[0]))

        self.cur.execute("SELECT Capacity FROM tblCapacity WHERE Vehicle_type = '4W' AND Area_Name = 'Facility' ORDER BY Date DESC")
        self.FacilityCapacity4W = self.cur.fetchone()[0]

        self.cur.execute("SELECT Capacity FROM tblCapacity WHERE Vehicle_type = '2W' AND Area_Name = 'Facility' ORDER BY Date DESC")
        self.FacilityCapacity2W = self.cur.fetchone()[0]

        self.txtFacilityCapacity4W.setText(str(self.FacilityCapacity4W))
        self.txtFacilityCapacity2W.setText(str(self.FacilityCapacity2W))

    def IN(self):
        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '2W' AND IN_OUT = 'IN'",
                         self.Unit_Id)
        self.occfacility2W = self.cur.fetchone()[0]
        self.txtFacility2WIn.setText(str(self.occfacility2W))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '2W' AND IN_OUT = 'IN' AND Area_name = 'B12w'",
                         self.Unit_Id)
        self.occb12w = self.cur.fetchone()[0]
        self.txtB12WIn.setText(str(self.occb12w))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '2W' AND IN_OUT = 'IN' AND Area_name = 'B22w'",
                         self.Unit_Id)
        self.occb22w = self.cur.fetchone()[0]
        self.txtB22WIn.setText(str(self.occb22w))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '4W' AND IN_OUT = 'IN'",
                         self.Unit_Id)
        self.occfacility4W = self.cur.fetchone()[0]
        self.txtFacility4WIn.setText(str(self.occfacility4W))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '4W' AND IN_OUT = 'IN' AND Area_name = 'B14w'",
                         self.Unit_Id)
        self.occb14w = self.cur.fetchone()[0]
        self.txtB14WIn.setText(str(self.occb14w))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '4W' AND IN_OUT = 'IN' AND Area_name = 'B24w'",
                         self.Unit_Id)
        self.occb24w = self.cur.fetchone()[0]
        self.txtB24WIn.setText(str(self.occb24w))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '4W' AND IN_OUT = 'IN' AND Area_name = 'B34w'",
                         self.Unit_Id)
        self.occb34w = self.cur.fetchone()[0]
        self.txtB34WIn.setText(str(self.occb34w))

    def Out(self):
        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '2W' AND IN_OUT = 'OUT'",
                         self.Unit_Id)
        self.occfacility2W = self.cur.fetchone()[0]
        self.txtFacility2WOut.setText(str(self.occfacility2W))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '2W' AND IN_OUT = 'OUT' AND Area_name = 'B12w'",
                         self.Unit_Id)
        self.occb12w = self.cur.fetchone()[0]
        self.txtB12WOut.setText(str(self.occb12w))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '2W' AND IN_OUT = 'OUT' AND Area_name = 'B22w'",
                         self.Unit_Id)
        self.occb22w = self.cur.fetchone()[0]
        self.txtB22WOut.setText(str(self.occb22w))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '4W' AND IN_OUT = 'OUT'",
                         self.Unit_Id)
        self.occfacility4W = self.cur.fetchone()[0]
        self.txtFacility4WOut.setText(str(self.occfacility4W))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '4W' AND IN_OUT = 'OUT' AND Area_name = 'B14w'",
                         self.Unit_Id)
        self.occb14w = self.cur.fetchone()[0]
        self.txtB14WOut.setText(str(self.occb14w))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '4W' AND IN_OUT = 'OUT' AND Area_name = 'B24w'",
                         self.Unit_Id)
        self.occb24w = self.cur.fetchone()[0]
        self.txtB24WOut.setText(str(self.occb24w))

        self.cur.execute("SELECT Count(*) FROM tblTrans WHERE unit_id = ? AND Convert(date,EnteredOn) = Convert(date,Getdate()) AND Vehicle_type = '4W' AND IN_OUT = 'OUT' AND Area_name = 'B34w'",
                         self.Unit_Id)
        self.occb34w = self.cur.fetchone()[0]
        self.txtB34WOut.setText(str(self.occb34w))

    def CalculateAvailability(self):
        available2W = self.FacilityCapacity2W - (self.occfacility2W + self.occb12w + self.occb22w)
        self.txtAvailable2W.setText(str(available2W))

        available4W = self.FacilityCapacity4W - (self.occfacility4W + self.occb14w + self.occb24w + self.occb34w)
        self.txtAvailable4W.setText(str(available4W))

    def Occupancy(self):
        occupancy2W = (self.occfacility2W + self.occb12w + self.occb22w) / self.FacilityCapacity2W * 100
        self.txt2WOccupancy.setText(str(round(occupancy2W, 2)))

        occupancy4W = (self.occfacility4W + self.occb14w + self.occb24w + self.occb34w) / self.FacilityCapacity4W * 100
        self.txt4WOccupancy.setText(str(round(occupancy4W, 2)))

if __name__ == "__main__":
    app = QApplication([])
    window = Sitedata()
    window.show()
    app.exec_()
