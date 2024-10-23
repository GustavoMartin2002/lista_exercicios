"""
4-Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.

Valores esperados:

múltiplo(8, 4) == True

múltiplo(7, 3) == False

múltiplo(5, 5) == True
"""

def func(num1,num2):
    if num1 % num2 == 0:
        resultado = True
    else:
        resultado = False

    print(resultado)
    return resultado
    
func(8,4)
func(7,3)
func(5,5)
