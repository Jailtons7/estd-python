class Autor:
    def __init__(self, nome, endereco, cpf, num_obras, descr_pessoal):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.num_obras = num_obras
        self.descr_pessoal = descr_pessoal


class Livro:
    def __init__(self, isbn,  titulo, ano, autores):
        self.isbn = isbn
        self.titulo = titulo
        self.ano = ano
        self.autores = autores


class Aquisicao:
    def __init__(self,  livro, data_aquisicao, custo):
        self.livro = livro
        self.data_aquisicao = data_aquisicao
        self.custo = custo


