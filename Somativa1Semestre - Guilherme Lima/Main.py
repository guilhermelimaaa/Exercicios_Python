import pandas
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

login = uic.loadUi('login.ui')
menu = uic.loadUi('menu.ui')
adicionar = uic.loadUi('create.ui')
ler = uic.loadUi('read.ui')
atualizar = uic.loadUi('update.ui')
excluir = uic.loadUi('delete.ui')


def logar():
    if login.txtLogin.text() == 'senai' and login.txtSenhaLogin.text() == '123456':
        menu.show()
        login.close()
    else:
        login.lblInfoLogin.setText('Acesso negado! =(')


def adicionarPlanilha():
    planilhaAdd = pandas.read_excel('professores.xlsx')
    linhas = len(planilhaAdd)

    planilhaAdd.loc[linhas + 1, 'id'] = adicionar.txtIdAdicionar.text()
    planilhaAdd.loc[linhas + 1, 'nome'] = adicionar.txtNomeAdicionar.text()
    planilhaAdd.loc[linhas + 1, 'formacao'] = adicionar.txtFormacaoAdicionar.text()
    planilhaAdd.loc[linhas + 1, 'categoria'] = adicionar.txtCategoriaAdicionar.text()
    planilhaAdd.loc[linhas + 1, 'cargo'] = adicionar.txtCargoAdicionar.text()
    planilhaAdd.loc[linhas + 1, 'situacao_servidor'] = adicionar.txtSitServidorAdicionar.text()
    planilhaAdd.loc[linhas + 1, 'classe_funcional'] = adicionar.txtClasseFuncionalAdicionar.text()
    planilhaAdd.loc[linhas + 1, 'idade'] = adicionar.txtIdadeAdicionar.text()

    planilhaAdd.to_excel('professores.xlsx', index=False)


def lerPlanilha():
    planilhaLer = pandas.read_excel('professores.xlsx')

    ler.lblExibirConteudo.setText(planilhaLer.to_string())


def atualizarPlanilha():
    planilhaAtualizar = pandas.read_excel('professores.xlsx')

    qtdLinhas = len(planilhaAtualizar)
    idAtualizar = atualizar.txtIdAtualizar.text()

    try:
        for cont in range(qtdLinhas):
            if str(idAtualizar) == str(planilhaAtualizar['id'][cont]):
                planilhaAtualizar.loc[cont, 'id'] = atualizar.txtIdNovoAtualizar.text()
                planilhaAtualizar.loc[cont, 'nome'] = atualizar.txtNomeAtualizar.text()
                planilhaAtualizar.loc[cont, 'formacao'] = atualizar.txtFormacaoAtualizar.text()
                planilhaAtualizar.loc[cont, 'categoria'] = atualizar.txtCategoriaAtualizar.text()
                planilhaAtualizar.loc[cont, 'cargo'] = atualizar.txtCargoAtualizar.text()
                planilhaAtualizar.loc[cont, 'situacao_servidor'] = atualizar.txtSitServidorAtualizar.text()
                planilhaAtualizar.loc[cont, 'classe_funcional'] = atualizar.txtClasseFuncionalAtualizar.text()
                planilhaAtualizar.loc[cont, 'idade'] = atualizar.txtIdadeAtualizar.text()

                planilhaAtualizar.to_excel('professores.xlsx', index=False)

                break
    except:
        print('Id não encontrado =(')


def excluirPlanilha():
    planilhaExcluir = pandas.read_excel('professores.xlsx')

    qtdLinhas = len(planilhaExcluir)
    idExclusao = excluir.txtIdExcluir.text()

    for cont in range(qtdLinhas):
        if str(idExclusao) == str(planilhaExcluir['id'][cont]):
            planilhaExcluir = planilhaExcluir.drop(cont)
            planilhaExcluir.to_excel('professores.xlsx', index=False)
            break

def exibirCreate():
    adicionar.show()
    adicionar.btnCadastrarAdicionar.clicked.connect(adicionarPlanilha)

def exibirRead():
    ler.show()
    lerPlanilha()

def exibirUpdate():
    atualizar.show()
    atualizar.btnAtualizar.clicked.connect(atualizarPlanilha)

def exibirDelete():
    excluir.show()
    excluir.btnEntrarExcluir.clicked.connect(excluirPlanilha)

def sairPrograma():
    menu.close()
    login.show()
    login.txtLogin.clear()
    login.txtSenhaLogin.clear()



login.show()
login.btnEntrarLogin.clicked.connect(logar)


menu.btnCreate.clicked.connect(exibirCreate)
menu.btnRead.clicked.connect(exibirRead)
menu.btnUpdate.clicked.connect(exibirUpdate)
menu.btnDelete.clicked.connect(exibirDelete)
menu.btnExit.clicked.connect(sairPrograma)


app.exec_()