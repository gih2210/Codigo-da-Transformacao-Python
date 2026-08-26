import os
import shutil

# Pasta onde estão os arquivos importantes
pasta_origem = "arquivos"

# Pasta onde será feito o backup
pasta_backup = "backup"

# Criar as pastas caso elas não existam
if not os.path.exists(pasta_origem):
    os.mkdir(pasta_origem)

if not os.path.exists(pasta_backup):
    os.mkdir(pasta_backup)

# Copiar os arquivos
for arquivo in os.listdir(pasta_origem):

    caminho_origem = os.path.join(pasta_origem, arquivo)
    caminho_backup = os.path.join(pasta_backup, arquivo)

    # Verifica se é um arquivo
    if os.path.isfile(caminho_origem):
        shutil.copy2(caminho_origem, caminho_backup)

print("Backup realizado com sucesso!")