class Retangulo:
    def __init__ (self, largura = 0, altura = 0, area = 0, perimetro = 0):
        self.altura = int(input("Qual é a altura do retangulo? \n"))
        self.largura = int(input("Qual é a largura do retangulo? \n"))
        self.area = area
        self.perimetro = perimetro

    def calcularArea(self):
        self.area = self.largura * self.altura
        print(f"A área do retangulo é: {self.area}")

    def calcularPerimetro(self):
        self.perimetro = 2 * (self.altura + self.largura)
        print(f"O perímetro do retângulo é: {self.perimetro}")


retangulo = Retangulo()
retangulo.calcularArea()
retangulo.calcularPerimetro()
