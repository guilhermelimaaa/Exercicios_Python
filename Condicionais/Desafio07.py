salario = float(input('Digite seu salário: '))

if salario > 1250.0:
    reajusteMaior = (salario*10)/100
    print('Seu novo salário será de R$', salario + reajusteMaior)
else:
    reajusteMenor = (salario * 15) / 100
    print('Seu novo salário será de R$', salario + reajusteMenor)