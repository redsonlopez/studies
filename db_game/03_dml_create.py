import sqlite3

conn= sqlite3.connect('data_base/data_base.db')
cursor= conn.cursor()

dados= [
        (),
        ('espada', None, None)
]

cursor.executemany("""
INSERT INTO item (item, descricao, proprietario)
VALUES (?, ?, ?)""", dados)

conn.commit()

cursor.close()
conn.close()

