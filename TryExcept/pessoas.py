def menu():
    opcao = 3

    while opcao != '0':
        print('\n======== Sistema de cadastro de pessoas =======')
        print('[1] - Novo cadastro')
        print('[2] - Pessoas cadastradas')
        print('[0] - Sair\n')
        opcao = input('\nDigite uma das opções acima: ')
        if opcao == '1':
            novoCadastro()
        if opcao == '2':
            pessoasCadastradas()
        if opcao == '0':
            break
        if opcao != '1' and opcao != '2':
            print('Opção inválida =(')



def novoCadastro():
    try:
        nome = input('Informe o nome: ').capitalize()
        idade = (input('Informe a idade: '))

        with open('cadastro.txt','a') as arquivoTxt:
            arquivoTxt.write('\n'+nome + ' '*40 + str(idade))
    except:
        print('Arquivo inexistente ou removido =(')


def pessoasCadastradas():
    try:
        with open('cadastro.txt', 'r') as arquivoTxt:
            lerArquivo = arquivoTxt.read()

        print('\n' + lerArquivo)
    except:
        print('Arquivo inexistente ou removido =(')



