palavra = input('Digite algo: ')

print('o tipo primitivo é', type(palavra))
print('Só tem espacos', (palavra.isspace()))
print('é um número ?', (palavra.isnumeric()))
print('é um alfabético ?', (palavra.isalpha()))
print('é um alfanumérico ?', (palavra.isalnum()))
print('Está em maiúsculas ?', (palavra.isupper()))
print('Está em minúsculas ?', (palavra.islower()))
print('Está capitalizada ?', (palavra.isprintable()))