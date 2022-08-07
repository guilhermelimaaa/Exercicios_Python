def aumentar(valor, taxa, uniMonetaria):
    aumento = (valor * taxa) / 100
    aumento = valor + aumento
    return uniMonetaria + str(aumento)

def diminuir(valor, taxa, uniMonetaria):
    diminuicao = (valor * taxa) / 100
    diminuicao = valor - diminuicao
    return uniMonetaria + str(diminuicao)

def dobro(valor, uniMonetaria):
    dobrado = valor * 2
    return uniMonetaria + str(dobrado)

def metade(valor, uniMonetaria):
    dividido = valor / 2
    return uniMonetaria + str(dividido)

def moeda(uniMonetaria):
    return uniMonetaria

def resumo(valor, taxaAumento, taxaReducao, uniMonetaria):
    print('\nValor principal:', uniMonetaria + str(valor))
    dobroValor = valor * 2
    print('Dobro:', uniMonetaria + str(dobroValor))
    metadeValor = valor / 2
    print('Metade:', uniMonetaria + str(metadeValor))
    aumentoValor = valor + ((valor * taxaAumento)/100)
    print('Aumento:', uniMonetaria + str(aumentoValor))
    reduzirValor = valor - ((valor * taxaReducao)/100)
    print('Diminuição:', uniMonetaria + str(reduzirValor))
