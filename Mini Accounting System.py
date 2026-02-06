
# Mini Accounting System


import time
from datetime import datetime

# ------------------ Databases ------------------

accounts_db = {
    "A001": {"name": "Cash Account", "balance": 10000},
    "A002": {"name": "Bank Account", "balance": 50000}
}

transactions_db = []

# ------------------ Utilities ------------------

def loading():
    print("\nProcessing", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print("\n")

# ------------------ Menu ------------------

def menu():
    print("\n========= MINI ACCOUNTING SYSTEM =========")
    print("1. View Accounts")
    print("2. Add Income")
    print("3. Add Expense")
    print("4. Transfer Funds")
    print("5. Transaction History")
    print("6. Financial Report")
    print("7. Exit")

# ------------------ View Accounts ------------------

def view_accounts():
    print("\n====== Account Balances ======")
    for aid, acc in accounts_db.items():
        print(f"{aid} | {acc['name']} | Balance: NPR {acc['balance']}")

# ------------------ Add Income ------------------

def add_income():
    view_accounts()
    aid = input("\nEnter Account ID: ")

    if aid not in accounts_db:
        print("Invalid Account ID!")
        return

    try:
        amount = float(input("Enter Income Amount: "))
        note = input("Income Description: ")

        accounts_db[aid]["balance"] += amount

        transaction = {
            "type": "Income",
            "account": accounts_db[aid]["name"],
            "amount": amount,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        transactions_db.append(transaction)
        loading()
        print("\n✅ Income Added Successfully!")
    except:
        print("Invalid Input!")

# ------------------ Add Expense ------------------

def add_expense():
    view_accounts()
    aid = input("\nEnter Account ID: ")

    if aid not in accounts_db:
        print("Invalid Account ID!")
        return

    try:
        amount = float(input("Enter Expense Amount: "))
        note = input("Expense Description: ")

        if amount > accounts_db[aid]["balance"]:
            print("Insufficient Balance!")
            return

        accounts_db[aid]["balance"] -= amount

        transaction = {
            "type": "Expense",
            "account": accounts_db[aid]["name"],
            "amount": amount,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        transactions_db.append(transaction)
        loading()
        print("\n✅ Expense Recorded Successfully!")
    except:
        print("Invalid Input!")

# ------------------ Transfer Funds ------------------

def transfer_funds():
    view_accounts()
    src = input("\nFrom Account ID: ")
    dest = input("To Account ID: ")

    if src not in accounts_db or dest not in accounts_db:
        print("Invalid Account ID!")
        return

    try:
        amount = float(input("Enter Transfer Amount: "))
        note = input("Transfer Note: ")

        if amount > accounts_db[src]["balance"]:
            print("Insufficient Balance!")
            return

        accounts_db[src]["balance"] -= amount
        accounts_db[dest]["balance"] += amount

        transaction = {
            "type": "Transfer",
            "from": accounts_db[src]["name"],
            "to": accounts_db[dest]["name"],
            "amount": amount,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        transactions_db.append(transaction)
        loading()
        print("\n✅ Transfer Successful!")
    except:
        print("Invalid Input!")

# ------------------ Transaction History ------------------

def transaction_history():
    print("\n====== Transaction History ======")

    if not transactions_db:
        print("No transactions recorded.")
        return

    for t in transactions_db:
        if t["type"] == "Transfer":
            print(f"{t['date']} | Transfer | {t['from']} -> {t['to']} | NPR {t['amount']} | {t['note']}")
        else:
            print(f"{t['date']} | {t['type']} | {t['account']} | NPR {t['amount']} | {t['note']}")

# ------------------ Financial Report ------------------

def financial_report():
    print("\n====== Financial Report ======")

    income = 0
    expense = 0

    for t in transactions_db:
        if t["type"] == "Income":
            income += t["amount"]
        elif t["type"] == "Expense":
            expense += t["amount"]

    profit = income - expense

    print(f"Total Income  : NPR {income}")
    print(f"Total Expense : NPR {expense}")
    print(f"Net Balance   : NPR {profit}")

# ------------------ Main System ------------------

def accounting_system():
    while True:
        menu()
        ch = input("\nChoose Option (1-7): ")

        if ch == "1":
            view_accounts()
        elif ch == "2":
            add_income()
        elif ch == "3":
            add_expense()
        elif ch == "4":
            transfer_funds()
        elif ch == "5":
            transaction_history()
        elif ch == "6":
            financial_report()
        elif ch == "7":
            print("\nExiting Mini Accounting System...")
            time.sleep(1)
            break
        else:
            print("Invalid Option!")

        input("\nPress Enter to continue...")

# ------------------ Run Program ------------------
accounting_system()
