'''
Criar uma funçao e aplicar em uma lista - coleções
'''
# lambda que calcula pg
pg = lambda x: x * 2
pa = lambda x: x + 2

# Algoritmo Principal
if __name__ == "__main__":
    # lista
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Exibe a pa e a pg
    print(f"Progressao Geometrica: {list(map(pg, numeros))}")
    print(f"Progressao Aritimetica: {list(map(pa, numeros))}")

