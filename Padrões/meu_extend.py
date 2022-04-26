def meu_extend(lista1, lista2):
    lista = lista1
    for elemento in lista2:
        lista.append(elemento)

    return lista  

print(meu_extend([1,2], [3,4]))