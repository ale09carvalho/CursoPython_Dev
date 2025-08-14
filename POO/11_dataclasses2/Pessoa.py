from dataclasses import dataclass


# classe Pessoa
@dataclass
class Pessoa:
    # atributos + a tipagem
    email: str
    telefone: str
    endereco: str
