-- Descubra o produto mais vendido por região.

use db_sales;

-- criando uma view das vendas por região para o ano atual
create view vw_vendas_regiao (nome_regiao, cod_produto, desc_produto, quantidade) as
select 
d.nome_regiao,
a.cod_produto,
b.desc_produto,
sum(a.quantidade) as quantidade
from vendas a
inner join produtos b on a.cod_produto = b.cod_produto
inner join clientes c on a.cod_cliente = c.cod_cliente
inner join regiao d on c.cod_regiao = d.cod_regiao
Where year(data) = year(curdate())
group by d.nome_regiao, a.cod_produto, b.desc_produto
order by d.nome_regiao, quantidade DESC;

-- criando ranqueamento e selecionando apenas o ranking 1 de cada região
select * from (
	select  
	nome_regiao,
	cod_produto,
	desc_produto,
	quantidade,
	ROW_NUMBER() OVER (PARTITION BY nome_regiao ORDER BY quantidade DESC) AS ranking
	from vw_vendas_regiao) x
where x.ranking = 1
