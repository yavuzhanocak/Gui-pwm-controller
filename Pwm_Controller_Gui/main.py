
from PyQt5.QtWidgets import*
from designer_python import Ui_MainWindow
from PyQt5.QtSerialPort import QSerialPortInfo,QSerialPort
from PyQt5.QtCore import QIODevice,QTimer
from PyQt5.QtGui import QDoubleValidator,QIcon

class ders_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.serial()
        self.init()
        self.connectUi()
        self.setStart()

    def setStart(self): #Başlangıç durum atamaları.
        self.setWindowIcon(QIcon("icons/icon1.png"))
        self.ui.buttonDisconnect.setEnabled(False)
        self.ui.buttonSend.setEnabled(False)
        self.ui.lineFrequency.setEnabled(False)
        self.ui.lineDutycycle.setEnabled(False)
        self.ui.second.setChecked(True)
        self.ui.labelPercent.setHidden(True)
        self.ui.comboSecond.setEnabled(False)
        self.ui.comboBoudrate.addItems(["4800", "9600", "14400", "19200", "28800", "38400", "57600 ", "115200"])
        self.ui.comboSecond.addItems(["ms", "µs"])
        self.onlyInt = QDoubleValidator()
        self.ui.lineFrequency.setValidator(self.onlyInt)
        self.ui.lineDutycycle.setValidator(self.onlyInt)

    def radioButton(self):
        if self.ui.second.isChecked()==True:
            self.ui.label_2.setText("Pulse Width")
            self.ui.lineDutycycle.clear()
            self.ui.labelPercent.setHidden(True)
            self.ui.comboSecond.setHidden(False)
        elif self.ui.percent.isChecked():
            self.ui.label_2.setText("Duty Cycle")
            self.ui.comboSecond.setHidden(True)
            self.ui.lineDutycycle.clear()
            self.ui.labelPercent.setHidden(False)


    def serial(self): #Seri portların çekilmesi.
        for serialPort in QSerialPortInfo.availablePorts():
            self.ui.comboComport.addItem((serialPort.portName()))

    def init(self):
        self.serialPort=QSerialPort()

    def portSenddata(self):
        if self.ui.lineFrequency.text()=="" or self.ui.lineDutycycle.text()=="":
            QMessageBox.about(self, "Error", "Please check the values!")

        else:
            self.freqData=self.ui.lineFrequency.text()+'f'
            self.serialPort.write(self.freqData.encode())
            QTimer.singleShot(500,self.sendDutycycle)



    def sendDutycycle(self):
        text = str(self.ui.comboSecond.currentText())
        if text == "ms" and self.ui.second.isChecked() == True:
            secData=float(self.ui.lineDutycycle.text())*1000
            self.dutyData=str(secData)+'s'
        elif text == "µs" and self.ui.second.isChecked() == True:
            self.dutyData = self.ui.lineDutycycle.text() + 's'
        else:
            self.dutyData = self.ui.lineDutycycle.text() + 'd'
        self.serialPort.write( self.dutyData.encode())
    def portConnect(self):

        self.serialPort.setPortName(self.ui.comboComport.currentText())
        self.serialPort.setBaudRate(int(self.ui.comboBoudrate.currentText()))
        self.serialPort.setDataBits(QSerialPort.Data8)
        self.serialPort.setStopBits(QSerialPort.OneStop)
        self.serialPort.setParity(QSerialPort.NoParity)
        if not self.serialPort.isOpen():
            self.serialPort.open(QIODevice.ReadWrite)
            self.ui.buttonConnect.setEnabled(False)
            self.ui.buttonDisconnect.setEnabled(True)
            self.ui.buttonSend.setEnabled(True)
            self.ui.comboComport.setEnabled(False)
            self.ui.comboBoudrate.setEnabled(False)
            self.ui.lineFrequency.setEnabled(True)
            self.ui.lineDutycycle.setEnabled(True)
            self.ui.comboSecond.setEnabled(True)
    def portDisconnect(self):
        if self.serialPort.isOpen():
            self.serialPort.close()
            self.ui.buttonConnect.setEnabled(True)
            self.ui.buttonDisconnect.setEnabled(False)
            self.ui.buttonSend.setEnabled(False)
            self.ui.comboComport.setEnabled(True)
            self.ui.comboBoudrate.setEnabled(True)
            self.ui.lineFrequency.setEnabled(False)
            self.ui.lineDutycycle.setEnabled(False)
            self.ui.lineFrequency.clear()
            self.ui.lineDutycycle .clear()
            self.ui.comboSecond.setEnabled(False)
    def connectUi(self):
        self.ui.buttonConnect.clicked.connect(self.portConnect)
        self.ui.buttonDisconnect.clicked.connect(self.portDisconnect)
        self.ui.buttonSend.clicked.connect(self.portSenddata)
        self.ui.second.toggled.connect(self.radioButton)
        self.ui.percent.toggled.connect(self.radioButton)


uygulama = QApplication([])
pencere=ders_2()
pencere.showNormal()
uygulama.exec_()
