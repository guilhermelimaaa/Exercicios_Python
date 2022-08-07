opcao = 'S'
somaPreco = 0
produtosMil = 0
maisBarato = 9999999999999999999999999999999999999999999999
nomeBarato = ''

while opcao == 'S':
    nomeProduto = input('Digite o nome do produto: ')
    precoProduto = float(input('Digite o preço do produto: '))

    somaPreco+= precoProduto

    if precoProduto > 1000.0:
        produtosMil+=1

    if precoProduto < maisBarato:
        maisBarato = precoProduto
        nomeBarato = nomeProduto

    if maisBarato < precoProduto:
        maisBarato = precoProduto
        nomeBarato = nomeProduto

    opcao = input('Deseja continuar ? (S/N): ').upper()
    while opcao != 'S' and opcao != 'N':
        opcao = input('Deseja continuar ? (S/N): ').upper()


print('O Total gasto foi de R$', somaPreco)
print('O Total de produtos que custam mais de R$ 1000:', produtosMil)
print('O Produto mais barato é o(a):', nomeBarato.capitalize())

