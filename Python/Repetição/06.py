""" 
6-Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, 
a qual coletaram os seguintes dados referentes a cada habitante para serem analisados:

sexo (masculino e feminino)
cor dos olhos (azuis, verdes ou castanhos)
cor dos cabelos (louros, castanhos, pretos)
idade
Faça um um programa que determine e escreva:

a maior idade dos habitantes;
a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
a quantidade de indivíduos que tenham olhos verdes e cabelos louros;
O final do conjunto de habitantes é reconhecido pelo valor -1 informado como idade.
"""
maiorIdade_i = 0
sexo_feminino_idade = 0
olhos_verdes_loiros = 0
idade = 0
while(idade != -1):
    sexo = input("qual seu sexo? (f) para feminino ou (m) para masculino: ").lower()
    cor_olhos = input("qual a cor do seus olhos? (azuis), (verdes), (castanhos):").lower()
    cor_cabelos = input("qual a cor dos seus cabelos? (loiro), (castanhos), (pretos): ").lower()
    idade = int(input("qual a sua idade? "))

    # a maior idade dos habitantes;
    if idade > maiorIdade_i:
        maiorIdade_i = idade
    
    # a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
    if (sexo == "f" and idade > 18 and idade < 35):
        sexo_feminino_idade += 1

    # a quantidade de indivíduos que tenham olhos verdes e cabelos louros;
    if (cor_olhos == "verdes" and cor_olhos == "loiro"):
        olhos_verdes_loiros += 1

print(f"""
a maior idade dos habitantes: {maiorIdade_i}
a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos: {sexo_feminino_idade}
a quantidade de indivíduos que tenham olhos verdes e cabelos louros: {olhos_verdes_loiros}
""")