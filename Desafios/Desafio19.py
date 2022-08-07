catetoOp = float(input('Digite a medida do cateto oposto do triângulo: '))
catetoAdj = float(input('Digite a medida do cateto adjacente do triângulo: '))
hipotenusa = (catetoOp**2 + catetoAdj**2) ** 0.5

print('O Sen α é', catetoOp / hipotenusa)
print('O Cos α é', catetoAdj / hipotenusa)
print('A Tg α é', catetoOp / catetoAdj)

