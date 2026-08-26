lista = []

while True:
    print("\n1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        item = input("Digite o item: ")
        lista.append(item)

    elif opcao == "2":
        item = input("Digite o item para remover: ")
        if item in lista:
            lista.remove(item)
        else:
            print("Item não encontrado!")

    elif opcao == "3":
        print("Lista de compras:", lista)

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")