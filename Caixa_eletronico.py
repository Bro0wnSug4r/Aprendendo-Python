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

    print("\n Oque você deseja fazer?\n")
    escolha = input("I- CONSULTAR SALDO; \nII- REALIZAR SAQUE; \nIII- REALIZAR DEPÓSITO; \nIV- SAIR DO SISTEMA.\n\n").strip().lower()

    if escolha in ["1", "i"]:
        print(f"\nSeu saldo atual é: R${saldo}\n")

    if escolha in ["2", "ii"]:
        valor = int(input("Digite o valor a ser adicionado: "))
        

    if escolha in ["4", "iv"]:
       print("\nObrigado, tenha um ótimo dia!\n")