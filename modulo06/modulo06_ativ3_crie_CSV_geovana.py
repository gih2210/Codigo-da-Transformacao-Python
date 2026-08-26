import csv

nome_arquivo = "notas.csv"

# --- ADICIONAR ALUNOS ---
alunos = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nAluno {i + 1}")

    nome = input("Nome: ")
    nota = float(input("Nota: "))

    alunos.append([nome, nota])

# --- SALVAR NO CSV ---
with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["Nome", "Nota"])

    for aluno in alunos:
        escritor.writerow(aluno)

print("\nNotas salvas com sucesso!")

# --- LER E EXIBIR O CSV ---
print("\n--- NOTAS DOS ALUNOS ---")

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for aluno in leitor:
        print(f"Nome: {aluno['Nome']} | Nota: {aluno['Nota']}")