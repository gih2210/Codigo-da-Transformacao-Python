import sqlite3


def gerenciar_crud():
  conexao = sqlite3.connect("sistema_vendas.db")
  cursor = conexao.cursor()

  # Inserir registros
  cursor.execute(
      "INSERT INTO Clientes (nome, email) VALUES (?, ?)",
      ("Ana Souza", "ana@email.com"),
  )
  cursor.execute(
      "INSERT INTO Clientes (nome, email) VALUES (?, ?)",
      ("Carlos Lima", "carlos@email.com"),
  )
  conexao.commit()

  # Consultar registros
  print("--- Lista Inicial de Clientes ---")
  cursor.execute("SELECT * FROM Clientes")
  for linha in cursor.fetchall():
    print(linha)

  # Atualizar registro
  cursor.execute(
      "UPDATE Clientes SET email = ? WHERE nome = ?",
      ("ana.nova@email.com", "Ana Souza"),
  )
  conexao.commit()

  # Deletar registro
  cursor.execute("DELETE FROM Clientes WHERE nome = ?", ("Carlos Lima",))
  conexao.commit()

  conexao.close()


gerenciar_crud()