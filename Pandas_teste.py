import pandas as pd

dados = {
    "ID": range(1, 11),
    "Nome": ["Alice", "Bruno", "Carlos", "Diana", "Eduardo", "Anna", "Victor", "Lucas", "Gabriela", "Bernardo"],
    "Desempenho": [9.8, 7, 0, 6.5, 5, 8.5, 8, 8, 7.5, 9.9],
    "Setor": ["TI", "RH", "Financeiro", "Marketing", "Adminitrativo"]*2,
    "Salário": [5000, 4500, 6000, 5200, 4800]*2
}

Df = pd.DataFrame(dados)
Df_ordem = Df.sort_values("Desempenho", ascending=False)
Df_media = (Df["Desempenho"].mean())
Df_Pior = (Df["Desempenho"].min())
Df_Melhor = (Df["Desempenho"].max())
Df_ordem["Bônus (%)"] = Df_ordem["Desempenho"]*5
Df_ordem["Salário com bônus"] = Df_ordem["Salário"] * (1 + Df_ordem["Bônus (%)"]/100)
 
print(f"\nLista de funcionários da empresa: \n\n{Df_ordem}\n")
print(f"Média de desempenho dos funconários: \n{Df_media:.2f}\n")
print(f"Melhor desempenho: \n{Df_Melhor}\n")
print(f"Pior desempenho: \n{Df_Pior}\n")