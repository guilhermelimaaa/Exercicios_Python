pessoas = {}
nome = []
sexo = []
idade = []
mulheres = []
idadeAcima = []

qtdPessoas = int(input('Digite a quantidade de pessoas que deseja cadastrar: '))

for cont in range(qtdPessoas):
    entradaNome = input('\nDigite o nome da pessoa: ')
    nome.append(entradaNome)
    entradaSexo = input('Digite o sexo da pessoa (M/F): ')
    sexo.append(entradaSexo)
    if entradaSexo == 'F' or entradaSexo == 'f':
        mulheres.append(entradaNome)
    entradaIdade = int(input('Digite a idade da pessoa: '))
    idade.append(entradaIdade)

pessoas ['Nome'] = nome
pessoas ['Sexo'] = sexo
pessoas ['Idade'] = idade

mediaIdade = sum(idade) / qtdPessoas

for cont in range(qtdPessoas):
    if idade[cont] > mediaIdade:
        idadeAcima.append(nome[cont])


print(pessoas)
print('O Total de pessoas cadastradas foi:', qtdPessoas)
print('A Média das idades é:', sum(idade)/qtdPessoas)
print('As mulheres cadastradas são:', mulheres)
print('As pessoas com idade acima da média são:', idadeAcima)