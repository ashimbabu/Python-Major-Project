# ==============================
# ATM Machine Full Simulation
# ==============================

import time

# Dummy Database
users_db = {
    "1234567890": {
        "pin": "1234",
        "name": "Ashim Shrestha",
        "balance": 50000,
        "transactions": []
    },
    "9876543210": {
        "pin": "4321",
        "name": "User Two",
        "balance": 30000,
        "transactions": []
    }
}

# ------------------------------
def clear():
    print("\n" * 2)

def loading():
    print("\nProcessing", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print("\n")

# ------------------------------
def login():
    clear()
    print("========== ATM MACHINE ==========")
    card = input("Enter Card Number: ")
    pin = input("Enter PIN: ")

    if card in users_db and users_db[card]["pin"] == pin:
        print("\nLogin Successful!")
        loading()
        return card
    else:
        print("\nInvalid Card Number or PIN!")
        time.sleep(1.5)
        return None

# ------------------------------
def show_menu():
    print("\n========== ATM MENU ==========")
    print("1. Balance Inquiry")
    print("2. Cash Deposit")
    print("3. Cash Withdrawal")
    print("4. Mini Statement")
    print("5. Change PIN")
    print("6. Exit")

# ------------------------------
def balance_inquiry(card):
    balance = users_db[card]["balance"]
    print(f"\nCurrent Balance: NPR {balance}")

# ------------------------------
def deposit(card):
    try:
        amount = float(input("\nEnter Deposit Amount: "))
        if amount <= 0:
            print("Invalid amount!")
            return
        users_db[card]["balance"] += amount
        users_db[card]["transactions"].append(f"Deposited: NPR {amount}")
        loading()
        print("Deposit Successful!")
    except:
        print("Invalid input!")

# ------------------------------
def withdraw(card):
    try:
        amount = float(input("\nEnter Withdrawal Amount: "))
        if amount <= 0:
            print("Invalid amount!")
            return

        if amount > users_db[card]["balance"]:
            print("Insufficient Balance!")
            return

        users_db[card]["balance"] -= amount
        users_db[card]["transactions"].append(f"Withdrawn: NPR {amount}")
        loading()
        print("Please collect your cash.")
    except:
        print("Invalid input!")

# ------------------------------
def mini_statement(card):
    print("\n====== Mini Statement ======")
    if not users_db[card]["transactions"]:
        print("No transactions yet.")
    else:
        for t in users_db[card]["transactions"][-5:]:
            print("-", t)

# ------------------------------
def change_pin(card):
    old_pin = input("\nEnter Old PIN: ")
    if old_pin == users_db[card]["pin"]:
        new_pin = input("Enter New PIN: ")
        confirm_pin = input("Confirm New PIN: ")
        if new_pin == confirm_pin:
            users_db[card]["pin"] = new_pin
            loading()
            print("PIN Changed Successfully!")
        else:
            print("PIN Mismatch!")
    else:
        print("Wrong Old PIN!")

# ------------------------------
def atm_system():
    while True:
        card = login()
        if card:
            while True:
                clear()
                print(f"Welcome, {users_db[card]['name']}")
                show_menu()
                choice = input("\nSelect Option (1-6): ")

                if choice == "1":
                    balance_inquiry(card)
                elif choice == "2":
                    deposit(card)
                elif choice == "3":
                    withdraw(card)
                elif choice == "4":
                    mini_statement(card)
                elif choice == "5":
                    change_pin(card)
                elif choice == "6":
                    print("\nThank you for using ATM. Goodbye!")
                    time.sleep(1.5)
                    break
                else:
                    print("\nInvalid Option!")

                input("\nPress Enter to continue...")

# ------------------------------
# Run Program
atm_system()