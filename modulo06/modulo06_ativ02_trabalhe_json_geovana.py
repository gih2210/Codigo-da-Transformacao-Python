import json

# 2. Criar um dicionário de clientes

clientes = {
    "cliente1": {
        "nome": "Geovana",
        "idade": 16,
        "email": "geovana@email.com"
    },
    "cliente2": {
        "nome": "João",
        "idade": 17,
        "email": "joao@email.com"
    },
    "cliente3": {
        "nome": "Maria",
        "idade": 18,
        "email": "maria@email.com"
    }
}

# --- SALVAR JSON ---
with open("clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

print("Clientes salvos com sucesso!")

# --- CARREGAR JSON ---
with open("clientes.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print("\nClientes cadastrados:")

for cliente, informacoes in dados.items():
    print(f"\n{cliente}")
    print(f"Nome: {informacoes['nome']}")
    print(f"Idade: {informacoes['idade']}")
    print(f"E-mail: {informacoes['email']}")