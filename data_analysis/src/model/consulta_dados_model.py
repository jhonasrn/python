from sqlalchemy.orm import sessionmaker
from model.gera_massa_dados_model import UserActivity
from model.db_config import engine  # Usando o engine do SQLAlchemy

# Criando uma sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Função para consultar todas as atividades dos usuários
def get_all_user_activities_from_db():
    try:
        # Realizando a consulta para obter todas as atividades de usuários
        activities = session.query(UserActivity).all()

        # Se houver registros, retorna os dados
        if activities:
            return activities
        else:
            print("Nenhuma atividade encontrada.")
            return []

    except Exception as e:
        print(f"Erro ao consultar atividades: {e}")
        return []

    finally:
        # Fechar a sessão após a execução
        session.close()

# Exemplo de como usar a função
if __name__ == "__main__":
    activities = get_all_user_activities_from_db()
    for activity in activities:
        print(f"ID: {activity.id}, User ID: {activity.user_id}, Tipo de Atividade: {activity.activity_type}, "
              f"Duração: {activity.duration}, Data: {activity.timestamp}")
