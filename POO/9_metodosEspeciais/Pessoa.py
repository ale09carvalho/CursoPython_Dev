# métodos especiais também conhecidos como métodos mágicos ou Dunder, 
# são métodos que definem o comportamento de classes e objetos,sendo invocados automaticamente sob circunstâncias especiais.
#  começam e terminam com dois sublinhados (__).

class Pessoa:
    # método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self): # o objeto deve ser representado como uma string
        # return f"Olá, meu nome é: {self.nome} e tenho {self.idade} anos."
        return f"Olá, meu nome é: {self.nome} e tenho {len(self)} anos."
    
    def __len__(self): # retorna um valor inteiro maior ou igual a zero
        return self.idade
    
    # metodo destrutor  
    def __del__(self):
        print(f"Objeto {self.nome} destruido com sucesso.")
    