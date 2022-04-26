#Padrão Conta ímpares
def conta_impares(lista):
    contador = 0

    for elemento in lista:
        if elemento % 2 == 1:
            contador += 1 

    return contador