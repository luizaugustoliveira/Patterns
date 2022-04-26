#Padrão Conta Pares
def conta_pares(lista):
    contador = 0 

    for elemento in lista:
        if elemento % 2 == 0:
            contador += 1

    return contador