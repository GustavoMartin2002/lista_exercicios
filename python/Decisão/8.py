"""
8-Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato."""

produto1 = float(input("digite o preco do produto 1: "))
produto2 = float(input("digite o preco do produto 2: "))
produto3 = float(input("digite o preco do produto 3: "))

lista = [produto1, produto2, produto3]

produto_recomendado = min(lista)

print(f"o produto recomendado que você deve comprar é o de preco: {produto_recomendado}")