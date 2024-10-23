"""
3.0-Sem utilizar a operação de multiplicação, escreva um programa que multiplique dois números inteiros.
Por exemplo: 2 * 2 = 2 + 2.
"""

vezes = 0
num = int(input(f"digite um numero : "))
for i in range(1, 11, 1):
    vezes += num
    print(f"{num}x{i} = {vezes}")