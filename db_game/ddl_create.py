import sqlite3

conn= sqlite3.connect('redland.db')
cursor= conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mapa(
    idlocal INTEGER NOT NULL PRIMARY KEY,
    nome TEXT NOT NULL,
    area TEXT NOT NULL,
    reino TEXT,
    idlord INTEGER,
    FOREIGN KEY (idlord) REFERENCES personagem(idpersonagem)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS personagem(
    idpersonagem INTEGER NOT NULL PRIMARY KEY,
    nome TEXT NOT NULL,
    idhabitacao INTEGER,
    titulo TEXT,
    nivel VARCHAR(1),
    ouro INTEGER,
    status TEXT,
    FOREIGN KEY (idhabitacao) REFERENCES mapa(idlocal),
    CHECK (nivel IN ('s', 'a', 'b', 'c', 'd', 'e') OR nivel IS NULL)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS item(
    item TEXT NOT NULL,
    descricao TEXT,
    idproprietario INTEGER,
    FOREIGN KEY (idproprietario) REFERENCES personagem(idpersonagem)
);
""")

conn.commit()
conn.close()

