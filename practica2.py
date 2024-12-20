class Chassis:
    def __init__(self,pid ,partNumber ,serialNumber ,BU):
        self.pid = pid
        self.partNumber = partNumber
        self.serialNumber = serialNumber
        self.BU = BU
        self.cantRsp = 0
        self.width = 0
        self.height = 0
        self.depth = 0
    def iAm (self):
        print(f"Mi BU es:{self.BU}")
        print(f"Mi PID es: {self.pid}")
        print(f"Mi número de parte es: {self.partNumber}")
        print(f"Mi número de serie es: {self.serialNumber}")
        print(f"Mis medidas son:\nAncho: {self.width} in \nAltura: {self.height} in \nProfundidad: {self.depth} in")
        print(F"RSP requeridas: {self.cantRsp}")
    def turnOn(self):
        print(f"\nIniciando sistema....  {self.pid}")

class Pabu (Chassis):
    def __init__(self,pid ,partNumber ,serialNumber ,BU):
        super(Pabu, self).__init__(pid ,partNumber ,serialNumber ,BU)
        self.ima = 0
    def verifyIma (self):
        if self.ima > 0:
            print(f"La unidad requiere {self.ima} IMA y se verificaron correctamente")
        else:
            print("La unidad no requiere IMA ")
class Crbu (Chassis):
    def __init__(self,pid ,partNumber ,serialNumber ,BU):
        super(Crbu, self).__init__(pid ,partNumber ,serialNumber ,BU)
        self.linecardLancer = 0
    def verifyLinecardLancer(self):
        if self.linecardLancer > 0:
            print(f"La unidad requiere {self.linecardLancer} linecard LANCER y se verificaron correctamente")
        else:
            print("La unidad no requiere linecard LANCER ")
class Erbu (Chassis):
    def __init__(self,pid ,partNumber ,serialNumber ,BU):
        super(Erbu, self).__init__(pid ,partNumber ,serialNumber ,BU)
        self.linecardFlex = 0
    def verifyLinecardFlex(self):
        if self.linecardFlex > 0:
            print(f"La unidad requiere {self.linecardFlex} linecard FLEX y se verificaron correctamente")
        else:
            print("La unidad no requiere linecard FLEX ")

chassis1 = Pabu("nc560-452-ac", "68-1254-01", "FOC2854542", "pabu")
chassis1.cantRsp = 2
chassis1.width = 3
chassis1.height = 4
chassis1.depth = 5
chassis1.ima = 5
chassis1.turnOn()
chassis1.iAm()
chassis1.verifyIma()

chassis2 = Crbu("8808","68-72648-03 " ,"FOC28457D","CRBU")
chassis2.cantRsp = 1
chassis2.width = 5
chassis2.height = 10
chassis2.depth = 8
chassis2.linecardLancer = 6
chassis2.turnOn()
chassis2.iAm()
chassis2.verifyLinecardLancer()

chassis3 = Erbu("ASR-9006","68-17485-01 ","FOX2843G55","ERBU")
chassis3.cantRsp = 2
chassis3.width = 4
chassis3.height = 6
chassis3.depth = 7
chassis3.linecardFlex = 5
chassis3.turnOn()
chassis3.iAm()
chassis3.verifyLinecardFlex()