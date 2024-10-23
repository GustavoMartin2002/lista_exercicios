"""Crie uma classe Círculo com um atributo de raio e métodos para calcular a área e o perímetro"""
class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        area = 3.14*(self.raio * self.raio)
        print(f"Área: {area}")

    def perimetro(self):
        perimetro = 2 * 3.14 * self.raio
        print(f"Perímetro: {perimetro}")

raio = float(input("Digite o raio do circulo: "))     
raioX = Circulo(raio)
Circulo.area(raioX)
Circulo.perimetro(raioX)