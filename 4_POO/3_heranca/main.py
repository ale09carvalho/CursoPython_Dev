import classes as c
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")


# função main para inserir cod pinc.
# metodo main
def main():
       # instaciar as classes
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="")

    # definir os valores dos atributos - input do USUARIO
    print("Entre com os dados do Usuário:\n")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf =  input("Informe o cpf: ").strip()
    usuario.telefone =  input("Informe o telefone: ").strip()
    usuario.endereco =  input("Informe o endereço: ").strip().title()
    
    limpar()

   # definir os valores dos atributos - input da EMPRESA
    print("Entre com os dados da Empresa:\n")
    
    empresa.nome_fantasia = input("Informe o Nome da empresa: ").strip().title()
    empresa.cnpj =  input("Informe o CNPJ: ").strip()
    empresa.telefone =  input("Informe o telefone: ").strip()
    empresa.endereco =  input("Informe o endereço: ").strip().title()

    # Output “saída”
    limpar()
    print("Dados do usuario: ")
    usuario.exibir_dados()

    print("Dados da Empresa: ")
    empresa.exibir_dados()


# chama o metodo main
if __name__ == "__main__":
    main()

 