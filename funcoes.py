from random import *
def cria_pecas ():
    pecas = []
    peca = []
    
    for i in range(7):
        for j in range(7):
            peca = []
            peca.append(i)
            peca.append(j)
            if peca not in pecas:
                pecas.append(peca)
           
    shuffle(pecas)
    return pecas
print(cria_pecas())