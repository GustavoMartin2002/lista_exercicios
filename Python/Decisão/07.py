"""
7-Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num1 = int(input("digite o numero 1: "))
num2 = int(input("digite o numero 2: "))
num3 = int(input("digite o numero 3: "))

"""maior = max(num1, num2, num3)
menor = min(num1, num2, num3)"""

#logica maior numero
if (num1 > num2 and num1 > num3):
    maior = num1
elif (num2 > num1 and num2 > num3):
    maior = num2
else:
    maior = num3

#logica menor numero
if (num1 < num2 and num1 < num3):
    maior = num1
elif (num2 < num1 and num2 < num3):
    maior = num2
else:
    maior = num3

print(f"o maior numero é:  {maior}")
print(f"o menor numero é:  {menor}")