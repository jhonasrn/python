# db_config.py
from sqlalchemy import create_engine

# Configuração de conexão com o banco de dados PostgreSQL
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/data-analytics"

# Criar engine de conexão
engine = create_engine(DATABASE_URL, echo=True)

# Função para obter a conexão
def get_connection():
    return engine.connect()
