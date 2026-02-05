
# File-Based Chat Application

# Chat messages are stored in a file (chat_db.txt)
# Multiple users can chat using shared file storage

import time
from datetime import datetime

CHAT_FILE = "chat_db.txt"

# ------------------ Utilities ------------------

def loading():
    print("\nConnecting", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print("\n")

# ------------------ User Login ------------------

def user_login():
    print("\n====== File-Based Chat System ======")
    username = input("Enter Username: ").strip()

    if username:
        loading()
        print(f"Welcome, {username}!")
        return username
    else:
        print("Invalid username!")
        return None

# ------------------ Menu ------------------

def menu():
    print("\n========= MENU =========")
    print("1. Send Message")
    print("2. View Chat")
    print("3. Clear Chat (Admin Mode)")
    print("4. Exit")

# ------------------ Send Message ------------------

def send_message(user):
    msg = input("\nEnter Message: ")
    if not msg:
        print("Empty message not allowed!")
        return

    record = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {user}: {msg}\n"

    with open(CHAT_FILE, "a", encoding="utf-8") as f:
        f.write(record)

    loading()
    print("\n✅ Message Sent!")

# ------------------ View Chat ------------------

def view_chat():
    print("\n====== Chat History ======")
    try:
        with open(CHAT_FILE, "r", encoding="utf-8") as f:
            data = f.readlines()

        if not data:
            print("No messages yet.")
        else:
            for line in data[-30:]:   # show last 30 messages
                print(line.strip())

    except FileNotFoundError:
        print("No chat file found. Start chatting first!")

# ------------------ Clear Chat ------------------

def clear_chat():
    key = input("\nEnter Admin Key to Clear Chat: ")

    if key == "admin123":
        with open(CHAT_FILE, "w", encoding="utf-8") as f:
            f.write("")
        loading()
        print("\n🗑 Chat Cleared Successfully!")
    else:
        print("Invalid Admin Key!")

# ------------------ Main System ------------------

def chat_system():
    while True:
        user = user_login()
        if user:
            while True:
                menu()
                ch = input("\nChoose Option (1-4): ")

                if ch == "1":
                    send_message(user)
                elif ch == "2":
                    view_chat()
                elif ch == "3":
                    clear_chat()
                elif ch == "4":
                    print("\nExiting Chat System...")
                    time.sleep(1)
                    break
                else:
                    print("Invalid Option!")

                input("\nPress Enter to continue...")

# ------------------ Run Program ------------------
chat_system()
