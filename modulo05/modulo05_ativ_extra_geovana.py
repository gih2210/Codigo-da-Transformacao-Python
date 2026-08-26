usuarios = {
    "admin": "1234",
    "aluno": "python"
}


def validar_login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    else:
        return False


usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if validar_login(usuario, senha):
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos!")