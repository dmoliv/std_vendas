-- Determine o mês de maior faturamento e identifique os fatores

use db_sales;

-- verificando mês com maior quantidade vendida
select month(data) as mes,  sum(a.quantidade) as quantidade
from vendas a
inner join produtos b on a.cod_produto = b.cod_produto
Where year(a.data) = year(curdate())
group by 1
order by 2 DESC LIMIT 2;

-- verificando mês com maior faturamento, indicando que foram vendidos menores quantidades porém
-- produtos com maior valor agregado
select month(data) as mes,  concat('R$ ',sum(a.quantidade*b.preco)) as valor
from vendas a
inner join produtos b on a.cod_produto = b.cod_produto
Where year(a.data) = year(curdate())
group by 1
order by 2 DESC LIMIT 2;
