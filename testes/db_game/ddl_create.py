import sqlite3

conn= sqlite3.connect('redland.db')
cursor= conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mapa(
    idlocal INTEGER NOT NULL PRIMARY KEY,
    nome VARCHAR(25) NOT NULL,
    area VARCHAR(7) NOT NULL,
    reino VARCHAR(15),
    idlord INTEGER,
    FOREIGN KEY (idlord) REFERENCES personagem(idpersonagem),
    CHECK (area IN ('cinza', 'verde', 'laranja'))
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS personagem(
    idpersonagem INTEGER NOT NULL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    idhabitacao INTEGER,
    titulo VARCHAR(25),
    nivel INTEGER,
    ouro INTEGER,
    status VARCHAR(25),
    FOREIGN KEY (idhabitacao) REFERENCES mapa(idlocal),
    CHECK (status IN ('normal', 'enfraquecido', 'controlado', 'imobilizado', 'morto') OR status IS NULL)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS item(
    item VARCHAR(50) NOT NULL,
    descricao TEXT,
    idproprietario INTEGER,
    FOREIGN KEY (idproprietario) REFERENCES personagem(idpersonagem)
);
""")

conn.commit()
conn.close()

