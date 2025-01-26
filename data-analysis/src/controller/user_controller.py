from models.user_model import create_table, insert_user, get_all_users

def add_user(name, email, age, registration_date):
    user = (name, email, age, registration_date)
    insert_user(user)

def list_users():
    return get_all_users()
