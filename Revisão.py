Alunos = {
    "Alice": [8.0, 7.5, 9.0],
    "Bruno": [6.0, 5.5, 6.5],
    "Carla": [4.0, 3.5, 5.0],
}

def MediaNotas(notas):
    soma = 0
    for nota in notas:
        soma += nota
        return soma / len(notas)

def Situacao_media(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

while True: 
    print("\n----MENU----\n")
    print("1. Ver Boletim completo")
    print("2. Ver aluno por nome")
    print("3. Sair")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        for nome, notas in Alunos.itens():
            media = MediaNotas(notas)
            situacao = Situacao_media(media)
            print(f"\nAluno {nome}")
            print(f"Notas: {notas}")
            print(f"Média: {media:.2f} - Situação: {situacao}")
    elif opcao == "2":
        Situacao_media()
    elif opcao == "3":
        print("Desligando sistema.")
        break
    else:
        print("escolha uma opção válida") 
