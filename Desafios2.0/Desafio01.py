num = 0
while num >= 0:
    num = int(input('Digite um numero para calcular a tabuada: '))
    for cont in range (10):
        print(num, 'X', cont, '=', num * cont)