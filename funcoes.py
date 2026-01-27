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
        


        
        
        