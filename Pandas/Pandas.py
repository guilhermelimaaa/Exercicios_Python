import pandas

def menu():
    while escolha != 0:
        print('[1] - Adicionar')
        print('[2] - Ler')
        print('[3] - Atualizar')
        print('[4] - Excluir')
        print('[0] - Sair')
        escolha = int(input('Digite sua escolha: '))

def adicionar():
    planilhaAdd = pandas.read_excel('paises.xlsx')
    linhas = len(planilhaAdd)
    planilhaAdd.loc[linhas + 1, 'País'] = input('Digite o nome do país: ')
    planilhaAdd.loc[linhas + 1, 'Capital'] = input('Digite a capital do país: ')
    planilhaAdd.loc[linhas + 1, 'População'] = input('Digite a população do país: ')
    planilhaAdd.to_excel('paises.xlsx', index=False)


def ler():
    planilhaLer = pandas.read_excel('paises.xlsx')
    print(planilhaLer)

'''
def atualizar():
'''
'''
def excluir():
'''

if __name__ == '__main__':
    adicionar()