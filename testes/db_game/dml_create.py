import sqlite3
from personagem import personagem
from item import item
from mapa import mapa

conn= sqlite3.connect('redland.db')
cursor= conn.cursor()

cursor.executemany("""
INSERT INTO personagem (idpersonagem, nome, idhabitacao, titulo, nivel, ouro, status)
VALUES (?, ?, ?, ?, ?, ?, ?)""", personagem)

cursor.executemany("""
INSERT INTO item (item, descricao, idproprietario)
VALUES (?, ?, ?)""", item)

cursor.executemany("""
INSERT INTO mapa (idlocal, nome, area, reino, idlord)
VALUES (?, ?, ?, ?, ?)""", mapa)

conn.commit()
conn.close()

