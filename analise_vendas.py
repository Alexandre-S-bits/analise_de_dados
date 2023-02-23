# -*- coding: utf-8 -*-
"""analise_vendas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s_smRE_cCV9zMSv5XvHidTKb-QPbK5G6
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# Upload de arquivos
from google.colab import files
arq = files.upload()

# Criando dataframe
df = pd.read_excel('AdventureWorks.xlsx')

# Receita Total
df['Valor Venda'].sum()

# Custo Total
df['Custo'] = df['Custo Unitário'].mul(df['Quantidade'])
df.head()

# Lucro Total
df['Lucro'] = df['Valor Venda'] - df['Custo']

# Tempo de entrega
df['Tempo de Entrega'] = df['Data Envio'] - df['Data Venda']
df['Tempo de Entrega'].dtype

# convertendo em valor númerio
df['Tempo de Entrega'] = (df['Data Envio'] - df['Data Venda']).dt.days
df['Tempo de Entrega'].dtype

df.groupby('Marca')['Tempo de Entrega'].mean()

# Lucro por ano e marca
df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum()

pd.options.display.float_format = '{:20,.2f}'.format

# Resetar o Index
lucro_ano = df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum().reset_index()
lucro_ano

# Quantidade de produtos vendidos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)

# Grafico total de produtos vendidos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).plot.barh(title='Total Produtos Vendidos')
plt.ylabel('Produto')
plt.xlabel('Total');