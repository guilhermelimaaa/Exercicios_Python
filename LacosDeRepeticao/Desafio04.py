divisiveis = 0

num = int(input('Digite um numero: '))

for cont in range(1,num+1):
    if num % cont == 0:
        divisiveis += 1
        print('\033[1;32m',cont, '\033[m', end='')
    else:
        print('\033[1;31m',cont, '\033[m', end='')


if divisiveis < 3:
    print('\n', num, 'é um número primo')
else:
    print('\n', num, 'não é um número primo')


