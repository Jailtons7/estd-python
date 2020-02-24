# Neste módulo estão os scripts da revisão sobre funções

def fatorial(n):
    '''
    :param n: inteiro
    :return: inteiro, fatorial de n
    '''
    if n < 0:
        print('não existe fatorial de um número negativo')
    elif n < 2:
        return 1
    else:
        return n * fatorial(n-1)

def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def par_ou_impar(n):
    if n % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

def maior_de_2(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

def maior_de_3(a,b,c):
    if a >= b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
def dia_da_semana(num):
    numeros = [1,2,3,4,5,6,7]
    dias = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']
    if num in numeros:
        indice = numeros.index(num)
        return dias[indice]
    else:
        return 'Dia inválido'

def hipotenusa(cat1, cat2):
    '''
    :param cat1: float
    :param cat2: float
    :return: float, hipotenusa usando o teorema de pitágoras
    '''
    hipotenusa = (cat1 ** 2 + cat2 ** 2) ** 0.5
    return hipotenusa

def eh_bissexto(ano):
    '''
    :param ano: inteiro
    :return: Booleano, True se for ano bissexto, False, caso contrário
    '''
    if (ano % 4 == 0):
        if (ano % 100 == 0 and ano % 400 != 0):
            return False
        else:
            return True
    else:
        return False

def eh_data_valida(dia, mes, ano):
    '''
    :param dia, mes, ano: inteiros
    :return: booleano; True, se for data válida. False, caso contrário
    '''
    bissexto = eh_bissexto(ano)
    meses_30 = [4, 6, 9, 11]
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    elif dia > 29 and mes == 2:
        return False
    elif dia == 29 and mes == 2 and not bissexto:
        return False
    elif mes in meses_30 and dia > 30:
        return False
    else:
        return True
