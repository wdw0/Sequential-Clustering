from distancia import distancia_euclidiana
from collections import defaultdict

def formar_ligacoes(pontos):
    n = len(pontos)
    visitados = [False] * n
    ligacoes = []
    atual = 0
    visitados[atual] = True

    for _ in range(n - 1):
        menor = None
        menor_dist = float('inf')
        for i, ponto in enumerate(pontos):
            if not visitados[i]:
                dist = distancia_euclidiana(pontos[atual], ponto)
                if(dist < menor_dist) or (dist == menor_dist and i < menor):
                    menor = i
                    menor_dist = dist
        ligacoes.append((atual + 1, menor + 1, menor_dist))
        visitados[menor] = True
        atual = menor
    return ligacoes

def formar_grupos(ligacoes, num_pontos, aux):
    ligacoes.sort(key=lambda x: x[2], reverse = True)
    ligacoes_separadas = ligacoes[k - 1:] #removendo as K-1 maiores ligacoes
    pais = {i: i for i in range(1, num_pontos + 1)}

    def encontrar(u):
        while pais[u] != u:
            pais[u] = pais[pais[u]]
            u = pais[u]
        return u

    def unir(u,v):
        ponto_u = encontrar(u)
        ponto_v = encontrar(v)
        if ponto_u != ponto_v:
            pais[ponto_u] = ponto_v
    
    for u, v, _ in ligacoes_separadas:
        unir(u, v)

    grupos_map = defaultdict(list)
    for i in range(1, num_pontos + 1):
        grupos_map[encontrar(i)].append(i)

    return list(grupos_map.values())