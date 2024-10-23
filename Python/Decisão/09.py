"""
9-Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

num1 = int(input("digite o numero 1: "))
num2 = int(input("digite o numero 2: "))
num3 = int(input("digite o numero 3: "))

lista = [num1, num2, num3]

print(sorted(lista, reverse=True))