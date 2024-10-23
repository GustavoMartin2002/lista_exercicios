"""
20-Faça um algoritmo que leia um número de 1 a 5 e escreva por extenso. Caso o usuário digite um número que não 
#esteja neste intervalo, exibir mensagem: número inválido.
"""
numero = int(input("digite um número de 1 a 5: "))

if numero == 1:
    print("um")
elif numero == 2:
    print("dois")
elif numero == 3:
    print("tres")
elif numero == 4:
    print("quatro")
elif numero == 5:
    print("cinco")
else:
    print("número inválido!")