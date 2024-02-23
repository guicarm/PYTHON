import pandas as pd
import matplotlib as plot

# Entrada
url="https://raw.githubusercontent.com/op1154/BaseDadosImoveisRJ/main/aluguel.csv"

# Processamento
df = pd.read_csv(url)

df.head()

df = pd.read_csv(url, sep =";")

df

df['Valor'].mean()

df.groupby('Tipo')

df.groupby('Tipo').mean(numeric_oly=True)

df_preco_tipo = df.groupby('Tipo')[['Valor']].mean(numeric_only=True).sort_values('Valor')

df_preco_tipo.plot(kind='barh', figsize(14, 10), color='purple')

