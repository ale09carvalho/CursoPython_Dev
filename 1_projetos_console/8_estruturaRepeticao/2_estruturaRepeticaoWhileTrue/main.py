# No python nao exite o comando  Do while, mas sim o while True

# while True: 
while True:
    # menu
    print(f"\n{'-'*20} MENU {'-'*20}")
    print("0 - Encerrar programa")
    print("1 - SOMAR")
    print("2 - Subtrar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print(f"{'-'*50}")
    
    operador = input("Informe a operaçao desejada: ").strip()
    # .strip() é usado para remover espaços em branco no início e no final da string.

    match operador:

        case "0": # implementar a logica de encerrar o programa
            print("Encerrando o programa...")
            break  # Encerra o loop e o programa

        case "1":  # Implementar a logica de somar
            try:
             # Entrada de dados
                x = float(input("Informe o valor de X: ").replace(',', '.'))
                y = float(input("Informe o valor de Y: ").replace(',', '.'))

                print(f"A soma dos valores é {x + y}.")
            except Exception as e:
                print(f"Não foi possível ocorreu um erro: {e}")
            finally:
                continue

        case "2": # Implementar a logica de subtrair
            try:
                # Entrada de dados
                x = float(input("Informe o valor de X: ").replace(',', '.'))
                y = float(input("Informe o valor de Y: ").replace(',', '.'))

                print(f"A subtração dos valores é {x - y}.")
            except Exception as e:
                print(f"Não foi possível ocorreu um erro: {e}")
            finally:
                continue
        case "3": # Implementar a logica de multiplicar
            try:
                # Entrada de dados
                x = float(input("Informe o valor de X: ").replace(',', '.'))
                y = float(input("Informe o valor de Y: ").replace(',', '.'))

                print(f"A multiplicação dos valores é {x * y}.")
            except Exception as e:
                print(f"Não foi possível ocorreu um erro: {e}")
            finally:
                continue
        case "4": # Implementar a logica de dividir
            try:
                # Entrada de dados
                x = float(input("Informe o valor de X: ").replace(',', '.'))
                y = float(input("Informe o valor de Y: ").replace(',', '.'))

                if y == 0: # y não pode ser zero para evitar divisão por zero
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    print(f"A divisão dos valores é {x / y}.")
            except Exception as e:
                print(f"Não foi possível ocorreu um erro: {e}")
            finally:
                continue
            print("Opcao invalida, tente novamente.")
        case _:  # Caso não corresponda a nenhum dos anteriores
            print("Opção inválida, por favor, escolha uma opção válida entre 0 e 4.")
            continue  # Continua o loop para solicitar novamente a operação
# Fim do programa
