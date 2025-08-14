# Dataclasses:forma simplificada de criar classes armazenam dados, classes com atributos e métodos específicos manipulação de dados.
import Pessoa
import os
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    # instanciar a classe Pessoa
    # ja esta encapsulado e com os metodo gett e sett
    usuario = Pessoa.Pessoa(
        nome="", 
        email="", 
        cpf="", 
        idade=0, 
        altura=0.0
    )

    #inputs
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.email = input("Informe o email: ").strip().lower()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.idade = int(input("Informe a idade: "))
    usuario.altura = float(input("Informe a altura: ").replace("," , "."))
    limpar()

    #output
    print(usuario)

    # fim do objeto
    del(usuario)

if __name__ == "__main__":
    main()

