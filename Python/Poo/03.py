"""Modele uma classe Produto com atributos de nome, preço e quantidade em estoque, e
métodos para atualizar o estoque."""

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizarEstoque(self, setQuantidade):
        self.quantidade = setQuantidade

    def info(self):
        print(f"""
        Nome:        {self.nome}
        Preço:       {self.preco}
        Quantidade:  {self.quantidade}
        Total:       {self.preco * self.quantidade}
        """)

nome = input("Digite o nome do produto: ")
preco = float(input(f"digite o preco do produto {nome}: "))
quantidade = int(input(f"digite a quantidade do produto {nome}: "))

produto1 = Produto(nome, preco, quantidade)
produto1.info()
print("\n")

quantidadeNova = int(input("insira a nova quantidade: "))
produto1.atualizarEstoque(quantidadeNova)

produto1.info()