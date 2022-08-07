from datetime import date

anoNasc = int(input('Digite o ano de nascimento: '))

atual = date.today().year

if (atual - anoNasc) == 18:
    print('Ano de Nascimento:', anoNasc)
    print('Idade:', atual - anoNasc, 'anos')
    print('Hora de se alistar')

elif (atual - anoNasc) < 18:
    print('Ano de Nascimento:', anoNasc)
    print('Idade:', atual - anoNasc, 'anos')
    print('Faltam', 18 - (atual - anoNasc), 'ano(s) para se alistar')

elif (atual - anoNasc) > 18:
    print('Ano de Nascimento:', anoNasc)
    print('Idade:', atual - anoNasc, 'anos')
    print('Passaram', (atual - anoNasc) - 18, 'ano(s) desde o alistamento')
