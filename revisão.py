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

def Situacao_media():
