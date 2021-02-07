class Pilha:
    itens = []

    def push(self, elem):
        self.itens.append(elem)

    def top(self):
        if self.has_element():
            return self.itens[-1]

    def pop(self):
        if self.has_element():
            topo = self.top()
            self.itens.remove(topo)
            return topo
        return None

    def has_element(self):
        return len(self.itens) > 0


if __name__ == '__main__':
    input_ = input('RPN: ').split()
    operadores = ['*', '/', '+', '-']
    p = Pilha()
    for element in input_:
        if element not in operadores:
            p.push(element)
        else:
            val_1 = p.pop()  # Recupera o valor do topo
            val_2 = p.pop()  # Recupera o novo valor do topo

            p.push(eval(f'{val_2} {element} {val_1}'))  # Adiciona o resultado
    print(f'Resultado {p.itens[0]}')
