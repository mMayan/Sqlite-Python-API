import sqlite3 as sql

DATABASE_NAME = 'supermarket.db'

def conecta_database():
    connection = sql.connect(DATABASE_NAME)
    return connection

def create_table():
    db = conecta_database()
    cursor = db.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS supermercado(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto VARCHAR(50) NOT NULL,
        valor FLOAT NOT NULL,
        estoque INTEGER NOT NULL);
        """)
        

# conexão e criação da tabela
# ============================
# CRUD

def insert_product(produto, valor, estoque):
    db = conecta_database()
    cursor = db.cursor()

    cursor.execute(
        """INSERT INTO supermercado(produto, valor, estoque)
        VALUES(?, ?, ?);
        """, (produto, valor, estoque))
    db.commit()
    return True


def get_product():
    db = conecta_database()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM supermercado;")
    return cursor.fetchall()


def update_product(produto, valor, estoque):
    db = conecta_database()
    cursor = db.cursor()

    cursor.execute("UPDATE supermercado SET estoque = ?, valor = ? WHERE produto = ?;", (estoque, valor, produto))
    db.commit()
    return True


def delete_product(id):
    db = conecta_database()
    cursor = db.cursor()

    cursor.execute("DELETE FROM supermercado WHERE id = ?;", (id,))
    db.commit()
    return True




    