class Produto:
    def __init__(self, id, nome, descricao, valor):
        if id != 0:
            self.id = id
        else:
            raise ValueError('O identificador deve ser diferente de zero')
        self.nome = nome
        self.descricao = descricao
        self. valor = valor


class Endereco:
    def __init__(self, rua, cep, cidade):
        self.rua = rua
        self.cep = cep
        self.cidade = cidade

    def __str__(self):
        return f'{self.rua}, {self.cidade} - {self.cep}'

    def __repr__(self):
        return f'{self.rua}, {self.cidade} - {self.cep}'


class Cliente:
    def __init__(self, nome, cpf, rua, cep, cidade):
        self.nome = nome
        self.cpf = cpf
        self.endereco = Endereco(rua, cep, cidade)


class Compra:
    def __init__(self, data, cliente, produtos):
        self.data = data
        self.cliente = cliente
        self.produtos = produtos

    def valor_compra(self):
        valor = 0
        for dict_prod in self.produtos:
            valor += dict_prod['produto'].valor * dict_prod['quantidade']
        return valor


if __name__ == '__main__':
    cad_prod = 'Cadastrar Produto'
    cad_compra = 'Cadastrar Compra'

    produtos = []
    compras = []
    while True:
        opcao = int(input(
            f'escolha uma opção: \n'
            f'1 - {cad_prod} \n'
            f'2 - {cad_compra} \n'
            f'3 - Sair \n'
        ))

        if opcao == 1:
            id = int(input('identificador: '))
            nome = input('nome: ')
            descricao = input('descricao: ')
            valor = float(input('valor: '))
            prod = Produto(id, nome, descricao, valor)
            produtos.append(prod)
            print('Produto criado com sucesso!')
        elif opcao == 2:
            if len(produtos) > 0:
                data = input('data: ')
                print('dados de endereco do cliente')
                rua = input('rua do cliente: ')
                cep = input('cep do cliente: ')
                cidade = input('cidade do cliente: ')
                print('dados pessoais do cliente')
                nome = input('nome cliente: ')
                cpf = input('cpf: ')
                cliente = Cliente(nome, cpf, rua, cep, cidade)
                cod_prod = list(map(int, input('identificadores dos produtos: ').split()))
                produtos_compra = []
                for prod in produtos:
                    if prod.id in cod_prod:
                        num_prod = int(input(f'quantidade de produtos {prod.id}: '))
                        produtos_compra.append(
                            {
                                'produto': prod,
                                'quantidade': num_prod
                            }
                        )

                c = Compra(data, cliente, produtos_compra)
                compras.append(c)
            else:
                print('Adicione um produto primeiro.')
        elif opcao == 3:
            break
        else:
            print('Escolha apenas as opções 1, 2 ou 3')
    print('Listando as compras:')
    for compra in compras:
        print(f'Data da compra: {compra.data}')
        print(f'CPF: {compra.cliente.cpf}')
        print(f'Nome do comprador: {compra.cliente.nome}')
        print(f'Valor total: {compra.valor_compra()}')
