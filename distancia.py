import math

#Vai receber dois vetores com as coordenadas dos dois pontos e retornar a distancia euclidiana entre eles
def distancia_euclidiana(p1, p2):
    distancia = math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
    return distancia