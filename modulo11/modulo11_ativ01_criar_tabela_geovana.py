import sqlite3

# Conectando ao banco de dados (ou criando se não existir)
conexao = sqlite3.connect("sistema_vendas.db")
cursor = conexao.cursor()

# Criando a tabela Clientes
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
"""
)

conexao.commit()
conexao.close()