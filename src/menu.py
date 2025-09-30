from __future__ import annotations
from .services import UserService

def render_users(users) -> None:
    print("\nLista de Usuários:")
    for u in users:
        status = "Ativo" if u.active else "Inativo"
        print(f"{u.id}: {u.name} ({u.email}) - {status}")
    print()

def menu_loop(service: UserService) -> None:
    while True:
        print("=== Sistema de Usuários ===")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Desativar usuário")
        print("4 - Buscar usuário na API")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                name = input("Digite o nome do usuário: ")
                email = input("Digite o email: ")
                user = service.add_user(name, email)
                print(f"Usuário {user.name} adicionado com sucesso!")
                render_users(service.list_users())

            elif opcao == "2":
                render_users(service.list_users())

            elif opcao == "3":
                uid = int(input("Digite o ID do usuário para desativar: "))
                ok = service.deactivate_user(uid)
                print("Usuário desativado." if ok else "Usuário não encontrado.")

            elif opcao == "4":
                uid = int(input("Digite o ID do usuário para buscar na API: "))
                data = service.fetch_user_from_api(uid)
                if data:
                    print(f"Usuário encontrado na API: {data['name']} ({data['email']})")
                else:
                    print("Usuário não encontrado na API.")

            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")
        except Exception as e:
            print(f"Erro: {e}")
