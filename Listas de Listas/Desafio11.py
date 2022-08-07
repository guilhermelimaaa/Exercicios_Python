import random

listaJogo = []
listaTemporaria = []

qtdJogos = int(input('Quantos jogos deseja sortear ?: '))

for cont in range(qtdJogos):
    listaTemporaria.append('Jogo ' + str(cont+1) + ':')
    listaJogo = listaTemporaria
    for cont2 in range(6):
        numSorteado = random.randint(1,60)
        while numSorteado in listaTemporaria:
            numSorteado = random.randint(1,60)
        listaTemporaria.append(numSorteado)

print(listaJogo)