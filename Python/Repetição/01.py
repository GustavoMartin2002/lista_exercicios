"""
"Quando mudamos a forma de ver as coisas, as coisas mudam de forma."

1-Faça um programa que calcule a média de salários de uma empresa, pedindo ao usuário a quantidade de funcionários, 
o nome e o salário de cada funcionário e devolvendo a média, o salário mais alto e o salário mais baixo.
"""

soma = 0.0
maiorSalario = 0.0
menorSalario = 7777777777.0

funcionarios = int(input("digite quantos funcionarios há na sua empresa: "))
for i in range(0, funcionarios, 1):
    nome = input("nome do funcionario: ")
    salario = float(input("salario do funcionario: "))

    # print("*"*25)
    # print(nome)
    # print(salario)
    # print("*"*25)

    print("-"*30)

    soma += salario

    if (salario > maiorSalario):
        maiorSalario = salario
    else:
         ("ERRO")

    if (salario < menorSalario):
        menorSalario = salario
    else:
        ("ERRO")


media = soma/funcionarios

print("\n")

print(f"media: {media}")
print("-"*25)
print(f"salario mais alto {maiorSalario}")
print("-"*25)
print(f" menor salario: {menorSalario}")