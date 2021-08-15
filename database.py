import sqlite3

DATABASE_NAME = "widgets.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    # SELECT name FROM sqlite_master WHERE type='table' AND name='table_name';
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT name FROM sqlite_master WHERE type='table' AND name='widgets'"
    cursor.execute(statement)
    check = cursor.fetchone()
    if check[0] == 'widgets':
        return

    tables = [
        """
        CREATE TABLE widgets (
            id           INTEGER     PRIMARY KEY AUTOINCREMENT,
            name         STRING (64),
            part_count   INTEGER     DEFAULT (1),
            created_date DATETIME,
            update_date  DATETIME
            )
        """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
