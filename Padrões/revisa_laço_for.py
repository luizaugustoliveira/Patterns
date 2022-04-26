#Padrões:
#- min / max 
#- soma
#- contador
#- acumulador
#- filtro
#- map
#- busca_linear

#Padrão Menor
def menor_elemento(lista):
    menor = lista[0]

    for elemento in lista:
        if elemento < menor:
            menor = elemento

    return menor

#Padrão Maior
def maior_elemento(lista):
    maior = lista[0]

    for elemento in lista:
        if elemento > maior:
            maior = elemento 

    return maior

#Padrão Soma
def soma_elementos(lista):
    soma = 0

    for elemento in lista:
        soma += elemento 

    return soma

#Padrão Conta Pares
def conta_pares(lista):
    contador = 0 

    for elemento in lista:
        if elemento % 2 == 0:
            contador += 1

    return contador

#Padrão Conta ímpares
def conta_impares(lista):
    contador = 0

    for elemento in lista:
        if elemento % 2 == 1:
            contador += 1 

    return contador

#Padrão Conta Múltiplos
def conta_multiplos(lista, num):
    contador = 0

    for elemento in lista:
        if elemento % num == 0:
            contador += 1

    return contador

#Padrão Filtro
def filtra(lista ,num):
    nova_lista = []
    
    for elemento in lista:
        if elemento != num:
            nova_lista.append(elemento)
    
    return nova_lista

#Padrão Map Duplica Elementos
def duplica_elementos(lista):
    nova_lista = []
    
    for elemento in lista:
        nova_lista.append(elemento * 2)

    return nova_lista

#Padrão Busca Linear
def busca_linear(lista, elemento):
    for posicao in range(len(lista)):
        if lista[posicao] == elemento:           
            return posicao
    return "não achei o elemento"



numeros = [1,2,3,4,5,6,7,8,9]
print(numeros)

print(menor_elemento(numeros))
print(maior_elemento(numeros))
print(soma_elementos(numeros))
print(conta_pares(numeros))
print(conta_impares(numeros))
print(conta_multiplos(numeros, 2))
print(filtra(numeros, 7))
print(duplica_elementos(numeros))
print(busca_linear(numeros, 15))
print(busca_linear(numeros, 7))

