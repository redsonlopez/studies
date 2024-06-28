import sqlite3

conn= sqlite3.connect('data_base/data_base.db')

ddl_create= """
CREATE TABLE IF NOT EXISTS item(
    item TEXT NOT NULL,
    descricao TEXT,
    proprietario INTEGER,
    FOREIGN KEY (proprietario) REFERENCES personagem(idpersonagem)
);
"""

cursor= conn.cursor()
cursor.execute(ddl_create)

cursor.close()
conn.close()

