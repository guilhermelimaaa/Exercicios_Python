pessoas = []
escolha = 'S'
menor = 999999999999999
maior = -9999999999999999
pesoMaior = ''
pesoMenor = ''


while escolha == 's' or escolha == 'S':
    pessoas.append(input('Digite um nome: '))
    pessoas.append(float(input('Digite um peso: ')))

    for cont in range(1,len(pessoas),2):
        if pessoas[cont] < menor:
            menor = pessoas[cont]
            pesoMenor = pessoas[cont-1]

        if pessoas[cont] > maior:
            maior = pessoas[cont]
            pesoMaior = pessoas[cont-1]

        if pessoas[cont] > maior:
            maior = pessoas[cont]
            pesoMaior = pessoas[cont-1]

        if pessoas[cont] < menor:
            menor = pessoas[cont]
            pesoMenor = pessoas[cont-1]


    escolha = input('Deseja continuar ? (S/N): ')

print('\nForam cadastradas', int(len(pessoas) / 2), 'pessoas')
print(pesoMaior, 'foi a pessoa mais pesada')
print(pesoMenor, 'foi a pessoa mais leve')
