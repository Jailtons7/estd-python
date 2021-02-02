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


if __name__ == '__main__':
    autores = []
    while True:
        opcao = int(input('selecione uma opção: \n'
                          '1 - Cadastrar autor \n'
                          '2 - Listar nomes de Autores \n'
                          '3 - Recuperar autor por CPF \n'
                          '4 - Deletar autor por CPF \n'
                          '5 - Cadastrar livro \n'))
        if opcao == 1:
            print('Insira os dados do autor para cadastrá-lo:')
            nome = input('Nome: ')
            endereco = input('Endereço: ')
            cpf = input('CPF: ')
            num_obras = input('Número de obras: ')
            descr_pessoal = input('Descricao pessoal: ')
            autores.append(Autor(nome, endereco, cpf, num_obras, descr_pessoal))
            print('Autor inserido no sistema!')
        elif opcao == 2:
            print('listando os autores: ')
            for autor in autores:
                print(autor.nome)
        elif opcao == 3:
            cpf_input = input('Insira o cpf: ')
            cpfs = []
            for autor in autores:
                if autor.cpf == cpf_input:
                    cpfs.append(autor.cpf)
                    print(
                        f'Nome: {autor.nome} \n'
                        f'Endereco: {autor.endereco} \n'
                        f'CPF: {autor.cpf} \n'
                        f'Número de obras: {autor.num_obras} \n'
                        f'Descrição pessoal: {autor.descr_pessoal} \n'
                    )
            if cpf_input not in cpfs:
                print('Não há autor com o CPF informado')
        elif opcao == 4:
            cpf_input = input('Insira o cpf: ')
            cpfs2 = []
            for autor in autores:
                if autor.cpf == cpf_input:
                    cpfs2.append(autor.cpf)
                    autores.remove(autor)
                    print(f'Autor {autor.nome} deletado com sucesso.')
            if cpf_input not in cpfs2:
                print('Não há autor com o CPF informado')
        elif opcao == 5:
            print('Insira os dados do livro para cadastrá-lo:')
            isbn = input('Nome: ')
            titulo = input('Nome: ')
            ano = input('Nome: ')
            autores = input('Nome: ')
        else:
            break
