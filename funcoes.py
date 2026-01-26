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
    indice = 0
    for jogador in range(n):
        dicio[jogador] = total[indice:indice+7]
        indice +=7
    dicio["monte"] = total[indice:]
    dicio["mesa"] = []

    return dicio



        
        
        