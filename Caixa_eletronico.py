saldo = [1000]
historico = []
entrada = "1234"
escolha = 0

senha = input("\nPara entrar no sistema, digite a senha correta: ")

while senha != entrada:
    print("\nSENHA INCORRETA!")
    senha = input("\nPara entrar no sistema, digite a senha correta: ")

if senha == entrada:
    print("\nBem vindo ao sistema!")

    print("\nOque você deseja fazer?\n")
    escolha = input("I- CONSULTAR SALDO; \nII- REALIZAR SAQUE; \nIII- REALIZAR DEPÓSITO; \nIV- CONFERIR HISTÓRICO; \nV- SAIR DO SISTEMA.\n\n").strip().lower()
    
def consultarSaldo():
    print(f"\nSeu saldo atual é: R${saldo[0]}\n")

def Saque():
    retirada = int(input("\nQual o valor do saque a ser realizado? "))
    saldo[0] -= retirada 
    historico.append(-retirada)
    print(f"\nForam sacados R${retirada}, Restam R${saldo[0]}\n")

def Deposito():
    soma = int(input("\nQual o valor do déposito a ser realizado? "))
    saldo[0] += soma
    historico.append(+soma)
    print(f"\nForam depositados R${soma}, seu saldo atual é de R${saldo[0]}\n")

def ConfHistorico():
    print(f"\nEsse é o histórico da sua conta: {historico}")

def saida():
    print("\nObrigado, tenha um ótimo dia!\n")

while escolha in ["1", "i"]:
    consultarSaldo()
    escolha = input("I- CONSULTAR SALDO; \nII- REALIZAR SAQUE; \nIII- REALIZAR DEPÓSITO; \nIV- CONFERIR HISTÓRICO \nV- SAIR DO SISTEMA.\n\n").strip().lower()
    
while escolha in ["2", "ii"]:
    Saque()
    escolha = input("I- CONSULTAR SALDO; \nII- REALIZAR SAQUE; \nIII- REALIZAR DEPÓSITO; \nIV- CONFERIR HISTÓRICO \nV- SAIR DO SISTEMA.\n\n").strip().lower()

while escolha in ["3", "iii"]:
    Deposito()
    escolha = input("I- CONSULTAR SALDO; \nII- REALIZAR SAQUE; \nIII- REALIZAR DEPÓSITO; \nIV- CONFERIR HISTÓRICO \nV- SAIR DO SISTEMA.\n\n").strip().lower()

while escolha in ["4", "iv"]:
    ConfHistorico()
    escolha = input("I- CONSULTAR SALDO; \nII- REALIZAR SAQUE; \nIII- REALIZAR DEPÓSITO; \nIV- CONFERIR HISTÓRICO \nV- SAIR DO SISTEMA.\n\n").strip().lower()

while escolha in ["5", "v"]:
    saida()
    break
