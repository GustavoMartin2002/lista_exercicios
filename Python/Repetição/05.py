"""
5-Foi feita uma pesquisa com um grupo de alunos de uma universidade, 
na qual se perguntou para cada aluno, o número de vezes que utilizou o restaurante da universidade no último mês.
Construa um programa que determine:
O percentual de alunos que utilizaram menos que 10 vezes o restaurante;
O percentual de alunos que utilizaram entre 10 e 15 vezes;
O percentual de alunos que utilizaram o restaurante acima de 15 vezes.
Ex.: 2, 3, 11, 12, 21, 22, 23 = a) 28%; b) 28%; c) 42%
Use o valor -1 como sentinela para sair.
"""

i = 0
percentualA = 0
percentualB = 0
percentualC = 0

while(i != 1):
    vezes = int(input("quantas vezes você utilizou o restaurente no ultimo mês: "))
    
    if vezes < 10:
        percentualA += vezes*(vezes/100)
    elif vezes <=15:
        percentualB += vezes*(vezes/100)
    elif vezes > 15:
        percentualC += vezes*(vezes/100)
    

    i = int(input("digite 0 para continuar ou digite 1 para sair: "))

print(f"""
percentual para quem utilizou menos que 10 vezes: {percentualA}%
percentual para quem utilizou entre 10 a 15 vezes: {percentualB}%
percentual para quem utilizou maior que 15 vezes: {percentualC}%
""")
