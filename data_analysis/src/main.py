from controllers.user_controller import add_user, list_users
from views.user_view import display_users

def main():
    while True:
        print("\n1. Adicionar Usuário")
        print("2. Listar Usuários")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Nome: ")
            email = input("Email: ")
            age = int(input("Idade: "))
            registration_date = input("Data de Registro (YYYY-MM-DD): ")
            add_user(name, email, age, registration_date)
        elif choice == "2":
            users = list_users()
            display_users(users)
        elif choice == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
