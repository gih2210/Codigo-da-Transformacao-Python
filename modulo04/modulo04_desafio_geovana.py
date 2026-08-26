agenda = {}

while True:
    print("\n1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Ver contatos")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
        print("Contato adicionado!")

    elif opcao == "2":
        nome = input("Nome do contato: ")

        if nome in agenda:
            print("Telefone:", agenda[nome])
        else:
            print("Contato não encontrado!")

    elif opcao == "3":
        print("\nContatos:")
        for nome, telefone in agenda.items():
            print(nome, "-", telefone)

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")