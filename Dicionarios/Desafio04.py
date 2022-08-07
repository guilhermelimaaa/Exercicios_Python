jogador = {}
gols = []

jogador ['Nome'] = entradaNome = input('Digite o nome do Jogador: ').capitalize()
jogador ['Partidas'] = entradaPartidas = int(input('Digite a quantidade de partidas que fez o jogador: '))
for cont in range(entradaPartidas):
    entradaGols = int(input(f'Quantidade de gols na partida {cont+1}: '))
    gols.append(entradaGols)

somaGols = sum(gols)

jogador['Gols'] = gols
jogador['Total de gols'] = somaGols

print(jogador)
