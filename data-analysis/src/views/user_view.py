def display_users(users):
    print("\n=== Lista de Usuários ===")
    for user in users:
        print(f"ID: {user[0]}, Nome: {user[1]}, Email: {user[2]}, Idade: {user[3]}, Data de Registro: {user[4]}")
    print("=========================\n")
