def imprimir_grupos(grupos):
    print("Agrupamentos:")
    for grupo in grupos:
        print(', '.join(map(str, sorted(grupo))))
        