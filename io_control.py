
def ler_csv_entrada(nome_arquivo):
    pontos = []
    with open(nome_arquivo, 'r') as file:
        for linha in file:
            if linha.strip():
                coords = list(map(float, linha.strip().split(',')))
                pontos.append(coords)
            
    return pontos

def escrever_csv_saida(grupos, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        for grupo in grupos:
            linha = ', '.join(map(str, sorted(grupo)))
            file.write(linha + '\n')

