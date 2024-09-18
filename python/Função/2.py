"""
2-Fazer uma função que recebe três argumentos, e que retorne o produto desses três argumentos.
"""

def func(num1, num2, num3):
    resultado = num1 + num2 * num3
    print(resultado)
    return resultado

num1 = int(input("digite o numero 1: "))
num2 = int(input("digite o numero 2: "))
num3 = int(input("digite o numero 3: "))

func(num1,num2,num3)
