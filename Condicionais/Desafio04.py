viagem = float(input('Digite a distância da viagem (em km): '))

if viagem > 200.0:
    print('O Custo da viagem será de R$', viagem * 0.45)
else:
    print('O Custo da viagem será de R$', viagem * 0.50)