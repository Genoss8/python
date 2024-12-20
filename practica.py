class ChassisPabu:
    def __init__(self, pid, partNumber, serialNumber,BU):
        self.pid = pid
        self.partNumber = partNumber
        self.serialNumber = serialNumber
        self.BU = BU
        self.cantRsp = 0
        self.ima = 0
        self.powerFanTray = 0
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
    def verifyIma (self):
        if self.ima > 0:
            print("La unidad lleva IMA y se verificaron correctamente")
        else:
            print("La unidad no requiere IMA ")

chassis1 = ChassisPabu("nc560-452-ac", "68-1254-01", "FOC2854542", "pabu")
chassis1.cantRsp = 2
chassis1.ima = 0
chassis1.powerFanTray = 1
chassis1.width = 4
chassis1.height = 2
chassis1.depth = 2
chassis1.turnOn()
chassis1.iAm()
print(f"Cantidad IMA: {chassis1.ima}")
print(f"Cantidad de power fan tray: {chassis1.powerFanTray}")
chassis1.verifyIma()




class chassisCrbu:
    def __init__(self, pid, partNumber, serialNumber,BU):
        self.pid = pid
        self.partNumber = partNumber
        self.serialNumber = serialNumber
        self.BU = BU
        self.cantRsp = 0
        self.fabriCard = 0
        self.linecardLancer = 0
        self.width = 0
        self.height = 0
        self.depth = 0

    def iAm (self):
        print(f"\nMi BU es:{self.BU}")
        print(f"Mi PID es: {self.pid}")
        print(f"Mi número de parte es: {self.partNumber}")
        print(f"Mi número de serie es: {self.serialNumber}")
        print(f"Mis medidas son:\nAncho: {self.width} in \nAltura: {self.height} in \nProfundidad: {self.depth} in")
        print(F"RSP requeridas: {self.cantRsp}")
    def turnOn(self):
        print(f"\nIniciando sistema....  {self.pid}")
    def verifyLinecardLancer(self):
        if self.linecardLancer > 0:
            print("La unidad requiere linecard LANCER y se verificaron correctamente")
        else:
            print("La unidad no requiere linecard LANCER ")
chassisC =  chassisCrbu("8808","68-72648-03 " ,"FOC28457D","CRBU")
chassisC.cantRsp = 1
chassisC.fabriCard = 8
chassisC.linecardLancer = 2
chassisC.width = 5
chassisC.height = 8
chassisC.depth = 12
chassisC.turnOn()
chassisC.iAm()
print(f"Cantidad de fabricard: {chassisC.fabriCard}")
print(f"Cantidad de linecard Lancer: {chassisC.linecardLancer}")
chassisC.verifyLinecardLancer()



class chassisErbu:
    def __init__(self,pid ,partNumber ,serialNumber ,BU):
        self.pid = pid
        self.partNumber = partNumber
        self.serialNumber = serialNumber
        self.BU = BU
        self.cantRsp = 0
        self.Mpa = 0
        self.linecardFlex = 0
        self.width = 0
        self.height = 0
        self.depth = 0
    def iAm(self):
        print(f"\nMi BU es:{self.BU}")
        print(f"Mi PID es: {self.pid}")
        print(f"Mi número de parte es: {self.partNumber}")
        print(f"Mi número de serie es: {self.serialNumber}")
        print(f"Mis medidas son:\nAncho: {self.width} in \nAltura: {self.height} in \nProfundidad: {self.depth} in")
        print(F"RSP requeridas: {self.cantRsp}")
    def turnOn(self):
        print(f"\nIniciando sistema....  {self.pid}")
    def verifyLinecardFlex(self):
        if self.linecardFlex > 0:
            print("La unidad requiere linecard FLEX y se verificaron correctamente")
        else:
            print("La unidad no requiere linecard FLEX ")
chassisE =  chassisErbu("ASR-9006","68-17485-01 ","FOX2843G55","ERBU")
chassisE.cantRsp = 2
chassisE.Mpa = 3
chassisE.linecardFlex = 3
chassisE.width = 3
chassisE.height = 5
chassisE.depth = 8
chassisE.turnOn()
chassisE.iAm()
print(f"Cantidad de linecards Flex: {chassisE.linecardFlex}")
print(f"Cantidad de MPA: {chassisE.Mpa}")
chassisE.verifyLinecardFlex()



listaChassis = [chassis1, chassisC, chassisE]
for i in listaChassis:
    i.iAm()
    