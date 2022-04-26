#Padrão Conta Múltiplos
def conta_multiplos(lista, num):
    contador = 0

    for elemento in lista:
        if elemento % num == 0:
            contador += 1

    return contador