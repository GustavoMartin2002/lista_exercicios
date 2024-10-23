"""25. Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mudarValorLado(self, valorLado):
        self.lado = valorLado
      
    def retornarValorLado(self):
        print(f"Valor do Lado: {self.lado}\n")
        return self.lado
    
    def calcularArea(self):
        calculo = self.lado**2
        print(f"""
        Area do Quadrado: {calculo}
                """)

lado = float(input("Defina o valor Lado do Quadrado: "))

quadrado = Quadrado(lado)
quadrado.retornarValorLado()

quadrado.calcularArea()

#mudando
print("\n")
mudarLado = float(input("Altere o valor do Lado: "))

quadrado.mudarValorLado(mudarLado)
quadrado.retornarValorLado()

quadrado.calcularArea()