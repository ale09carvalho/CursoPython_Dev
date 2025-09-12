import modulo as mo

# algoritmo principal - bloqueia o import e manter a integridade do sistema
if __name__ == "__main__":

    while True:
        print("1 - Calcular equaçao do 1º Grau: ")
        print("2 - Calcular equaçao do 2º Grau: ")
        print("3- Sair do Programa")

        opcao = input("Informe a opçao desejada: ").strip()
        mo.limpar_tela()

        match opcao:
            case "1":
                try:
                    a = float(input("Informe o valor de a: ").replace(",","."))
                    b = float(input("Informe o valor de b: ").replace(",","."))
                    mo.limpar_tela()

                    x = mo.primeiro_grau(a, b)
                    print(f"O valor de x é {x}. ")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            
            case "2":
                try:
                    a = float(input("Informe o valor de a: ").replace(",","."))
                    b = float(input("Informe o valor de b: ").replace(",","."))
                    c = float(input("Informe o valor de c: ").replace(",","."))
                    mo.limpar_tela()
                    x = mo.segundo_grau(a, b, c)
                    
                    # FIXIME print(f"{x}.") 


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