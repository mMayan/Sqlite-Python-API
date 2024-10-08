import dbb.crud_db as crud_db

def create_user_table():
    db = crud_db.conecta_database()
    cursor = db.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL);
        """)   

def register_user(nome, senha):
    db = crud_db.conecta_database()
    cursor = db.cursor()

    cursor.execute(
        """INSERT INTO users(username, password)
        VALUES(?, ?);
    """, (nome, senha))
    
    db.commit()
    return True


def get_one_user(nome, senha):
    db = crud_db.conecta_database()
    cursor = db.cursor()

    cursor.execute(
        """SELECT * FROM users
        WHERE username = ? and password = ?;
    """, (nome, senha))
    return cursor.fetchone()

def delete_user(id):
    db = crud_db.conecta_database()
    cursor = db.cursor()

    cursor.execute(
        """DELETE FROM users WHERE id = ?;
    """, (id,))

    db.commit()
    return True


def get_users():
    db = crud_db.conecta_database()
    cursor = db.cursor()

    cursor.execute(
        """SELECT * FROM users;""")
    
    return cursor.fetchall()


def update_user(senha, nome):
    db = crud_db.conecta_database()
    cursor = db.cursor()

    cursor.execute(
        """UPDATE users SET password = ? WHERE username = ?;
    """, (senha, nome))

    db.commit()
    return True

def get_user_by_name_only(nome):
    db = crud_db.conecta_database()
    cursor = db.cursor()

    cursor.execute(
        """SELECT username FROM users WHERE username = ?
    """, (nome,))

    return cursor.fetchone()