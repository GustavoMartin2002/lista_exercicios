"""
3-Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = input("digite (m) para masculino (f) para feminino: ").lower()

if (sexo == "m"):
  print("o sexo escolhido é masculino")
elif (sexo == "f"):
  print("o sexo escolhido é feminino")
else:
  print("sexo invalido")