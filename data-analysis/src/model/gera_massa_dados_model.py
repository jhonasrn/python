from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model.db_config import engine  # Usando o engine do SQLAlchemy

# Declarando a base
Base = declarative_base()

# Definindo a tabela UserActivity
class UserActivity(Base):
    __tablename__ = 'user_activities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    activity_type = Column(String(50), nullable=False)
    duration = Column(DECIMAL(5, 2), nullable=False)  # Usando DECIMAL para o tipo
    timestamp = Column(DateTime, nullable=False)

# Configurando a sessão do banco de dados
Session = sessionmaker(bind=engine)

def save_to_database(data):
    try:
        # Criar todas as tabelas no banco de dados (caso ainda não existam)
        Base.metadata.create_all(engine)

        # Criar uma sessão
        session = Session()

        # Inserir os dados na tabela
        user_activities = [UserActivity(**record) for record in data]
        session.add_all(user_activities)
        session.commit()

        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
    finally:
        session.close()
