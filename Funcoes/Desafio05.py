import time
import random

numeros = []
pares = []

def sorteia():
    for cont in range(5):
        time.sleep(0.5)
        numSorteado = random.randint(0,100)
        numeros.append(numSorteado)
    print('Os numeros sorteados foram:', numeros)


def somaPar():
    for cont in range(5):
        if numeros[cont] % 2 == 0:
            pares.append(numeros[cont])

    somaPares = sum(pares)
    print('Os numeros pares somados são:', somaPares)

if __name__ == '__main__':
    sorteia()
    somaPar()