import arranjos


def bubble_sort(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
            print(a)


if __name__ == '__main__':
    """
    testes de mesa
    """
    print("Bubble Sort arranjo 1:")
    bubble_sort(arranjos.arranjo_1)

    print("Bubble Sort arranjo 2:")
    bubble_sort(arranjos.arranjo_2)

    print("Bubble Sort arranjo 3:")
    bubble_sort(arranjos.arranjo_3)

    print("Bubble Sort arranjo 4:")
    bubble_sort(arranjos.arranjo_4)
