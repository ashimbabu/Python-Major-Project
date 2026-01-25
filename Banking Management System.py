import json
import os

FILE_NAME = "accounts.json"

# ---------------- File Handling ----------------
def load_accounts():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)

# ---------------- Account Functions ----------------
def create_account():
    accounts = load_accounts()
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account already exists!")
        return

    accounts[acc_no] = {
        "Name": input("Enter Account Holder Name: "),
        "Age": input("Enter Age: "),
        "Account_Type": input("Enter Account Type (Saving/Current): "),
        "Balance": float(input("Enter Initial Deposit: "))
    }

    save_accounts(accounts)
    print("Account created successfully!")

def view_accounts():
    accounts = load_accounts()
    if not accounts:
        print("No accounts found.")
        return

    for acc_no, details in accounts.items():
        print(f"\nAccount Number: {acc_no}")
        for k, v in details.items():
            print(f"{k}: {v}")

def search_account():
    accounts = load_accounts()
    key = input("Enter Account Number or Name: ").lower()

    found = False
    for acc_no, details in accounts.items():
        if key == acc_no.lower() or key in details["Name"].lower():
            print(f"\nAccount Number: {acc_no}")
            for k, v in details.items():
                print(f"{k}: {v}")
            found = True

    if not found:
        print("Account not found!")

def deposit_money():
    accounts = load_accounts()
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no]["Balance"] += amount
        save_accounts(accounts)
        print("Amount deposited successfully!")
    else:
        print("Account not found!")

def withdraw_money():
    accounts = load_accounts()
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= accounts[acc_no]["Balance"]:
            accounts[acc_no]["Balance"] -= amount
            save_accounts(accounts)
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def transfer_money():
    accounts = load_accounts()
    sender = input("Enter Sender Account Number: ")
    receiver = input("Enter Receiver Account Number: ")

    if sender in accounts and receiver in accounts:
        amount = float(input("Enter amount to transfer: "))
        if amount <= accounts[sender]["Balance"]:
            accounts[sender]["Balance"] -= amount
            accounts[receiver]["Balance"] += amount
            save_accounts(accounts)
            print("Transfer successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Invalid account number!")

def delete_account():
    accounts = load_accounts()
    acc_no = input("Enter Account Number to delete: ")

    if acc_no in accounts:
        del accounts[acc_no]
        save_accounts(accounts)
        print("Account deleted successfully!")
    else:
        print("Account not found!")

# ---------------- Main Menu ----------------
def main():
    while True:
        print("\n===== Banking Management System =====")
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Search Account")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Transfer Money")
        print("7. Delete Account")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            search_account()
        elif choice == "4":
            deposit_money()
        elif choice == "5":
            withdraw_money()
        elif choice == "6":
            transfer_money()
        elif choice == "7":
            delete_account()
        elif choice == "8":
            print("Thank you for using Banking Management System.")
            break
        else:
            print("Invalid choice! Try again.")

# ---------------- Run Program ----------------
if __name__ == "__main__":
    main()