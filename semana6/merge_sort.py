import arranjos


def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista)//2

        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        merge_sort(listaDaEsquerda)
        merge_sort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k] = listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            print(f'lista da esquerda {listaDaEsquerda} --> lista da direita {listaDaDireita}')
            k += 1

        while i < len(listaDaEsquerda):
            lista[k] = listaDaEsquerda[i]
            print(f'lista da esquerda {listaDaEsquerda}')
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k] = listaDaDireita[j]
            print(f'lista da direita {listaDaDireita}')
            j += 1
            k += 1

    return lista


if __name__ == '__main__':
    print("Merge Sort arranjo 1:")
    merge_sort(arranjos.arranjo_1)

    print("Merge Sort arranjo 2:")
    merge_sort(arranjos.arranjo_2)

    print("Merge Sort arranjo 3:")
    merge_sort(arranjos.arranjo_3)

    print("Merge Sort arranjo 4:")
    merge_sort(arranjos.arranjo_4)
