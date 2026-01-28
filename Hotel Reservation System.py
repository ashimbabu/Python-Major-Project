import sqlite3
from datetime import datetime

# ---------------- DATABASE SETUP ----------------
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("hotel.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            room_id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_type TEXT,
            price REAL,
            status TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            phone TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            room_id INTEGER,
            check_in TEXT,
            check_out TEXT,
            total_price REAL,
            FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY(room_id) REFERENCES rooms(room_id)
        )
        """)
        self.conn.commit()

db = Database()

# ---------------- ROOM MANAGEMENT ----------------
class Room:
    @staticmethod
    def add_room(room_type, price):
        db.cursor.execute(
            "INSERT INTO rooms (room_type, price, status) VALUES (?, ?, ?)",
            (room_type, price, "Available")
        )
        db.conn.commit()
        print("✅ Room added successfully!")

    @staticmethod
    def view_rooms():
        db.cursor.execute("SELECT * FROM rooms")
        rooms = db.cursor.fetchall()
        print("\n--- Available Rooms ---")
        for room in rooms:
            print(room)

# ---------------- CUSTOMER MANAGEMENT ----------------
class Customer:
    @staticmethod
    def register(name, email, phone):
        try:
            db.cursor.execute(
                "INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)",
                (name, email, phone)
            )
            db.conn.commit()
            print("✅ Customer registered successfully!")
        except sqlite3.IntegrityError:
            print("❌ Email already exists!")

    @staticmethod
    def get_customer(email):
        db.cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
        return db.cursor.fetchone()

# ---------------- BOOKING MANAGEMENT ----------------
class Booking:
    @staticmethod
    def book_room(customer_id, room_id, check_in, check_out):
        db.cursor.execute("SELECT price, status FROM rooms WHERE room_id = ?", (room_id,))
        room = db.cursor.fetchone()

        if room is None or room[1] != "Available":
            print("❌ Room not available!")
            return

        days = (datetime.strptime(check_out, "%Y-%m-%d") -
                datetime.strptime(check_in, "%Y-%m-%d")).days
        total_price = days * room[0]

        db.cursor.execute("""
        INSERT INTO bookings (customer_id, room_id, check_in, check_out, total_price)
        VALUES (?, ?, ?, ?, ?)
        """, (customer_id, room_id, check_in, check_out, total_price))

        db.cursor.execute("UPDATE rooms SET status = 'Booked' WHERE room_id = ?", (room_id,))
        db.conn.commit()
        print(f"✅ Booking successful! Total Price: NPR {total_price}")

    @staticmethod
    def cancel_booking(booking_id):
        db.cursor.execute("SELECT room_id FROM bookings WHERE booking_id = ?", (booking_id,))
        room = db.cursor.fetchone()

        if room:
            db.cursor.execute("UPDATE rooms SET status = 'Available' WHERE room_id = ?", (room[0],))
            db.cursor.execute("DELETE FROM bookings WHERE booking_id = ?", (booking_id,))
            db.conn.commit()
            print("✅ Booking cancelled successfully!")
        else:
            print("❌ Booking not found!")

    @staticmethod
    def view_bookings():
        db.cursor.execute("""
        SELECT b.booking_id, c.name, r.room_type, b.check_in, b.check_out, b.total_price
        FROM bookings b
        JOIN customers c ON b.customer_id = c.customer_id
        JOIN rooms r ON b.room_id = r.room_id
        """)
        bookings = db.cursor.fetchall()
        print("\n--- Bookings ---")
        for b in bookings:
            print(b)

# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("""
======== HOTEL RESERVATION SYSTEM ========
1. Admin: Add Room
2. View Rooms
3. Customer Registration
4. Book Room
5. View Bookings
6. Cancel Booking
7. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            room_type = input("Room Type (Single/Double/Deluxe): ")
            price = float(input("Price per night: "))
            Room.add_room(room_type, price)

        elif choice == "2":
            Room.view_rooms()

        elif choice == "3":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            Customer.register(name, email, phone)

        elif choice == "4":
            email = input("Customer Email: ")
            customer = Customer.get_customer(email)
            if not customer:
                print("❌ Customer not found!")
                continue

            room_id = int(input("Room ID: "))
            check_in = input("Check-in date (YYYY-MM-DD): ")
            check_out = input("Check-out date (YYYY-MM-DD): ")
            Booking.book_room(customer[0], room_id, check_in, check_out)

        elif choice == "5":
            Booking.view_bookings()

        elif choice == "6":
            booking_id = int(input("Booking ID: "))
            Booking.cancel_booking(booking_id)

        elif choice == "7":
            print("Thank you for using Hotel Reservation System!")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()