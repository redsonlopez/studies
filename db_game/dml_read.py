import sqlite3

conn= sqlite3.connect('data_base/data_base.db')
cursor= conn.cursor()

cursor.execute("SELECT nome_local, lord_local, reino_local FROM worldmap WHERE nome_local LIKE '%Castle%'")
resultado= cursor.fetchall()

for linha in resultado:
    print(linha)

cursor.close()
conn.close()

