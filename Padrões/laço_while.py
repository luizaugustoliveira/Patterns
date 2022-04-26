soma = 0
contagem = 0
while True:
    num = input()
    if num == "fim":
        break
    soma += int(num)
    contagem += 1

print(soma)
print(contagem)

