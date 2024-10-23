"""23. Biblioteca Virtual - Herança:
Modele uma biblioteca virtual com classes para Livro, Revista e Artigo, que herdam da classe base
Publicacao. Cada classe deve ter métodos para mostrar detalhes e conteúdo.
"""

class Publicacao:
    def __init__(self, data, conteudo):
        self.data = data
        self.conteudo = conteudo

    def mostrarDetalhes(self):
        pass
    
    def conteudo(self):
        pass

class Livro(Publicacao):
    def __init__(self, data, conteudo, nome, paginas):
        super().__init__(data, conteudo)
        self.nome = nome
        self.paginas = paginas

    def mostrarDetalhes(self):
        print(f"""
            Nome:    {self.nome}
            Data:    {self.data}
            Paginas: {self.paginas}
                """)
        
    def mostrarConteudo(self):
        print(f"""
            Conteudo: {self.conteudo}
                """)
        
class Revista(Publicacao):
    def __init__(self, data, conteudo, nome, paginas, assunto):
        super().__init__(data, conteudo)
        self.nome = nome
        self.paginas = paginas
        self.assunto = assunto

    def mostrarDetalhes(self):
        print(f"""
            Nome:    {self.nome}
            Data:    {self.data}
            Paginas: {self.paginas}
            Assunto: {self.assunto}
                """)
    def mostrarConteudo(self):
        print(f"""
            Conteudo: {self.conteudo}
                """)
        
class Artigo(Publicacao):
    def __init__(self, data, conteudo, nome, paginas, assunto, tangivel):
        super().__init__(data, conteudo)
        self.nome = nome
        self.paginas = paginas
        self.assunto = assunto
        self.tangivel = tangivel

    def mostrarDetalhes(self):
        print(f"""
  
            Nome:    {self.nome}
            Data:    {self.data}
            Paginas: {self.paginas}
            Assunto: {self.assunto}
            Tangível:{self.tangivel}

                """)
    def mostrarConteudo(self):
        print(f"""
              
            Conteudo: {self.conteudo}

                """)
        
# livro
print("LIVRO:")
livroData = input("Defina a data do Livro: ")
livroConteudo = input("Defina o Conteudo do Livro: ")
livroNome = input("Defina o Nome do Livro: ")
livroPaginas = int(input("Defina as paginas do Livro: "))

livro = Livro(livroData, livroConteudo, livroNome, livroPaginas)
livro.mostrarDetalhes()
livro.mostrarConteudo()

print("\nREVISTA:")
# revista
revistaData = input("Defina a data do Revista: ")
revistaConteudo = input("Defina o Conteudo do Revista: ")
revistaNome = input("Defina o Nome do Revista: ")
revistaPaginas = int(input("Defina as paginas do Revista: "))
revistaAssunto = input("defina o assunto da Revista: ")

revista = Revista(revistaData, revistaConteudo, revistaNome, revistaPaginas, revistaAssunto)
revista.mostrarDetalhes()
revista.mostrarConteudo()

print("\ARTIGO:")
# revista
artigoData = input("Defina a data do Artigo: ")
artigoConteudo = input("Defina o Conteudo do Artigo: ")
artigoNome = input("Defina o Nome do Artigo: ")
artigoPaginas = int(input("Defina as paginas do Artigo: "))
artigoAssunto = input("Defina o assunto do Artigo: ")
artigoTangivel = input("O artigo é tangivel? (sim) || (não): ")

artigo = Artigo(artigoData, artigoConteudo, artigoNome, artigoPaginas, artigoAssunto, artigoTangivel)
artigo.mostrarDetalhes()
artigo.mostrarConteudo()