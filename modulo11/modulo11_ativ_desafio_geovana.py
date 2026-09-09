import sqlite3


def sistema_tarefas():
  conexao = sqlite3.connect("tarefas.db")
  cursor = conexao.cursor()

  cursor.execute(
      """
        CREATE TABLE IF NOT EXISTS Tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL
        )
    """
  )
  conexao.commit()

  while True:
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Excluir Tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      desc = input("Digite a descrição da tarefa: ")
      cursor.execute("INSERT INTO Tarefas (descricao) VALUES (?)", (desc,))
      conexao.commit()
      print("Tarefa adicionada!")

    elif opcao == "2":
      cursor.execute("SELECT * FROM Tarefas")
      print("\nLista de Tarefas:")
      for t in cursor.fetchall():
        print(f"ID: {t[0]} - {t[1]}")

    elif opcao == "3":
      id_exc = input("Digite o ID da tarefa para excluir: ")
      cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id_exc,))
      conexao.commit()
      print("Tarefa excluída!")

    elif opcao == "4":
      break

  conexao.close()


# sistema_tarefas()