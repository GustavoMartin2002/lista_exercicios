"""Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor"""

class Bola:
    class ModelBola:
        def __init__(self, cor, circunferência, material):
            self.cor = cor
            self.circunferência = circunferência
            self.material = material
    
    def trocarCor(self, setCor):
        self.cor = setCor

    def mostraCor(self):
        print(f"A cor da bola é: {self.cor}")

cor = input("Cor da bola: ")
circunferência = float(input("Digite a circunferência da bola: "))
material = input("Digite o material da bola: ")
bola1 = Bola.ModelBola(cor, circunferência, material)

trocarCor = input("Digite a nova cor: ")
Bola.trocarCor(bola1, trocarCor)

Bola.mostraCor(bola1)
        