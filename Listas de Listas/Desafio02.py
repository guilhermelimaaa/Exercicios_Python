numeros = []
escolha = 'S'
cont = 0

while escolha == 'S' or escolha == 's':
    addNum = input('Digite um número para adicionar a lista: ')
    if addNum not in numeros:
        numeros.append(addNum)
    else:
        print('Número já adicionado =(')

    print(numeros)

    escolha = input('Deseja continuar ? (S/N): ')



