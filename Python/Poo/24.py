"""24.Implemente uma hierarquia de classes para modelar animais, como Mamifero, Ave e Peixe, 
com atributos e métodos específicos. Usando herança"""

class Animais:
    def __init__(self, nome):
        self.nome = nome
    def mover_se(self):
        pass

    def comer(self):
        pass

class Mamifero(Animais):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.tipo = tipo
    
    def mover_se(self):
        print("andando no solo")

    def comer(self):
        if self.tipo == "carnivoro".lower():
            print("comendo carne")
        elif self.tipo == "herbivoro".lower():
            print("comendo folhas")
        elif self.tipo == "onivoro".lower():
            print("comendo folhas ou carnes")
        else:
            print("erro")

class Ave(Animais):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.tipo = tipo
    
    def mover_se(self):
        print("voando pelo céu")

    def comer(self):
        if self.tipo == "carnivoro".lower():
            print("comendo carne")
        elif self.tipo == "herbivoro".lower():
            print("comendo folhas")
        elif self.tipo == "onivoro".lower():
            print("comendo folhas ou carnes")
        else:
            print("erro")

class Peixe(Animais):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.tipo = tipo

    def mover_se(self):
        print("nadando pelo mar")

    def comer(self):
            if self.tipo == "carnivoro".lower():
                print("comendo carne")
            elif self.tipo == "herbivoro".lower():
                print("comendo folhas")
            elif self.tipo == "onivoro".lower():
                print("comendo folhas ou carnes")
            else:
                print("erro")

# mamifero
nomeMamifero = input("nome do mamifero: ")
tipoMamifero = input("digite o tipo do animal (carnivoro) | (herbivoro) | (onivoro): ")
mamifero1 = Mamifero(nomeMamifero, tipoMamifero)
mamifero1.mover_se()
mamifero1.comer()

# ave
nomeAve = input("nome da ave: ")
tipoAve = input("digite o tipo do animal (carnivoro) | (herbivoro) | (onivoro): ")
ave1 = Ave(nomeAve, tipoAve)
ave1.mover_se()
ave1.comer()

# peixe
nomePeixe = input("nome do peixe: ")
tipoPeixe = input("digite o tipo do animal (carnivoro) | (herbivoro) | (onivoro): ")
peixe1 = Peixe(nomePeixe, tipoPeixe)
peixe1.mover_se()
peixe1.comer()

