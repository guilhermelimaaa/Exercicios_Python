import random

numeros = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))

print(numeros)

organizar = sorted(numeros)

print('O Menor valor é:', organizar[0])
print('O Maior valor é:', organizar[4])
