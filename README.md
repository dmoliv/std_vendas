# 📊 Projeto de Análise de Dados STD - Desempenho de Vendas Pet Shop

Bem-vindo!

## 📝 Descrição do Projeto

Neste projeto, você assume o papel de analista de dados e trabalha com diversas fontes de dados para responder perguntas cruciais sobre o desempenho global da empresa. Os dados estão disponíveis em diferentes formatos e sistemas.

---

## 🛠️ Tecnologias Utilizadas

### Infraestrutura
- **VsCode**
- **Ubuntu 24.04**
- **MySQL**
- **MongoDB**

---

## 📁 Estrutura do Repositório

```bash
├── data/                     # Diretório de dados brutos
│   ├── mysql/                # Schemas de criação das tabelas e insert dos dados
│   ├── json/                 # Exemplo de documentos NoSQL
│   ├── csv/                  # Arquivos CSV
├── notebooks/                # notebooks das analises dos dados
├── outputs/                  # Relatórios e gráficos gerados
├── README.md                 # Descrição do projeto
```

## 🚀 Como Executar o Projeto
Clone o repositório:

```bash
git clone git@github.com:dmoliv/std_vendas.git
cd std_vendas
```

- 1. Configure uma instancia MySQL e crie o banco de dados com nome db_sales
- 2. Execute os scripts **schema.sql**, **insert.sql** e **views.sql** contidos no diretório data\mysql
- 3. Configure uma instancia MongoDB 
- 4. No MongoDB crie um Database com nome 'petshop' e uma coleção com nome 'feedback'
- 5. No servidor onde está instalado o MongoDB crie um diretório '/download/json'
- 6. coloque todos os documentos contindos em data\json no diretório acima
- 7. no servidor execute o comando para importar os documentos:
```bash
cd /download/json
ls -1 *.json | sed 's/.json$//' | while read col; do mongoimport -d petshop -c feedback < $col.json; done
```
- 8. instale as bibliotecas pandas e mysql conenctor
```bash
pip install mysql-connector-python
pip install pandas
pip install pymongo
pip install matplotlib
```

---

# 📊 Exemplos de Insights

## SQL

### Produto mais vendido por região
<img src="https://i.ibb.co/xJkfWGR/vendas-por-regiao.png" width="600" height="200" alt="Produto mais vendido por região">


### Clientes que mais gastaram nos últimos 12 meses
<img src="https://i.ibb.co/3spbktg/vendas-por-clientes.png" width="200" height="150" alt="Clientes que mais gastaram nos últimos 12 meses">

### Mês de maior faturamento e identifique os fatores
###### indica o mês 2 com vendas em menor quantidade, porém em produtos com maior valor agregado
<img src="https://i.ibb.co/dJjv3BD/venda-maior-periodo.png" width="250" height="150" alt="Mês de maior faturamento e identifique os fatores">


## No-SQL

### 5 maiores médias de avaliação dos produtos
<img src="https://i.ibb.co/5GGBKnW/5-maiores-medias-feedback.png" width="300" height="150" alt="5 maiores médias de avaliação dos produtos">

### 2 palavras mais comuns em feedbacks positivos
<img src="https://i.ibb.co/G5DBdg5/palavras-comuns.png" width="300" height="50" alt="2 palavras mais comuns em feedbacks positivos">


## Pandas

### desvio entre metas e vendas realizadas
<img src="https://i.ibb.co/XS1dwZr/desvio.png" width="300" height="150" alt="desvio entre metas e vendas realizadas">

### Gráfico 5 produtos que ainda não bateram meta anual
<img src="https://i.ibb.co/P9bj6Ww/output.png" width="600" height="600" alt="Gráfico 5 produtos que ainda não bateram meta anual">

