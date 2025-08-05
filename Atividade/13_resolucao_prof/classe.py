# classe
import json

# classe
class Conta:

    # construtor
    def __init__(self, titular, cpf, agencia, conta, saldo):
    # Atributos
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    # metodos consulta_dados
    def consultar_dados(self):
        print(f"Titular: {self.titular}.")
        print(f"CPF: {self.cpf}.")
        print(f"Agencia: {self.agencia}.")
        print(f"Conta: {self.conta}.")
        print(f"Saldo: {self.saldo:.2f}.")
    
    # metodo deposito
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
     # metodo Saque
    def sacar(self, valor):
       self.saldo -= valor
       return self.saldo

    def imprimir_extrato(self):
        #dicionario
        dados = {
            'Nome do titular': self.titular,
            'CPF do titular': self.cpf,
            'Conta': self.conta,
            'Agencia': self.agencia,
            'Saldo': self.saldo
        }
        with open("conta.json","w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
