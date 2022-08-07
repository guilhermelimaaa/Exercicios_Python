numeros = []

numeros.insert(0, int(input('Digite um número: ')))
numeros.insert(1, int(input('Digite um número: ')))

while numeros[1] < numeros[0]:
    print('Número menor já inserido')
    numeros.insert(1, int(input('Digite um número: ')))

numeros.insert(2, int(input('Digite um número: ')))

while numeros[2] < numeros[1]:
    print('Número menor já inserido')
    numeros.insert(2, int(input('Digite um número: ')))

numeros.insert(3, int(input('Digite um número: ')))

while numeros[3] < numeros[2]:
    print('Número menor já inserido')
    numeros.insert(3, int(input('Digite um número: ')))

numeros.insert(4, int(input('Digite um número: ')))

while numeros[4] < numeros[3]:
    print('Número menor já inserido')
    numeros.insert(4, int(input('Digite um número: ')))


print(numeros[:5])
