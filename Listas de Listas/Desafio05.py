numeros = []
pares = []
impares = []
escolha = 'S'
cont = 0

while escolha == 's' or escolha == 'S':
    numeros.insert(cont, int(input('Digite um número: ')))
    if numeros[cont] % 2 == 0:
        pares.append( numeros[cont])
    elif numeros[cont] % 2 != 0:
        impares.append(numeros[cont])
    cont+=1

    escolha = input('Deseja continuar ? (S/N): ')

print('Lista geral:', numeros)
print('Lista de pares:', pares)
print('Lista de ímpares:', impares)
