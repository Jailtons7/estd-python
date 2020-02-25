# Neste módulo estão as funções sobre a lista 2 - strings.
# O desafio é usar o mínimo possível de funções built-in do Python


def para_maiuscula(frase):
    '''
    :param frase: String
    :return: String, a frase em maiúsculas
    '''
    minusculas = ['a','à','á','ã','â','b','c','ç','d','e','é','ê','f','g','h','i','í','j','k','l','m',
                  'n','o','ó','ô','õ','p','q','r','s','t','u','ú','v','w','x','y','z']
    maiusculas = ['A','À','Á','Ã','Â','B','C','Ç','D','E','É','Ê','F','G','H','I','Í','J','K','L','M',
                  'N','O','Ó','Ô','Õ','P','Q','R','S','T','U','Ú','V','W','X','Y','Z']

    resultado = ''
    for letra in frase:
        if letra in minusculas:
            indice = minusculas.index(letra)
            resultado += maiusculas[indice]
        else:
            resultado += letra
    return resultado


def retira_espaco(frase):
    '''
    :param frase: string
    :return: Frase sem espaços no início e no fim
    '''
    tamanho = comprimento(frase)
    cont_ini = 0
    cont_fim = 0
    for i in range(0, tamanho-1):
        if frase[i] == ' ':
            cont_ini += 1
        else:
            break
    for i in range(1, tamanho-1):
        if frase[-i] == ' ':
            cont_fim += 1
        else:
            break
    final = tamanho - cont_fim
    return frase[cont_ini:final]


def comprimento(iteravel):
    '''
    :param iteravel: pode ser string, lista, tupla...
    :return: tamanho da do iterável (minha versão da função len())
    '''
    contador = 0
    for item in iteravel:
        contador += 1
    return contador


def eh_palindroma(palavra):
    '''
    :param palavra: string
    :return: True, se a palavra for palíndroma e False, caso contrário.
    '''
    palavra = para_maiuscula(retira_espaco(palavra))
    tamanho = comprimento(palavra)
    for i in range(0, tamanho):
       if (palavra[i] != palavra[-i-1]):
           return False
    return True


def quantidade_palavras(texto):
    '''
    :param texto: string
    :return: inteiro, quantidade de palavras no texto
    '''
    texto_liquido = retira_espaco(texto)
    tamanho = comprimento(texto_liquido)
    contador = 1
    anterior = ''
    for i in range(0, tamanho):
        if texto_liquido[i] == ' ' and anterior != ' ' and anterior != '\n':
            contador += 1
        anterior = texto_liquido[i]
    return contador


def ultimo_nome(nome_completo):
    '''
    :param nome_completo: string
    :return: string, ultimo nome
    '''
    nome = retira_espaco(nome_completo)
    tamanho = comprimento(nome)
    contador = 0
    for i in range(1, tamanho+1):
        if nome[-i] != ' ':
            contador += 1
        else:
            break
    fatiamento = tamanho - contador
    return nome[fatiamento:]


def formato_aereas(nome_completo):
    '''
    :param nome_completo: String
    :return: String, nome no formato das companhias aéreas
    '''
    nome = retira_espaco(nome_completo)
    primeiro = ''
    for letra in nome:
        if letra != ' ':
            primeiro += letra
        else:
            break
    ultimo = ultimo_nome(nome)
    formato = ultimo + '/' + primeiro
    return formato


def formato_referencia(nome_completo):
    '''
    :param nome_completo: String
    :return: String, nome no formato de referência bibliográfica
    '''
    ultimo = para_maiuscula(ultimo_nome(nome_completo))
    alcance = comprimento(nome_completo) - comprimento(ultimo)
    nome_aux = para_maiuscula(nome_completo[0])+'.'
    for i in range(alcance-1):
        if nome_completo[i] == ' ':
            nome_aux += para_maiuscula(nome_completo[i+1])+'.'
    return '%s,%s' % (ultimo, nome_aux)


def gera_login(nome_completo):
    nome = retira_espaco(nome_completo)
    anterior = ''
    usuario = nome[0]
    for i in range(comprimento(nome)):
        if nome[i] == ' ' and anterior != ' ':
            usuario += nome[i+1]
        anterior = nome[i]
    return  usuario

