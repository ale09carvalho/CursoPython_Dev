'''
# TODO -  ATIVIDADE:
Crie um programa com o seguinte menu:
- Calcular àrea de um círculo
- Calcular tamanho de uma circunferência
- Sair do programa
'''
# importando biblioteca
import math as m

print(f"{'='*10}MENU{'='*20}\n")
print("Escolha a opção.")
print(" 1 - Calcular a area do cículo.")
print(" 2 - Calcular o tamanho da circunferência.")
print(" 3 - Sair do programa.")

opcao = int(input("Informe a opção desejada: ").strip())

try:
    match opcao:
        case 1:
            r = float(input("Informe o raio do circulo: "))
            a = m.pi *(r**2)
            print(f"A area do circulo corresponde a: {a}.")
        case 2: 
            r = float(input("Informe o raio do circulo: "))
            perimetro = 2 * m.pi * r
            print(f"O tamanho da circunferência corresponde a: {perimetro :.2f}")
        case 3:
            print("Programa encerrado.")    
        case _:
             print("Operação inválida.")

except Exception as e:
    print(f"Não foi possivel executar a operação. {e}.")

# fim programa
