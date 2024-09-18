""" 
12-Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 
11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:

Salário Bruto até 900 (inclusive) - isento

Salário Bruto até 1500 (inclusive) - desconto de 5%

Salário Bruto até 2500 (inclusive) - desconto de 10%

Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Exemplo:

Salário Bruto: (5 * 220)          : R$ 1100,00
  (-) IR (5%)                     : R$   55,00  
  (-) INSS ( 10%)                 : R$  110,00
  FGTS (11%)                      : R$  121,00
  Total de descontos              : R$  165,00
  Salário Liquido                 : R$  935,00
"""

valor_hora = float(input("digite o valor da sua hora: "))
horas_trabalhadas = float(input("digite a quantidade de horas trabalhadas no mes: "))

# salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# descontos
desconto_ir = salario_bruto * 0.05  # 5% de IR
desconto_inss = salario_bruto * 0.10  # 10% de INSS
fgts = salario_bruto * 0.11  # 11% de FGTS

# total de descontos
total_descontos = desconto_ir + desconto_inss

# salário líquido
salario_liquido = salario_bruto - total_descontos

# desconto do Imposto de Renda
if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
else:
    desconto_ir = salario_bruto * 0.20


# Saída de dados
print("\n")
print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas})          : {salario_bruto:}")
print(f"  (-) IR (5%)                     : R$ {desconto_ir}")
print(f"  (-) INSS (10%)                 : R$ {desconto_inss}")
print(f"  FGTS (11%)                      : R$ {fgts}")
print(f"  Total de descontos              : R$ {total_descontos}")
print(f"  Salário Líquido                 : R$ {salario_liquido}")