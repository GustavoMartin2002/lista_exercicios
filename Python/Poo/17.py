"""17. Veículos - Herança:
Modele uma hierarquia de classes para veículos, como Carro, Moto e Bicicleta, que herdam da classe 
base Veiculo. Cada classe deve ter métodos para acelerar e frear."""

class Veiculo:
    def __init__(self, nome):
        self.nome = nome

    def acelerar():
        pass

    def frear():
        pass

class Carro(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)

    def acelerar(self):
        return print("Acelerando carro.")

    def frear(self):
        return print("Freando carro.")

class Moto(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)

    def acelerar(self):
        return print("Acelerando moto.")
    
    def frear(self):
        return print("Freando moto.")

class Bicicleta(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)

    def acelerar(self):
        return print("Pedalando bicicleta.")
    
    def frear(self):
        return print("Freando bicicleta.")

#carro
nomeCarro = input("Digite o nome do carro: ")
carro = Carro(nomeCarro)
carro.acelerar()
carro.frear()

print("\n")
#carro
nomeMoto = input("Digite o nome da moto: ")
moto = Moto(nomeMoto)
moto.acelerar()
moto.frear()

print("\n")
#carro
nomeBicicleta = input("Digite o nome da bicicleta: ")
bicicleta = Bicicleta(nomeBicicleta)
bicicleta.acelerar()
bicicleta.frear()
