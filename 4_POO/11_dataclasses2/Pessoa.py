from abc import ABC, abstractmethod
from dataclasses import dataclass


# classe Pessoa
@dataclass
class Pessoa(ABC):
    # atributos + a tipagem
    email: str
    telefone: str
    endereco: str

    @abstractmethod
    def __str__(self):
        pass

