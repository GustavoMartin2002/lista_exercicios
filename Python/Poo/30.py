"""30.Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho 
Eletrônico):
a. Atributos: Nome, Fome, Saúde e Idade
b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso 
tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um 
campo calculado, então não devemos criar um atributo para armazenar esta informação por 
que ela pode ser calculada a qualquer momento."""

class BichinhoEletronico:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    # funcoes alterar
    def alterarNome(self, setNome):
        self.nome = setNome

    def alterarFome(self, setFome):
        self.fome = setFome

    def alterarSaude(self, setSaude):
        self.saude = setSaude

    def alterarIdade(self, setIdade):
        self.idade = setIdade

    # funcoes retornar
    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude
        
    def retornarIdade(self):
        return self.idade

    # funcao humor
    def humor(self):
        if self.fome <= 15 and self.saude <= 25:
            return "Triste"
        elif self.fome <= 35 and self.saude <= 50:
            return "Estressado"
        else:
           return "feliz"

    # funcao info
    def status(self):
        print(f""" 
NOME:   {self.nome}
FOME:   {self.fome}
SAUDE:  {self.saude}
IDADE:  {self.idade}
HUMOR:  {self.humor()}
        """)

# criando Bichinho Eletronico
nome = input("Nome: ")
fome = int(input("Fome (%): "))
saude = int(input("Saude (%):"))
idade = int(input("Idade: "))

bichinho = BichinhoEletronico(nome, fome, saude, idade)

print("\n")
bichinho.status()

# Alterando
print(f"\nALTERANDO INFOS: {bichinho.nome}.")
setNome = input("Digite um novo nome: ")
bichinho.alterarNome(setNome)

setFome = int(input("Digite a nova fome (%): "))
bichinho.alterarFome(setFome)

setSaude = int(input("Digite a nova saude(%): "))
bichinho.alterarSaude(setSaude)

setIdade = input("Digite a nova idade: ")
bichinho.alterarIdade(setIdade)

# Retornando
print(f"\nRETORNANDO STATUS: {bichinho.nome}")
print(f"""
NOME:   {bichinho.retornarNome()}
FOME:   {bichinho.retornarFome()}
SAUDE:  {bichinho.retornarSaude()}
IDADE:  {bichinho.retornarIdade()}
HUMOR:  {bichinho.humor()}
    """)