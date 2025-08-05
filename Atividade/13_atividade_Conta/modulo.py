def consultar_dados_conta(titular):
    print(f"Nome: {titular.get('nome')}")
    print(f"CPF: {titular.get('cpf')}")
    print(f"Agência: {titular.get('agencia')}")
    print(f"Conta: {titular.get('conta')}")
    print(f"Saldo: R$ {titular.get('saldo'):,.2f}")

def depositar(saldo, valor):
    saldo += valor
    return saldo

def sacar(saldo, valor):
    saldo -= valor
    return saldo

def imprimir_dados_conta(titular):
    print(f"{'='*30} EXTRATO BANCARIO{'='*30}")
    print(f"Nome: {titular.get('nome')}")
    print(f"Agência: {titular.get('agencia')}")
    print(f"Conta: {titular.get('conta')}")
    print(f"DEPOSITO DE : {titular.get('valor_depositar')}")
    print(f"SAQUE DE: {titular.get('valor_sacar')}")
    print(f"Saldo: R$ {titular.get('saldo'):,.2f}")
