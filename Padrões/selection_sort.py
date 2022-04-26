def selectionsort(lista):
    for i in range(len(lista) - 1, 0, -1):
        posicao_do_maior = 0
        for j in range(1, i + 1):
            if lista[j] > lista[posicao_do_maior]:
                posicao_do_maior = j

        elemento = lista[i]
        lista[i] = lista[posicao_do_maior]
        lista[posicao_do_maior] = elemento


lista = [54,26,93,17,77,31,44,55,20]
selectionsort(lista)
print(lista)
