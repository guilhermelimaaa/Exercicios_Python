nome = []
idade = []
maiorIdade = 0
menorIdade = 9999999999999999999999999999999999999999999999999

for cont in range(0,5,1):
    nome[cont] = input('Digite o nome da pessoa: ')
    idade[cont] = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa(M/F): ')

    if sexo == 'm' or sexo == 'M':
        if idade[cont] > maiorIdade:
            maiorIdade = idade[cont]

        if idade[cont] < menorIdade:
            menorIdade = idade[cont]

        if idade[cont] < menorIdade:
            menorIdade = idade[cont]
        elif idade[cont] > maiorIdade:
            maiorIdade = idade[cont]

    homemVelho = nome[cont]



print('A Média é:', (idade[1] + idade[2] + idade[3] + idade[5]) / 5)