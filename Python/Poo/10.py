"""Modele uma classe Veiculo com atributos de cor, marca e modelo, e métodos para acelerar e
frear."""

class Veiculo:
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
    
    def acelerar(self):
        print("\nacelerar: ")
        for i in range(1, 101, 1) :
            print(i)
    
    def frear(self):
        print("\nfrear: ")
        for i in range(100, -1, -1):
            print(i)

cor = input("Digite a cor do veiculo: ")
marca = input("Digite a marca do veiculo: ")
modelo = input("Digite a cor do modelo: ")

carro = Veiculo(cor, marca, modelo)
carro.acelerar()
carro.frear()