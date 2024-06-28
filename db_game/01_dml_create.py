import sqlite3

conn= sqlite3.connect('data_base/data_base.db')
cursor= conn.cursor()

dados= [
        (0, 'Igros Castle', 'cinza', 'Gallionne', 0),
        (1, 'Mandalia Plains', 'verde', 'Gallionne', 1),
        (2, 'Thieves Fort', 'laranja', 'Gallionne', 2),
        (3, 'Gariland Magic City', 'cinza', 'Gallionne', 3),
        (4, 'Sweegy Woods', 'verde', 'Gallionne', 4),
        (5, 'Dorter Trade City', 'cinza', 'Gallionne', 5),
        (6, 'Lenalia Plateau', 'verde', 'Gallionne', 6),
        (7, 'Fort Zeakden', 'cinza', 'Gallionne', 7),
        (8, 'Fovoham Plains', 'verde', 'Fovoham', 8),
        (9, 'Riovanes Castle', 'cinza', 'Fovoham', 9),
        (10, 'Yuguo Woods', 'verde', 'Fovoham', 10),
        (11, 'Yardow Fort City', 'cinza', 'Fovoham', 11),
        (12, 'Grog Hill', 'verde', 'Lesalia', 12),
        (13, 'Duguola Pass', 'verde', 'Lesalia', 13),
        (14, 'Bervenia Free City', 'cinza', 'Lesalia', 14),
        (15, 'Lesalia Imperial Capital', 'cinza', 'Lesalia', 15),
        (16, 'Goland Coal City', 'cinza', 'Lesalia', 16),
        (17, 'Zeklaus Desert', 'verde', 'Lesalia', 17),
        (18, 'Bervenia Volcano', 'verde', 'Lesalia', 18),
        (19, 'Orbonne Monastery', 'laranja', 'Lesalia', 19),
        (20, 'Araguay Woods', 'verde', 'Lesalia', 20),
        (21, 'Zirekile Falls', 'verde', 'Lesalia', 21),
        (22, 'Bethla Garrison', 'cinza', 'Lesalia', 22),
        (23, 'Finath River', 'verde', 'Zeltennia', 23),
        (24, 'Zeltennia Castle', 'cinza', 'Zeltennia', 24),
        (25, 'Zarghidas Trade City', 'cinza', 'Zeltennia', 25),
        (26, 'Germinas Peak', 'verde', 'Zeltennia', 26),
        (27, 'Poeskas Lake', 'verde', 'Limberry', 27),
        (28, 'Limberry Castle', 'cinza', 'Limberry', 28),
        (29, 'Doldobar Swamp', 'verde', 'Limberry', 29),
        (30, 'Bed Desert', 'verde', 'Limberry', 30),
        (31, 'Zaland Fort City', 'cinza', 'Lionel', 31),
        (32, 'Bariaus Hill', 'verde', 'Lionel', 32),
        (33, 'Lionel Castle', 'cinza', 'Lionel', 33),
        (34, 'Zigolis Swamp', 'verde', 'Lionel', 34),
        (35, 'Bariaus Valley', 'verde', 'Lionel', 35),
        (36, 'Golgorand Execution Site', 'laranja', 'Lionel', 36),
        (37, 'Warjilis Trade City', 'cinza', 'Lionel', 37),
        (38, 'Goug Machine City', 'cinza', 'Lionel', 38),
        (39, 'St. Murond Temple', 'laranja', 'Mullonde', 39),
        (40, 'Nelveska Temple', 'laranja', None, 40),
        (41, 'Deep Dungeon', 'verde', None, 41),
        (42, 'Murond Death City', 'laranja', None, 42)
]

cursor.executemany("""
INSERT INTO mapa (idlocal, nome, tipo, reino, lord)
VALUES (?, ?, ?, ?, ?)""", dados)

conn.commit()

cursor.close()
conn.close()

