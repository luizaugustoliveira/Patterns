lista = [1,2,2,2,2,2,3]

for i in range(len(lista) - 1, -1, -1):
    if lista[i] == 2:
        lista.pop(i)

print(lista)