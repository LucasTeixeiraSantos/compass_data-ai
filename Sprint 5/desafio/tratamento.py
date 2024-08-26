import pandas as pd

df = pd.read_csv('arquivo.csv', sep=';')

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.replace(',', '.', regex=False)

df = df.dropna()

df.to_csv('arquivo_tratado.csv', sep=';', index=False)
