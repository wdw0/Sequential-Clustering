from io_control import ler_csv_entrada, escrever_csv_saida
from clustering import formar_ligacoes, formar_grupos
from utils import imprimir_grupos

def main():
    entrada = input("Informe o nome do arquivo de entrada: ")
    saida = input("Informe o nome do arquivo de saida: ")
    k = int(input("Informe a quantidade de grupos (K): "))

    pontos = ler_csv_entrada(entrada) #Leitura de pontos do CSV
    ligacoes = formar_ligacoes(pontos) #Construcao da lista de ligacoes
    grupos = formar_grupos(ligacoes, len(pontos), k) #Criacao dos grupos

    escrever_csv_saida(grupos, saida)
    #imprimir_grupos (grupos) imprimindo no terminal para testes

if __name__ == "__main__":
    main()