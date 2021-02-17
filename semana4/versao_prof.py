class No:
    valor = 0
    proximo = None


class Lista:
    cabeca = No()

    def adicionar(self, novoValor):
        atual = self.cabeca
        while atual.proximo != None:
            atual = atual.proximo
        novoElemento = No()
        novoElemento.valor = novoValor
        atual.proximo = novoElemento

    def remover(self, valor):
        anterior = self.cabeca
        atual = self.cabeca.proximo

        while atual != None and atual.valor != valor:
            anterior = atual
            atual = atual.proximo
        if atual != None:
            anterior.proximo = atual.proximo

    def imprimir_lista(self):
        atual = self.cabeca.proximo
        while atual != None:
            print(str(atual.valor) + ' -> ', end=" ")
            atual = atual.proximo
        print()


if __name__ == '__main__':
    l = Lista()
    l.adicionar(10)
    l.imprimir_lista()
    l.adicionar(20)
    l.imprimir_lista()
    l.adicionar(30)

    l.imprimir_lista()
    l.remover(20)
    l.imprimir_lista()
