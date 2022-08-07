cidade = input('Digite o nome de uma cidade: ')

correcao = cidade.capitalize()

nomeSanto = correcao.find('Santo')

if nomeSanto == 0:
    print('Tem nome de Santo')
else:
    print('Não tem nome de Santo')

