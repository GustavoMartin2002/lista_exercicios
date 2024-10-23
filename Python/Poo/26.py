"""26.Classe Retangulo: Crie uma classe que modele um retangulo:
a. Atributos: LadoA, LadoB (ou Comprimento e largura, ou comprimento e largura, a escolher)
b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular 
Perímetro;
c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as 
medidas de um local. Depois, deve criar um objeto com as medidas e calcular a 
quantidade de pisos e de rodapés necessárias para o local."""

class Ratangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudarValorLados(self, novacomprimento, novalargura):
        self.comprimento = novacomprimento
        self.largura = novalargura
        print(f"""
nova comprimento: {self.comprimento}
nova largura: {self.largura}
        """)

    def rtornarValor(self):
        return print
        (f"""
comprimento: {self.comprimento}
largura: {self.largura}
        """)

    def calcularArea(self):
        area = self.comprimento * self.largura
        return area

    def calcularPerimetro(self):
        perimetro = (self.comprimento * 2) + (self.largura * 2)
        return perimetro

def main():
    comprimento = float(input("digite o comprimento do local: "))
    largura = float(input("digite a largura do local: "))

    local = Ratangulo(comprimento, largura)

    print(f"quantidade de pisos necessarios: {local.calcularArea()}")
    print("--------------------------------------------------------")
    print(f"quantidade de rodapes necessarios: {local.calcularPerimetro()}")

main()