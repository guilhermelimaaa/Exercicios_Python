def escreva(texto):
    return texto

inputTexto = input('Digite um texto qualquer: ')

if __name__ == '__main__':
    espaco = escreva(inputTexto.index(' '))
    print(escreva(inputTexto[0:espaco]))
    espaco2 = escreva(inputTexto.index(' ',espaco+1,len(inputTexto)))
    print(escreva(inputTexto[0:espaco2]))
    print(escreva(inputTexto))


