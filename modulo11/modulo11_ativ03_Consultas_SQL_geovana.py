import sqlite3

conexao = sqlite3.connect("sistema_vendas.db")
cursor = conexao.cursor()

# Filtrando clientes com nome começando com "A"
cursor.execute("SELECT * FROM Clientes WHERE nome LIKE 'A%'")
print("--- Clientes com nome começando em 'A' ---")
for linha in cursor.fetchall():
  print(linha)

conexao.close()