numeros = []
escolha = 'S'
cont = 0

while escolha == 's' or escolha == 'S':
    numeros.insert(cont, int(input('Digite um número: ')))
    cont+=1
    escolha = input('Deseja continuar ? (S/N): ')

print('\nA Quantidade de números é:', len(numeros))
numeros.sort(reverse=True)
print('Os numeros em ordem decrescente são:', numeros)
print('O Valor 5 está presente ?', numeros.__contains__(5))


