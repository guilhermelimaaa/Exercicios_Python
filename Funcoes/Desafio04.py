def maior():

    maiorNum = -999999999999999999999999999999999999999999999999999999999999999999

    qtdNum = int(input('Deseja analizar quantos números ?: '))
    for cont in range(qtdNum):
        numDigitado = int(input('Digite um número: '))
        if numDigitado > maiorNum:
            maiorNum = numDigitado

    print('O Maior numero digitado é:', maiorNum)

if __name__ == '__main__':
    maior()