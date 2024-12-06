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
│   ├── mongo/                # Exemplo de documentos NoSQL
│   ├── csv_excel/            # Arquivos CSV e Excel 
├── scripts/                  # Diretório de scripts
│   ├── views/                # views para criar no MySQL
│   ├── bash/                 # scripts bash
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
- 2. Execute os scripts **schema.sql** e **insert.sql** contidos no diretório data\mysql
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
```

---

# 📊 Exemplos de Insights

## SQL

### Produto mais vendido por região
<img src="https://cvws.icloud-content.com/B/AbURabx8jlzmPae165iLawioA0yiATID_QUCr02juqQayuq3iZXiOH7j/vendas_por_regiao.png?o=ArNNub2HEbulw__3nrnuE12zovtlSvnPr437Sxs2LoWT&v=1&x=3&a=CAogSVB5PqPWsrdngb_jS4E8S3F-hWRZGvCzHATM95O4l_ESbxDe4ereuTIY3r7G4LkyIgEAUgSoA0yiWgTiOH7jaidbYcahZn_oBRT90-P4c_b_F9xN5UD3tO_ShmPmJjN0xsnPwGh-9LFyJ3V1kgz2Sg_sAZZjsYo5RL7Ymoy1PTEIaWNn3-AA9cePXVeLKZ0kqQ&e=1733490220&fl=&r=466ec278-f2ae-477b-8d09-ecaea19968c9-1&k=1RJ4z-CNV5QIRLNomKIKIQ&ckc=com.apple.clouddocs&ckz=com.apple.CloudDocs&p=107&s=nk7uAuanCWJiDoY5fZg_EfQFyRA&cd=i" alt="Produto mais vendido por região">


### Clientes que mais gastaram nos últimos 12 meses
<img src="https://cvws.icloud-content.com/B/AS34-QncvEJKvC3aLr1_8EPrjmoPAQvOdEWvDY9zMaYhMmaHHfQrc3Ur/vendas_por_clientes.png?o=AsPdvAaN_Qlzm1Qea7nmOg4YFvnCeREmZYMZejQ_pyF9&v=1&x=3&a=CAogKBoMFC6Az3Ev5LDWY1VOG8EcaJdWBZaGVbvuJQl-lpYSbxDQ1ereuTIY0LLG4LkyIgEAUgTrjmoPWgQrc3Uraic_OONeG_gJGpLftVf5dUEjT7yeTwCzCytmWpPbzY0LFbr1p27U-G9yJ2tBsw_9eybLunLR2b91KYOc8ADyujqDHfG31apQw0LGuIzLCG1Upg&e=1733490219&fl=&r=7d1565c3-e084-47f0-b8dd-e86ca2dc0e30-1&k=UdudMptaO6Y0O4oODTtVOg&ckc=com.apple.clouddocs&ckz=com.apple.CloudDocs&p=107&s=FIpES4c--13XsE6vqROGvO-qLnA&cd=i" alt="Clientes que mais gastaram nos últimos 12 meses">

### Mês de maior faturamento e identifique os fatores
###### indica o mês 2 com vendas em menor quantidade, porém em produtos com maior valor agregado
<img src="https://cvws.icloud-content.com/B/AUko9iuB_S056kqxwJ9J8JARN8mhAexyogvrvRAr72Yq5o1iQqdYNyBz/venda_maior_periodo.png?o=As96-DAILR7V_fHh3Npv9FJNXH1zuIff4QxH8MuLs0Ux&v=1&x=3&a=CAoggYNOM0AJeBxnTXUR4CiQPsoHyrNeV1cSZ75zninFM-USbxD9k-reuTIY_fDF4LkyIgEAUgQRN8mhWgRYNyBzaieHXNgMsmuzE1cMIojz85hGTu3VSU6rea21hFSGv8skQiOfFaQ5gLVyJ5jHGFhmNJkp_oDqNkeG5QBysi9avJ1fUpcaxTMh6Klh_aErnFs_MQ&e=1733490210&fl=&r=53743c7d-d1a8-450a-b38e-a4f17ec8aa19-1&k=CrCT2fan6QVU-8_bbBW2nw&ckc=com.apple.clouddocs&ckz=com.apple.CloudDocs&p=107&s=N72nn_AYnTRUrwDMAXhx2i1ftpw&cd=i" alt="Mês de maior faturamento e identifique os fatores">


## No-SQL

### 5 maiores médias de avaliação dos produtos
<img src="https://www.icloud.com/iclouddrive/078uPyeSUVlqKSekyxlIGrDCQ#5_maiores_medias_feedback" alt="5 maiores médias de avaliação dos produtos">