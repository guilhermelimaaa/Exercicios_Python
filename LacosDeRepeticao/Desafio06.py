maior = 0
menor = 0

for cont in range(8):
    nasc = int(input('Digite o ano de nascimento da pessoa: '))

    if 2021 - nasc >= 18:
        maior+=1
    else:
        menor+=1
print('Maiores de idade:', maior)
print('Menores de idade:', menor)