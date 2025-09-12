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
import os
import random
import modulo as m

if __name__ == "__main__":
    conta = {}

    try:
        while True:
            print(f"{'='*30} BANCO DO DF {'='*30}")
            print(" 0 - Sessão encerrada")
            print(" 1 - Criar nova conta bancaria")
            print(" 2 - Consultar dados da conta")
            print(" 3 - Realizar Depositar")
            print(" 4-  Realizar Saque")
            print(" 5 - Gerar extrato - dados da conta")

            opcao = input("Opcao desejada: ")
            os.system('cls')
            
            match opcao:
                case "0":
                    print("Programa encerrado!")
                    break
            
                case "1": # Criar nova conta
                    conta["agencia"] = 1010
                    conta["conta"] = random.randint(10000, 99999)  # gerar números aleatórios, randint() 
                    conta["saldo"] = 0 # inica o saldo com 0
                    conta["nome"] = input("Informe o nome do titular: ")
                    conta["cpf"] = input("Informe o CPF do titular: ")
                
                    os.system('cls')
                    print(f"Conta: {conta.get('conta')} cadastrada com sucesso!\n")
                    continue

                case "2": # Consultar dados da conta Bancaria
                    os.system('cls')
                    m.consultar_dados_conta(conta)
                    continue
                
                case "3": # Realizar deposito
                    os.system('cls')
                    valor_depositar = float(input("Informe o valor a ser depositado: R$ ").replace(",", "."))
                    conta["saldo"] = m.depositar(conta.get("saldo"), valor_depositar)
                    os.system('cls')
                    print(f"Valor depositado com sucesso!")
                    print(f"Seu novo saldo é: R$ {self.conta('saldo'):,.2f}\n")
                    continue

                case "4": # Realizar Saque
                    os.system('cls')
                    valor_sacar = float(input("Informe o valor a ser sacado: R$ ").replace(",", "."))
                    saldo = conta.get("saldo")

                    if valor_sacar <= saldo:
                        conta["saldo"] = m.sacar(saldo, valor_sacar)
                        os.system('cls')
                        print("Valor retirado com sucesso!")
                        print(f"Seu novo saldo é: R$ {conta.get('saldo'):,.2f}\n")
                    else:
                        print("Saldo insuficiente!")
                        continue
                case "5": # Gerar extrato
                    os.system('cls')
                    m.imprimir_dados_conta(conta)
                    continue
                
                case _:
                    os.system('cls')
                    print("Opcao invalida! Tente novamente.\n")
                    continue

    except Exception as e:
        print(f"Nao foi possivel cadastrar a conta bancaria. Erro: {e}")





