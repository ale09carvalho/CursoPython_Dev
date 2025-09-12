import classes as c
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

# instaciar as classes
def main ():
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="")

    # setando os valores do usuario - definir os valores dos atributos
    print("Insira os dados do usuario:\n")
    #--------metodo set--------------------
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip().title()
    usuario.telefone = input("Informe o Telefone: ").strip().title()
    usuario.endereco = input("Informe o Endereco: ").strip().title()

    limpar()

    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.telefone = input("Informe o Telefone: ").strip()
    empresa.endereco = input("Informe o Endereço: ").strip().title()

    limpar()

    #chamando os metodos get obj usuario
    print("DADOS DO USUARIO: \n")
    print(f"Nome do usuario: {usuario.nome}")
    print(f"CPF do usuario: {usuario.cpf}")
    print(f"Telefone do usuario: {usuario.telefone}")
    print(f"Endereço do usuario: {usuario.endereco}")
    
    #chamando os metodos get obj empresa
    print("\nDADOS DA EMPRESA:\n")
    print(f"Nome da empresa: {empresa.nome_fantasia}")
    print(f"CNPJ da empresa: {empresa.cnpj}")
    print(f"Telefone da empresa: {empresa.telefone}")
    print(f"Endereço do usuario: {empresa.endereco}")

# chama o metodo main
if __name__ == "__main__":
    main()



