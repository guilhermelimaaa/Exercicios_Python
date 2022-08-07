reta1 = float(input('Digite a medida da primeira reta: '))
reta2 = float(input('Digite a medida da segunda reta: '))
reta3 = float(input('Digite a medida da terceira reta: '))

if (reta2 - reta3) < reta1 < reta2 + reta3 and (reta1 - reta3) < reta2 < reta1 + reta3 and (reta2 - reta1) < reta3 < reta2 + reta1:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')