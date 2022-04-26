def bubblesort(lista):
    for passagens in range(len(lista) - 1, 0, -1):
        for i in range(passagens):
            if lista[i] > lista[i + 1]:
                elemento = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = elemento

lista = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
bubblesort(lista)
print(lista)
