import sqlite3

conn= sqlite3.connect('data_base/data_base.db')

ddl_create= """
CREATE TABLE IF NOT EXISTS mapa(
    idlocal INTEGER NOT NULL PRIMARY KEY,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    reino TEXT,
    lord INTEGER
);
"""

cursor= conn.cursor()
cursor.execute(ddl_create)

cursor.close()
conn.close()

