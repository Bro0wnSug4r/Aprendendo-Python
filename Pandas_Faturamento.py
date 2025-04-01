import pandas as pd
import random

dados = {
    "Nome": ["Processador", "Placa-mãe", "Placa de vídeo", "Memória RAM", "Gabinete"],
    "Preço": [1000, 600, 1500, 250, 200],
    "Quantidade vendida": [10, 7, 5, 8, 4],
    "Custo": [600, 200, 1000, 150, 100]
}

Df = pd.DataFrame(dados)
Df["Faturamento total"] = Df["Preço"] * Df["Quantidade vendida"]
Df["Desconto (%)"] = [random.randint(5,15) for _ in range(len(Df))]
Df["Faturamento com desconto"] = Df["Faturamento total"] * (1 - Df["Desconto (%)"]/100)
Df["Custo total"] = Df["Custo"] * Df["Quantidade vendida"]
Df["Lucro bruto"] = Df["Faturamento total"] - Df["Custo total"] 

preco_medio = Df["Preço"].mean()
lucro_medio = Df["Lucro bruto"].mean()

print(f"\n{Df}\n")
print(f"{preco_medio}")
print(f"{lucro_medio}")