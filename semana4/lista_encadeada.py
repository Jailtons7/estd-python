class No:
    tamanho = 0
    proximo = None
    identificador = None
    inicio = 0
    preenchido = "O"

    def __repr__(self):
        return f"{self.tamanho} > {self.proximo}"


class ListaEncadeada:
    cabeca = No()

    def __repr__(self):
        return f'{self.cabeca}'

    def adicionar(self, id_processo, tamanho, estrategia=None):
        atual = self.cabeca
        ini = 0
        while atual.proximo is not None:
            atual = atual.proximo
            ini = ini + atual.tamanho
        novo_elem = No()
        novo_elem.tamanho = tamanho
        novo_elem.inicio = ini
        novo_elem.identificador = id_processo
        atual.proximo = novo_elem

    def deletar(self, id_processo):
        anterior = self.cabeca
        atual = self.cabeca.proximo

        while atual is not None:
            if atual.identificador != id_processo:
                anterior = atual
                atual = atual.proximo
            else:
                atual.preenchido = "D"
                anterior = atual
                atual = atual.proximo


        if atual is not None:
            anterior.proximo = atual.proximo

    def imprimir(self):
        atual = self.cabeca.proximo
        saida = ''
        while atual is not None:
            saida += f'[{atual.preenchido} | {atual.inicio} | {atual.tamanho}] > '
            atual = atual.proximo
        print(saida)


if __name__ == '__main__':
    l = ListaEncadeada()
    l.adicionar(1, 2)
    l.adicionar(2, 4)
    l.adicionar(3, 5)
    l.adicionar(4, 8)
    l.adicionar(5, 7)
    l.deletar(2)
    l.deletar(3)
    l.imprimir()
