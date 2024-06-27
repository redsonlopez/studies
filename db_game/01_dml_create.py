import sqlite3

conn= sqlite3.connect('data_base/data_base.db')
cursor= conn.cursor()

dados= [
        (0, 'Igros Castle', 'cinza', 'Elo', 'Gallionne'),
        (1, 'Mandalia Plains', 'verde', 'Satiro', 'Gallionne'),
        (2, 'Thieves Fort', 'laranja', 'Cyclops', 'Gallionne'),
        (3, 'Gariland Magic City', 'cinza', 'Ungoliant', 'Gallionne'),
        (4, 'Sweegy Woods', 'verde', 'Freddy', 'Gallionne'),
        (5, 'Dorter Trade City', 'cinza', 'Vicio', 'Gallionne'),
        (6, 'Lenalia Plateau', 'verde', 'Naga', 'Gallionne'),
        (7, 'Fort Zeakden', 'cinza', 'Evil Santa', 'Gallionne'),
        (8, 'Fovoham Plains', 'verde', 'Recaida', 'Fovoham'),
        (9, 'Riovanes Castle', 'cinza', 'Asagi', 'Fovoham'),
        (10, 'Yuguo Woods', 'verde', 'Lavadeiromante', 'Fovoham'),
        (11, 'Yardow Fort City', 'cinza', 'Serket', 'Fovoham'),
        (12, 'Grog Hill', 'verde', 'Estresse Sombrio', 'Lesalia'),
        (13, 'Duguola Pass', 'verde', 'Coelinhos Ferais', 'Lesalia'),
        (14, 'Bervenia Free City', 'cinza', 'Hanzo', 'Lesalia'),
        (15, 'Lesalia Imperial Capital', 'cinza', 'Agonia', 'Lesalia'),
        (16, 'Goland Coal City', 'cinza', 'Goliath', 'Lesalia'),
        (17, 'Zeklaus Desert', 'verde', 'Granit', 'Lesalia'),
        (18, 'Bervenia Volcano', 'verde', 'Minotaur', 'Lesalia'),
        (19, 'Orbonne Monastery', 'laranja', 'Justia', 'Lesalia'),
        (20, 'Araguay Woods', 'verde', 'Basilist', 'Lesalia'),
        (21, 'Zirekile Falls', 'verde', 'Goblin', 'Lesalia'),
        (22, 'Bethla Garrison', 'cinza', 'Kitsune', 'Lesalia'),
        (23, 'Finath River', 'verde', 'Clever', 'Zeltennia'),
        (24, 'Zeltennia Castle', 'cinza', 'Defronowe', 'Zeltennia'),
        (25, 'Zarghidas Trade City', 'cinza', 'Heider', 'Zeltennia'),
        (26, 'Germinas Peak', 'verde', 'Arryl', 'Zeltennia'),
        (27, 'Poeskas Lake', 'verde', 'Vera', 'Limberry'),
        (28, 'Limberry Castle', 'cinza', 'Tengu', 'Limberry'),
        (29, 'Doldobar Swamp', 'verde', 'Silene', 'Limberry'),
        (30, 'Bed Desert', 'verde', 'Exaustao', 'Limberry'),
        (31, 'Zaland Fort City', 'cinza', 'Hipnos', 'Lionel'),
        (32, 'Bariaus Hill', 'verde', 'Hehta', 'Lionel'),
        (33, 'Lionel Castle', 'cinza', 'LoTrix', 'Lionel'),
        (34, 'Zigolis Swamp', 'verde', 'Zalidus', 'Lionel'),
        (35, 'Bariaus Valley', 'verde', 'Strik', 'Lionel'),
        (36, 'Golgorand Execution Site', 'laranja', 'Ironknight', 'Lionel'),
        (37, 'Warjilis Trade City', 'cinza', 'Enlil', 'Lionel'),
        (38, 'Goug Machine City', 'cinza', 'Lilium', 'Lionel'),
        (39, 'St. Murond Temple', 'laranja', 'Ismat', 'Mullonde'),
        (40, 'Nelveska Temple', 'laranja', 'Stheno', 'Others'),
        (41, 'Deep Dungeon', 'verde', 'Lashna', 'Others'),
        (42, 'Murond Death City', 'laranja', 'Djinn', 'Others')
]

cursor.executemany("""
INSERT INTO worldmap (id_local, nome_local, tipo_local, lord_local, reino_local)
VALUES (?, ?, ?, ?, ?)""", dados)

conn.commit()

cursor.close()
conn.close()
