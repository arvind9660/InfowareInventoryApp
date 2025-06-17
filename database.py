import sqlite3

def create_connection():
    conn=sqlite3.connect("inventory.db")
    return conn
def init_db():
    conn=create_connection()
    cursor=conn.cursor()

    #USER TABLE
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT)'''
    )
    # Product Master table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product_master (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barcode TEXT,
            sku_id TEXT,
            category TEXT,
            subcategory TEXT,
            name TEXT,
            description TEXT,
            tax REAL,
            price REAL,
            unit TEXT,
            image_path TEXT
        )
    ''')

    # Goods Receiving table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS goods_receiving (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            supplier TEXT,
            quantity INTEGER,
            unit TEXT,
            rate_per_unit REAL,
            tax REAL,
            total_rate REAL
        )
    ''')

    # Sales table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            customer TEXT,
            quantity INTEGER,
            unit TEXT,
            rate_per_unit REAL,
            tax REAL,
            total_rate REAL
        )
    ''')

    # 2 default users
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("arvind", "pass123"))
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("operator2", "pass456"))
    except:
        pass 

    conn.commit()
    conn.close()