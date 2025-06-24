#  Resolução do Professor
import os
import datetime
from datetime import date

# formatando data e hora
data = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

# filmes das salas
sala1 = "A Roda Quadrada"
sala2 = "A Volta dos Que Não Foram"
sala3 = "Poeira em Alto Mar"
sala4 = "As Tranças do Rei Careca"
sala5 = "A Vingança do Peixe Frito"

# tratamento de exceção
try:
    # input do usuário
    nome = input("Informe seu nome: ").title().strip()
    idade = int(input("Informe sua idade: "))

    while True:
        # menu
        print(f"{'-'*20}🎞️  CINE COBRA 🎞️{'-'*20}")
        print(f"Sala 1 - {sala1} - Livre")
        print(f"Sala 2 - {sala2} - 12 anos")
        print(f"Sala 3 - {sala3} - 14 anos")
        print(f"Sala 4 - {sala4} - 16 anos")
        print(f"Sala 5 - {sala5} - 18 anos")
        sala = input("Informe o número da sala desejada: ").strip()
        os.system("cls" if os.name == "nt" else "clear")

        match sala:
            case "1":
                idade_minima = 0
                filme = sala1
            case "2":
                idade_minima = 12
                filme = sala2
            case "3":
                idade_minima = 14
                filme = sala3
            case "4":
                idade_minima = 16
                filme = sala4
            case "5":
                idade_minima = 18
                filme = sala5
            case _:
                print("Sala inexistente. Favor escolher outra sala.")
                continue
        if idade >= idade_minima:
            print(f"{'-'*20}🐍 INGRESSO CINE COBRA 🐍{'-'*20}")
            print(f"{'-'*60}\n")
            print(f"🎟️ Filme: {filme} - {idade_minima}")
            print(f"Ingresso comprado por {nome} no dia {data} às {hora}.")
            print("TENHA UM BOM FILME!!! 😎")
            print(f"{'-'*60}")
            break
        else:
            print(f"{nome} não possui a idade mínima para ver {filme}.")
            print("Favor escolher outro filme.")
            continue
        
except Exception as e:
    print(f"Não foi possível comprar ingresso. {e}.")        