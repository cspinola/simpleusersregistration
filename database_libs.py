import sqlite3

# Connect to a Database
def conect_db(database_name):
    conection = sqlite3.connect(database_name)
    return conection

def desconect_db(database_name):
        database_name.close()

# Create table
def create_table(conection):
    cursor = conection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            nome TEXT PRIMARY KEY,
            email TEXT  NOT NULL,
            age INTEGER NOT NULL,
            phone TEXT NOT NULL
        );
    """)
    
    conection.commit()

# Insert a new user
def insert_user(conection, nome, email, age, phone):
    cursor = conection.cursor()
    cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?)",
                   (nome, email, age, phone))
    conection.commit()

# List all users
def show_users(conection):
    cursor = conection.cursor()
    cursor.execute(f"SELECT * FROM Users")
    return cursor.fetchall()
