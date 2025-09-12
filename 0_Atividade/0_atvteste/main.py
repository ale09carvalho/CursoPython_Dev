class Conta:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0.0

    def exibir_dados(self):
        print(f"Nome do titular: {self.nome}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

def menu():
    conta = None
    while True:
        print("\n===== MENU =====")
        print("1. Criar conta")
        print("2. Exibir dados da conta")
        print("3. Depositar valor")
        print("4. Sacar valor")
        print("5. Encerrar conta")
        print("6. Sair do programa")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            if conta is None:
                nome = input("Digite o nome do titular: ")
                conta = Conta(nome)
                print("Conta criada com sucesso!")
            else:
                print("Conta já existe. Encerre a atual antes de criar outra.")

        elif opcao == '2':
            if conta:
                conta.exibir_dados()
            else:
                print("Nenhuma conta criada.")

        elif opcao == '3':
            if conta:
                valor = float(input("Digite o valor a depositar: "))
                conta.depositar(valor)
            else:
                print("Nenhuma conta criada.")

        elif opcao == '4':
            if conta:
                valor = float(input("Digite o valor a sacar: "))
                conta.sacar(valor)
            else:
                print("Nenhuma conta criada.")

        elif opcao == '5':
            if conta:
                print(f"Conta de {conta.nome} encerrada.")
                conta = None
            else:
                print("Nenhuma conta criada para encerrar.")

        elif opcao == '6':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
