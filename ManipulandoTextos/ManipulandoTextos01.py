nome = input('Digite seu nome completo: ')
maiusculo = nome.upper()
minusculo = nome.lower()
sepPrimNome = nome.find(' ')
letrasPrimNome = sepPrimNome
juntar = nome.strip()
qtdLetras = len(juntar)

print(maiusculo)
print(minusculo)
print(qtdLetras)
print(letrasPrimNome)