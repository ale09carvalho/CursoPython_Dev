# importa modulo - melhor opção para usar import 
'''
A expressão from module import name em Python
importa um nome específico (função, variável, classe, etc.) de um módulo para o namespace atual,
permitindo que você use esse nome diretamente, sem precisar do prefixo do nome do módulo. 
'''

from modulo import limpar_tela, velocidade_media, aceleracao_media


# algoritmo principal - bloqueia o import e manter a integridade do sistema
if __name__ == "__main__":
    v = 0

    while True:
        print("1 - Calcular velocidade média")
        print("2 - Calcular aceleraçao")
        print("3- Sair do Programa")

        opcao = input("Informe a opçao desejada: ").strip()
        limpar_tela()
        match opcao:
            case "1":
                try:
                    vi = float(input("Informe a velocidade inicial: ").replace(",","."))
                    vf = float(input("Informe a velocidade final: ").replace(",","."))
                    v = velocidade_media(vf,vi)
                    limpar_tela()
                    print (f"A velocidade media é: {v}")

                except Exception as e:
                    print( f"Erro. {e}.")
                finally:
                    continue
            case "2":
                try:
                    t = float(input("Informe o tempo: ").replace(",","."))
                    limpar_tela()
                    #if v != 0:
                    if v is not 0:
                        a = aceleracao_media(v, t)
                        print(f"Aceleraçao média: {a}.")
                    else:
                        print("Sem informaçao da velocidade média.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "3":
                print("Programa encerrado! ")
                break
            case _:
                print ("Opçao invalida. ")
                continue 


