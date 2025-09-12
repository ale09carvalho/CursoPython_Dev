# Progressão Geometrica
def progressao_geometrica(a, r, n):
    resultado = []
    termo_atual = a
    for i in range(n):
        resultado.append(termo_atual)
        termo_atual *= r
    return resultado

a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
n = int(input("Digite o número de termos: "))
if n > 0:
    pg = progressao_geometrica(a1, r, n)
    print(pg)
else:
    print("O número de termos deve ser positivo.")