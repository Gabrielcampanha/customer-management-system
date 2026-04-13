from crud import *

while True:
    print("\n1 - Criar cliente")
    print("2 - Listar clientes")
    print("3 - Listar clientes por intervalo de ID")
    print("4 - Atualizar cliente")
    print("5 - Deletar cliente")
    print("6 - Limpar tabela")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ").strip()
        idade_str = input("Idade: ").strip()

        if not nome or not idade_str:
            print("Os campos nome e idade não podem ser vazios")
            continue

        if not idade_str.isdigit():
            print("Idade deve ser um número!")
            continue

        idade = int(idade_str)

        create_customer(nome, idade)
        print("Cliente criado com sucesso!")

    elif op == "2":
        clientes = get_customers()
        for c in clientes:
            print(c)
    
    elif op == "3":
        id_inicio = int(input("ID inicial: "))
        id_fim = int(input("ID final: "))
        if id_inicio > id_fim:
            print("Intervalo inválido!")
        else:
            clientes = get_customers_by_range(id_inicio, id_fim)

            if clientes:
                for c in clientes:
                    print(c)
            else:
                print("Nenhum cliente encontrado nesse intervalo.")

    elif op == "4":
        id = int(input("ID: "))
        idade = int(input("Nova idade: "))
        update_customer(id, idade)

    elif op == "5":
        id = int(input("ID: "))
        delete_customer(id)

    elif op == "6":
        confirm = input("Tem certeza que deseja apagar TODOS os dados? (s/n): ")
        if confirm.lower() == 's':
            clear_table()
            print("Tabela limpa com sucesso!")
        else:
            print("Operação cancelada.")

    elif op == "0":
        break

    else:
        print("Opção inválida!")