ano = int(input('Digite um ano do calendário gregoriano: '))

if ano == 0:
    print('O Ano 2021 não é bissexto')
elif ano % 4 == 0:
    print('O Ano', ano, 'é bissexto')
else:
    print('O Ano', ano, 'não é bissexto')