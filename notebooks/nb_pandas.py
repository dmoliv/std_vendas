# %%
from pymongo import MongoClient
import mysql.connector

# Conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    host="192.168.0.199",
    user="daniel",
    password="admin...",
    database="db_sales"
)

# Conexão Mongo DB
client = MongoClient('192.168.0.199:27017')
db = client['petshop']
colecao = db['feedback']

# %%
import pandas as pd

# Carregando csv das metas
df_metas = pd.read_csv('../data/csv/metas_produtos.csv', sep=',')
df_metas

# %%
# Verificando se há algum dado faltante no df de metas
df_metas.isna().any()

# %%
# carregando o df de vendas
query = 'select * from vendas'

df_vendas = pd.read_sql_query(query, conn)
df_vendas


# %% 
# META ANUAL
# Agrupando os dataframes por produtos
df_vendas = df_vendas.groupby(['cod_produto'])['quantidade'].sum().reset_index()
df_metas = df_metas.groupby(['CodigoProduto'])['MetaQuantidade'].sum().reset_index()

# %%

# Juntando os dataframes (Merge)
df_metasvendas = df_metas.merge(df_vendas, 
                   how='left', #left vou manter tudo o que conheço do df_metas
                   left_on='CodigoProduto', #chave id do df_metras
                   right_on='cod_produto')  #chave id do df_vendas
df_metasvendas

# %%
# Calculando o desvio entre metas e vendas realizadas
df_metasvendas['Desvio'] = df_metasvendas['quantidade'] - df_metasvendas['MetaQuantidade']
print(df_metasvendas)

# %%
# Verificando os produtos que ainda não bateram a meta
condicao = (df_metasvendas['quantidade'] <= df_metasvendas['MetaQuantidade'])
# ordernando pelos 5 produtos com as maiores metas
df_metasvendas = df_metasvendas[condicao].sort_values(by='MetaQuantidade', ascending=False).head(5)

# %%
# gerando grafico de meta x quantidade vendida
import matplotlib.pyplot as plt
import numpy as np

# Configurar as posições e largura das barras
x = np.arange(len(df_metasvendas['cod_produto']))  # Posições no eixo X
largura = 0.4  # Largura das barras

# Criar a figura
fig, ax = plt.subplots(figsize=(12, 6))

# Barras para MetaQuantidade
ax.bar(x - largura/2, df_metasvendas['MetaQuantidade'], largura, label='Meta', color='blue')

# Barras para quantidade
ax.bar(x + largura/2, df_metasvendas['quantidade'], largura, label='Vendas', color='orange')

# Personalizar o gráfico
ax.set_xlabel('Produtos')
ax.set_ylabel('Quantidade')
ax.set_title('Comparação entre Meta e Vendas Realizadas')
ax.set_xticks(x)
ax.set_xticklabels(df_metasvendas['cod_produto'])
ax.legend()

# Ajustar layout e exibir o gráfico
plt.tight_layout()
plt.savefig('../output/meta_x_vendas', format='png', dpi=300)  # Salva o gráfico em alta resolução
plt.show()