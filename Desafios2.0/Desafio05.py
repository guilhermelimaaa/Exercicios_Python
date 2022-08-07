valorSaque = int(input('Digite o valor que deseja sacar: '))


cedulasCinquenta = valorSaque / 50
round(cedulasCinquenta - 0.5)

valorSaque = valorSaque - (cedulasCinquenta * 50)


cedulasVinte = valorSaque / 20
round(cedulasVinte-0.5)

valorSaque = valorSaque - (cedulasVinte * 20)


cedulasDez = valorSaque / 10
round(cedulasDez-0.5)

valorSaque = valorSaque - (cedulasDez * 10)


cedulasUm = valorSaque / 1
round(cedulasUm-0.5)

valorSaque = valorSaque - (cedulasUm * 1)


print('Total de cédulas de 50:', cedulasCinquenta)
print('Total de cédulas de 20:', cedulasVinte)
print('Total de cédulas de 10:', cedulasDez)
print('Total de cédulas de 1:', cedulasUm)





