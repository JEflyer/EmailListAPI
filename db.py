import sqlite3
from data import Email


connection = sqlite3.connect(
    ":memory:"
)  # instead of :memory: use DbName.db in production

cursor = connection.cursor()


def createTable():
    cursor.execute(
        """CREATE TABLE EmailList (id INTEGER AUTOINCREMENT, firstName text, lastName text, email text, number text)"""
    )

def addEmail(Email):
    cursor.execute(
        """INSERT INTO EmailList VALUES (?,?,?,?)""",
        (
            Email.firstName,
            Email.lastName,
            Email.email,
            Email.number
        )
    )

def __init__():
    createTable()