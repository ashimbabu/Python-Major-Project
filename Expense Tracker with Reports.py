

# Expense Tracker with Reports


import json
import time
from datetime import datetime

DB_FILE = "expense_db.json"

# ------------------ Database ------------------

def load_data():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ------------------ Utilities ------------------

def loading():
    print("\nProcessing", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="")
    print("\n")

# ------------------ Menu ------------------

def menu():
    print("\n========= EXPENSE TRACKER SYSTEM =========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category-wise Report")
    print("4. Monthly Report")
    print("5. Summary Report")
    print("6. Delete Expense")
    print("7. Exit")

# ------------------ Add Expense ------------------

def add_expense(data):
    try:
        amount = float(input("Enter Amount: "))
        category = input("Enter Category (Food/Travel/Rent/Study/Other): ")
        note = input("Note: ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        record = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": date
        }

        data.append(record)
        save_data(data)
        loading()
        print("\n✅ Expense Added Successfully!")
    except:
        print("Invalid Input!")

# ------------------ View Expenses ------------------

def view_expenses(data):
    print("\n====== All Expenses ======")
    if not data:
        print("No expenses recorded.")
        return

    for i, e in enumerate(data, 1):
        print(f"{i}. {e['date']} | NPR {e['amount']} | {e['category']} | {e['note']}")

# ------------------ Category Report ------------------

def category_report(data):
    print("\n====== Category-wise Report ======")
    report = {}

    for e in data:
        report[e['category']] = report.get(e['category'], 0) + e['amount']

    for cat, amt in report.items():
        print(f"{cat} : NPR {amt}")

# ------------------ Monthly Report ------------------

def monthly_report(data):
    print("\n====== Monthly Report ======")
    report = {}

    for e in data:
        month = e['date'][:7]  # YYYY-MM
        report[month] = report.get(month, 0) + e['amount']

    for m, amt in report.items():
        print(f"{m} : NPR {amt}")

# ------------------ Summary Report ------------------

def summary_report(data):
    print("\n====== Summary Report ======")

    total = sum(e['amount'] for e in data)
    categories = set(e['category'] for e in data)

    print(f"Total Expenses : NPR {total}")
    print(f"Total Entries  : {len(data)}")
    print(f"Categories    : {len(categories)}")

# ------------------ Delete Expense ------------------

def delete_expense(data):
    view_expenses(data)
    if not data:
        return

    try:
        idx = int(input("\nEnter Expense Number to Delete: "))
        if 1 <= idx <= len(data):
            data.pop(idx-1)
            save_data(data)
            loading()
            print("\n✅ Expense Deleted Successfully!")
        else:
            print("Invalid Number!")
    except:
        print("Invalid Input!")

# ------------------ Main System ------------------

def expense_tracker():
    data = load_data()

    while True:
        menu()
        ch = input("\nChoose Option (1-7): ")

        if ch == "1":
            add_expense(data)
        elif ch == "2":
            view_expenses(data)
        elif ch == "3":
            category_report(data)
        elif ch == "4":
            monthly_report(data)
        elif ch == "5":
            summary_report(data)
        elif ch == "6":
            delete_expense(data)
        elif ch == "7":
            print("\nExiting Expense Tracker...")
            time.sleep(1)
            break
        else:
            print("Invalid Option!")

        input("\nPress Enter to continue...")

# ------------------ Run Program ------------------
expense_tracker()
