# %%

from pymongo import MongoClient

# Conexão com o MongoDB sem autenticação
client = MongoClient('192.168.0.199:27017')

# Selecionar o banco de dados
db = client['petshop']

# Listar as coleções para verificar a conexão
colecoes = db.list_collection_names()
print("Coleções disponíveis no banco de dados 'petshop':")
for colecao in colecoes:
    print(colecao)

# Conectar à coleção
colecao = db['feedback']

# Executar um find para obter todos os documentos
#documentos = colecao.find({"Nota": 5})

#soma das notas por produto
documentos = colecao.aggregate([
    { 
        "$group": { 
            "_id": "$ProdutoID", 
            "total": { "$sum": "$Nota" } 
        } 
    }
])


# Iterar pelos documentos e exibi-los
for doc in documentos:
    print(doc)