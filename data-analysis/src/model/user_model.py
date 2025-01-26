from models.db_config import get_connection

def create_table():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL UNIQUE,
                    age INT NOT NULL,
                    registration_date DATE NOT NULL
                );
            """)
            connection.commit()
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
        finally:
            cursor.close()
            connection.close()

def insert_user(user):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO users (name, email, age, registration_date)
                VALUES (%s, %s, %s, %s);
            """, user)
            connection.commit()
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            connection.close()

def get_all_users():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users;")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar usuários: {e}")
        finally:
            cursor.close()
            connection.close()
