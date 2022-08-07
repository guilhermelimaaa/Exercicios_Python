nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media <= 3.0:
    print('Reprovado(a)')
elif media <= 4.9:
    print('Recuperação')
elif media <= 6.9:
    print('Regular')
elif media <= 10.0:
    print('Aprovado(a)')