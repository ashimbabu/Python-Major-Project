import sqlite3
from datetime import date

# =========================
# Database Setup
# =========================
class Database:
    def __init__(self, db_name="school_fee.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            class TEXT,
            roll_no TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS fees (
            class TEXT PRIMARY KEY,
            total_fee REAL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            amount_paid REAL,
            payment_date TEXT,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
        """)
        self.conn.commit()

    def close(self):
        self.conn.close()


# =========================
# Fee Management
# =========================
class FeeManagement:
    def __init__(self, db):
        self.db = db

    def add_student(self, name, class_name, roll_no):
        self.db.cursor.execute("""
        INSERT INTO students (name, class, roll_no)
        VALUES (?, ?, ?)
        """, (name, class_name, roll_no))
        self.db.conn.commit()
        print("Student registered successfully.")

    def set_class_fee(self, class_name, total_fee):
        self.db.cursor.execute("""
        INSERT OR REPLACE INTO fees (class, total_fee)
        VALUES (?, ?)
        """, (class_name, total_fee))
        self.db.conn.commit()
        print("Class fee set successfully.")

    def pay_fee(self, student_id, amount):
        self.db.cursor.execute("""
        INSERT INTO payments (student_id, amount_paid, payment_date)
        VALUES (?, ?, ?)
        """, (student_id, amount, date.today().isoformat()))
        self.db.conn.commit()
        print("Fee payment recorded.")

    def view_students(self):
        self.db.cursor.execute("SELECT * FROM students")
        for row in self.db.cursor.fetchall():
            print(row)

    def fee_status(self, student_id):
        self.db.cursor.execute("""
        SELECT s.name, s.class, f.total_fee
        FROM students s
        JOIN fees f ON s.class = f.class
        WHERE s.student_id = ?
        """, (student_id,))
        student = self.db.cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        self.db.cursor.execute("""
        SELECT SUM(amount_paid) FROM payments WHERE student_id = ?
        """, (student_id,))
        paid = self.db.cursor.fetchone()[0] or 0

        due = student[2] - paid

        print("\nStudent Name:", student[0])
        print("Class:", student[1])
        print("Total Fee:", student[2])
        print("Paid Amount:", paid)
        print("Due Amount:", due)

    def payment_history(self, student_id):
        self.db.cursor.execute("""
        SELECT amount_paid, payment_date
        FROM payments WHERE student_id = ?
        """, (student_id,))
        records = self.db.cursor.fetchall()

        print("\nPayment History:")
        for r in records:
            print(f"Amount: {r[0]}, Date: {r[1]}")


# =========================
# Menu System
# =========================
def menu():
    print("""
School Fee Management System
----------------------------
1. Add Student
2. Set Class Fee
3. Pay Fee
4. View Students
5. Fee Status
6. Payment History
7. Exit
""")


def main():
    db = Database()
    system = FeeManagement(db)

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Student Name: ")
            class_name = input("Class: ")
            roll_no = input("Roll No: ")
            system.add_student(name, class_name, roll_no)

        elif choice == "2":
            class_name = input("Class: ")
            fee = float(input("Total Fee: "))
            system.set_class_fee(class_name, fee)

        elif choice == "3":
            student_id = int(input("Student ID: "))
            amount = float(input("Amount Paid: "))
            system.pay_fee(student_id, amount)

        elif choice == "4":
            system.view_students()

        elif choice == "5":
            student_id = int(input("Student ID: "))
            system.fee_status(student_id)

        elif choice == "6":
            student_id = int(input("Student ID: "))
            system.payment_history(student_id)

        elif choice == "7":
            db.close()
            print("System closed.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()