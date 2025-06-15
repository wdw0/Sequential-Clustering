from distancia import distancia_euclidiana
from collections import defaultdict

def formar_ligacoes(pontos):
    ##gera a lista de ligacoes entre os pontos, comecando do 1. A cada passo, conecta o ponto atual ao mais proximo ainda nao visitado.
    ##retorna uma lista de tuplas: (ponto_a, ponto_b, distancia)
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
                ##desempate por menor ID
                dist = distancia_euclidiana(pontos[atual], ponto)
                if(dist < menor_dist) or (dist == menor_dist and i < menor):
                    menor = i
                    menor_dist = dist
        ligacoes.append((atual + 1, menor + 1, menor_dist))
        visitados[menor] = True
        atual = menor
    return ligacoes

def formar_grupos(ligacoes, num_pontos, k):
    ##forma K grupos cortando as K-1 maiores ligacoes, usei union-find para agrupar.

    
    ligacoes.sort(key=lambda x: x[2], reverse = True)
    ligacoes_separadas = ligacoes[k - 1:] #removendo as K-1 maiores ligacoes
    # Inicializa os pais de cada ponto (Union-Find)
    pais = {i: i for i in range(1, num_pontos + 1)}

    def encontrar(u):
        # Encontra o representante do conjunto (com compressao de caminho)
        while pais[u] != u:
            pais[u] = pais[pais[u]]
            u = pais[u]
        return u

    def unir(u, v):
        # Une dois conjuntos
        ponto_u = encontrar(u)
        ponto_v = encontrar(v)
        if ponto_u != ponto_v:
            pais[ponto_u] = ponto_v

    # Une os pontos conforme as ligacoes restantes
    for ponto_u, ponto_v, _ in ligacoes_separadas:
        unir(ponto_u, ponto_v)

    # Agrupa os pontos pelo representante de conjunto
    grupos_map = defaultdict(list)
    for i in range(1, num_pontos + 1):
        grupos_map[encontrar(i)].append(i)

    return list(grupos_map.values())