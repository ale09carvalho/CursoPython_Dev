# Progressão Aritmética

a1 = int(input("Digite o primeiro termo: "))
n = int(input("Número de Termos: "))
razao = int(input("Razao: ") )
ultimo = a1 + (n-1)*razao
ultimo = ultimo + 1

for var in range(a1, ultimo, razao):
    print(f'{var:.0f}', end=' -> ')
print("FIM")