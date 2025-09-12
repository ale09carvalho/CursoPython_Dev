# Dataclasses - Herança
import PessoaFisica
import PessoaJuridica
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")


def main():
    usuario = PessoaFisica.PessoaFisica(email="",telefone="",endereco="", nome="",cpf="", idade=0)
    empresa = PessoaJuridica.PessoaJurica(email="",telefone="",endereco="", razao_social="",nome_fantasia="",cnpj="")

#input do usuario
    print("Entre com os dados do Usuário:\n")
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf =  input("Informe o cpf: ").strip()
    usuario.idade = int(input("Informe a idade: "))
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.telefone =  input("Informe o telefone: ").strip()
    usuario.endereco =  input("Informe o endereço: ").strip() 
    limpar()

    #definir os valores dos atributos - input da EMPRESA
    print("Entre com os dados da Empresa:\n")
    empresa.razao_social = input("Informe a razão social: ").strip().title()
    empresa.nome_fantasia = input("Informe o Nome da empresa: ").strip().title()
    empresa.cnpj =  input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o e-mail: ").strip().lower()
    empresa.telefone =  input("Informe o telefone: ").strip()
    empresa.endereco =  input("Informe o endereço: ").strip().title()
    limpar()

    # output
    print(usuario)
    print(empresa)

if __name__ == "__main__":
    main()
