def insertion_sort(lista):
    for i in range(1, len(lista)):
        valor_atual = lista[i]
        posicao = i

        while posicao > 0 and lista[posicao - 1] > valor_atual:
            lista[posicao] = lista[posicao - 1]
            posicao = posicao - 1

        lista[posicao] = valor_atual


#lista = [54,26,93,17,77,31,44,55,20]
alist = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
#insertion_sort(lista)
insertion_sort(alist)
#print(lista)
print(alist)