opcao = 'S'
pessoasDezoito = 0
homens = 0
mulheresVinte = 0

print('=======Cadastro de pessoas=======')

while opcao == 'S':
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa (M/F): ').upper()
    while sexo != 'F' and sexo != 'M':
        sexo = input('Digite o sexo da pessoa (M/F): ').upper()

    if idade > 18:
        pessoasDezoito+=1

    if sexo == 'M':
        homens+=1

    if sexo == 'F' and idade < 20:
        mulheresVinte+=1

    opcao = input('Deseja continuar ? (S/N): ').upper()
    while opcao != 'S' and opcao != 'N':
        opcao = input('Deseja continuar ? (S/N): ').upper()

print('A Quantidade de pessoas com mais de 18 anos é de:', pessoasDezoito)
print('A Quantidade de homens cadastrados é de:', homens)
print('A Quantidade de mulheres com menos de 20 anos é de:', mulheresVinte)
