from mini_biblioteca.livros import Livro
from mini_biblioteca.usuario import Usuario

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario):
        if not livro.disponivel:
            raise ValueError("Livro indisponível para empréstimo")

        self.livro = livro
        self.usuario = usuario
        self.ativo = True

        livro.disponivel = False

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True
