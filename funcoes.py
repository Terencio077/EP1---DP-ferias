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
