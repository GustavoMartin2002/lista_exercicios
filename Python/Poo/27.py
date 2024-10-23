"""27. Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que 
nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm."""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        print(f"se passou um ano. {self.nome} possui {self.idade} anos atualmente.")
    
    def engordar(self):
        self.peso += 5.0
        print(f"engordou, pesando {self.peso} quilos")
    
    def emagrecer(self):
        self.peso -= 2.5
        print(f"emagreceu, pesando {self.peso} quilos")
    
    def crescer(self):
        if idade < 21:
            self.altura += 0.05
            self.idade += 1
            print(f"cresceu, altura atual {self.altura} cm.")
        else:
            print(f"você tem {self.idade}, altura maxima já atingida.")

nome = input("insira seu nome: ")
idade = int(input("insira sua idade: "))
peso = float(input("insira seu peso: "))
altura = float(input("insira sua altura: "))

pessoa = Pessoa(nome, idade, peso, altura)

print("\n")
pessoa.envelhecer()
print("\n")
pessoa.engordar()
print("\n")
pessoa.emagrecer()
print("\n")
pessoa.crescer()
