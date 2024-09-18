"""
4-Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input("digita uma letra: ").lower()

if (letra in "aeiou"):
  print("vogal")
else:
  print("consoante")