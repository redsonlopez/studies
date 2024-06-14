import sqlite3

conn= sqlite3.connect('redDB.db')
cursor= conn.cursor()

cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor= 2")
conn.commit()

cursor.execute("SELECT * FROM fornecedor")
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conn.close()

