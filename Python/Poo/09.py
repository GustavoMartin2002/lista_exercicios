"""9. Crie uma classe Livro com atributos de título, autor e número de páginas, e métodos para
exibir informações do livro. As informações são solicitadas ao usuário."""

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def exibirInformacoes(self):
        opcao = 0
        while (opcao != 2):
            print("\n-=-=-=Menu=-=-=-")
            print("1 Exibir Informação")
            print("2 Sair\n")
            opcao = int(input("Escolha: "))
            if opcao == 1:
                print(f"Livro {self.titulo}")
                print(f"Autor do Livro: {self.autor}")
                print(f"Paginas do Livro {self.paginas}\n")

titulo = input("Digite o titulo: ")
autor = input("Digite o autor: ")
paginas = int(input("Digite as paginas: "))

livro = Livro(titulo, autor, paginas)
livro.exibirInformacoes()