#Padrão Busca Linear
def busca_linear(lista, elemento):
    for posicao in range(len(lista)):
        if lista[posicao] == elemento:           
            return posicao
    return "não achei o elemento"