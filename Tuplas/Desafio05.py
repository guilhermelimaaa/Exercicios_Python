papelaria = ('1 Lápis', 'R$ 1.75', '2 Borracha', 'R$ 2.00', '3 Caderno', 'R$ 15.90', '4 Estojo', 'R$ 25.00', '5 Transferidor', 'R$ 4.20', '6 Compasso', 'R$ 9.99', '7 Mochila', 'R$ 120.50','8 Canetas', 'R$ 22.30', '9 Livro', 'R$ 50.30')

for cont in range(0,len(papelaria),2):
    print(papelaria[cont] + '.'*30 + papelaria[cont+1])