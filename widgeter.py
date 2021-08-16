from database import get_db


def insert_widget(name, part_count, created_date):
    db = get_db()
    cursor = db.cursor()
    update_date = created_date
    statement = "INSERT INTO widgets(name, part_count, created_date, " \
                "update_date) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [name, part_count, created_date, update_date])
    db.commit()
    return True


def update_widget(id, name, part_count, update_date):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE widgets SET name = ?, part_count = ?, " \
                "update_date = ? WHERE id = ?"
    cursor.execute(statement, [name, part_count, update_date, id])
    db.commit()
    return True


def delete_widget(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM widgets WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, part_count, created_date, update_date " \
                "FROM widgets WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_widgets():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, part_count, created_date, update_date " \
            "FROM widgets"
    cursor.execute(query)
    return cursor.fetchall()
