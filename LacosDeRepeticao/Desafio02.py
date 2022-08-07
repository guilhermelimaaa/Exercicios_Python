soma = 0

for cont in range(6):
    num = int(input('Digite um valor: '))

    if num % 2 == 0:
        soma = num + num

print('A Soma entre os pares é:', soma)