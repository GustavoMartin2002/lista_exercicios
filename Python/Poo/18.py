"""18. Jogo de Cartas - Abstração:
Crie classes para representar cartas de um baralho, incluindo Carta, Baralho, Jogador. Utilize 
abstração para definir métodos como embaralhar, distribuir_carta e mostrar_mao.
"""
class Carta:
    def __init__(self, cartas):
        self.cartas = cartas

class Baralho(Carta):
    def __init__(self, cartasJogador, cartas):
        super().__init__(cartas)
        self.cartasJogador = cartasJogador

    def embaralhar(self):
        print("embaralhando cartas...")

    def distribuir_carta(self):
        if not self.cartas:
            print("Sem cartas")
            return None
        else:
            self.cartas -= self.cartasJogador
            print(f"retirada {self.cartasJogador} cartas, resta {self.cartas}")
    
class Jogador(Baralho):
    def __init__(self, nome, cartasJogador, cartas):
        super().__init__(cartasJogador, cartas)
        self.nome = nome

    def mostrar_mao(self):
        print(f"Cartas em mão: {self.cartasJogador}")

# carta
numeroCartas = int(input("Digite quantas cartas havera no jogo: "))
carta = Carta(numeroCartas)

# baralho
cartasJogador1 = int(input("Digite o numero de cartas por jogador: "))
baralho = Baralho(cartasJogador1, numeroCartas)
baralho.embaralhar()
baralho.distribuir_carta()

# jogador
nome1 = input("digite seu nome: ")
jogador1 = Jogador(nome1, cartasJogador1, numeroCartas)
jogador1.mostrar_mao()