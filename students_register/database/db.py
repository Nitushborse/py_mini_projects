import sqlite3

DB_NAME = "students.db"


# ✅ Create table if not exists
def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            class TEXT NOT NULL,
            city TEXT NOT NULL
        )
    """)

    # insert_dummy_records()

    conn.commit()
    conn.close()

def insert_dummy_records():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    students = []
    for i in range(1, 51):  # 1 to 50
        students.append((
            i,
            f"Student {i}",
            f"{(i % 12) + 1}th",  # Random class from 1th to 12th
            f"City {i}"
        ))

    cur.executemany("INSERT OR REPLACE INTO students (roll, name, class, city) VALUES (?, ?, ?, ?)", students)
    conn.commit()
    conn.close()


# ✅ Insert Student
def add_student(roll, name, class_, city):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (roll, name, class, city) VALUES (?, ?, ?, ?)",
        (roll, name, class_, city)
    )
    conn.commit()
    conn.close()


# ✅ Read All Students
def get_all_students():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows


# ✅ Update Student
def update_student(roll, name, class_, city):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name=?, class=?, city=? WHERE roll=?",
        (name, class_, city, roll)
    )
    conn.commit()
    conn.close()


# ✅ Delete Student
def delete_student(roll):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll=?", (roll,))
    conn.commit()
    conn.close()
