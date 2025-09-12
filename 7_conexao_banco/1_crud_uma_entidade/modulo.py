from datetime import datetime
import os
import pandas as pd
import openpyxl

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# FUNÇAO CADASTRAR NOVA PESSOA-------------
def cadastrar_pessoa(session, Pessoa):
    try:
        print("--CADASTRAR PESSOA--")
        nome = input("Informe o nome: ").strip().title()
        email = input("Informe o Email: ").strip().lower()

        # fezer pesquisa na base de dados EMAIL
        # TODO: correçao bug aula 28/08
        pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"{email}")).all()

        # verificar se o email ja existe na base de dados
        if email in [pessoa.email for pessoa in pessoas]:
            print ("Email ja cadastrado.")
        else:  
            # solicitar a data de nascimento
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
            # converter a string data_nascimento para o formato date do python
            data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            # criar uma nova instância da classe Pessoa vai fazer o insert na tabela pessoa
            nova_pessoa = Pessoa(nome=nome, email=email, data_nascimento=data_nascimento)

            session.add(nova_pessoa)  # adicionar a nova pessoa na sessão
            session.commit()  # confirmar a transação

            # msg de sucesso
            print(f"Pessoa {nome} cadastrada com sucesso!") 
    except Exception as e:
        print(f"Erro ao CADASTRAR pessoas: {e}")

# FUNÇÃO LISTAR PESSOAS CADASTRADAS-------
def listar_pessoas(session, Pessoa):
    try:
        print("--LISTAR PESSOAS--")
        pessoas = session.query(Pessoa).all() # consulta todas as pessoas na tabela .all()toda tabela

        print("\nPessoas cadastradas:\n")
        for pessoa in pessoas:
            # exibir os dados de cada pessoa
            # print(f"ID: {pessoa.id_pessoa} | Nome: {pessoa.nome} | Email: {pessoa.email} | Data de Nascimento: {pessoa.data_nascimento.strftime('%d/%m/%Y')}")
            print(f"ID: {pessoa.id_pessoa} ")
            print(f"Nome: {pessoa.nome} ")
            print(f"Email: {pessoa.email} ")
            print(f"Data de Nascimento: {pessoa.data_nascimento.strftime('%d/%m/%Y')}")
            print("-"*20)  

    except Exception as e:
        print("Erro ao LISTAR pessoas: {e}")

# FUNÇÃO PESQUISAR PESSOAS CADASTRADAS----
def pesquisar_pessoas(session, Pessoa):
    print("Filtrar pessoas por campo:")
    print("1 - ID:")
    print("2 - Nome:")
    print("3 - E-mail:")
    print("4 - Data de Nascimento:")
    print("5 - Retornar:")
    
    campo = input("Escolha o campo a ser pesquisado: ").strip()
    limpar()
    match campo:
        case "1":
            valor = input("Informe o ID que deseja buscar:").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.id_pessoa.like(f"{valor}")).all() # all() para retornar todos os valores deste campo
        case "2":
            valor = input("Informe o Nome que deseja pesquisar:").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.nome.like(f"%{valor}%")).all()
        case "3":
            valor = input("Informe o E-mail que deseja pesquisar:").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"%{valor}%")).all()

        case "4":
            valor = input("Informe o data de nascimento (dd/mm/aaaa) que deseja pesquisar:").strip()
            data_nascimento = datetime.strptime(valor, "%d/%m/%Y").date()
            pessoas = session.query(Pessoa).filter(Pessoa.data_nascimento == data_nascimento).all()
        case "5":
            return
        case _:
            print("Opção inválida. Tente novamente.")
            return
    limpar()
    print("\nResultado da pesquisa:\n")
    if pessoas:
        for pessoa in pessoas:
            print(f"ID:{pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail:{pessoa.email}")
            print(f"Data de Nascimento: {pessoa.data_nascimento.strftime('%d/%m/%Y')}")
            print("-" * 40)
    else:
        print("Nenhuma pessoa foi encontrada.")

# FUNÇAO ALTERAR DADOS DA PESSOA------
def alterar_dados(session, Pessoa):
    id_pessoa = ""
    email = ""
    novo_nome = ""
    novo_email = ""
    nova_data_nascimento = ""

    try:
        print("Escolha o campo para pesquisar a pessoa a ter os dados alterados:")
        print("1 - ID")
        print("2 - E-mail")
        print("3 - Retornar")
        opcao = input("Escolha o campo que deseja pesquisar: ").strip()
        limpar()
        match opcao:
            case "1":
                id_pessoa = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email = input("Informe o e-mail: ").strip()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "3":
                return ""
            case _:
                print("Opção inválida")
        if pessoa:
            while True:
                print("Qual campo deseja alterar:\n")
                print(f"ID {pessoa.id_pessoa}")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                print(f"3 - Data de nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
                print("4 - Finalizar")
                campo = input("Informe o campo que deseja alterar: ").strip()
                limpar()
                match campo:
                    case "1":
                        novo_nome = input("Informe o novo nome: ").strip().title()
                        print(f"Nome a ser cadastrado: {novo_nome}.")
                        continue
                    case "2":
                        novo_email = input("Informe o novo e-mail: ").strip().lower()
                        pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                        if email in [pessoa.email for pessoa in pessoas]:
                            print("E-mail já cadastrado.")
                        else:
                            print(f"E-mail a ser cadastrado: {novo_email}.")
                        continue
                    case "3":
                        nova_data_nascimento = input("Informe a nova data de nascimento (dd/mm/aaaa): ").strip()
                        print(f"Data de nascimento a ser cadastrada: {nova_data_nascimento}.")
                        continue
                    case "4":
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        novo_email = novo_email if novo_email != "" else pessoa.email
                        nova_data_nascimento = datetime.strptime(nova_data_nascimento, "%d/%m/%Y").date() if nova_data_nascimento != "" else pessoa.data_nascimento
                        break
                    case _:
                        print("Campo inexistente")
                        continue
            pessoa.nome = novo_nome
            pessoa.email = novo_email
            pessoa.data_nascimento = nova_data_nascimento

            session.commit()

            print("Pessoa cadastrada com sucesso!")
        else:
            print("Pessoa não encontrada.")
    except Exception as e:
        print(f"Não foi possível alterar. {e}.")

def excluir_pessoa(session, Pessoa):
    id_pessoa = " " 
    email = ""
    pessoa = ""

    print("--EXCLUIR PESSOA--")
    print("Escolha o campo para localizar a pessoa a ser excluída:")
    print("1 - ID:")
    print("2 - E-mail:")
    print("3 - Retornar:")
    opcao = input("Escolha a opção que deseja pesquisar: ").strip()
    limpar()
    match opcao:
        case "1":
            id_pessoa = input("Informe o ID:").strip()
            pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first() # first() retorna o 1 resultado da pesquisa
        case "2":
            email = input("Informe o e-mail a ser e:").strip().lower()
            pessoa = session.query(Pessoa).filter_by(email=email).first() # first() retorna o 1 resultado da pesquisa
        case "3":
            return ""
        case _:
            print("Opção inválida. Tente novamente.")
            return
        
    if pessoa:
        limpar
        # exibir os dados da pessoa a ser excluída
        print("Dados da pessoa a ser excluída:")
        print(f"ID: {pessoa.id_pessoa}")
        print(f"Nome: {pessoa.nome}")
        print(f"E-mail: {pessoa.email}")
        print(f"Data de Nascimento: {pessoa.data_nascimento.strftime('%d/%m/%Y')}")
        
        # solicitar confirmação
        excluir = input("Tem certeza que deseja excluir essa pessoa?  [S] - SIM - [N] - NAO): ").strip().lower()

        match excluir:
            case "s":
                session.delete(pessoa)
                session.commit()
                print("Pessoa excluída com sucesso.")
            case "n":
                print("Operação de exclusão cancelada.")
            case _:
                print("Opção inválida. Tente novamente.")
                return
    else:
        print("Pessoa não encontrada.")

# TODO: Criar a função  - que exporta para CSV ou Excel

def exportar_para_csv(engine):  
    try:
        query = "SELECT * FROM pessoa"
        df = pd.read_sql_query(query, engine)
        df.to_csv("1_crud_uma_entidade/planilhas_exportadas/pessoas.csv", index=False)
        print("ados exportados com sucesso para pessoas_exportadas.csv")
    except Exception as e:
        print(f"Erro ao exportar dados: {e}")

def exportar_para_excel(session, Pessoa):  
    try:
        pessoas = session.query(Pessoa).all()
        dados = [
            {
            "ID": pessoa.id_pessoa,
            "Nome": pessoa.nome,
            "Email": pessoa.email,
            "Data de Nascimento": pessoa.data_nascimento.strftime('%d/%m/%Y')
        } 
        for pessoa in pessoas # list comprehension - para cada pessoa na lista pessoas
        ]
        df = pd.DataFrame(dados)
        df.to_excel("1_crud_uma_entidade/planilhas_exportadas/pessoas.xlsx", index=False)
        print("Dados exportados com sucesso para pessoas_exportadas.xlsx")
    except Exception as e:
        print(f"Erro ao exportar dados: {e}")