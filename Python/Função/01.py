""" 
1-Crie uma função chamada "par_ou_impar" que receba um número como parâmetro e retorne se o número é par ou ímpar.
"""

def par_ou_impar(numero):
    if numero %2==0:
        print(f"o numero {numero} é par")
    else:
        print(f"o numero {numero} é impar")

numero = int(input("digite um numero: "))
par_ou_impar(numero)