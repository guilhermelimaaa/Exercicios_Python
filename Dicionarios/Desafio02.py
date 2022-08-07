import random

tabela = {}

for cont in range(4):
    tabela ['Jogador '+ str(cont+1)] = random.randint(1,6)

ordenado = sorted(tabela.items(), key= lambda item : item[1], reverse=True)
print(ordenado)