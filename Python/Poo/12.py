"""Crie uma classe Elevador para armazenar as informações de um elevador de prédio. A classe
deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o
térreo), capacidade do elevador e quantas pessoas estão presentes nele. A classe deve também
disponibilizar os seguintes métodos:
• Inicializar: que deve receber como parâmetros a capacidade do elevador e o total de andares
no prédio (os elevadores sempre começam no térreo e vazio);
• Entrar: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver
espaço);
• Sair: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
• Subir: para subir um andar (não deve subir se já estiver no último andar);
• Descer: para descer um andar (não deve descer se já estiver no térreo);
• Obs.: Encapsular todos os atributos da classe (criar os métodos set e get)"""

class Elevador():
    def __init__(self):
        self.__terreo = 0
        self.__totalAndares = 0
        self.__capacidade = 0
        self.__pessoas = 0

    def inicializar(self, capacidade, totalAndares):
        """ 
        Inicializar: que deve receber como parâmetros a capacidade do elevador e o total de andares
        no prédio (os elevadores sempre começam no térreo e vazio);
        """
        self.__capacidade = capacidade
        self.__totalAndares = totalAndares
        self.__terreo = 0
        self.__pessoas = 0

    def entrar(self, pessoas):
        if pessoas > self.__capacidade:
            print(f"Capacidade inesperada, há {self.__pessoas} no elevador")
        else:
            self.__pessoas = pessoas
            print(f"há {self.__pessoas} pessoas no elevador")

    def sair(self, pessoas):
        if pessoas <= 0:
            print('não há ninguem no elevador')   
        else:
            print("saindo...")
            self.__pessoas -= pessoas
            print(f"há {self.__pessoas} pessoas no elevador")
    
    def subir(self, andar):
        if andar > self.__totalAndares:
            print('já estamos no ultimo andar')
        else:
            print(f'Subindo para o andar: {andar}')


    def descer(self, andar):
        if andar == self.__terreo:
            print('já estamos no ultimo andar')
        else:
            print(f'Descendo para o andar {andar}')

# -----------
# METODOS SET
# -----------
    def terroSet(self, terreo):
        self.__terreo = terreo
    
    def totalAndaresSet(self, totalAndares):
        self.__totalAndares = totalAndares 

    def capacidadeSet(self, capacidade):
        self.__capacidade = capacidade 

    def pessoasSet(self, pessoas):
        self.__pessoas = pessoas

# -----------
# METODOS GET
# -----------
    def terroGet(self):
        return self.__terreo
    
    def totalAndaresGet(self):
        return self.__totalAndares

    def capacidadeGet(self):
        return self.__capacidade

    def pessoasGet(self):
        return self.__pessoas

elevador200 = Elevador()

print("\nINICIALIZAR:")
andares = int(input("Digite a quantidade de andares: "))
capacidade = int(input("Digite a quantidade de pessoas que o elevador aguenta: "))
elevador200.inicializar(capacidade, andares)

print("\nENTRAR:")
entrar = int(input("Digite a quantidade de pessoas que irão entrar no elevador: "))
elevador200.entrar(entrar)

print("\nSAIR:")
sair = int(input("Digite a quantidade de pessoas que irão sair do elevador: "))
elevador200.sair(sair)

print("\nSUBIR:")
subir = int(input("Digite para qual andar deseja subir: "))
elevador200.subir(subir)

print("\nDESCER:")
descer = int(input("Digite para qual andar deseja descer: "))
elevador200.descer(descer)

print("\n SETS: ")
setTerro = int(input("Novo terreo: "))
elevador200.terroSet(setTerro)

setTotalAndares = int(input("Nova quantidade de andares: "))
elevador200.totalAndaresSet(setTotalAndares)

setCapacidade = int(input("Nova capacidade: "))
elevador200.capacidadeSet(setCapacidade)

setPessoas = int(input("Nova quantidade de pessoas: "))
elevador200.pessoasSet(setPessoas)

print("\n GETS: ")
print("Terreo: ", elevador200.terroGet())
print("Total Andares: ", elevador200.totalAndaresGet())
print("Capacidade: ", elevador200.capacidadeGet())
print("Pessoas: ", elevador200.pessoasGet())