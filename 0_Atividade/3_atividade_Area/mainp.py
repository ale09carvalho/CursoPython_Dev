'''
# TODO -  ATIVIDADE:
Crie um programa com o seguinte menu:
- Calcular àrea de um círculo
- Calcular tamanho de uma circunferência
- Sair do programa
'''
# importando biblioteca
import math as m
import os 

while True:
    # Menu
    print(f"{'='*10}MENU{'='*20}\n")
    print("Escolha a opção.")
    print(" 1 - Calcular a area do cículo.")
    print(" 2 - Calcular o tamanho da circunferência.")
    print(" 3 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    
    # se sistema for linux (clear)
    # utiliza  ternário
    os.system( "cls" if os.name == "nt" else "clear") 
    try:
        if opcao == "1" or opcao == "2":
            raio = float(input("Informe o raio do circulo: ").replace(",","."))
        else:
            os.system( "cls" if os.name == "nt" else "clear") 
        match opcao:
            case "1":
                # "A=πr2"
                area = (m.pi*raio**2)
                print(f"A area do circulo corresponde a: {area :.2f}.")
            case "2":
                # C = 2πr
                circuferencia = (2 * m.pi * raio)
                print(f"O tamanho da circunferência corresponde a: {circuferencia :.2f}")
            case "3":
                print("Programa Encerrado.")
                break
            case _:
                print("Operação inválida.")

    except Exception as e:
        print(f"Não foi possivel executar a operação. {e}.")
        continue

# fim programa

