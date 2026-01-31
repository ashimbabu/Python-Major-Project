
# Railway Ticket Booking System - Python

import random
import time
from datetime import datetime

# ------------------ Database ------------------

users_db = {
    "ashim": {"password": "1234", "bookings": []},
    "user1": {"password": "1111", "bookings": []}
}

trains_db = {
    "1001": {
        "name": "Koshi Express",
        "from": "Kathmandu",
        "to": "Biratnagar",
        "seats": 50,
        "fare": 1200
    },
    "1002": {
        "name": "Gandaki Express",
        "from": "Kathmandu",
        "to": "Pokhara",
        "seats": 40,
        "fare": 800
    },
    "1003": {
        "name": "Karnali Express",
        "from": "Kathmandu",
        "to": "Surkhet",
        "seats": 30,
        "fare": 1500
    }
}

# ------------------ Utilities ------------------

def loading():
    print("\nProcessing", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print("\n")

def generate_pnr():
    return "PNR" + str(random.randint(100000, 999999))

# ------------------ Login ------------------

def login():
    print("\n====== Railway Reservation System ======")
    username = input("Username: ")
    password = input("Password: ")

    if username in users_db and users_db[username]["password"] == password:
        print("\nLogin Successful!")
        loading()
        return username
    else:
        print("\nInvalid Login!")
        return None

# ------------------ Menu ------------------

def menu():
    print("\n========= MAIN MENU =========")
    print("1. View Trains")
    print("2. Search Train")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. Booking History")
    print("6. Exit")

# ------------------ Train Functions ------------------

def view_trains():
    print("\n========== Available Trains ==========")
    for tid, t in trains_db.items():
        print(f"""
Train No: {tid}
Name   : {t['name']}
Route  : {t['from']} -> {t['to']}
Seats  : {t['seats']}
Fare   : NPR {t['fare']}
----------------------------------
""")

def search_train():
    frm = input("\nFrom: ").title()
    to = input("To: ").title()
    found = False

    print("\nSearch Results:")
    for tid, t in trains_db.items():
        if t["from"] == frm and t["to"] == to:
            found = True
            print(f"{tid} - {t['name']} | Seats: {t['seats']} | Fare: NPR {t['fare']}")
    if not found:
        print("No trains found.")

# ------------------ Booking ------------------

def book_ticket(user):
    view_trains()
    tid = input("\nEnter Train No: ")

    if tid not in trains_db:
        print("Invalid Train Number!")
        return

    train = trains_db[tid]

    if train["seats"] <= 0:
        print("No seats available!")
        return

    name = input("Passenger Name: ")
    age = input("Passenger Age: ")
    seats = int(input("Number of Seats: "))

    if seats > train["seats"]:
        print("Not enough seats available!")
        return

    total_fare = seats * train["fare"]
    pnr = generate_pnr()

    booking = {
        "pnr": pnr,
        "train_no": tid,
        "train_name": train["name"],
        "route": f"{train['from']} - {train['to']}",
        "passenger": name,
        "age": age,
        "seats": seats,
        "fare": total_fare,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    users_db[user]["bookings"].append(booking)
    train["seats"] -= seats

    loading()
    print("\n🎟 Ticket Booked Successfully!")
    print(f"PNR Number : {pnr}")
    print(f"Train      : {train['name']}")
    print(f"Route      : {train['from']} -> {train['to']}")
    print(f"Seats      : {seats}")
    print(f"Total Fare : NPR {total_fare}")

# ------------------ Cancel Ticket ------------------

def cancel_ticket(user):
    pnr = input("\nEnter PNR Number: ")
    bookings = users_db[user]["bookings"]

    for b in bookings:
        if b["pnr"] == pnr:
            trains_db[b["train_no"]]["seats"] += b["seats"]
            bookings.remove(b)
            loading()
            print("Ticket Cancelled Successfully!")
            return

    print("PNR not found!")

# ------------------ Booking History ------------------

def booking_history(user):
    print("\n========= Booking History =========")
    if not users_db[user]["bookings"]:
        print("No bookings found.")
    else:
        for b in users_db[user]["bookings"]:
            print(f"""
PNR   : {b['pnr']}
Train : {b['train_name']}
Route : {b['route']}
Name  : {b['passenger']}
Seats : {b['seats']}
Fare  : NPR {b['fare']}
Date  : {b['date']}
-----------------------------
""")

# ------------------ Main System ------------------

def railway_system():
    while True:
        user = login()
        if user:
            while True:
                menu()
                ch = input("\nChoose Option (1-6): ")

                if ch == "1":
                    view_trains()
                elif ch == "2":
                    search_train()
                elif ch == "3":
                    book_ticket(user)
                elif ch == "4":
                    cancel_ticket(user)
                elif ch == "5":
                    booking_history(user)
                elif ch == "6":
                    print("\nThank you for using Railway Booking System!")
                    time.sleep(1)
                    break
                else:
                    print("Invalid Option!")

                input("\nPress Enter to continue...")

# ------------------ Run ------------------
railway_system()
