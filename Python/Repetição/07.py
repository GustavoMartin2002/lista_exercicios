"""
7-Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. 
Imprima o cálculo da operação escolhida. Repita até que a opção saída seja escolhida.
"""
escolha = 0
operacao = 0.0
while(escolha != 5):

    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite outro numero: "))

    print(f"""
    OPÇÕES DE MENU

    1 - adição
    2 - subtração
    3 - divisão
    4 - multiplicação
    5 - sair
    """)

    escolha = int(input("qual operação você deseja fazer?"))

    if escolha == 1:
        operacao = num1 + num2
    elif escolha ==2:
        operacao = num1 + num2
    elif escolha ==3:
        operacao = num1 / num2
    elif escolha ==4:
        operacao = num1 * num2
    else:
        escolha == 5

    print(operacao)

    
