def insere_ordenanda(lista, num):
    lista.append(num)
    
    for i in range(len(lista) - 1, -1, -1):
        if num > lista[i]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            
    return lista