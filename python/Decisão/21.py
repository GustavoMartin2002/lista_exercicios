"""
**21-Considere que o último concurso vestibular apresentou três provas: Português, Matemática e Conhecimentos Gerais. Considerando que para cada candidato tem-se um registro contendo o seu nome e as notas obtidas em cada uma das provas, construa um algoritmo que forneça:

a) o nome e as notas em cada prova do candidato

b) a média do candidato

c) uma informação dizendo se o candidato foi aprovado ou não. Considere que um candidato é aprovado se sua média for maior que 7.0 e se não apresentou nenhuma nota abaixo de 5.0**
"""

nome = input("digite o nome do candidato: ")
nota_portugues = float(input("digite a nota de português: "))
nota_matematica = float(input("digite a nota de matemática: "))
nota_conhecimentos_gerais = float(input("digite a nota de conhecimentos gerais: "))

media = (nota_portugues + nota_matematica + nota_conhecimentos_gerais) / 3

print(f"nome do candidato: {nome}")
print(f"nota de Português: {nota_portugues:.1f}")
print(f"nota de Matemática: {nota_matematica:.1f}")
print(f"nota de Conhecimentos Gerais: {nota_conhecimentos_gerais:.1f}")
print(f"média: {media}")

if media >= 7 and nota_portugues >= 5 and nota_matematica >= 5 and nota_conhecimentos_gerais >= 5:
    print("Aprovado!")
else:
    print("Reprovado!")
