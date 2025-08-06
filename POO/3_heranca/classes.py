# superclasse ou classe-pai
class Pessoa:

    # construtor 
    def __init__(self, telefone, endereco):
        # Atributos
        self.telefone = telefone
        self.endereco = endereco

    # metodo da classe Pai
    def exibir_dados(self):
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

# subclasses ou classes-filha
class PessoaFisica(Pessoa):
    # construtor da classe PF
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        # super().Pegar os atributos da superclasse
        super().__init__(telefone, endereco)

    # poliformismo
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        super().exibir_dados()


# subclasses ou classes-filha
class PessoaJuridica(Pessoa):
    # construtor da classe PJ
    def __init__(self,nome_fantasia, cnpj, telefone, endereco):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        # super().Pegar os atributos da superclasse
        super().__init__(telefone, endereco)
    
    # poliformismo
    def exibir_dados(self):
        print(f"Nome Empresa: {self.nome_fantasia}")
        print(f"Cnpj: {self.cnpj}")
        super().exibir_dados()




