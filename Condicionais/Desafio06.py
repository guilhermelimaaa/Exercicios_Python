maior = 0
menor = 0
for cont in range(3):
    numero = int(input('Digite um número: '))
    if numero > maior:
        maior = numero
    elif numero <= menor and numero < maior:
        menor = numero

print('O Maior é', maior, 'e o menor é', menor)
