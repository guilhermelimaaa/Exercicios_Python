def area():
    inputLarg = float(input('Digite a largura do retângulo: '))
    inputComp = float(input('Digite o comprimento do retângulo: '))
    return 'A Area é de: ' + str(inputLarg * inputComp) + ' m²'

if __name__ == '__main__':
    print(area())