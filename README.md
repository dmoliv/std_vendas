# 📊 Projeto de Análise de Dados STD - Desempenho de Vendas Pet Shop

Bem-vindo!

## 📝 Descrição do Projeto

Neste projeto, você assume o papel de analista de dados e trabalha com diversas fontes de dados para responder perguntas cruciais sobre o desempenho global da empresa. Os dados estão disponíveis em diferentes formatos e sistemas.

---

## 🛠️ Tecnologias Utilizadas

### Infraestrutura
- **MySQL**
- **MongoDB**

---

## 📁 Estrutura do Repositório

```bash
├── data/                     # Diretório de dados brutos
│   ├── mysql/                # Schemas de criação das tabelas e insert dos dados
│   ├── mongo/                # Exemplo de documentos NoSQL
│   ├── csv_excel/            # Arquivos CSV e Excel 
├── scripts/                  # Diretório para scripts SQL/Bash
│   ├── sql/                  # Scripts SQL para analise dos dados
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
- Execute os scripts **schema.sql** e **insert.sql** contidos no diretório data\mysql

- 2. Configure uma instancia MongoDB 

---

# 📊 Exemplos de Insights

## SQL

### Produto mais vendido por região
<img src="https://cvws.icloud-content.com/B/AdhHt-mQOMEJtT8M0QZdtQzXzqIwAQ0WshAZKr86AFy00tDr8Lxtu1nd/vendas_por_regiao.png?o=Aj-N3sZdpmMeD4iJcgsTCXTX3SGJ-0YryePEMamXLuZO&v=1&x=3&a=CAogTWykEveZFW5qsq7DNMzTgsVDt0l0NFHNGdTF9eK3TykSbxCq66mXuTIYqsiFmbkyIgEAUgTXzqIwWgRtu1ndaiczOpgc2kfnBtXD4K-I1dda9rvNjsYEE_-KlLrZvnBvWQnZ-VvLKsFyJyOlPqvEOPsYOsmAA3UVGVxqMfZADCG-DaZpwHUk3fRXIiyijVttKA&e=1733340259&fl=&r=0668f7df-72ad-4f6b-b66a-59c33f1d25b4-1&k=K_VlRgMSpW6CaNOP875cHQ&ckc=com.apple.clouddocs&ckz=com.apple.CloudDocs&p=107&s=_re_T7PRhhiwvF87-2bOtGEtqP0&cd=i" alt="Produto mais vendido por região">


### Clientes que mais gastaram nos últimos 12 meses
<img src="https://cvws.icloud-content.com/B/AV_bH9EB52pfavqvZGc8bMLTjDFHAQkGmokSnRXBZ1Vy1wzBmq-4zztC/clientes_maiores_gastos.png?o=As9JgySkC7arjjiH1DWNhkvUw4jqpcpc3czgvWehDz60&v=1&x=3&a=CAoguhhAT7UhnRMU0J4KCnv4b2RdHX0EsNVvKPPzCenSAQcSbxDy2qmXuTIY8reFmbkyIgEAUgTTjDFHWgS4zztCaif5cK3_uxLcTLqDWNqeGT_CuJeLtFbkk1vkTv6iG3OSz0QyF5PxxrVyJwdArbdLwDvY8dvaN7PLkA9PbTgHERFWlJAxVf_qD33eVpKqM1c6vw&e=1733340257&fl=&r=4cc3f53b-22a7-4ba0-a487-cfd216e7a398-1&k=7hKUih3szO1Wc4m22KVD1Q&ckc=com.apple.clouddocs&ckz=com.apple.CloudDocs&p=107&s=K_ZE7p2cPg7fdlVBhJawdVQ7xYY&cd=i" alt="Clientes que mais gastaram nos últimos 12 meses">

### Mês de maior faturamento e identifique os fatores
###### indica o mês 2 com vendas em menor quantidade, porém em produtos com maior valor agregado
<img src="https://cvws.icloud-content.com/B/AVzmHx-JfF4vY53JRq17tIPjatxdAZG9C1ok33Z_9UDJPhrRrbD-TD4M/mes_maior_fat.png?o=ApeWUr5Buu5ND1E7Oqw6KrbLTZ8fd5Ld6qBffD_mekDi&v=1&x=3&a=CAogjAQGJHpmVuje4MlohlCagXcxEgIYVHbJ_gH9-CTSz_QSbxDRtfWXuTIY0ZLRmbkyIgEAUgTjatxdWgT-TD4MaieidrUS3FPiohqc2MAIk_otQBol2PfuCsTb8qe1j4FVfllG-uP_ivZyJzqYIOca0k1lMoog6Nxu2JZY08JBcFG2QC08IcJAZ09HkCR_8IjS0w&e=1733341497&fl=&r=4241bcce-cc14-463b-a370-23c4a1c4a19d-1&k=ZxO0yuEw8fPY4NKbjFABhA&ckc=com.apple.clouddocs&ckz=com.apple.CloudDocs&p=107&s=pDmLMvOsZ5WHqRUvj3zF4V2qo8Y&cd=i" alt="Mês de maior faturamento e identifique os fatores">
