def shortbubblesort(lista):
    trocas = True
    passagens = len(lista) - 1
    while passagens > 0 and trocas:
        trocas = False
        for i in range(passagens):
            if lista[i] > lista[i + 1]:
                trocas = True
                elemento = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = elemento
            passagens -= 1

lista = [9,8,7,6,5]
shortbubblesort(lista)
print(lista)