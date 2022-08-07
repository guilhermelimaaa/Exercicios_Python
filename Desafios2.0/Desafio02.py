import random
vitorias = 0
derrota = 0
while derrota < 1:
    decisao = input('Você escolhe Par ou Ímpar (P/I)?: ').upper()
    numJogador = int(input('Digite o numero que deseja jogar: '))
    numMaquina = random.randint(0,10)
    print('Numero da máquina:', numMaquina)
    jogo = numJogador + numMaquina
    print('A Soma dos números foi:', jogo)
    print('Você tem', vitorias, 'vitória(s)')

    if decisao == 'P' and jogo % 2 == 0:
        print('Você venceu =)')
        vitorias+=1

    elif decisao == 'I' and jogo % 2 != 0:
        print('Você venceu =)')
        vitorias+=1

    else:
        print('Voce perdeu =(')
        print('Você teve', vitorias, 'vitória(s)')
        derrota+=1