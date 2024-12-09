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

# %%

# Determine as 5 maiores médias de avaliação dos produtos
documentos = colecao.aggregate([
    { 
        "$group": { 
            "_id": "$ProdutoID",
            "avg": { "$avg": "$Nota" } 
        } 
    },
    { 
        "$sort": { "avg": -1 }  # Ordena pela média em ordem decrescente
    },
    { 
        "$limit": 5  # Limita aos 5 primeiros resultados
    }
])
     
# Iterar pelos documentos e exibi-los
for doc in documentos:
    print(doc)


# %%

# Identifique 2 palavras mais comuns em feedbacks positivos (rating >= 4)

# Biblioteca para contar as ocorrências de palavras
from collections import Counter

# Filtrar os documentos com Nota >= 4
documentos = colecao.find({"Nota": {"$gte": 4}})

contador_palavras = Counter() # inicializa contador
for doc in documentos:
    comentario = doc.get("Comentario", "")  # Pegar o campo 'Comentario'
    palavras = comentario.split()  # Dividir o texto em palavras
    contador_palavras.update(palavras)  # Atualizar o contador com as palavras

# Mostrar as 2 palavras mais comuns
palavras_comuns = contador_palavras.most_common(2)
palavras_comuns
