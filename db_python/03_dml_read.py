import sqlite3

conn= sqlite3.connect('redDB.db')
cursor= conn.cursor()

cursor.execute("SELECT * FROM fornecedor")
resultado= cursor.fetchall()

for linha in resultado:
    print(linha)

cursor.close()
conn.close()

