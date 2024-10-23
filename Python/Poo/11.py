"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos
que:
a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i. tipoCombustivel.
ii. valorLitro
iii. quantidadeCombustivel
b. Possua no mínimo esses métodos:
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra
a quantidade de litros que foi colocada no veículo

ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de
combustível e mostra o valor a ser pago pelo cliente.

iii. alterarValor( ) – altera o valor do litro do combustível.

iv. alterarCombustivel( ) – altera o tipo do combustível.

v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na
bomba. 

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de
combustível total na bomba."""

class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombu):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombu = quantidadeCombu
        global gasolina
        global etanol
        global biodisel
        gasolina =  6.09
        etanol = 4.04 
        biodisel =  6.01 

    def abastecerPorValor(self, valor):
        if self.tipoCombustivel == "gasolina".lower():
            valor = self.valorLitro/gasolina
        elif self.tipoCombustivel == "etanol".lower():
            valor = self.valorLitro/etanol
        elif self.tipoCombustivel == "biodisel".lower():
            valor = self.valorLitro/biodisel
        else:
            print("invalido")

        print(f"quantidade de litros que foi colocada no veículo: {valor}")
        
        self.quantidadeCombu -= valor
        print(f"Bomba de combustivel: {self.quantidadeCombu}")

    def abastecerPorLitro(self, litros):
        if self.tipoCombustivel == "gasolina".lower():
            self.valorLitro = gasolina*litros
        elif self.tipoCombustivel == "etanol".lower():
            self.valorLitro = etanol*litros
        elif self.tipoCombustivel == "biodisel".lower():
            self.valorLitro = biodisel*litros
        else:
            print("invalido")

        print(f"valor a ser pago: {self.valorLitro}R$")

        self.quantidadeCombu -= litros
        print(f"Bomba de combustivel: {self.quantidadeCombu}")

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor
    
    def alterarCombustivel(self, novoTipo):
        self.tipoCombustivel = novoTipo

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombu = novaQuantidade

tipoCombustivel = input("Digite o tipo do combustivel = (gasolina) || (etanol) || (biodisel): ")
valorLitro = float(input("Digite o valor do litro: "))
quantidadeCombustivel = float(input("Digite a quantidade de combustivel: "))

bombinha = bombaCombustivel(tipoCombustivel, valorLitro, quantidadeCombustivel)

abastecerLitro = float(input("Digite o valor para abastecer por litro: "))
bombinha.abastecerPorLitro(abastecerLitro)

abastecerValor = float(input("Digite o valor em reais a ser abastecido: "))
bombinha.abastecerPorValor(abastecerValor)

resp = input("Deseja alterar valores? sim ou não: ")

while resp == "sim".lower():
    alterarValorLitro = float(input("Digite o novo valor por litro: "))

    novoCombustivel = input("Digite o novo combustivel: ")

    alterarQuantidade = float(input("Digite a nova quantidae do combustivel: "))
    break

bombinha.alterarValor(alterarValorLitro)
bombinha.alterarCombustivel(novoCombustivel)
bombinha.alterarQuantidadeCombustivel(alterarQuantidade)