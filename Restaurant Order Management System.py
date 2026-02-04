
# Restaurant Order Management System

import time
from datetime import datetime

# ------------------ Databases ------------------

customers_db = {
    "T1": {"name": "Table 1", "orders": []},
    "T2": {"name": "Table 2", "orders": []},
    "T3": {"name": "Table 3", "orders": []},
    "T4": {"name": "Table 4", "orders": []},
    "T5": {"name": "Table 5", "orders": []}
}

menu_db = {
    "M1": {"name": "Momo", "price": 150},
    "M2": {"name": "Chowmein", "price": 120},
    "M3": {"name": "Pizza", "price": 450},
    "M4": {"name": "Burger", "price": 250},
    "M5": {"name": "Coffee", "price": 100}
}

orders_log = []

# ------------------ Utilities ------------------

def loading():
    print("\nProcessing", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print("\n")

# ------------------ Login ------------------

def table_login():
    print("\n====== Restaurant Order System ======")
    tid = input("Enter Table ID (T1/T2/T3/T4/T5): ")

    if tid in customers_db:
        print(f"Welcome, {customers_db[tid]['name']}")
        loading()
        return tid
    else:
        print("Invalid Table ID!")
        return None

# ------------------ Menu ------------------

def menu():
    print("\n========= MENU =========")
    print("1. View Menu")
    print("2. Place Order")
    print("3. View My Orders")
    print("4. Generate Bill")
    print("5. Exit")

# ------------------ Menu List ------------------

def view_menu():
    print("\n====== Restaurant Menu ======")
    for mid, m in menu_db.items():
        print(f"{mid}. {m['name']} - NPR {m['price']}")

# ------------------ Place Order ------------------

def place_order(tid):
    view_menu()
    mid = input("\nEnter Item ID: ")

    if mid not in menu_db:
        print("Invalid Item ID!")
        return

    qty = int(input("Enter Quantity: "))

    item = menu_db[mid]
    total = qty * item['price']

    order = {
        "item_id": mid,
        "item": item['name'],
        "price": item['price'],
        "qty": qty,
        "total": total,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    customers_db[tid]['orders'].append(order)
    orders_log.append(order)

    loading()
    print("\n✅ Order Placed Successfully!")

# ------------------ View Orders ------------------

def view_orders(tid):
    print("\n====== My Orders ======")
    orders = customers_db[tid]['orders']

    if not orders:
        print("No orders placed yet.")
        return

    for o in orders:
        print(f"{o['item']} x{o['qty']} = NPR {o['total']}")

# ------------------ Generate Bill ------------------

def generate_bill(tid):
    print("\n====== BILL ======")
    orders = customers_db[tid]['orders']

    if not orders:
        print("No orders to bill.")
        return

    subtotal = 0
    for o in orders:
        print(f"{o['item']} x{o['qty']} = NPR {o['total']}")
        subtotal += o['total']

    tax = subtotal * 0.13
    grand_total = subtotal + tax

    print("---------------------------")
    print(f"Subtotal : NPR {subtotal}")
    print(f"Tax (13%): NPR {round(tax,2)}")
    print(f"Total    : NPR {round(grand_total,2)}")

    customers_db[tid]['orders'].clear()

    print("\n✅ Bill Generated Successfully!")

# ------------------ Main System ------------------

def restaurant_system():
    while True:
        tid = table_login()
        if tid:
            while True:
                menu()
                ch = input("\nChoose Option (1-5): ")

                if ch == "1":
                    view_menu()
                elif ch == "2":
                    place_order(tid)
                elif ch == "3":
                    view_orders(tid)
                elif ch == "4":
                    generate_bill(tid)
                elif ch == "5":
                    print("\nThank you for visiting our restaurant!")
                    time.sleep(1)
                    break
                else:
                    print("Invalid Option!")

                input("\nPress Enter to continue...")

# ------------------ Run Program ------------------
restaurant_system()
