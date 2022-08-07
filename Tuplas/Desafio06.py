tuplaVariasPalavras = []

qtdCadastros = int(input('Digite a quantidade de dados que deseja inserir: '))

for cont in range(qtdCadastros):
    tuplaVariasPalavras.append(input('Digite uma palavra: ').upper())
    vogaisA = tuplaVariasPalavras[cont].count('A')
    vogaisE = tuplaVariasPalavras[cont].count('E')
    vogaisI = tuplaVariasPalavras[cont].count('I')
    vogaisO = tuplaVariasPalavras[cont].count('O')
    vogaisU = tuplaVariasPalavras[cont].count('U')
    print('A Palavra', tuplaVariasPalavras, 'contém as seguintes vogais: ')
    print('A'*vogaisA + 'E'*vogaisE + 'I'*vogaisI + 'O'*vogaisO + 'U'*vogaisU)
