from dataclasses import dataclass

# classe Pessoa
@dataclass

class Pessoa:
    # atributos + a tipagem
    nome: str
    email: str
    cpf: str
    idade: int
    altura: float

    # metodos especiais da classe
    def  __str__(self):
        return f"Nome: {self.nome}\nE-mail: {self.email}\nCPF: {self.cpf}\nIdade: {len(self)}\nAltura: {self.altura}"

    def __len__(self):
        return self.idade
    
    def __del__(self):
        print(f"Fim do objeto {self.nome}.")


