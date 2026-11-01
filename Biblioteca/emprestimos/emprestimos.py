class EmprestimoDeLivros: 

    def __init__(self, livro, usuario, data_emprestimo, nome, numero_identificacao):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None # Inicialmente, a data de devolução é None
        self.nome = nome 
        self.numero_identificacao = numero_identificacao

def realizar_emprestimo(self):
    if self.livro.copias_disponiveis > 0:
        self.livro.copias_disponiveis -= 1

        print(
            f"Livro {self.livro.titulo} emprestado para {self.usuario.nome}"
        )
    else: 
        print("Livro Indisponivel")

