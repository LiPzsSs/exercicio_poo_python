class Retangulo:
    def __init__ (self, largura = 0, altura = 0, area = 0, perimetro = 0):
        self.altura = int(input("Qual é a altura do retangulo? \n"))
        self.largura = int(input("Qual é a largura do retangulo? \n"))

    def calcularArea(self):
        print(f"A área do retangulo é: {self.largura * self.altura}")

    def calcularPerimetro(self):
        print(f"O perímetro do retângulo é: {2 * (self.altura + self.largura)}")


retangulo = Retangulo()
retangulo.calcularArea()
retangulo.calcularPerimetro()
