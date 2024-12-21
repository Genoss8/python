class Figura:
    def __init__(self,area,perimetro):
        self.area = area
        self.perimetro = perimetro
    def calcularArea(self):
        print("Mi area es: ", self.area)
    def calcularPerimetro(self):
        print("Mi perimetro es: ", self.perimetro)

class Cuadrado(Figura):
    def __init__(self,lado):
        area = lado * lado
        perimetro = lado * 4
        super().__init__(area,perimetro)

class Circulo(Figura):
    def __init__(self,radio):
        area = 
        perimetro = lado * 4
        super().__init__(area,perimetro)
       
        
cuadrado1 = Cuadrado(5)
cuadrado1.calcularArea()
cuadrado1.calcularPerimetro()