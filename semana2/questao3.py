class Banco:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class Conta:
    def __init__(self, id, id_usuario, id_banco, saldo):
        self.id = id
        self.id_usuario = id_usuario
        self.id_banco = id_banco
        self.saldo = saldo


class Transferencia:
    def __init__(self, id, id_c_origem, id_c_destino, valor):
        self.id = id
        self.id_c_origem = id_c_origem
        if id_c_origem != id_c_destino:
            self.id_c_destino = id_c_destino
        else:
            raise ValueError('A conta de destino deve ser diferente da origem')
        self.valor = valor


class Deposito:
    def __init__(self, id, id_conta, valor):
        self.id = id
        self.id_conta = id_conta
        self.valor = valor


class Saque:
    def __init__(self, id, id_conta, valor):
        self.id = id
        self.id_conta = id_conta
        self.valor = valor


if __name__ == '__main__':
    usuarios = []
    bancos = []
    contas = []
    while True:
        opcao = int(input('selecione uma opção: \n'
                          '1 - Criar usuário \n'
                          '2 - Criar banco \n'
                          '3 - Criar conta \n'
                          '4 - Depositar \n'
                          '5 - Sacar \n'
                          '6 - Transferência \n'
                          '7 - Saldo \n'
                          '8 - Transações \n'
                          '9 - Sair \n'))
        if opcao == 1:
            id_ = input('identificador do usuário: ')
            nome = input('nome do usuário: ')
            usuarios.append(Usuario(id_, nome))
            print('Usuário criado com sucesso.')
        elif opcao == 2:
            id_ = input('identificador do usuário: ')
            nome = input('nome do usuário: ')
            bancos.append(Banco(id_, nome))
            print('banco criado com sucesso.')
        elif opcao == 3:
            id_ = input('identificador: ')
            id_usuario = input('identificador do usuário: ')
            id_banco = input('identificador do banco: ')
            saldo = float(input('saldo: ').strip().replace(',', '.'))
            contas.append(Conta(id_, id_usuario, id_banco, saldo))
            print('Conta criada com sucesso.')

        elif opcao == 4:
            id_ = input('id da transferência: ')
            id_conta = input('id da conta: ')
            valor = float(input('valor: ').strip().replace(',', '.'))
            ids_contas = [cont.id for cont in contas]
            if id_conta in ids_contas:
                for conta in contas:
                    if id_conta == conta.id:
                        conta.saldo += valor
                        print(f'novo saldo: {conta.saldo}')
            else:
                print('conta não encontrada')
        elif opcao == 5:
            id_ = input('identificador: ')
            id_conta = input('identificador da conta: ')
            valor = float(input('valor: ').replace(',', '.').strip())
            ids_contas = [cont.id for cont in contas]
            if id_conta in ids_contas:
                for conta in contas:
                    if id_conta == conta.id:
                        conta.saldo -= valor
                        print(f'novo saldo: {conta.saldo}')
            else:
                print('conta não encontrada')
        elif opcao == 6:
            pass
        elif opcao == 7:
            pass
        elif opcao == 8:
            pass
        else:
            break
