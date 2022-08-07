somaPares = 0
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]


for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor na linha {linha} e coluna {coluna}: '))

print(matriz[0])
print(matriz[1])
print(matriz[2])

for linha in range(3):
    for coluna in range(3):
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]

somaTerceiraColuna = matriz[0][2] + matriz[1][2] + matriz[2][2]

print('A Soma dos valores pares é:', somaPares)
print('A Soma dos valores da terceira coluna é de:', somaTerceiraColuna)
matriz[1].sort(reverse=True)
print('O Maior valor da segunda linha é:', matriz[1][0])