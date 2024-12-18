import sqlite3

connection = sqlite3.connect('bot_shop.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')


def get_all_products():
    product_list = cursor.execute("SELECT * FROM Products").fetchall()
    connection.commit()
    return product_list