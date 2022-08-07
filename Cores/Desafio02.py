numero = int(input('Digite um número: '))
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')

escolha = input('Escolha uma das bases: ')

if escolha == '1':
    if numero != 0 or numero != 1:
        print('\033[1;37;43m', bin(numero), '\033[m')
    else:
        print(numero)
elif escolha == '2':
    if numero < 0 or numero > 8:
        print('\033[1;97;44m', oct(numero), '\033[m')
    else:
        print(numero)
elif escolha == '3':
    if numero < 0 or numero > 9:
        print('\033[1;37;45m', hex(numero), '\033[m')
    else:
        print(numero)