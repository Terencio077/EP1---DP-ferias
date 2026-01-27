from random import *
def cria_pecas ():
    pecas = []
    peca = []
    
    for i in range(7):
        for j in range(i,7):
            peca = []
            peca.append(i)
            peca.append(j)
            pecas.append(peca)
           
    shuffle(pecas)
    return pecas
total = cria_pecas()

def inicia_jogo(n,total):
    dicio = {}
    dicio2 = {}
    indice = 0
    for jogador in range(n):
        dicio2[jogador] = total[indice:indice+7]
        indice +=7
    dicio["jogadores"] = dicio2
    dicio["monte"] = total[indice:]
    dicio["mesa"] = []
    return dicio

def verifica_ganhador(dicionario):
    for jogador,pecas in dicionario.items():
        if len(pecas) == 0:
            return jogador
    return -1
        
def conta_pontos(lista):
    if lista == []:
        return 0
    soma = 0
    for sub_lista in lista:
        for numero in sub_lista:
            soma+=numero
    return soma

conta_pontos([[1,0],[2,3],[6,6]])



        
        
        