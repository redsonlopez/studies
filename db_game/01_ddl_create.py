import sqlite3

conn= sqlite3.connect('data_base/data_base.db')

ddl_create= """
CREATE TABLE IF NOT EXISTS worldmap(
    id_local INTEGER NOT NULL PRIMARY KEY,
    nome_local TEXT NOT NULL,
    lord_habitica TEXT,
    lord_antihabitica TEXT,
    reino TEXT
);
"""

cursor= conn.cursor()
cursor.execute(ddl_create)

cursor.close()
conn.close()

