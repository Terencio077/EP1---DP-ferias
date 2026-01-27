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

def posicoes_possiveis(mesa,pecas):
    posicoes = []
    if mesa == []:
        for i in range(len(pecas)):
            posicoes.append(i)

    else:
        inicio = mesa[0][0]
        fim = mesa[len(mesa)-1][1]
        i = 0

        while i<len(pecas):
            numero1 = pecas[i][0]
            numero2 = pecas[i][1]
            if numero1 == inicio or numero2 == inicio or numero1 == fim or numero2 == fim:
                posicoes.append(i)
            i+=1

    return posicoes
def adiciona_na_mesa(peca_add,mesa):
    mesa_final = []
    if mesa == []:
        mesa_final.append(peca_add)
    else:
        inicio = mesa[0][0]
        fim = mesa[len(mesa)-1][1]

       
        if peca_add[0] == inicio:
            peca = [peca_add[1],peca_add[0]]
            mesa_final.append(peca)
            for coisa in mesa:
                mesa_final.append(coisa)

        elif peca_add[1] == inicio:
                    mesa_final.append(peca_add)
                    for peca in mesa:
                        mesa_final.append(peca)
        elif peca_add[0] == fim:
            mesa.append(peca_add)
            mesa_final = mesa

        elif peca_add[1] == fim:
            peca = [peca_add[1],peca_add[0]]
            mesa.append(peca)
            mesa_final = mesa 

    return mesa_final





        
        
        