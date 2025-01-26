import argparse
from controller.gera_massa_dados_controller import generate_and_save_data
from controller.consulta_dados_controller import get_and_display_user_activities

# Função para definir os argumentos e executar o script com base na escolha
def main():
    # Definir os parâmetros de linha de comando
    parser = argparse.ArgumentParser(description="Gerar ou consultar dados no banco de dados.")
    parser.add_argument(
        '--action', 
        choices=['gera', 'consulta'], 
        required=True, 
        help="Ação a ser executada: 'gera' para gerar dados ou 'consulta' para consultar dados"
    )

    # Obter o parâmetro passado
    args = parser.parse_args()

    # Realizar a ação com base no parâmetro
    if args.action == 'gera':
        print("Gerando e salvando dados...")
        generate_and_save_data()  # Chama a função que gera e salva os dados
    elif args.action == 'consulta':
        print("Consultando dados...")
        get_and_display_user_activities()  # Chama a função que consulta e exibe os dados

# Execução do script
if __name__ == "__main__":
    main()
