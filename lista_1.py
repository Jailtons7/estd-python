SEXO = ['m', 'f']
COR_OLHOS = ['a', 'v', 'c']
COR_CABELO = ['l', 'c', 'p']


def questao_1():
    """
    Determina a idade do habitante mais velho e a porcentagem
    de mulheres loiras de olhos verdes com idade i tal que 18 <= i <= 35
    """
    count = 0
    while count < 100:
        try:
            idade = int(input('Idade: '))
        except ValueError:
            print('A idade deve ser um número')
            return None

        dados_adicionais = input('Sexo, olhos e cabelo (Separados por espaço)').split(' ')
        if len(dados_adicionais) == 1:
            break
        elif len(dados_adicionais) == 3:
            # Código aqui
            pass
        else:
            print('você separou por vírgulas?')
            break

        count += 1


def questao_5():
    lista = []
    while True:
        input_ = input().strip().split(' ')
        if len(input_) != 5:
            raise ValueError(
                'O número de dados de entrada deve ser igual a 5'
            )
        if input_[0] == 0:
            break
        if input_ not in lista:
            lista.append(input_)
