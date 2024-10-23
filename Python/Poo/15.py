"""15. Loja Online - Herança:
Modele uma hierarquia de classes para uma loja online, incluindo classes como Produto, Eletronico,
Roupa que herdam da classe Produto. Cada classe deve ter métodos para mostrar detalhes e preço."""

class Produto:
    def __init__(self, nome='', preco=0.0, descricao=''):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def mostrarDetalhes(self):
        print(f"Nome: {self.nome}\nDescrição: {self.descricao}")

    def mostrarPreco(self):
        print(f"Preço: R${self.preco:.2f}")


class Eletronico(Produto):
    def __init__(self, nome='', preco=0.0, descricao=''):
        super().__init__(nome, preco, descricao)

    def cadastrar(self):
        self.nome = input("Informe o Produto Eletrônico: ")
        self.preco = float(input("Informe o Preço: "))
        self.descricao = input("Informe a descrição do Produto: ")


class Roupa(Produto):
    def __init__(self, nome='', preco=0.0, descricao=''):
        super().__init__(nome, preco, descricao)

    def cadastrar(self):
        self.nome = input("Informe o Produto Roupa: ")
        self.preco = float(input("Informe o Preço: "))
        self.descricao = input("Informe a Descrição do Produto: ")


def menu1():
    print("""
        1 - Cadastrar Produto
        2 - Mostrar Detalhes
        3 - Sair
    """)
    return input("Escolha uma opção: ")


def menu2():
    print("""
        1 - Eletrônico
        2 - Roupa
    """)
    return input("Escolha o tipo de produto: ")


eletronico = Eletronico()
roupa = Roupa()


while True:
    opcao = menu1()

    if opcao == '1':
        tipo_prod = menu2()

        if tipo_prod == '1':
            eletronico.cadastrar()
        elif tipo_prod == '2':
            roupa.cadastrar()
        else:
            print("Opção inválida!")

    elif opcao == '2':
        tipo_prod = menu2()

        if tipo_prod == '1':
            eletronico.mostrarDetalhes()
            eletronico.mostrarPreco()
        elif tipo_prod == '2':
            roupa.mostrarDetalhes()
            roupa.mostrarPreco()
        else:
            print("Opção inválida!")

    elif opcao == '3':
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
