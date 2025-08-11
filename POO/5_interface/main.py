import classes as c
import os

def limpar_terminal(): os.system("cls" if os.name == "nt" else "clear")

def main():
    # instancia objeto da clsse Conta
    cc = c.ContaCorrente(
        titular="",
        cpf="", 
        agencia="1230-0", 
        conta="52318-1", 
        saldo=0.0)
    
    while True:
        print(f"{'-'*20}  🐍BANCO COBRA 🐍 🐍 {'-'*20}\n")
        print("1 - Informar dados do titular")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Consultar dados da conta")
        print("5 - Sair do programa")
        opcao = input("Informe a opcao desejada: ").strip()
        limpar_terminal()

        match opcao:
            case "1": # informar dados do titular
                try:
                    cc.nome_titular = input("Informe o nome do titular: ").strip().title()
                    cc.cpf_titular = input("Informe o CPF do titular: ").strip()
                    conta = cc.conta
                    agencia = cc.agencia
                    limpar_terminal()
                    print("Dados cadastrado com sucesso!")
                except Exception as e:
                    print(f"Nao foi possivel informar os dados. Erro: {e}")
                finally:
                    continue
            case "2": # depositar
                try:
                    valor = float(input("Informe o valor a ser depositado: ").strip().replace(',','.'))
                    limpar_terminal()
                    if valor > 0:
                        print(f"Deposito efetuado!")
                        print(f"Seu novo saldo é: R$ {cc.depositar(valor):.2f}")
                    else:
                        print("Valor invalido!")
                except Exception as e:
                    print(f"Nao foi possivel depositar. Erro: {e}")
                finally:
                    continue
            case "3": # sacar
                try:
                    valor = float(input("Informe o valor a ser sacado: ").strip().replace(',','.'))
                    limpar_terminal()
                    if valor > 0:
                        if valor <= cc.saldo:
                            print(f"Valor sacado com sucesso!")
                            print(f"Seu novo saldo é: R$ {cc.sacar(valor):.2f}")
                        else:
                            print("Saldo insuficiente!")
                    else:
                        print("Valor invalido!")
                except Exception as e:
                    print(f"Nao foi possivel sacar. Erro: {e}")
                finally:
                    continue
            case "4": # consultar dados da conta
                limpar_terminal()
                cc.consultar_dados()
                continue
            case "5":
                print("Encerrado!")
                break
            case _:
                print("Opcao invalida!")
                continue    

if __name__ == "__main__":
    main()