class Fila:
    itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if self.has_element():
            return self.itens.pop(0)

    def has_element(self):
        return len(self.itens) > 0


if __name__ == '__main__':
    expression = input('Expressão numérica: ')

    abertura, fechamento = '(', ')'
    fila = Fila()
    anterior = ''
    for caracter in expression:
        if caracter == ' ':
            continue
        elif caracter != fechamento:
            fila.enqueue(caracter)


