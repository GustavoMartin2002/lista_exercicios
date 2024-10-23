"""13 . Crie uma classe chamada Forma, que possui os atributos area e perimetro. – Implemente as
subclasses Retangulo e Triangulo, que devem conter os métodos calculaArea e calculaPerimetro. A
classe Triangulo deve ter também o atributo altura. • No código de teste crie um objeto da classe
Triangulo e outro da Classe Retângulo e calcule a área de cada um."""

class Forma:
    def __init__(self, area, perimetro):
        self.area = area
        pass
        self.perimetro = perimetro
        pass
    def calculaArea(self):
        pass

    def calculaPerimetro(self):
        pass

class Retangulo(Forma):
        def calculaArea(self, largura, altura):
            self.area = largura * altura
            return self.area

        def calculaPerimetro(self, largura, altura):
            self.perimetro = 2 * (largura + altura)
            return self.perimetro

class Triangulo(Forma):
        def __init__(self, base, altura, lado1, lado2, lado3):
            self.base = base
            self.altura = altura
            self.lado1 = lado1
            self.lado2 = lado2
            self.lado3 = lado3
        def calculaArea(self):
            self.area = (self.base * self.altura) / 2
            return self.area
        
        def calculaPerimetro(self):
            self.perimetro = self.lado1 + self.lado2 + self.lado3
            return self.perimetro


larguraR = float(input("(Retangulo) Informe a Largura: "))
alturaR = float(input("(Retangulo) Informe a Altura: "))
larguraT = float(input("(Triangulo) Informe a Largura: "))
alturaT = float(input("(Triangulo) Informe a Altura: "))
base = float(input("(Triangulo) Informe a Base: "))
lado1 = float(input("(Triangulo) Informe o Lado1: "))
lado2 = float(input("(Triangulo) Informe o Lado2: "))
lado3 = float(input("(Triangulo) Informe o Lado3: "))

retangulo = Retangulo(larguraR, alturaR)
triangulo = Triangulo(base, alturaT, lado1, lado2, lado3)

print(f"""

    Area do Retangulo       {retangulo.calculaArea(larguraR, alturaR)}
    Perimetro do Retangulo  {retangulo.calculaPerimetro(larguraR, alturaR)}


    Area do Triangulo       {triangulo.calculaArea()}
    Perimetro do Traingulo  {triangulo.calculaPerimetro()}

""")