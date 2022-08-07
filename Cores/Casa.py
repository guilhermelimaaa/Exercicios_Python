valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
qtdAnos = int(input('Digite a quantidade de anos em que a casa será paga: '))

valorParcela = valorCasa / (qtdAnos * 12)
porcSalario = (salario * 30) / 100

if porcSalario >= valorParcela:
    print(f'\033[0;32mCompra do imóvel aprovada =)')
else:
    print(f'\033[0;31mCompra do imóvel negada =(')