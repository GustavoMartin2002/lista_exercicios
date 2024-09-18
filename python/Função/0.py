"""
0-Faça um programa que solicite o nome do usuário e a idade do usuário, depois disso exiba a mensagem: 
"{nome} possui {idade} anos.". Esta mensagem deve ser escrita em uma função.
"""

def mensagem(nome, idade):
    print(f"{nome} possui {idade} anos.")

nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))

mensagem(nome, idade)
