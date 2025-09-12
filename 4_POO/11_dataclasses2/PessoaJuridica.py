import Pessoa
from dataclasses import dataclass


@dataclass
class PessoaJurica(Pessoa.Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj:str

    def __str__(self):
        return f"{'-'*20} DADOS DA EMPRESA {'-'*20}\n\nNome da Empresa: {self.razao_social}\n Nome fantasia:{self.razao_social}\nCNPJ: {self.cnpj}\nE-mail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"
    
