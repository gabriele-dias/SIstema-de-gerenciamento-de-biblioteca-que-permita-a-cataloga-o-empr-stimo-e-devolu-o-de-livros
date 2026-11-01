class CadastroDeLivros:
    def __init__(self, titulo, autor, ano_publicacao, genero, id_livro, copias_disponiveis):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero
        self.id_livro = id_livro
        self.copias_disponiveis = copias_disponiveis

    def disponivel(self):
        return self.copias_disponiveis > 0
