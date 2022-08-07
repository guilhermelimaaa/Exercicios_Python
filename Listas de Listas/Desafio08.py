numeros = []
pares = []
impares = []

for cont in range(7):
    numDigitar = (int(input('Digite um número: ')))
    if numDigitar % 2 == 0:
        pares.append(numDigitar)
    elif numDigitar % 2 != 0:
        impares.append(numDigitar)

pares.sort()
impares.sort()

numeros = 'Pares: ' + str(pares) + ', Ímpares: '+ str(impares)

print(numeros)

