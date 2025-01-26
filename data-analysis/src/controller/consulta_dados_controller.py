# src/controller/gera_massa_dados_controller.py
from model.gera_massa_dados_model import save_to_database
from faker import Faker
import random

def get_and_display_user_activities ():
    fake = Faker()

    # Gerando dados fictícios para a massa
    data = []
    for _ in range(100):  # Gerar 100 entradas
        activity = {
            'user_id': random.randint(1, 10),  # Gerando um ID de usuário aleatório
            'activity_type': fake.word(),  # Gerando um tipo de atividade aleatório
            'duration': round(random.uniform(1, 120), 2),  # Duração aleatória entre 1 e 120 minutos
            'timestamp': fake.date_time_this_year(),  # Gerando um timestamp aleatório para este ano
        }
        data.append(activity)

    print(f"Gerando os seguintes dados: {data[:5]}")  # Exibe os primeiros 5 dados gerados para conferência

    # Chama a função para salvar os dados no banco
    save_to_database(data)
