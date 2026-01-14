from mini_biblioteca.livros import Livro
from mini_biblioteca.usuario import Usuario
from mini_biblioteca.emprestimos import Emprestimo


def main():
    usuario = Usuario("Maria", "U001")
    livro = Livro("1984", "George Orwell", "L001")

    emprestimo = Emprestimo(livro, usuario)

    print("Após empréstimo:")
    print("Livro disponível?", livro.disponivel)
    print("Empréstimo ativo?", emprestimo.ativo)

    emprestimo.devolver()

    print("\nApós devolução:")
    print("Livro disponível?", livro.disponivel)
    print("Empréstimo ativo?", emprestimo.ativo)


if __name__ == "__main__":
    main()
