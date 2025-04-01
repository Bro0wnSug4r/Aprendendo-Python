import pandas as pd

dados = {
    "Título do livro": ["Drácula", "1984", "Jogador N1", "Dom Casmurro", "Morellonomicon"],
    "Custo por unidade": [30, 20, 50, 25, 70],
    "Preço": [50, 40, 120, 60, 99],
    "Quantidade vendida": [120, 90, 150, 60, 110]
}

df = pd.DataFrame(dados)
df["Faturamento total"] = df["Preço"] * df["Quantidade vendida"]
df["Custo total"] = df["Custo por unidade"] * df["Quantidade vendida"]
df["Lucro bruto"] = df["Faturamento total"] - df["Custo total"]

preco_medio = df["Preço"].mean()
lucro_medio = df["Lucro bruto"].mean()
lucro_total = df["Lucro bruto"].sum()

print(f"\n{df}\n")
print(f"Preço médio: {preco_medio}\n")
print(f"Lucro médio: {lucro_medio}\n")
print(f"Lucro total: {lucro_total}\n")