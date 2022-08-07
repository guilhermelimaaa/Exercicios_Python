velocidade = float(input('Digite a velocidade do carro (em km/h): '))

if velocidade > 80.0:
    multa = (velocidade - 80.0) * 7
    print('Sua velocidade', velocidade,'km/h, ultrapassou o limite de 80km/h; e por isso você foi multado em', 'R$', multa)
else:
    print('Muito bem, você está no limite de velocidade permitido =)')