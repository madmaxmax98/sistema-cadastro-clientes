from database import criar_tabela, inserir_cliente, listar_clientes, buscar_cliente, atualizar_cliente, deletar_cliente
from cliente import Cliente

criar_tabela()

while True:
    print("\n===== SISTEMA DE CADASTRO DE CLIENTES =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Atualizar cliente")
    print("5 - Deletar cliente")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")

        cliente = Cliente(nome, email, telefone)
        inserir_cliente(cliente)

        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":
        clientes = listar_clientes()

        print("\n===== CLIENTES CADASTRADOS =====")
        for cliente in clientes:
            print(cliente)

    elif opcao == "3":
        nome = input("Digite o nome do cliente: ")
        clientes = buscar_cliente(nome)

        print("\n===== RESULTADO DA BUSCA =====")
        for cliente in clientes:
            print(cliente)

    elif opcao == "4":
        id_cliente = int(input("Digite o ID do cliente: "))
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        telefone = input("Novo telefone: ")

        cliente = Cliente(nome, email, telefone, id_cliente)
        atualizar_cliente(cliente)

        print("Cliente atualizado com sucesso!")

    elif opcao == "5":
        id_cliente = int(input("Digite o ID do cliente que deseja deletar: "))
        deletar_cliente(id_cliente)

        print("Cliente deletado com sucesso!")

    elif opcao == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")