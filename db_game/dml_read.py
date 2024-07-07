import sqlite3

conn= sqlite3.connect('redland.db')
cursor= conn.cursor()

cursor.execute("""
SELECT 
    personagem.nome AS Nome, 
    personagem.titulo AS Titulo, 
    personagem.nivel AS Nivel, 
    personagem.status AS Status, 
    mapa.nome AS Habitacao, 
    mapa.reino AS Reino
FROM 
    personagem
JOIN 
    mapa ON personagem.idhabitacao = mapa.idlocal
WHERE
    Habitacao LIKE '%dorter trade city%' OR Habitacao LIKE '%orbonne monastery%'
ORDER
    BY Habitacao;
""")

colunas = [descricao[0] for descricao in cursor.description]
resultado= cursor.fetchall()

print(colunas)

for linha in resultado:
    print(linha)

cursor.close()
conn.close()

