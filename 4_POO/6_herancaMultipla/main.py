# criar objetos - criar um objeto da classe ContaCorrente
import ContaCorrente as cc
import os

def limpar_terminal(): 
    os.system("cls" if os.name == "nt" else "clear")

# função main
def main():
    # instancia do objeto
    conta = cc.ContaCorrente(
        nome="", 
        cpf="", 
        email="", 
        profissao="", 
        telefone="", 
        endereco="", 
        salario=0.0, 
        agencia="1230-0", 
        numero="52318-6", 
        saldo=0.0
    )
    #conta.exibir_dados()

    while True:
        print(f"{'-'*20} 😁BANCO COBRA {'-'*20}")
        print("1 - Cadastrar Conta Corrente")
        print("2 - Exibir dados da conta")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Sair")
        opcao = input("Opcao desejada: ").strip()
        limpar_terminal()

        match opcao:
            case "1": # Cadastrar 
                try: 
                    conta.nome = input("NOME do titular : ").strip().title()
                    conta.cpf = input("CPF do titular: ").strip()
                    conta.email = input("E-MAIL do titular: ").strip()
                    conta.profissao = input("PROFISSÃO do titular: ").strip().title()
                    conta.telefone = input("TELEFONE do titular: ").strip()
                    conta.endereco = input("ENDEREÇO do titular: ").strip().title()
                    conta.salario = float(input("SALÁRIO atual do titular: ").strip().replace(',','.'))
                    limpar_terminal()
                    print("Conta cadastrada com sucesso!")
                except Exception as e:
                    print(f"Nao foi possivel cadastrar a conta. Erro: {e}")
                finally:
                    continue
            case "2": # Exibir dados da conta
                try: 
                    conta.exibir_dados()
                except Exception as e:
                    print(f"Nao foi possivel exibir os dados da conta. Erro: {e}")
                finally:
                    continue
            case "3": # Depositar
                try: 
                    valor = float(input("Informe o valor a ser depositado: ").strip().replace(',','.'))
                    limpar_terminal()
                    if valor > 0:
                        print(f"Valor R$ {valor:.2f} depositado com sucesso! Novo saldo: {conta.fazer_deposito(valor)}")
                    else:
                        print("O valor deve ser maior que zero!")
                except Exception as e:
                    print(f"Nao foi possivel depositar o valor. Erro: {e}")
                finally:
                    continue
            case "4":
                try: 
                    valor = float(input("Informe o valor a ser sacado: ").strip().replace(',','.'))
                    limpar_terminal()
                    if valor > 0:
                        if valor <= conta.saldo:
                            print(f"Valor R$ {valor:.2f} sacado com sucesso! Novo saldo: {conta.fazer_saque(valor)}")
                        else:
                            print("Saldo insuficiente!")
                    else: 
                        print("O valor deve ser maior que zero.")
                except Exception as e:
                    print(f"Nao foi possivel sacar o valor. Erro: {e}")
                finally:
                    continue
            case "5":
                print("Saindo do programa...")
                break

            case _:
                print("Opcao invalida!")
                continue

# impede a importação
if __name__ == "__main__":
    main()