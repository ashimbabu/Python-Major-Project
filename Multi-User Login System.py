
# Multi-User Login System

import json
import time
import hashlib
from datetime import datetime

DB_FILE = "users_db.json"

# ------------------ Database ------------------

def load_users():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_users(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ------------------ Security ------------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------ Utilities ------------------

def loading():
    print("\nProcessing", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="")
    print("\n")

# ------------------ Menu ------------------

def main_menu():
    print("\n========= MULTI-USER LOGIN SYSTEM =========")
    print("1. Register")
    print("2. Login")
    print("3. View Users (Admin)")
    print("4. Delete User (Admin)")
    print("5. Exit")

# ------------------ Register ------------------

def register(data):
    print("\n====== User Registration ======")
    username = input("Username: ")

    for u in data:
        if u['username'] == username:
            print("Username already exists!")
            return

    password = input("Password: ")
    role = input("Role (admin/user): ").lower()
    if role not in ["admin", "user"]:
        role = "user"

    user = {
        "username": username,
        "password": hash_password(password),
        "role": role,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(user)
    save_users(data)
    loading()
    print("\n✅ Registration Successful!")

# ------------------ Login ------------------

def login(data):
    print("\n====== User Login ======")
    username = input("Username: ")
    password = input("Password: ")
    hp = hash_password(password)

    for u in data:
        if u['username'] == username and u['password'] == hp:
            loading()
            print(f"\n✅ Login Successful! Welcome {username}")
            return u

    print("Invalid Username or Password!")
    return None

# ------------------ Admin Panel ------------------

def admin_panel(data):
    while True:
        print("\n====== ADMIN PANEL ======")
        print("1. View All Users")
        print("2. Delete User")
        print("3. Logout")

        ch = input("Choose Option: ")

        if ch == "1":
            print("\n--- Registered Users ---")
            for u in data:
                print(f"{u['username']} | {u['role']} | {u['created']}")

        elif ch == "2":
            uname = input("Enter Username to Delete: ")
            for i, u in enumerate(data):
                if u['username'] == uname:
                    data.pop(i)
                    save_users(data)
                    loading()
                    print("User Deleted Successfully!")
                    break
            else:
                print("User not found!")

        elif ch == "3":
            break

        else:
            print("Invalid Option!")

# ------------------ User Panel ------------------

def user_panel(user):
    while True:
        print(f"\n====== USER DASHBOARD ({user['username']}) ======")
        print("1. View Profile")
        print("2. Change Password")
        print("3. Logout")

        ch = input("Choose Option: ")

        if ch == "1":
            print("\n--- Profile ---")
            print(f"Username: {user['username']}")
            print(f"Role    : {user['role']}")
            print(f"Created : {user['created']}")

        elif ch == "2":
            new_pass = input("New Password: ")
            user['password'] = hash_password(new_pass)
            users = load_users()
            for u in users:
                if u['username'] == user['username']:
                    u['password'] = user['password']
            save_users(users)
            loading()
            print("Password Changed Successfully!")

        elif ch == "3":
            break

        else:
            print("Invalid Option!")

# ------------------ Main System ------------------

def system():
    data = load_users()

    # Auto-create super admin if DB empty
    if not data:
        admin = {
            "username": "admin",
            "password": hash_password("admin123"),
            "role": "admin",
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        data.append(admin)
        save_users(data)

    while True:
        main_menu()
        ch = input("\nChoose Option (1-5): ")

        if ch == "1":
            register(data)
        elif ch == "2":
            user = login(data)
            if user:
                if user['role'] == "admin":
                    admin_panel(data)
                else:
                    user_panel(user)
        elif ch == "3":
            print("Admin Login Required")
            user = login(data)
            if user and user['role'] == "admin":
                for u in data:
                    print(f"{u['username']} | {u['role']} | {u['created']}")
        elif ch == "4":
            print("Admin Login Required")
            user = login(data)
            if user and user['role'] == "admin":
                uname = input("Username to delete: ")
                for i, u in enumerate(data):
                    if u['username'] == uname:
                        data.pop(i)
                        save_users(data)
                        print("User Deleted!")
                        break
        elif ch == "5":
            print("\nExiting Multi-User Login System...")
            time.sleep(1)
            break
        else:
            print("Invalid Option!")

# ------------------ Run Program ------------------
system()
