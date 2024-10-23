"""
1-Crie um programa no qual o usuário deverá inserir os valores da altura, 
largura e profundidade de uma caixa d’água, em cm. No final, exiba o volume dessa caixa d’água. Dica: 
Volume = Altura x Largura x Profundidade
"""

#ENTRADA DE DADOS
altura = float(input("Digite uma altura: "))
largura = float(input("Informe a sua largura: "))
profundidade = float (input("Insira o valor da profundidade: "))

#PROCESSAMENTO
volume = altura * largura * profundidade

#SAÍDA
print("O volume é: ",volume)