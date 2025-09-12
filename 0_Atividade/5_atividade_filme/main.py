'''
TODO - ATIVIDADE: Crie um programa que recebe do usuario o nome e a idade, e em seguida, mostre um menu de filmes com suas respevtivas classificações indicativas e 
e salas de exibiçao. Exemplo:
- Sala 1: A Roda Quadrada - livre
- Sala 2 A volta dos que não foram - 12 anos
- Sala 3: Poeira em Alto Mar - 14 anos
- Sala 4: As Tranças do Rei Careca - 16 anos
- Sala 5: A Vingança do Peixe Frito - 18 anos
Usuario deve escolher a sala que esta passando o filme que deseja assistir.
- Se o usuario tiver a idde mínima ou mais para ver o filme, o programa imprime o ingresso com o nome do usuário, a sala, o nome do filme, a data e a hora da compra do ingresso,
e deseja bom filme, e em seguida, encerra o programa.
- Se o usuário não tiver a idade minima para ver o filme, o programa bloqueia a sua entrada, e re-exibe o menu de filmes para que ele escolha outro filme.
'''
import datetime
from datetime import date

hoje = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

try:
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))

    #laço repetição
    while True:

        print(f"{'-'*20}LISTA DE FILMES DISPONÍVEL{'-'*20}\n")
        print ("Sala 1 - A Roda Quadrada - LIVRE")
        print ("Sala 2 - A Volta Dos Que Não Foram - 12 anos")
        print ("Sala 3 - A Trança Do Rei Careca - 14 anos")
        print ("Sala 4 - Poeira em Alto Mar - 16 anos")
        print ("Sala 5 - A Vingança do Peixe Frito - 18 anos")

        # Opção de sala desejada
        sala = input(f"\nSala escolhida: ")

        # verifica a sala escolhida
        match sala:
            case "1":
                idade_minima = 0
            case "2":
                idade_minima = 12
            case "3":
                idade_minima = 14
            case "4":
                idade_minima = 16
            case "5":
                idade_minima = 18
            case _:
                idade_minima = idade+1 # Obriga o usuario escolher uma sala valida
        
        # Verificar se o usuario tem a idade minima para assistir o filme

        if idade >= idade_minima:
            print(f"Olá, {nome} no dia: {hoje} as: {hora}, por favor dirija a sala {sala} escolhida. Tenha um bom filme!")
            break # encerra laço
        else:
            print(f"{nome}, você não tem idade para assistir a esse filme.")
            print("Por favor, escolha outra opçcao de filme.")
            continue # continua o laço de repeticao
except Exception as e:
    print (f"Não foi possivel executar a operaçao! {e}.")
finally:
    print("Programa encerrado")