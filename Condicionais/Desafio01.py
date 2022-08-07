import random

numRandom = int(random.uniform(0,5))
numero = int(input('Digite o número em que o computador pensou (de 0 a 5): '))

if numRandom == numero:
    print('Você acertou =D, realmente pensei em', numRandom)
else:
    print('Voce errou =(, pensei no número', numRandom)