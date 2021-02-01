"""
Resolução da lista de exercícios de Estruturas de Dados
Os enunciados das questões estão no pdf em "listas_pdf/semana1.pdf"
"""

SEXO = ['m', 'f']
COR_OLHOS = ['a', 'v', 'c']
COR_CABELO = ['l', 'c', 'p']


def eh_palindroma(palavra):
    for i in range(len(palavra)):
        if palavra[i] != palavra[-i - 1]:
            return False
    return True


def questao_1():
    """
    Determina a idade do habitante mais velho e a porcentagem
    de mulheres loiras de olhos verdes com idade i tal que 18 <= i <= 35
    """
    maximum = 0
    count = 0
    dados = {}
    idades = []
    while maximum < 100:
        try:
            idade = int(input('Idade: ').strip())
        except ValueError:
            print('A idade deve ser um número')
            return None
        if idade == -1:
            break

        dados_entrada = input('Sexo, cabelo e olhos (Separados por espaço)').strip().split(' ')
        if len(dados_entrada) == 1:
            break
        elif len(dados_entrada) == 3:
            idades.append(idade)
            dados[count] = dados_entrada
        else:
            print('Você separou os 3 valores por espaço?')
            break

        maximum += 1
        count += 1

    tot = 0
    for key, value in dados.items():
        if 18 <= idades[key] <= 35 and value[0] == 'f' and value[1] == 'l' and value[2] == 'v':
            tot += 1

    percentual = tot / len(dados) * 100
    maior_idade = max(idades)
    print(f"mais velho: {maior_idade}")
    print(f"Mulheres com olhos verdes, loiras com 18 a 35 anos: {percentual}%")


def questao_2():
    """
    Resolve a questão 2 (listas_pdf/semana1.pdf)
    """
    n = int(input())
    lista_1 = []
    for _ in range(n):
        lista_1.append(input())

    lista_2 = []
    for _ in range(n):
        lista_2.append(input())

    for i in range(n):
        print(lista_1[i])
        print(lista_2[i])


def questao_3():
    """
    Resolve a questão 3 (listas_pdf/semana1.pdf)
    """
    n = int(input())
    array = list(map(int, input().strip().split(' ')))
    conjunto = set(array)
    if len(conjunto) != len(array) or len(conjunto) != n:
        raise ValueError(
            f'O número de elementos deve ser igual a {n}. '
            f'Repetições não são permitidas.'
        )

    min_ = min(array)
    index_ = array.index(min_)
    print(f'Menor valor: {min_}')
    print(f'Posição: {index_}')


def questao_4():
    """
    Dado o número de casos testes e as palavras testes
    separadas por espaço determina quantas delas são palíndromas
    """
    n = int(input())
    dicionario = dict()
    for i in range(n):
        dicionario[i] = input().split(' ')

    for key in dicionario:
        count = 0
        for palavra in dicionario[key]:
            if eh_palindroma(palavra):
                count += 1
        print(count)


def questao_5():
    lista = []
    while True:
        input_ = list(map(int, input().strip().split(' ')))
        if len(input_) != 5:
            print(
                'O número de dados de entrada deve ser igual a 5'
            )
            continue
        if input_[0] == 0:
            break
        if input_ not in lista:
            lista.append(input_)
    tempos = []
    for entrada in lista:
        meses_dif = entrada[3] - entrada[1]
        anos_dif = entrada[4] - entrada[2]
        meses = meses_dif + anos_dif * 12
        tempos.append(meses)

    index_ = tempos.index(max(tempos))
    print(lista[index_][0])


def questao_6():
    valores = []
    while True:
        input_ = list(map(int, input().strip().split(' ')))
        if len(input_) != 2:
            print(
                "Só é permito um salário e um número de filhos por entrada"
            )
            continue
        if input_[0] < 0:
            break
        valores.append(input_)
    salarios = [valor[0] for valor in valores]
    filhos = [valor[1] for valor in valores]
    count = 0
    maior = -1.0
    soma_salario = 0.0
    for sal in salarios:
        soma_salario += sal
        if sal > maior:
            maior = sal
        if sal <= 2500.0:
            count += 1

    soma_filhos = 0
    for fil in filhos:
        soma_filhos += fil

    n_salarios = len(salarios)
    media_salarios = soma_salario / n_salarios
    media_filhos = soma_filhos / len(filhos)
    percentual = count / n_salarios
    print(f'{media_salarios} {media_filhos} {maior} {percentual}')


def questao_7():
    raise NotImplementedError


def questao_8():
    """
    Determina a quantidade mínima de notas para se chegar a uma
    determinada quantia (notas disponíveis: 100, 50, 10, 5, 1)
    """
    notas = [100, 50, 10, 5, 1]
    quantia = int(input().strip())
    dict_notas = {}
    for nota in notas:
        if quantia // nota != 0:
            dict_notas[nota] = quantia // nota
            quantia = quantia % nota

    saidas = [f'{value} nota(s) de R$ {key}' for key, value in dict_notas.items() if value]
    for saida in saidas:
        print(saida)


def questao_9():
    n = int(input().strip())
    loop = 0
    lista = []
    matriz = []
    lista_interna = []
    while loop < n:
        input_ = input().strip()
        m = len(input_) ** 0.5
        if m % 1 == 0.0:
            count = 0
            last_loop = 1
            for i in range(len(input_)):
                if count < m:
                    lista_interna.append(input_[i])
                    count += 1
                    if last_loop % m == 0:
                        matriz.append(lista_interna)
                        lista_interna = list()
                        count = 0
                else:
                    count = 0
                    matriz.append(lista_interna)
                    lista_interna = list()
                    lista_interna.append(input_[i])
                last_loop += 1
            lista_interna = list()

        else:
            matriz.append(lista_interna.append('Inválido'))
        lista.append(matriz)
        loop += 1
    print(matriz)


def questao_10():
    raise NotImplementedError


if __name__ == '__main__':
    questao_1()
