def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar nova tarefa")
    print("2. Listar todas as tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

def adicionar_tarefa(tarefas, nova_tarefa):
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa}")

def remover_tarefa(tarefas, indice):
    try:
        indice = int(indice)
        if 1 <= indice <= len(tarefas):
            tarefa_removida = tarefas.pop(indice - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Índice inválido. Por favor, insira um índice válido.")
    except ValueError:
        print("Erro: Insira um índice válido.")

def main():
    tarefas = []

    while True:
        mostrar_menu()

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            nova_tarefa = input("Digite o nome da nova tarefa: ")
            adicionar_tarefa(tarefas, nova_tarefa)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            indice_tarefa = input("Digite o índice da tarefa a ser removida: ")
            remover_tarefa(tarefas, indice_tarefa)
        elif escolha == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
