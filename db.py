import sqlite3
from data import Email
import pandas as pd


connection = sqlite3.connect(
    "emails.db"
)  # instead of :memory: use DbName.db in production

cursor = connection.cursor()


def createTable():
    with connection:
        cursor.execute(
            """CREATE TABLE EmailList ( firstName text, lastName text, email text)"""
        )

def addEmail(Email):
    with connection:
        cursor.execute(
            """INSERT INTO EmailList VALUES (?,?,?)""",
            (
                Email.firstName,
                Email.lastName,
                Email.email
            )
        )


def getEmails():
    return cursor.execute(
        """SELECT rowId,email FROM EmailList"""
    )

def __init__():
    try:
        createTable()
    except:
        return


__init__()