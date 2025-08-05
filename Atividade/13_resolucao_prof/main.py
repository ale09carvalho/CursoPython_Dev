''' ATIVIDADE:
# TODO - atividade: Crie um programa de aplicativo de banco, onde:
- O usuário cria uma conta no banco com os seguintes dados:
-- Titular da conta
-- CPF do titular
-- Agência
-- Número da conta
-- Saldo
O usuário pode fazer no programa:
- Consultar dados
- Depositar valor
- Sacar valor
- Imprimir extrato (entende-se: gerar arquivo com os dados da conta)
- Sair do programa
# NOTE - o nome da classe é Conta
'''
# Import bibliotecas
import os
import classe as c

# funçao limpa tela
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    
    # instancia da classe
    cc = c.Conta(titular="", cpf="", agencia="", conta="", saldo= 0.0)

    # define os valores dos atributos
    cc.titular = input("Informe o nome do titular da Conta: ").strip().title()
    cc.cpf = input("Informe o CPF do titular: ").strip()
    cc.agencia = "1010-1"
    cc.conta = "10101-1"
    limpar()

    while True:
        print(f"{'='*30} 🐍 BANCO COBRA {'='*30}")
        print(" 1 - Consultar dados da conta")
        print(" 2 - Realizar Depositar")
        print(" 3 -  Realizar Saque")
        print(" 4 - Gerar extrato - dados da conta")
        print(" 5 - Sessão encerrada")
        
        opcao = input("Opcao desejada: ")
        limpar()

        match opcao:
            case "1": # Consultar dados
                cc.consultar_dados()
                continue

            case "2": # Realizar Deposito
                try:
                    valor = float(input("Informe o valor a ser depositado: R$ ").replace(",", "."))
                    limpar()
                    if valor > 0:
                        print(f"Deposito efetuado com sucesso! Saldo: R$ {cc.depositar(valor):.2f}")
                    else:   
                        print("Valor Inválido para depósito")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue

            case "3": # Realizar Saque
                try:
                    valor = float(input("Informe o valor a ser sacado: R$ ").replace(",", "."))
                    limpar()
                    if valor > 0:
                        if valor <= cc.saldo:
                            print(f"Saque efetuado com sucesso: R$ {cc.sacar(valor):.2f}.")
                        else:
                            print("Saldo insuficiente.")
                    else:
                        print("Valor para saque inválido.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "4": # Gerar arquivo conta.json (extrato)
                try:
                    cc.imprimir_extrato()
                    print("Extrato impresso com sucesso!")

                except Exception as e:
                    print(f" Erro. não foi possivel imprimir extrato {e}.")
                finally:
                    continue

            case "5": # programa Encerrado
                print("Programa encerrado!")
                break
            case __:
                print("Opcao invalida! Tente novamente.\n")
                continue