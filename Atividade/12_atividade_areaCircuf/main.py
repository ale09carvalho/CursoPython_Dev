'''
# TODO - atividade: crie um programa que calcule a area e a circunferência de um circulo
# NOTE - use o lambda

'''
# funcao usuando o recurso lambda
import math
import os

# Funçao Normal
# def calcular_area_circulo(r):
    # A = π * r²
#    return math.pi * (r** 2)

# Funçao Lambda
area_circunferencia = lambda r: math.pi * (r**2)
comprimento_circunferencia = lambda r: 2*math.pi*r
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

# Algoritmo Principal
if __name__ == "__main__":
    try:
        r = float(input("Informe o raio do circulo: ").replace(",","."))
        A = area_circunferencia(r)
        comp = comprimento_circunferencia(r)
        
        limpar()
        print(f"A area do circulo é: {A:,.2f}")
        print(f"Comprimento da circunferencia: {comp}")
    except Exception as e:
        print(f"Nao foi possivel calcular a area do circulo. Erro: {e}")

