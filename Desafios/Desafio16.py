import random

alunos = []

for cont in range(4):
   alunos.append(input('Digite o nome do aluno: '))

r = random.choice(alunos)

print('O Aluno(a) sorteada é:', r)