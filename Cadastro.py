usuarios = []

def exibir_menu():
    print()
    print("1. Registrar um novo usuário")
    print("2. Fazer login")
    print("3. Exibir ususários cadastrados")
    print("4. Sair")

def novo_usuario():
    user = input("\nDigite o nome do novo usuário: ")
    if user in usuarios:
        print("\nUsuário já utilizado!")
    else:
        senha = input("\nDigite uma senha: ")
        usuarios[user] = senha
        usuarios.append(f"{user}")
        print("\nNovo usuário cadastrado!")

def exibir():
    print("\nUsuários cadastrados:")
    for lista in usuarios:
        print(lista)
    print()

def login():
    entrada = input("\nDigite o login: ")
    senha = input("Digite sua senha: ")
    if entrada in usuarios and usuarios[entrada] == senha:
        print(f"Login bem sucessido! Bem-vindo, {entrada}")
    else:
        print("\nUsuário não cadastrado!")

def login_2():
    print("\nPara ter acesso a lista de usuários, você precisa estar logado!")
    login()

def saida():
    print("\nObrigado, tenha um ótimo dia!\n")

while True:
    exibir_menu()
    escolha = input("\nEscolha uma opção: ").strip().lower()

    if escolha in ["1", "i"]:
        novo_usuario()
    elif escolha in ["2", "ii"]:
        login()
    elif escolha in ["3", "iii"]:
        login_2()
    elif escolha in ["4", "iv"]:
        saida()
        break 
    else:
        print("\nOpção inválida! Tente novamente.\n")