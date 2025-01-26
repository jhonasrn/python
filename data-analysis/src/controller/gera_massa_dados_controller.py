# src/controller/consulta_dados_controller.py
from model.gera_massa_dados_model import UserActivity
from model.db_config import engine
from sqlalchemy.orm import sessionmaker

# Configurando a sessão do banco de dados
Session = sessionmaker(bind=engine)

def generate_and_save_data():
    try:
        # Criar uma sessão
        session = Session()

        # Consultar todas as atividades de usuário
        user_activities = session.query(UserActivity).all()

        # Exibir as atividades
        for activity in user_activities:
            print(f"ID: {activity.id}, User ID: {activity.user_id}, "
                  f"Activity: {activity.activity_type}, Duration: {activity.duration}, "
                  f"Timestamp: {activity.timestamp}")

    except Exception as e:
        print(f"Erro ao consultar dados: {e}")
    finally:
        session.close()
