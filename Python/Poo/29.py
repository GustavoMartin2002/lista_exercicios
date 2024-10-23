"""29.Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário 
deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""

class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

        if self.canal > 50 or self.volume < 0:
            print("Canal indisponivel! Insira um canal de 0 a 50.")
        else:
            print(f"Canal disponivel! canal atual {self.canal}")

        if self.volume > 100 or self.volume < 0:
            print("Volume indisponivel! Insira um volume de 0 a 100.")
        else:
            print(f"Volume disponivel! volume atual {self.volume}")
    
    def setCanal(self, novoCanal):
        if novoCanal > 50 or novoCanal < 0:
            print("Canal indisponivel! Insira um canal de 0 a 50.")
        else:
            self.canal = novoCanal
            print(f"Canal alterado com sucesso! canal atual = {self.canal}")

    def setVolume(self, novoVolume):
        if novoVolume > 100 or novoVolume < 0:
            print("Volume indisponivel! Insira um volume de 0 a 100.")
        else:
            self.volume = novoVolume
            print(f"Volume alterado com sucesso! volume atual = {self.volume}")
            
canal = int(input("Insira o canal desejado: "))
volume = int(input("Insira o volume desejado: "))
televisao = Tv(canal, volume)

print("\n")
novoCanal = int(input("digite um novo canal: "))
televisao.setCanal(novoCanal)

print("\n")
novoVolume = int(input("digite um novo volume: "))
televisao.setVolume(novoVolume)