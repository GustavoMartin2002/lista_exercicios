"""
5-Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item 
antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

def somaImposto(taxaImposto, custo):
    print(f"""
    taxa imposto: {taxaImposto}%
    custo: {custo}
    """)

    custo = custo * (taxaImposto/100)
    print(f"""
    custo depois do imposto : {custo:.2f}
    """)
    return custo

taxaImposto = float(input("digite a taxa do imposto: "))
custo = float(input("digite o custo antes do imposto: "))

somaImposto(taxaImposto, custo)