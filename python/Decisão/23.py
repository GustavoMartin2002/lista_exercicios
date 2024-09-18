"""
23-Uma empresa produz três tipos de peças mecânicas: parafusos, porcas e arruelas.
Têm-se os preços unitários de cada tipo de peça e sabe-se que sobre estes preços incidem descontos de 10% 
para porcas, 20% para parafusos e 30% para arruelas. Escreva um programa que calcule o valor total da compra de 
um cliente. Deve ser mostrado o nome do cliente. O número de cada tipo de peça que o mesmo comprou, 
o total de desconto e o total a pagar pela compra.
"""

nome = input("digite o nome do cliente: ")

# Preços unitários
preco_parafuso = float(input("digite o preço unitário do parafuso: "))
preco_porca = float(input("digite o preço unitário da porca: "))
preco_arruela = float(input("digite o preço unitário da arruela: "))

# Quantidades
qtd_parafusos = int(input("digite a quantidade de parafusos: "))
qtd_porcas = int(input("digite a quantidade de porcas: "))
qtd_arruelas = int(input("digite a quantidade de arruelas: "))

# Descontos
desconto_parafuso = preco_parafuso * 0.20
desconto_porca = preco_porca * 0.10
desconto_arruela = preco_arruela * 0.30

# Valores totais sem desconto
valor_total_parafusos = preco_parafuso * qtd_parafusos
valor_total_porcas = preco_porca * qtd_porcas
valor_total_arruelas = preco_arruela * qtd_arruelas

# Valores totais com desconto
valor_total_parafusos_com_desconto = valor_total_parafusos - (qtd_parafusos * desconto_parafuso)
valor_total_porcas_com_desconto = valor_total_porcas - (qtd_porcas * desconto_porca)
valor_total_arruelas_com_desconto = valor_total_arruelas - (qtd_arruelas * desconto_arruela)

# Total da compra
total_compra = valor_total_parafusos_com_desconto + valor_total_porcas_com_desconto + valor_total_arruelas_com_desconto

# Total do desconto
total_desconto = (qtd_parafusos * desconto_parafuso) + (qtd_porcas * desconto_porca) + (qtd_arruelas * desconto_arruela)

print(f"Nome do cliente: {nome}")
print(f"Quantidade de parafusos: {qtd_parafusos}")
print(f"Quantidade de porcas: {qtd_porcas}")
print(f"Quantidade de arruelas: {qtd_arruelas}")
print(f"Total de desconto: R$ {total_desconto}")
print(f"Total da compra: R$ {total_compra}")
