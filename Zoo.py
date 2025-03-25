import pandas as pd 

dados_animais = {
    "Nome": ["Leão", "Elefante", "Tigre", "Girafa", "Zebra"],
    "Idade": [8, 15, 6, 12, 10],
    "Habitat": ["Selva", "Savana", "Selva", "Savana", "Savana"],
    "Peso": [190, 5000, 220, 800, 400]
}

Dataf = pd.DataFrame(dados_animais)
df_filtrado = Dataf[Dataf["Habitat"] == "Savana"]
df_sorted = df_filtrado.sort_values("Peso", ascending=False)
df_pesoMedio = (df_sorted["Peso"].mean())

print(f"\nLista dos animais do zoológico: \n\n{Dataf}\n")
print(f"\nLista filtrada: \n\n{df_sorted}\n")
print(f"\nPeso médio dos animais: \n\n{df_pesoMedio:.2f}kg\n")