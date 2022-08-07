nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite outra nota: '))

media = (nota1 + nota2) / 2

if media < 3:
    print(f'\033[0;31mMédia:', media, 'Reprovado')
elif media < 5:
    print(f'\033[0;33mMédia:' , media, 'Recuperação')
elif media < 8:
    print(f'\033[0;34mMédia:', media, 'Normal')
elif media <= 10:
    print(f'\033[0;32mMédia:', media, 'Aprovado')