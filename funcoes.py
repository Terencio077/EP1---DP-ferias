from random import *
def cria_pecas ():
    pecas = []
    peca = []
    
    for i in range(7):
        for j in range(i+1):
            peca = []
            peca.append(j)
            peca.append(i)
            pecas.append(peca)
           
    shuffle(pecas)
    return pecas
