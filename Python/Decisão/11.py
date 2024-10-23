"""
11-As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para 
desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:

salários até 280,00 (incluindo): aumento de 20%

salários entre 280,00 e 700,00: aumento de 15%

salários entre 700,00 e 1500,00: aumento de 10%

salários de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela:

salário antes do reajuste;
percentual de aumento aplicado;
valor do aumento;
novo salário, após o aumento.
"""

salario = float(input("digite o salário do colaborador: "))

if salario <= 280:
    aumento = 20
elif salario <= 700:
    aumento = 15
elif salario <= 1500:
    aumento = 10
else:
    aumento = 5

valor_aumento = salario * (aumento / 100)
novo_salario = salario + valor_aumento

print("\n")
print(f"salário antes do reajuste: {salario}")
print(f"aumento aplicado: {aumento}%")
print(f"valor do aumento: {valor_aumento}")
print(f"Novo salário: {novo_salario}")