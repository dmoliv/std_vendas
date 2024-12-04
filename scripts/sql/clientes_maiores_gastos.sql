-- Encontre clientes que mais gastaram nos últimos 12 meses

use db_sales;

-- realizando a Soma total e limitando os 5 primeiros resultados
select a.cod_cliente, b.nom_cliente, sum(a.quantidade*c.preco) as val_tot 
from vendas a
inner join clientes b on a.cod_cliente = b.cod_cliente
inner join produtos c on a.cod_produto = c.cod_produto
where data >= month(curdate())-12
group by 1,2
order by 3 DESC LIMIT 5