import pandas as pd
import sqlite3

cursor= sqlite3.connect('redDB.db').cursor()

cursor.execute("SELECT * FROM fornecedor")
print(pd.DataFrame(cursor.fetchall(), columns=None, index=None))

cursor.close()

