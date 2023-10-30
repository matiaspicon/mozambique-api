import sqlite3

db_path = "database.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        barcode INTEGER NOT NULL,
        invoice_number TEXT NOT NULL,
        supplier_id INTEGER NOT NULL,
        n_units INTEGER NOT NULL,
        timestamp TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        barcode INTEGER NOT NULL,
        customer_name TEXT NOT NULL,
        customer_phone_number TEXT NOT NULL,
        price FLOAT NOT NULL,
        n_units INTEGER NOT NULL,
        timestamp TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("Base de datos y tabla creadas exitosamente en", db_path)