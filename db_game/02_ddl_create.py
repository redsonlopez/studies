import sqlite3

conn= sqlite3.connect('data_base/data_base.db')

#idpessoa, nome, local, titulo, tier, status
ddl_create= """
CREATE TABLE IF NOT EXISTS personagem(
    idpersonagem INTEGER NOT NULL PRIMARY KEY,
    nome TEXT NOT NULL,
    idlocal INTEGER,
    titulo TEXT,
    nivel VARCHAR(2),
    CHECK (nivel IN ('ss', 's', 'a', 'b', 'c', 'd', 'e') OR nivel IS NULL),
    status TEXT,
    FOREIGN KEY (idlocal) REFERENCES mapa(idlocal)
);
"""

cursor= conn.cursor()
cursor.execute(ddl_create)

cursor.close()
conn.close()

