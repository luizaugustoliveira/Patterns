#Padrão Filtro
def filtra(lista ,num):
    nova_lista = []
    
    for elemento in lista:
        if elemento != num:
            nova_lista.append(elemento)
    
    return nova_lista