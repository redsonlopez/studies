import sqlite3

conn= sqlite3.connect('data_base/data_base.db')
cursor= conn.cursor()

dados= [
        (0, 'Igros Castle', 'Vito Corleone', , 'Gallionne')
        (1, 'Mandalia Plains', 'Philip J. Fry', , 'Gallionne')
        (2, 'Thieves Fort', , , 'Gallionne')
        (3, 'Gariland Magic City', , , 'Gallionne')
        (4, 'Sweegy Woods', , , 'Gallionne')
        (5, 'Dorter Trade City', , , 'Gallionne')
        (6, 'Lenalia Plateau', , , 'Gallionne')
        (7, 'Fort Zeakden', , , 'Gallionne')
        (8, 'Fovoham Plains', , , 'Fovoham')
        (9, 'Riovanes Castle', , , 'Fovoham')
        (10, 'Yuguo Woods', , , 'Fovoham')
        (11, 'Yardow Fort City', , , 'Fovoham')
        (12, 'Grog Hill', , , 'Lesalia')
        (13, 'Duguola Pass', , , 'Lesalia')
        (14, 'Bervenia Free City', , , 'Lesalia')
        (15, 'Lesalia Imperial Capital', , , 'Lesalia')
        (16, 'Goland Coal City', , , 'Lesalia')
        (17, 'Zeklaus Desert', , , 'Lesalia')
        (18, 'Bervenia Volcano', , , 'Lesalia')
        (19, 'Orbonne Monastery', , , 'Lesalia')
        (20, 'Araguay Woods', , , 'Lesalia')
        (21, 'Zirekile Falls', , , 'Lesalia')
        (22, 'Bethla Garrison', , , 'Lesalia')
        (23, 'Finath River', , , 'Zeltennia')
        (24, 'Zeltennia Castle', , , 'Zeltennia')
        (25, 'Zarghidas Trade City', , , 'Zeltennia')
        (26, 'Germinas Peak', , , 'Zeltennia')
        (27, 'Poeskas Lake', , , 'Limberry')
        (28, 'Limberry Castle', , , 'Limberry')
        (29, 'Doldobar Swamp', , , 'Limberry')
        (30, 'Bed Desert', , , 'Limberry')

•Lionel
Zaland Fort City
Bariaus Hill
Lionel Castle
Zigolis Swamp
Bariaus Valley
Golgorand Execution Site
Warjilis Trade City
Goug Machine City

•Mullonde
St. Murond Temple

•Others
Nelveska Temple
Deep Dungeon
Murond Death City

###

cursor.executemany("""
INSERT INTO worldmap (id_local, nome_local, lord_habitica, lord_antihabitica, reino)
VALUES (?, ?, ?, ?, ?)""", dados)
)

conn.commit()

cursor.close()
conn.close()

