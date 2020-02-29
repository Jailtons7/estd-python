# Soluções da lista sobre recursividade
from lista_strings import comprimento

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)


def inverte_palavra(palavra):
    tamanho = comprimento(palavra)
    invertida = palavra[tamanho-1]
    nova_palavra = palavra[0:tamanho-2]
    return invertida + inverte_palavra[nova_palavra]


def inverte_palavra(palavra):
    tamanho = len(palavra)
    if tamanho >= 1:
      invertida = palavra[tamanho-1]
      nova_palavra = palavra[0:tamanho-1]
      return invertida + str(inverte_palavra(nova_palavra))
