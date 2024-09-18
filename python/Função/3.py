"""
3-Crie uma função chamada "calculadora" que receba dois números e uma operação matemática 
(soma, subtração, multiplicação ou divisão) como parâmetros e retorne o resultado da operação escolhida.

Ex.

calculadora(2,8,"*")
16
"""

def calculadora(num1, num2, operacao):
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        print("erro")

    print(resultado)

calculadora(50,25,"+")
calculadora(50,25,"-")
calculadora(50,25,"*")
calculadora(50,25,"/")