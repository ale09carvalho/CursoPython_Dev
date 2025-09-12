from sqlalchemy import Column, Integer, String, Date


def criar_tb_pessoa(engine, Base):
    # Criar o engine do banco de dados SQLite
    try:
    

        # Definir a classe Pessoa que representa a tabela pessoas no banco de dados
        class Pessoa(Base):
            __tablename__ = "pessoa"

            # definir as colunas da tabela
            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            email = Column(String, nullable=False, unique=True)
            data_nascimento = Column(Date, nullable=False)

        # Criar a tabela no banco de dados
        Base.metadata.create_all(engine)

        return Pessoa
    except Exception as e:
        print("Erro ao criar o engine do banco de dados:. {e}")