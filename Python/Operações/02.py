"""
2-Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.
"""

num = int(input("digite um numero: "))

antecessor = num - 1
sucessor = num + 1

print(f"""
o numero é {num}
o seu antecessor é {antecessor}
o sucessor é {sucessor}
""")