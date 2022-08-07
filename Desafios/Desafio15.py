km = float(input('Digite a quantidade de kms rodados: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))

precoDias = 60.0 * dias
precoKm = 0.15 * km

print('O Preço a ser pago pelo aluguel é de R$', precoDias + precoKm)