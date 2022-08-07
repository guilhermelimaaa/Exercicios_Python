def contador(inicio,fim,passo):

    for cont1 in range(1,10,1):
        print(cont1)

    print('Fim da contagem 1 =) \n')

    for cont2 in range(10,0,-2):
        print(cont2)

    print('Fim da contagem 2 =) \n')

    for contPers in range(inicio,fim,passo):
        print(contPers)

    print('Fim da contagem personalizada =)')

inputInicio = int(input('Digite o numero de início da contagem: '))
inputFim = int(input('Digite o numero final da contagem: '))
inputPasso = int(input('Digite a razão da contagem: '))

if __name__ == '__main__':
    print(contador(inputInicio,inputFim,inputPasso))