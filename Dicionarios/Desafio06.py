diciGeral = {}
jogador = []
gols = []

continuar = 'S'

while continuar == 'S' or continuar == 's':

    entradaNome = input('Digite o nome do Jogador: ').capitalize()
    entradaPartidas = int(input('Digite a quantidade de partidas que fez o jogador: '))
    for cont in range(entradaPartidas):
        entradaGols = int(input(f'Quantidade de gols na partida {cont+1}: '))
        gols.append(entradaGols)

    jogador.append([entradaNome, gols[-entradaPartidas:], sum(gols[-entradaPartidas:])])


    resumir = input('Deseja visualizar algum jogador específico ? (S/N): ')
    if resumir == 's' or resumir == 'S':
        pesquisaJogador = int(input('Digite a ordem de cadastro do jogador desejado: '))
        print(jogador[pesquisaJogador-1])

    continuar = input('Deseja continuar ? (S/N): ')

    diciGeral = jogador

    print(diciGeral)
