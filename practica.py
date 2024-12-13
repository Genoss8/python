pid = 'nc560-452-ac'
partNumber = '68-1254-01'
serialNumber = 'FOC2854542'
BU = 'PABU'
class chassisPabu:
    def __init__(self, pid, partNumber, serialNumber,BU):
        self.pid = pid
        self.partNumber = partNumber
        self.serialNumber = serialNumber
        self.BU = BU
    def iAm (self):
        print(f"Mi BU es:{self.BU}")
        print(f"Mi PID es: {self.pid}")
        print(f"Mi número de parte es: {self.partNumber}")
        print(f"Mi número de serie es: {self.serialNumber}")
chassis1 =  chassisPabu(pid, partNumber, serialNumber, BU)

chassis1.iAm()
