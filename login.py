import json
import os


usuarios = "usuarios.json"

def carregar_usuarios():
    if not os.path.exists(usuarios):
        return {}
    with open(usuarios, "r") as f:
        return json.load(f)
    
def salvar_usuarios(usuarios):
    with open(usuarios, "w") as f:
        json.dump(usuarios, f, indent=4)

def cadastrar_usuario(email, senha, admin=False):
    usuarios = carregar_usuarios()
    if email in usuarios:
        return False
    usuarios[email] = {"senha": senha, "admin": admin}
    salvar_usuarios(usuarios)
    return True

def verificar_usuario(email, senha):
    usuarios = carregar_usuarios()
    if email not in usuarios:
        return False
    if usuarios[email]["senha"] != senha:
        return False
    return True


def main():
    usuarios = carregar_usuarios()
    while True:
        print("você gostaria de fazer login ou cadastrar um novo usuario?")
        opcao = input("1 - login, 2 - cadastro, 3 - sair")
        if opcao == "1":
            email = input("Digite o seu email: ")
            senha = input("Digite a sua senha: ")
            if verificar_usuario(email, senha):
                print("Bem vindo!")
                break
            else:
                print("Email ou senha inválidos. Tente novamente.")
        if opcao == "2":
            email = input("Digite o seu email: ")
            senha = input("Digite a sua senha: ")
            cadastrar_usuario(email, senha)
            print("cadastro feito com sucesso")
            break
        if opcao == "3":
            break

if __name__ == "__main__":
    main()