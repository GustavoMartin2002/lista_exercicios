"""Figuras Geométricas - Polimorfismo:
Crie uma classe abstrata FiguraGeometrica com métodos para calcular área e perímetro. Em 
seguida, crie subclasses como Quadrado, Círculo, Triângulo que implementam esses métodos de 
maneira específica."""

class FiguraGeometrica:
    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass

class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado**2

    def calcularPerimetro(self):
        return 4 * self.lado

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcularArea(self):
        return 3.14 *(self.raio**2)

    def calcularPerimetro(self):
        return 2 * 3.14 * self.raio

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcularArea(self):
        return (self.base * self.altura)/2

    def calcularPerimetro(self):
        return lado1 + lado2 + lado3

# quadrado
print("QUADRADO:\n")
lado = float(input("Qual tamanho de cada lado do quadrado? "))
quadrado = Quadrado(lado)

print(f"""
AREA:      {quadrado.calcularArea()}
PERIMETRO: {quadrado.calcularPerimetro()}
""")
print("\n")

# circulo
print("CIRCULO:\n")
raio = float(input("Qual o raio do circulo? "))
circulo = Circulo(raio)

print(f"""
AREA:      {circulo.calcularArea()}
PERIMETRO: {circulo.calcularPerimetro()}
""")

print("\n")
#triangulo
print("TRIANGULO:\n")
base = float(input("Qual a base do triangulo? "))
altura = float(input("Qual a altura do triangulo? "))
lado1 = float(input("Qual o lado1 do triangulo? "))
lado2 = float(input("Qual o lado2 do triangulo? "))
lado3 = float(input("Qual o lado3 do triangulo? "))

triangulo = Triangulo(base, altura, lado1, lado2, lado3)

print(f"""
AREA:      {triangulo.calcularArea()}
PERIMETRO: {triangulo.calcularPerimetro()}
""")