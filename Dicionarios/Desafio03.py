pessoa = {}

pessoa ['Nome']= entradaNome = input('Digite o nome da pessoa: ')
pessoa ['Ano de nascimento']= entradaAnoNasc = int(input('Digite o ano de nascimento: '))
pessoa ['CTPS'] = entradaCtps = int(input('Digite o numero da carteira de trabalho (caso não tenha digite 0): '))
if entradaCtps != 0:
    pessoa ['Ano de contratacao'] = entradaAnoContr = int(input('Digite o ano de contratação: '))
    pessoa ['Salário'] = entradaSalario = float(input('Digite o salário recebido: '))
    pessoa ['Aposentadoria'] = (entradaAnoContr + 35) - entradaAnoNasc

print(pessoa)