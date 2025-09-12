# CRUD - operações sistema que interage com um banco de dados: 
# Create (Criar), Read (Ler), Update (Atualizar) e Delete (Apagar).
# SQLAlchemy - biblioteca Python para interagir com bancos de dados relacionais.
# IMPORTAR A BIBLIOTECA SQLALCHEMY
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import entidade as ent
import modulo as md
     
def main():
    engine = create_engine("sqlite:///1_crud_uma_entidade/database/db_crud.db")
    # criar a base declarativa
    Base = declarative_base()
 
    # criar a tabela pessoa
    Pessoa = ent.criar_tb_pessoa(engine, Base)
    
    # instaciar uma sessao
    Session = sessionmaker(bind=engine)
    session = Session()

    md.limpar()
    while True:
        # exibir o menu
        print(f"{'-'*20}===CRUD==={'-'*20}")
        print("[ 1 ] - Cadastrar pessoa")
        print("[ 2 ] - Listar pessoas")
        print("[ 3 ] - Pesquisar pessoas")
        print("[ 4 ] - Alterar dados da pessoa")
        print("[ 5 ] - Excluir pessoa") 
        print ("[ 6 ] - Exportar dados para CSV") 
        print ("[ 7 ] - Exportar dados para Excel") 
        print("[ 8] - Sair do programa")
        
        # opação do menu
        opcao = input("Escolha uma opção: ").strip()
        md.limpar()
        match opcao:
            case "1":
                # chamar a função para cadastrar uma nova pessoa
                md.cadastrar_pessoa(session, Pessoa)
                continue  # volta para o início do loop
            case "2":
                md.listar_pessoas(session, Pessoa)
                continue  # volta para o início do loop
            case "3":
                md.pesquisar_pessoas(session, Pessoa)
                continue # volta para o início do loop
            case "4":
                md.alterar_dados(session, Pessoa)
                continue  # volta para o início do loop
            case "5":
                md.excluir_pessoa(session, Pessoa)
                continue  # volta para o início do loop
            case "6":
                md.exportar_para_csv(engine)
                continue  # volta para o início do loop
            case "7":
                md.exportar_para_excel(session, Pessoa)
            case "8":
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue  # volta para o início do loop

    #encerra a sessão
    session.close()

if __name__ == "__main__":
    main()