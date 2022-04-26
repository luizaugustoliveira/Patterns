#Padrão Map Duplica Elementos
def duplica_elementos(lista):
    nova_lista = []
    
    for elemento in lista:
        nova_lista.append(elemento * 2)

    return nova_lista