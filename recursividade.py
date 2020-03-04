# Soluções da lista sobre recursividade

from lista_strings import comprimento

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)


def inverte_palavra(palavra):
    '''
    :param palavra: string
    :return: string, a palavra invertida
    '''
    tamanho = comprimento(palavra)
    if tamanho >= 1:
        invertida = palavra[-1]
        nova_palavra = palavra[0:tamanho-1]
        return invertida + str(inverte_palavra(nova_palavra))
    else:
        return ''


def conta_letra(letra, palavra):
    '''
    :param letra, palavra: string
    :return: inteiro, quantas vezes a "letra" aparece na "palavra"
    '''
    tamanho = comprimento(palavra)
    if tamanho >= 1:
        if palavra[0] == letra:
            nova_palavra = palavra[1:]
            return 1 + conta_letra(letra, nova_palavra)
        else:
            nova_palavra = palavra[1:]
            return conta_letra(letra, nova_palavra)
    else:
        return 0


def n_primeiros_decrescente(numero):
    '''
    :param numero: inteiro
    :return: None, apenas imprime os n primeiros números em ordem crescente começando do zero
    '''
    if numero >= 0:
        novo_numero = numero - 1
        print(novo_numero+1)
        n_primeiros_decrescente(novo_numero)
