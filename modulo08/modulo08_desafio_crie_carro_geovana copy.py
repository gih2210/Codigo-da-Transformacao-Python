class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and not livro.emprestado:
                livro.emprestado = True
                print("Livro emprestado.")
                return
        print("Livro não disponível.")

    def mostrar_livros(self):
        for livro in self.livros:
            status = "Emprestado" if livro.emprestado else "Disponível"
            print(livro.titulo, "-", status)

biblioteca = Biblioteca()

biblioteca.adicionar_livro(Livro("Dom Casmurro"))
biblioteca.adicionar_livro(Livro("O Pequeno Príncipe"))

biblioteca.mostrar_livros()
biblioteca.emprestar_livro("Dom Casmurro")
biblioteca.mostrar_livros()