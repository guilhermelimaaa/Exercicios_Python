from Utilidades import moeda

valor = float(input('Digite um valor: '))
uniMonetaria = input('Digite uma unidade monetária: ')
taxaAumento = float(input('Digite a taxa de aumento a ser atribuída ao valor (em %): '))
taxaReducao = float(input('Digite a taxa de redução a ser atribuída ao valor (em %): '))

'''
taxa = float(input('Digite a taxa a ser atribuída ao valor: '))

print('O valor aumentado em', taxa,'%', 'é de', moeda.aumentar(valor,taxa,moeda.moeda(uniMonetaria)))
print('O valor diminuido em', taxa,'%', 'é de', moeda.diminuir(valor,taxa,moeda.moeda(uniMonetaria)))
print('O valor dobrado é de', moeda.dobro(valor,moeda.moeda(uniMonetaria)))
print('O valor pela metade é de', moeda.metade(valor,moeda.moeda(uniMonetaria)))
'''

moeda.resumo(valor, taxaAumento, taxaReducao, uniMonetaria)
