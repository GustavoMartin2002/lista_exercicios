class Carro:
    def __init__(self,marca,ano):
        self.marca = marca
        self.ano = ano

    def info(self):
        print(f"""
        Marca: {self.marca}
        ano:   {self.ano}
        """)

marca = input("Digite a marca do carro: ")
ano = int(input("Digite o ano do carro: "))

carro = Carro(marca, ano)
Carro.info(carro)