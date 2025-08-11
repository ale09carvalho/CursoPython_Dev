# Abstraçao: sao classes que nao podem ser instanciadas, ou seja, nao podem ser criados objetos a partir delas.
# Classes abstratas: sao classes que nao podem ser instanciadas, ou seja, nao podem ser criados objetos a partir delas.
# Classes finais: sao classes que nao podem ser herdadas, ou seja, nao podem ser extendidas por outras classes.
# Interface
from abc import ABC
from abc import abstractmethod

# Classe abstrada (ABC)
class Conta(ABC):
    # construtor 
    @abstractmethod
    def __init__(self, saldo):
        # atributos private
        self.__saldo = saldo
    
    # metodo getter do atributo saldo
    @property
    def saldo(self):
        return self.__saldo

    # metodo setter do atributo saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    

    # Metodo de açao - @abstractmethod funciona como uma interface, obriga as subclasses a desenvolverem os metodos da superclasse 
    @abstractmethod # garantir que a subsclasse tenha esse metodo
    def consultar_dados(self):
        pass # utilizado como reticencia ...
    
    @abstractmethod
    def depositar(self, valor):
        pass  # utilizado como reticencia ...

    @abstractmethod
    def sacar(self, valor):
        pass  # utilizado como reticencia ...

# Classe filha - ContaCorrente herdando da classe Conta
class ContaCorrente(Conta):
    def __init__(self,titular, cpf, agencia, conta, saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = conta
        # super().Pegar os atributos da superclasse
        super().__init__(saldo)

    # metodos getter e setter
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta = conta
    
    # Metodos obrigatorio da Interface
    def consultar_dados(self):
        print (f"{'-'*20} 🐍DADOS DA CONTA🐍 {'-'*20}\n")
        print (f"Titular da conta: {self.__titular}")
        print (f"CPF do Titular: {self.__cpf}")
        print (f"Agencia: {self.__agencia}")
        print (f"Num Conta: {self.__conta}")
        print (f"Saldo: R$ {self.saldo:.2f}")
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo
    
    


       

