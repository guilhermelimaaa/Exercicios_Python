numero = (input('Digite um numero de 0 a 9999: '))

print('Unidade:', numero[3:])
print('Dezena:', numero[2::3])
print('Centena:', numero[1::3])
print('Milhar:', numero[0::4])

