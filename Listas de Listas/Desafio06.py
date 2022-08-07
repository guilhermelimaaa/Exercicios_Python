expressao = input('Digite uma expressão numérica: ')
abreParenteses = expressao.count('(')
fechaPareneses = expressao.count(')')

if abreParenteses == fechaPareneses:
    print('Expressão válida =)')
else:
    print('Expressão inválida =(')