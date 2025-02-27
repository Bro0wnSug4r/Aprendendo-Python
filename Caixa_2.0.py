saldo = [1000]
historico = []
entrada = "1234"

def consultarSaldo():
    print(f"\nSeu saldo atual é: R${saldo[0]}\n")

def Saque():
    retirada = int(input("\nQual o valor do saque a ser realizado? "))
    if retirada > saldo[0]:
        print("\nSaldo insuficiente para realizar o saque.")
    else:
        saldo[0] -= retirada
        historico.append(f"Saque: -R${retirada}")
        print(f"\nForam sacados R${retirada}. Saldo restante: R${saldo[0]}\n")

def Deposito():
    soma = int(input("\nQual o valor do depósito a ser realizado? "))
    saldo[0] += soma
    historico.append(f"Depósito: +R${soma}")
    print(f"\nForam depositados R${soma}. Saldo atual: R${saldo[0]}\n")

def ConfHistorico():
    print("\nHistórico da conta:")
    for operacao in historico:
        print(operacao)
    print()

def saida():
    print("\nObrigado, tenha um ótimo dia!\n")

senha = input("\nPara entrar no sistema, digite a senha correta: ")

while senha != entrada:
    print("\nSENHA INCORRETA!")
    senha = input("\nPara entrar no sistema, digite a senha correta: ")

print("\nBem-vindo ao sistema!")

while True:
    print("\nO que você deseja fazer?\n")
    escolha = input("1- CONSULTAR SALDO; \n2- REALIZAR SAQUE; \n3- REALIZAR DEPÓSITO; \n4- CONFERIR HISTÓRICO; \n5- SAIR DO SISTEMA.\n\n").strip().lower()

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

#Versão corrigoda pela Deepseek do meu código de caixa eletrônico, apenas para estudo.