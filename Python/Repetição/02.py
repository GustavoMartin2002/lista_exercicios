"""
2-Um hotel com 30 quartos cobra R$ 50,00 por diária e mais uma taxa de serviços. A taxa de serviços é de:

• R 4,00 por diária, se o número de diárias for < 15;

• R 3,60 por diária, se o número de diárias for = 15;

• R 3,00 por diária, se o número de diárias for > 15.

Faça um programa que imprima o nome e o total da conta de cada cliente do hotel.
Imprima também o total ganho pelo hotel.
"""
totalGanhoHotel = 0
totalConta = 0
diaria = 50.00

for i in range(0, 2, 1):
    nomeCliente = input("insira seu nome: ")
    dias = int(input("insira quantos dias você ficara no hotel: "))

    if(dias < 15):
        taxa = 4.0
    elif (dias >15):
        taxa = 3.60
    else:
        taxa = 3.0

    totalConta = dias*diaria+taxa
    totalGanhoHotel += totalConta

    print(f"sua conta é de {totalConta}")
    

print(f"""
o hotel ganhou {totalGanhoHotel}R$
""")