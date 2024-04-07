# Module Imports
import mariadb
import sys

def ConnectToDatabase():
    # Change this for your database information
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="DESKTOP-PGCUKPO",
            port=3306,
            database="card_harbor"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()

    return cur

