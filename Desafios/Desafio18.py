import random

alunos = []

for cont in range(4):
   alunos.append(input('Digite o nome do aluno: '))

r = random.shuffle(alunos)

print('Os Alunos sorteada na ordem é:', alunos)