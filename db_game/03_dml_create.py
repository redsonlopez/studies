import sqlite3

conn= sqlite3.connect('data_base/data_base.db')
cursor= conn.cursor()

dados= [
        ('mapa', None, None),
        ('flauta', None, 1),
        ('escudo da meia noite', None, None),
        ('luva das sombras', None, None),
        ('foice', None, 4),
        ('glaive do grifo mistico falsa', None, None),
        ('espada das almas sombrias falsa', None, None),
        ('espadas gemeas', None, 6),
        ('besta', None, None),
        ('cajado', None, 8),
        ('orbe sinistro', None, None),
        ('machado', None, None),
        ('espadas gemeas', None, 14),
        ('faca adaga', None, None),
        ('pocao da tentacao', None, None),
        ('espada de magma', None, 18),
        ('faca', None, 21),
        ('arco', None, 21),
        ('arco', None, 23),
        ('maca', None, None),
        ('espada sabre', None, 25),
        ('faca', None, 25),
        ('pistola', None, 29),
        ('chicote de minos', None, None),
        ('espada', None, 32),
        ('luva', None, None),
        ('grimorio', None, 33),
        ('boneco de vodu', None, 33),
        ('luva da escuridao', None, None),
        ('espadas gemeas da escuridao', None, 34),
        ('espada', None, 36),
        ('espada amaldicoada', None, None),
        ('arco da luz', None, 39),
        ('martelo luminoso falso', None, None),
        ('espada de espectro', None, None),
        ('espada rapieira', None, None),
        ('besta', None, None),
        ('espada das sombras', None, None),
        ('relogio de bolso', None, None),
        ('bengala real', None, 43),
        ('lupa', None, 43),
        ('espada curta', None, None),
]

cursor.executemany("""
INSERT INTO item (item, descricao, proprietario)
VALUES (?, ?, ?)""", dados)

conn.commit()

cursor.close()
conn.close()

