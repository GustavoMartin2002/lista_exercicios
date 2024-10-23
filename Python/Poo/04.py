"""Crie uma classe Pessoa com atributos de nome, idade e cidade, e um método para apresentar
informações da pessoa."""

class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos, e moro na cidade de {self.cidade}.")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite a sua cidade: ")

pessoa = Pessoa(nome, idade, cidade)
Pessoa.apresentar(pessoa)