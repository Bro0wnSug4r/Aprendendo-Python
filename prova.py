import pandas as pd

df = pd.DataFrame({
"Filme": ["Terror", "Comédia", "Aventura", "Ação", "Drama"],
"Preço do Ingresso (R$)": [25, 20, 18, 30, 22],
"Ingressos Vendidos": [120, 80, 150, 95, 110]
})

df["Receita (R$)"] = df["Preço do Ingresso (R$)"] * df["Ingressos Vendidos"]

def ExibirDF():
    print(f"\n{df}\n")

def Maior_Menor():
    Pior = df.loc[df["Ingressos Vendidos"].idxmin()]
    Melhor = df.loc[df["Ingressos Vendidos"].idxmax()]
    print(f"\nFilme com o maior público: {Melhor['Filme']} - {Melhor['Ingressos Vendidos']} Ingressos vendidos.")
    print(f"\nFilme com o menor público: {Pior['Filme']} - {Pior['Ingressos Vendidos']} Ingressos vendidos.")

def Receita():
    soma = 0
    for receita in df["Receita (R$)"]:
        soma += receita
    print(f"\nReceita total do cinema: R${soma}")

def saida():
    print("\nSistema Encerrado.\n")

while True:
    print("\nO que você deseja fazer?\n")
    escolha = input("1- EXIBIR TODOS OS DADOS; \n2- EXIBIR MAIOR E MENOR PÚBLICO; \n3- EXIBIR RECEITA TOTAL; \n4- ENCERRAR PROGRAMA.\n\n").strip().lower()

    if escolha in ["1", "i"]:
        ExibirDF()
    elif escolha in ["2", "ii"]:
        Maior_Menor()
    elif escolha in ["3", "iii"]:
        Receita()
    elif escolha in ["4", "iv"]:
        saida()
        break 
    else:
        print("\nOpção inválida! Tente novamente.\n")