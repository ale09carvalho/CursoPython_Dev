'''
# TODO - ATIVIDADE:
Crie um programa que receba de um professor várias notas de um aluno de 0 a 10 (não importa qts notas)
Ao final do programa, a media das notas devera ser calculada e informada, e em seguida, o programa irá informar
se o aluno:
- Foi aprovado, caso a media for maior ou igual a 7
- Ficou de recuperaçao, caso a media for entre 5 e 7
- Foi reprovado, caso a média for menor que 5.
'''
import os

# declaraçao de variavel
notas = []

while True: 
    print("[1] - Informe a nota do aluno de 0 a 10;")
    print("[2] - Tirar a média e sair do programa;")

    opcao = input("Informe a opcao desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal
    
    match opcao:
        case "1":
            try:
                nova_nota = float(input("Inseria a nova nota ").replace(",","."))
                if nova_nota >= 0 and nova_nota <= 10:
                   os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal
                   notas.append(nova_nota) # append() adiciona novo valor a nota ao final da lista

                   print("Nota inserida com sucesso")
                else:
                    print("Nota invalida.")
            except Exception as e:
                   print (f"Nao foi possivel insarir a nota {e}.")
            finally:
                continue
        case "2":
            try:
                media = sum(notas)/ len(notas)
                print(f"Media: {media:.2f}")
                if media >= 7:
                     print("Aluno esta aprovado")
                elif media >= 5:
                      print("Aluno esta recuperção")
                else:
                    print("Aluno está reprovado.")
            except Exception as e:
                print(f"Não foi possível calcular a média.")
            finally:
                break
        case _:
            print("Opção inválida.")
            continue