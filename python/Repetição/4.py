"""
4-Faça um programa que leia um conjunto de números (X) e imprima a quantidade de números pares (QPares) e a 
quantidade de números impares (QImpares) lidos. Admita que o valor 9999 é utilizado como sentinela para fim de 
leitura.
"""
qPares = 0
qImpares = 0
i = 0

while i != 9999:
    x = int(input("digite um numero: "))
    if x %2 == 0:
        qPares += 1
    elif x%2 == 1:
        qImpares +=1

    print(f"""
quantidade de pares: {qPares}
quantidade de impares: {qImpares}
      """)
    
    i = int(input("digite 1 para continuar e 9999 para sair: "))