"""20. Loja de Livros - Herança:
Modele uma loja de livros com classes para Livro, Ebook e Audiolivro, que herdam da classe base 
Produto. Cada classe deve ter métodos para mostrar detalhes e preço."""

class Produto:
    def __init__(self, nome, genero, preco):
        self.nome = nome
        self.genero = genero
        self.preco = preco
    
    def mostrar_detalhes(self):
        pass

    def mostrar_preco(self):
        print(f"preço: {self.preco}")

class Livro(Produto):
    def __init__(self, nome, genero, preco, paginas):
        super().__init__(nome, genero, preco)
        self.paginas = paginas
    
    def mostrar_detalhes(self):
        print(f"""
nome:    {self.nome}
genero:  {self.genero}
paginas: {self.paginas}
        """)

class Ebook(Produto):
    def __init__(self, nome, genero, preco, paginas):
        super().__init__(nome, genero, preco)
        self.paginas = paginas
    
    def mostrar_detalhes(self):
        print(f"""
nome:    {self.nome}
genero:  {self.genero}
paginas: {self.paginas}
        """)

class AudioLivro(Produto):
    def __init__(self, nome, genero, preco, horasAudio):
        super().__init__(nome, genero, preco)
        self.horasAudio = horasAudio

    def mostrar_detalhes(self):
        print(f"""
nome:           {self.nome}
genero:         {self.genero}
Horas de Audio: {self.horasAudio}
        """)

# livro
print("\n")
nomeLivro = input("digite o nome do livro: ")
generoLivro = input("digite o genero do livro: ")
precoLivro = float(input("digite o preço do livro: "))
paginasLivro = int(input("digite as paginas do livro: "))

livro1 = Livro(nomeLivro, generoLivro, precoLivro, paginasLivro)
livro1.mostrar_detalhes()
livro1.mostrar_preco()


# ebook
print("\n")
nomeEbook = input("digite o nome do Ebook: ")
generoEbook = input("digite o genero do Ebook: ")
precoEbook = float(input("digite o preço do Ebook: "))
paginasEbook = int(input("digite as paginas do Ebook: "))

ebook1 = Ebook(nomeEbook, generoEbook, precoEbook, paginasEbook)
ebook1.mostrar_detalhes()
ebook1.mostrar_preco()


# Audiolivro
print("\n")
nomeAudioLivro = input("digite o nome do Audio Livro: ")
generoAudioLivro = input("digite o genero do Audio Livro: ")
precoAudioLivro = float(input("digite o preço do Audio Livro: "))
horasAudioLivro = float(input("digite as horas do Audio Livro: "))

audioLivro1 = AudioLivro(nomeAudioLivro, generoAudioLivro, precoAudioLivro, horasAudioLivro)
audioLivro1.mostrar_detalhes()
audioLivro1.mostrar_preco()