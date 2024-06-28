import sqlite3

conn= sqlite3.connect('data_base/data_base.db')
cursor= conn.cursor()

dados= [
        (0, 'elo', 0, 'monarca da peversao', 's', None),
        (1, 'satiro', 1, 'bardo', 'b', None),
        (2, 'cyclops', 2, 'gigante desespero', 'b', None),
        (3, 'ungoliant', 3, 'gula', 'a', None),
        (4, 'freddy', 4, 'terror', 'b', None),
        (5, 'vicio', 5, 'vicio', 'b', None),
        (6, 'naga', 6, 'distracao', 'b', None),
        (7, 'evil santa', 7, None, 'b', None),
        (8, 'recaida', 8, 'necromante', 'b', None),
        (9, 'asagi', 9, 'odio', 's', None),
        (10, 'lavadeiromante', 10, 'necromante', 'c', None),
        (11, 'serket', 11, 'monarca da inveja', 'a', None),
        (12, 'estresse sombrio', 12, 'estresse sombrio', 'c', None),
        (13, 'coelinhos ferais', 13, 'poeira', 'd', None),
        (14, 'Hanzo sama', 14, 'monarca da ira', 'a', None),
        (15, 'madame agonia', 15, 'agonia', 'a', None),
        (16, 'goliath', 16, 'monarca da gula', 'a', None),
        (17, 'granit', 17, 'criatura da caverna', 'b', None),
        (18, 'minotaur', 18, 'ira', 'b', None),
        (19, 'justia', 19, 'injustica', 'b', None),
        (20, 'basilist', 20, 'lista basica', 'd', None),
        (21, 'goblin', 21, 'ladrao de propositos', 'c', None),
        (22, 'kitsune', 22, 'entorpecente', 'b', None),
        (23, 'clever', 23, 'distracao', 'b', None),
        (24, 'defronowe', 24, 'succubus djinn', 'a', None),
        (25, 'heider', 25, 'monarca da avareza', 'a', None),
        (26, 'arryl', 26, None, 'a', None),
        (27, 'vera', 27, None, 'b', None),
        (28, 'tengu', 28, 'ladrao de conhecimento', 's', None ),
        (29, 'silene', 29, None, 'b', None),
        (30, 'exaustao', 30, 'exaustao e cansaco', 'b', None),
        (31, 'Hipnos', 31, 'monarca da preguica', 'a', None),
        (32, 'Hehta', 32, None, 'a', None),
        (33, 'madame lotrix', 33, 'marionetista', 's', None),
        (34, 'zalidus', 34, None, 'a', None),
        (35, 'strik', 35, 'agonia', 'b', None),
        (36, 'ironknight', 36, 'devorador de orgulho', 'b', None),
        (37, 'enlil', 37, 'manipuladora dos ventos', 'b', None),
        (38, 'lilium', '38', 'monarca da luxuria', 'a', None),
        (39, 'ismat', 39, 'monarca da soberba', 'a', None),
        (40, 'Stheno', 40, 'distracao', 'a', None),
        (41, 'lashna', 41, 'kraken do incompleto', 'a', None),
        (42, 'djinn', 42, 'djinn', 'b', None),
        (43, 'hades', 3, 'mago', 'a', 'charme')
]

cursor.executemany("""
INSERT INTO personagem (idpessoa, nome, local, titulo, tier, status)
VALUES (?, ?, ?, ?, ?, ?)""", dados)

conn.commit()

cursor.close()
conn.close()

