import sqlite3

conn= sqlite3.connect('redland.db')
cursor= conn.cursor()

cursor.execute("SELECT * FROM personagem WHERE titulo LIKE '%monarca%'")
resultado= cursor.fetchall()

for linha in resultado:
    print(linha)

cursor.close()
conn.close()

