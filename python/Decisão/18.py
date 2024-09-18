"""
**18-Uma empresa de vendas tem três corretores. A empresa paga ao corretor uma comissão calculada de acordo com 
o valor de suas vendas.

Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido.

Se o valor da venda do corretor estiver entre R$ 30.000.00 e R50.000.00 (incluindo extremos)
a comissão será de 9.5%.

Em qualquer outro caso, a comissão será de 7%. Escreva um algoritmo que gere um relatório contendo nome, 
valor da venda e comissão de cada um dos corretores. O relatório deve mostrar também o total de vendas da empresa.**
"""
total_vendas = 0

for i in range(1, 4):
    nome = input(f"digite o nome do corretor {i}: ")
    valor_venda = float(input(f"digite o valor da venda do corretor {i}: "))

    total_vendas += valor_venda

    if valor_venda > 50000:
        comissao = valor_venda * 0.12
    elif valor_venda >= 30000:
        comissao = valor_venda * 0.095
    else:
        comissao = valor_venda * 0.07

    print(f"relatório do corretor {i}:")
    print(f"nome: {nome}")
    print(f"valor da venda: R$ {valor_venda}")
    print(f"comissão: R$ {comissao}")

print(f"total de vendas da empresa: R$ {total_vendas}")