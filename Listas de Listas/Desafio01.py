numeros = []
maior = -99999999999999999
menor = 999999999999999999
posmaior = 0
posmenor = 0

for cont in range (5):
    numeros.insert(cont, int(input('Digite um número: ' )))
    if numeros[cont] < menor:
        menor = numeros[cont]
        posmenor = cont

    if numeros[cont] > maior:
        maior = numeros[cont]
        posmaior = cont

    if numeros[cont] > maior:
        maior = numeros[cont]
        posmaior = cont

    if numeros[cont] < menor:
        menor = numeros[cont]
        posmenor = cont

print('O Maior número foi:', maior, 'na posição', posmaior)
print('O Menor número foi:', menor, 'na posição', posmenor)
