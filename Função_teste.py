nomes = []
exibirNomes = "s"

while exibirNomes == "s":
    nome = input("\nDigite seu nome: ")
    nomes.append(nome)
    exibirNomes = input("\nDeseja continuar (s/n)? ")


print("\nNomes digitados: ")
for nome in nomes:
    print(nome)