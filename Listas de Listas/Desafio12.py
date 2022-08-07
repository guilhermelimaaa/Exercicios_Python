listaGeral = []
boletins = []

resposta = 'S'

while resposta == 's' or resposta == 'S':

    nome = input('Digite o nome do(a) aluno(a): ').capitalize()
    nota1 = float(input(f'Digite a primeira nota de {nome}: '))
    nota2 = float(input(f'Digite a segunda nota de {nome}: '))
    media = (nota1 + nota2) / 2

    boletins.append([nome,[nota1,nota2],media])
    listaGeral.append([nome,media])

    print(listaGeral)


    respostaMostrarAluno = input('Deseja ver as notas de um aluno específico ? (S/N): ')
    if respostaMostrarAluno == 's' or respostaMostrarAluno == 'S':
        mostrarAluno = int(input('Digite o numero do aluno que deseja ver as notas: '))
        print(boletins[mostrarAluno-1])
    resposta = input('Deseja continuar ? (S/N): ')


