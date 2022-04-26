def meu_in(sequencia, elemento):
    for valor in sequencia:
        if valor == elemento:          
            return True
    return False

palavras = input().split()
letra = input()

for indice in range(len(palavras)):
    if meu_in(palavras[indice], letra):
        print(indice)