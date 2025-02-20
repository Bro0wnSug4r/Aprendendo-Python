print("\nAcesso permitido apenas para maiores de idade ou menores com permissão parental!")
idade = int(input("\nDigite sua idade: "))

if idade >= 18:
    print("\nAcesso liberado!\n")
else:
    permissao = input("\nVocê tem a permissão dos seus pais? (sim/não): ").strip().lower()
    
    if permissao in ["sim", "s", "yes", "y"]:
        print("\nAcesso liberado!\n")
    elif permissao in ["não", "nao", "no", "n"]:
        print("\nAcesso negado!\n")
    else:
        print('\nResposta inválida! Por favor, responda com "sim" ou "não".\n')