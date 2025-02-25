cadastro = []

while True:
    pessoa = {
        "nome" : input("\nDigite seu nome: "),   
        "idade" : int(input("\nDigite sua idade: ")), 
        "cpf" : input("\nDigite seu cpf: "),
        "email" : input("\nDigite seu email: ")
    }

    cadastro.append(pessoa)

    continuar = input("\nDeseja cadastrar oura pessoa? (s/n)")
    if continuar != "s":
        break

print("\nLista de pessoas cadastradas: ")
for pessoa in cadastro:
    print(pessoa)