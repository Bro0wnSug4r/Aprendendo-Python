print("\nAcesso permitido apenas para maiores de idade ou menores com permissão parental!")
idade = int(input("\nDigite sua idade: "))

if (idade >= 18):
    print ("\nacesso liberado!\n")

elif (idade < 18 ):
    permissao = input("\nVocê tem a permissão dos seus pais? ")
    if (permissao == "sim") or (permissao == "s") or (permissao == "yes") or (permissao == "y"):
        print ("\nacesso liberado!\n")

    elif (permissao == "não") or (permissao == "no") or(permissao == "n") or (permissao == "nao"):
        print ("\nacesso negado!\n")

    else:
        print ('\nApenas válido "sim" ou "não" como resposta!(sim,não/yes,no/s,n/y,n)\n')
               