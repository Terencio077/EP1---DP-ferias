from funcoes import *
import random

cores = {
    0: "\033[31m",
    1: "\033[32m",
    2: "\033[33m",
    3: "\033[34m",
    4: "\033[35m",
    5: "\033[36m",
    6: "\033[30m",
}
reset = "\033[0m"

print("Jogo de dominó bem maneiro")

entrada = input("quantos jogadores? (2-4)")
while not entrada.isdigit() or int(entrada) < 2 or int(entrada) > 4:
    print("Entrada inválida. Digite um número entre 2 e 4.")
    entrada = input("quantos jogadores? (2-4)")
n = int(entrada)

jogar_novamente = True
while jogar_novamente:
    pecas = cria_pecas()
    jogo = inicia_jogo(n, pecas)

    turno = random.randint(0, n - 1)
    passes_consecutivos = 0
    terminou = False

   
    if turno == 0:
        print("Você começa!")
    else:
        print(f"Jogador {turno} começa!")

    while not terminou:
        jogador_atual = turno % n

        if jogo["mesa"]:
            linha = ""
            for p in jogo["mesa"]:
                linha = (
                    linha
                    + "["
                    + cores[p[0]] + str(p[0]) + reset
                    + "|"
                    + cores[p[1]] + str(p[1]) + reset
                    + "]"
                )
            print("MESA: " + linha)
        else:
            print("MESA: (vazia)")

        mesa_count = len(jogo["mesa"]) if jogo["mesa"] else 0
        jogadores_counts = []
        for j in jogo["jogadores"]:
            jogadores_counts.append((j, len(jogo["jogadores"][j])))
        counts_str = []
        for j, cnt in jogadores_counts:
            if j == 0:
                counts_str.append("Você: " + str(cnt))
            else:
                counts_str.append("Jogador " + str(j) + ": " + str(cnt))
        print("Peças na mesa: " + str(mesa_count) + " | " + " | ".join(counts_str))

        if jogador_atual == 0:
            mao = jogo["jogadores"][0]
            jogou = False
            jogada_encerrada = False

            while (not jogou) and (not jogada_encerrada):
                linha_mao = ""
                linha_indices = ""
                for i, p in enumerate(mao):
                    linha_mao = (
                    linha_mao +
                    "[" +
                    cores[p[0]] + str(p[0]) + reset +
                    "|" +
                    cores[p[1]] + str(p[1]) + reset +
                    "] "
                    )
                    linha_indices += str(i + 1).center(6)
                print("Sua mão:")
                print(linha_mao)
                print(linha_indices)
              

                pos = posicoes_possiveis(jogo["mesa"], mao)
                if not pos:
                  
                    while (not pos) and jogo["monte"]:
                        compra = jogo["monte"][0]
                        del jogo["monte"][0]
                        jogo["jogadores"][0].append(compra)
                        print("como não há jogadas, você comprou uma peça " + "[" + str(compra[0]) + "|" + str(compra[1]) + "]")
                        pos = posicoes_possiveis(jogo["mesa"], mao)

                    if not pos:
                       
                        print("Sem jogadas e monte vazio — você passou.")
                        jogada_encerrada = True
                        passes_consecutivos = passes_consecutivos + 1
                else:
                    escolha_ok = False
                    primeiro_aviso = True
                    while not escolha_ok:
                        escolha_str = input("Escolha sua peça: ")
                        if not escolha_str.isdigit():
                            print("Entrada inválida — digite o número da peça.")
                            if primeiro_aviso:
                                opcoes = []
                                for i in pos:
                                    opcoes.append(i + 1)
                                print("peças jogáveis: " + str(opcoes))
                                primeiro_aviso = False
                            else:
                                opcoes = []
                                for i in pos:
                                    opcoes.append(i + 1)
                                print("peças jogáveis: " + str(opcoes))
                        else:
                            escolha_num = int(escolha_str)
                            indice = escolha_num - 1
                            valido = False
                            for x in pos:
                                if x == indice:
                                    valido = True
                            if not valido:
                                print("Peça não jogável. Escolha uma peça válida.")
                                if primeiro_aviso:
                                    opcoes = []
                                    for i in pos:
                                        opcoes.append(i + 1)
                                    print("peças jogáveis: " + str(opcoes))
                                    primeiro_aviso = False
                            else:
                                escolha_ok = True

                    peca = mao[indice]
                    del mao[indice]
                    jogo["mesa"] = adiciona_na_mesa(peca, jogo["mesa"])
                    print("Você colocou: " + "[" + str(peca[0]) + "|" + str(peca[1]) + "]")
                    jogou = True
                    passes_consecutivos = 0

            ganhador = verifica_ganhador(jogo["jogadores"])
            if ganhador != -1:
                if ganhador == 0:
                    print("Você venceu")
                else:
                    print("Jogador " + str(ganhador) + " venceu")
                print_classificacao(jogo)
                terminou = True

        else:
            mao_cpu = jogo["jogadores"][jogador_atual]
            pos_cpu = posicoes_possiveis(jogo["mesa"], mao_cpu)
            if pos_cpu:
                indice_jogavel = pos_cpu[0]
                peca = mao_cpu[indice_jogavel]
                del mao_cpu[indice_jogavel]
                jogo["mesa"] = adiciona_na_mesa(peca, jogo["mesa"])
                print("jogador automatico " + str(jogador_atual) + " colocou " + "[" + str(peca[0]) + "|" + str(peca[1]) + "]")
                passes_consecutivos = 0
            else:
                
                while (not pos_cpu) and jogo["monte"]:
                    compra = jogo["monte"][0]
                    del jogo["monte"][0]
                    jogo["jogadores"][jogador_atual].append(compra)
                    print("jogador automatico " + str(jogador_atual) + " comprou " + "[" + str(compra[0]) + "|" + str(compra[1]) + "]")
                    pos_cpu = posicoes_possiveis(jogo["mesa"], mao_cpu)

                if pos_cpu:
                    indice_jogavel = pos_cpu[0]
                    peca = mao_cpu[indice_jogavel]
                    del mao_cpu[indice_jogavel]
                    jogo["mesa"] = adiciona_na_mesa(peca, jogo["mesa"])
                    print("jogador automatico " + str(jogador_atual) + " colocou " + "[" + str(peca[0]) + "|" + str(peca[1]) + "]")
                    passes_consecutivos = 0
                else:
                    print(str(jogador_atual) + " passou a jogada")
                    passes_consecutivos = passes_consecutivos + 1

            ganhador = verifica_ganhador(jogo["jogadores"])
            if ganhador == jogador_atual:
                if jogador_atual == 0:
                    print("parabéns, você venceu")
                else:
                    print("você conseguiu perder pro jogador " + str(jogador_atual))
                print_classificacao(jogo)
                terminou = True

        if (passes_consecutivos >= n) and (not jogo["monte"]):
            print("\nJogo bloqueado! Ninguém conseguiu jogar e monte está vazio.")
            pontos = {}
            for j in jogo["jogadores"]:
                soma = conta_pontos(jogo["jogadores"][j])
                pontos[j] = soma

          
            menor = min(pontos.values())
            vencedores = [j for j, pts in pontos.items() if pts == menor]

            print("Pontos por jogador (soma das peças nas mãos):")
            for j in pontos:
                print("  Jogador " + str(j) + ": " + str(pontos[j]) + " pontos")

            print_classificacao(jogo)

            if len(vencedores) > 1:
                nomes_vencedores = []
                for v in vencedores:
                    if v == 0:
                        nomes_vencedores.append("Você")
                    else:
                        nomes_vencedores.append("Jogador " + str(v))
                print("Jogo empatado entre: " + ", ".join(nomes_vencedores))
            else:
                vencedor = vencedores[0]
                if vencedor == 0:
                    print("você ganhou por ter menos pontos")
                else:
                    print("o jogador " + str(vencedor) + " ganhou por ter menos pontos")

            terminou = True

        turno = turno + 1

    print("\nEstado final da mesa:")
    if jogo["mesa"]:
        linha_f = ""
        for p in jogo["mesa"]:
            linha_f = (
                linha_f +
                "[" +
                cores[p[0]] + str(p[0]) + reset +
                "|" +
                cores[p[1]] + str(p[1]) + reset +
                "] "
            )
        print(linha_f)
    else:
        print("(vazia)")

    print("Fim do jogo.")
    
    resposta_valida = False
    while not resposta_valida:
        resposta = input("\nQuer jogar de novo? (sim/não): ")
        if resposta == "sim" or resposta == "s":
            resposta_valida = True
            jogar_novamente = True
        elif resposta == "não" or resposta == "nao" or resposta == "n":
            resposta_valida = True
            jogar_novamente = False
        else:
            print("Resposta inválida. Digite 'sim' ou 'não'.")
