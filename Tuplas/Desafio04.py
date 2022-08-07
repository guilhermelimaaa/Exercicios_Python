tuplaMain = []
listaPares = []

for cont in range(6):
    tuplaMain.append(int(input('Digite um número: ')))

tuple = tuplaMainConvert = tuplaMain
print(tuplaMainConvert)

for cont in range(len(tuple)):
    if tuplaMainConvert[cont] % 2 == 0:
        listaPares.append(tuplaMainConvert[cont])

print('O Valor 9, aparece',tuplaMainConvert.count(9),'vezes')
print('O Primeiro valor 3 aparece na posição', tuplaMainConvert.index(3))
print('Os valores pares digitados são:', listaPares)