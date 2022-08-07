alunos = {}


alunos ['Nome'] = entradaNome = input('Digite o nome do(a) aluno(a): ')
alunos ['Nota'] = entradaNota = float(input('Digite a nota do(a) aluno(a)'))
if(entradaNota <= 3.9 and entradaNota >= 0):
    alunos ['Situacao'] = 'Reprovado(a)'
elif(entradaNota >= 4.0 and entradaNota <= 6.9):
    alunos ['Situacao'] = 'Recuperação'
elif(entradaNota <= 10 and entradaNota >= 7.0):
    alunos ['Situacao'] = 'Aprovado(a)'

print(alunos)