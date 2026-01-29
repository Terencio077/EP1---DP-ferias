from funcoes import conta_pontos

# Simula estado de jogo bloqueado com empate entre jogadores 1 e 2
jogo = {
    "jogadores": {
        0: [[6,6]],            # 12 pontos
        1: [[3,3],[0,0]],     # 6 points
        2: [[2,2],[1,1],[0,0]],# 6 points -> tie with player 1
    },
    "monte": [],
    "mesa": []
}

pontos = {}
for j in jogo["jogadores"]:
    pontos[j] = conta_pontos(jogo["jogadores"][j])

menor = min(pontos.values())
vencedores = [j for j, pts in pontos.items() if pts == menor]

print("Pontos por jogador:")
for j in sorted(pontos.keys()):
    print(f"  Jogador {j}: {pontos[j]} pontos")

if len(vencedores) > 1:
    print("Resultado do teste: empate entre ->", vencedores)
else:
    print("Resultado do teste: vencedor ->", vencedores[0])
