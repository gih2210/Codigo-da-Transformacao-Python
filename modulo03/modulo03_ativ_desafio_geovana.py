while True:
    print("\n--- MENU ---")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado:", num1 + num2)

    elif opcao == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado:", num1 - num2)

    elif opcao == "3":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")