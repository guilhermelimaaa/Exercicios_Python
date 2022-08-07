maior = 0
menor = 9999999999999999999999999999999999999999999999999
for cont in range(5):
    peso = float(input('Digite um peso: '))
    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

    if peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso


print('Maior peso:', maior, 'Kg')
print('Menor peso:', menor, 'Kg')

