"""
22-Um hotel cobra R$ 60.00 a diária e mais uma taxa de serviços. A taxa de serviços é de:

• R$ 5.50 por diária, se o número de diárias for maior que 15;

• R$ 6.00 por diária, se o número de diárias for igual a 15;

• R$ 8.00 por diária, se o número de diárias for menor que 15.

Construa um algoritmo que mostre o nome e o total da conta de um cliente.**
"""

nome = input("digite o nome do cliente: ")
diarias = int(input("digite o número de diárias: "))

valor_diarias = diarias * 60

if diarias > 15:
    taxa_servicos = diarias * 5.50
elif diarias == 15:
    taxa_servicos = diarias * 6.00
else:
    taxa_servicos = diarias * 8.00

total_conta = valor_diarias + taxa_servicos

print(f"nome do cliente: {nome}")
print(f"total da conta: {total_conta}")
