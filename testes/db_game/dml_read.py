import sqlite3

conn= sqlite3.connect('redland.db')
cursor= conn.cursor()

cursor.execute("""
SELECT 
    pe.nome AS Nome, 
    pe.titulo AS Titulo, 
    pe.nivel AS Nivel, 
    pe.status AS Status, 
    ma.nome AS Habitacao, 
    ma.reino AS Reino
FROM 
    personagem pe
JOIN 
    mapa ma
ON
    pe.idhabitacao = ma.idlocal
WHERE
    ma.area LIKE '%%'
ORDER BY
    Habitacao;
""")

colunas = [descricao[0] for descricao in cursor.description]
resultado= cursor.fetchall()

print(colunas)

for linha in resultado:
    print(linha)

cursor.close()
conn.close()

