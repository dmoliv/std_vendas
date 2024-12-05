# %%

import mysql.connector
import pandas as pd

# Conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    host="192.168.0.199",
    user="daniel",
    password="admin...",
    database="db_sales"
)

# %%

#  Descubra o produto mais vendido por região.
# criando ranqueamento e selecionando apenas o ranking 1 de cada região
# obs: criar a view vw_vendas_regiao contida em \scripts\sql

query = """
    select * from (
	select  
	nome_regiao,
	cod_produto,
	desc_produto,
	quantidade,
	ROW_NUMBER() OVER (PARTITION BY nome_regiao ORDER BY quantidade DESC) AS ranking
	from vw_vendas_regiao) x
    where x.ranking = 1;
    """

df = pd.read_sql_query(query, conn)
df


# %%

#  Descubra o produto mais vendido por cliente.
query = """
    select a.cod_cliente, b.nom_cliente, sum(a.quantidade*c.preco) as val_tot 
    from vendas a
    inner join clientes b on a.cod_cliente = b.cod_cliente
    inner join produtos c on a.cod_produto = c.cod_produto
    where data >= month(curdate())-12
    group by 1,2
    order by 3 DESC LIMIT 5
    """

df = pd.read_sql_query(query, conn)
df


# %%

#  Determine o mês de maior faturamento e identifique os fatores

# verificando mês com maior quantidade vendida
query1 = """
select month(data) as mes,  sum(a.quantidade) as quantidade
from vendas a
inner join produtos b on a.cod_produto = b.cod_produto
Where year(a.data) = year(curdate())
group by 1
order by 2 DESC LIMIT 2;
    """

df1 = pd.read_sql_query(query1, conn)

# verificando mês com maior faturamento, indicando que foram vendidos menores quantidades porém
# produtos com maior valor agregado
query2 = """
select month(data) as mes,  concat('R$ ',sum(a.quantidade*b.preco)) as valor
from vendas a
inner join produtos b on a.cod_produto = b.cod_produto
Where year(a.data) = year(curdate())
group by 1
order by 2 DESC LIMIT 2;
    """

df2 = pd.read_sql_query(query2, conn)

df3 = pd.merge(df1, df2, how = 'inner', on = 'mes')
df3
# podemos ver que o mês com maior faturamento foi o 2, apenas do 7 ser maior em volume