# superclasse ou classe-pai exemplo
# Public -->    self.telefone = telefone 
# Protected --> self.__telefone = telefone # Private __
# Private -->   self._endereco = endereco # Protected _
class Pessoa:
    # construtor 
    def __init__(self, telefone, endereco):
        # Atributos
        self.__telefone = telefone # Private
        self.__endereco = endereco # Private

    # métodos getter e setter utilizados para controlar o acesso e modificação de atributos de uma classe
    
    # metodo  Getters retornam o valor de um atributo, permitindo acesso controlado ao atributo
    # metodo getter 
    @property
    def telefone(self):
        return self.__telefone
    
    # metodo  Setters definem ou modificam esse valor, muitas vezes com validação. 
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    # metodo getter 
    @property
    def endereco(self):
        return self.__endereco
    
    # metodo  Setters
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

#--------------------------
# subclasses ou classes-filha
class PessoaFisica(Pessoa):
    # construtor da classe PF
    def __init__(self, nome, cpf, telefone, endereco):
        self.__nome = nome
        self.__cpf = cpf
        # super().Pegar os atributos da superclasse
        super().__init__(telefone, endereco)
    
    # metodo getter 
    @property
    def nome(self):
        return self.__nome
    
     # metodo  Setters
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    # metodo  Getters
    @property
    def cpf(self):
        return self.__cpf
    
    # metodo  Setters
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
# ---------------------------
# subclasses ou classes-filha
class PessoaJuridica(Pessoa):
    # construtor da classe PJ
    def __init__(self,nome_fantasia, cnpj, telefone, endereco):
        self.__nome_fantasia = nome_fantasia
        self.__cnpj = cnpj
        # super().Pegar os atributos da superclasse
        super().__init__(telefone, endereco)

    # metodos getter e setter
    @property
    def nome_fantasia(self):
        return self.__nome_fantasia
  
    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self.__nome_fantasia = nome_fantasia
    
    @property
    def cnpj(self):
        return self.__cnpj
  
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj


    

    



