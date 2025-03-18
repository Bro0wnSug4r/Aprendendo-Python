import random
saldo = []
historico = []
contas = {}

def gerar_numero_conta():
    return str(random.randint(1000,9999))

def Login_true():
    while True:
            Menu_2()
            escolha = input("\nEscolha uma opção: ").strip().lower()

            if escolha in ["1", "i"]:
                consultarSaldo()
            elif escolha in ["2", "ii"]:
                Saque()
            elif escolha in ["3", "iii"]:
                Deposito()
            elif escolha in ["4", "iv"]:
                ConfHistorico()
            elif escolha in ["5", "v"]:
                saida()
                break 
            else:
                print("\nOpção inválida! Tente novamente.\n")

def Menu_1():
    print()
    print("1. Registrar um novo usuário")
    print("2. Entar com um usuário já cadastrado e número da conta")
    print("3. Sair")

def Menu_2():
    print()
    print("1. Consultar saldo")
    print("2. Relizar saque")
    print("3. Realizar Depósito")
    print("4. Exibir Histórico")
    print("5. Sair")

def CriarConta():
    user = input("\nDigite o nome do novo usuário: ").strip().capitalize()
    senha = gerar_numero_conta()

    while senha in contas:
        senha = gerar_numero_conta()
    
    contas[user] = senha

    print("\nNovo usuário cadastrado!")
    print(f"\n{senha} é o número da conta, utilize para ter acesso às outras funções do sistema!")

def consultarSaldo():
    print(f"\nSeu saldo atual é: R${saldo[0]:.2f}\n")

def Saque():
    retirada = float(input("\nQual o valor do saque a ser realizado? "))
    if retirada > saldo[0]:
        print("\nSaldo insuficiente para realizar o saque.")
    else:
        saldo[0] -= retirada
        historico.append(f"Saque: -R${retirada:.2f}")
        print(f"\nForam sacados R${retirada:.2f}. Saldo restante: R${saldo[0]:.2f}\n")

def Deposito():
    soma = float(input("\nQual o valor do depósito a ser realizado? "))
    saldo[0] += soma
    historico.append(f"Depósito: +R${soma:.2f}")
    print(f"\nForam depositados R${soma:.2f}. Saldo atual: R${saldo[0]:.2f}\n")

def ConfHistorico():
    print("\nHistórico da conta:")
    for transação in historico:
        print(transação)
    print()

def saida():
    print("\nObrigado, tenha um ótimo dia!\n")

def Entrar():
    user = input("Quem está acessando o sistema? ")
    senha = input("Digite o número da conta: ")
    if senha in contas:
        print(f"Login bem sucedido! Bem-vindo, {user}")
        Login_true()        
    else:
        print("\nUsuário não cadastrado!")

print("\nBem-vindo ao sistema!")

while True:   
    Menu_1()
    escolha = input("\nEscolha uma opção: ").strip().lower()

    if escolha in ["1", "i"]:
        CriarConta()
    elif escolha in ["2", "ii"]:
        Entrar()
    elif escolha in ["3", "iii"]:
        saida()
        break
    else:
        print("\nOpção inválida! Tente novamente.\n")