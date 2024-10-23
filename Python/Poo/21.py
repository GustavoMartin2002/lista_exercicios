"""21. Animais de Estimação - Polimorfismo:
Crie classes para representar animais de estimação, como Cachorro, Gato e Peixe. Implemente um
método comum emitir_som em cada classe e demonstre o polimorfismo chamando esse método para
diferentes tipos de animais."""

class Animais:
    def emitir_som(self):
        pass

class Cachorro(Animais):
    def emitir_som(self):
        return print("Cachorro Emite um som de Latido")

class Gato(Animais):
    def emitir_som(self):
        return print("Gato Emite um som de Miado")

class Peixe(Animais):
    def emitir_som(self):
        return print("Peixe não Emite som")


animais = [Cachorro(), Gato(), Peixe()]

for animal in animais:
    print(animal.emitir_som())

print(Animais)