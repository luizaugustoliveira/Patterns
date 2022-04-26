def meu_insert(lista, posicao, elemento):
    lista.append(elemento)
    for i in range(len(lista) - 1, -1, -1):
        if  i == posicao:
            break
        lista[i], lista[i - 1] = lista[i - 1], lista[i]

    return lista

print(meu_insert([1,2,3], 1, 8))